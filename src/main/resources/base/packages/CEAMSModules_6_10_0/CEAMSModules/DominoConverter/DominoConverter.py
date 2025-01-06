"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    DominoConverter
    Class to convert DOMINO accessory files (ASCII) in one Snooz accessory tsv file.

    Format supported : "ASCII Export-ANALYSIS DATA- WITHOUT SLEEP PROFILE" 

        -------------------------------------------------------------------
        2 columns format :
            i.e. "Sleep Profile - XXXXXXXX.txt"

            Signal ID: SchlafProfil\profil
            Start Time: 17/11/2010 23:57:00
            Unit: 
            Signal Type: Discret
            Events list: N4,N3,N2,N1,REM,Wake,Movement
            Rate: 30 s

            23:57:00,000; Wake
            23:57:30,000; Wake
            23:58:00,000; Wake
            23:58:30,000; Wake
                ...
        -------------------------------------------------------------------
        3 columns format :
            i.e. "Spindle K - XXXXXXXX.txt"

            Signal ID: Spindel\spindel
            Start Time: 17/11/2010 23:57:00
            Unit: ms
            Signal Type: Impuls

            23:57:39,992-23:57:40,992; 1000;Spindle
            23:57:45,242-23:57:45,992; 750;Spindle
            23:57:47,492-23:57:47,992; 500;Spindle            
                ...

        Files with other formats are skipped.

"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from CEAMSModules.PSGReader import commons
from CEAMSModules.EventReader.manage_events import create_event_dataframe

import datetime
import numpy as np
from os import listdir
from os.path import isfile, join, splitext
import pandas as pd
import time

DEBUG = False

class DominoConverter(SciNode):
    """
    To convert DOMINO accessory files (ASCII) in one Snooz accessory tsv file.
    Inputs:
        "folders": String of list of string
            List of folders to run through to convert all the supported ASCII files included.
        "log_filename" : String
            Path and filename to save the log warning message of the conversion. 
    Outputs:
        None, a file with the exact same name as the edf, but with the extension "tsv" is saved for each folder. 
    """
    def __init__(self, **kwargs):
        """ Initialize module DominoConverter """
        super().__init__(**kwargs)
        if DEBUG: print('DominoConverter.__init__')

        # Input plugs
        InputPlug('folders',self)
        InputPlug('log_filename',self)
        # Output plugs
        # nothing

        # Variables
        self.psg_ext = '.edf'
        self.snooz_annot_ext = '.tsv'
        self.somno_annot_ext = '.txt'
        self.separator = ';'

        self.warning_col = ['recording','filename','warning']
        self.warning_message = pd.DataFrame(columns=self.warning_col)
        
        # Dictionary of sleep stages label to use in Snnoz
        self._snooz_stage_label = commons.sleep_stages_name
        self._somno_stage_label = \
            {'Wake':self._snooz_stage_label['W'],\
            'N1': self._snooz_stage_label['N1'],\
            'N2': self._snooz_stage_label['N2'],\
            'N3': self._snooz_stage_label['N3'],\
            'N4': self._snooz_stage_label['N4'],\
            'REM' : self._snooz_stage_label['R'],\
            'Movement' : self._snooz_stage_label['movement']}

        # A master module allows the process to be reexcuted multiple time.
        self._is_master = False 
    
    def compute(self, folders, log_filename):
        """
        To convert DOMINO accessory files (ASCII) in one Snooz accessory tsv file.
        Inputs:
            "folders": String of list of string
                List of folders to run through to convert all the supported ASCII files included.
            "log_filename" : String
                Path and filename to save the log warning message of the conversion. 
        Outputs:
            None, a file with the exact same name as the edf, but with the extension "tsv" is saved for each folder. 
        """

        if len(folders)>0:
            folders = eval(folders)

        if log_filename =='':
            raise NodeInputException(self.identifier, "log_filename", \
                f"DominoConverter input log_filename has to be defined")

        # Run through folders to convert all the supported ASCII files included.
        for folder in folders:
            snooz_annot_lst = []

            # Extract accessory filenames and edf filename
            annot_files = [f for f in listdir(folder) if isfile(join(folder, f)) and splitext(f)[1].lower()==self.somno_annot_ext]
            edf_files = [f for f in listdir(folder) if isfile(join(folder, f)) and splitext(f)[1].lower()==self.psg_ext]

            # Quality control on the edf file
            if len(edf_files)>1:
                current_warning = pd.DataFrame(data=[[folder, "all", f"has more than one edf files, only {edf_files[0]} is considered"]], columns=self.warning_col)
                self.warning_message = pd.concat([self.warning_message,current_warning],axis=0)                
            elif len(edf_files)==0:
                current_warning = pd.DataFrame(data=[[folder, "all", f"does not include any edf file, folder is skipped"]], columns=self.warning_col)
                self.warning_message = pd.concat([self.warning_message,current_warning],axis=0)    

            if len(edf_files)>0:
                edf_files = edf_files[0]
                edf_filename, edf_ext = splitext(edf_files)

                # Run through the current folder to convert all the supported ASCII files included.
                for annot_file in annot_files:
                    file_to_read = folder+'/'+annot_file
                    # ---------------------------------------------
                    # Preprocess the file to evaluate the format
                    # ---------------------------------------------
                    with open(file_to_read) as f:
                        contents = f.readlines()
                    # Look for the empty line
                    event_group = None
                    start_time = None
                    unit = None
                    fix_duration = None
                    n_rows_hdr = None
                    for i, line in enumerate(contents):
                        if "Signal ID:" in line:
                            event_group = line.split('\\')[-1].replace('\n','')
                        elif "Start Time:" in line :
                            start_time = line.split()[-1].replace('\n','')
                        elif "Unit:" in line:
                            annot_unit = line.split()[-1].replace('\n','')
                            if not annot_unit=='':
                                unit = annot_unit
                        elif "Rate" in line:
                            fix_duration = line.split()[1]
                            unit_duration = line.split()[-1].replace('\n','')
                            if unit_duration=='ms':
                                fix_duration = float(fix_duration)/1000
                            elif unit_duration=='s':
                                fix_duration = float(fix_duration)
                            else:
                                current_warning = pd.DataFrame(data=[[edf_filename, annot_file, \
                                    "Unexpected unit duration ({unit_duration})"]], columns=self.warning_col)
                                self.warning_message = pd.concat([self.warning_message,current_warning],axis=0)                                
                        elif line=='\n':
                            n_rows_hdr = i+1
                            break
                    if n_rows_hdr is not None:
                        if len(contents)>n_rows_hdr:
                            n_columns = len(contents[n_rows_hdr].split(';'))
                        else:
                            n_columns = 0
                    else:
                        current_warning = pd.DataFrame(data=[[edf_filename, annot_file, "Header was not found"]], columns=self.warning_col)
                        self.warning_message = pd.concat([self.warning_message,current_warning],axis=0)
                    # Empty
                    if n_columns==0:
                        current_warning = pd.DataFrame(data=[[edf_filename, annot_file, "empty"]], columns=self.warning_col)
                        self.warning_message = pd.concat([self.warning_message,current_warning],axis=0)
                        continue
                    # Sleep staging format
                    if n_columns==2:
                        if event_group is None : 
                            current_warning = pd.DataFrame(data=[[edf_filename, annot_file, "2 columns format but no Signal ID"]], columns=self.warning_col)
                            self.warning_message = pd.concat([self.warning_message,current_warning],axis=0)
                            continue
                        if start_time is None : 
                            current_warning = pd.DataFrame(data=[[edf_filename, annot_file, "2 columns format but no start_time ID"]], columns=self.warning_col)
                            self.warning_message = pd.concat([self.warning_message,current_warning],axis=0)         
                            continue               
                        if fix_duration is None :
                            current_warning = pd.DataFrame(data=[[edf_filename, annot_file, "2 columns format but no Rate"]], columns=self.warning_col)
                            self.warning_message = pd.concat([self.warning_message,current_warning],axis=0)     
                            continue
                        # -------------------------------------------------------------
                        # Read the whole file and convert data into a pandas dataframe
                        # -------------------------------------------------------------
                        somno_df = pd.read_csv(file_to_read, sep=self.separator, header=None, skiprows=n_rows_hdr-1, \
                            encoding='utf_8', names=['clock_time', 'name']) 
                    # Expert Annotations
                    elif n_columns==3:
                        if event_group is None : 
                            current_warning = pd.DataFrame(data=[[edf_filename, annot_file, "3 columns format but no Signal ID"]], columns=self.warning_col)
                            self.warning_message = pd.concat([self.warning_message,current_warning],axis=0)
                            continue
                        if start_time is None : 
                            current_warning = pd.DataFrame(data=[[edf_filename, annot_file, "3 columns format but no start_time ID"]], columns=self.warning_col)
                            self.warning_message = pd.concat([self.warning_message,current_warning],axis=0)   
                            continue      
                        if unit is None :
                            current_warning = pd.DataFrame(data=[[edf_filename, annot_file, "3 columns format but no unit"]], columns=self.warning_col)
                            self.warning_message = pd.concat([self.warning_message,current_warning],axis=0)    
                            continue  
                        # -------------------------------------------------------------
                        # Read the whole file and convert data into a pandas dataframe
                        # -------------------------------------------------------------
                        somno_df = pd.read_csv(file_to_read, sep=self.separator, header=None, skiprows=n_rows_hdr-1, \
                            encoding='utf_8', names=['clock_time', 'duration_sec','name']) 
                    else:
                        current_warning = pd.DataFrame(data=[[edf_filename, annot_file, "Unexpected number of columns ({n_columns})"]], columns=self.warning_col)
                        self.warning_message = pd.concat([self.warning_message,current_warning],axis=0)     
                        continue                        

                    # ---------------------------------------------------------------------------------------    
                    # Convert into Snooz DataFrame Columns: [group, name, start_sec, duration_sec, channels]    
                    # ---------------------------------------------------------------------------------------
                    # Special case for sleep profil
                    if event_group== "profil":
                        event_group = "stage"
                        # Convert sleep stage into number
                        somno_df['name'] = somno_df['name'].str.strip()
                        somno_df['name'].replace(to_replace=self._somno_stage_label, inplace=True)
                    # Start time conversion
                    edf_time = time.strptime(start_time,'%H:%M:%S') # EDF start '17/11/2010' '23:57:00'
                    for index, row in somno_df.iterrows():
                        # Compute the elapsed time in seconde since the beginning of the recording
                        time_start_stop = row['clock_time'].split('-')      # ['23:57:23,145', '23:57:23,734']
                        time_start = time_start_stop[0].replace(',','.')    # '23:57:23,145'
                        start_s_float = time_start.split(':')[-1]           # 23,145
                        annot_start_time = time.strptime(time_start,'%H:%M:%S.%f') # time object
                        # Compute the elapsed time but force the float decimal second
                        onset_elapsed_sec = datetime.timedelta(days=0,hours=annot_start_time.tm_hour-edf_time.tm_hour,\
                            minutes=annot_start_time.tm_min-edf_time.tm_min,seconds=float(start_s_float)).total_seconds()
                        if onset_elapsed_sec<0:
                            onset_elapsed_sec = datetime.timedelta(days=1,hours=annot_start_time.tm_hour-edf_time.tm_hour,\
                                minutes=annot_start_time.tm_min-edf_time.tm_min,seconds=float(start_s_float)).total_seconds()                            
                        # Compute the annotation duration
                        if len(time_start_stop)==2:
                            time_stop = time_start_stop[1].replace(',','.') # '23:57:23,734'
                            stop_s_float = time_stop.split(':')[-1]         # 23,734
                            annot_stop_time = time.strptime(time_stop,'%H:%M:%S.%f') # time object
                            cur_duration_sec = datetime.timedelta(hours=annot_stop_time.tm_hour-annot_start_time.tm_hour,\
                                minutes=annot_stop_time.tm_min-annot_start_time.tm_min,seconds=float(stop_s_float)-float(start_s_float)).total_seconds()
                        else:
                            cur_duration_sec=fix_duration
                        # Create the snooz annotation ['group','name','start_sec','duration_sec','channels']
                        snooz_annot_lst.append([event_group, row['name'], onset_elapsed_sec, cur_duration_sec, '[]'])          
                    # Mark sucess to keep trask of succesful conversion
                    current_warning = pd.DataFrame(data=[[edf_filename, annot_file, "Success"]], columns=self.warning_col)
                    self.warning_message = pd.concat([self.warning_message,current_warning],axis=0)  
            # ---------------------------------------------------------------------------------------    
            # Write the Snooz event into the accessory file: [group, name, start_sec, duration_sec, channels]    
            # ---------------------------------------------------------------------------------------
            # Create the snooz annotation dataframe
            snooz_df = pd.DataFrame(data=snooz_annot_lst, columns=['group','name','start_sec','duration_sec','channels'])
            # Reset index
            snooz_df.reset_index(inplace=True, drop=True)
            # Sort events based on the start_sec
            snooz_df.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')           
            try:     
                # Write the snooz accessory file
                snooz_df.to_csv(folder+'/'+edf_filename+self.snooz_annot_ext, sep='\t', index=False)      
                # Log message for the Logs tab
                self._log_manager.log(self.identifier, f'{folder}/{edf_filename}{self.snooz_annot_ext} is written')
            except : 
                error_message = f"ERROR : Snooz can not write in the file {folder+'/'+edf_filename+self.snooz_annot_ext}."+\
                    f"Check if the dive is accessible and the file is not already open."
                raise NodeRuntimeException(self.identifier, "DominoConverter", error_message)
    
        try:
            # Write the log file if there are any warnings
            self.warning_message.to_csv(log_filename, sep='\t')
            # Log message for the Logs tab
            self._log_manager.log(self.identifier, f'{log_filename} is written')
        except : 
            error_message = f"ERROR : Snooz can not write in the file {log_filename}."+\
                    f"  Check if the drive is accessible and ensure the file is not already open."
            raise NodeRuntimeException(self.identifier, "DominoConverter", error_message)

        # Write to the cache to use the data in the resultTab
        cache = {}
        cache['events'] = snooz_df
        self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
        }