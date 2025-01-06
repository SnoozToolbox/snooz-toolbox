"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    ThresholdComputation
    To compute the value to threshold (i.e. µV) from a signals (i.e. EEG time series) 
    based on a threshold definition (i.e. 4) and a metric or a unit (i.e. standard deviation).
"""
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from flowpipe import SciNode, InputPlug, OutputPlug
from flowpipe.ActivationState import ActivationState
from ..PSGReader import commons

import numpy as np
import pandas as pd

DEBUG = False

class ThresholdComputation(SciNode):
    """
    To compute the value to threshold (i.e. µV) from a signals (i.e. EEG time series) 
    based on a threshold definition (i.e. 4) and a metric or a unit (i.e. standard deviation).

    Parameters
    -----------
        signals: dict of SignalModel, the key is the label of the channel.
            signals[channel_label].samples : The actual signal data as numpy list
        cycle_events : pandas DataFrame
            Events (columns=['group','name','start_sec','duration_sec','channels'])   
            Sleep cycles are defined with the 'group' cycle and the 'name' nremp or remp
        threshold_definition: float
            threshold definition to compute the value from the signals
        threshold_metric: String
            Metric (unit) used for thresholding.
            "percentile", "standard deviation", "variance" or "median"
        threshold_scope : String
            '0' to compute a threshold per item of signals
            '1' to compute a threshold per sleep cycle and channel
            '2' to compute a threshold per channel (through all signals).
        
    Returns
    -----------  
        threshold_value: list of float 
            The value to threshold for each signal included in signals.
            (Can vary for each item of signals depending of the threshold_scope.)
        
    """
    def __init__(self, **kwargs):
        """ Initialize module ThresholdComputation """
        super().__init__(**kwargs)

        # Input plugs
        InputPlug('signals',self)
        InputPlug('cycle_events',self)
        InputPlug('threshold_definition',self)
        InputPlug('threshold_metric',self)
        InputPlug('threshold_scope',self)
        # Output plugs
        OutputPlug('threshold_value',self)

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    

    def compute(self, signals, cycle_events, threshold_definition, threshold_metric, threshold_scope):
        """
        To compute the value to threshold (i.e. µV) from a signals (i.e. EEG time series) 
        based on a threshold definition (i.e. 4) and a metric or a unit (i.e. standard deviation).

        Parameters
        -----------
            signals: dict of SignalModel, the key is the label of the channel.
                signals[channel_label].samples : The actual signal data as numpy list
            cycle_events : pandas DataFrame
                Events (columns=['group','name','start_sec','duration_sec','channels'])   
                Sleep cycles are defined with the 'group' cycle and the 'name' nremp or remp
            threshold_definition: float
                threshold definition to compute the value from the signals
            threshold_metric: String
                Metric (unit) used for thresholding.
                "percentile", "standard deviation", "variance" or "median"
            threshold_scope : String
                '0' to compute a threshold per item of signals
                '1' to compute a threshold per sleep cycle and channel
                '2' to compute a threshold per channel (through all signals).
                
        Returns
        -----------  
            threshold_value: list of float 
                The value to threshold for each signal included in signals.
        """
        self.clear_cache()

        # It is possible to bypass the ThresholdComputation by passing the 0 value threshold to the output
        if self.activation_state == ActivationState.BYPASS:
            return {
                'threshold_value': []
            }

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if isinstance(signals,str) and signals=='':
            raise NodeInputException(self.identifier, "signals", \
                f"ThresholdComputation this input is not connected.")       
        elif not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", \
                f"ThresholdComputation input of wrong type. Expected: <class 'list'> received: {type(signals)}")                         

        # Convert input parameter
        try: 
            threshold_definition = float(threshold_definition)
        except:
            raise NodeInputException(self.identifier, "threshold_definition",\
                 f"ThresholdComputation the type of this input is unexpected.")

        threshold_value = [] # To store threshold value
        channel_lst = [] # To keep track of the channels
        samples_all_chan = {} # To accumulate the samples for each channel

        cycle_df = []
        if threshold_scope=='1':
            if isinstance(cycle_events,str) and cycle_events=='':
                raise NodeInputException(self.identifier, "cycle_events", \
                    f"ThresholdComputation this input is not connected.")
            if not isinstance(cycle_events,pd.DataFrame):
                raise NodeInputException(self.identifier, "cycle_events", \
                    f"ThresholdComputation input of wrong type. Expected: <class pd.DataFrame> received: {type(cycle_events)}")                     
            cycle_df = cycle_events[cycle_events.group==commons.sleep_cycle_group]
            # Format events_df event list
            cycle_df = cycle_df.sort_values(by=['start_sec'])
            cycle_df = cycle_df.reset_index(drop=True)            

        # Loop through all channels and all events
        for i, signal_model in enumerate(signals):
            
            if len(signal_model.samples) == 0:
                err_message = f' WARNING: ThresholdComputation, signals is empty for channel:{signal_model.channel}'
                self._log_manager.log(self.identifier, err_message)
                print(err_message)
                continue

            # Compute the threshold value
            # One threshold per item of signals
            if threshold_scope == '0':
                sample_value = None
                if "standard deviation" in threshold_metric:
                    std_value = np.nanstd(signal_model.samples)
                    sample_value = threshold_definition * std_value
                elif "percentile" in threshold_metric:
                    sample_value = np.nanpercentile(signal_model.samples,threshold_definition)
                elif "median" in threshold_metric:
                    med_value = np.nanmedian(signal_model.samples)
                    sample_value = threshold_definition * med_value
                elif "variance" in threshold_metric:
                    var_value = np.nanvar(signal_model.samples)
                    sample_value = threshold_definition * var_value
                else:
                    raise NodeInputException(self.identifier, "threshold_metric",\
                        f"ThresholdComputation this input is unexpected.")
                # Cache only the data from the first channel
                if i == 0:
                    cache = {}
                    cache['channel_label'] = signal_model.channel
                    cache['sample'] = signal_model.samples
                    cache['threshold_metric'] = threshold_metric
                    cache['threshold_definition'] = threshold_definition
                    cache['threshold_value'] = sample_value
                    self._cache_manager.write_mem_cache(self.identifier, cache)
                # Accumulate threshold value through all the channels
                threshold_value.append(sample_value)

            # If a threshold is computed for each sleep cycle
            # Accumulate samples for each channel and each cycle
            elif int(threshold_scope)>0:
                if threshold_scope=='1':
                    # Find which sleep cycles start before the current signal_model starts
                    (idx_start,) = np.where(signal_model.start_time-cycle_df.start_sec>=-0.1) # -0.1 to support non interger sampling rate in Stellate
                    # Find which sleep cycles end after the current signal_model ends
                    (idx_stop,) = np.where((cycle_df.start_sec+cycle_df.duration_sec)-(signal_model.start_time+signal_model.duration)>=-0.1) # -0.1 to support non interger sampling rate in Stellate
                    # Find intersection between idx_start and idx_stop
                    idx_include_signal = np.intersect1d(idx_start,idx_stop).tolist()
                else:
                    idx_include_signal=[0]
                if len(idx_include_signal)==1:
                    cycle_i = idx_include_signal[0]
                    if not signal_model.channel in channel_lst:
                        channel_lst.append(signal_model.channel)
                        samples_all_chan[signal_model.channel] = [signal_model.samples]
                    elif len(samples_all_chan[signal_model.channel])==cycle_i:
                        samples_all_chan[signal_model.channel].append(signal_model.samples)
                    else:
                        samples_all_chan[signal_model.channel][cycle_i] = \
                            np.concatenate((samples_all_chan[signal_model.channel][cycle_i],signal_model.samples))
                else:
                    if len(idx_include_signal)==0:
                        raise NodeRuntimeException(self.identifier, "cycle_events",\
                            f"ThresholdComputation signal to process not included in the sleep cycle.")
                    else:
                        raise NodeRuntimeException(self.identifier, "cycle_events",\
                            f"ThresholdComputation signal to process found twice in the sleep cycle.")                        

        # Compute the threshold for the whole list "signals"
        # Still one threshold per channel
        if int(threshold_scope) > 0:
            # Loop through channels
            threshold_all_chan = {}
            for chan_label, chan_samples in samples_all_chan.items(): 
                threshold_all_chan[chan_label]=[]
                for i_cycle, chan_samples_cycle in enumerate(chan_samples):
                    sample_value = None
                    if "standard deviation" in threshold_metric:
                        std_value = np.nanstd(chan_samples_cycle,axis=0)
                        sample_value = threshold_definition * std_value
                    elif "percentile" in threshold_metric:
                        sample_value = np.nanpercentile(chan_samples_cycle,threshold_definition)
                    elif "median" in threshold_metric:
                        med_value = np.nanmedian(chan_samples_cycle)
                        sample_value = threshold_definition * med_value
                    elif "variance" in threshold_metric:
                        var_value = np.nanvar(chan_samples_cycle)
                        sample_value = threshold_definition * var_value
                    else:
                        raise NodeInputException(self.identifier, "threshold_metric",\
                            f"ThresholdComputation this input is unexpected.")
                    threshold_all_chan[chan_label] = np.append(threshold_all_chan[chan_label],sample_value)        

                # Cache only the data from the first channel
                if channel_lst[0] == chan_label and i_cycle==0:
                    cache = {}
                    cache['channel_label'] = chan_label
                    cache['sample'] = chan_samples
                    cache['threshold_metric'] = threshold_metric
                    cache['threshold_definition'] = threshold_definition
                    cache['threshold_value'] = sample_value
                    self._cache_manager.write_mem_cache(self.identifier, cache)

            # Spread the channel threshold for each item of signals
            threshold_value = [] # Create an empty list to append thresholds
            for i, signal_model in enumerate(signals):
                # Find in which sleep cycle the current signal_model is included
                if threshold_scope=='1':
                    # Find which sleep cycles start before the current signal_model starts
                    (idx_start,) = np.where(signal_model.start_time-cycle_df.start_sec>=-0.1) # -0.1 to support non interger sampling rate in Stellate
                    # Find which sleep cycles end after the current signal_model ends
                    (idx_stop,) = np.where((cycle_df.start_sec+cycle_df.duration_sec)-(signal_model.start_time+signal_model.duration)>=-0.1) # -0.1 to support non interger sampling rate in Stellate
                    # Find intersection between idx_start and idx_stop
                    idx_include_signal = np.intersect1d(idx_start,idx_stop).tolist()
                else:
                    idx_include_signal=[0]
                if len(idx_include_signal)==1:
                    cycle_i = idx_include_signal[0]
                    # Propagate threshold value through all the events
                    threshold_value.append(threshold_all_chan[signal_model.channel][cycle_i])

        return {
            'threshold_value': threshold_value
        }