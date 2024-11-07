"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    This plugin resamples a signal.

    Parameters
    -----------
        signals : a list of SignalModel
            signal.samples : The actual signal data as numpy list
            signal.sample_rate : the original  sampling rate of the signal
            signal.channel : current channel label
        sample_rate : float
            The wanted sampling rate
        upsample : str (bool)
            Flag to allow upsampling.
            If False, the resampled data is never upsampled, the original sampling rate is kept.

    Returns
    -----------
        signals : a list of SignalModel
            signal.samples : The actual signal data as numpy list
            signal.sample_rate : the new sampling rate of the signal
            signal.channel : current channel label

"""
import config
from commons.NodeInputException import NodeInputException
from flowpipe.ActivationState import ActivationState
from flowpipe import SciNode, InputPlug, OutputPlug

import numpy as np
from scipy import signal, fft

DEBUG = False

class Resample(SciNode):
    """
    This class resamples a signal.

    Parameters
    -----------
        signals : a list of SignalModel
            signal.samples : The actual signal data as numpy list
            signal.sample_rate : the original  sampling rate of the signal
            signal.channel : current channel label
        sample_rate : float
            The wanted sampling rate
        upsample : str (bool)
            Flag to allow upsampling.
            If False, the resampled data is never upsampled, the original sampling rate is kept.

    Returns
    -----------
        signals : a list of SignalModel
            signal.samples : The actual signal data as numpy list
            signal.sample_rate : the new sampling rate of the signal
            signal.channel : current channel label

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('Resample.__init__')
        self._cache_duration = 30 # in seconds
        InputPlug('signals', self)
        InputPlug('sample_rate', self)
        InputPlug('upsample', self)
        OutputPlug('signals', self)

        self.dyadic_len = True


    def __del__(self):
        if DEBUG: print('Resample.__del__')


    def subscribe_topics(self):
        pass


    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'Resample.on_topic_update {topic}:{message}')


    def compute(self, signals, sample_rate, upsample):
        """
        To resamples a signal.

        Parameters
        -----------
            signals : a list of SignalModel
                signal.samples : The actual signal data as numpy list
                signal.sample_rate : the original  sampling rate of the signal
                signal.channel : current channel label
            sample_rate : float
                The wanted sampling rate
            upsample : str (bool)
                Flag to allow upsampling.
                If False, the resampled data is never upsampled, the original sampling rate is kept.

        Returns
        -----------
            signals : a list of SignalModel
                signal.samples : The actual signal data as numpy list
                signal.sample_rate : the new sampling rate of the signal
                signal.channel : current channel label

        """
        if DEBUG: print('Resample.compute')
        
        self.clear_cache()
        
        if not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", \
                f"Resample input of wrong type. Expected: <class 'list'> received: {type(signals)}")

        # Convert string to bool if needed
        if isinstance(upsample,str): 
            upsample = eval(upsample)

        if isinstance(sample_rate,str) and sample_rate=='':
            raise NodeInputException(self.identifier, "sample_rate", \
                f"Resample sample_rate has to be defined")            
        
        # It is possible to bypass the filter by passing the input signals directly
        # to the output signals without any modification
        if self.activation_state == ActivationState.BYPASS:
            return {
                'signals': signals
            }

        output_signals = []

        for i, signal_model in enumerate(signals):
            sample_rate = int(sample_rate)
            factor = signal_model.sample_rate / sample_rate
            if isinstance(signal_model.samples,list):
                nsamples = len(signal_model.samples)
            elif isinstance(signal_model.samples,np.ndarray):
                nsamples = signal_model.samples.size
            if self.dyadic_len:
                # Since resample is using the fft, we want to have dyadic number of samples to speed up performance
                fast_size = fft.next_fast_len(nsamples)
                num = int(fast_size / factor)
                real_num = int(round(nsamples / factor,0)) # final number of samples (without fast_size)
            else:
                real_num = int(round(nsamples / factor,0)) # final number of samples (without fast_size)
            
            if factor==1 or (not upsample and factor<=1): # also works with 1.0
                self._log_manager.log(self.identifier, "No resample needed")
                #resampled_signal = signal_model.clone(clone_samples=True)
                resampled_signal = signal_model # Use a reference to increase speed processing.
            elif self.dyadic_len:
                resampled_signal = signal_model.clone(clone_samples=False)
                # Since resample is using the fft, we zeros pad to have dyadic number of samples to speed up performance
                total_pading = (fast_size-nsamples)
                n_pad_start = int(total_pading/2) if (total_pading % 2) == 0 else int(total_pading/2)+1
                n_pad_end = int(total_pading/2)
                n_pad_resampled = int(round(n_pad_start/factor,0))
                resampled_signal.samples = signal.resample(np.pad(signal_model.samples,(n_pad_start,n_pad_end)), num)[n_pad_resampled:real_num+n_pad_resampled]
                resampled_signal.sample_rate = sample_rate
            else:
                resampled_signal = signal_model.clone(clone_samples=False)
                resampled_signal.samples = signal.resample(signal_model.samples, real_num)
                # if factor < 0:
                #     up_factor = int(1/factor)
                #     down_factor = 1
                # if factor > 0:
                #     up_factor = 1
                #     down_factor = int(factor)
                # resampled_signal.samples = signal.resample_poly(signal_model.samples, up_factor, down_factor)
                resampled_signal.sample_rate = sample_rate                
                
            output_signals.append(resampled_signal)

            # Cache only the data from the first channel
            cache = {}
            if config.is_dev: # Avoid save of the recording when not developping
                if i == 0:
                    input_nsamples = int(signal_model.sample_rate * self._cache_duration)
                    output_nsamples = int(sample_rate * self._cache_duration)

                    if isinstance(resampled_signal.samples,list):
                        nsamples_res = len(resampled_signal.samples)
                    elif isinstance(resampled_signal.samples,np.ndarray):
                        nsamples_res = resampled_signal.samples.size

                    cache['input_sample_rate'] = signal_model.sample_rate         
                    cache['input_sample_count'] = nsamples
                    cache['input_signal'] = signal_model.samples[0:input_nsamples]

                    cache['output_sample_rate'] = sample_rate
                    cache['output_sample_count'] = nsamples_res
                    cache['output_signal'] = resampled_signal.samples[0:output_nsamples]

                    cache['channel'] = signal_model.channel
                    
                    self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'signals': output_signals
        }
        