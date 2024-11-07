#! /usr/bin/env python3

"""
    Read events from a file.

    All index starts at 1.

    Parameters
    -----------
        filename       : string 
            The filename to read.
        delimiter      : string 
            Delimiter of the columns.
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
            The column index of the duration of the events
        channels_col_i       : integer
            The column index of the channel of the events
        input_as_time : Bool
            If 1, the content of the column are in time (s)
            if 0, the content are in samples
        event_center : Bool
            If 1, the content of the onset is the event center
            if 0, the content of the onset is the event onset
        dur_disable : Bool
            If 1, the duration is disabled
            if 0, the content of duration is valid
        fixed_dur : float
            Valide only when dur_disable=1.  The fixed duration of all the events.  
        personalized_header : string of int
            '1' to read directly the input filename via read_csv and output the pandas datadrame of the file. 
            '0' to convert the filename into snooz dataframe columns=['group','name','start_sec','duration_sec','channels']

    Returns
    -----------    
        events   : Pandas DataFrame
            List of events (columns=['group','name','start_sec','duration_sec','channels'])
        filename : string
            The filename read.

"""
from ast import literal_eval
import numpy as np
import pandas as pd

from flowpipe import SciNode, InputPlug, OutputPlug
from CEAMSModules.EventReader import manage_events
from commons.NodeInputException import NodeInputException

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
                The column index of the duration of the events
            channels_col_i       : integer
                The column index of the channel of the events
            input_as_time : Bool
                If 1, the content of the column are in time (s)
                if 0, the content are in samples
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


    def compute(self, filename, delimiter, group_col_i, group_def, name_col_i, name_def, \
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
                group_def     : string
                    Group event definition if group_col_i=0
                name_col_i    : integer
                    The column index of the event names
                name_def        : string
                    Name event definition if name_col_i=0.
                onset_col_i         : integer
                    The column index of the onset of the events
                onset_col_i         : integer
                    The column index of the onset of the event
                duration_col_i      : integer
                    The column index of the duration of the event
                channels_col_i       : integer
                    The column index of the channels of the event
                input_as_time : Bool
                    If 1, the content of the column are in time (s)
                    if 0, the content are in samples
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

            # Import events into df
            events_pre_process = pd.read_csv(filename, 
                                                sep=delimiter, 
                                                header=0,
                                                engine='python',
                                                encoding = 'utf_8')      
            
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
                    channel = [list(new_chan.split("@@"))[1] if (isinstance(new_chan,str) and '@@' in new_chan) else '[]' for new_chan in name_data]
                else:
                    events_pre_process['channels'] = (events_pre_process['channels'].apply(literal_eval))
                    channel = np.hstack(events_pre_process.iloc[:,[int(channels_col_i) - 1]].values).tolist()
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

                # Make sure there is NaN in number columns
                events['start_sec'] = events['start_sec'].fillna(0)
                events['duration_sec'] = events['duration_sec'].fillna(0)

                if not fixed_dur=='':
                        events["duration_sec"] = np.ones(len(events)) * float(fixed_dur)

                # Convert start and duration in sec if not already
                if not int(input_as_time):
                    sample_rate = int(sample_rate)
                    events['start_sec'] = events['start_sec'].apply(lambda x:x/sample_rate)
                    if 'duration_sec' in events:
                        events['duration_sec'] = events['duration_sec'].apply(lambda x:x/sample_rate)

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
