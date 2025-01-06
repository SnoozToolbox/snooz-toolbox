"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Read events from a CSV file.  Can read many files in a loop (master node).
    All index starts at 1.

    Parameters
    -----------
        files         : List of string 
            The files to read
        file_separator : string
            The file separator as '\t' or ','.
        group_col_i   : integer
            The column index of the group
        name_col_i    : integer
            The column index of the event names
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
        fixed_dur : float
            Valid only when duration_col_i=0.  The fixed duration of all the events.  
        personnalized_header    : bool
            True to output the header of the event passed in parameters. False to
            ouput a default header (columns=['group','name','start_sec','duration_sec','channels'])

    Returns
    -----------    
        events   : Pandas DataFrame
            List of events (columns=['group','name','start_sec','duration_sec','channels'])     
            OR list of events with personalized columns
        filename : String
            Last filename read (or current filename)
"""
from ast import literal_eval
import numpy as np
import pandas as pd

from flowpipe import SciNode, InputPlug, OutputPlug

from CEAMSModules.EventReader import manage_events
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = False

class CsvReaderMaster(SciNode):
    """
        Read events from a CSV file.
        All index starts at 1.

        Parameters
        -----------
            files         : List of string 
                The files to read
            file_separator : string
                The file separator as '\t' or ','.
            group_col_i   : integer
                The column index of the group
            name_col_i    : integer
                The column index of the event names
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
            fixed_dur : float
                Valide only when duration_col_i==0.  The fixed duration of all the events.  
            personnalized_header    : bool
                True to output the header of the event passed in parameters. False to
                ouput a default header (columns=['group','name','start_sec','duration_sec','channels'])

        Returns
        -----------    
            events   : Pandas DataFrame
                List of events (columns=['group','name','start_sec','duration_sec','channels'])     
                OR list of events with personalized columns
            filename : String
                Last filename read (or current filename)
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('CsvReaderMaster.__init__')
        # The iteration over a list of files is not complete yet
        self.is_done = False
        # Allow iteration over a list of files
        self.is_master = True
        InputPlug('files', self)
        InputPlug('file_separator', self)
        InputPlug('group_col_i', self)
        InputPlug('name_col_i', self)
        InputPlug('onset_col_i', self)
        InputPlug('duration_col_i', self)
        InputPlug('channels_col_i', self)
        InputPlug('sample_rate', self)
        InputPlug('input_as_time', self)
        InputPlug('event_center', self)
        InputPlug('fixed_dur', self)   
        InputPlug('personnalized_header', self)   
        OutputPlug('events', self)
        OutputPlug('filename', self)


    # The plugin subscribes to the publisher to receive the settings (messages) as input
    def subscribe_topics(self):
        pass

    def compute(self, files, file_separator, group_col_i, name_col_i, onset_col_i, duration_col_i,\
         channels_col_i, sample_rate, input_as_time, event_center, fixed_dur,\
        personnalized_header):
        """
            Read events from a CSV file.
            All index starts at 1.

            Parameters
            -----------
                files         : List of string 
                    The files to read
                file_separator : string
                    The file separator as '\t' or ','.
                group_col_i   : integer
                    The column index of the group
                name_col_i    : integer
                    The column index of the event names
                onset_col_i         : integer
                    The column index of the onset of the events
                duration_col_i      : integer
                    The column index of the duration of the events
                channels_col_i       : integer
                    The column index of the channel of the events
                    The column index of the channel of the events
                input_as_time : Bool
                    If 1, the content of the column are in time (s)
                    if 0, the content are in samples
                event_center : Bool
                    If 1, the content of the onset is the event center
                    if 0, the content of the onset is the event onset
                fixed_dur : float
                    Valide only when duration_col_i=0.  The fixed duration of all the events. 
                personnalized_header    : bool
                    True to output the header of the event passed in parameters. False to
                    ouput a default header (columns=['group','name','start_sec','duration_sec','channels'])

            Returns
            -----------    
                events   : Pandas DataFrame
                    List of events (columns=['group','name','start_sec','duration_sec','channels'])     
                    OR list of events with personalized columns
                filename : String
                    Last filename read (or current filename)
        """
        if DEBUG: print('CsvReaderMaster.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None           

        self.default_col_name = manage_events.create_event_dataframe(None).columns

        if files == '' or files is None or len(files) == 0:
            raise NodeInputException(self.identifier, "files", \
                "CsvReaderMaster files parameter must be set.")

        # Get the next filename
        filename = files[self._iteration_counter]

        # Set the iteration_identifier in case there is a problem during the process.
        # This will be used to identify the problematic file.
        self.iteration_identifier = filename

        # Check if done
        if self._iteration_counter + 1 >= len(files):
            self.is_done = True

        group_col_i = int(group_col_i)
        name_col_i = int(name_col_i)
        onset_col_i = int(onset_col_i)
        duration_col_i = int(duration_col_i)
        channels_col_i = int(channels_col_i)

        if filename is not None:
            try :

                if eval(personnalized_header):
                    names = None
                    usecols = None
                else:
                    usecols = []
                    names = []
                    for col_name in self.default_col_name:
                        if col_name == 'group' and group_col_i>0:
                            usecols.append(group_col_i-1)
                            names.append(col_name)
                        elif col_name == 'name':
                            if name_col_i==0:
                                raise NodeInputException(self.identifier, "name_col_i", "CsvReaderMaster column for event name is mandatory.")
                            else:
                                usecols.append(name_col_i-1)
                                names.append(col_name)     
                        elif col_name == 'start_sec':
                            if onset_col_i==0:
                                raise NodeInputException(self.identifier, "onset_col_i", "CsvReaderMaster column for event onset is mandatory.")
                            else:
                                usecols.append(onset_col_i-1)
                                names.append(col_name)
                        elif col_name == 'duration_sec' and duration_col_i>0:
                            usecols.append(duration_col_i-1)
                            names.append(col_name)
                        elif col_name == 'channels' and channels_col_i>0:
                            usecols.append(channels_col_i-1)
                            names.append(col_name)

                index_order = np.argsort(np.array(usecols))
                names_ordered = [names[index] for index in index_order]
                events = pd.read_csv(filename, sep=file_separator, usecols=usecols, \
                                    header=0, encoding='utf_8', names=names_ordered)
                events = events[names]
                
                if not eval(personnalized_header) and duration_col_i==0:
                    # Case with a fixed duration for all the events                  
                    if not fixed_dur=='':
                        events["duration_sec"] = np.ones(len(events)) * float(fixed_dur)
                    else:
                        events["duration_sec"] = np.zeros(len(events))

                    # Reorder the colonne index as expected
                    events = events[self.default_col_name]

                # EdfReader is expecting {group:str, name:str, start_sec:float, duration_sec:float}
                # Some duration can be empty when there is no duration, we have to change the empty for 0
                events['duration_sec']=events['duration_sec'].replace('',0).astype(float)
                events['duration_sec']=events['duration_sec'].fillna(0)

                # Convert start and duration in sec if not already
                if not eval(personnalized_header) and not int(input_as_time) :
                    sample_rate = int(sample_rate)
                    events.start_sec = events.start_sec.apply(lambda x:x/sample_rate)
                    if 'duration_sec' in events:
                        events.duration_sec = events.duration_sec.apply(lambda x:x/sample_rate)

                # The event is identified with its center instead of the onset 
                if not eval(personnalized_header) and int(event_center):
                    if 'duration_sec' in events:
                        events.start_sec = events.start_sec-(events.duration_sec/2)

                # name is mandatory
                name_data = np.hstack(events['name'].values).tolist()
                name = [list(new_name.split("@@"))[0] if (isinstance(new_name,str) and '@@' in new_name) else new_name for new_name in name_data]
                # Really important to avoid self._annotations.loc[:]['name']
                #   They data may be not modified
                events.loc[:,'name'] = name

                if int(channels_col_i)==0:
                    channel = [list(new_name.split("@@"))[1] if (isinstance(new_name,str) and '@@' in new_name) else "" for new_name in name_data]
                    if not ('channels' in events):
                        events['channels'] = channel
                    else:
                        # Really important to avoid self._annotations.loc[:]['name']
                        #   They data may be not modified                        
                        events.loc[:,'channels'] = channel
                else:
                    events['channels'] = (events['channels'].apply(literal_eval))   

                if group_col_i>0:
                    # Clean up lists of channels for a single channel (string) per event
                    events = self.convert_event_df_to_single_channel(events)

                # In NATUS/Stellate the annotations can be duplicated
                events.drop_duplicates(inplace=True, ignore_index=True) 

                if events is not None:
                    cache = {}
                    cache['events'] = events
                    self._cache_manager.write_mem_cache(self.identifier, cache)

                # Update progression information
                self.iteration_count = len(files)

                return {
                    'events': events,
                    'filename' : filename
                }
            
            except Exception as e:
                err_message = "ERROR: {} not read. {}".format(filename, e)
                self._log_manager.log(self.identifier, err_message)

                raise NodeRuntimeException(self.identifier, "files", err_message)

        else:
            err_message = "ERROR: filename not initialized"
            self._log_manager.log(self.identifier, err_message)
            
            raise NodeRuntimeException(self.identifier, "files", err_message)


    def convert_event_df_to_single_channel(self, events1):
        """
            Clean up lists of channels for a single channel
            Duplicate events with more than one channels
            Events without channel are skipped

            Parameters:
                events1 : pandas DataFrame with columns : group, name, start_sec, duration_sec, channels
                List of events. An event can be spread on many channels.

            Return:
                event_df_single_chan : pandas DataFrame with columns : group, name, start_sec, duration_sec, channels
                List of events with a single channel in the column "channels"

        """
        # Look for lists of channels with more than a single channel
        channels = events1['channels'].values
        index_many_chans = [i for i, chan_lst in enumerate(channels) if len(chan_lst)>1]
        
        # Convert the list of a single channel into a string
        if len(index_many_chans)>0:
            events1_single = events1.drop(index_many_chans)
            channels = events1_single['channels'].values
        else:
            events1_single = events1
        channels_string = [chan_lst[0] if len(chan_lst)>0 else "" for chan_lst in channels]
        events1_single.loc[:,'channels'] = channels_string

        # Duplicate events spread on more than one channels
        if len(index_many_chans)>0:
            events1_many = events1.iloc[index_many_chans]
            single_chan_events1 = []
            for index, event in events1_many.iterrows():
                if len(event.channels)>0:
                    for i_chan in range(len(event.channels)):
                        single_chan_events1.append([event['group'],event['name'],event['start_sec'], event['duration_sec'], event.channels[i_chan]])
            event_df_single_chan = pd.DataFrame(data=single_chan_events1,columns=['group','name','start_sec','duration_sec','channels'])
            events1_single = pd.concat([events1_single,event_df_single_chan])
        return events1_single    