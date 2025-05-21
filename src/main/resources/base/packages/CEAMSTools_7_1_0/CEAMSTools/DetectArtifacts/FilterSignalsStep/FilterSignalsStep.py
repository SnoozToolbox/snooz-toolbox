"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    FilterSignalsStep
    Settings viewer of the filters (artefact rejection)
    This custom step is usefull to use context with filters.
"""

from qtpy import QtWidgets

from CEAMSTools.DetectArtifacts.FilterSignalsStep.Ui_FilterSignalsStep import Ui_FilterSignalsStep
from CEAMSTools.DetectArtifacts.InputFilesArtStep.InputFilesArtStep import InputFilesStep
from commons.BaseStepView import BaseStepView
import config
from flowpipe.ActivationState import ActivationState

from widgets.WarningDialog import WarningDialog


class FilterSignalsStep( BaseStepView,  Ui_FilterSignalsStep, QtWidgets.QWidget):
    """
        FilterSignalsStep
        Settings viewer of the filters (artefact rejection)
        This custom step is usefull to use context with filters.
    """
    # Key for the context shared with other step of the preset
    context_notch = "notch_band"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # self.setStyleSheet(f"color: {config.C.text_foreground_color_X};")
        # self.setStyleSheet(f"background-color: {config.C.background_color_X};")

        # Node identifier taken from resources/presets/ArtefactDetection_PowerLine/ArtefactDetection_PowerLine.json
        self._node_id_bandpass_filter = "e5120882-ba1a-48c6-8414-a51b2286ce65"
        self._node_id_notch_filter = "d5bec732-c479-4928-aea5-75484116f972"
        self._node_id_SpectralDetector_60Hz_abs = "f15c4b54-bc09-4338-983a-df244c7eb915"
        self._node_id_SpectralDetector_60Hz_rel = "eb5f8c18-de1e-4bef-a747-2888c774c878"
        self._node_id_SpectralDetector_60Hz_abs1 = "ff04ef89-738b-46be-a8d4-0a5f2fd3aa31"

        # Input node topic
        self._low_high_cutoff_topic = f'{self._node_id_bandpass_filter}.cutoff'
        self._pub_sub_manager.subscribe(self, self._low_high_cutoff_topic)
        self._notch_cutoff_topic = f'{self._node_id_notch_filter}.cutoff'
        self._pub_sub_manager.subscribe(self, self._notch_cutoff_topic)
        self._type_filter_topic = f'{self._node_id_bandpass_filter}.type'
        self._pub_sub_manager.subscribe(self, self._type_filter_topic)


        # Definition : Notch activated (True) and cutoff frequencies
        self.notch_stopband = [False, "59 61"] # Default cutoff init for the notch
        # _context_manager is inherited from the BaseStepView
        # it allows to share information between steps in the step-by-step interface
        # ContextManager is a dictionary that publish an update through the 
        # PubSubManager whenever a value is modified.
        self._context_manager[FilterSignalsStep.context_notch] = self.notch_stopband

        # Suggested frequency band of band pass filter
        self.MAX_FREQ = 128
        self.LOW_FREQ = 0.3


    def update_low_cutoff_slot(self):
        if not float(self.low_cutoff_lineEdit.text()) == self.LOW_FREQ:
            warning_message = "Modifying the low cutoff frequency will have a huge impact on the Baseline Variation Detector, adjust the threshold properly."
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(warning_message)
            msg.setWindowTitle("Filter")
            msg.exec()


    def update_high_cutoff_slot(self):    
        if float(self.high_cutoff_lineEdit.text())>self.MAX_FREQ:
            error_message = "The high cutoff frequency is limited to 128 Hz due to downsampling at 256 Hz."
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText(error_message)
            msg.setWindowTitle("Filter")
            self.high_cutoff_lineEdit.setText('128')
            msg.exec()


    # Called when the user clic on the checkbox of the radio button
    def update_filter_settings(self):
        # Bandpass settings
        if self.bp_checkBox.isChecked():
            self.low_cutoff_lineEdit.setEnabled(True)
            self.high_cutoff_lineEdit.setEnabled(True)
        else:
            self.low_cutoff_lineEdit.setEnabled(False)
            self.high_cutoff_lineEdit.setEnabled(False)
        # Notch settings
        if self.notch_checkBox.isChecked():
            self.radioButton_60Hz.setEnabled(True)
            self.radioButton_50Hz.setEnabled(True)
            if self.radioButton_50Hz.isChecked():
                self.notch_stopband = [True, "49 51"]
            if self.radioButton_60Hz.isChecked():
                self.notch_stopband = [True, "59 61"]
        else:
            self.radioButton_60Hz.setEnabled(False)
            self.radioButton_50Hz.setEnabled(False)
            self.notch_stopband = [False, "59 61"]
        self._context_manager[FilterSignalsStep.context_notch] = self.notch_stopband


    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._low_high_cutoff_topic, 'ping')
        self._pub_sub_manager.publish(self, self._notch_cutoff_topic, 'ping')
        # Activation state
        self._pub_sub_manager.publish(self, self._node_id_bandpass_filter+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_notch_filter+".get_activation_state", None)        
        self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_60Hz_abs+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_60Hz_rel+".get_activation_state", None)     
        self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_60Hz_abs1+".get_activation_state", None)


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if float(self.high_cutoff_lineEdit.text())>(self.min_fs/2):
            message = f'The high frequency cutoff ({self.high_cutoff_lineEdit.text()}Hz) '\
                + f'of the band pass filter is higher than the Nyquist frequency ({self.min_fs/2}Hz)'\
                    + f'\n\nIn step 2- Filter EEG signals : lower the high frequency cutoff of the band '\
                        + f'pass below the Nyquist frequency of {self.min_fs/2}Hz.'
            WarningDialog(message)     
            return False
        else:
            return True


    # Called when the user clic on RUN
    # Message are sent to the publisher
    def on_apply_settings(self):
        if float(self.low_cutoff_lineEdit.text())>0:
            self._pub_sub_manager.publish(self, self._type_filter_topic, 'bandpass')
            self._pub_sub_manager.publish(self, self._low_high_cutoff_topic, \
                self.low_cutoff_lineEdit.text() + ' ' + self.high_cutoff_lineEdit.text())
        else:
            self._pub_sub_manager.publish(self, self._type_filter_topic, 'lowpass')
            self._pub_sub_manager.publish(self, self._low_high_cutoff_topic, self.high_cutoff_lineEdit.text()) 
     
        self._pub_sub_manager.publish(self, self._notch_cutoff_topic, \
            str( self.notch_stopband[1]) )
        # Activate the notch filter and by-pass the power line detectors
        if self.notch_checkBox.isChecked():
            self._pub_sub_manager.publish(self, self._node_id_notch_filter\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_60Hz_abs\
                +".activation_state_change", ActivationState.BYPASS)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_60Hz_rel\
                +".activation_state_change", ActivationState.BYPASS)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_60Hz_abs1\
                +".activation_state_change", ActivationState.BYPASS)
        # By-pass the notch filter and activate the power line detectors
        else:
            self._pub_sub_manager.publish(self, self._node_id_notch_filter\
                +".activation_state_change", ActivationState.BYPASS)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_60Hz_abs\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_60Hz_rel\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_60Hz_abs1\
                +".activation_state_change", ActivationState.ACTIVATED)
        # Activate the bandpass filter
        if self.bp_checkBox.isChecked():
            self._pub_sub_manager.publish(self, self._node_id_bandpass_filter\
                +".activation_state_change", ActivationState.ACTIVATED)
        # By-pass the bandpass filter
        else:
            self._pub_sub_manager.publish(self, self._node_id_bandpass_filter\
                +".activation_state_change", ActivationState.BYPASS)


    # To init 
    # Called by a node in response to a ping request. 
    # Ping request are sent whenever we need to know the value of a parameter of a node.
    def on_topic_response(self, topic, message, sender):
        if topic == self._low_high_cutoff_topic:
            cutoff = message.split(' ')
            if len(cutoff)==1:
                self.low_cutoff_lineEdit.setText('0')
                self.high_cutoff_lineEdit.setText(cutoff[0])
            elif len(cutoff)>1:
                self.low_cutoff_lineEdit.setText(cutoff[0])
                self.high_cutoff_lineEdit.setText(cutoff[1])
        if topic == self._notch_cutoff_topic:
            self.notch_stopband[1] = message
            if message=="49 51":
                self.radioButton_50Hz.setChecked(True)
            elif message=="59 61":
                self.radioButton_60Hz.setChecked(True)
            self._context_manager[FilterSignalsStep.context_notch] = self.notch_stopband
        if topic == self._node_id_bandpass_filter+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.bp_checkBox.setChecked(True)
            elif message == ActivationState.BYPASS:
                self.bp_checkBox.setChecked(False)
            self.update_filter_settings()
        if topic == self._node_id_notch_filter+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.notch_checkBox.setChecked(True)
                self.notch_stopband[0] = True
            elif message == ActivationState.BYPASS:
                self.notch_checkBox.setChecked(False)
                self.notch_stopband[0] = False
            self._context_manager[FilterSignalsStep.context_notch] = self.notch_stopband
            self.update_filter_settings()


    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.
        
        if topic == self._context_manager.topic:
            # The message will be the KEY of the value that's been updated inside the context.
            # If it's the one you are looking for, we can then take the updated value and use it.
            if message == InputFilesStep.context_files_view:
                self.reader_settings_view = self._context_manager[InputFilesStep.context_files_view]
                alias = self.reader_settings_view.get_alias()
                eeg_chan_alias = alias['EEG']
                channels_info_df = self.reader_settings_view.channels_table_model.get_data()
                chans_used = channels_info_df[(channels_info_df['Use']==True) & channels_info_df['Channel'].isin(eeg_chan_alias)]
                if len(chans_used)>0:
                    self.min_fs = float(min(chans_used['Sample rate'].to_list()) )
                else:
                    self.min_fs = 256 # Default value when no channels are selected


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._low_high_cutoff_topic)
            self._pub_sub_manager.unsubscribe(self, self._notch_cutoff_topic)
            self._pub_sub_manager.unsubscribe(self, self._type_filter_topic)