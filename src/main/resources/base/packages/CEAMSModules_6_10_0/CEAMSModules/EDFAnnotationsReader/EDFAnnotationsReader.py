"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.

    EDFAnnotationsReader
    Class to read the EDF Annotations signal and create a pandas dataframe with the events.
"""
import numpy as np
import os
import pandas as pd
import pyedflib
import re
import xml.etree.ElementTree as ET

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

from CEAMSModules.EventReader import manage_events
from CEAMSModules.PSGReader import commons


DEBUG = True

class EDFAnnotationsReader(SciNode):
    """
    Class to read the EDF Annotations signal and create a pandas dataframe with the events.

    Parameters
    ----------
        annot_files: list of string
            List of edf file to read.
        psg_files: list of string
            List of edf file to read.
        
    Returns
    -------
        filename: string
            The current file read.
        events: Pandas DataFrame with columns ['group','name','start_sec','duration_sec','channels']
            The list of events read.
        
    """
    def __init__(self, **kwargs):
        """ Initialize module EDFAnnotationsReader """
        super().__init__(**kwargs)
        if DEBUG: print('EDFAnnotationsReader.__init__')

        # Input plugs
        InputPlug('annot_files',self)
        InputPlug('psg_files',self)
        # Output plugs
        OutputPlug('filename',self)
        OutputPlug('events',self)

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = True
        self.is_done = False

        self.EPOCH_LEN_S = 30

    
    def compute(self, annot_files, psg_files):
        """
        Read one EDF file at the time (from the list) and extract the events from theEDF Annotations signal.

        Parameters
        ----------
            annot_files: list of string
                List of edf file to read.
            psg_files: list of string
                List of edf file to read.
            
        Returns
        -------
            filename: string
                The current file read.
            events: Pandas DataFrame with columns ['group','name','start_sec','duration_sec','channels']
                The list of events read.
            
        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """

        if isinstance(annot_files, str) and not annot_files=='':
            annot_files = eval(annot_files)

        if annot_files == '' or annot_files is None or len(annot_files) == 0:
            raise NodeInputException(self.identifier, "annot_files", \
                "EDFAnnotationsReader annot_files parameter must be set.")

        if isinstance(psg_files, str) and not psg_files=='':
            psg_files = eval(psg_files)

        if psg_files == '' or psg_files is None or len(psg_files) == 0:
            raise NodeInputException(self.identifier, "psg_files", \
                "EDFAnnotationsReader psg_files parameter must be set.")

        annot_filename = annot_files[self.iteration_counter]
        psg_filename = psg_files[self.iteration_counter]

        # Set the iteration_identifier in case there is a problem during the process.
        # This will be used to identify the problematic file.
        self.iteration_identifier = annot_filename

        # Check if the file exist
        if(not os.path.isfile(annot_filename)):
            raise NodeRuntimeException(self.identifier, "annot_files", \
                f"EDFAnnotationsReader file not found:{annot_filename}")
        if(not os.path.isfile(psg_filename)):
            raise NodeRuntimeException(self.identifier, "psg_files", \
                f"EDFAnnotationsReader file not found:{psg_filename}")


        #--------------------------------------------------------------------
        # Read the header (including the annotations) of the annotations file
        #--------------------------------------------------------------------
        try : 
            edf_header = pyedflib.highlevel.read_edf_header(annot_filename)
            if 'annotations' not in edf_header:
                raise NodeRuntimeException(self.identifier, "annot_files", \
                    f"The EDF Annotations signal is not found in {annot_filename}")
            else:
                edf_annotations = edf_header['annotations']
                if len(edf_annotations)==0:
                    raise NodeRuntimeException(self.identifier, "annot_files", \
                        f"The EDF Annotations signal is empty in {annot_filename}")
                else:
                    # Read the start time of the annotations file
                    annot_startdate = edf_header['startdate']
                    # Convert the list of annotations in a dataframe
                    annot_df = pd.DataFrame(data=edf_annotations, columns=['start_sec', 'duration_sec', 'description'])
        except : 
            raise NodeRuntimeException(self.identifier, "annot_files", \
                f"Error reading the header of the edf file:{annot_filename}")

        #--------------------------------------------------------------------
        # Read the header of the psg file
        #--------------------------------------------------------------------
        try : 
            psg_header = pyedflib.highlevel.read_edf_header(psg_filename)
            # Read the start time of the psg file
            psg_start_time = psg_header['startdate']
        except : 
            raise NodeRuntimeException(self.identifier, "annot_files", \
                f"Error reading the header of the edf file:{annot_filename}")

        #--------------------------------------------------------------------
        # Offset the annotations to match the start time of the psg file
        #--------------------------------------------------------------------
        if annot_startdate != psg_start_time:
            # Compute the difference between the start time of the annotations and the start time of the psg file
            delta = psg_start_time - annot_startdate
            # Convert the delta in seconds
            delta_sec = delta.total_seconds()*10 # The delta time is off per a factor or 10
            # Adapt the startime of each annotation to match the starttime of the psg file
            annot_df['start_sec'] = annot_df['start_sec'] - delta_sec

        # Convert the duration_sec in float
        annot_df['duration_sec'] = annot_df['duration_sec'].astype(float)

        # Add the columns 'group' at the beginning and the column 'channels' at the end
        annot_df.insert(0, 'group', 'EDF annotations')
        annot_df.insert(1, 'name', 'EDF annotations')
        annot_df.insert(4, 'channels', '[]')


        #--------------------------------------------------------------------
        # Define the group and channels
        #--------------------------------------------------------------------
        # iterate over the rows of the dataframe
        for index, row in annot_df.iterrows():
            try :
                # Parse the description in case it is an XML string
                root = ET.fromstring(row['description'])
                # Extract attributes and fill the dataframe
                # For MASS compatibility
                fields_dict = root.attrib
                if "channel" in fields_dict.keys():
                    annot_df.at[index, 'channels'] = f"['{fields_dict['channel']}']"
                if "groupName" in fields_dict.keys():
                    annot_df.at[index, 'group'] = fields_dict['groupName']
                if "name" in fields_dict.keys():
                    annot_df.at[index, 'name'] = fields_dict['name']
            except :
                annot_df.at[index, 'name'] = row['description']

        #--------------------------------------------------------------------
        # Define the sleep stages
        #--------------------------------------------------------------------
        # Look for the string "Sleep stage" in the name column and add 'stage' in the group column
        annot_df['group'] = annot_df['name'].str.contains('Sleep stage', case=False).fillna(False).apply(lambda x: 'stage' if x else 'EDF annotations')

        # commons.EDF_plus_stages is a dictionary where the keys are the EDF+ sleep stage name 
        #   and the values are the corresponding stage number
        # rename the sleep stage to the corresponding stage number
        annot_df['name'] = annot_df['name'].replace(commons.EDF_plus_stages)
        annot_df['name'] = annot_df['name'].replace(commons.EDF_plus_stages_v1)

        # Split the sleep stages into epochs if Continuous sleep stages are grouped together
        #-------------------------------------------------------------------------
        # extract the sleep stages from the annot_df
        sleep_stage_ori = annot_df[(annot_df['group']=='stage')]
        # Round the duration of events (especially for stellate cases)
        duration_sec = sleep_stage_ori['duration_sec'].to_numpy().astype(float)
        duration_sec = np.around(duration_sec, decimals=2)
        sleep_stage_ori.loc[:,'duration_sec']=duration_sec.astype(float)
        # Compute the unique list of sleep stage duration
        # The last epoch is often shorter, we exlude it in the epoch length computation
        unique_duration = np.unique(duration_sec[0:-1])
        
        # Sometime Continuous sleep stages are grouped together
        # We segment the data to create epochs
        if len(unique_duration) > 1:
            # drop the sleep stages from the annot_df
            annot_df = annot_df.drop(annot_df[(annot_df['group']=='stage')].index)
            if 20 in unique_duration:
                self.EPOCH_LEN_S = 20
            elif 30 in unique_duration:
                self.EPOCH_LEN_S = 30
            else:
                raise NodeRuntimeException(self.identifier, "annot_files", \
                    f"Error in the duration of the sleep stage: {unique_duration}")
            # Accumulate all the short events (no modification)
            sleep_stage_out = sleep_stage_ori[(duration_sec <= unique_duration[0])]

            # For each too long events, split it
            event_too_long = sleep_stage_ori[(duration_sec > self.EPOCH_LEN_S)]
            for index, row in event_too_long.iterrows():
                n_events = int(row['duration_sec']/self.EPOCH_LEN_S)
                last_duration = row['duration_sec']%self.EPOCH_LEN_S
                split_event = [(row['group'], row['name'], row['start_sec']+i_evt*self.EPOCH_LEN_S, self.EPOCH_LEN_S, row['channels']) for i_evt in range(n_events)]
                if last_duration>0:
                    split_event.append((row['group'], row['name'], row['start_sec']+n_events*self.EPOCH_LEN_S, last_duration, row['channels']))
                # Create a pandas dataframe of events (each row is an event)
                events_split_df = pd.DataFrame(split_event, columns=['group','name','start_sec','duration_sec','channels']) 
                sleep_stage_out = pd.concat([sleep_stage_out,events_split_df])

            # Add back the sleep stage into the annot_df
            annot_df = pd.concat([annot_df, sleep_stage_out])
            # Reset index
            annot_df.reset_index(inplace=True, drop=True)
            # Sort events based on the start_sec
            annot_df.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')

        #--------------------------------------------------------------------
        # Drop the description column
        #--------------------------------------------------------------------
        annot_df = annot_df.drop(['description'], axis=1)

        annot_df['channels'] = annot_df['channels'].apply(eval)
        # Clean up lists of channels for a single channel (string) per event
        annot_df = manage_events.convert_event_df_to_single_channel(annot_df)
        # In NATUS/Stellate the annotations can be duplicated
        annot_df.drop_duplicates(inplace=True, ignore_index=True) 

        #--------------------------------------------------------------------
        # Prepare the annotation.tsv file
        #--------------------------------------------------------------------
        # The filename of the annotation file is the psg_filename with the extension .tsv instead of .edf
        #tsv_filename = psg_filename.replace('.edf', '.tsv')
        #tsv_filename = re.sub(r'\.edf$', '.tsv', psg_filename, flags=re.IGNORECASE)
        # verify if the tsv file already exists
        # if os.path.exists(tsv_filename):
        #     # Append the annotations in the tsv file
        #     annot_df.to_csv(tsv_filename, sep='\t', header=False, mode='a', index=False)
        # else:
        #     # Write the annotations in the tsv file
        #     annot_df.to_csv(tsv_filename, sep='\t', header=True, mode='x', index=False)

        #--------------------------------------------------------------------
        # Write to the cache to use the data in the resultTab
        #--------------------------------------------------------------------
        cache = {}
        cache['events'] = annot_df
        self._cache_manager.write_mem_cache(self.identifier, cache)
        # Log message for the Logs tab
        self._log_manager.log(self.identifier, f"{annot_filename} has been read.")

        # Update progression information
        self.iteration_count = len(annot_files)
        self.is_done = (self.iteration_counter + 1 == len(annot_files))

        return {
            'filename': psg_filename,
            'events': annot_df
        }