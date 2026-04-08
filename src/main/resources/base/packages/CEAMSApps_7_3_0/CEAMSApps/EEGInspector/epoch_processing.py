"""Epoch processing and visualization"""

import mne
import numpy as np
from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtCore import Qt, QCoreApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from .constants import *
import sys

class EpochProcessor:
    """Handles epoch creation and visualization"""
    
    def __init__(self, parent_widget):
        self.parent = parent_widget
        self.epochs = None
        self.mne_plot_select_epochs = None
        self.canvas_select_epochs = None
        self.epoch_dur = None
        self.bad_epochs_by_duration = {}  # Store bad epochs for each duration
        self._popup_figures = []  # Track popup figures for cleanup

    def _is_mne_object_valid(self, obj):
        """Safely check if MNE object exists and is accessible"""
        if obj is None:
            return False
        try:
            # Try to access a basic property without triggering length checks
            return hasattr(obj, 'info')
        except (RuntimeError, AttributeError):
            return False

    def cleanup(self):
        """Clean up epoch processor resources"""
        # Close MNE plot windows
        if self.mne_plot_select_epochs:
            try:
                # Close the MNE plot window
                if hasattr(self.mne_plot_select_epochs, 'close'):
                    self.mne_plot_select_epochs.close()
                elif hasattr(self.mne_plot_select_epochs, 'fig'):
                    import matplotlib.pyplot as plt
                    plt.close(self.mne_plot_select_epochs.fig)
            except (RuntimeError, AttributeError, ValueError) as e:
                # Expected errors during cleanup:
                # - RuntimeError: wrapped C/C++ object has been deleted
                # - AttributeError: object has no attribute (already cleaned up)
                # - ValueError: figure not managed by backend
                if hasattr(self.parent, 'DEBUG') and self.parent.DEBUG:
                    print(f"Expected cleanup error (safe to ignore): {e}")
            except Exception as e:
                # Unexpected errors - log for debugging
                if hasattr(self.parent, 'DEBUG') and self.parent.DEBUG:
                    print(f"Unexpected error during MNE plot cleanup: {e}")
            self.mne_plot_select_epochs = None
        
        # Close popup figures
        self._close_popup_figures()
        
        # AGGRESSIVE: Clear epochs data and force deletion
        # Safe check for epochs existence (MNE can raise RuntimeError on len())
        if self._is_mne_object_valid(self.epochs):
            try:
                # Force deletion of underlying data arrays
                if hasattr(self.epochs, '_data'):
                    del self.epochs._data
            except (RuntimeError, AttributeError):
                # MNE may raise RuntimeError if epochs not preloaded
                pass
        self.epochs = None
        
        # Clear padded raw data
        if hasattr(self, 'padded_raw') and self._is_mne_object_valid(self.padded_raw):
            try:
                if hasattr(self.padded_raw, '_data'):
                    del self.padded_raw._data
            except (RuntimeError, AttributeError):
                pass
        self.padded_raw = None
        
        # Clear epochs_display
        if hasattr(self, 'epochs_display') and self._is_mne_object_valid(self.epochs_display):
            try:
                if hasattr(self.epochs_display, '_data'):
                    del self.epochs_display._data
            except (RuntimeError, AttributeError):
                # MNE may raise RuntimeError if epochs not preloaded
                pass
        self.epochs_display = None
        
        # Clear canvas
        self.canvas_select_epochs = None
        
        # Clear bad epochs storage
        self.bad_epochs_by_duration.clear()
        
        # Force aggressive garbage collection
        import gc
        gc.collect()

    def _close_popup_figures(self):
        """Close all popup figures created by right-click"""
        import matplotlib.pyplot as plt
        for fig in self._popup_figures:
            try:
                if fig and hasattr(fig, 'number'):
                    plt.close(fig)
            except Exception:
                pass
        self._popup_figures.clear()

    def setup_epochs(self, eeg_bad_chs_removed, duration_rec):
        """Setup epoch processing and visualization with incomplete epoch handling
            Called only once by EEGInspector when loading the data.
            apply_new_epoch_duration() is called when changing the epoch duration and using back pushbutton.
        """

        # Update epoch duration labels for long recordings
        if duration_rec > SLEEP_RECORDING_THRESHOLD_SEC:
            # Update all three items
            text_to_display = f"{EPOCH_SLEEP_LONG_CHAR} minutes - display whole recording"
            self.parent.Epoch_len_comboBox.setItemText(0, QCoreApplication.translate("EEGInspectorView", text_to_display, None))
            text_to_display = f"{EPOCH_SLEEP_SHORT_CHAR} minutes - display whole recording"
            self.parent.Epoch_len_comboBox.setItemText(1, QCoreApplication.translate("EEGInspectorView", text_to_display, None))

        # Set epoch duration based on recording length and user selection
        if duration_rec > SLEEP_RECORDING_THRESHOLD_SEC:
            if EPOCH_SLEEP_LONG_CHAR in self.parent.Epoch_len_comboBox.currentText():
                self.epoch_dur = EPOCH_SLEEP_LONG_SEC
            else:
                 self.epoch_dur = EPOCH_SLEEP_SHORT_SEC
        else:
            self.epoch_dur = EPOCH_COMA_SHORT_SEC if EPOCH_COMA_SHORT_CHAR in self.parent.Epoch_len_comboBox.currentText() else EPOCH_COMA_LONG_SEC

        # Create and display epochs
        self._create_and_display_epochs(eeg_bad_chs_removed, duration_rec, self.epoch_dur)
        
        # Enable next button
        self.parent.NextButton3.setEnabled(True)


    def _create_and_display_epochs(self, eeg_bad_chs_removed, duration, current_epoch_dur, old_epoch_duration=None):
        """Create and display epochs with incomplete epoch handling"""

        # Create epochs with incomplete last epoch
        self.epochs = self._create_epochs_with_incomplete(eeg_bad_chs_removed)

        # Calculate number of epochs to display entire recording
        if duration > SLEEP_RECORDING_THRESHOLD_SEC:
            n_epochs_display = len(self.epochs.events)  # Use events length to Show all epochs for sleep data
        else:
            n_epochs_display = N_EPOCH_DISPLAY_COMA_SHORT if self.epoch_dur == EPOCH_COMA_SHORT_SEC else N_EPOCH_DISPLAY_COMA_LONG
        
        # Create decimated version for display
        padded_duration_s = len(self.epochs.events) * self.epoch_dur        
        self.epochs_display = self._create_decimated_epochs(padded_duration_s)

        # Use appropriate plot scales based on recording duration
        plot_scales = PLOT_SCALES_SLEEP if duration > SLEEP_RECORDING_THRESHOLD_SEC else PLOT_SCALES_COMA

        # Create epoch plot using display version
        self.mne_plot_select_epochs = self.epochs_display.plot(
            n_channels=EPOCH_N_CHANNELS, 
            scalings=plot_scales, 
            n_epochs=n_epochs_display, 
            show=False
        )
        # Set bad epochs directly after plot creation
        self._restore_bad_epochs_in_plot(current_epoch_dur, old_epoch_duration)

        # Connect to MNE's bad epoch changes
        self._connect_bad_epoch_listener()

        # Add right-click handler for 30-second epoch viewing
        if duration > SLEEP_RECORDING_THRESHOLD_SEC:
            self._add_right_click_handler()

        # Update MNE's internal n_times to reflect padded duration
        if hasattr(self, 'incomplete_epoch_duration') and self.incomplete_epoch_duration is not None:
            padded_n_times = int(padded_duration_s * self.epochs_display.info['sfreq'])
            self.mne_plot_select_epochs.mne.n_times = padded_n_times + 1 # Hack to display last epoch in MNE object
            #self.mne_plot_select_epochs.mne.n_times = padded_n_times

        self.canvas_select_epochs = FigureCanvas(self.mne_plot_select_epochs.canvas.figure)
        self.canvas_select_epochs.setFocusPolicy(Qt.StrongFocus)
        self.canvas_select_epochs.setFocus()

        # Setup canvas in placeholder
        placeholder3 = self.parent.findChild(QWidget, "figure_placeholder3")
        self._setup_canvas_in_placeholder(placeholder3, self.canvas_select_epochs)


    def _create_decimated_epochs(self, duration):
        """Create decimated version of epochs for display"""
        # Choose decimation factor based on recording duration
        if duration > SLEEP_RECORDING_THRESHOLD_SEC:
            decimation_factor = DECIMATION_FACTOR_WHOLE_REC if self.epoch_dur > EPOCH_SLEEP_STAGE_SEC else DECIMATION_FACTOR_NONE
        else:
            decimation_factor = DECIMATION_FACTOR_NONE
        
        # Get original epochs data
        epochs_data = self.epochs.get_data()
        
        # Decimate each epoch
        decimated_epochs_data = epochs_data[:, :, ::decimation_factor]
        
        # Calculate new sampling frequency
        new_sfreq = self.epochs.info['sfreq'] / decimation_factor
        
        # Create new info with decimated sampling rate
        info_display = mne.create_info(
            ch_names=self.epochs.ch_names,
            sfreq=new_sfreq,
            ch_types='eeg'
        ) # info_display is not valid since we hack the display by decimating (without filter) 
        
        # Create decimated epochs object
        epochs_display = mne.EpochsArray(
            decimated_epochs_data,
            info_display,
            tmin=self.epochs.tmin
        )
        
        return epochs_display

    def _create_epochs_with_incomplete(self, eeg_bad_chs_removed):
        """Create epochs including incomplete last epoch - MEMORY OPTIMIZED"""
        # Use actual data duration
        actual_duration = eeg_bad_chs_removed.times[-1]
        
        # Calculate remaining time
        remaining_time = actual_duration % self.epoch_dur
        
        # MEMORY OPTIMIZATION: Use in-place operations and minimize data duplication
        if remaining_time > 0:
            # Calculate samples needed for padding
            samples_needed = int((self.epoch_dur - remaining_time) * eeg_bad_chs_removed.info['sfreq'])
            
            # Get data reference (avoid get_data() copy if possible)
            original_data = eeg_bad_chs_removed._data
            n_channels, n_times = original_data.shape
            
            # Create padded data more efficiently - minimize memory allocation
            padded_data = np.empty((n_channels, n_times + samples_needed), dtype=original_data.dtype)
            
            # Copy original data
            padded_data[:, :n_times] = original_data
            
            # Zero pad the end (more memory efficient than concatenate)
            padded_data[:, n_times:] = 0
            
            # Clear reference to original data to help GC
            del original_data
            
            # Update info object with new sample count
            info_padded = eeg_bad_chs_removed.info.copy()
            # Create padded raw object and store it
            self.padded_raw = mne.io.RawArray(padded_data, info_padded)
            
            # Clear padded_data reference immediately
            del padded_data
            import gc
            gc.collect()
            
            self.incomplete_epoch_duration = remaining_time
        else:
            self.padded_raw = eeg_bad_chs_removed
            self.incomplete_epoch_duration = None
        
        # Create epochs from padded raw data
        epochs = mne.make_fixed_length_epochs(
            self.padded_raw, 
            duration=self.epoch_dur, 
            overlap=0
        )
        
        return epochs

    def _connect_bad_epoch_listener(self):
        """Connect listener to intercept bad epoch selections"""
        def on_bad_epochs_changed():
            # Update bad_epochs_by_duration whenever user clicks on epochs
            if hasattr(self.mne_plot_select_epochs.mne, "bad_epochs"):
                bad_epoch_indices = list(self.mne_plot_select_epochs.mne.bad_epochs)
                self.bad_epochs_by_duration[self.epoch_dur] = bad_epoch_indices.copy()
        
        # Connect to matplotlib button press events
        def on_button_press(event):
            if event.button == 1 and event.inaxes:  # Left mouse button
                # Small delay to let MNE process the click first
                self.mne_plot_select_epochs.canvas.figure.canvas.mpl_connect('draw_event', 
                    lambda evt: on_bad_epochs_changed())
        
        # Connect to mouse clicks on the plot
        self.mne_plot_select_epochs.canvas.mpl_connect('button_press_event', on_button_press)

    def get_bad_epochs(self):
        """Get bad epoch indices from MNE - now just returns current state"""
        if self.epoch_dur in self.bad_epochs_by_duration:
            return np.array(self.bad_epochs_by_duration[self.epoch_dur])
        return np.array([])

    def _convert_bad_epochs(self, new_duration, old_duration):
        """Convert bad epochs from old duration to new duration"""
        if old_duration not in self.bad_epochs_by_duration:
            return []
        
        old_bad_epochs = self.bad_epochs_by_duration[old_duration]
        converted_bad_epochs = []
        lost_epochs = []
        
        # Calculate conversion ratio from constants
        ratio = EPOCH_SLEEP_LONG_SEC // EPOCH_SLEEP_SHORT_SEC  # 3600 // 1200 = 3
        
        if old_duration == EPOCH_SLEEP_LONG_SEC and new_duration == EPOCH_SLEEP_SHORT_SEC:
            # Convert long epochs to short epochs (1:ratio mapping)
            for old_idx in old_bad_epochs:
                for i in range(ratio):
                    new_idx = old_idx * ratio + i
                    converted_bad_epochs.append(new_idx)
                    
        elif old_duration == EPOCH_SLEEP_SHORT_SEC and new_duration == EPOCH_SLEEP_LONG_SEC:
            # Convert short epochs to long epochs only if ALL children are bad
            parent_groups = {}
            
            # Group short epochs by their parent long epoch
            for old_idx in old_bad_epochs:
                parent_idx = old_idx // ratio
                if parent_idx not in parent_groups:
                    parent_groups[parent_idx] = []
                parent_groups[parent_idx].append(old_idx)
            
            # Only mark parent as bad if all children are bad
            for parent_idx, child_indices in parent_groups.items():
                expected_children = [parent_idx * ratio + i for i in range(ratio)]
                
                if len(child_indices) == ratio and set(child_indices) == set(expected_children):
                    # All children are bad, mark parent as bad
                    converted_bad_epochs.append(parent_idx)
                else:
                    # Some children missing, track as lost
                    lost_epochs.extend(child_indices)
        
        # Show warning if epochs were lost
        if lost_epochs:
            self._show_lost_epochs_warning(lost_epochs, old_duration, new_duration)
        
        return converted_bad_epochs

    def _show_lost_epochs_warning(self, lost_epochs, old_duration, new_duration):
        """Show warning popup for lost bad epoch selections"""
        from PySide6.QtWidgets import QMessageBox
        
        old_duration_text = f"{old_duration // 60} minutes"
        new_duration_text = f"{new_duration // 60} minutes"
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Bad Epoch Selection Lost")
        msg.setText(f"Some bad epoch selections have been lost when switching from "
                    f"{old_duration_text} to {new_duration_text} epochs.")
        msg.setDetailedText(f"Lost epochs: {lost_epochs}\n\n"
                        f"Only complete {new_duration_text} periods that were "
                        f"entirely marked as bad have been preserved.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def apply_new_epoch_duration(self, eeg_bad_chs_removed, duration_rec):
        """Apply new epoch duration and refresh visualization"""
        # Store current bad epochs from the MNE object in the class before changing duration

        old_duration = self.epoch_dur

        if duration_rec > SLEEP_RECORDING_THRESHOLD_SEC:
            if str(self.parent.Epoch_len_comboBox.currentText()).find(EPOCH_SLEEP_LONG_CHAR) != -1:
                self.epoch_dur = EPOCH_SLEEP_LONG_SEC
            else:
                self.epoch_dur = EPOCH_SLEEP_SHORT_SEC
        else:
            if str(self.parent.Epoch_len_comboBox.currentText()).find(EPOCH_COMA_SHORT_CHAR) != -1:
                self.epoch_dur = EPOCH_COMA_SHORT_SEC
            else:
                self.epoch_dur = EPOCH_COMA_LONG_SEC
                
        # Create and display epochs
        self._create_and_display_epochs(eeg_bad_chs_removed, duration_rec, self.epoch_dur, old_duration)
        # The conversion and restoration is handled by _restore_bad_epochs_in_plot(current_epoch_dur, old_epoch_duration=None) 
        #   which is called inside _create_and_display_epochs()
        
    def get_epochs(self):
        """Get epochs for processing"""
        if self._is_mne_object_valid(self.epochs):
            try:
                return self.epochs.copy()
            except (RuntimeError, AttributeError):
                # MNE may raise RuntimeError if epochs not preloaded
                return None
        return None

    def _setup_canvas_in_placeholder(self, placeholder, canvas):
        """Setup canvas widget in placeholder"""
        if placeholder.layout() is None:
            layout = QVBoxLayout()
            placeholder.setLayout(layout)
        else:
            layout = placeholder.layout()
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        layout.addWidget(canvas)
        size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        canvas.setSizePolicy(size_policy)

    def _add_right_click_handler(self):
        """Add right-click functionality to show 30-second epoch details"""
        def on_right_click(event):
            if event.button == 3 and event.inaxes:  # Right mouse button
                # Calculate which epoch was clicked
                click_time = event.xdata
                if click_time is not None:
                    epoch_idx = int(click_time // self.epoch_dur)
                    self._show_30s_epoch_detail(epoch_idx, click_time)
        
        # Connect right-click handler
        canvas = self.mne_plot_select_epochs.canvas
        canvas.mpl_connect('button_press_event', on_right_click)

    def _show_30s_epoch_detail(self, epoch_idx, click_time):
        """Show detailed 30-second epoch view in popup"""
        # Calculate 30-second window around click
        epoch_start_time = epoch_idx * self.epoch_dur
        relative_click_time = click_time - epoch_start_time
        
        # Center 30-second window around click
        window_start = max(0, relative_click_time - EPOCH_SLEEP_STAGE_SEC/2)
        window_end = min(self.epoch_dur, window_start + EPOCH_SLEEP_STAGE_SEC)
        
        # Extract 30-second data from original epochs
        epoch_data = self.epochs[epoch_idx].get_data()[0]  # Get first (only) epoch
        sfreq = self.epochs.info['sfreq']
        
        start_sample = int(window_start * sfreq)
        end_sample = int(window_end * sfreq)
        windowed_data = epoch_data[:, start_sample:end_sample]
        
        # Create 30-second epoch for display
        info_30s = self.epochs.info.copy()
        epoch_30s = mne.EpochsArray(
            windowed_data[np.newaxis, :, :],  # Add epoch dimension
            info_30s,
            tmin=0
        )
        
        # Convert window_start in seconds to HH:MM:SS format
        total_seconds = int(epoch_start_time + window_start)
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        time_str = f"{hours:02}:{minutes:02}:{seconds:02}"

        # Show in popup window
        fig = epoch_30s.plot(
            n_channels=EPOCH_N_CHANNELS,
            scalings=PLOT_SCALES_SLEEP,
            title=f'{str(EPOCH_SLEEP_STAGE_SEC)}-second detail: Epoch {epoch_idx}, Time elapsed: {time_str}',
            show=False,  # Don't show automatically
            block=False
        )
        
        # Track figure for cleanup and set size to sleep tech preferred dimensions
        self._popup_figures.append(fig)
        fig.set_size_inches(EPOCH_POPUP_FIGURE_SIZE)
        
        # Limit the number of open popup figures to prevent memory bloat
        if ENABLE_AUTOMATIC_MEMORY_CLEANUP and len(self._popup_figures) > MAX_POPUP_FIGURES:
            # Close oldest figures
            import matplotlib.pyplot as plt
            while len(self._popup_figures) > MAX_POPUP_FIGURES:
                old_fig = self._popup_figures.pop(0)
                try:
                    if old_fig and hasattr(old_fig, 'number'):
                        plt.close(old_fig)
                except Exception:
                    pass

        # Add 1-second vertical grid lines
        ax = fig.mne.ax_main
        for second in range(1, EPOCH_SLEEP_STAGE_SEC):  # Add lines at 1, 2, 3... 29 seconds
            ax.axvline(x=second, color='lightgray', linestyle='--', alpha=0.5, linewidth=0.8)
        
        # Show only this popup window
        fig.show()      


    def _restore_bad_epochs_in_plot(self, current_epoch_dur, old_epoch_duration=None):
        """Set bad epochs directly in MNE object"""

        # Not the first call
        if old_epoch_duration:
            # If there is a change of duration, try to convert bad epochs if they exist
            if old_epoch_duration != current_epoch_dur:
                # If the bad epoch are already defined for the old epoch length
                if old_epoch_duration in self.bad_epochs_by_duration:
                    # Convert bad epochs from old duration to current duration
                    bad_epochs = self._convert_bad_epochs(current_epoch_dur, old_epoch_duration)
                else:
                    bad_epochs = []
            # Not a change, but bad epochs may have been selected
            else:
                if current_epoch_dur in self.bad_epochs_by_duration:
                    bad_epochs = self.bad_epochs_by_duration[current_epoch_dur]
                else:
                    bad_epochs = []
        # First call
        else:
            bad_epochs = []

        # Add bad epochs to the MNE object to PLot the bad epochs in red
        self.mne_plot_select_epochs.mne.bad_epochs=bad_epochs.copy()

        # Force redraw to show bad epochs in red
        self.mne_plot_select_epochs._redraw()

        # Update bad_epochs_by_duration for the current duration
        self.bad_epochs_by_duration[current_epoch_dur] = bad_epochs