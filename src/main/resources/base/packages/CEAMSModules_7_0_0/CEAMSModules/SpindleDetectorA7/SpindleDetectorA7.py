"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    SpindleDetectorA7
    Class to detect spindles based on the a7 algorithm
"""
import pandas as pd
import numpy as np
import time

import config
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from flowpipe import SciNode, InputPlug, OutputPlug
from flowpipe.ActivationState import ActivationState
from .detect_spindles import detect_spindles
from CEAMSModules.EventReader import manage_events

DEBUG = False

class SpindleDetectorA7(SciNode):
    """
    Class to detect spindles based on the a7 algorithm

    Parameters
    ----------
        signals : List of SignalModel
            List of signal with dictionary of channels with SignalModel with 
            properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original
        thresholds : dict
            thresh_abs_sigma_pow_uv2 : threshold for the absolute sigma power (uv2)
            thresh_rel_sigma_pow_z : threshold for the relative sigma power (z-score)
            thresh_sigma_cov_z : threshold for the sigma covariance (z-score)
            thresh_sigma_cor_perc : threshold for the sigma correlation (%)
        event_group : String
            List of Event group to filter separated by comma (discard too long, short)
        event_name : String
            List of Event name to filter separated by comma (discard too long, short)
        artifact_events : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
            Selected events list for artifacts.

    Returns
    -------
        events: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
            Events list for spindle detections.
        
    """
    def __init__(self, **kwargs):
        """ Initialize module SpindleDetectorA7 """
        super().__init__(**kwargs)
        if DEBUG: print('SpindleDetectorA7.__init__')

        # Input plugs
        InputPlug('signals',self)
        InputPlug('thresholds',self)
        InputPlug('event_group',self)
        InputPlug('event_name',self)
        InputPlug('artifact_events',self)
        # Output plugs
        OutputPlug('events',self)

        self._is_master = False 

        # Fixed parameters for A7
        self.WIN_LENGTH_SEC = 0.3
        self.WIN_STEP_SEC = 0.1
        self.BSL_LENGTH_SEC = 30
    

    def compute(self, signals, thresholds, event_group, event_name, artifact_events):
        """
        Function to detect spindles based on the a7 algorithm.

        Parameters
        ----------
            signals : List of SignalModel
                List of signal with dictionary of channels with SignalModel with 
                properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original
            thresholds: dict
                thresh_abs_sigma_pow_uv2 : threshold for the absolute sigma power (uv2)
                thresh_rel_sigma_pow_z : threshold for the relative sigma power (z-score)
                thresh_sigma_cov_z : threshold for the sigma covariance (z-score)
                thresh_sigma_cor_perc : threshold for the sigma correlation (%)

            event_group : String
                List of Event group to filter separated by comma (discard too long, short)

            event_name : String
                List of Event name to filter separated by comma (discard too long, short)

            artifact_events: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
                Selected events list for artifacts.

        Returns
        -------
            events: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
                Events list for spindle detections.

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        if isinstance(signals, str) and signals=='':
            raise NodeInputException(self.identifier, "signals", \
                f"SpindleDetectorA7 this input is empty, no signals no spindles.")     
        if isinstance(thresholds, str) and thresholds=='':
            raise NodeInputException(self.identifier, "thresholds", \
                f"SpindleDetectorA7 this input is empty, no thresholds no spindles.")
        if isinstance(event_group, str) and event_group=='':
            raise NodeInputException(self.identifier, "event_group", \
                f"SpindleDetectorA7 this input is empty, no event_group no spindles.")
        if isinstance(event_name, str) and event_name=='':
            raise NodeInputException(self.identifier, "event_name", \
                f"SpindleDetectorA7 this input is empty, no event_name no spindles.")
        
        if not isinstance(thresholds, dict):
            thresholds = eval(thresholds)
        if not isinstance(thresholds, dict):
            raise NodeInputException(self.identifier, "thresholds", \
                f"SpindleDetectorA7 this input is a {type(thresholds)}, it is expected to be a dict.")

        if not isinstance(artifact_events, pd.DataFrame) and not artifact_events=='':
            raise NodeInputException(self.identifier, "artifact_events", \
                f"SpindleDetectorA7 this input is a {type(artifact_events)}, it is expected to be a Pandas DataFrame.")            

        # Pre-processing is done previous to the detection of spindles
            # The filtering 0.3-30 Hz and the downsampling to 100 Hz are already done at this point

        thresholds_np = np.array([thresholds['thresh_abs_sigma_pow_uv2'], thresholds['thresh_rel_sigma_pow_z'],\
             thresholds['thresh_sigma_cov_z'], float(thresholds['thresh_sigma_cor_perc'])/100])

        # It is possible to bypass the detection of spindles
        if self.activation_state == ActivationState.BYPASS:
            return {
                'events': manage_events.create_event_dataframe(None)
            }   

        # Code are extracted from the SUMO project (https://github.com/dslaborg/sumo)
        # detect_spindles has been modified to keep all spindles
            # The removal of too short and long spindles are done at the end of the process
        event_lst = []
        i_signal = 0
        if config.is_dev: # Avoid save of the recording when not developping
            features_signals = []
            feature_names = ['absSigmaPowUv2', 'relSigmaPowZ', 'sigmaCovZ', 'sigmaCorPerc']
        for signal in signals:
            if DEBUG: 
                print(f"SpindleDetectorA7.compute signal {i_signal} starts at {time.strftime('%H:%M:%S', time.gmtime(signal.start_time))}")
                i_signal += 1

            data = signal.samples
            sample_rate = signal.sample_rate
            features, events_index_lst  = detect_spindles(data, thresholds_np, \
                self.WIN_LENGTH_SEC, self.WIN_STEP_SEC, self.BSL_LENGTH_SEC, sample_rate)
            if config.is_dev:
                for i in range(features.shape[1]):
                    feature_signal = signal.clone()
                    feature_signal.samples = features[:,i]
                    feature_signal.channel = feature_names[i]
                    feature_signal.meta = {'threshold': thresholds_np[i]}
                    features_signals.append(feature_signal)
            events_sec_list = events_index_lst / sample_rate
            # Add the event_name and the channel label to the events list
            events_cur = [(event_group, event_name, signal.start_time+start_sec, stop_sec-start_sec, signal.channel) \
                for start_sec, stop_sec in events_sec_list]
            event_lst.extend(events_cur)

        # Create a pandas dataframe of events (each row is an event) for the current pds
        events_df = manage_events.create_event_dataframe(event_lst)

        # Write to the cache to use the data in the resultTab
        cache = {}
        if config.is_dev: # Avoid save of the recording when not developping
            signals_2_plot = signals.copy()
            signals_2_plot.extend(features_signals)
            # Extract the number of channels
            channel_lst = [signal.channel for signal in signals_2_plot]
            n_chan = len(np.unique(np.array(channel_lst)))
            cache['signals'] = signals_2_plot
            cache['n_chan'] = n_chan
            cache['events'] = events_df
            self._cache_manager.write_mem_cache(self.identifier, cache)

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, f"{len(events_df)} spindles  were found.")

        return {
            'events': events_df
        }