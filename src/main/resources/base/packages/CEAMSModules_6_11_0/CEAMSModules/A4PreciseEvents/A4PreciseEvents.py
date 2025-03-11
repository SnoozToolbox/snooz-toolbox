"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    A4PreciseEvents
    Class dedicated to the a4 spindle detector.
    The class precise the onset and the duration of each event by computing more precisely the RMS value.

    - The originally detected spindle duration is set according to the sliding 
    windows used to compute the RMS value (i.e. 0.25 sec)
    - To precise the event, the RMS value is computed again from 0.5 sec before 
    to 0.5 sec after each spindle.
    - The new RMS windows is a sliding window sample per sample with a duration of 0.25 sec.
    - The spindle limits (onset and end) are stretched until the RMS value of
     the evaluated sample goes below the threshold.
    - The threshold is the same as the one used originnaly.

"""
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from flowpipe.ActivationState import ActivationState
from flowpipe import SciNode, InputPlug, OutputPlug
from CEAMSModules.PSGReader.SignalModel import SignalModel

import numpy as np
import pandas as pd

DEBUG = False

class A4PreciseEvents(SciNode):
    """
    Precise the A4 spindle events.

    Parameters
    -----------
        "signals": a list of SignalModel
            signal.samples : The actual signal data as numpy list
            signal.sample_rate : sampling rate of the signal (used to STFT)
            signal.channel : current channel label    
        "events":  Pandas DataFrame
            DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])   
            A4 Events detected with a windows length and windows step = 0.25 sec
        threshold_events : list of float
            A threshold value for each event nammed "event_name" from this current detector
        "win_len_sec": Float
            The window length in seconds used to compute the RMS value.
        "len_adjust_sec": Float
            The window length in seconds to evaluate before and after each event in order to precise the event.
        "min_len_sec" : float
            The accepted minimum length in sec (any spindle shorter are discarded)
        "max_len_sec" : float
            The accepted maximum length in sec (any spindle longer are discarded)
        "event_group" : string
            The event group to limit the length and precise the onset and duration.
            All the events are selected when event_group is empty.                
        "event_name" : string
            The event name to limit the length and precise the onset and duration.
            All the events are selected when event_name is empty.

    Returns
    -----------
        "events": Pandas DataFrame
            DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])
            New events with precise onset and duration.      
        
    """
    def __init__(self, **kwargs):
        """ Initialize module A4PreciseEvents """
        super().__init__(**kwargs)
        if DEBUG: print('A4PreciseEvents.__init__')

        # Input plugs
        InputPlug('signals',self)
        InputPlug('events',self)
        InputPlug('threshold_events',self)
        InputPlug('win_len_sec',self)
        InputPlug('len_adjust_sec',self)
        InputPlug('min_len_sec',self)
        InputPlug('max_len_sec',self)
        InputPlug('event_group',self)
        InputPlug('event_name',self)
        
        # Output plugs
        OutputPlug('events',self)

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, signals,events,threshold_events,win_len_sec,len_adjust_sec, min_len_sec,max_len_sec,event_group,event_name):
        """
        Precise the A4 spindle events.

        Parameters
        -----------
            "signals": a list of SignalModel
                signal.samples : The actual signal data as numpy list
                signal.sample_rate : sampling rate of the signal (used to STFT)
                signal.channel : current channel label    
            "events":  Pandas DataFrame
                DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])   
                A4 Events detected with a windows length and windows step = 0.25 sec
            threshold_events : list of float
                A threshold value for each event nammed "event_name" from this current detector
            "win_len_sec": Float
                The window length in seconds used to compute the RMS value.
            "len_adjust_sec": Float
                The window length in seconds to evaluate before and after each event in order to precise the event.
            "min_len_sec" : float
                The accepted minimum length in sec (any spindle shorter are discarded)
            "max_len_sec" : float
                The accepted maximum length in sec (any spindle longer are discarded)
            "event_group" : string
                The event group to limit the length and precise the onset and duration.
                All the events are selected when event_group is empty.                
            "event_name" : string
                The event name to limit the length and precise the onset and duration.
                All the events are selected when event_name is empty.

        Returns
        -----------
            "events": Pandas DataFrame
                DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])
                New events with precise onset and duration.      
            
        """

        if not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", \
                f"A4PreciseEvents input of wrong type. Expected: <class 'list'> received: {type(signals)}")

        if not isinstance(events,pd.DataFrame):
            raise NodeInputException(self.identifier, "events", \
                f"A4PreciseEvents input of wrong type. Expected: <class 'DataFrame'> received: {type(events)}")
        
        # It is possible to bypass the A4 Precise Events plugin by passing 
        # the input events directly to the output envents with the limitation on the length only
        if self.activation_state == ActivationState.BYPASS:
            # Write to the cache to use the data in the resultTab
            cache = {}
            cache['events'] = events
            self._cache_manager.write_mem_cache(self.identifier, cache)
            return {
                'events': events
            }

        precise_events = events # Spindle events to precise
        events_to_keep = events # Other events to keep aside and append at the end

        min_len_sec = float(min_len_sec)
        max_len_sec = float(max_len_sec)

        # Events selection
        if len(event_group)>0 and len(event_name)>0:
            # Store events to keep intact
            events_to_keep = events_to_keep.drop(events_to_keep[ \
                events_to_keep['group'].str.contains(event_group,regex=False) & \
                    events_to_keep['name'].str.contains(event_name,regex=False)].index)
            # Filter events based on their name
            precise_events = precise_events[\
                precise_events['group'].str.contains(event_group,regex=False) &\
                     precise_events['name'].str.contains(event_name,regex=False)]

        if not isinstance(threshold_events,list):
            raise NodeInputException(self.identifier, "threshold_events", \
                f"A4PreciseEvents input of wrong type. Expected: <class 'list'> received: {type(threshold_events)}")
        
        win_len_sec = float(win_len_sec)
        len_adjust_sec = float(len_adjust_sec)

        # Extract the properties from the signals
        start_time_signal = SignalModel.get_attribute(signals, 'start_time', 'start_time').flatten()
        end_time_signal = SignalModel.get_attribute(signals, 'end_time', 'start_time').flatten()
        channel_signal = SignalModel.get_attribute(signals, 'channel', 'start_time').flatten()
        # For each spindle
        for index, row in precise_events.iterrows():
            # Extract the NREM bout where the spindle has been detected
            valid_start = start_time_signal <= (row.start_sec+row.duration_sec) 
            valid_end = end_time_signal>=row.start_sec
            valid_chan = channel_signal==row['channels']
            intersection = ((valid_start & valid_end) & valid_chan)
            intersection = intersection.flatten()
            sel_i = np.where(intersection)[0]
            if len(sel_i)>1:
                raise NodeRuntimeException(self.identifier, "events", \
                    f"A4PreciseEvents : spindle found in more than one signal")
            
            # Extract threshold of the first bout
            threshold_value = threshold_events[sel_i[0]]
            # Extract the bout
            signal_chan_start = signals[sel_i[0]]
            fs = signal_chan_start.sample_rate
            nsample_win = win_len_sec*fs
            if not nsample_win.is_integer() and index==0:
                # Compute the real win_len used to compute the RMS
                err_message = f' Warning : win_len_sec {win_len_sec} is changed for {int(round(nsample_win))/fs}'
                self._log_manager.log(self.identifier, err_message)               
            win_len_sec = int(round(nsample_win))/fs
            nsample_win = int(round(win_len_sec*fs))   

            # Compute the start and stop index of the signal to compute the RMS 
            n_start_sec = row['start_sec']-signal_chan_start.start_time # n sec offset for the spindle onset in the bout
            event_start_i = int(round( (n_start_sec) * fs)) # event start index in the bout
            if n_start_sec>len_adjust_sec:
                min_limit_smp = int(round( (n_start_sec-len_adjust_sec) * fs))
            else:
                min_limit_smp = 0
            # Adjust the onset of the window to compute the RMS
            offset_start_smp = 1 # variable to increment sample by sample
            start_RMS_win_i = event_start_i-int(round(nsample_win/2)) # The RMS window is centered around the sample to evaluate
            stop_RMS_win_i = event_start_i+int(round(nsample_win/2)) # The RMS window is centered around the sample to evaluate
            # The windows is moved left for each iteration (to move the possible onset of the spindle)
            event_window_cur = signal_chan_start.samples[start_RMS_win_i-offset_start_smp:stop_RMS_win_i-offset_start_smp]
            RMS_cur_win = np.sqrt(np.mean(np.power(event_window_cur, 2)))
            while (RMS_cur_win >= threshold_value) and (event_start_i-offset_start_smp >= min_limit_smp):
                precise_events.at[index,'start_sec'] = (event_start_i-offset_start_smp)/fs + signal_chan_start.start_time
                offset_start_smp = offset_start_smp + 1
                event_window_cur = signal_chan_start.samples[start_RMS_win_i-offset_start_smp:stop_RMS_win_i-offset_start_smp]
                RMS_cur_win = np.sqrt(np.mean(np.power(event_window_cur, 2)))
            
            # Adjust the end of the window to compute the RMS
            signal_end_sec = signal_chan_start.start_time+signal_chan_start.duration
            event_end_sec = row['start_sec']+row['duration_sec'] # End of the spindle
            n_sec_after_event = signal_end_sec-event_end_sec  # n sec available inthe bout after the end of the spindle 
            if n_sec_after_event>len_adjust_sec:
                max_limit_smp = int(round((event_end_sec-signal_chan_start.start_time+len_adjust_sec) * fs))
            else:
                max_limit_smp = len(signal_chan_start.samples)    
            event_stop_i = int(round( (event_end_sec-signal_chan_start.start_time) * fs)) # event stop index in the bout
            offset_end_smp = 1  # variable to increment sample by sample
            start_RMS_win_i = event_stop_i-int(round(nsample_win/2)) # The RMS window is centered around the sample to evaluate
            stop_RMS_win_i = event_stop_i+int(round(nsample_win/2)) # The RMS window is centered around the sample to evaluate
            # The windows is moved right for each iteration (to move the possible end of the spindle)
            event_window_cur = signal_chan_start.samples[start_RMS_win_i+offset_end_smp:stop_RMS_win_i+offset_end_smp]
            RMS_cur_win = np.sqrt(np.mean(np.power(event_window_cur, 2)))
            while (RMS_cur_win >= threshold_value) and (event_stop_i+offset_end_smp < max_limit_smp):
                precise_duration_smp = (event_stop_i+offset_end_smp)-(event_start_i-offset_start_smp)+1
                precise_events.at[index,'duration_sec'] = precise_duration_smp / fs
                offset_end_smp = offset_end_smp + 1
                event_window_cur = signal_chan_start.samples[start_RMS_win_i+offset_end_smp:stop_RMS_win_i+offset_end_smp]
                RMS_cur_win = np.sqrt(np.mean(np.power(event_window_cur, 2)))
         
        # Filter events  based on their length
        precise_events = precise_events.drop(precise_events[precise_events.duration_sec < min_len_sec].index)
        precise_events = precise_events.drop(precise_events[precise_events.duration_sec > max_len_sec].index)
        # Reset index
        precise_events.reset_index(inplace=True, drop=True)
        # Sort events based on the start_sec
        precise_events.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')            

        # Write to the cache to use the data in the resultTab
        if events is not None:
            cache = {}
            cache['events'] = precise_events
            self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'events': precise_events
        }