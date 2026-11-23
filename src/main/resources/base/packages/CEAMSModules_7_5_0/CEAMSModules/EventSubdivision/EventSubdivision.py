"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    Create a new pandas DataFrame of events with subwindow of every input events named events_names.

    Parameters
    -----------
        events: pandas DataFrame
            df of events with field
                group: Group of events this event is part of (String)
                name: Name of the event (String)
                start_sec: Starting time of the event in sec (Float)
                duration_sec: Duration of the event in sec (Float)
                channels: Channel where the event occures (String)
        events_names: String
            String of the desired events to take in account. Separated by a 
            comma. ex)'stage_2' or ex)'stage_1,stage2,stage3'
        window_sec: Integer
            Duration of new subwindow in second. Must be a dividers of previous
            events.
        n_window: Integer [Optionnal]
            Number of windows in one window.
        filename: String
            The filename of the input recording.

    Returns
    -----------    
        new_events: pandas DataFrame
            df of events with field :
                group: Group of events this event is part of (String)
                name: Name of the event (String)
                start_sec: Starting time of the event in sec (Float)
                duration_sec: Duration of the event in sec (Float)
                channels: Channel where the event occures (String)
            New event name will be name_sub

"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import os
import pandas as pd
import numpy as np

DEBUG = False

class EventSubdivision(SciNode):
    """
    Create a new pandas DataFrame of events with subwindow of every input events named events_names.

        Parameters
        -----------
            events: pandas DataFrame
                df of events with field
                group: Group of events this event is part of (String)
                name: Name of the event (String)
                start_sec: Starting time of the event in sec (Float)
                duration_sec: Duration of the event in sec (Float)
                channels: Channel where the event occures (String)
            events_names: String
                String of the desired events to take in account. Separated by a 
                comma. ex)'stage_2' or ex)'stage_1,stage2,stage3'
            window_sec: Integer
                Duration of new subwindow in second. Must be a dividers of previous
                events.
            n_window: Integer [Optionnal]
                Number of windows in one window.
            filename: String
                The filename of the input recording.

        Returns
        -----------    
            new_events: pandas DataFrame
                df of events with field :
                    group: Group of events this event is part of (String)
                    name: Name of the event (String)
                    start_sec: Starting time of the event in sec (Float)
                    duration_sec: Duration of the event in sec (Float)
                    channels: Channel where the event occures (String)
                New event name will be name_sub
    """
    def __init__(self, **kwargs):
        """ Initialize module EventSubdivision """
        super().__init__(**kwargs)
        if DEBUG: print('SleepReport.__init__')

        # Input plugs
        InputPlug('events',self)
        InputPlug('events_names',self)
        InputPlug('window_sec',self)
        InputPlug('n_window',self)
        InputPlug('filename',self)
        

        # Output plugs
        OutputPlug('new_events',self)
        
        self._is_master = False 

    def _raise_if_no_matching_events(self, duration_times, df, events_names, filename):
        """Raise a runtime error when no events match events_names for the current recording."""
        if len(duration_times) == 0 or len(df) == 0:
            recording_label = os.path.basename(filename) if isinstance(filename, str) and filename.strip() else "the current recording"
            err_message = (
                f"No events matching events_names '{events_names}' were found for {recording_label}. "
                f"Meaning no annotation file was provided for this recording."
            )
            self._log_manager.log(self.identifier, err_message)
            raise NodeRuntimeException(self.identifier, "events_names", err_message)
    
    def compute(self, events,events_names,window_sec,n_window,filename=''):
        """
        Create a new pandas DataFrame of events with subwindow of every input events named events_names.

            Parameters
            -----------
                events: pandas DataFrame
                    df of events with field
                    group: Group of events this event is part of (String)
                    name: Name of the event (String)
                    start_sec: Starting time of the event in sec (Float)
                    duration_sec: Duration of the event in sec (Float)
                    channels: Channel where the event occures (String)
                events_names: String
                    String of the desired events to take in account. Separated by a 
                    comma. ex)'stage_2' or ex)'stage_1,stage2,stage3'
                window_sec: Integer
                    Duration of new subwindow in second. Must be a dividers of previous
                    events.
                n_window: Integer [Optionnal]
                    Number of windows in one window.
                filename: String
                    The filename of the input recording.

            Returns
            -----------    
                new_events: pandas DataFrame
                    df of events with field :
                        group: Group of events this event is part of (String)
                        name: Name of the event (String)
                        start_sec: Starting time of the event in sec (Float)
                        duration_sec: Duration of the event in sec (Float)
                        channels: Channel where the event occures (String)
                    New event name will be name_sub
        """

        self.clear_cache() # It  makes the cache=None             

        # Verify inputs
        if isinstance(events, str) and events == '':
            err_message = "ERROR: events not connected"
            self._log_manager.log(self.identifier, err_message)
            print('EventSubdivision:' + err_message)
            return {'new_events': ''}

        if not isinstance(events, pd.DataFrame):
            err_message = "ERROR: events is not a panda dataFrame"
            self._log_manager.log(self.identifier, err_message)
            print('EventSubdivision:' + err_message)
            return {'new_events': ''}

        # split list to check on the desired events
        event_name = list(events_names.split(","))
        new_events = events.copy()

        # Check if window_sec is set to 0 in case no subdivision is done
        # More useful in EOG rejection preset not to have 2 presets in case 
        # user don't want to subdivise window
        if window_sec == 0:
            if (events_names == ''):
                new_events['name'] = new_events['name'].values + '_sub'
            else:
                # Making having same format as a usual subdivision so I keep
                # last df append with new EventName_sub
                new_events = new_events.loc[new_events['name'].isin(event_name)].reset_index(drop=True)
                self._raise_if_no_matching_events(
                    new_events['duration_sec'].to_numpy(), new_events, events_names, filename)
                df = events.loc[events['name'].isin(event_name)].reset_index(drop=True).copy()
                df['name'] = df['name'].values + '_sub'
                new_events = pd.concat([new_events,df])
                new_events = new_events.sort_values('start_sec', axis=0, ascending=True, ignore_index=True)
            return {'new_events': new_events}

        # Transform to samples
        if (events_names == ''):
            duration_times = pd.to_numeric(events['duration_sec'], errors='coerce').to_numpy(dtype=float)
            df = events.copy()
        else:
            duration_times = pd.to_numeric(events.loc[events['name'].isin(event_name), 'duration_sec'], errors='coerce').to_numpy(dtype=float)
            df = events.loc[events['name'].isin(event_name)].reset_index(drop=True).copy()
            new_events = events.loc[events['name'].isin(event_name)].reset_index(drop=True).copy()
            self._raise_if_no_matching_events(duration_times, df, events_names, filename)

        # Ignore tiny floating-point residues such as 29.99345 when the
        # duration is effectively meant to be a whole number of seconds.
        if np.isnan(duration_times).any():
            err_message = "ERROR: duration_sec contains non-numeric values"
            self._log_manager.log(self.identifier, err_message)
            print('EventSubdivision:' + err_message)
            return {'new_events': ''}
        duration_times = np.round(duration_times).astype(int)
        
        if int(n_window)<= 1:
            # Check if window_sec is a divider of windows lenght
            is_dividable = np.mod(duration_times, window_sec) == 0
            event_not_int = np.where(is_dividable == False)

            # Warning about event who does divide perfectly
            if not is_dividable.all():
                err_message = "WARNING: " + events_names + ' have event of ' + str(duration_times[event_not_int[0]].astype(str)[0]) \
                    + " seconds which is not dividable by " + str(window_sec) + " and will not be subdivised."
                self._log_manager.log(self.identifier, err_message)
                print('EventSubdivision:' + err_message)
            
            # Remove row with duration not divisible
            duration_times = np.delete(duration_times, event_not_int[0])
            df = df.drop(event_not_int[0])

            # Create new events
            divider = (duration_times / window_sec).astype(int)
            df = pd.DataFrame(np.repeat(df.values, divider, axis=0), columns=df.columns)
            df['name'] = df['name'].values + '_sub'
            df['duration_sec'] = window_sec
            add_time = np.hstack([np.arange(0,n,window_sec) for n in duration_times])
            df['start_sec'] = df['start_sec'].values + add_time

            # Add new events to existing df
            #new_events = pd.concat([new_events,df])
            new_events = df
            new_events = new_events.sort_values('start_sec', axis=0, ascending=True, ignore_index=True)
        else:
            # Check time between windows
            is_dividable = (n_window * window_sec - duration_times)/(n_window-1) >= 0
            event_not_int = np.where(is_dividable == False)

            # Warning about event who does divide perfectly
            if not is_dividable.all():
                err_message = "WARNING: events number: " + ", ".join(event_not_int[0].astype(str)) \
                    + " does not have enough windows/lenght to fill entire event and will not be subdivised."
                self._log_manager.log(self.identifier, err_message)
                print('EventSubdivision:' + err_message)

             # Remove row with duration not divisible
            duration_times = np.delete(duration_times, event_not_int[0])
            df = df.drop(event_not_int[0])

            # Create new events
            df = pd.DataFrame(np.repeat(df.values, n_window, axis=0), columns=df.columns)
            df['name'] = df['name'].values + '_sub'
            df['duration_sec'] = window_sec
            add_time = np.hstack([np.linspace(0,n-window_sec,n_window) for n in duration_times])
            df['start_sec'] = df['start_sec'].values + add_time

            # Add new events to existing df
            #new_events = pd.concat([new_events,df])
            new_events = df
            new_events = new_events.sort_values('start_sec', axis=0, ascending=True, ignore_index=True)

        if new_events is not None:
            cache = {}
            cache['events'] = new_events
            self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'new_events': new_events
        }