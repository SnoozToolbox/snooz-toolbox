"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    This plugin detects events based on the absolute signal amplitude.
    The plugin is flexible, an event can be detected when activity goes above 
    or below the threshold.  The threshold can be fixed or adaptive based on 
    a baseline window around the event.  The adaptive threshold can be x times 
    the baseline median value or x times the standard deviation of the baseline.
    When a z-score is used as threshold (x BSL STD), the absolute signal 
    amplitude can be log10 transformed to make them more normally distributed.

    Parameters
    -----------
        signals    : a list of SignalModel
            signal.samples : The actual signal data as numpy list
            signal.sample_rate : sampling rate of the signal (used to STFT)
            signal.channel : current channel label               
        event_name : string, event label.
        pad_sec : string
            The padding event (length in second) to add to the beginning and 
            the end of the originally detected event.
        threshold_val : string or a list of float
            String : the value to threshold to detect events.
            list : the value to threshold for each signal included in signals.
        threshold_unit : string
            The threshold unit (fixed, x BSL median, x BSL STD or x BSL STD(log10)).
        threshold_behavior : string
            Above : Event is detected when activity goes above the threshold. 
            Below : Event is detected when activity goes below the threshold. 
        baseline_win_len : string
            (optional) The baseline window length in seconds
        art_events : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])   
            (optional) Artefact events previously detected
        channel_dbg : String
            Channel label to save and exit detection info.

    Returns
    -----------  
        events          : Pandas DataFrame
            DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])
        det_activity    : list of ndarray of n_windows
            An array per item of the list signals.
            An array is the absolute signal amplitude or the std amplitude value relative to the baseline.
        bsl_activity    : list of ndarray of n_windows
            An array per item of the list signals.
            (Optional) Median\STD amplitude of the baseline window.

    @author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)

    Log : 
        2021-05-14 : First release, klacourse
"""
import pandas as pd

from flowpipe.ActivationState import ActivationState
from flowpipe import SciNode, InputPlug, OutputPlug

from CEAMSModules.AmplitudeDetector import amplitude_detection as amplitude_detection
from CEAMSModules.EventCompare import performance as performance
from CEAMSModules.EventReader import manage_events
from commons.NodeInputException import NodeInputException

DEBUG = False

class AmplitudeDetector(SciNode):
    """
    This plugin detects events based on the absolute signal amplitude.
    The plugin is flexible, an event can be detected when activity goes above 
    or below the threshold.  The threshold can be fixed or adaptive based on 
    a baseline window around the event.  The adaptive threshold can be x times 
    the baseline median value or x times the standard deviation of the baseline.
    When a z-score is used as threshold (x BSL STD), the absolute signal 
    amplitude can be log10 transformed to make them more normally distributed.

    Parameters
    -----------
        signals    : a list of SignalModel
                    signal.samples : The actual signal data as numpy list
                    signal.sample_rate : sampling rate of the signal (used to STFT)
                    signal.channel : current channel label                 
        event_group : string, event group.
        event_name : string, event label.
        pad_sec : string
            The padding event (length in second) to add to the beginning and 
            the end of the originally detected event.
        threshold_val : string or a list of float
            String : the value to threshold to detect events.
            list : the value to threshold for each signal included in signals.
        threshold_unit : string
            The threshold unit (fixed, x BSL median, x BSL STD or x BSL STD(log10)).
        threshold_behavior : string
            Above : Event is detected when activity goes above the threshold. 
            Below : Event is detected when activity goes below the threshold. 
        baseline_win_len : string
            (optional) The baseline window length in seconds
        art_events : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])   
            (optional) Artefact events previously detected
    Returns
    -----------  
        events          : Pandas DataFrame
            DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])     
        det_activity    : list of ndarray of n_windows
            An array per item of the list signals.
            An array is the absolute signal amplitude or the std amplitude value relative to the baseline.
        bsl_activity    : list of ndarray of n_windows
            An array per item of the list signals.
            (Optional) Median\STD amplitude of the baseline window.   

    @author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)    
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('AmplitudeDetector.__init__')
        InputPlug('signals', self)
        InputPlug('event_group', self)
        InputPlug('event_name', self)
        InputPlug('pad_sec', self)
        InputPlug('threshold_val', self)
        InputPlug('threshold_unit', self)
        InputPlug('threshold_behavior', self)
        InputPlug('baseline_win_len', self)  
        InputPlug('art_events', self)  
        InputPlug('channel_dbg', self)  
        OutputPlug('events', self)
        OutputPlug('det_activity', self)
        OutputPlug('bsl_activity', self)
          

    def __del__(self):
        if DEBUG: print('AmplitudeDetector.__del__')


    def subscribe_topics(self):
        pass


    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'AmplitudeDetector.on_topic_update {topic}:{message}')


    def compute(self, signals, event_group, event_name, pad_sec, threshold_val, \
        threshold_unit, threshold_behavior, baseline_win_len, art_events, channel_dbg):
        """
        This function detects events based on the absolute signal amplitude.
        The function is flexible, an event can be detected when activity goes above 
        or below the threshold.  The threshold can be fixed or adaptive based on 
        a baseline window around the event.  The adaptive threshold can be x times 
        the baseline median value or x times the standard deviation of the baseline.
        When a z-score is used as threshold (x BSL STD), the absolute signal 
        amplitude can be log10 transformed to make them more normally distributed.

        Parameters
        -----------
            signals    : a list of SignalModel
                        signal.samples : The actual signal data as numpy list
                        signal.sample_rate : sampling rate of the signal (used to STFT)
                        signal.channel : current channel label       
            event_group : string, group of the event              
            event_name : string, event name label.
            pad_sec : string
                The padding event (length in second) to add to the beginning and 
                the end of the originally detected event.
            threshold_val : string or a list of float
                String : the value to threshold to detect events.
                list : the value to threshold for each signal included in signals.
            threshold_unit : string
                The threshold unit (fixed, x BSL median, x BSL STD or x BSL STD(log10)).
            threshold_behavior : string
                Above : Event is detected when activity goes above the threshold. 
                Below : Event is detected when activity goes below the threshold. 
            baseline_win_len : string
                (optional) The baseline window length in seconds
            art_events : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])   
                (optional) Artefact events previously detected
            channel_dbg : String
                Channel label to save and exit detection info.
        Returns
        -----------  
            events          : Pandas DataFrame
                DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])     
            det_activity    : list of ndarray of n_windows
                An array per item of the list signals.
                An array is the absolute signal amplitude or the std amplitude value relative to the baseline.
            bsl_activity    : list of ndarray of n_windows
                An array per item of the list signals.
                (Optional) Median\STD amplitude of the baseline window.   

        @author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)
        """
        if DEBUG: print('AmplitudeDetector.compute {}'.format(event_name))

        self.clear_cache()

        # If art_events is not connected
        if isinstance(art_events,str):
            if art_events=='':
                art_events = manage_events.create_event_dataframe(None)
            else:
                err_message='ERROR: unexpected art_events type'
                self._log_manager.log(self.identifier, err_message)

        # It is possible to bypass the "AmplitudeDetector" by passing the input 
        # art_events to the output events without any modification
        if self.activation_state == ActivationState.BYPASS:
            return {
                'events': art_events
            }        

        if not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", \
                f"AmplitudeDetector input of wrong type. Expected: <class 'list'> received: {type(signals)}")

        if isinstance(threshold_val,str) and threshold_val=='':
            raise NodeInputException(self.identifier, "threshold_val", \
                f"AmplitudeDetector is not connected")

        pad_sec = float(pad_sec)

        if 'above' in threshold_behavior.lower():
            above_thresh_det=True
        elif 'below' in threshold_behavior.lower():
            above_thresh_det=False
        else:
            above_thresh_det=False
            raise NodeInputException(self.identifier, "threshold_behavior", \
                f"AmplitudeDetector input of wrong values, 'above' or 'below' is expected")

        # Create a pandas dataframe of events (each row is an event)
        dataframe = manage_events.create_event_dataframe(None)
        detections = 0

        # Save debugging info 
        if DEBUG==True:
            dbg_chan_found = 0
            detections_dbg = manage_events.create_event_dataframe(None)
            det_activity_dbg = []
            win_bsl_dbg = []
            fs_dbg = []
            threshold_val_dbg = []
            start_time_dbg = []

        # A fixed threshold is used
        if baseline_win_len=='':
            win_bsl = None
            if not ("fixed" in threshold_unit.lower()):
                err_message="ERROR : threshold_unit is not fixed and no baseline length was provided"
                self._log_manager.log(self.identifier, err_message)   
                print('AmplitudeDetector ' + err_message)       

            # Detects events based on the absolute amplitude
            for i, signal_model in enumerate(signals):
            #for i, (label, channel) in enumerate(signals.items()):

                if isinstance(threshold_val, str):
                    threshold_val_cur = float(threshold_val)
                elif isinstance(threshold_val, list):
                    threshold_val_cur = threshold_val[i]

                signal_cur = signal_model.samples
                fs = signal_model.sample_rate

                # detections : Array of zeros and ones where zero means no event and one means an event.
                # detections is samples based
                # det_activity : Absolute amplitude of the time series.
                # det_activity is samples based
                detections, det_activity  = amplitude_detection.fix_compute(
                    signal_cur,
                    pad_sec,
                    threshold_val_cur,
                    above_thresh_det,
                    fs)

                # Add the amplitude detections into the dataframe as events named
                # with the event_name and the channel as suffix
                (dataframe, dataframe_amp) = self._add_amplitude_events(\
                    dataframe, event_group, event_name, detections, signal_model)     

                # Save debugging info for the selected channel
                if DEBUG==True:
                    if channel_dbg in signal_model.channel:
                        dbg_chan_found = 1
                        detections_dbg = pd.concat([detections_dbg,dataframe_amp])
                        det_activity_dbg.append(det_activity)
                        win_bsl_dbg.append(win_bsl)
                        fs_dbg = fs
                        start_time_dbg.append(signal_model.start_time)
                        threshold_val_dbg.append(threshold_val_cur)

        # An adaptive threhold is used
        else:
            if "median" in threshold_unit.lower():
                median_use = True
                log10_data = False
            elif "std" in threshold_unit.lower():
                median_use = False
                if "log10" in threshold_unit.lower():
                    log10_data = True
                else:
                    log10_data = False
            else:
                err_message="ERROR : threshold_unit is not relative to the baseline and a baseline length is provided"
                self._log_manager.log(self.identifier, err_message)
                print('AmplitudeDetector ' + err_message) 
                return {
                    'events': '',
                    'det_activity' : '',
                    'bsl_activity'  : ''
                }  

            baseline_win_len = float(baseline_win_len)

            # For each channel detects events based on the PSD information
            for i, signal_model in enumerate(signals):

                if isinstance(threshold_val, str):
                    threshold_val_cur = float(threshold_val)
                elif isinstance(threshold_val, list):
                    threshold_val_cur = threshold_val[i]

                signal_cur = signal_model.samples
                fs = signal_model.sample_rate
                
                # Drop any event without channel information
                art_events_chan = art_events.dropna(axis=0, how='any', inplace=False)
                # Filter the previously detected artifact for the current channel
                art_events_chan = art_events_chan[art_events_chan.channel.str.contains(signal_model.channel)]

                # Detects events based on the absolute amplitude
                detections_bin, det_activity, win_bsl  = amplitude_detection.adp_compute(
                    signal_cur,
                    pad_sec,
                    threshold_val_cur,
                    above_thresh_det,
                    baseline_win_len, 
                    median_use,
                    log10_data,
                    fs,
                    art_events_chan)

                # Add the amplitude detections into the dataframe as events named
                # with the event_name and the channel as suffix
                (dataframe, dataframe_amp) = self._add_amplitude_events(\
                    dataframe, event_group, event_name, detections_bin, signal_model)   

                # Save debugging info for the selected channel
                if DEBUG==True:
                    if channel_dbg in signal_model.channel:
                        dbg_chan_found = 1
                        detections_dbg = pd.concat([detections_dbg,dataframe_amp])
                        det_activity_dbg.append(det_activity)
                        win_bsl_dbg.append(win_bsl)
                        fs_dbg = fs
                        start_time_dbg.append(signal_model.start_time)
                        threshold_val_dbg.append(threshold_val_cur)

        # Add previously detected artefact
        dataframe = pd.concat([dataframe,art_events])
        # Reset index
        dataframe.reset_index(inplace=True, drop=True)
        # Sort events based on the start_sec
        dataframe.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')        

        if DEBUG==True:
            if dbg_chan_found==0:
                err_message='ERROR: no debug channel found'
                self._log_manager.log(self.identifier, err_message)
                return {
                    'events': dataframe,
                    'det_activity' : '',
                    'bsl_activity'  : ''
                }
            else:
                # Save the information to show on the results View
                # For now : only the first signal of the selected channel is saved
                cache = {}
                cache['detections'] = detections_dbg
                cache['det_activity'] = det_activity_dbg[0]
                cache['fs'] = fs_dbg
                cache['event_name'] = event_name
                cache['threshold_val'] = threshold_val_dbg[0]
                cache['start_time'] = start_time_dbg[0]
                self._cache_manager.write_mem_cache(self.identifier, cache)
                return {
                    'events': dataframe,
                    'det_activity' : det_activity_dbg,
                    'bsl_activity'  : win_bsl_dbg
                }
        else:
            return {
                'events': dataframe,
                'det_activity' : '',
                'bsl_activity'  : ''
            }
    
           
    def _add_amplitude_events(self, dataframe, event_group, event_name, detections, channel):
        """ 
            Add the spectral detections into the dataframe as events named
            "event_name" with the channel label added in the dataframe (label saved in the psd dict).

            Parameters
            -----------
            dataframe : pandas dataframe 
                List of events (each row is an event)
            event_group : string
                Event group
            event_name : string
                Event name
            detections : ndarray
                Events array, 0 means no event and 1 means an event (the size of the signal)
            channel : SignalModel
                channel.samples : signal array
                channel.sample_rate : sampling rate of the signal (used to STFT)
                channel.channel : current channel label              
                channel.start_time : start time in sec of the signal array  
            Returns
            -----------  
            dataframe : pandas dataframe
                List of events including previously detected events.
            dataframe_amp : pandas dataframe
                List of events detected in the current instance.
        """

        # Create an event for each pair of starts and ends
        event_list = performance.bin_evt_to_lst(detections)
        # Convert event in samples into events in seconds
        event_list = event_list/channel.sample_rate

        if len(event_list)>0:
            # The event padding can create partially supperposed events
            # We re-create the events list to merge any suppoerposed events
            det_event_bin = performance.evt_lst_to_bin(event_list, fs=channel.sample_rate)
            event_list = performance.bin_evt_to_lst_sec(det_event_bin, fs=channel.sample_rate)

        # Concatenate the channel label to the event_name
        # Add the event_name and the channel label to the events list
        events = [(event_group, event_name, start + channel.start_time, dur, channel.channel) for start, dur in event_list]

        # Create a pandas dataframe of events (each row is an event) for the current signal
        dataframe_amp = manage_events.create_event_dataframe(events)
        
        # Returns the whole dataframe (can include other events)
        #   and the current events
        return (pd.concat([dataframe,dataframe_amp]), dataframe_amp)
