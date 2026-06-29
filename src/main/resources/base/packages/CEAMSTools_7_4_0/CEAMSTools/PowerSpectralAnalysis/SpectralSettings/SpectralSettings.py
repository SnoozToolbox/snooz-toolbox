#! /usr/bin/env python3
"""
    SpectralSettings
    To define the settings to perform the Short Time Fourier Transform and the Power Spectral Analysis.
"""

from CEAMSTools.PowerSpectralAnalysis.SpectralSettings.Ui_SpectralSettings import Ui_SpectralSettings
from CEAMSTools.PowerSpectralAnalysis.SelectionStep.SelectionStep import SelectionStep
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState
from widgets.WarningDialog import WarningDialog

from qtpy import QtWidgets
from qtpy.QtWidgets import QMessageBox

class SpectralSettings(BaseStepView, Ui_SpectralSettings, QtWidgets.QWidget):
    """
        SpectralSettings
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform modules of the spectral settings and
        the selected stages and periods.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules and nodes to talk to
        #self._node_id_SleepStageEvent = "137420bc-d6ce-4928-a040-7121ba024020" # provide in which sleep stage and periods we analyse the spectral power
        self._node_id_stft_std = "159bfdad-5000-474b-ae38-8e95ff4142b2" # provide the win len and win step to the stft and activate if std
        self._node_id_stft_event = "ea31a87d-038c-4e24-a9c2-66b54aaca483" # provide the win len and win step to the stft and activate if std and on events
        self._node_id_IRASA = "fe5c4a13-f709-4edc-9e5f-9c7908c85e35"  # provide the win len and win step to the IRASA and activate if R&A
        self._node_id_PSA_std = "4bb8c9ac-64e8-4cec-9c2c-5a00c80b4eae" # provide the band width to the PSA Compilation
        self._node_id_PSA_evt = "9dfbe6b9-1887-452a-ac3b-33f1235f9b0a"  # provide the band width to the PSA on Events
        #add the IRASA compilation (another instance of PSA Compilation but plugged to the IRASA computation)
        self._node_id_PSA_Rhythmic_IRASA = "d16022c4-3ac0-4982-aa3e-dfff4cada99a"  # provide the band width to the PSA on IRASA
        self._node_id_PSA_Arhythmic_IRASA = "0ddf2d8d-943d-4583-8b2d-6184ad208119" # provide the band width to the Arhythmic component of IRASA
        self._node_id_PSA_FOOOF = "05044aa2-4a45-44ae-a5a8-b6182ecf8ec2" # provide the band width to the PSA on FOOOF
        
        self._node_id_constant_first_freq = "414a9746-fee0-4807-8d2e-44aba2369c16"
        self._node_id_constant_last_freq = "64038a3b-6640-437a-96b1-2d9bf7f5db7f"
        self._node_id_constant_mini_band = "fb63a9cd-9858-4aab-b33c-5b584702f23d"

        self._node_id_constant_win_len_step = "989ef4f7-2ce1-4727-bc80-5b6d18c34390"
        self._node_id_constant_win_step_sec = "1279a45a-d0d2-4f7e-85f9-e365ecdcd1d6"

        # Subscribe to the publisher for each node you want to talk to
        self._win_name_IRASA_topic = f'{self._node_id_IRASA}.window_name'
        self._pub_sub_manager.subscribe(self, self._win_name_IRASA_topic)
        self._flag_IRASA_topic = f'{self._node_id_IRASA}.flag'
        self._pub_sub_manager.subscribe(self, self._flag_IRASA_topic)

        self._constant_first_freq_topic = f'{self._node_id_constant_first_freq}.constant'
        self._pub_sub_manager.subscribe(self, self._constant_first_freq_topic)
        self._constant_last_freq_topic = f'{self._node_id_constant_last_freq}.constant'
        self._pub_sub_manager.subscribe(self, self._constant_last_freq_topic)
        self._constant_mini_band_topic = f'{self._node_id_constant_mini_band}.constant'
        self._pub_sub_manager.subscribe(self, self._constant_mini_band_topic)
        self._constant_win_len_topic = f'{self._node_id_constant_win_len_step}.constant'
        self._pub_sub_manager.subscribe(self, self._constant_win_len_topic)
        self._constant_win_step_topic = f'{self._node_id_constant_win_step_sec}.constant'
        self._pub_sub_manager.subscribe(self, self._constant_win_step_topic)

        # Connect radio buttons to update activation states immediately
        self.std_radioButton.clicked.connect(self.update_activation_states)
        self.RA_radioButton.clicked.connect(self.update_activation_states)
        self.FoooF_radioButton.clicked.connect(self.update_activation_states)

    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView

        self._pub_sub_manager.publish(self, self._node_id_stft_std+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_PSA_std+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_IRASA+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_PSA_FOOOF+".get_activation_state", None)

        self._pub_sub_manager.publish(self, self._win_name_IRASA_topic, 'ping')
        self._pub_sub_manager.publish(self, self._flag_IRASA_topic, 'ping')

        self._pub_sub_manager.publish(self, self._constant_first_freq_topic, 'ping')
        self._pub_sub_manager.publish(self, self._constant_last_freq_topic, 'ping')
        self._pub_sub_manager.publish(self, self._constant_mini_band_topic, 'ping')
        self._pub_sub_manager.publish(self, self._constant_win_len_topic, 'ping')
        self._pub_sub_manager.publish(self, self._constant_win_step_topic, 'ping')

        # Update activation states based on current radio button selection
        self.update_activation_states()

    # Called when the user clic on RUN or save
    # Message are sent to the publisher   
    def on_apply_settings(self):
        # Double check the values in case the user did not fix them
        self.miniband_edit_slot()
        self.lastfreq_edit_slot()

        self._pub_sub_manager.publish(self, self._constant_first_freq_topic, self.first_freq_lineEdit.text())
        self._pub_sub_manager.publish(self, self._constant_last_freq_topic, self.last_freq_lineEdit.text())
        self._pub_sub_manager.publish(self, self._constant_mini_band_topic, self.miniband_lineEdit.text())
        self._pub_sub_manager.publish(self, self._constant_win_len_topic, self.win_len_lineEdit.text())
        self._pub_sub_manager.publish(self, self._constant_win_step_topic, self.win_step_lineEdit.text())

        # Update activation states based on radio button selection
        self.update_activation_states()
            
    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        try: 
            fft_win_len = float(self.win_len_lineEdit.text())
        except:
            WarningDialog(f"Unable to convert the text entered for 'fft window length' into a float number (expected format: x.x) in step '6 - Spectral Settings'.")
            return False
        freq_bins = 1.0/fft_win_len
        try:
            fft_win_step = float(self.win_step_lineEdit.text())
        except:
            WarningDialog(f"Unable to convert the text entered for 'fft window step' into a float number (expected format: x.x) in step '6 - Spectral Settings'.")
            return False
        try:
            mini_bandwidth = float(self.miniband_lineEdit.text())
        except:
            WarningDialog(f"Unable to convert the text entered for 'mini bandwidth' into a float number (expected format: x.x) in step '6 - Spectral Settings'.")
            return False
        if not (mini_bandwidth/freq_bins).is_integer():
            WarningDialog(f"The width of each mini band ({mini_bandwidth}Hz) is not a multiple of the frequency bins ({freq_bins}Hz) in step '6 - Spectral Settings'.")
            return False
        try:
            start_freq = float(self.first_freq_lineEdit.text())
        except:
            WarningDialog(f"Unable to convert the text entered for 'First frequency analyzed' into a float number (expected format: x.x) in step '6 - Spectral Settings'.")
            return False               
        if (start_freq+freq_bins)>mini_bandwidth and start_freq<mini_bandwidth:
            WarningDialog(f"It's impossible to start the first mini band at {start_freq}Hz with the current frequency bins ({freq_bins}Hz) and the current mini bandwidth ({mini_bandwidth}Hz) in step '6 - Spectral Settings'.")
            return False
        try:
            end_freq = float(self.last_freq_lineEdit.text())
        except:
            WarningDialog(f"Unable to convert the text entered for 'Last frequency analyzed' into a float number (expected format: x.x) in step '6 - Spectral Settings'.")
            return False
        if self.RA_radioButton.isChecked() and start_freq == 0:
            WarningDialog(f"First frequency analyzed cannot be set to 0 Hz when IRASA method is selected in step '6 - Spectral Settings'.")
            return False

        return True


    # Called when the user edit the mini band width or the fft windows length
    def miniband_edit_slot(self):
        try:
            fft_win_len = float(self.win_len_lineEdit.text())
        except:
            WarningDialog(f"Unable to convert the text entered for 'fft window length' into a float number (expected format: x.x).")
            self.win_len_lineEdit.setText('5')
            fft_win_len = float(self.win_len_lineEdit.text())
        freq_bins = 1.0/fft_win_len
        try :
            minibandwidth = float(self.miniband_lineEdit.text())
        except:
            WarningDialog(f"Unable to convert the text entered for 'mini bandwidth' into a float number (expected format: x.x).")
            self.miniband_lineEdit.setText('1')
            minibandwidth = float(self.miniband_lineEdit.text())
        if minibandwidth < freq_bins:
            log_msg = QMessageBox()
            log_msg.setWindowTitle("Log Message")
            message_1 = "The width of the mini band has to be equal or larger than the FFT frequency bin resolution (Hz) which is " + str(freq_bins) + " Hz"
            message_2 = "Increase the the mini bandwidth or update the STFT windows length (s) currently set to "+str(fft_win_len)+ " s"
            message_3 = "Make sure the mini bandwidth is a multiple of the frequency bin resolution i.e. "+str(freq_bins)+" Hz, "+str(freq_bins*2)+" Hz or "+str(freq_bins*3)+" Hz..."
            self.miniband_lineEdit.setText(str(freq_bins))
            log_msg.setText(message_1 + '\n' + message_2 + '\n' + message_3)
            log_msg.setIcon(QMessageBox.Critical)
            log_msg.exec_()


    # Called when the user edit last frequency 
    def lastfreq_edit_slot(self):
        # The limitation is applied in the PSACompilation code instead than in the UI.
        pass 

    def update_activation_states(self):
        """Update module activation states based on radio button selections"""
        if self.std_radioButton.isChecked() and self._context_manager[SelectionStep.context_PSA_annot_selection]==0:
            self._pub_sub_manager.publish(self, self._node_id_stft_std+".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_std+".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_IRASA+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_Rhythmic_IRASA+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_Arhythmic_IRASA+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_FOOOF+".activation_state_change", ActivationState.DEACTIVATED)
        elif self.RA_radioButton.isChecked() and self._context_manager[SelectionStep.context_PSA_annot_selection]==0:
            self._pub_sub_manager.publish(self, self._node_id_stft_std+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_std+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_IRASA+".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_Rhythmic_IRASA+".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_Arhythmic_IRASA+".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_FOOOF+".activation_state_change", ActivationState.DEACTIVATED)
        elif self.FoooF_radioButton.isChecked() and self._context_manager[SelectionStep.context_PSA_annot_selection]==0:
            self._pub_sub_manager.publish(self, self._node_id_stft_std+".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_std+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_IRASA+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_Rhythmic_IRASA+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_Arhythmic_IRASA+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_FOOOF+".activation_state_change", ActivationState.ACTIVATED)
        else:
            self._pub_sub_manager.publish(self, self._node_id_stft_std+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_std+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_IRASA+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_Rhythmic_IRASA+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_Arhythmic_IRASA+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_FOOOF+".activation_state_change", ActivationState.DEACTIVATED)
    
    def Disable_PSA_technique(self):
        if self._context_manager[SelectionStep.context_PSA_annot_selection]==1:
            self.std_radioButton.setChecked(True)
            self.std_radioButton.setEnabled(False)
            self.RA_radioButton.setEnabled(False)
            self.FoooF_radioButton.setEnabled(False)
            self.label_5.setEnabled(False)
            self.label_11.setEnabled(False)
            self.label_12.setEnabled(False)
        else:
            self.std_radioButton.setEnabled(True)
            self.RA_radioButton.setEnabled(True)
            self.FoooF_radioButton.setEnabled(True)
            self.label_5.setEnabled(True)
            self.label_11.setEnabled(True)
            self.label_12.setEnabled(True)
    # Called by a node in response to a ping request. 
    # Ping request are sent whenever we need to know the value of a parameter of a node.
    def on_topic_response(self, topic, message, sender):

        if topic == self._constant_first_freq_topic:
            self.first_freq_lineEdit.setText(message)
        if topic == self._constant_last_freq_topic: 
            self.last_freq_lineEdit.setText(message)
        if topic == self._constant_mini_band_topic:
            self.miniband_lineEdit.setText(message)
        if topic == self._constant_win_len_topic:
            self.win_len_lineEdit.setText(message)
        if topic == self._constant_win_step_topic:
            self.win_step_lineEdit.setText(message)
            
        if topic == self._node_id_PSA_std+".get_activation_state":
            # Store the activation state to use with flag handling
            self._PSA_std_activated = (message == ActivationState.ACTIVATED)
            if self._PSA_std_activated:
                self.std_radioButton.setChecked(True)
                self.RA_radioButton.setChecked(False)
                self.FoooF_radioButton.setChecked(False)
        if topic == self._node_id_IRASA+".get_activation_state":
            self._IRASA_activated = (message == ActivationState.ACTIVATED)
            if self._IRASA_activated:
                self.RA_radioButton.setChecked(True)
                self.std_radioButton.setChecked(False)
                self.FoooF_radioButton.setChecked(False)
        if topic == self._node_id_PSA_FOOOF+".get_activation_state":
            self._FOOOF_activated = (message == ActivationState.ACTIVATED)
            if self._FOOOF_activated:
                self.FoooF_radioButton.setChecked(True)
                self.std_radioButton.setChecked(False)
                self.RA_radioButton.setChecked(False)

    def on_topic_update(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
            at any update, does not necessary answer to a ping.
            To listen to any modification not only when you ask (ping)
        """
        super().on_topic_update(topic, message, sender)

        if topic==self._context_manager.topic:
            # PSA section selection changed
            if message==SelectionStep.context_PSA_annot_selection: # key of the context dict
                if self._context_manager[SelectionStep.context_PSA_annot_selection]==1:
                    self.Disable_PSA_technique()
                else:
                    self.Disable_PSA_technique()

    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._win_name_IRASA_topic)
            self._pub_sub_manager.unsubscribe(self, self._flag_IRASA_topic)

            self._pub_sub_manager.unsubscribe(self, self._constant_first_freq_topic)
            self._pub_sub_manager.unsubscribe(self, self._constant_last_freq_topic)
            self._pub_sub_manager.unsubscribe(self, self._constant_mini_band_topic)
            self._pub_sub_manager.unsubscribe(self, self._constant_win_len_topic)
            self._pub_sub_manager.unsubscribe(self, self._constant_win_step_topic)