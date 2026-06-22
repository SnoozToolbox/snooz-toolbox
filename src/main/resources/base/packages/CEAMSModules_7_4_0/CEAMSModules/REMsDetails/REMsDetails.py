"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
"""
    REMsDetails
    To average REMs events characteristics such as duration, amplitude and density per stage and sleep cycle.
"""
import numpy as np
import os
import pandas as pd

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

from CEAMSModules.PSGReader import commons
from CEAMSModules.PSGReader.SignalModel import SignalModel
from CEAMSModules.SleepReport import SleepReport
from CEAMSModules.REMsDetails.REMsDetailsDoc import write_doc_file
from CEAMSModules.REMsDetails.REMsDetailsDoc import _get_doc
from CEAMSModules.SpindlesDetails.SpindlesDetails import SpindlesDetails as EventsDetails

DEBUG = False

class REMsDetails(SciNode):
    """
    To average REMs events characteristics such as duration, amplitude and density per stage and sleep cycle.

    Inputs:
        "recording_path" : string
            The recording path.
        "subject_info": dict
            filename : Recording filename without path and extension.
            id1 : Identification 1
            id2 : Identification 2
            first_name : first name of the subject recorded
            last_name : last name of the subject recorded
            sex :
            ...
        "signals": a list of SignalModel
            Each item of the list is a SignalModel object as described below:
                signal.samples : The actual signal data as numpy list
                signal.sample_rate : the sampling rate of the signal
                signal.channel : current channel label
                signal.start_time : The start time of the signal in sec
                signal.end_time : The end time of the signal in sec
                (for more info : look into common/SignalModel)
        "rems_events_details": Pandas DataFrame
            REMs events defined as (columns=['group', 'name', 'start_sec','duration_sec','channels'])
        "artifact_events": Pandas DataFrame
            Artifact events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
            Artifacts are forced to zeros for the detection (with a tukey window)
        "sleep_cycle_param": Dict
            Options used to define the cycles
        "stages_cycles": Pandas DataFrame
            Events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
            The sleep stage group has to be commons.sleep_stage_group "stage" and 
            the sleep cycle group has to be commons.sleep_cycle_group "cycle".
        "rems_det_param": Dict
            rems_event_name : String label of the event name
            stage_sel : Sleep stages selection to detect REMs in.
        "report_constants": dict
            Constants used in the report (N_HOURS, N_CYCLES)   
        "cohort_filename": string
            Path and filename to save the REMs characteristics for the cohort. 
        "export_rems": bool or string
            True : generate a file per subject of the characteristics of each REM event.
    
    Outputs:
        None
        
    """
    def __init__(self, **kwargs):
        """ Initialize module REMsDetails """
        super().__init__(**kwargs)
        if DEBUG: print('REMsDetails.__init__')

        # Input plugs
        InputPlug('recording_path',self)
        InputPlug('subject_info',self)
        InputPlug('signals',self)
        InputPlug('rems_events_details',self)
        InputPlug('artifact_events',self)
        InputPlug('sleep_cycle_param',self)
        InputPlug('stages_cycles',self)
        InputPlug('rems_det_param',self)
        InputPlug('report_constants',self)
        InputPlug('cohort_filename',self)
        InputPlug('export_rems',self)
        
        # Init module variables
        # REMs only occur in REM sleep stage (R)
        self.stage_stats_labels = ['R']

        # A master module allows the process to be reexcuted multiple time.
        self._is_master = False 

        self.rems_columns = ['group','name','cycle','Stage','start_sec','duration_sec','amplitude_uV','channels']
        self.rems_characteristics = ['duration_sec','amplitude_uV']
    

    def compute(self, recording_path, subject_info, signals, rems_events_details, artifact_events, \
        sleep_cycle_param, stages_cycles, rems_det_param, report_constants, cohort_filename, export_rems):
        """
        To average REMs events characteristics such as duration, amplitude and density per stage and sleep cycle.

        Inputs:
            "recording_path" : string
                The recording path.
            "subject_info": dict
                filename : Recording filename without path and extension.
                id1 : Identification 1
                id2 : Identification 2
                first_name : first name of the subject recorded
                last_name : last name of the subject recorded
                sex :
                ...
            "signals": a list of SignalModel
                Each item of the list is a SignalModel object as described below:
                    signal.samples : The actual signal data as numpy list
                    signal.sample_rate : the sampling rate of the signal
                    signal.channel : current channel label
                    signal.start_time : The start time of the signal in sec
                    signal.end_time : The end time of the signal in sec
                    (for more info : look into common/SignalModel)
            "rems_events_details": Pandas DataFrame
                REMs events defined as (columns=['group', 'name', 'start_sec','duration_sec','channels'])
            "artifact_events": Pandas DataFrame
                Artifact events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
                Artifacts are forced to zeros for the detection (with a tukey window)
            "sleep_cycle_param": Dict
                Options used to define the cycles
            "stages_cycles": Pandas DataFrame
                REMs events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
                The sleep stage group has to be commons.sleep_stage_group (stage) and 
                the sleep cycle group has to be commons.sleep_cycle_group (cycle)
            "rems_det_param": Dict
                rems_event_name : String label of the event name
                stage_sel : Sleep stages selection to detect REMs in.
            "report_constants": dict
                Constants used in the report (N_HOURS, N_CYCLES)   
            "cohort_filename": string
                Path and filename to save the REMs characteristics for the cohort. 
            "export_rems": bool or string
                True : generate a file per subject of the characteristics of each REM event.
        """
        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if isinstance(export_rems, str):
            export_rems = eval(export_rems)
        if not isinstance(export_rems, bool):
            raise NodeInputException(self.identifier, "export_rems", \
                f"REMsDetails the type of the input is {type(export_rems)} and bool is expected.")            
        if recording_path=='':
            raise NodeInputException(self.identifier, "recording_path", \
                f"REMsDetails this input is empty, it needs to identify the recording to analyze.")
        if subject_info=='':
            raise NodeInputException(self.identifier, "subject_info", \
                f"REMsDetails this input is empty, it needs to identify the subject recorded.")
        if cohort_filename=='' and not export_rems:
            raise NodeInputException(self.identifier, "cohort_filename", \
                f"REMsDetails has nothing to generate, 'cohort_filename' is empty and 'export_rems' is False")    
        if isinstance(signals, str) and signals=='':
            raise NodeInputException(self.identifier, "signals", \
                f"REMsDetails this input is empty, no signals no details.")              
        if isinstance(rems_events_details, str) and rems_events_details=='':
            raise NodeInputException(self.identifier, "rems_events_details", \
                f"REMsDetails this input is empty, no rems_events_details no details.")     
        if isinstance(stages_cycles, str) and stages_cycles=='':
            raise NodeInputException(self.identifier, "stages_cycles", \
                f"REMsDetails this input is empty")    
        if isinstance(sleep_cycle_param, str) and sleep_cycle_param=='':
            raise NodeInputException(self.identifier, "sleep_cycle_param", \
                f"REMsDetails this input is empty")  
        if isinstance(rems_det_param, str) and rems_det_param=='':
            raise NodeInputException(self.identifier, "rems_det_param", \
                f"REMsDetails this input is empty")  

        if len(signals)==0:
            raise NodeRuntimeException(self.identifier, "signals", \
                f"REMsDetails this input is empty, no signals no details.")       

        if isinstance(report_constants,str) and report_constants == '':
            raise NodeInputException(self.identifier, "report_constants", \
                "REMsDetails report_constants parameter must be set.")
        elif isinstance(report_constants,str):
            report_constants = eval(report_constants)
        if isinstance(report_constants,dict) == False:
            raise NodeInputException(self.identifier, "report_constants",\
                "REMsDetails report_constants expected type is dict and received type is " + str(type(report_constants)))   
        self.N_CYCLES = int(float(report_constants['N_CYCLES']))
        self.N_HOURS = int(float(report_constants['N_HOURS']))

        # To convert string to dict
        if isinstance(sleep_cycle_param, str):
            sleep_cycle_param = eval(sleep_cycle_param)
        if isinstance(rems_det_param, str):
            rems_det_param = eval(rems_det_param)

        # Extract subject info
        subject_info_params = {"filename": subject_info['filename']}
        if (subject_info['id1'] is not None) and len(subject_info['id1'].strip())>0:
            subject_info_params['id1'] = subject_info['id1']
        elif (subject_info['id2'] is not None) and len(subject_info['id2'].strip())>0:
            subject_info_params['id1'] = subject_info['id2']
        else:
            subject_info_params['id1'] = subject_info['id1']
        #-----------------------------------------------------------------------------------
        # Define the rems parameters
        #-----------------------------------------------------------------------------------
        rems_det_param_dict = rems_det_param

        #-----------------------------------------------------------------------------------
        # Sleep stages and cyles extraction
        #-----------------------------------------------------------------------------------        
        # Extract sleep cycle parameters
        cycle_info_param = SleepReport.get_sleep_cycle_parameters(self, sleep_cycle_param)    
        sleep_cycles_df = stages_cycles[stages_cycles['group']==commons.sleep_cycle_group].copy()
        sleep_cycles_df.reset_index(inplace=True, drop=True)
        sleep_cycle_count = {}
        sleep_cycle_count['cyc_count']=len(sleep_cycles_df) # 'Number of sleep cycles.',

        # Extract sleep stage info
        sleep_stage_df = stages_cycles[stages_cycles['group']==commons.sleep_stages_group].copy()
        sleep_stage_df.reset_index(inplace=True, drop=True)      
        # Keep stage from the first awake or sleep until the last awake or sleep
        sleep_stage_df['name'] = sleep_stage_df['name'].apply(int)
        index_valid = sleep_stage_df[sleep_stage_df['name']<8].index
        stage_rec_df = sleep_stage_df.loc[index_valid[0]:index_valid[-1]]
        stage_rec_df.reset_index(inplace=True, drop=True)
        recording_lights_off = stage_rec_df['start_sec'].values[0]
        recording_lights_on = stage_rec_df['start_sec'].values[-1]+stage_rec_df['duration_sec'].values[-1]

        # Edit the cycle number 
        cycle_cnt = 1
        for index, row in sleep_cycles_df.iterrows():
            sleep_cycles_df.loc[index,'name']=cycle_cnt
            cycle_cnt = cycle_cnt+1

        # Exclude sleep stage before Sleep Onset
        # Exclude sleep stage after the end of the last cycle
        stage_in_cycle_df = EventsDetails.exlude_stages_before_SO_after_awake(EventsDetails, sleep_cycles_df, sleep_stage_df)

        # Cycle events
        cycle_starts = sleep_cycles_df['start_sec'].values
        cycle_durations = sleep_cycles_df['duration_sec'].values

        # Compute duration (min)
        sleep_onset_sec = cycle_starts[0]
        end_sleep_sec = cycle_starts[-1]+cycle_durations[-1]
        
        # 'Total period for detection - Duration (min) of the sleep period.'
        sleep_cycle_count['sleep_period_min'] = (end_sleep_sec - sleep_onset_sec)/60
        sleep_cycle_count['recording_min'] = (recording_lights_on - recording_lights_off)/60

        if export_rems: 
            # Extract sleep stages selected by the user from stage_in_cycle_df
            # Create a list from string separated by comma
            sleep_stage_sel_list = rems_det_param_dict['stage_sel'].split(',')
            # Convert the list to integer
            sleep_stage_sel_list = [int(i) for i in sleep_stage_sel_list]
            stage_detection_df = stage_in_cycle_df[stage_in_cycle_df['name'].isin(sleep_stage_sel_list)]  
            # In a folder at the cohort level
            if len(cohort_filename)>0:
                # Extract folder of the file
                folder_cohort = os.path.dirname(cohort_filename)
                # Make directory specific for rems characteristics
                folder_rems_stage = os.path.join(folder_cohort, 'rems_sleep_stages')
                if not os.path.isdir(folder_rems_stage):
                    os.makedirs(folder_rems_stage)
                rems_stage_filename = os.path.join(folder_rems_stage,subject_info['filename'])
                rems_stage_filename = rems_stage_filename+'_'+rems_det_param_dict["rems_event_name"]+'_'+'stages'+'.tsv'
                # Write the stage_detection_df dataframe into the rems_stage_filename file
                stage_detection_df.to_csv(rems_stage_filename, sep='\t', index=False, header=True)

        # For each REMs events add its sleep stage and cycle
        # Need to have "start_sec" and "duration_sec" to use add_stage_cycle_to_spindle_df
        rems_events_details = EventsDetails.add_stage_cycle_to_spindle_df(EventsDetails, rems_events_details, stage_in_cycle_df, sleep_cycles_df)

        # Add amplitude to REMs events if not present
        rems_events_details = self.add_amplitude_to_rems(rems_events_details, signals)

        #-----------------------------------------------------------------------------------
        # Compute and organize characteristics
        #----------------------------------------------------------------------------------_
        
        channels_list = np.unique(SignalModel.get_attribute(signals, 'channel', 'channel'))
        CombinedChannels = ', '.join(channels_list)
        # Define the dataframe to save
        cohort_characteristics_df = []
        rems_characteristics_df = pd.DataFrame()
        # Define the channel info
        fs_chan = SignalModel.get_attribute(signals, 'sample_rate', 'channel', channels_list[0])[0][0] 
        channel_info_param = {}
        channel_info_param['chan_label']=CombinedChannels
        channel_info_param['chan_fs']=fs_chan
        # Organize data for the output (GENERAL)
        cur_chan_general_dict = subject_info_params | cycle_info_param | rems_det_param_dict | channel_info_param | sleep_cycle_count     

        # Create empty artifact DataFrame for functions that require it
        artifact_cur_chan_df = pd.DataFrame(columns=['group','name','start_sec','duration_sec','channels'])    

        # Select rems events for the current channel
        rems_cur_chan_df = rems_events_details[rems_events_details['channels']==CombinedChannels].copy() # dataFrame
        rems_cur_chan_df.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')  
        rems_cur_chan_df.reset_index(inplace=True, drop=True)

        # Manage REMs event, reset the index
        rems_cur_chan_df = rems_cur_chan_df.reset_index(drop=True)
        # Order columns as expected in the doc
        if 'amplitude_uV' not in rems_cur_chan_df.columns:
            rems_cur_chan_df['amplitude_uV'] = np.nan
        rems_cur_chan_sort = rems_cur_chan_df[self.rems_columns]

        # ---------------------------------------------------------------------------------------------------------
        # Compute the stats for total
        # ---------------------------------------------------------------------------------------------------------
        label_stats = 'total'
        tot_stats = self.compute_tot_stats_per_stage(rems_cur_chan_sort, artifact_cur_chan_df, stage_in_cycle_df, \
            commons.sleep_stages_name, rems_det_param_dict['stage_sel'], label_stats, self.stage_stats_labels)

        # ---------------------------------------------------------------------------------------------------------
        # Compute the stats for cycle
        # ---------------------------------------------------------------------------------------------------------
        label_stats = 'cyc'
        cyc_stats = self.compute_cyc_stats_per_stage(rems_cur_chan_sort, artifact_cur_chan_df, stage_in_cycle_df, sleep_cycles_df,\
            commons.sleep_stages_name, rems_det_param_dict['stage_sel'], label_stats, self.stage_stats_labels)

        # ---------------------------------------------------------------------------------------------------------
        # Compute the stats for clock_h
        # ---------------------------------------------------------------------------------------------------------
        label_stats = 'clock_h'
        clock_h_stats = self.compute_clock_h_stats_per_stage(rems_cur_chan_sort, artifact_cur_chan_df, stage_in_cycle_df,\
            commons.sleep_stages_name, rems_det_param_dict['stage_sel'], label_stats, self.stage_stats_labels)

        # ---------------------------------------------------------------------------------------------------------
        # Compute the stats for stage_h
        # ---------------------------------------------------------------------------------------------------------
        label_stats = 'stage_h'
        stage_h_stats = self.compute_stage_h_stats_per_stage(rems_cur_chan_sort, artifact_cur_chan_df, stage_in_cycle_df,\
            commons.sleep_stages_name, rems_det_param_dict['stage_sel'], label_stats, self.stage_stats_labels)

        # Organize data to write the cohort rems report
        # Construction of the pandas dataframe that will be used to create the TSV file
        # There is a new line for each channel and mini band
        cur_chan_dict = cur_chan_general_dict | tot_stats | cyc_stats | clock_h_stats | stage_h_stats
        cur_chan_df = pd.DataFrame.from_records([cur_chan_dict])

        # --------------------------------------------------------------------------
        # Organize data to Write the file
        # --------------------------------------------------------------------------
        if len(cohort_characteristics_df):
            cohort_characteristics_df = pd.concat([cohort_characteristics_df, cur_chan_df])
        else:
            cohort_characteristics_df = cur_chan_df
        # Organize data to write the rems characteristics
        if export_rems:
            if len(rems_characteristics_df)==0:
                rems_characteristics_df = rems_cur_chan_sort
            else:
                rems_characteristics_df = pd.concat([rems_characteristics_df, rems_cur_chan_sort],ignore_index=True)

        #----------------------------------------------------------------------------
        # REMs characteristics TSV file
        #----------------------------------------------------------------------------
        if export_rems:
            if len(rems_characteristics_df)>0:
                # We need to link the rems characteristics file with the PSG recording
                subject_id = subject_info['filename'] 
                # In a folder at the cohort level
                if len(cohort_filename)>0:
                    # Extract folder of the file
                    folder_cohort = os.path.dirname(cohort_filename)
                    # Make directory specific for rems characteristics
                    folder_rems_char = os.path.join(folder_cohort, 'rems_characteristics')
                    if not os.path.isdir(folder_rems_char):
                        os.makedirs(folder_rems_char)
                    rems_char_filename = os.path.join(folder_rems_char,subject_id)
                    rems_char_filename = rems_char_filename+'_'+rems_det_param_dict["rems_event_name"]+'.tsv'
                # In the subject folder
                else:
                    # Extract folder of the file
                    folder_subject = os.path.dirname(recording_path)
                    rems_char_filename = os.path.join(folder_subject,subject_id)
                    rems_char_filename = rems_char_filename+'_'+rems_det_param_dict["rems_event_name"]+'.tsv'
                # Sort from start_time (events are ordered per channel) and remove index for the output text file
                rems_characteristics_df = rems_characteristics_df.sort_values(by=['start_sec'])
                rems_characteristics_df = rems_characteristics_df.reset_index(drop=True) # do not add an index column
                try : 
                    rems_characteristics_df.to_csv(path_or_buf=rems_char_filename, sep='\t', index=False, index_label='False', mode='w', header=True, encoding="utf_8")
                    # Log message for the Logs tab
                    self._log_manager.log(self.identifier, f"REMs characteristics from {subject_info['filename']} has been generated.")
                except :
                    error_message = f"Snooz can not write in the file {rems_char_filename}."+\
                        f" Check if the drive is accessible and ensure the file is not already open."
                    raise NodeRuntimeException(self.identifier, "REMsDetails", error_message)
            else:
                # Log message for the Logs tab
                self._log_manager.log(self.identifier, f"No REMs for {subject_info['filename']}.")

        #----------------------------------------------------------------------------
        # Cohort TSV file
        #----------------------------------------------------------------------------
        if len(cohort_filename)>0:
            # Write the current report for the current subject into the cohort tsv file
            write_header = not os.path.exists(cohort_filename)
            # Order columns as the doc file
            out_columns = list(_get_doc(self.N_CYCLES, self.N_HOURS).keys())
            cohort_characteristics_df = cohort_characteristics_df[out_columns]
            try : 
                cohort_characteristics_df.to_csv(path_or_buf=cohort_filename, sep='\t', \
                    index=False, index_label='False', mode='a', header=write_header, encoding="utf_8")
            except :
                error_message = f"Snooz can not write in the file {cohort_filename}."+\
                    f" Check if the drive is accessible and ensure the file is not already open."
                raise NodeRuntimeException(self.identifier, "REMsDetails", error_message)            

            # To write the info text file to describe the variable names
            if write_header:
                # Write the documentation file
                file_name, file_extension = os.path.splitext(cohort_filename)
                doc_filepath = file_name+"_info"+file_extension
                if not os.path.exists(doc_filepath):
                    write_doc_file(doc_filepath, self.N_CYCLES, self.N_HOURS)
                    # Log message for the Logs tab
                    self._log_manager.log(self.identifier, f"The file {doc_filepath} has been created.")

            # Log message for the Logs tab
            self._log_manager.log(self.identifier, f"{subject_info['filename']} is added to {cohort_filename}.")

        return {
        }

    def add_amplitude_to_rems(self, rems_events_details, signals):
        """Add amplitude to REMs events by extracting from signals."""
        if 'amplitude_uV' in rems_events_details.columns:
            return rems_events_details
        
        # Extract amplitude from signals for each REM event
        amplitude_list = []
        for idx, row in rems_events_details.iterrows():
            # Get channels for this event
            channels_str = row['channels']
            if isinstance(channels_str, str):
                channels = [ch.strip() for ch in channels_str.split(',')]
            else:
                channels = [channels_str]
            
            # Find matching signal
            amplitude = np.nan
            segmentDict = {}
            for signal in signals:
                if signal.channel in channels:
                    # Extract signal segment for this REM event
                    start_time = row['start_sec']
                    duration = row['duration_sec']
                    start_sample = int((start_time - signal.start_time) * signal.sample_rate)
                    end_sample = int(start_sample + duration * signal.sample_rate)
                    
                    if start_sample >= 0 and end_sample <= len(signal.samples):
                        segment = signal.samples[start_sample:end_sample]
                        segmentDict[signal.channel] = segment
            
            # Calculate amplitude from LOC-ROC difference
            LOC = None
            ROC = None
            for channel, segments in segmentDict.items():
                if 'L' in channel:
                    LOC = segments
                else:
                    ROC = segments
            
            if LOC is not None and ROC is not None and len(LOC) == len(ROC):
                Subtracted_segment = LOC - ROC
                if len(Subtracted_segment) > 0:
                    # Calculate peak-to-peak amplitude
                    amplitude = np.max(Subtracted_segment) - np.min(Subtracted_segment)
            amplitude_list.append(amplitude)
        
        rems_events_details['amplitude_uV'] = amplitude_list
        return rems_events_details

    def compute_tot_stats_per_stage(self, rems_cur_chan_sort, artifact_cur_chan_df, \
        stage_in_cycle_df, sleep_stages_name, stage_sel, label_stats, stage_stats_labels):
        # Compute valid duration (min)
        #   Return a dict as valid_dur[f'{label_stats}_valid_min_{stage}']
        # artifact_cur_chan_df is kept for future use but currently not used
        valid_dur = EventsDetails.compute_valid_dur_min(artifact_cur_chan_df, \
            stage_in_cycle_df, sleep_stages_name, stage_sel, label_stats, stage_stats_labels)

        # Skip total calculations since REMs only occur in R stage
        # Total values would be identical to R stage values, so we only keep R stage values
        mean_tot = {}
        rems_count_tot = {}                
        # Average characteristique per stage (REMs only occur in R stage)
        mean_stage = {}
        rems_count_stage = {}
        rems_density_stage = {}
        stage = 'R'  # REMs only occur in REM sleep
        # Extract rems for the R stage
        rems_cur_chan_stage = rems_cur_chan_sort[rems_cur_chan_sort['Stage']==int(sleep_stages_name[stage])]
        rems_cur_chan_stage = rems_cur_chan_stage[self.rems_characteristics]
        # Format the rems_cur_chan_stage dataframe values into float
        rems_cur_chan_stage = rems_cur_chan_stage.applymap(float)
        # Compute the number of detection per stage
        n_rems = len(rems_cur_chan_stage)
        rems_count_stage[f'{label_stats}_{stage}_rems_count'] = n_rems
        # Compute the density (per 30-second epoch)
        # 1 minute = 2 epochs (30 seconds each)
        if valid_dur[f'{label_stats}_{stage}_valid_min']>0:
            rems_density_stage[f'{label_stats}_{stage}_rems_density'] = n_rems/(valid_dur[f'{label_stats}_{stage}_valid_min'] * 2)
        else:
            rems_density_stage[f'{label_stats}_{stage}_rems_density'] = np.nan
        # Average the characteristiques for the current recording and stage
        if n_rems==0:
            for key in self.rems_characteristics:
                if key=='duration_sec':
                    mean_stage[f'{label_stats}_{stage}_rems_sec'] = np.NaN 
                else:
                    mean_stage[f'{label_stats}_{stage}_{key}'] = np.NaN      
        else:
            mean_char_series = rems_cur_chan_stage.mean(axis=0, skipna=True, numeric_only=True)
            mean_char_series = mean_char_series.round(decimals=2)
            mean_char_stage = mean_char_series.to_dict()
            for key, value in mean_char_stage.items():
                if key=='duration_sec':
                    mean_stage[f'{label_stats}_{stage}_rems_sec'] = value
                else:
                    mean_stage[f'{label_stats}_{stage}_{key}'] = value              
        # Skip total density and variance since they're identical to R stage values
        rems_density_tot = {}
        rems_density_variance = {}
        
        # Filter out redundant total valid_min (same as R since REMs only occur in R)
        # Remove keys like 'total_valid_min' but keep 'total_R_valid_min'
        valid_dur_filtered = {k: v for k, v in valid_dur.items() 
                             if not (k == f'{label_stats}_valid_min' and f'{label_stats}_R_valid_min' in valid_dur)}
        
        tot_stats =  valid_dur_filtered | rems_count_stage | mean_stage | rems_density_stage
        return tot_stats


    def compute_cyc_stats_per_stage(self, rems_cur_chan_sort, artifact_cur_chan_df, stage_in_cycle_df, \
        sleep_cycles_df, sleep_stages_name, stage_sel, label_stats, stage_stats_labels):

        # REMs events
        rems_start_times = rems_cur_chan_sort['start_sec'].to_numpy().astype(float)   # numpy array
        rems_duration_times = rems_cur_chan_sort['duration_sec'].to_numpy().astype(float)  # numpy array
        rems_end_times = rems_start_times+rems_duration_times        

        # Stage events
        stage_starts = stage_in_cycle_df['start_sec'].values
        stage_durations = stage_in_cycle_df['duration_sec'].values
        stage_ends = stage_starts+stage_durations  

        # Cycle events
        cycle_starts = sleep_cycles_df['start_sec'].values
        cycle_durations = sleep_cycles_df['duration_sec'].values
        cycle_ends = cycle_starts+cycle_durations

        # Stage columns labels
        stage_col_label = stage_in_cycle_df.columns

        valid_dur= {}
        rec_dur = {}
        mean_stage = {}
        rems_count_stage = {}
        rems_density_stage = {}
        # For each sleep cycle
        for i_cycle in range(self.N_CYCLES):
            cycle_label = label_stats+str(i_cycle+1)
            
            # If the cycle exist
            if len(cycle_durations)>i_cycle:
                # Select the stages from the current cycle
                i_cycle_start = cycle_starts[i_cycle]
                i_cycle_end = cycle_ends[i_cycle]
                stages_bool = (stage_starts>=i_cycle_start) & (stage_ends<=i_cycle_end)
                stages_i_sel = np.nonzero(stages_bool)[0]
                stage_sel_df = stage_in_cycle_df.iloc[stages_i_sel]

                # Select the rems from the current cycle
                rems_bool = (rems_start_times>=i_cycle_start) & (rems_end_times<=i_cycle_end)
                rems_sel_i = np.nonzero(rems_bool)[0]
                rems_sel_df = rems_cur_chan_sort.iloc[rems_sel_i]
            else:
                stage_sel_df = pd.DataFrame(columns=stage_col_label)
                rems_sel_df = pd.DataFrame(columns=self.rems_columns)

            # Extract characteristics to average
            rems_sel_to_mean = rems_sel_df[self.rems_characteristics]
            # Format the rems_cur_chan_stage dataframe values into float
            rems_sel_to_mean = rems_sel_to_mean.applymap(float)

            if len(cycle_durations)>i_cycle:
                # Compute duration (min)
                rec_dur[f'{cycle_label}_min'] = cycle_durations[i_cycle]/60
            else:
                rec_dur[f'{cycle_label}_min'] = 0

            # Compute valid duration (min)
            #   For each sleep stage included in stage_sel_df, compute the duration without artifact (valid_min).
            # artifact_cur_chan_df is kept for future use but currently not used
            valid_dur_cur = EventsDetails.compute_valid_dur_min(artifact_cur_chan_df, stage_sel_df, \
                commons.sleep_stages_name, stage_sel, cycle_label, self.stage_stats_labels)
            # Accumulate for each cycle
            valid_dur = valid_dur | valid_dur_cur
            # Skip cycle-level totals since REMs only occur in R stage
            # Cycle totals would be identical to R stage values within that cycle          

            # Average characteristique per stage (REMs only occur in R stage)
            stage = 'R'  # REMs only occur in REM sleep
            # Extract rems for the R stage
            rems_cur_chan_stage = rems_sel_df[rems_sel_df['Stage']==int(sleep_stages_name[stage])]
            rems_cur_to_mean = rems_cur_chan_stage[self.rems_characteristics]
            # Format the rems_cur_chan_stage dataframe values into float
            rems_cur_to_mean = rems_cur_to_mean.applymap(float)

            # Compute the number of detection per stage
            n_rems = len(rems_cur_chan_stage)
            rems_count_stage[f'{cycle_label}_{stage}_rems_count'] = n_rems
            # Compute the density (per 30-second epoch)
            # 1 minute = 2 epochs (30 seconds each)
            if valid_dur_cur[f'{cycle_label}_{stage}_valid_min']>0:
                rems_density_stage[f'{cycle_label}_{stage}_rems_density'] = n_rems/(valid_dur_cur[f'{cycle_label}_{stage}_valid_min'] * 2)
            else:
                rems_density_stage[f'{cycle_label}_{stage}_rems_density'] = np.nan

            # Average the characteristiques for the current recording and stage
            if n_rems==0:
                for key in self.rems_characteristics:
                    if key=='duration_sec':
                        mean_stage[f'{cycle_label}_{stage}_rems_sec'] = np.NaN
                    else:
                        mean_stage[f'{cycle_label}_{stage}_{key}'] = np.NaN                        
            else:
                mean_char_series = rems_cur_to_mean.mean(axis=0, skipna=True, numeric_only=True)
                mean_char_series = mean_char_series.round(decimals=2)
                mean_char_stage = mean_char_series.to_dict()
                for key, value in mean_char_stage.items():
                    if key=='duration_sec':
                        mean_stage[f'{cycle_label}_{stage}_rems_sec'] = value
                    else:
                        mean_stage[f'{cycle_label}_{stage}_{key}'] = value

            # Calculate variance of densities across cycles using R stage densities
            density_values = [rems_density_stage.get(f'cyc{i+1}_R_rems_density', np.nan) 
                            for i in range(self.N_CYCLES)]
            density_values = [d for d in density_values if not np.isnan(d)]
            if len(density_values) > 1:
                rems_density_variance = {'rems_density_var': np.var(density_values, ddof=1)}
            else:
                rems_density_variance = {'rems_density_var': np.nan}
            
            # Filter out redundant cycle-level valid_min (same as R since REMs only occur in R)
            # Remove keys like 'cyc1_valid_min' but keep 'cyc1_R_valid_min'
            valid_dur_filtered = {}
            for k, v in valid_dur.items():
                if k.startswith('cyc') and k.endswith('_valid_min') and not k.endswith('_R_valid_min'):
                    # Check if corresponding R version exists
                    cycle_num = k.split('_')[0]  # e.g., 'cyc1'
                    if f'{cycle_num}_R_valid_min' in valid_dur:
                        continue  # Skip this redundant entry
                valid_dur_filtered[k] = v
            
            cyc_stats =  valid_dur_filtered | rec_dur | rems_count_stage | mean_stage | rems_density_stage | rems_density_variance
        return cyc_stats

    def compute_clock_h_stats_per_stage(self, rems_cur_chan_sort, artifact_cur_chan_df, stage_in_cycle_df, \
        sleep_stages_name, stage_sel, label_stats, stage_stats_labels):
        """""
        Compute statistics for each clock hour

        Parameters
        -----------
            rems_cur_chan_sort : pandas DataFrame
                REMs events including the characteristics
            artifact_cur_chan_df : pandas DataFrame
                List of artifacts events (kept for future use, currently not used)
            stage_in_cycle_df   : pandas DataFrame
                List of sleep stages included in the cycles.
            sleep_stages_name : dict
                Dict of sleep stage label to number (commons.sleep_stages_name)
            stage_sel     : list
                List of sleep stage number selected (ex. ['2', '3'])
            label_stats         : str
                The label of the statistics to export. I.e. : 'clock_h', ...
            stage_stats_labels : list
                List of label to use for the stages.

        Returns
        -----------  
            stats   : dict
                List of statistics for each clock hour.
        """""
        # REMs events
        rems_start_times = rems_cur_chan_sort['start_sec'].to_numpy().astype(float)   # numpy array
        rems_duration_times = rems_cur_chan_sort['duration_sec'].to_numpy().astype(float)  # numpy array
        rems_end_times = rems_start_times+rems_duration_times        

        # Stage events
        stage_starts = stage_in_cycle_df['start_sec'].values
        stage_durations = stage_in_cycle_df['duration_sec'].values
        stage_ends = stage_starts+stage_durations    

        # For each clock hour
        hour_valid_dur_stats = {}
        hour_rems_stats = {}
        hour_rec_dur_stats = {}
        
        # Get the start time of the recording (first sleep stage)
        recording_start_time = stage_in_cycle_df['start_sec'].iloc[0] if len(stage_in_cycle_df) > 0 else 0
        
        for i_hour in range(self.N_HOURS):
            hour_label = label_stats+str(i_hour+1)
            
            # Calculate hour boundaries (similar to PSACompilation approach)
            start_hour = recording_start_time + i_hour * 3600  # 3600 seconds = 1 hour
            end_hour = start_hour + 3600
            
            # Select the stages from the current hour
            stages_bool = (stage_starts >= start_hour) & (stage_ends <= end_hour)
            stages_i_sel = np.nonzero(stages_bool)[0]
            stage_sel_df = stage_in_cycle_df.iloc[stages_i_sel] if len(stages_i_sel) > 0 else pd.DataFrame()

            # Select the rems from the current hour
            rems_bool = (rems_start_times >= start_hour) & (rems_end_times <= end_hour)
            rems_sel_i = np.nonzero(rems_bool)[0]
            # To know in which sleep stage the rems occurs
            rems_sel_df = rems_cur_chan_sort.iloc[rems_sel_i]

            # Compute recording duration (min) for this hour
            hour_duration = min(3600, end_hour - start_hour) if end_hour > start_hour else 0
            hour_rec_dur_stats[f'{hour_label}_min'] = hour_duration / 60

            # Compute valid duration (min) for this hour
            # For each sleep stage included in stage_sel_df, compute the duration without artifact (valid_min).
            # artifact_cur_chan_df is kept for future use but currently not used
            if len(stage_sel_df) > 0:
                valid_dur_stats_cur = EventsDetails.compute_valid_dur_min(artifact_cur_chan_df, stage_sel_df, \
                    sleep_stages_name, stage_sel, hour_label, stage_stats_labels)
                hour_valid_dur_stats = hour_valid_dur_stats | valid_dur_stats_cur

                # Compute the rems count and characteristics per stage
                rems_stats_cur = self.compute_rems_stats_per_stage(valid_dur_stats_cur, rems_sel_df, stage_sel, hour_label, stage_stats_labels)
                hour_rems_stats = hour_rems_stats | rems_stats_cur
            else:
                # No stages in this hour - set R stage values to NaN (skip totals since they're redundant)
                # REMs only occur in R stage
                stage = 'R'
                hour_valid_dur_stats[f'{hour_label}_{stage}_valid_min'] = np.NaN
                hour_rems_stats[f'{hour_label}_{stage}_rems_count'] = np.NaN
                hour_rems_stats[f'{hour_label}_{stage}_rems_sec'] = np.NaN
                hour_rems_stats[f'{hour_label}_{stage}_amplitude_uV'] = np.NaN
                hour_rems_stats[f'{hour_label}_{stage}_rems_density'] = np.NaN

        # Calculate variance of densities across clock hours using R stage densities
        density_values = [hour_rems_stats.get(f'clock_h{i+1}_R_rems_density', np.nan) 
                        for i in range(self.N_HOURS)]
        density_values = [d for d in density_values if not np.isnan(d)]
        if len(density_values) > 1:
            hour_rems_stats['clock_h_rems_density_var'] = np.var(density_values, ddof=1)
        else:
            hour_rems_stats['clock_h_rems_density_var'] = np.nan

        # Filter out redundant clock hour-level valid_min (same as R since REMs only occur in R)
        # Remove keys like 'clock_h1_valid_min' but keep 'clock_h1_R_valid_min'
        hour_valid_dur_stats_filtered = {}
        for k, v in hour_valid_dur_stats.items():
            if k.startswith('clock_h') and k.endswith('_valid_min') and not k.endswith('_R_valid_min'):
                # Check if corresponding R version exists
                hour_num = k.split('_')[0] + '_' + k.split('_')[1]  # e.g., 'clock_h1'
                if f'{hour_num}_R_valid_min' in hour_valid_dur_stats:
                    continue  # Skip this redundant entry
            hour_valid_dur_stats_filtered[k] = v

        # Organize data for the output
        return hour_rec_dur_stats | hour_valid_dur_stats_filtered | hour_rems_stats

    def compute_stage_h_stats_per_stage(self, rems_cur_chan_sort, artifact_cur_chan_df, stage_in_cycle_df, \
        sleep_stages_name, stage_sel, label_stats, stage_stats_labels):
        """""
        Compute statistics for each stage hour (window-based segmentation)

        Parameters
        -----------
            rems_cur_chan_sort : pandas DataFrame
                REMs events including the characteristics
            artifact_cur_chan_df : pandas DataFrame
                List of artifacts events (kept for future use, currently not used)
            stage_in_cycle_df   : pandas DataFrame
                List of sleep stages included in the cycles.
            sleep_stages_name : dict
                Dict of sleep stage label to number (commons.sleep_stages_name)
            stage_sel     : list
                List of sleep stage number selected (ex. ['2', '3'])
            label_stats         : str
                The label of the statistics to export. I.e. : 'stage_h', ...
            stage_stats_labels : list
                List of label to use for the stages.

        Returns
        -----------  
            stats   : dict
                List of statistics for each stage hour.
        """""
        # REMs events
        rems_start_times = rems_cur_chan_sort['start_sec'].to_numpy().astype(float)   # numpy array
        rems_duration_times = rems_cur_chan_sort['duration_sec'].to_numpy().astype(float)  # numpy array
        rems_end_times = rems_start_times+rems_duration_times        

        # Stage events
        stage_starts = stage_in_cycle_df['start_sec'].values
        stage_durations = stage_in_cycle_df['duration_sec'].values
        stage_ends = stage_starts+stage_durations    

        # For each stage hour (window-based segmentation)
        stage_hour_valid_dur_stats = {}
        stage_hour_rems_stats = {}
        stage_hour_rec_dur_stats = {}
        
        # Calculate expected windows per hour (assuming 30-second epochs)
        # Extract the first value of the unique list of duration_sec in stage_in_cycle_df
        epoch_duration = round(np.unique(stage_durations)[0])
        expected_windows_per_hour = 3600.0 / epoch_duration  # 120 windows per hour
        
        # Collect R stages and rems (REMs only occur in R stage)
        stage_label = 'R'
        stage_data = []
        rems_data = []
        
        # Collect R stages
        stage_mask = stage_in_cycle_df['name'] == int(sleep_stages_name[stage_label])
        if stage_mask.any():
            stage_data.extend(stage_in_cycle_df[stage_mask].to_dict('records'))
        # Sort stages by start time
        stage_data.sort(key=lambda x: x['start_sec'])
        # Collect rems in R stage
        rems_mask = rems_cur_chan_sort['Stage'] == int(sleep_stages_name[stage_label])
        if rems_mask.any():
            rems_data.extend(rems_cur_chan_sort[rems_mask].to_dict('records'))
        # Sort rems by start time
        rems_data.sort(key=lambda x: x['start_sec'])
        
        # Process each hour
        for i_hour in range(self.N_HOURS):
            hour_label = label_stats+str(i_hour+1)
            
            # Calculate window indices for this hour
            start_window = int(i_hour * expected_windows_per_hour)
            end_window = int((i_hour + 1) * expected_windows_per_hour)
            
            # Apply window-based segmentation for R stage
            stages_cur_hour = []
            rems_cur_hour = []
            
            if len(stage_data) > start_window:
                stages_cur_hour = stage_data[start_window:min(end_window, len(stage_data))]           
                # Filter rems_cur_hour to only include REMs within the stage time range
                stage_start_time = stages_cur_hour[0]['start_sec']
                stage_end_time = stages_cur_hour[-1]['start_sec'] + stages_cur_hour[-1]['duration_sec']
                rems_cur_hour = [rem for rem in rems_data if stage_start_time <= rem['start_sec'] <= stage_end_time]

            # Convert back to DataFrames for processing
            if stages_cur_hour:
                stage_sel_df = pd.DataFrame(stages_cur_hour)
            else:
                stage_sel_df = pd.DataFrame()
            
            if rems_cur_hour:
                rems_sel_df = pd.DataFrame(rems_cur_hour)
            else:
                rems_sel_df = pd.DataFrame()
            
            # Compute valid duration and rems statistics for R stage and hour
            # artifact_cur_chan_df is kept for future use but currently not used
            if len(stage_sel_df) > 0:
                valid_dur_stats_cur = EventsDetails.compute_stage_duration_for_single_stage(stage_sel_df, \
                    artifact_cur_chan_df, stage_label, hour_label, stage_sel)
                stage_hour_valid_dur_stats = stage_hour_valid_dur_stats | valid_dur_stats_cur

                # Only compute rems statistics if we have rems
                if len(rems_sel_df) > 0:
                    # Compute statistics for R stage only
                    rems_stats_cur = self.compute_rems_stats_for_single_stage(valid_dur_stats_cur, rems_sel_df, stage_label, hour_label)
                    stage_hour_rems_stats = stage_hour_rems_stats | rems_stats_cur
                else:
                    # No rems in this hour - set all rems values to NaN
                    stage_hour_rems_stats[f'{hour_label}_{stage_label}_rems_count'] = np.NaN
                    stage_hour_rems_stats[f'{hour_label}_{stage_label}_rems_sec'] = np.NaN
                    stage_hour_rems_stats[f'{hour_label}_{stage_label}_amplitude_uV'] = np.NaN
                    stage_hour_rems_stats[f'{hour_label}_{stage_label}_rems_density'] = np.NaN
            else:
                # No stages in this hour - set all values to NaN
                stage_hour_valid_dur_stats[f'{hour_label}_{stage_label}_valid_min'] = np.NaN
                stage_hour_rems_stats[f'{hour_label}_{stage_label}_rems_count'] = np.NaN
                stage_hour_rems_stats[f'{hour_label}_{stage_label}_rems_sec'] = np.NaN
                stage_hour_rems_stats[f'{hour_label}_{stage_label}_amplitude_uV'] = np.NaN
                stage_hour_rems_stats[f'{hour_label}_{stage_label}_rems_density'] = np.NaN
            
            # Compute total statistics for this hour (same as R since REMs only occur in R)
            # Apply window segmentation for totals
            if len(stage_data) > start_window:
                total_stages_hour = len(stage_data) - start_window
                stage_hour_rec_dur_stats[f'{hour_label}_min'] = min(total_stages_hour * epoch_duration / 60, 60)  # Max 60 minutes
            else:
                stage_hour_rec_dur_stats[f'{hour_label}_min'] = 0
            
        # Calculate variance of densities across stage hours using R stage densities
        density_values = [stage_hour_rems_stats.get(f'stage_h{i+1}_R_rems_density', np.nan) 
                        for i in range(self.N_HOURS)]
        density_values = [d for d in density_values if not np.isnan(d)]
        if len(density_values) > 1:
            stage_hour_rems_stats['stage_h_rems_density_var'] = np.var(density_values, ddof=1)
        else:
            stage_hour_rems_stats['stage_h_rems_density_var'] = np.nan

        # Filter out redundant stage hour-level valid_min (same as R since REMs only occur in R)
        # Remove keys like 'stage_h1_valid_min' but keep 'stage_h1_R_valid_min'
        stage_hour_valid_dur_stats_filtered = {}
        for k, v in stage_hour_valid_dur_stats.items():
            if k.startswith('stage_h') and k.endswith('_valid_min') and not k.endswith('_R_valid_min'):
                # Check if corresponding R version exists
                hour_num = k.split('_')[0] + '_' + k.split('_')[1]  # e.g., 'stage_h1'
                if f'{hour_num}_R_valid_min' in stage_hour_valid_dur_stats:
                    continue  # Skip this redundant entry
            stage_hour_valid_dur_stats_filtered[k] = v

        # Organize data for the output
        return stage_hour_rec_dur_stats | stage_hour_valid_dur_stats_filtered | stage_hour_rems_stats

    def compute_rems_stats_per_stage(self, valid_dur, rems_cur_chan_df, sleep_stage_sel, label_stats, stage_stats_labels):
        """""
        Compute the general REMs characteristics such as count and average characteristics 
        for all REMs in rems_cur_chan_df.

        Parameters
        -----------
            valid_dur : dict
                Dictionary containing valid duration information
            rems_cur_chan_df : pandas DataFrame
                REMs events for the current stage type
            sleep_stage_sel     : list of string
                List of sleep stage number selected (ex. ['2', '3'])
            label_stats : string
                The label of the statistics to export. I.e. : 'total', 'cycle1', 'cycle2', ...
            stage_stats_labels : list
                List of label to use for the stages.
        Returns
        -----------  
            rems_stats   : dict
                Dictionary containing statistics for the REMs
        """""
        rems_count = {}
        rems_sec = {}
        amplitude_uV = {}
        rems_density = {}
        
        # REMs only occur in R stage
        stage = 'R'
        # Count the number of REMs for R stage
        rems_cur_stage = rems_cur_chan_df[rems_cur_chan_df['Stage']==int(commons.sleep_stages_name[stage])]
        rems_count_cur_stage = len(rems_cur_stage)

        if valid_dur[f'{label_stats}_{stage}_valid_min']>0:
            rems_count[f'{label_stats}_{stage}_rems_count'] = rems_count_cur_stage
        else:
            rems_count[f'{label_stats}_{stage}_rems_count'] = np.nan
        # Compute the density (per 30-second epoch)
        # 1 minute = 2 epochs (30 seconds each)
        if valid_dur[f'{label_stats}_{stage}_valid_min']>0:
            rems_density[f'{label_stats}_{stage}_rems_density'] = rems_count_cur_stage/(valid_dur[f'{label_stats}_{stage}_valid_min'] * 2)
        else:
            rems_density[f'{label_stats}_{stage}_rems_density'] = np.nan

        if rems_count_cur_stage>0:
            rems_sec[f'{label_stats}_{stage}_rems_sec'] = rems_cur_stage['duration_sec'].sum()/rems_count_cur_stage
            amplitude_uV[f'{label_stats}_{stage}_amplitude_uV'] = rems_cur_stage['amplitude_uV'].sum()/rems_count_cur_stage
        else:
            rems_sec[f'{label_stats}_{stage}_rems_sec'] = np.NaN
            amplitude_uV[f'{label_stats}_{stage}_amplitude_uV'] = np.NaN

        # Skip total stats since they're identical to R stage values (REMs only occur in R)
        # Only return R stage values to avoid repetition

        rems_stats = rems_count | rems_sec | amplitude_uV | rems_density
        return rems_stats

    def compute_rems_stats_for_single_stage(self, valid_dur, rems_cur_chan_df, stage_label, label_stats):
        """""
        Compute statistics for R stage (REMs only occur in REM sleep).
        This is a simplified version of compute_rems_stats_per_stage for single stage processing.

        Parameters
        -----------
            valid_dur : dict
                Dictionary containing valid duration information
            rems_cur_chan_df : pandas DataFrame
                REMs events for the current stage type
            stage_label : str
                The stage label (should be 'R' since REMs only occur in REM sleep)
            label_stats : str
                The label for the statistics (e.g., "stage_h1")
                
        Returns
        -----------  
            rems_stats : dict
                Dictionary containing statistics for the single stage
        """""
        # Get the valid duration for this specific stage
        valid_dur_key = f'{label_stats}_{stage_label}_valid_min'
        if valid_dur_key not in valid_dur:
            valid_dur_key = f'{label_stats}_valid_min'  # fallback to general valid duration
        
        valid_duration = valid_dur.get(valid_dur_key, 0)
        
        # Count REMs
        rems_count = len(rems_cur_chan_df)
        
        # Initialize result dictionary
        result = {}
        
        # REMs count
        if valid_duration > 0:
            result[f'{label_stats}_{stage_label}_rems_count'] = rems_count
        else:
            result[f'{label_stats}_{stage_label}_rems_count'] = np.nan
        # Compute the density (per 30-second epoch)
        # valid_duration is in minutes, 1 minute = 2 epochs (30 seconds each)
        if valid_duration > 0:
            result[f'{label_stats}_{stage_label}_rems_density'] = rems_count/(valid_duration * 2)
        else:
            result[f'{label_stats}_{stage_label}_rems_density'] = np.nan
            
        # Other characteristics (only if we have REMs) - using same approach as original
        if rems_count > 0:
            # Use the same calculation method as compute_rems_stats_per_stage
            result[f'{label_stats}_{stage_label}_rems_sec'] = rems_cur_chan_df['duration_sec'].sum() / rems_count
            result[f'{label_stats}_{stage_label}_amplitude_uV'] = rems_cur_chan_df['amplitude_uV'].sum() / rems_count
        else:
            result[f'{label_stats}_{stage_label}_rems_sec'] = np.nan
            result[f'{label_stats}_{stage_label}_amplitude_uV'] = np.nan
            
        return result

