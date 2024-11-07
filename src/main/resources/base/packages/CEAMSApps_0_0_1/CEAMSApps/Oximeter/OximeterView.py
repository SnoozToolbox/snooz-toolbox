"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
DEBUG = False
from scipy import signal, fft
import numpy as np

from PySide2.QtWidgets import QMessageBox
from qtpy import QtWidgets
from qtpy.QtWidgets import QFrame

from CEAMSApps.Oximeter.ChannelSelectionDialog import ChannelSelectionDialog
from CEAMSApps.Oximeter.ui.Ui_OximeterView import Ui_OximeterView

from CEAMSModules.PSGReader.PSGReaderManager import PSGReaderManager

class OximeterView(Ui_OximeterView, QtWidgets.QWidget):
    """
    """
    def __init__(self, managers, params, **kwargs):
        super().__init__(**kwargs)
        self._managers = managers
        self._params = params
        self._selected_montage = None
        self._selected_oximeter = None
        self._current_filename = None
        self._current_signal_models = []
        self._events = None
        self._event_name = "art_SpO2"
        self._group_name = "SpO2"
        
        # init UI
        self.setupUi(self)

        # Craete control buttons to the navigation bar
        self._open_file_pushButton = QtWidgets.QPushButton("Open File")
        self._save_file_pushButton = QtWidgets.QPushButton("Save File")
        self._close_file_pushButton = QtWidgets.QPushButton("Close File")
        self._channel_selection_pushButton = QtWidgets.QPushButton("Channel Selection")

        self._open_file_pushButton.clicked.connect(self._open_file)
        self._save_file_pushButton.clicked.connect(self._save_file)
        self._close_file_pushButton.clicked.connect(self._close_file)
        self._channel_selection_pushButton.clicked.connect(self._channel_selection_dialog)

        self._managers.navigation_manager.add_app_widget(self._open_file_pushButton)
        self._managers.navigation_manager.add_app_widget(self._save_file_pushButton)
        self._managers.navigation_manager.add_app_widget(self._close_file_pushButton)

        # Create horizontal line widget
        self._line = QtWidgets.QFrame()
        self._line.setObjectName(u"line")
        self._line.setFrameShape(QFrame.HLine)
        self._line.setFrameShadow(QFrame.Sunken)

        self._managers.navigation_manager.add_app_widget(self._line)
        self._managers.navigation_manager.add_app_widget(self._channel_selection_pushButton)

        if params is not None and "startup_action" in params and params["startup_action"] == "open_file":
            self._open_file()
    
    def remove_all_clicked(self):
        self.oximeter_draw_area.reset_exclusion_events()

    def remove_new_clicked(self):
        self.oximeter_draw_area.exclusion_events = self._get_exclusion_events()
        self.oximeter_draw_area.update()

    def close_app(self):
        self._managers.navigation_manager.remove_app_widget(self._line)
        self._managers.navigation_manager.remove_app_widget(self._open_file_pushButton)
        self._managers.navigation_manager.remove_app_widget(self._save_file_pushButton)
        self._managers.navigation_manager.remove_app_widget(self._close_file_pushButton)
        self._managers.navigation_manager.remove_app_widget(self._channel_selection_pushButton)

    def is_dirty(self):
        return False
    
    def min_saturation_change(self, text):
        self.oximeter_draw_area.min_saturation = int(text)

    def _ask_user_file(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, True)
        dlg.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        psg_reader_manager = PSGReaderManager()
        psg_reader_manager._init_readers()
        dlg.setNameFilters(psg_reader_manager.get_file_extensions_filters())

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            return filenames[0]
        return None

    def _open_file(self):
        filename = self._ask_user_file()
        if filename is not None:
            self._current_filename = filename

            psg_reader_manager = PSGReaderManager()
            psg_reader_manager._init_readers()
            psg_reader_manager.open_file(filename)

            self._events = psg_reader_manager.get_events() # Type DataFrame
            self._montages = psg_reader_manager.get_montages()
            self._channels = {}
            for montage in self._montages:
                channels = psg_reader_manager.get_channels(montage.index)
                self._channels[montage.name] = channels

            psg_reader_manager.close_file()
            self._channel_selection_dialog()

            log_msg = QMessageBox()
            log_msg.setWindowTitle("Information")
            log_msg.setText("File loaded")
            log_msg.setIcon(QMessageBox.Information)
            log_msg.exec_()

    def _save_file(self):
        print("save_file")

        if self._selected_oximeter is None:
            log_msg = QMessageBox()
            log_msg.setWindowTitle("Information")
            log_msg.setText("Nothing to save")
            log_msg.setIcon(QMessageBox.Information)
            log_msg.exec_()
            return
        
        psg_reader_manager = PSGReaderManager()
        psg_reader_manager._init_readers()
        success = psg_reader_manager.open_file(self._current_filename)
        if not success:
            log_msg = QMessageBox()
            log_msg.setWindowTitle("Error")
            log_msg.setText(f"Could not save file {self._current_filename}")
            log_msg.setIcon(QMessageBox.Critical)
            log_msg.exec_()

            psg_reader_manager.close_file()
            return
        
        psg_reader_manager.remove_events_by_name(self._event_name, self._group_name)
        for exclusion_event in self.oximeter_draw_area.exclusion_events:
            start_time = min(exclusion_event)
            end_time = max(exclusion_event)
            duration = end_time - start_time
            
            success = psg_reader_manager.add_event("art_SpO2", "SpO2", start_time, duration, \
                                         self._selected_oximeter, \
                                         self._selected_montage)
            if not success:
                error_message = psg_reader_manager.get_last_error()
                log_msg = QMessageBox()
                log_msg.setWindowTitle("Error")
                log_msg.setText(f"Could not add event to file: {error_message}")
                log_msg.setIcon(QMessageBox.Critical)
                log_msg.exec_()
                psg_reader_manager.close_file()
                return

        psg_reader_manager.save_file()
        psg_reader_manager.close_file()

        psg_reader_manager = PSGReaderManager()
        psg_reader_manager._init_readers()
        success = psg_reader_manager.open_file(self._current_filename)
        self._events = psg_reader_manager.get_events() # Type DataFrame
        psg_reader_manager.close_file()
        self.oximeter_draw_area.exclusion_events = self._get_exclusion_events()

        self.oximeter_draw_area.update()

        log_msg = QMessageBox()
        log_msg.setWindowTitle("Information")
        log_msg.setText("File saved")
        log_msg.setIcon(QMessageBox.Information)
        log_msg.exec_()
        return

    def _close_file(self):
        print("close_file")
        self._selected_montage = None
        self._selected_oximeter = None
        self._current_filename = None
        self._events = None
        self._current_signal_models = []

        self.oximeter_draw_area.reset_exclusion_events()
        self.oximeter_draw_area.set_signal_models([])
        self.oximeter_draw_area.update()

    def _channel_selection_dialog(self):
        if self._current_filename is None:
            return
        
        dialog = ChannelSelectionDialog(self._channels, 
                                         self._selected_montage, 
                                         self._selected_oximeter)
        if dialog.exec_():
            if dialog.montage_selection == self._selected_montage and \
                dialog.oximeter_selection == self._selected_oximeter:
                return
            
            self._selected_montage = dialog.montage_selection
            self._selected_oximeter = dialog.oximeter_selection

            psg_reader_manager = PSGReaderManager()
            psg_reader_manager._init_readers()
            psg_reader_manager.open_file(self._current_filename)
            signal_models = psg_reader_manager.get_signal_models(self._selected_montage, [self._selected_oximeter])
            psg_reader_manager.close_file()

            self._current_signal_models = []
            for signal_model in signal_models:
                if signal_model.channel == self._selected_oximeter:
                    resampled_signal_model = self._resample_signal(signal_model, 1)
                    self._current_signal_models.append(resampled_signal_model)

            self.oximeter_draw_area.exclusion_events = self._get_exclusion_events()
            self.oximeter_draw_area.set_signal_models(self._current_signal_models)
            self.oximeter_draw_area.update()


    def _get_exclusion_events(self):
        if self._selected_oximeter is None:
            return
        
        # iterate over the self._events pandas dataframe
        events = self._events[self._events['channels'] == self._selected_oximeter]
        events = events[events['group'] == self._group_name]
        events = events[events['name'] == self._event_name]

        exclusion_events = []

        # iterate over the events pandas dataframe
        for event in events.itertuples():
            end_sec = event.start_sec + event.duration_sec
            exclusion_events.append((event.start_sec, end_sec))
        
        return exclusion_events

    def _resample_signal(self, signal_model, target_sample_rate: int):
        resampled_signal_model = signal_model.clone(clone_samples=False)

        #sample_rate = int(sample_rate)
        factor = signal_model.sample_rate / target_sample_rate
        nsamples = signal_model.samples.size

        # Since resample is using the fft, we want to have dyadic number of samples to speed up performance
        fast_size = fft.next_fast_len(nsamples)
        num = int(fast_size / factor)
        real_num = int(round(nsamples / factor,0)) # final number of samples (without fast_size)
        
        # Since resample is using the fft, we zeros pad to have dyadic number of samples to speed up performance
        total_pading = (fast_size-nsamples)
        n_pad_start = int(total_pading/2) if (total_pading % 2) == 0 else int(total_pading/2)+1
        n_pad_end = int(total_pading/2)
        n_pad_resampled = int(round(n_pad_start/factor,0))
        resampled_samples = signal.resample(np.pad(signal_model.samples,(n_pad_start,n_pad_end)), num)[n_pad_resampled:real_num+n_pad_resampled]
        resampled_signal_model.samples = resampled_samples
        resampled_signal_model.sample_rate = target_sample_rate
        return resampled_signal_model