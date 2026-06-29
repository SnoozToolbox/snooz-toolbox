"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    IRASAYASA
    
    This class implements signal decomposition to separate rhythmic (periodic/oscillatory) components 
    from arhythmic (aperiodic/broadband) components of EEG or other time-series signals. The algorithm 
    uses the YASA library's IRASA implementation to perform the spectral decomposition.
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

import numpy as np
import math
from fractions import Fraction
from scipy.signal import resample_poly, periodogram, welch
from scipy.optimize import curve_fit
from joblib import Parallel, delayed
import matplotlib.pyplot as plt
from scipy import fft as sp_fft
from CEAMSModules.PSGReader import SignalModel as test
import yasa

DEBUG = False

class IRASAYASA(SciNode):
    """
    Spectral power decomposition using IRASA algorithm (Iterative Rational Autocorrelation Decomposition Analysis).
    
    This class implements signal decomposition to separate rhythmic (periodic/oscillatory) components 
    from arhythmic (aperiodic/broadband) components of EEG or other time-series signals. The algorithm 
    uses the YASA library's IRASA implementation to perform the spectral decomposition.

    Inputs:
    -------
        signals : list of SignalModel objects
            - signal.samples : numpy array of shape (N_samples,) containing the raw signal data
            - signal.sample_rate : float, sampling rate of the signal in Hz
            - signal.channel : str, channel label/name for identification
            - signal.start_time : float, start time of the signal in seconds (optional)
        
        win_len_sec : float or str
            Window length in seconds for the spectral analysis (e.g., 4.0)
            Determines the time-frequency resolution of the analysis.
        
        win_step_sec : float or str
            Window step/overlap in seconds between consecutive FFT windows.
            Controls  the temporal resolution of the PSD computation.
        
        window_name : str
            Name of the windowing function to apply before FFT (e.g., 'hann', 'hamming', 'blackman').
            Reduces spectral leakage from windowing effects.
        
        first_freq : float or str
            Lower frequency boundary (Hz) for the IRASA decomposition analysis.
            Only frequency components within [first_freq, last_freq] are analyzed.
        
        last_freq : float or str
            Upper frequency boundary (Hz) for the IRASA decomposition analysis.
            Only frequency components within [first_freq, last_freq] are analyzed.
        
        flag : bool or str, optional (default: False)
            It does nothing right now and can be used in the future to control whether to bypass the computation or not.

    Outputs:
    --------
        rhythmic_psd : list of dicts
            List of dictionaries (one per input signal) containing rhythmic spectral components.
            Each dictionary contains:
                - 'psd' : numpy array of shape (N_epochs, N_freq_bins)
                  Rhythmic power spectral density (periodic component ratio)
                - 'freq_bins' : numpy array of shape (N_freq_bins,)
                  Frequency bins in Hz corresponding to the PSD spectrum
                - 'win_len' : float
                  Window length used for FFT in seconds
                - 'win_step' : float
                  Window step/overlap in seconds
                - 'sample_rate' : float
                  Sampling rate of the original signal in Hz
                - 'chan_label' : str
                  Channel label from the input signal
                - 'start_time' : float
                  Start time of the signal in seconds
                - 'end_time' : float
                  End time of the signal in seconds
                - 'duration' : float
                  Total duration of the signal in seconds
                - 'flag' : str (value: 'rhythmic')
                  Flag indicating this is the rhythmic component
        
        arhythmic_psd : list of dicts
            List of dictionaries (one per input signal) containing arhythmic spectral components.
            Each dictionary has identical structure to rhythmic_psd but with:
                - 'psd' : numpy array of shape (N_epochs, N_freq_bins)
                  Arhythmic power spectral density (aperiodic component)
                - 'flag' : str (value: 'arhythmic')
                  Flag indicating this is the arhythmic component
    """
    def __init__(self, **kwargs):
        """ Initialize module IRASAYASA """
        super().__init__(**kwargs)
        if DEBUG: print('IRASAYASA.__init__')

        # Input plugs
        InputPlug('signals',self)
        InputPlug('win_len_sec',self)
        InputPlug('win_step_sec',self)
        InputPlug('window_name',self)
        InputPlug('first_freq',self)
        InputPlug('last_freq',self)
        InputPlug('flag',self)
        

        # Output plugs
        OutputPlug('rhythmic_psd',self)
        OutputPlug('arhythmic_psd',self)
        
        self._is_master = False 
    
    def compute(self, signals, win_len_sec, win_step_sec, window_name, first_freq, last_freq, flag=False):
        """
        Decompose input signals into rhythmic and arhythmic spectral components using IRASA algorithm.
        
        This function processes each input signal by:
        1. Splitting the signal into overlapping windows of specified length
        2. Stacking windows to create a 2D signal matrix (epochs x samples)
        3. Applying IRASA decomposition to separate periodic (rhythmic) and aperiodic (arhythmic) components
        4. Computing power spectral densities for both components
        5. Returning structured output dictionaries with all spectral and metadata information

        Parameters:
        -----------
            signals : list of SignalModel objects
                List containing one or more SignalModel objects with:
                    - samples : numpy array of raw signal data (N_samples,)
                    - sample_rate : float, sampling rate in Hz
                    - channel : str, channel label/identifier
                    - start_time : float, optional start time of signal in seconds
            
            win_len_sec : float or str
                Window length in seconds for spectral analysis.
                Controls frequency resolution (lower = better frequency resolution)
                Typical range: 2.0 to 10.0 seconds
            
            win_step_sec : float or str
                Window step/stride in seconds between consecutive windows.
                Determines temporal resolution of the spectral analysis.
                Controls overlap between windows.
            
            window_name : str
                Name of windowing function to apply before FFT.
                Common options: 'hann', 'hamming', 'blackman', 'boxcar'
                Reduces spectral leakage from finite-length signal segments.
            
            first_freq : float or str
                Lower frequency boundary (Hz) for IRASA band-limited analysis.
                Only spectral components above this frequency are decomposed.
            
            last_freq : float or str
                Upper frequency boundary (Hz) for IRASA band-limited analysis.
                Only spectral components below this frequency are decomposed.
            
            flag : bool or str, optional (default: False)
                Currently does not affect computation. Can be used in the future to control bypassing the analysis.
        Returns:
        --------
            dict with two keys:
            
            'rhythmic_psd' : list of dicts
                Rhythmic (periodic/oscillatory) spectral components.
                One dict per input signal containing:
                    - 'psd' : numpy array (N_epochs, N_freq_bins)
                      Rhythmic power (ratio of combined to aperiodic spectrum)
                      Values > 1 indicate presence of periodic oscillations
                    - 'freq_bins' : numpy array (N_freq_bins,)
                      Frequency values in Hz for corresponding PSD bins
                    - 'win_len' : float
                      Window length in seconds
                    - 'win_step' : float
                      Window step in seconds
                    - 'sample_rate' : float
                      Sampling rate in Hz
                    - 'chan_label' : str
                      Input signal channel label
                    - 'start_time' : float
                      Start time of analysis in seconds
                    - 'end_time' : float
                      End time of analysis in seconds
                    - 'duration' : float
                      Total duration analyzed in seconds
                    - 'flag' : str = 'rhythmic'
                      Component type identifier
            
            'arhythmic_psd' : list of dicts
                Arhythmic (aperiodic/broadband) spectral components.
                One dict per input signal containing same structure as rhythmic_psd but:
                    - 'psd' : numpy array (N_epochs, N_freq_bins)
                      Background aperiodic power spectrum typically 1/f shaped
                    - 'flag' : str = 'arhythmic'
                      Component type identifier
        
        Raises:
        -------
            NodeInputException
                If signals is not a list
        
        Notes:
        ------
            - Windows with all NaN values are handled gracefully with NaN output
            - Output arrays are padded to consistent size across epochs
            - Division by zero in residu calculation is handled with NaN replacement
            - All output values are in power units (µV^2) for EEG signals
        """

        # Code examples

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", \
                f"RandB input of wrong type. Expected: <class 'list'> received: {type(signals)}")
        cache = {}

        win_len_sec = float(win_len_sec)
        win_step_sec = float(win_step_sec)
        first_freq = float(first_freq)
        last_freq = float(last_freq)
        if isinstance(flag, str):
            flag = flag.strip().lower() == 'true'
        # get data

        #sign2d = test.SignalModel.get_attribute(signals,'samples' , None)       
        fs = test.SignalModel.get_attribute(signals,'sample_rate' , None)
        allsignals = test.SignalModel.get_attribute(signals,'samples' , None)
        channel = test.SignalModel.get_attribute(signals,'channel' , None)
        rhythmic_psd = []
        arhythmic_psd = []
        # get data and split and stack accordingly
        for i, signal_model in enumerate(signals):
            sign2d_split, new_chan, start_time, end_time, new_dur = self.split_and_stack(signal_model, win_len_sec, fs)
            # compute rythmic spectral analysis
            if flag:
                continue
            else:
                residu, psd_aperiodic, freq_bins  = self.IRASA(sign2d_split, fs,first_freq,last_freq, window_name, window_sec=win_len_sec, new_chan=new_chan, return_fit=False)
            # Define output
            data_rhythmic = {}
            data_rhythmic['psd'] = residu
            data_rhythmic['freq_bins'] = freq_bins
            data_rhythmic['win_len'] = win_len_sec
            data_rhythmic['win_step'] = win_step_sec
            data_rhythmic['sample_rate'] = fs[i]
            data_rhythmic['chan_label'] = new_chan[0]
            data_rhythmic['start_time'] = start_time[0]
            data_rhythmic['end_time'] = end_time[-1]
            data_rhythmic['duration'] = sum(new_dur)
            data_rhythmic['flag'] = "rhythmic"

            data_arhythmic = {}
            data_arhythmic['psd'] = psd_aperiodic
            data_arhythmic['freq_bins'] = freq_bins
            data_arhythmic['win_len'] = win_len_sec
            data_arhythmic['win_step'] = win_step_sec
            data_arhythmic['sample_rate'] = fs[i]
            data_arhythmic['chan_label'] = new_chan[0]
            data_arhythmic['start_time'] = start_time[0]
            data_arhythmic['end_time'] = end_time[-1]
            data_arhythmic['duration'] = sum(new_dur)
            data_arhythmic['flag'] = "arhythmic"

            rhythmic_psd.append(data_rhythmic.copy())
            arhythmic_psd.append(data_arhythmic.copy())
        return {
            'rhythmic_psd': rhythmic_psd,
            'arhythmic_psd': arhythmic_psd
        }
    
    def split_and_stack(self, signals, win_len_sec, fs):
        # split data according to time and then stack it 

        nsample = int(win_len_sec*fs[0])
        sign = np.asarray(signals.samples)
        remainder = sign.shape[0] % nsample
        ####################
        if remainder > 0:
            if sign.shape[0]/2 > nsample:
                col_keep = (sign.shape[0]//nsample) * nsample
                cols_to_cut = sign.shape[0]-col_keep
                sign = sign[:-cols_to_cut]
            else:
                col_keep = nsample
                cols_to_cut = sign.shape[0]-col_keep
                sign = sign[:-cols_to_cut]
        if remainder ==  0:
            col_keep = sign.shape[0]
        ####################

        cols_per_div = sign.shape[0] // nsample
        segments = np.split(sign, cols_per_div, axis= 0)
        new_arr = np.vstack(segments)
        new_chan = np.repeat(np.asarray(signals.channel), cols_per_div)
        new_dur =  np.repeat(np.asarray(win_len_sec), cols_per_div)

        startTime = signals.start_time
        time_array = np.empty((cols_per_div, 2))
        for j in range(cols_per_div):
            endTime = startTime + (win_len_sec)
            time_array[j,0] = startTime
            time_array[j,1] =endTime
            startTime = startTime + win_len_sec
        start_time = time_array[:,0]
        end_time = time_array[:,1]

        return new_arr, new_chan, start_time, end_time, new_dur

    def IRASA(self, signals, fs, first_freq, last_freq, window_name, window_sec, new_chan, return_fit=False):
        # Apply the IRASA technique
        fs = fs[0]  # Use the first sampling rate (assuming all are the same)
        n_epochs = signals.shape[0]
        n_samples = signals.shape[1]  # Number of samples per epoch
        # Use fixed nfft for all scales to ensure consistent frequency grids based on the original paper's recommendation
        #fixed_nfft = 2 * (int(2 ** np.ceil(np.log2(n_samples)))) # The one suggested by the original paper
        fixed_nfft = sp_fft.next_fast_len(n_samples, real=True) # The one used in the Stft module
        # First pass: run analysis and determine target column count.
        periodic_rows = []
        aperiodic_rows = []
        freqs_rows = []
        residu_rows = []
        target_cols = 0

        for i in range(n_epochs):
            if np.isnan(signals[i, :]).any():
                periodic_rows.append(None)
                aperiodic_rows.append(None)
                freqs_rows.append(None)
                residu_rows.append(None)
                continue

            irasa_result = yasa.irasa(
                signals[i, :], fs, ch_names=new_chan[i],
                band=(first_freq, last_freq), win_sec=window_sec, return_fit=return_fit,
                kwargs_welch=dict(average="median", window=window_name, nfft=fixed_nfft, scaling='spectrum', detrend=False)
            )

            freqs_i = np.asarray(irasa_result[0])
            aperiodic_i = np.asarray(irasa_result[1])
            periodic_i = np.asarray(irasa_result[2])

            residu_i = None
            if return_fit and len(irasa_result) > 3:
                fit_params = irasa_result[3]
                residu_i = np.exp((-fit_params['Intercept'][0])) * (freqs_i)**((-fit_params['Slope'][0])) * (aperiodic_i + periodic_i)
            
            periodic_rows.append(periodic_i)
            aperiodic_rows.append(aperiodic_i)
            freqs_rows.append(freqs_i)
            residu_rows.append(residu_i)
            target_cols = max(target_cols, periodic_i.shape[0], aperiodic_i.shape[0], freqs_i.shape[0])

        # Second pass: allocate fixed 2D arrays and fill available values.
        if target_cols == 0: # Add this exception in case all the segments of a signal were Nan values
            target_cols = int(last_freq * window_sec)
        periodic_array = np.zeros((n_epochs, target_cols))
        aperiodic_array = np.zeros((n_epochs, target_cols))
        freqs = np.zeros(target_cols)
        residu_array = np.zeros((n_epochs, target_cols))

        for row_freqs in freqs_rows:
            if row_freqs is not None and row_freqs.shape[0] > 0:
                freqs[:row_freqs.shape[0]] = row_freqs
                break
            else:
                freqs = np.linspace(0, last_freq, num = target_cols+1)

        for i in range(n_epochs):
            p_i = periodic_rows[i]
            a_i = aperiodic_rows[i]
            r_i = residu_rows[i]
            if p_i is None or a_i is None:
                periodic_array[i, :] = np.nan
                aperiodic_array[i, :] = np.nan
                residu_array[i, :] = np.nan
                continue
            if p_i.shape[1] > 0:
                periodic_array[i, :p_i.shape[1]] = p_i
            if a_i.shape[1] > 0:
                aperiodic_array[i, :a_i.shape[1]] = a_i
            if return_fit and r_i is not None and r_i.shape[1] > 0:
                residu_array[i, :r_i.shape[1]] = r_i

        if return_fit:
            return residu_array, aperiodic_array, freqs

        # Compute ratio-style residu to match rhythmic_spectral_analysis output
        # residu = (aperiodic + periodic) / aperiodic = 1 + (periodic / aperiodic)
        with np.errstate(divide='ignore', invalid='ignore'):
            residu = (aperiodic_array + periodic_array) / aperiodic_array
            residu[~np.isfinite(residu)] = np.nan  # Handle division by zero or invalid values

        return residu, aperiodic_array, freqs