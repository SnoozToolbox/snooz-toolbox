#! /usr/bin/env python3

"""
    Read events from a file.
"""
from ast import literal_eval
import numpy as np
import pandas as pd

from flowpipe import SciNode, InputPlug, OutputPlug
from CEAMSModules.EventReader import manage_events
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = False

class EventReader(SciNode):
    """
        Read events from a Tsv file

        Parameters
        -----------
            filename       : string
                The filename to read.
            delimiter      : string 
                Delimiter of the columns.
            nrows_header   : integer
                The number of rows for the header.
            encoding        : string
                The file format encoding, default utf_8.
            group_col_i   : integer
                The column index of the group
            group_def     : string
                Group event definition if group_col_i=0
            name_col_i    : integer
                The column index of the event names
            name_def        : string
                Name event definition if name_col_i=0.
            onset_col_i         : integer
                The column index of the onset of the events (always in elapsed time)
            duration_col_i      : integer
                The column index of the duration of the events
            channels_col_i       : integer
                The column index of the channel of the events
            input_as_time : string
                If "seconds", the content are in time (s)
                if "samples", the content are in samples
                or any valid datetime string format, see https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
                ex) "%H:%M:%S%f" for "14:30:45"
                    "%H%M%S%f" for "14:30:45.123456"
            event_center : Bool
                If 1, the content of the onset is the event center
                if 0, the content of the onset is the event onset
            dur_disable : Bool
                If 1, the duration is disabled
                if 0, the content of duration is valid
            fixed_dur : float
                Valide only when dur_disable=1.  The fixed duration_col_i of all the events.  
            personalized_header : string of int
                '1' to read directly the input filename via read_csv and output the pandas datadrame of the file. 
                '0' to convert the filename into snooz dataframe columns=['group','name','start_sec','duration_sec','channels']

        Returns
        -----------    
            events   : Pandas DataFrame
                List of events
            filename : string
                The input filename is return.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('EventReader.__init__')
        self._filename = None
        InputPlug('filename', self)
        InputPlug('delimiter', self)
        InputPlug('nrows_header', self)
        InputPlug('encoding', self)
        InputPlug('group_col_i', self)
        InputPlug('group_def', self)
        InputPlug('name_col_i', self)
        InputPlug('name_def', self)
        InputPlug('onset_col_i', self)
        InputPlug('duration_col_i', self)
        InputPlug('channels_col_i', self)
        InputPlug('sample_rate', self)
        InputPlug('input_as_time', self)
        InputPlug('event_center', self)
        InputPlug('dur_disable', self)
        InputPlug('fixed_dur', self)    
        InputPlug('personalized_header', self)       
        OutputPlug('events', self)
        OutputPlug('filename', self)


    # The plugin subscribes to the publisher to receive the settings (messages) as input
    def subscribe_topics(self):
        pass


    def compute(self, filename, delimiter, nrows_header, encoding, group_col_i, group_def, name_col_i, name_def, \
        onset_col_i, duration_col_i, channels_col_i, sample_rate, \
        input_as_time, event_center, dur_disable, fixed_dur, personalized_header):
        """
            Read events from a Tsv file

            Parameters
            -----------
                filename       : string 
                    The filename to read.
                delimiter      : string 
                    Delimiter of the columns.
                nrows_header   : integer
                    The number of rows for the header.
                encoding        : string
                    The file format encoding, default utf_8.
                group_col_i   : integer
                    The column index of the group
                group_def     : string
                    Group event definition if group_col_i=0
                name_col_i    : integer
                    The column index of the event names
                name_def        : string
                    Name event definition if name_col_i=0.
                onset_col_i         : integer
                    The column index of the onset of the events
                duration_col_i      : integer
                    The column index of the duration of the event
                channels_col_i       : integer
                    The column index of the channels of the event
                input_as_time : string
                    If "seconds", the content are in time (s)
                    if "samples", the content are in samples
                    or any valid datetime string format, see https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
                    ex) "%H:%M:%S%f" for "14:30:45"
                        "%H%M%S%f" for "14:30:45.123456"
                event_center : Bool
                    If 1, the content of the onset is the event center
                    if 0, the content of the onset is the event onset
                dur_disable : Bool
                    If 1, the duration is disabled
                    if 0, the content of duration is valid
                fixed_dur : float
                    Valide only when dur_disable=1.  The fixed duration of all the events.  

            Returns
            -----------    
                events   : Pandas DataFrame
                    List of events
                filename : string
                    The filename (same as the input).
        """

        if DEBUG: print('EventReader.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None             

        if filename == '':
            filename = self._filename

        if filename is not None:

            try: 
                # Import events into df
                events_pre_process = pd.read_csv(filename, 
                                                    sep=delimiter, 
                                                    header=0,
                                                    engine='python',
                                                    encoding = encoding,
                                                    skiprows=nrows_header,
                                                    skip_blank_lines=True)      
            except:
                raise NodeRuntimeException(self.identifier, "filename", f"Problem with the file {filename}")
            
            if not eval(personalized_header):
                n = len(events_pre_process)
                group = []

                # Check which column is available
                if int(group_col_i) == 0:
                    if len(group_def)>0:
                        group = [group_def for i in range(n)]
                    else:
                        group = ['n/a' for i in range(n)]
                else:
                    group = np.hstack(events_pre_process.iloc[:,[int(group_col_i) - 1]].values).tolist()
                name = []
                if int(name_col_i) == 0:
                    if len(name_def)>0:
                        name = [name_def for i in range(n)]
                    else:
                        name = ['n/a' for i in range(n)]
                else:
                    name_data = np.hstack(events_pre_process.iloc[:,[int(name_col_i) - 1]].values).tolist()
                    name = [list(new_name.split("@@"))[0] if (isinstance(new_name,str) and '@@' in new_name) else new_name for new_name in name_data]
                channel = [] 
                if int(channels_col_i) == 0:
                    channel = [list(new_chan.split("@@"))[1] if (isinstance(new_chan,str) and '@@' in new_chan) else [] for new_chan in name_data]
                else:
                    channel = events_pre_process.iloc[:,int(channels_col_i) - 1].apply(lambda x: self.convert_to_list(x)).tolist()
                start_sec = []
                if int(onset_col_i) == 0:
                    start_sec = [0 for i in range(n)]
                else:
                    start_sec = np.hstack(events_pre_process.iloc[:,[int(onset_col_i) - 1]].values).tolist()
                duration_sec = []
                if int(duration_col_i) == 0:
                    duration_sec = [0 for i in range(n)]
                else:
                    duration_sec = np.hstack(events_pre_process.iloc[:,[int(duration_col_i) - 1]].values).tolist()
                
                # Create dataframe
                event = list(zip(group, name, start_sec, duration_sec, channel))
                events = manage_events.create_event_dataframe(event) # Convert into a DataFrame

                if not fixed_dur=='':
                        events["duration_sec"] = np.ones(len(events)) * float(fixed_dur)

                # Convert start and duration in sec if not already
                if input_as_time=="samples":
                    # Make sure there is NaN in number columns
                    events['start_sec'] = events['start_sec'].fillna(0)
                    events['duration_sec'] = events['duration_sec'].fillna(0)
                    sample_rate = int(sample_rate)
                    events['start_sec'] = events['start_sec'].apply(lambda x:x/sample_rate)
                    if 'duration_sec' in events:
                        events['duration_sec'] = events['duration_sec'].apply(lambda x:x/sample_rate)
                elif not input_as_time=="seconds":
                    self.input_as_time = input_as_time
                    events['start_sec'] = events['start_sec'].apply(self.convert_to_seconds)
                    if pd.isnull(events['start_sec']).any():
                        error_message = f"Snooz can not read properly {filename}, the start_sec is not defined by the time format {input_as_time}, row {pd.isnull(events['start_sec']).to_numpy().nonzero()[0][0]}"
                        raise NodeRuntimeException(self.identifier, "EventReader", error_message)
                    if 'duration_sec' in events:
                        try : 
                            events['duration_sec'] = events['duration_sec'].apply(self.convert_to_seconds)
                        except : 
                            events['duration_sec'] = events['duration_sec'].fillna(0)
                
                # The event is identified with its center instead of the onset 
                if int(event_center):
                    events['start_sec'] = events['start_sec'] - (events['duration_sec']/2)

                # Clean up lists of channels for a single channel (string) per event
                events = manage_events.convert_event_df_to_single_channel(events)
                # In NATUS/Stellate the annotations can be duplicated
                events.drop_duplicates(inplace=True, ignore_index=True) 
                              
            else:
                events = events_pre_process
                # Event if it is personalized, we look for the columns channels.
                # Plugins in Snooz expect a channels as a string, not a list.
                if 'channels' in events.columns:
                    # Look for lists of channels with more than a single channel
                    channels = events['channels'].values
                    index_many_chans = [i for i, chan_lst in enumerate(channels) if len(eval(chan_lst))>1]
                    # Convert the list of a single channel into a string
                    if len(index_many_chans)>0:
                        err_message = "ERROR: annotations spread on more than one channel is not supported."
                        self._log_manager.log(self.identifier, err_message)
                        raise NodeInputException(self.identifier, "filename", \
                            f"EventReader annotations spread on more than one channel is not supported.")
                    channels_string = [eval(chan_lst)[0] if len(eval(chan_lst))>0 else "" for chan_lst in channels]
                    events['channels'] = channels_string

            if events is not None:
                cache = {}
                cache['events'] = events
                self._cache_manager.write_mem_cache(self.identifier, cache)
                
            return { 
                'events': events,
                'filename':filename
            }
            
        else:
            err_message = "ERROR: filename not initialized"
            self._log_manager.log(self.identifier, err_message)
            print(err_message)    

            return {
                'events': '',
                'filename' : ''
            }


    def convert_to_list(self, x):
        try:
            return literal_eval(x)
        except:
            return [x]


    # Function to convert elapsed time to seconds using pd.to_datetime
    def convert_to_seconds(self, time_str):
        # Parse the time string using pd.to_datetime, specifying the format if known
        if isinstance(time_str,str):
            time_obj = pd.to_datetime(time_str, format=self.input_as_time, errors='coerce')
        
            # Convert to total seconds
            if not pd.isnull(time_obj):
                seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
                return float(seconds)
            else:
                return np.nan
        else:
            return np.nan