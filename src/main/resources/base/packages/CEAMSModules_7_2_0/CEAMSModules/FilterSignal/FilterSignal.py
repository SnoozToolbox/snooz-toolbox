"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    This plugin applies a FIR\lIIR filter to EEG signals.

    Parameters
    -----------
        signals            -- An array of SignalModel to filter
        type               -- 'bandpass', 'lowpass', 'highpass', 'bandstop'
        IR_family          -- 'IIR', 'FIR'
        use_std_order      -- If True, the order is calculated based on the 
                                formula: order=5*(sample_rate/lower frequency)
                                If False, the order is taken from the [order]
                                parameter.
        order              -- Filter order
        cutoff             -- Cutoff frequency, must be an increasing value
                                between 0 and sample_rate/2
        window             -- Desired window ex: 'hamming'
            -- see: https://docs.scipy.org/doc/scipy/reference/generated/
            -- scipy.signal.get_window.html#scipy.signal.get_window
            -- for all options.

    Returns
    -----------  
        signals  -- Filtered signals
"""
from scipy import signal
import numpy as np

import config
from flowpipe.ActivationState import ActivationState
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = False

class FilterSignal(SciNode):
    """
        This plugin applies a FIR\lIIR filter to EEG signals.

        Parameters
        -----------
            signals            -- An list of SignalModel to filter
            type               -- 'bandpass', 'lowpass', 'highpass', 'bandstop'
            IR_family          -- 'IIR', 'FIR'
            use_std_order      -- If True, the order is calculated based on the 
                                    formula: order=5*(sample_rate/lower frequency)
                                  If False, the order is taken from the [order]
                                    parameter.
            order              -- Filter order
            cutoff             -- Cutoff frequency, must be an increasing value
                                  between 0 and sample_rate/2
            window             -- Desired window ex: 'hamming'
                -- see: https://docs.scipy.org/doc/scipy/reference/generated/
                -- scipy.signal.get_window.html#scipy.signal.get_window
                -- for all options.

        Returns
        -----------  
            signals  -- Filtered signals
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('FilterSignal.__init__')
        self._cache_duration = 30 # in seconds
        InputPlug('signals', self)
        InputPlug('type', self)
        InputPlug('IR_family', self)
        InputPlug('use_std_order', self)
        InputPlug('order', self)
        InputPlug('cutoff', self)
        InputPlug('window', self)
        OutputPlug('signals', self)

    def __del__(self):
        if DEBUG: print('FilterSignal.__del__')

    def subscribe_topics(self):
        pass

    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'FilterSignal.on_topic_update {topic}:{message}')

    def compute(self, signals, type, IR_family, use_std_order, order, cutoff, window):
        """
            Apply a FIR\IIR filter on a channel from a list of signals.

            Keyword arguments:

            signals             -- An array of SignalModel to filter
            type                -- 'bandpass', 'lowpass', 'highpass', 'bandstop'
            IR_family           -- String : The filter is 'IIR' or 'FIR'.
            use_std_order       -- If True, the order is calculated based on the 
                                   formula: order=5*(sample_rate/lower frequency)
                                   If False, the order is taken from the [order]
                                   parameter.
            order               -- Length of the filter (the filter order + 1)
            cutoff              -- string of cutoff frequency, 2 values are needed for bandpass and stopband
                                   Cutoff frequency 
                                   between 0 and sample_rate/2
                                   For digital filters, if fs is specified, cutoff is in the same units as fs.
            window              -- Desired window ex: 'hamming'
                -- see: https://docs.scipy.org/doc/scipy/reference/generated/
                -- scipy.signal.get_window.html#scipy.signal.get_window
                -- for all options.

        """
        if DEBUG: 
            print('FilterSignal.compute')
            print(self.identifier + ' ' + IR_family + ' ' + type + ' ' + cutoff)

        self.clear_cache()

        if isinstance(signals,str) and signals=='':
            raise NodeInputException(self.identifier, "signals", f"FilterSignal this input is not connected.")
        if not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", f"FilterSignal input of wrong type. Expected: <class 'list'> received: {type(signals)}")
        elif isinstance(signals, list) and len(signals)==0:
            return {
                'signals': signals
            }
        
        # It is possible to bypass the filter by passing the input signals directly
        # to the output signals without any modification
        if self.activation_state == ActivationState.BYPASS:
            return {
                'signals': signals
            }

        map_object = map(float, cutoff.split())
        freqs = list(map_object)
        
        output_signals = []

        # Filter all channel
        for i, signal_model in enumerate(signals):

            if len(signal_model.samples) == 0:
                err_message = f' WARNING: Signal has no samples for channel:{signal_model.channel}'
                self._log_manager.log(self.identifier, err_message)
                print(err_message)
                raise NodeRuntimeException(self.identifier, "signals", f"{err_message}")   

            # Compute the order of the filter if the standard option has been
            # choosen.
            if use_std_order == 'True':
                order = 5*(signal_model.sample_rate/freqs[0])

            # Nyquist respect
            if max(freqs) >= (signal_model.sample_rate/2):
                err_message = "ERROR: Nyquist not respected, max frequency is {} Hz and sampling rate is {} Hz."\
                .format(max(freqs), signal_model.sample_rate)
                self._log_manager.log(self.identifier, err_message)
                print("FilterSignal " + err_message)
                raise NodeRuntimeException(self.identifier, "cutoff", f"{err_message}")   

            # We expect to have NaN values in chunk (if any)
            #   so we filter the signal (without nan values) even if it could have border effects
            #   and we reconstruct the filtered signal with the original NaN values.

            samples_to_filter = signal_model.samples
            # Extract where are the NaN values
            non_nan_indices = np.where(~np.isnan(samples_to_filter))
            if len(non_nan_indices) > 0:
                # reshape the i_nan_samples (x,1) to (x,)
                non_nan_indices = np.squeeze(non_nan_indices)
                samples_without_nan = samples_to_filter[non_nan_indices]

                # Setup the filter
                if IR_family=='IIR':
                    order_filtfilt = int(order)/2
                    sos = signal.butter(int(order_filtfilt), freqs,\
                        btype=type, output='sos', fs=signal_model.sample_rate)
                    filtered_signal = signal.sosfiltfilt(\
                        sos, samples_without_nan).copy() # .copy() is a hack to make 
                                                # recording the EDF with pyedflib much
                                                # much much faster
                else:
                    taps = signal.firwin(int(order), 
                        freqs, 
                        window=window, 
                        pass_zero=type,
                        fs=signal_model.sample_rate) 
                    filtered_signal = signal.filtfilt(
                        taps, 1, samples_without_nan).copy() # .copy() is a hack to make 
                                                # recording the EDF with pyedflib much
                                                # much much faster

            # Clone the signal object and set it back into the dictionary
            s = signal_model.clone(clone_samples=False)
            s.samples = np.empty_like(signal_model.samples)
            s.samples.fill(np.nan)
            if len(non_nan_indices) > 0:
                s.samples[non_nan_indices] = filtered_signal
            s.is_modified = True
            output_signals.append(s)

            # Write the cache
            cache = {}
            if config.is_dev: # Avoid save of the recording when not developping
                # Extract the number of channels
                channel_lst = [signal.channel for signal in output_signals]
                n_chan = len(np.unique(np.array(channel_lst)))
                cache['n_chan'] = n_chan
                cache['signals'] = output_signals
                self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'signals': output_signals
        }