"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    WindowsToSamples
    To convert information based on windows (i.e. RMS energy) into a time series 
    (i.e. RMS values synchronized - aligned with the eeg signal).  
    If the step window used to compute the information is longer than 1/sampling rate
    the window value is replicated along windows step length to match the 
    sampling rate of the signal in input.
"""
from commons.NodeInputException import NodeInputException
from flowpipe import SciNode, InputPlug, OutputPlug
from flowpipe.ActivationState import ActivationState

import numpy as np

DEBUG = False

class WindowsToSamples(SciNode):
    """
    To convert information based on windows (i.e. RMS energy) into a time series 
    (i.e. RMS values synchronized - aligned with the eeg signal).  
    If the step window used to compute the information is longer than 1/sampling rate
    the window value is replicated along windows step length to match the 
    sampling rate of the signal in input.

    Parameters
    -----------
        "signals_windows": list of SignalModel
            signal_windows.samples : The actual windows data as array.
            signal.sample_rate : the original  sampling rate of the signal
            signal.channel : current channel label 
        "win_step_sec": Float
            The window step length in seconds used to compute the information signals_windows.
        
    Returns
    -----------  
        "samples_values": dict of SignalModel, the key is the label of the channel.
            samples_values[channel_label].samples : The actual samples values as array
        
    """
    def __init__(self, **kwargs):
        """ Initialize module WindowsToSamples """
        super().__init__(**kwargs)

        # Input plugs
        InputPlug('signals_windows',self)
        InputPlug('win_step_sec',self)
        
        # Output plugs
        OutputPlug('samples_values',self)

        # Init module variables
        self.this_is_an_example_you_can_delete_it = 0

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 

        # Signal duration in second to save in the cache
        self._cache_duration = 30
    

    def compute(self,signals_windows,win_step_sec):
        """
        To convert information based on windows (i.e. RMS energy) into a time series 
        (i.e. RMS values synchronized - aligned with the eeg signal).  
        If the step window used to compute the information is longer than 1/sampling rate
        the window value is replicated along windows step length to match the 
        sampling rate of the signal in input.

        Parameters
        -----------
            "signals_windows": list of SignalModel
                signal_windows.samples : The actual windows data as array.
                signal.sample_rate : the original  sampling rate of the signal
                signal.channel : current channel label 
            "win_step_sec": Float
                The window step length in seconds used to compute the information signals_windows.
            
        Returns
        -----------  
            "samples_values": dict of SignalModel, the key is the label of the channel.
                samples_values[channel_label].samples : The actual samples values as array
        """

        self.clear_cache()

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if isinstance(signals_windows,str) and signals_windows=='':
            raise NodeInputException(self.identifier, "signals_windows", \
                f"WindowsToSamples this input is not connected.")
        elif not isinstance(signals_windows,list):
            raise NodeInputException(self.identifier, "signals_windows", \
                f"WindowsToSamples input of wrong type. Expected: <class 'list'> received: {type(signals_windows)}")              
        
        # Convert input parameter
        try: 
            win_step_sec = float(win_step_sec)
        except:
            raise NodeInputException(self.identifier, "win_step_sec",\
                 f"WindowsToSamples the type of these inputs is unexpected.")

        # It is possible to bypass the "WindowsToSamples" by passing the input 
        # signals_windows to the output samples_values without any modification
        if self.activation_state == ActivationState.BYPASS:
            return {
                'samples_values': signals_windows
            }        

        # Create an empty list
        samples_values = []

        # Loop through all channels
        for i, signal_window in enumerate(signals_windows):
        #for i, (label, channel) in enumerate(signals.items()):

            # Extract the array to convert from windows to samples
            signals_windows_cur = signal_window.samples

            # Clone signals without the samples to create a SignalModel
            samples_values.append(signal_window.clone(clone_samples=False))

            fs = signal_window.sample_rate

            if len(signal_window.samples) == 0:
                err_message = f' WARNING: Signal has no samples for channel:{signal_window.channel}'
                self._log_manager.log(self.identifier, err_message)
                print(err_message)
                continue

            # Convert a by-window information to by-sample information to match the signal
            if win_step_sec != 0:
                nsample_step = win_step_sec*fs
                if not nsample_step.is_integer():
                    # Compute the real win_step used
                    err_message = f' Warning : win_step_sec {win_step_sec} is changed for {int(round(nsample_step))/fs}'
                    self._log_manager.log(self.identifier, err_message)        
                    win_step_sec = int(round(nsample_step))/fs
                    nsample_step = int(round(win_step_sec*fs))
                reps = np.ones(signals_windows_cur.shape[0],dtype=np.int64) * int(nsample_step)
                signal_sample_cur = np.repeat(signals_windows_cur, reps)
                samples_values[-1].samples = signal_sample_cur
            else:
                samples_values[-1].samples = signals_windows_cur

            # # Different length when the last window is incomplete
            # # I think the best way is to duplicate the last info
            # if len(signal_chan.samples) > len(samples_values):
            #     values_2_pad = np.ones(len(signal_chan.samples)-len(det_act_smp[i]))*det_act_smp[i][-1]
            #     det_act_smp[i] = np.concatenate((det_act_smp[i],values_2_pad))
            # elif len(signal_chan.samples) < len(det_act_smp[i]):
            #     err_message = 'ERROR : unexpected length of windows detection'
            #     self._log_manager.log(self.identifier, err_message)

            # Cache only the data from the first signal
            if i == 0:
                cache = {}
                nwindows = int(round(self._cache_duration/win_step_sec))
                if len(signal_window.samples)>=nwindows:
                    nsamples = int(round(fs * self._cache_duration))
                else:
                    nwindows = len(signal_window.samples)
                    cur_cache_dur = nwindows * win_step_sec
                    nsamples = int(round(fs * cur_cache_dur))
                cache['samples_values'] = samples_values[-1].samples[0:nsamples]                  
                cache['channel'] = signal_window.channel
                cache['sample_rate'] = fs
                self._cache_manager.write_mem_cache(self.identifier, cache)            

        return {
            'samples_values': samples_values
            }
