"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    MovingRMS
    Compute RMS (Root Mean Squared) value on a moving window.

"""
from commons.NodeInputException import NodeInputException
from flowpipe.ActivationState import ActivationState
from flowpipe import SciNode, InputPlug, OutputPlug
from CEAMSModules.Stft import ts2windows as ts2w

import numpy as np

DEBUG = False

class MovingRMS(SciNode):
    """
    Compute RMS (Root Mean Squared) value on a moving window.

    Parameters
    -----------
        signals : a list of SignalModel
            signal.samples : The actual signal data as numpy list
            signal.sample_rate : the original  sampling rate of the signal
            signal.channel : current channel label
        win_len_sec     : float
            window length in sec (how much data is taken for each RMS computation)
        win_step_sec    : float 
            window step in sec (each time the RMS computation is applied)
        
    Returns
    -----------  
        moving_RMS_values: dict of SignalModel object, the key is the label of the channel.
            moving_RMS_values[channel_label].samples: One RMS value per moving window as numpy array.
        
    """
    def __init__(self, **kwargs):
        """ Initialize module MovingRMS """
        super().__init__(**kwargs)
        if DEBUG: print('SleepReport.__init__')

        # Input plugs
        InputPlug('signals',self)
        InputPlug('win_len_sec',self)
        InputPlug('win_step_sec',self)

        # Output plugs
        OutputPlug('moving_RMS_values',self)

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
        self._cache_duration = 30 # in seconds
    

    def compute(self, signals, win_len_sec, win_step_sec):
        """
        Compute RMS (Root Mean Squared) value on a moving window.

        Parameters
        -----------
            signals : a list of SignalModel
                signal.samples : The actual signal data as numpy list
                signal.sample_rate : the original  sampling rate of the signal
                signal.channel : current channel label 
            win_len_sec     : float
                window length in sec (how much data is taken for each RMS computation)
            win_step_sec    : float 
                window step in sec (each time the RMS computation is applied)
            
        Returns
        -----------  
            moving_RMS_values: list of SignalModel object
                item.samples: One RMS value per moving window as numpy array.
                item.channel: channel label of the signal item 
                
        """

        self.clear_cache()

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if isinstance(signals,str) and signals=='':
            raise NodeInputException(self.identifier, "signals", f"MovingRMS this input is not connected.")
        elif not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", \
                f"MovingRMS input of wrong type. Expected: <class 'list'> received: {type(signals)}")     
        elif len(signals)==0:
            return {
                'moving_RMS_values': []
            }            
        
        # It is possible to bypass the "MovingRMS" by passing the input signals directly
        # to the output moving_RMS_values without any modification
        if self.activation_state == ActivationState.BYPASS:
            return {
                'moving_RMS_values': signals
            }        

        # Convert input parameter
        try: 
            win_len_sec = float(win_len_sec)
            win_step_sec = float(win_step_sec)
        except:
            raise NodeInputException(self.identifier, "win_len_sec or win_step_sec",\
                 f"MovingRMS the type of these inputs is unexpected.")

        # Create an empty list
        moving_RMS_values = []

        # Loop through all channels
        for i, signal_model in enumerate(signals):
        #for i, (label, channel) in enumerate(signals.items()):

            if len(signal_model.samples) == 0:
                err_message = f' WARNING: Signal has no samples for channel:{signal_model.channel}'
                self._log_manager.log(self.identifier, err_message)
                print(err_message)
                continue

            # Convert the signal into windows
            fs = signal_model.sample_rate
            nsample_win = win_len_sec*fs
            if not nsample_win.is_integer():
                # Compute the real win_len used
                err_message = f' Warning : win_len_sec {win_len_sec} is changed for {int(round(nsample_win))/fs}'
                self._log_manager.log(self.identifier, err_message)               
                win_len_sec = int(round(nsample_win))/fs

            nsample_step = win_step_sec*fs
            if not nsample_step.is_integer():
                # Compute the real win_step used
                err_message = f' Warning : win_step_sec {win_step_sec} is changed for {int(round(nsample_step))/fs}'
                self._log_manager.log(self.identifier, err_message)        
                win_step_sec = int(round(nsample_step))/fs

            nsample_win = int(round(win_len_sec*fs))
            nsample_ovlp = int(round((win_len_sec-win_step_sec)*fs))

            # To shape a 1-D tall array into 2D array of windows such as [nwin x nsample_win] 
            # Strides are made to avoid data duplication when there is overlapping
            ts_in_win = ts2w.compute_windows(signal_model.samples.copy(), nsample_win, nsample_ovlp)

            # Compute power 2 of the time series 
            # when the data is modified, the strides are modified to avoid
            # modifying twice the data in memory
            # Here the data is duplicated in memory (when there is overlap)
            ts_in_win = np.power(ts_in_win, 2)

            # Compute the average of each window
            ts_in_win_avg = np.nanmean(ts_in_win, axis=1)

            # Compute squared root
            ts_in_win_sqrt = np.sqrt(ts_in_win_avg)

            # Clone signals without the samples wo create a list of SignalModel
            moving_RMS_values.append(signal_model.clone(clone_samples=False))
            # Save the RMS values with the channel information
            moving_RMS_values[-1].samples = ts_in_win_sqrt

            # Cache only the data from the first channel
            if i == 0:
                nsamples = int(signal_model.sample_rate * self._cache_duration)
                nwindows = int(self._cache_duration / win_step_sec)
                cache = {}
                cache['in_signal'] = signal_model.samples[0:nsamples]
                cache['moving_RMS_values'] = moving_RMS_values[i].samples[0:nwindows]
                cache['channel'] = signal_model.channel
                cache['sample_rate'] = signal_model.sample_rate
                cache['win_step_sec'] = win_step_sec
                self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'moving_RMS_values': moving_RMS_values
            }