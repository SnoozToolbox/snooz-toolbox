"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    This plugin detects events based on maximum amplitude variation in a 
    narrow time windows.  The amplitude variation is computed as max - min 
    of amplitude values included in a sliding window.  The threshold can be 
    fixed or a z-score (a number of standard deviations) from the baseline window. 
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
        event_group     : string, event group.                
        event_name      : string, event label.
        win_len_sec     : string
            The window length (in second) used to compute the amplitude variation. 
        win_step_sec    : string
            The window step (in seconds) between two amplitude variation calculations.
        pad_sec         : string
            The padding event (length in second) to add to the beginning and 
            the end of the originally detected event.
        threshold_val   : string
            The threshold value to detect events.
        threshold_unit  : string
            The threshold unit (fixed, x BSL median, x BSL STD or x BSL STD(log10)).
        threshold_behavior : string
            Above : Event is detected when activity goes above the threshold. 
            Below : Event is detected when activity goes below the threshold. 
        baseline_win_len : string
            (optional) The baseline window length in seconds
        art_events      : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])   
            (optional) Artefact events previously detected
        channel_dbg     : String
            Channel label to save and exit detection info.

    Returns
    -----------  
        events          : Pandas DataFrame
            DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])     
        det_activity    : ndarray of n_windows
            Absolute signal amplitude or the std amplitude value relative to the baseline.
        bsl_activity    : ndarray of n_windows
            (Optional) Median\STD amplitude of the baseline window.   

    @author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)

"""
import pandas as pd

from flowpipe.ActivationState import ActivationState
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException

from CEAMSModules.AmplitudeDetector import amplitude_detection as amplitude_detection
from CEAMSModules.EventCompare import performance as performance
from CEAMSModules.EventReader import manage_events

DEBUG = False

class AmplitudeVarDetector(SciNode):
    """
    This plugin detects events based on maximum amplitude variation in a 
    narrow time windows.  The amplitude variation is computed as max - min 
    of amplitude values included in a sliding window.  The threshold can be 
    fixed or a z-score (a number of standard deviations) from the baseline window. 
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
        event_name : string
            event label.
        win_len_sec : string
            The window length (in second) used to compute the amplitude variation. 
        win_step_sec : string
            The window step (in seconds) between two amplitude variation calculations.
        pad_sec : string
            The padding event (length in second) to add to the beginning and 
            the end of the originally detected event.            
        threshold_val : string
            The threshold value to detect events.
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
            List of events (columns=['group','name','start_sec','duration_sec','channels'])         
        det_activity    : ndarray of n_windows
            Absolute signal amplitude or the std amplitude value relative to the baseline.
        bsl_activity    : ndarray of n_windows
            (Optional) Median\STD amplitude of the baseline window.    

    @author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)    
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('AmplitudeVarDetector.__init__')
        InputPlug('signals', self)
        InputPlug('event_group', self)
        InputPlug('event_name', self)
        InputPlug('win_len_sec', self)
        InputPlug('win_step_sec', self)
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


    def subscribe_topics(self):
        pass


    def compute(self, signals, event_group, event_name, win_len_sec, win_step_sec, pad_sec, threshold_val, \
        threshold_unit, threshold_behavior, baseline_win_len, art_events, channel_dbg):
        """
        This function detects events based on maximum amplitude variation in a 
        narrow time windows.  The amplitude variation is computed as max - min 
        of amplitude values included in a sliding window.  The threshold can be 
        fixed or a z-score (a number of standard deviations) from the baseline window. 
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
            win_len_sec : string
                The window length (in second) used to compute the amplitude variation. 
            win_step_sec : string
                The window step (in seconds) between two amplitude variation calculations.
            pad_sec : string
                The padding event (length in second) to add to the beginning and 
                the end of the originally detected event. 
            threshold_val : string
                The threshold value to detect events.
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
            det_activity    : ndarray of n_windows
                Absolute signal amplitude or the std amplitude value relative to the baseline.
            win_bsl         : ndarray of n_windows
                (Optional) Median\STD amplitude of the baseline window.     

        @author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)
        """
        if DEBUG: print('AmplitudeVarDetector.compute {}'.format(event_name))

        self.clear_cache()

        if not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", \
                f"AmplitudeVarDetector input of wrong type. Expected: <class 'list'> received: {type(signals)}")

        if isinstance(threshold_val,str) and threshold_val=='':
            raise NodeInputException(self.identifier, "threshold_val", \
                f"AmplitudeVarDetector is not connected")

        results = []

        threshold_val = float(threshold_val)
        win_len_sec = float(win_len_sec)
        win_step_sec = float(win_step_sec)
        pad_sec = float(pad_sec)

        if 'above' in threshold_behavior.lower():
            above_thresh_det=True
        elif 'below' in threshold_behavior.lower():
            above_thresh_det=False
        else:
            above_thresh_det=False
            raise NodeInputException(self.identifier, "threshold_behavior", \
                f"AmplitudeVarDetector input of wrong values, 'above' or 'below' is expected")

        # If art_events is not connected
        if isinstance(art_events,str):
            if art_events=='':
                art_events =  manage_events.create_event_dataframe(None)
            else:
                err_message='ERROR: unexpected art_events type'
                self._log_manager.log(self.identifier, err_message)

        # Create a pandas dataframe of events (each row is an event)
        dataframe =  manage_events.create_event_dataframe(None)

        # Save debugging info 
        if DEBUG==True:
            dbg_chan_found = 0
            det_activity_dbg = []
            win_bsl_dbg = []
            fs_dbg = []

        # A fixed threshold is used
        if baseline_win_len=='':
            win_bsl = None
            if not ("fixed" in threshold_unit.lower()):
                err_message="ERROR : threshold_unit is not fixed and no baseline length was provided"
                self._log_manager.log(self.identifier, err_message)                    
                print(err_message)

            # Detects events based on the max amplitude variation
            for i, signal_model in enumerate(signals):

                signal_cur = signal_model.samples
                fs = signal_model.sample_rate

                # Detects events based on the max amplitude variation
                    # det_bin_win : ndarray 
                    #     Events array, 0 means no event and 1 means an event (each value represents a window).
                    # var_win_act : ndarray
                    #     Maximum variation within each window (µV).
                det_bin_win, var_win_act  = amplitude_detection.var_fix_compute(
                    signal_cur,
                    win_len_sec, 
                    win_step_sec, 
                    threshold_val,
                    above_thresh_det,
                    fs)

                # Add the var amplitude detections into the dataframe as events named
                # with the event_name and the channel as suffix
                (dataframe, dataframe_amp) = self._add_windows_events(\
                    dataframe, event_group, event_name, det_bin_win, win_len_sec, \
                        win_step_sec, pad_sec, signal_model.sample_rate, signal_model.channel)    

                # Save debugging info 
                if DEBUG==True:
                    if channel_dbg in signal_model.channel:
                        dbg_chan_found = 1
                        signal_cur_dbg = signal_cur
                        events_dbg = dataframe_amp
                        det_activity_dbg = var_win_act
                        win_bsl_dbg = win_bsl
                        fs_dbg = signal_model.sample_rate

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
                median_use = False
                log10_data = False

            baseline_win_len = float(baseline_win_len)

            # For each channel detects events based on the PSD information
            for i, signal_model in enumerate(signals):

                signal_cur = signal_model.samples
                fs = signal_model.sample_rate
                # Filter the previously detected artifact for the current channel
                art_events_chan = art_events[art_events.signal_models.str.contains(signal_model.channel)]

                # Detects events based on the max variation of amplitude
                    # det_bin_win : ndarray 
                    #     Events array, 0 means no event and 1 means an event (each value represents a window).
                    # var_win_act : ndarray
                    #     Maximum variation within each window.
                    # bsl_win : ndarray of n_windows (or [2 x n_windows])                    
                det_bin_win, var_win_act, win_bsl  = amplitude_detection.var_adp_compute(
                    signal_cur,
                    win_len_sec, 
                    win_step_sec,
                    threshold_val,
                    above_thresh_det,
                    baseline_win_len, 
                    median_use,
                    log10_data,
                    fs,
                    art_events_chan)

                # Add the var amplitude detections into the dataframe as events named
                # with the event_name and the channel as suffix
                (dataframe, dataframe_amp) = self._add_windows_events(\
                    dataframe, event_group, event_name, det_bin_win, win_len_sec, \
                        win_step_sec, pad_sec, signal_model.sample_rate, signal_model.channel) 

                # Save debugging info 
                if DEBUG==True:
                    if channel_dbg in signal_model.channel:
                        dbg_chan_found = 1
                        signal_cur_dbg = signal_cur
                        events_dbg = dataframe_amp
                        det_activity_dbg = var_win_act
                        win_bsl_dbg = win_bsl
                        fs_dbg = signal_model.sample_rate

        # Add previously detected artefact
        dataframe = pd.concat([dataframe,art_events])
        # Reset index
        dataframe.reset_index(inplace=True, drop=True)
        # Sort events based on the start_sec
        dataframe.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')  

        if dbg_chan_found==0:
            err_message='ERROR: no debug channel found, the last channel is used as debug channel'
            self._log_manager.log(self.identifier, err_message)
            signal_cur_dbg = signal_cur
            events_dbg = dataframe_amp
            det_activity_dbg = var_win_act
            win_bsl_dbg = win_bsl 
            fs_dbg = fs

        # Save the information to show on the results View
        if DEBUG==True:
            cache = {}
            cache['events'] = events_dbg
            cache['signal'] = signal_cur_dbg
            cache['fs'] = fs_dbg
            self._cache_manager.write_mem_cache(self.identifier, cache)
            return {
                'events': dataframe,
                'det_activity' : det_activity_dbg,
                'bsl_activity' : win_bsl_dbg
            }
        else:
            return {
                'events': dataframe,
                'det_activity' : "",
                'bsl_activity' : ""
            }


    def _add_windows_events(self, dataframe, event_group, event_name, detections, win_len,\
         win_step, pad_sec, fs, chan_label):
        """ 
            Add the windows detections into the dataframe as events named
            "event_name" with the chan_label as suffix.

            Parameters
            -----------
            dataframe   : pandas dataframe 
                List of events (each row is an event).
            event_group : string
                Event group.
            event_name  : string
                Event name.
            detections  : ndarray of n_windows
                Events array, 0 means no event and 1 means an event.
            win_len     : float
                The window length (in seconds) used to compute the amplitude variation.
            win_step    : float
                The window step (in seconds) between two amplitude variation calculations.
            pad_sec     : float
                The padding event (length in second) to add to the beginning and 
                the end of the originally detected event. 
            fs          : float 
                Sampling rate in Hz
            chan_label  : string
                Cahnnel label

            Returns
            -----------  
            dataframe : pandas dataframe
                List of events including previously detected events.
            dataframe_psd : pandas dataframe
                List of events detected in the current instance.
        """
        #--------------------------------------------------------------------------
        # Add padding to the event (original event can be only one sample long)
        #--------------------------------------------------------------------------
        # Convert the events array into a list of events with start and duration in samples. 
        # The array must contain only 0 and 1, 0 means no events and 1 means an event.
        # Create an event for each pair of starts and ends
        #   event_list is a list of events and its units are windows
        event_list = performance.bin_evt_to_lst(detections)

        # event_list is windows based
        #   events is in seconds because the win_step are in seconds
        #   warning : the duration of the event cannot be multiplied by win_dur
        #       imagine you have win_len=5s and win_step=1s and an event
        #       5 "step" window long, it would make the event duration
        #       5 win * 5 sec = 25 seconds long and only 
        #       9 seconds of data was taken into account 
        #       Taking dur*win_step+(win_len-win_step) means that the
        #       artefact will be as long as the data taken for the STFT.
        #       ex) win_len=5s and win_step=1s; 5 windows * 1s + 4s = 9 s

        nsample_win = win_len*fs
        if not nsample_win.is_integer():
            # Compute the real win_len used
            print("Warning : win_len {} is changed for {}".format(win_len, int(round(nsample_win))/fs))
            win_len = int(round(nsample_win))/fs

        nsample_step = win_step*fs
        if not nsample_step.is_integer():
            # Compute the real win_step used
            print("Warning : win_step {} is changed for {}".format(win_step, int(round(nsample_step))/fs))
            win_step = int(round(nsample_step))/fs       

        events = [(start*win_step, dur*win_step+(win_len-win_step)) for start, dur in event_list]

        # Add padding to both the beginning and the end of the original event
        events_pad = [(start-pad_sec if start-pad_sec > 0 else 0, dur+2*pad_sec) for start, dur in events]

        if len(events_pad)>0:
            # dur*win_len when win_len>win_step can supperpose events
            # We re-create the events list to merge any suppoerposed events
            #   events is a list of events in secondes
            #   det_event_bin is a binary vector in samples
            det_event_bin = performance.evt_lst_to_bin(events_pad, fs=fs)
            #   events is a list of events in secondes without supperposition
            events = performance.bin_evt_to_lst_sec(det_event_bin, fs=fs)

        # Concatenate the channel label to the event_name
        # Add the event_name and the channel label to the events list
        events = [(event_group, event_name, start, dur, chan_label) for start, dur in events]

        # Create a pandas dataframe of events (each row is an event) for the current pds
        dataframe_cur =  manage_events.create_event_dataframe(events)
        # Events detected from other psds (channels) are also added to the df
        dataframe = pd.concat([dataframe,dataframe_cur])
        return (dataframe, dataframe_cur)