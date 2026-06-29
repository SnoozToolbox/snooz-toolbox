"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2025
See the file LICENCE for full license details.
==============================================================================
EEG Inspector View – CIUSSS DU NORD-DE-L'ÎLE-DE-MONTRÉAL

Author: Hanieh Bazregarzadeh  
last update: July 2025
Reviewer: Karine Lacourse September 2025

Description:
-------------
This script provides the main logic for the EEG Inspector application.
The tool enables users to quickly detect and mark bad channels and noisy epochs through visual inspection of EEG signals, making preprocessing faster and more reliable.
It first displays the EEG channels to allow the user to identify and select non-brain channels for removal.
It then applies basic preprocessing (filtering 100 Hz and resampling 256 Hz (or 200 Hz), for visualization only) and visualizes the EEG data so the user can mark additional noisy channels.
Depending on the total recording length, the data is automatically segmented: for long recordings (e.g., sleep data), into 5- or 15-minute epochs; for shorter recordings (less than one hour), into 10- or 30-second epochs.
The user can then inspect these segments and mark noisy epochs to be saved as annotations.
Finally, the script displays the PSD (Power Spectral Density) of the remaining cleaned channels to verify that the data is ready and sufficiently clean before saving the annotations.

CEAMSApps/EEGInspector/
├── constants.py                    # Constants and configuration
├── data_processing.py              # Data loading and processing
├── channel_selection.py            # Channel selection widget
├── eeg_visualization.py            # EEG plotting components  
├── epoch_processing.py             # Epoch creation and management
├── psd_visualization.py            # PSD plotting
├── event_manager.py                # Event saving and management
└── EEGInspectorView.py             # Main view controller

==============================================================================

Main EEG Inspector View - Controller class"""

# Standard library imports
import os
import re


for env_name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(env_name, '1')

# Third-party imports
import mne
import numpy as np
from mne.channels import get_builtin_montages, make_standard_montage

# Qt imports
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QCoreApplication


# Local imports
from CEAMSModules.PSGReader.PSGReaderManager import PSGReaderManager
from CEAMSApps.EEGInspector.MontageSelectionDialog import MontageSelectionDialog
from .ui.Ui_EEGInspectorView import Ui_EEGInspectorView
from .data_processing import DataProcessor
from .channel_selection import ChannelSelector
from .eeg_visualization import EEGVisualizer
from .epoch_processing import EpochProcessor
from .psd_visualization import PSDVisualizer
from .event_manager import EventManager
from .constants import *

DEBUG = False

class EEGInspectorView(Ui_EEGInspectorView, QWidget):
    """Main controller for EEG Inspector application"""
    def __init__(self, managers, params, **kwargs):
        super().__init__(**kwargs)
        self._managers = managers
        self._params = params
        self.setupUi(self)

        # Initialize components
        self.channel_selector = ChannelSelector(self)
        self.eeg_visualizer = EEGVisualizer(self)
        self.epoch_processor = EpochProcessor(self)
        self.psd_visualizer = PSDVisualizer(self)
        self.event_manager = EventManager(self)
        
        self._connect_signals()
        self._setup_ui()

        self.bad_channels = []


    def _connect_signals(self):
        """Connect UI signals to handlers"""
        self.edf_pushButton.clicked.connect(self.on_choose_file) 
        self.NextButton1.clicked.connect(self.on_next_page1)
        self.SkipButton1.clicked.connect(self.on_skip_page1)
        self.NextButton2.clicked.connect(self.on_next_page2)
        self.BackButton2.clicked.connect(self.on_back_page2)
        self.NextButton3.clicked.connect(self.on_next_page3)
        self.BackButton3.clicked.connect(self.on_back_page3)
        self.BackButton4.clicked.connect(self.on_back_page4)
        self.ApplyButton.clicked.connect(self.on_apply_epochs)
        self.SaveButton.clicked.connect(self.on_save)
        self.BrowseButton.clicked.connect(self.on_browse_save)
        self.checkBox_same_file.toggled.connect(self.on_same_file)

    def _setup_ui(self):
        """Initial UI setup"""
        self.StackedWidget.setCurrentIndex(0)
        # Disable the SaveButton until the checkBox_same_file is checked or a different path is provided
        #self.SaveButton.setEnabled(False) # by default the save same file is checked now.


    def on_choose_file(self):
        """Handle file selection"""
        # Create file dialog for selecting existing files
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.ExistingFile)

        # Initialize PSG reader to get supported file extensions
        self._psg_reader_manager = PSGReaderManager()
        self._psg_reader_manager._init_readers()
        dlg.setNameFilters(self._psg_reader_manager.get_file_extensions_filters())

        # Show dialog and process selected file
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            if len(filenames) == 1:
                self.edf_lineEdit.setText(filenames[0])  # Set file path in UI
                self.on_run()  # Start processing the selected file

    def on_run(self):
        """Load PSG file and setup channel selection interface"""
        
        self.input_dir = self.edf_lineEdit.text()
        self.file_name_label1.setText(os.path.splitext(os.path.basename(self.input_dir))[0])

        try:
            # Clean up any existing data before loading new file
            # (after PSG reader manager is already initialized in on_choose_file)
            self._cleanup_before_new_file()
            
            # Open PSG file and get montage info
            self._psg_reader_manager.open_file(self.input_dir)
            self._events = self._psg_reader_manager.get_events()
            self._montages = self._psg_reader_manager.get_montages()

            # Get channels for each montage
            self._channels = {}
            for montage in self._montages:
                channels = self._psg_reader_manager.get_channels(montage.index)
                self._channels[montage.name] = channels

            self._psg_reader_manager.close_file()

            # Show montage selection dialog
            dialog = MontageSelectionDialog(self._channels, None)
            if dialog.exec_():
                self._selected_montage_name = dialog.montage_name
                self._selected_montage = dialog.montage_selection

            # Create channel names list
            self.intial_channel_names = [ch.name for ch in self._channels[self._selected_montage_name]]

            # Find best montage for channel detection
            best_montage = self._find_best_montage(self.intial_channel_names)
            
            # Setup channel selection UI using ChannelSelector
            placeholder1 = self.findChild(QWidget, "figure_placeholder1")
            confirm_button = self.channel_selector.setup_channel_selection_ui(
                placeholder1, self.intial_channel_names, best_montage
            )
            confirm_button.clicked.connect(self._on_channels_confirmed)

            self.NextButton1.setEnabled(False)
            self.NextButton1.setVisible(True)
            self.SkipButton1.setEnabled(True)

        except Exception as e:
            self.on_data_error(str(e))

    def _find_best_montage(self, channel_names):
        """Find best matching montage for channels"""
        # Create dummy raw for montage detection
        sfreq = 256
        data = np.zeros((len(channel_names), int(2*sfreq)))
        info = mne.create_info(ch_names=channel_names, sfreq=sfreq, ch_types='eeg')
        raw = mne.io.RawArray(data, info)
        
        return self.find_and_set_best_montage(raw)

    def find_and_set_best_montage(self, raw):
        """Find best matching montage using MNE"""
        data = raw.copy()
        ch_names = data.info['ch_names']
        
        # Try different channel name mappings
        ch_map_name_try1 = {}
        for ch in raw.ch_names:
            if ch.lower().find('vref') != -1:
                ch_map_name_try1[ch] = 'Cz'
            else:   
                ch_map_name_try1[ch] = ch.replace('EEG ', 'E')

        ch_map_name_try2 = {ch: re.sub('[^0-9a-z]+', '', ch.lower().replace('eeg', '')) for ch in ch_names}

        best_montage = ''
        best_found_chs = 0

        # Try different built-in montages to find the best fit
        for item in get_builtin_montages():
            montage = make_standard_montage(item)
            data.set_montage(montage, match_alias=True, match_case=False, on_missing='ignore')
            if len(data.info['dig']) > best_found_chs:
                best_montage = item
                best_found_chs = len(data.info['dig'])

        # Test with renamed channels
        data.rename_channels(ch_map_name_try1)
        for item in get_builtin_montages():
            montage = make_standard_montage(item)
            data.set_montage(montage, match_alias=True, match_case=False, on_missing='ignore')
            if len(data.info['dig']) > best_found_chs:
                best_montage = item
                best_found_chs = len(data.info['dig'])

        data = raw.copy()
        data.rename_channels(ch_map_name_try2)
        for item in get_builtin_montages():
            montage = make_standard_montage(item)
            data.set_montage(montage, match_alias=True, match_case=False, on_missing='ignore')
            if len(data.info['dig']) > best_found_chs:
                best_montage = item
                best_found_chs = len(data.info['dig'])

        return best_montage

    def _on_channels_confirmed(self):
        """Handle channel selection confirmation"""
        self.channel_selector.save_selected_channels(self.intial_channel_names)
        self.selected_channels = self.channel_selector.selected_channels
        self.selected_non_brain_channels = self.channel_selector.selected_non_brain_channels
        self.NextButton1.setEnabled(True)

    def on_skip_page1(self):
        """Skip channel selection and proceed with all EEG channels"""
        self.selected_channels = self.intial_channel_names
        self.selected_non_brain_channels = []
        self.on_next_page1()

    def on_next_page1(self):
        try:
            """Start data loading thread"""
            self.desc_label13.setText('Loading...')
            # The "Confirm Selection" button is disabled after clicking on "Next"
            self.channel_selector.confirm_button.setEnabled(False)
            # The list of channels is disabled after clicking on "Next" to prevent changes
            self.channel_selector.channel_list_widget.setEnabled(False)
            self.NextButton1.setEnabled(False)
            self.SkipButton1.setEnabled(False)
            
            # Start data processing thread
            self.data_processor = DataProcessor(self.input_dir, self.selected_channels, self._selected_montage)
            self.data_processor.data_loaded.connect(self.on_visualize_eeg_channels)
            self.data_processor.error_occurred.connect(self.on_data_error)
            self.data_processor.start()
        except Exception as e:
            self.on_data_error(str(e))

    def on_visualize_eeg_channels(self):
        try:
            """Setup EEG visualization using EEGVisualizer"""
            self.StackedWidget.setCurrentIndex(1)
            
            # Get data from processor
            self.eeg_selected = self.data_processor.raw_eeg
            self._start_time = self.data_processor._start_time
            self._duration = self.data_processor._duration
            
            # Pass raw_eeg to visualizer - it will choose display version internally
            self.eeg_visualizer.setup_visualization(self.eeg_selected, self._duration)
        except Exception as e:
            self.on_data_error(str(e))

    def keyPressEvent(self, event):
        """Handle keyboard navigation"""
        if self.StackedWidget.currentIndex() == 1:
            if event.key() in [Qt.Key_Left, Qt.Key_Right]:
                self.eeg_visualizer.canvas_select_chs.setFocus()
        elif self.StackedWidget.currentIndex() == 2:
            if event.key() in [Qt.Key_Left, Qt.Key_Right]:
                self.epoch_processor.canvas_select_epochs.setFocus()
        super().keyPressEvent(event)

    def on_next_page2(self):
        try:
            """Setup epoch processing using EpochProcessor"""
            if not hasattr(self, "selected_channels") or not self.selected_channels:
                QMessageBox.warning(self, "Warning", "No channels selected. Please select channels first.")
                return

            # Show loading message and force UI update
            self.desc_label22.setText('Loading...')
            self.BackButton2.setEnabled(False)
            self.NextButton2.setEnabled(False)
            QCoreApplication.processEvents()  # Force UI refresh

            # Use EpochProcessor to setup epochs
            self.StackedWidget.setCurrentIndex(2)

            # Get bad channels and create clean EEG data once
            self.bad_channels = self.eeg_visualizer.get_bad_channels()
            self.eeg_bad_chs_removed = self.eeg_selected.copy().drop_channels(self.bad_channels)
            self.epoch_processor.setup_epochs(self.eeg_bad_chs_removed, self._duration)

            # Reset message after processing
            self.desc_label22.setText('Click on "Next" once your selection is finished.')            
        except Exception as e:
            self.on_data_error(str(e))

    def on_next_page3(self):
        try:
            # Show loading message and force UI update
            self.desc_label_33.setText('Loading...')
            self.BackButton3.setEnabled(False)
            self.NextButton3.setEnabled(False)
            QCoreApplication.processEvents()  # Force UI refresh

            """Setup PSD visualization using PSDVisualizer"""
            self.StackedWidget.setCurrentIndex(3)

            # Ensure bad epochs are updated
            bad_epochs = self.epoch_processor.get_bad_epochs()  

            # In sleep data
            if self._duration > SLEEP_RECORDING_THRESHOLD_SEC:
                # Check if epochs are segmented in long epochs and segment to shorter epochs for PSD
                if self.epoch_processor.epoch_dur == EPOCH_SLEEP_LONG_SEC:
                    # Update self.epoch_processor.epochs and self.epoch_processor.epoch_dur
                    #   Warning : the MNE plot is not updated
                    self._convert_epochs_for_psd(self.eeg_bad_chs_removed)
                    if self.epoch_processor.epoch_dur in self.epoch_processor.bad_epochs_by_duration:
                        bad_epochs = self.epoch_processor.bad_epochs_by_duration[self.epoch_processor.epoch_dur]
        
            self.save_lineedit.clear()

            # Get current epochs after bad channel removal
            epochs = self.epoch_processor.epochs.copy()

            # Drop bad epochs
            epochs.drop(bad_epochs, reason='USER')

            # Drop bad epochs for computing PSD
            epochs.drop_bad()

            # Use PSDVisualizer to setup PSD plot
            self.psd_visualizer.setup_psd_plot(epochs, self.data_processor.cutoff_freq)

            # Reset message after processing
            self.desc_label_33.setText('Click on "Next" once your selection is finished.')
        except Exception as e:
            self.on_data_error(str(e))


    def _convert_epochs_for_psd(self, eeg_bad_chs_removed):
        """Segment long (1-hour) epochs into shorter (20-minute) epochs for PSD calculation"""
        
        # Get bad epochs from current display
        current_bad_epochs = self.epoch_processor.get_bad_epochs()
        # Change epoch duration for segmentation
        self.epoch_processor.epoch_dur = EPOCH_SLEEP_SHORT_SEC
        # Create short epochs using the same method but with NaN padding
        epoch_short = self.epoch_processor._create_epochs_with_incomplete(eeg_bad_chs_removed)

        # Convert bad epochs from 1-hour to 20-minute indices
        ratio = EPOCH_SLEEP_LONG_SEC // EPOCH_SLEEP_SHORT_SEC  # 3
        bad_epochs_short = []
        for bad_idx in current_bad_epochs:
            # Each 1-hour bad epoch becomes 3 consecutive 20-minute bad epochs
            for i in range(ratio):
                new_idx = bad_idx * ratio + i
                if new_idx < len(epoch_short.events):
                    bad_epochs_short.append(new_idx)
        # Update the conversion of the bad epochs for the new duration
        self.epoch_processor.bad_epochs_by_duration[EPOCH_SLEEP_SHORT_SEC] = bad_epochs_short  # Update self.epoch_processor.
        # Save the new epochs in self.epoch_processor
        self.epoch_processor.epochs = epoch_short
        # Using back button still works since apply_new_epoch_duration will be called again 
        #  the bad epochs should be still defined since the EpochProcessor constructor wont be called.


    def on_back_page2(self):
        """Navigate back to channel selection"""
        self.StackedWidget.setCurrentIndex(0)
        self.desc_label13.setText(u"Click on \"Next\" once your selection is finished or click on \"skip\" if you want to skip this step.")
        # Find best montage for channel detection
        best_montage = self._find_best_montage(self.intial_channel_names)
        # Setup channel selection UI using ChannelSelector
        placeholder1 = self.findChild(QWidget, "figure_placeholder1")
        confirm_button = self.channel_selector.setup_channel_selection_ui(
            placeholder1, self.intial_channel_names, best_montage
        )
        confirm_button.clicked.connect(self._on_channels_confirmed)
        self.NextButton1.setEnabled(False)
        self.NextButton1.setVisible(True)
        self.SkipButton1.setEnabled(True)
        self.channel_selector.confirm_button.setEnabled(True)


    def on_back_page3(self):
        """Navigate back to EEG visualization"""
        self.desc_label22.setText('Click on "Next" once your selection is finished.')
        self.StackedWidget.setCurrentIndex(1)
        self.NextButton2.setEnabled(True)
        self.BackButton2.setEnabled(True)

    def on_back_page4(self):
        """Navigate back to epoch processing"""
        self.StackedWidget.setCurrentIndex(2)
        # Use already processed data
        self.epoch_processor.apply_new_epoch_duration(self.eeg_bad_chs_removed, self._duration)
        self.NextButton3.setEnabled(True)
        self.BackButton3.setEnabled(True)

    def on_apply_epochs(self):
        """Apply new epoch duration using EpochProcessor"""
        # Use already processed data
        self.epoch_processor.apply_new_epoch_duration(self.eeg_bad_chs_removed, self._duration)

    def on_save(self):
        try:
            """Save annotations using EventManager"""
            # Get bad channels and epochs
            bad_epochs = self.epoch_processor.bad_epochs_by_duration[self.epoch_processor.epoch_dur].copy()            
            # Get current epochs after bad channel removal
            epochs = self.epoch_processor.epochs.copy()
            # Drop bad epochs
            epochs.drop(bad_epochs, reason='USER')
            # Mark the epochs as clean only
            epochs.drop_bad()
            
            # Use EventManager to save annotations
            self.event_manager.save_annotations(
                selected_non_brain_channels=self.selected_non_brain_channels,
                marked_bad_chs=self.bad_channels,
                bad_epoch_idxs=bad_epochs,
                input_dir=self.input_dir,
                save_path=self.save_lineedit.text(),
                same_file_checked=self.checkBox_same_file.isChecked(),
                overwrite_checked=self.checkBox_overwrite.isChecked(),
                start_time=self._start_time,
                duration=self._duration,
                epoch_dur=self.epoch_processor.epoch_dur,
                epochs=epochs, # Bad epochs already dropped
                selected_montage=self._selected_montage
            )
        except Exception as e:
            self.on_data_error(str(e))

    def on_browse_save(self):
        """Browse for save file location"""
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        
        # Set appropriate file extension filter
        if self.input_dir.find('.edf') != -1:
            extension = 'EDF (*.edf)'
        elif self.input_dir.find('.sts') != -1:
            extension = 'Harmonie (*.sts)'
        elif self.input_dir.find('.eeg') != -1:
            extension = 'Xltek (*.eeg)'
        else:
            extension = f'(*.{self.input_dir[-3:]})'

        dlg.setNameFilters([extension])
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            if len(filenames) == 1:
                self.save_lineedit.setText(filenames[0])
                self.SaveButton.setEnabled(True)

    def on_same_file(self):
        """Handle same file checkbox toggle"""
        if self.checkBox_same_file.isChecked():
            self.BrowseButton.setEnabled(False)
            self.save_lineedit.setEnabled(False)
            self.desc_label42.setEnabled(False)
            self.SaveButton.setEnabled(True)
        else:
            self.BrowseButton.setEnabled(True)
            self.save_lineedit.setEnabled(True)
            self.desc_label42.setEnabled(True)
            if len(self.save_lineedit.text()) > 0:
                self.SaveButton.setEnabled(True)
            else:
                self.SaveButton.setEnabled(False)

    def on_data_error(self, error_message):
        """Handle data loading errors"""
        QMessageBox.critical(self, "Data Load Error",
                           f"An error occurred while loading data:\n{error_message}")
        
        # Reset UI state
        placeholder1 = self.findChild(QWidget, "figure_placeholder1")
        if placeholder1 and placeholder1.layout():
            while placeholder1.layout().count():
                child = placeholder1.layout().takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            old_layout = placeholder1.layout()
            QWidget().setLayout(old_layout)

        self.desc_label13.setText(u"Click on \"Next\" once your selection is finished or click on \"skip\" if you want to skip this step.")
        self.NextButton1.setEnabled(False)
        self.SkipButton1.setEnabled(False)
        self.edf_lineEdit.setText("")

    def is_dirty(self):
        """Check if view has unsaved changes"""
        return False

    def close_app(self):
        """Clean up EEG Inspector specific resources before closing"""

        # Only clean up EEG Inspector specific resources:
        # 1. Matplotlib figures (critical for EEG Inspector)
        self._close_matplotlib_figures()
        
        # 2. Clean up MNE objects and large data structures
        self._cleanup_mne_objects()
        
        # 3. EEG Inspector specific components cleanup
        self._cleanup_components()
        
        # 4. Virtual memory cleanup (remove MNE and other safe modules)
        self._managers.package_manager._cleanup_safe_protected_modules()
        
        # Let Snooz AppManager handle the rest (garbage collection, memory management, etc.)
        #   QWidget.close() Snooz intercepts and AppManager handles
        self.close()

    def _cleanup_before_new_file(self):
        """Clean up resources before loading a new file"""

        # Close matplotlib figures
        self._close_matplotlib_figures()

        # Clean up PSG reader (only if it exists)
        if hasattr(self, '_psg_reader_manager') and self._psg_reader_manager:
            try:
                self._psg_reader_manager.close_file()
            except Exception as e:
                pass
        
        # Clean up components (only if they exist)
        if hasattr(self, 'epoch_processor') and self.epoch_processor:
            self.epoch_processor.cleanup()
        
        if hasattr(self, 'eeg_visualizer') and self.eeg_visualizer:
            self.eeg_visualizer.cleanup()
        
        if hasattr(self, 'psd_visualizer') and self.psd_visualizer:
            self.psd_visualizer.cleanup()
        
        # Clean up data processor thread if running
        if hasattr(self, 'data_processor') and self.data_processor:
            if self.data_processor.isRunning():
                self.data_processor.quit()
                self.data_processor.wait()
            self.data_processor.cleanup()
            self.data_processor = None
        
        # Clean up MNE objects and large data structures
        # (This will handle eeg_selected, raw_eeg, eeg_bad_chs_removed, channels, etc.)
        self._cleanup_mne_objects()
        
        # Clear bad channels list (only if it exists)
        if hasattr(self, 'bad_channels'):
            self.bad_channels.clear()
        
        # VIRTUAL MEMORY CLEANUP: Remove safe-to-remove modules (especially MNE)
        # This helps release virtual memory that accumulates with each file load
        self._managers.package_manager._cleanup_safe_protected_modules()
        
        # MORE AGGRESSIVE CLEANUP: Force garbage collection like ContentManager does
        # This mimics what happens when the app is completely closed and reopened
        import gc
        gc.collect(1)  # Force garbage collection to mimic app restart behavior


    def _close_matplotlib_figures(self):
        """Close all matplotlib figures to free memory"""
        try:
            import matplotlib.pyplot as plt
            plt.close('all')  # Close all matplotlib figures
        except Exception as e:
            pass

    def _cleanup_mne_objects(self):
        """Clean up MNE objects and large data structures"""
        
        # Clean up raw data objects (can be very large in memory)
        if hasattr(self, 'eeg_selected'):
            self.eeg_selected = None
            
        if hasattr(self, 'raw_eeg'):
            self.raw_eeg = None
            
        if hasattr(self, 'eeg_bad_chs_removed'):
            self.eeg_bad_chs_removed = None
        
        # Clean up processed data arrays
        if hasattr(self, 'bad_channels'):
            self.bad_channels.clear()
            
        # Clear channel and montage data (only if they exist)
        if hasattr(self, '_channels'):
            self._channels = None
            
        if hasattr(self, '_montages'):
            self._montages = None
            
        if hasattr(self, 'intial_channel_names'):
            self.intial_channel_names = None

    def _cleanup_components(self):
        """Clean up component-specific resources"""
        # Clean up epoch processor
        if hasattr(self, 'epoch_processor') and self.epoch_processor:
            self.epoch_processor.cleanup()
        
        # Clean up EEG visualizer
        if hasattr(self, 'eeg_visualizer') and self.eeg_visualizer:
            self.eeg_visualizer.cleanup()
        
        # Clean up PSD visualizer
        if hasattr(self, 'psd_visualizer') and self.psd_visualizer:
            self.psd_visualizer.cleanup()
    



