"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Compute the STFT (right-side only) on the signal splitted into 
    sliding windows.  Different normalization of the FFT output is available.
    
    Parameters
    -----------
    signals    : a list of SignalModel
                signal.samples : The actual signal data as numpy list
                signal.sample_rate : sampling rate of the signal (used to STFT)
                signal.channel : current channel label
    win_len_sec     : float
        window length in sec (how much data is taken for each fft)
    win_step_sec    : float 
        window step in sec (each time the fft is applied)
    zeros_pad       : bool, optional
        To zero pad the data to the next fast size of input data to fft.
        (the zeros padding can increases the frequency resolution and 
        decreases the computing time, rounding up to the next power of 2 is 
        not necessary optimal)
        (default = False)
    window_name     : string, optional
        Window's name to scale the extracted time series before applying the fft
    rm_mean         : bool, optional
        To remove mean of each window prior to the fft process
        (defautl = True)
    norm            : string, optional
        The normalization applied to the fft.
        (default = integrate)
        "integrate" : To integrate (sum) the signal power within a frequency 
                        range of the true spectrum (units² ex. µV²)                    
        "rms"       : To read the RMS value signals from the power spectral density.
                        (units²/Hz ex. µV²/Hz)
        "noise"     : To read the noise level from an FFT the power spectral density.
                        (units²/Hz ex. µV²/Hz)
        "no"        : No normalization
    filename        : string
        The python filename (including path) to save the STFT cache 
        in order to navigate through epochs.
        
    Returns
    -----------
    psd             : list of dicts
        key of the dict:
            psd : power (µV^2)
            freq_bins : frequency bins (Hz)
            win_len : windows length (s)
            win_step : windows step (s)
            sample_rate : sampling rate of the original signal (Hz)
            chan_label : channel label
"""
import numpy as np
import os
from scipy import signal

import config
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from flowpipe import SciNode, InputPlug, OutputPlug
from scipy import fft as sp_fft
from CEAMSModules.Stft import ts2windows as ts2w


DEBUG = False

class Stft(SciNode):
    """
        Compute the STFT (right-side only) on the signal splitted into 
        sliding windows.  Different normalization of the FFT output is available.
        
        Parameters
        -----------
        signals    : a list of SignalModel
                    signal.samples : The actual signal data as numpy list
                    signal.sample_rate : sampling rate of the signal (used to STFT)
                    signal.channel : current channel label
        win_len_sec     : float
            window length in sec (how much data is taken for each fft)
        win_step_sec    : float 
            window step in sec (each time the fft is applied)
        zeros_pad       : bool, optional
            To zero pad the data to the next fast size of input data to fft.
            (the zeros padding can increases the frequency resolution and 
            decreases the computing time, rounding up to the next power of 2 is 
            not necessary optimal)
            (default = False)
        window_name     : string, optional
            Window's name to scale the extracted time series before applying the fft
        rm_mean         : bool, optional
            To remove mean of each window prior to the fft process
            (defautl = True)
        norm            : string, optional
            The normalization applied to the fft.
            (default = integrate)
            "integrate" : To integrate (sum) the signal power within a frequency 
                            range of the true spectrum (units² ex. µV²)                    
            "rms"       : To read the RMS value signals from the power spectral density.
                            (units²/Hz ex. µV²/Hz)
            "noise"     : To read the noise level from an FFT the power spectral density.
                            (units²/Hz ex. µV²/Hz)
            "no"        : No normalization
        filename        : string
            The python filename (including path) to save the STFT cache 
            in order to navigate through epochs.
            
        Returns
        -----------
        psd             : list of dicts
            key of the dict:
                psd : power (µV^2) narray [n_fft_windows x n_frequency_bins]
                freq_bins : frequency bins (Hz)
                win_len : windows length (s)
                win_step : windows step (s)
                sample_rate : sampling rate of the original signal (Hz)
                chan_label : channel label
                start_time : start (s) of the signal (item of signals) on which the ffts are performed
                end_time : end (s) of the signal (item of signals) on which the ffts are performed
                duration : duraiton (s) of the signal (item of signals) on which the ffts are performed
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('Stft.__init__')
        self._cache_duration = 30 # in seconds
        InputPlug('signals', self)
        InputPlug('win_len_sec', self)
        InputPlug('win_step_sec', self)
        InputPlug('zeros_pad', self)
        InputPlug('window_name', self)
        InputPlug('rm_mean', self)
        InputPlug('norm', self)
        InputPlug('filename', self)
        OutputPlug('psd', self)

    def __del__(self):
        if DEBUG: print('Stft.__del__')

    def subscribe_topics(self):
        pass

    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'Stft.on_topic_update {topic}:{message}')

    def compute(self, signals, win_len_sec, win_step_sec, zeros_pad, window_name,
        rm_mean, norm, filename):
        """
            Compute the STFT (right-side only) on the signal splitted into 
            sliding windows.  Different normalization of the FFT output is available.
            
            Parameters
            -----------
            signals    : a list of SignalModel
                        signal.samples : The actual signal data as numpy list
                        signal.sample_rate : sampling rate of the signal (used to STFT)
                        signal.channel : current channel label
            win_len_sec     : float
                window length in sec (how much data is taken for each fft)
            win_step_sec    : float 
                window step in sec (each time the fft is applied)
            zeros_pad       : bool, optional
                To zero pad the data to the next fast size of input data to fft.
                (the zeros padding can increases the frequency resolution and 
                decreases the computing time, rounding up to the next power of 2 is 
                not necessary optimal)
                (default = False)
            window_name     : string, optional
                Window's name to scale the extracted time series before applying the fft
            rm_mean         : bool, optional
                To remove mean of each window prior to the fft process
                (defautl = True)
            norm            : string, optional
                The normalization applied to the fft.
                (default = integrate)
                "integrate" : To integrate (sum) the signal power within a frequency 
                                range of the true spectrum (units² ex. µV²)                    
                "rms"       : To read the RMS value signals from the power spectral density.
                                (? units²/Hz ex. µV²/Hz)
                "noise"     : To read the noise level from an FFT the power spectral density.
                                (units²/Hz ex. µV²/Hz)
                "no"        : No normalization
            filename        : string
                The python filename (including path) to save the STFT cache 
                in order to navigate through epochs.
                        
            Returns
            -----------
            psd             : list of dicts (length of signals)
                One item of psd per item of signals.
                key of each dict:
                    psd : power (µV^2) narray [n_fft_windows x n_frequency_bins]
                    freq_bins : frequency bins (Hz)
                    win_len : windows length (s)
                    win_step : windows step (s)
                    sample_rate : sampling rate of the original signal (Hz)
                    chan_label : channel label
                    start_time : start (s) of the signal (item of signals) on which the ffts are performed
                    end_time : end (s) of the signal (item of signals) on which the ffts are performed
                    duration : duraiton (s) of the signal (item of signals) on which the ffts are performed

        """
        if DEBUG: print('Stft.compute')

        # Clear the cache and the file on the disk (usefull for the second run)
        self.clear_cache()
        if not filename=='':
            if os.path.exists(filename):
                os.remove(filename)
                war_message = "WARNING : {} has been erased".format(filename)
                self._log_manager.log(self.identifier, war_message)
        
        if not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", \
                f"Stft input of wrong type. Expected: <class 'list'> received: {type(signals)}")

        psd = []

        # Default init is 1 sec
        win_len_sec = float(win_len_sec)
        win_step_sec = float(win_step_sec)

        if isinstance(zeros_pad,str):
            zeros_pad = eval(zeros_pad)
        if isinstance(rm_mean,str):
            rm_mean = eval(rm_mean)      

        # Apply FFT to all channels
        cache = {}
        for i, signal_model in enumerate(signals):
            fs = signal_model.sample_rate
            nsample_win = win_len_sec*fs
            if not nsample_win.is_integer():
                # Compute the real win_len used
                if DEBUG:
                    print("Stft.Warning : win_len {} is changed for {}".\
                        format(win_len_sec, int(round(nsample_win))/fs))
                self._log_manager.log(self.identifier, "win_len {} is changed for {}".\
                    format(win_len_sec, int(round(nsample_win))/fs))
                win_len_sec = int(round(nsample_win))/fs

            nsample_step = win_step_sec*fs
            if not nsample_step.is_integer():
                # Compute the real win_step used
                if DEBUG:
                    print("Stft.Warning : win_step {} is changed for {}".\
                        format(win_step_sec, int(round(nsample_step))/fs))
                self._log_manager.log(self.identifier, "win_step {} is changed for {}".\
                    format(win_len_sec, int(round(nsample_step))/fs))
                win_step_sec = int(round(nsample_step))/fs   

            if nsample_win > len(signal_model.samples):
                self._log_manager.log(self.identifier, f"Stft - The signal {i} from {signal_model.channel} "\
                    + f"is shoter than the fft window length of {win_len_sec}s.")

            data = {}
            data['psd'], data['freq_bins'] = self.fft_norm(
                                        signal_model.samples,
                                        fs,
                                        win_len_sec,
                                        win_step_sec,
                                        zeros_pad,
                                        window_name,
                                        rm_mean,
                                        norm)
            data['win_len'] = win_len_sec
            data['win_step'] = win_step_sec
            data['sample_rate'] = fs
            data['chan_label'] = signal_model.channel
            data['start_time'] = signal_model.start_time
            data['end_time'] = signal_model.end_time
            data['duration'] = signal_model.duration

            # psd is a list of dicts
            #  each dict contains the channel and the psd information 
            psd.append(data)

            # The cache contains only the header of the first signal model (first epoch, first channel)
            # but contains the psd value concatenated from the signals of the selected channel to display
            # Works only with one channel
            if config.is_dev: # Avoid save of the recording when not developping
                if len(cache)==0:
                    cache['psd'] = data['psd']
                    cache['freq_bins'] = data['freq_bins']
                    cache['channel'] = signal_model.channel
                    cache['sample_rate'] = signal_model.sample_rate
                    cache['win_step_sec'] = win_step_sec
                    cache['win_len'] = win_len_sec
                    cache['filename'] = filename
                    self._cache_manager.write_mem_cache(self.identifier, cache)
                else:
                    cache['psd'] = np.concatenate((cache['psd'],data['psd']),axis=0)
                
            if not filename=='':
                # Save the whole data into the file in settings (on disk)
                # The cache is also saved on the disk to navigate through windows
                np.save(filename, cache)
                war_message = "WARNING : {} has been written".format(filename)
                self._log_manager.log(self.identifier, war_message)

        return {
            'psd': psd
        }


    def fft_norm(self, ts_signal, fs, win_len_sec, win_step_sec, zeros_pad=False, \
                window_name='hann', rm_mean=True, norm='integrate'):
        """ Compute the FFT (right-side only) on the signal splitted into 
        sliding windows.  Different normalization of the FFT output is available.
        
        Parameters
        -----------
        ts_signal        : any form that can be converted to an array 1-d array. 
            This includes lists, tuples and ndarrays. 
            Array of data, the time series of the signal in physical values
        fs              : float
            Sampling frequency (Hz)
        win_len_sec     : float
            window length in sec (how much data is taken for each fft)
        win_step_sec    : float 
            window step in sec (each time the fft is applied)
        zeros_pad       : bool, optional
            To zero pad the data to the next fast size of input data to fft.
            (the zeros padding can increases the frequency resolution and 
            decreases the computing time, rounding up to the next power of 2 is 
            not necessary optimal)
            (default = False)
        window_name     : string, optional
            Window's name to scale the extracted time series before applying the fft
        rm_mean         : bool, optional
            To remove mean of each window prior to the fft process
            (defautl = True)
        norm            : string, optional
            The normalization applied to the fft.
            (default = integrate)
            "integrate" : To integrate (sum) the signal power within a frequency 
                            range of the true spectrum (units² ex. µV²)                    
            "rms"       : To read the RMS value signals from the power spectral density.
                            (? units²/Hz ex. µV²/Hz)
            "noise"     : To read the noise level from an FFT the power spectral density.
                            (units²/Hz ex. µV²/Hz)
            "no"        : No normalization
            
        Returns
        -----------
        psd_data        : ndarray [fft_win_count x 0-fs/2 Hz]
            Power spectral density data as an array.
            A value of the power for each frequency bin for each extracted window.
        freq_bins       : ndarray
            The frequency bins array (Hz)
        
        Usage : psd_data, freq_bins = compute(ts_signal, 100, 1, 0.5, 1)
        
        Inspired by : 
        https://github.com/scipy/scipy/blob/9da1c4bad19f434e7e511a164e0a7af954a4202d/scipy/signal/spectral.py#L1869
        
        
        """    
        
        #---------------------
        # General init
        
        # Number of sample to extract from the time series to perform the FFT
        nsample_win = int(win_len_sec * fs)
        # Number of samples to step between each fft window
        nsample_step = int(win_step_sec * fs)
        # Number of samples that overlap between 2 windows
        nsample_ovlp = nsample_win - nsample_step  
        # Frequency range
        fbin = fs/nsample_win
        #---------------------

        # total number of samples included in the fft window
        if zeros_pad:
            nsample_fft = sp_fft.next_fast_len(nsample_win, real=True)
            if nsample_fft != nsample_win:
                print("The FFT is computed with {} samples".format(nsample_fft))
        else:
            nsample_fft = nsample_win
        
        # Ensure we have np.arrays, get outdtype
        ts_signal = np.asarray(ts_signal)
            
        # Calculate the number of frequency bins (= number of cols in the output)
        freq_bins = sp_fft.rfftfreq(nsample_fft, 1./fs)
        # frequency bin resolution = (FS/2)/(N/2) = 50Hz/15=3.33

        # Make sure the signal is 1-D
        if ts_signal.ndim>1:
            ts_signal = np.squeeze(ts_signal)  

        # Number of windows : if 5 samples and less are missing they are added to have an fft window
        MAX_SAMPLES_PAD = 5 # Stellate bug with non integer sampling rate, we dont want to skip an almost complete window for 5 samples
        nsample_avail = len(ts_signal)-nsample_win
        if nsample_avail<-MAX_SAMPLES_PAD:
            psd_data = np.empty((1,len(freq_bins)))
            psd_data[:]=np.NaN
            return psd_data, freq_bins
        else:
            nwin_tot_real = nsample_avail/nsample_step+1# we keep an extra windows higher
            if not nwin_tot_real.is_integer():
                nwin_max = np.ceil(nwin_tot_real)
                nmiss_sample = len(ts_signal)-(nwin_max*nsample_step)
                if (nmiss_sample<0) and (nmiss_sample>-MAX_SAMPLES_PAD):
                    ts_signal = np.concatenate((ts_signal,np.zeros(int(np.abs(nmiss_sample)))),axis=0)

        # To shape a 1-D tall array into 2D array of windows such as [nwin x nsample_win] 
        # Strides are made to avoid data duplication when there is overlapping
            # Stellate bug with epoc shorter than 30 s
            # number of sample available to start a window
            # Some samples could be missing when using nsample_ovlp 
        ts_in_win = ts2w.compute_windows(ts_signal, nsample_win, nsample_ovlp)
            #index_last_start = nsample_step*ts_in_win.shape[0]
            #ts_last_win = ts_signal[index_last_start:]
        
        # (1) Remove the mean of the signal, dc offset
        if rm_mean:
            # when the data is modified, the strides are modified to avoid
            # modifying twice the data in memory
            # Here the data is duplicated in memory (when there is overlap)
            ts_in_win = ts_in_win - np.mean(ts_in_win, axis=1, keepdims=True)
                #ts_last_win = ts_last_win - np.mean(ts_last_win)
        
        # (2) Apply the window scaling function (ie hanning window)
        # Window Scaling Function - weight the values in the analysis window 
        # ie hann = w(n)=0.5−0.5cos(2πn/(M−1)) 0≤n≤M−1
        win_scale_coeff = signal.windows.get_window(window_name, nsample_win)
            #win_scale_last = signal.windows.get_window(window_name,len(ts_last_win))
        # Reference : Hanspeter Schmid, 2012
        # Coherent gain for reading signal RMS values
        coherent_gain = sum(win_scale_coeff)/len(win_scale_coeff)
            #coh_gain_last = sum(win_scale_last)/len(win_scale_last)
        # Noise gain for IntegSpectPow
        noise_gain = sum(win_scale_coeff**2)/len(win_scale_coeff)    
            #noise_g_last = sum(win_scale_last**2)/len(win_scale_last)    
        # (3) Perform the one sided right fft (*** zeros paddind included if any ***)
        # ts_in_win must be [nwindows x nsamples_in_win] because the fft is applied 
        # on the last dimension (-1 which is on every row)
        fft_result_win = sp_fft.rfft(win_scale_coeff*ts_in_win, n=nsample_fft, axis=1)
            #fft_result_last_win = sp_fft.rfft(win_scale_last*ts_last_win, n=nsample_fft)
            #fft_result = np.vstack((fft_result_win, fft_result_last_win))
        # (4) Normalization
        if norm=="integrate":
            # IntegSpectPow Normalization (Hanspeter Schmid, 2012)
            fft_norm = fft_result_win/nsample_win
            # The imaginary part should be zero
            psd_data = abs((2.0 * np.conjugate(fft_norm) * fft_norm)/noise_gain)
        elif norm=="rms":
            fft_norm = fft_result_win/(nsample_win*coherent_gain)
            # The imaginary part should be zero
            psd_data = abs(2.0 * np.conjugate(fft_norm) * fft_norm)
        elif norm=="noise":
            # supposed to be equivalent to pwelch from matlab
            fft_norm = fft_result_win/nsample_win
            # The imaginary part should be zero
            psd_data = abs((2.0 * np.conjugate(fft_norm) * fft_norm)/(noise_gain*fbin))
        else:
            # The imaginary part should be zero
            psd_data = abs(2.0 * np.conjugate(fft_result_win) * fft_result_win)
            
        # special case for psd_data at the frequency 0
        psd_data[0:,0] = psd_data[0:,0]/2
            
        return psd_data, freq_bins