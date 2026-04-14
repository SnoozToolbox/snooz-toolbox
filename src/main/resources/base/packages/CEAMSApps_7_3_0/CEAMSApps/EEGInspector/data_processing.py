"""Data loading and signal processing"""

import mne
import numpy as np
from scipy import fft
from scipy.signal import resample, butter, filtfilt
from PySide6.QtCore import QThread
from qtpy.QtCore import Signal as pyqtSignal

from CEAMSModules.PSGReader.PSGReaderManager import PSGReaderManager
from .constants import *

class DataProcessor(QThread):
    """Thread for loading and processing EEG data"""
    data_loaded = pyqtSignal()
    error_occurred = pyqtSignal(str)

    def __init__(self, input_dir, selected_channels, selected_montage):
        super().__init__()
        self.input_dir = input_dir
        self.selected_channels = selected_channels
        self._selected_montage = selected_montage
        self.raw_eeg = None
        self.raw_eeg_display = None
        self._events = None

    def cleanup(self):
        """Clean up data processor resources - AGGRESSIVE VERSION"""
        import gc
        
        # Clear raw data objects and force memory release
        if self.raw_eeg is not None:
            # Force deletion of underlying data
            if hasattr(self.raw_eeg, '_data'):
                del self.raw_eeg._data
            self.raw_eeg = None
        
        if self.raw_eeg_display is not None:
            # Force deletion of underlying data
            if hasattr(self.raw_eeg_display, '_data'):
                del self.raw_eeg_display._data
            self.raw_eeg_display = None
            
        self._events = None
        
        # Clear arrays and lists
        if hasattr(self, 'selected_channels'):
            if hasattr(self.selected_channels, 'clear'):
                self.selected_channels.clear()
            else:
                self.selected_channels = None
        
        # NOUVEAU: Nettoyer toutes les variables d'instance
        for attr_name in dir(self):
            if not attr_name.startswith('_') and attr_name not in ['cleanup', 'run', 'load_data']:
                try:
                    attr = getattr(self, attr_name)
                    if hasattr(attr, '__array__'):  # NumPy array
                        delattr(self, attr_name)
                    elif str(type(attr)).find('mne') != -1:  # MNE object
                        delattr(self, attr_name)
                except:
                    pass
        
        # Force immediate garbage collection
        gc.collect()
        
        # Additional: Try to release numpy memory
        try:
            import numpy as np
            # Clear numpy internal caches
            np.seterr(all='ignore')  # Prevent warnings during cleanup
        except:
            pass

    def run(self):
        try:  
            success = self.load_data()
            if success:
                self.data_loaded.emit()
            else:
                self.error_occurred.emit("Failed to load data")
        except Exception as e:
            self.error_occurred.emit(str(e))

    def load_data(self):
        """Load and process EEG data"""
        psg_reader_manager = PSGReaderManager()
        psg_reader_manager._init_readers()
        
        # Open file and get signal models
        output = psg_reader_manager.open_file(self.input_dir)
        if isinstance(output, tuple) and len(output) == 2:
            success, error = output
        else:
            success = output
            
        if not success:
            error_msg = error if error else "ERROR PSGReaderManager could not open the file"
            self.error_occurred.emit(error_msg)
            return False
            
        self._events = psg_reader_manager.get_events()
        signal_models = psg_reader_manager.get_signal_models(self._selected_montage, self.selected_channels)
        
        # Check for discontinuous signals
        section_count = psg_reader_manager.current_reader.get_signal_section_count()
        if section_count > 1:
            self.error_occurred.emit("The signal is discontinuous and cannot be visualized.")
            return False
            
        psg_reader_manager.close_file()

        # Process signals
        self.cutoff_freq = self._process_signals(signal_models)

        return True

    def _process_signals(self, signal_models):
        """Apply filtering and resampling to signals"""
        max_sample_rate = max([s.sample_rate for s in signal_models])
        target_rate = TARGET_RATE_LOW if max_sample_rate % 5 == 0 else TARGET_RATE_HIGH
        if max_sample_rate <= TARGET_RATE_LOW:
            target_rate = max_sample_rate

        processed_signals = []
        self._start_time = signal_models[0].start_time
        self._duration = signal_models[0].duration

        # Apply low-pass filter if needed and resamplem force a integer as frequency bin
        cutoff_freq = LOWPASS_CUTOFF_HZ if (target_rate / 2) > LOWPASS_CUTOFF_HZ else int(target_rate / 2)
        for signal_model in signal_models:
            if signal_model.sample_rate > target_rate:
                b, a = butter(FILTER_ORDER, cutoff_freq, fs=signal_model.sample_rate, btype='low', analog=False)
                signal_model.samples = filtfilt(b, a, signal_model.samples)
            
            if signal_model.sample_rate != target_rate:
                processed_signal = self._resample_signal(signal_model, target_rate)
            else:
                processed_signal = signal_model.clone(clone_samples=False)
                processed_signal.samples = signal_model.samples * SCALE_FACTOR_UV
                
            processed_signals.append(processed_signal)

        # Create full resolution raw object
        self._create_raw_object(processed_signals)
        
        # Clear processed_signals immediately to free memory
        del processed_signals
        import gc
        gc.collect()
        
        # Only create display version if needed (for long recordings)
        if self._duration > SLEEP_RECORDING_THRESHOLD_SEC:
            self._create_display_version(EPOCH_SLEEP_LONG_SEC)

        return cutoff_freq


    def _resample_signal(self, signal_model, target_rate):
        """Resample a single signal using FFT optimization"""
        factor = signal_model.sample_rate / target_rate
        nsamples = len(signal_model.samples)
        
        # Use FFT-optimized resampling
        fast_size = fft.next_fast_len(nsamples)
        num = int(fast_size / factor)
        real_num = int(round(nsamples / factor, 0))

        resampled_signal = signal_model.clone(clone_samples=False)
        
        # Zero-pad for FFT optimization
        total_padding = fast_size - nsamples
        n_pad_start = int(total_padding / 2) if (total_padding % 2) == 0 else int(total_padding / 2) + 1
        n_pad_end = int(total_padding / 2)
        n_pad_resampled = int(round(n_pad_start / factor, 0))
        
        resampled_signal.samples = resample(
            np.pad(signal_model.samples * SCALE_FACTOR_UV, (n_pad_start, n_pad_end)), 
            num
        )[n_pad_resampled:real_num + n_pad_resampled]
        resampled_signal.sample_rate = target_rate   

        return resampled_signal

    def _create_raw_object(self, resampled_signals):
        """Create MNE Raw object from resampled signals"""
        sfreq = resampled_signals[0].sample_rate
        data = np.array([r.samples for r in resampled_signals])
        ch_names = [r.channel for r in resampled_signals]
        info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types='eeg')
        self.raw_eeg = mne.io.RawArray(data, info)

    def _create_display_version(self, window_duration_sec):
        """Create decimated version with proper MNE object"""
        # Choose decimation factor based on window duration
        if window_duration_sec >= EPOCH_SLEEP_SHORT_SEC:  # 15 minutes
            decimation_factor = DECIMATION_FACTOR_WHOLE_REC
        else:
            decimation_factor = DECIMATION_FACTOR_NONE
        
        # Decimate the data directly
        decimated_data = self.raw_eeg.get_data()[:, ::decimation_factor]
        new_sfreq = self.raw_eeg.info['sfreq'] / decimation_factor
        print(f'New fs is {new_sfreq} Hz')
        
        # Create new MNE info with correct sampling rate
        info_display = mne.create_info(
            ch_names=self.raw_eeg.ch_names, 
            sfreq=new_sfreq, 
            ch_types='eeg'
        )
        
        # Create new MNE Raw object with decimated data
        self.raw_eeg_display = mne.io.RawArray(decimated_data, info_display)
        self.decimation_factor = decimation_factor