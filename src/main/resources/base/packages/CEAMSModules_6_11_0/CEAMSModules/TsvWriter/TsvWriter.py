"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Saves events to a CSV file.
    Parameters
    -----------
        filename : string
            The filename to save to
        events : pandas DataFrame
            The list of events to save
        EDF_annot : String of bool
            Flag to generate the event_name with @@channel_label.
        time_elapsed : String of bool
            Flag to add a column with the time elapsed (HH:MM:SS)
        append_data : String of bool
            Flag to append data to file instead of rewriting
        header_from_event : String of bool
            Flag to use the header of the event instead of the default header
    Returns
    -----------   
        None
"""
import numpy as np
from operator import floordiv
import os
import pandas as pd

from flowpipe import SciNode, InputPlug
from commons.NodeRuntimeException import NodeRuntimeException
from CEAMSModules.EventReader import manage_events

DEBUG = False

class TsvWriter(SciNode):
    """
    Saves events to a CSV file.
    Parameters
    -----------
        filename : string
            The filename to save to
        events : pandas DataFrame
            The list of events to save
        EDF_annot : bool
            Flag to generate the event_name with @@channel_label.
        time_elapsed : String of bool
            Flag to add a column with the time elapsed (HH:MM:SS)
        append_data : String of bool
            Flag to append data to file instead of rewriting
    Returns
    -----------   
        None
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('TsvWriter.__init__')
        self._cache_duration = 30 # in seconds
        InputPlug('filename', self)
        InputPlug('events', self)
        InputPlug('EDF_annot', self)
        InputPlug('time_elapsed', self)
        InputPlug('append_data', self)
        InputPlug('add_index', self)
        

    def subscribe_topics(self):
        pass


    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'TsvWriter.on_topic_update {topic}:{message}')


    def compute(self, filename, events, EDF_annot, time_elapsed, append_data, add_index):
        """
        Saves events to a CSV file.
        Parameters
        -----------
            filename : string
                The filename to save to
            events : pandas DataFrame
                The list of events to save
            EDF_annot : bool
                Flag to generate the event_name with @@channel_label.
            time_elapsed : String of bool
                Flag to add a column with the time elapsed (HH:MM:SS)
            append_data : String of bool
                Flag to append data to file instead of rewriting
            add_index : String of bool
                Flag to add the indexes to the file
        Returns
        -----------   
            None
        """
        if DEBUG: print('TsvWriter.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None      
    
        # Log message for the Logs tab
        self._log_manager.log(self.identifier, f"{filename} in process...")            

        # It is important to make a copy otherwise other instance of events
        # will also be modified.
        if isinstance(events,pd.DataFrame):
            events_to_write = events.copy()
        else:
            events_to_write = ''

        if not isinstance(time_elapsed, bool):
            time_elapsed = bool(int(time_elapsed))
            
        if not isinstance(EDF_annot, bool):
            EDF_annot = bool(int(EDF_annot))

        if not isinstance(append_data, bool):
            append_data = bool(int(append_data))

        if isinstance(events_to_write,pd.DataFrame):# and events_to_write.size > 0:
            # If a filename isn't given directly as an argument of the module
            # use the filename received from the pubsubManager for the input file.
            if (events_to_write.size > 0) and time_elapsed:
                time_elapsed_df = pd.DataFrame()
                # Compute the time elapsed for each event
                time_elapsed_df["HH"] = (np.floor(events_to_write.start_sec/3600)).astype(int)
                time_elapsed_df["MM"] = ( np.floor( (events_to_write.start_sec-time_elapsed_df["HH"]*3600) / 60 )).astype(int)
                time_elapsed_df["SS"] = events_to_write.start_sec-time_elapsed_df["HH"]*3600 - time_elapsed_df["MM"]*60

                # concatenate the time as HH:MM:SS and add it to the events dataframe
                events_to_write['time elapsed(HH:MM:SS)'] = time_elapsed_df.HH.apply(str)\
                        + ':' + time_elapsed_df.MM.apply(str) + ':' + time_elapsed_df.SS.apply(str)

            # To write specific channel event in the EDF+ format
            # event_name = event_name@@channel_label ex) spindle@@EEG C3
            if (events_to_write.size > 0) and EDF_annot:
                event_name_all = []
                for index, event in events_to_write.iterrows():
                    current_chan = event["channels"]
                    if len(current_chan)>0:
                        event["name"] = event["name"]+"@@"+current_chan
                    event_name_all.append(event["name"])
                events_to_write["name"] = event_name_all

            if 'channels' in events.columns:
                # Convert the single channel (string) into a list of channels for each event in the events dataframe.
                events_to_write = manage_events.convert_single_chan_string_to_list(events_to_write)

            # Define writing mode
            if append_data:
                mode = 'a'      # Append mode
            else:
                mode = 'w'      # Write mode

            # Define header according to parameters
            if os.path.exists(filename) and mode == 'a':
                header = None
            else:
                header = events.columns.values.tolist()

                if time_elapsed:
                    header.append('time elapsed(HH:MM:SS)')
            
            # Sort events based on the start_sec
            if (mode=='w') and ('start_sec' in events_to_write.columns):
                events_to_write.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')    

            # To write the csv file
            if filename is not None and filename != '':
                try:
                    events_to_write.to_csv(filename, sep='\t', index=eval(add_index), \
                        header=header, mode=mode)
                except :
                    error_message = f"Snooz can not write in the file {filename}."+\
                        f" Check if the drive is accessible and ensure the file is not already open."
                    raise NodeRuntimeException(self.identifier, "TsvWriter", error_message)  

            # Write the cache
            cache = {}
            cache['events'] = events_to_write
            self._cache_manager.write_mem_cache(self.identifier, cache)
            
        else:
            err_message = "ERROR: no events"
            self._log_manager.log(self.identifier, err_message)                
            
