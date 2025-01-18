"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    DetectorsStep
    Step in the Artefact detection interface to select detectors to run.
"""

from qtpy import QtWidgets
from qtpy.QtCore import QRegExp
from qtpy.QtGui import QRegExpValidator

from CEAMSTools.DetectArtifacts.FilterSignalsStep.FilterSignalsStep import FilterSignalsStep
from CEAMSTools.DetectArtifacts.DetectorsStep.Ui_DetectorsStep import Ui_DetectorsStep
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState

class DetectorsStep( BaseStepView,  Ui_DetectorsStep, QtWidgets.QWidget):
    """
        DetectorsStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to activate or by-pass the appropriate modules to run, 
        in order to run or not specific detectors.
    """
    
    # Key for the context shared with other step of the preset
    context_common_group = "artifact_group"
    context_common_name = "artifact_name"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Set input validators
        # Create a QRegExpValidator with the desired regular expression
        # Regular expression for alphanumeric, space, dash, and latin1 (ISO/CEI 8859-1) characters
        regex = QRegExp(r'^[a-zA-Z0-9ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ\s-_]*$')
        validator = QRegExpValidator(regex)

        self.stages_sel = '1,2,3,5'

        # Set the validator for the QLineEdit
        self.unique_name_lineEdit.setValidator(validator)
        self.unique_name_lineEdit.setMaxLength(64)
        self.unique_group_lineEdit.setValidator(validator)
        self.unique_group_lineEdit.setMaxLength(64)
        
        # Define modules, state and nodes to talk to
        # flatline
        self._node_id_SpectralDetector_flatline = "bb852d74-45b5-4bd3-9e8b-73ae5ef93f7f"
        # high freq
        self._node_id_stft_highfreq = "99e3de6b-d59e-4151-9b3a-2b69aa015820"
        self._node_id_SpectralDetector_glitch_rel = "55ca6e02-e2b3-469e-b5f9-a878d1b3ec2c"
        self._node_id_SpectralDetector_glitsh_abs = "787ab295-8f3b-4a76-91b6-4d0303261d73"
        # persistent noise
        self._node_id_SpectralDetector_noise = "3c2ea592-fbbd-4d95-9be9-c2414157ddc0"
        # power line
        self._node_id_SpectralDetector_60Hz_abs = "f15c4b54-bc09-4338-983a-df244c7eb915"
        self._node_id_SpectralDetector_60Hz_rel = "eb5f8c18-de1e-4bef-a747-2888c774c878"
        self._node_id_SpectralDetector_60Hz_abs1 = "ff04ef89-738b-46be-a8d4-0a5f2fd3aa31"
        # bsl var
        self._node_id_lowpass_bslvar = "b5fc288d-302d-4ab0-8124-e8fef65c63e1"
        self._node_id_stft_bslvar = "ea6060df-a4da-4ec1-a75c-399ece7a3c1b"
        self._node_id_SpectralDetector_bslvar = "9f5b5bca-82d9-449c-a93b-59fc406cd38b"
        # muscle
        self._node_id_bandpadd_muscle_emg = "2071b3de-85ce-4cdd-a573-4871e1d77cfd"
        self._node_id_resample_muscle_emg = "094c3c5a-1572-4925-8263-5acc7f75fbc7"
        self._node_id_stft_muscle_emg = "20a3a456-06d7-4133-8a9f-0da225db865a"
        self._node_id_SpectralDetector_muscle_emg = "a64a02ed-d17b-493d-8175-2c85c48731d9"
        self._node_id_bandpadd_muscle_eeg = "97d5a68e-7113-46a4-9177-6e2fc8bbb6b8"
        self._node_id_resample_muscle_eeg = "6053f3b3-ff5d-4674-b691-a9fde318f9ca"
        self._node_id_stft_muscle_eeg = "cd5bf880-cde1-4a79-8d1b-6aea292d878c"
        self._node_id_SpectralDetector_muscle_eeg = "77e5dad4-f76e-46a0-bf68-6f0d3c677318"
        self._node_id_SpectralDetector_muscle_eeg_1 = "060cb108-2c37-4fc9-9e89-83b777133d01"
        # common group and name
        self._node_id_combine_event = "ac5efd3e-15f4-428c-a5d7-5b5ac3fce300"

        # Sleep Stage Events 
        self._node_id_sleep_stages = "d7196198-e2f9-432c-9134-c825e7a19193"

        # Subscribe to the publisher for each topic
        # Input nodes port
        self._low_freq_topic_abs = f'{self._node_id_SpectralDetector_60Hz_abs}.low_freq'
        self._pub_sub_manager.subscribe(self, self._low_freq_topic_abs)
        self._high_freq_topic_abs = f'{self._node_id_SpectralDetector_60Hz_abs}.high_freq'
        self._pub_sub_manager.subscribe(self, self._high_freq_topic_abs)
        self._low_freq_topic_rel = f'{self._node_id_SpectralDetector_60Hz_rel}.low_freq'
        self._pub_sub_manager.subscribe(self, self._low_freq_topic_rel)
        self._high_freq_topic_rel = f'{self._node_id_SpectralDetector_60Hz_rel}.high_freq'
        self._pub_sub_manager.subscribe(self, self._high_freq_topic_rel)
        self._high_freq_topic_rel_bsl = f'{self._node_id_SpectralDetector_60Hz_rel}.bsl_high_freq'
        self._pub_sub_manager.subscribe(self, self._high_freq_topic_rel_bsl)
        self._low_freq_topic_abs1 = f'{self._node_id_SpectralDetector_60Hz_abs1}.low_freq'
        self._pub_sub_manager.subscribe(self, self._low_freq_topic_abs1)
        self._high_freq_topic_abs1 = f'{self._node_id_SpectralDetector_60Hz_abs1}.high_freq'
        self._pub_sub_manager.subscribe(self, self._high_freq_topic_abs1)

        self._new_event_group_topic = f'{self._node_id_combine_event}.new_event_group'
        self._pub_sub_manager.subscribe(self, self._new_event_group_topic)
        self._new_event_name_topic = f'{self._node_id_combine_event}.new_event_name'
        self._pub_sub_manager.subscribe(self, self._new_event_name_topic)

        # Default value of the current context
        if self.common_radioButton.isChecked():
            self._context_manager[DetectorsStep.context_common_group] = "art_snooz"
            self._context_manager[DetectorsStep.context_common_name] = "art_snooz"
        else:
            self._context_manager[DetectorsStep.context_common_group] = ""
            self._context_manager[DetectorsStep.context_common_name] = ""            

        self._sleep_stage_topic = f'{self._node_id_sleep_stages}.stages'
        self._pub_sub_manager.subscribe(self, self._sleep_stage_topic)

    # Ask for the settings to the publisher to display on the SettingsView
    def load_settings(self):

        # Input nodes
        self._pub_sub_manager.publish(self, self._low_freq_topic_abs, 'ping')
        self._pub_sub_manager.publish(self, self._high_freq_topic_abs, 'ping')
        self._pub_sub_manager.publish(self, self._low_freq_topic_rel, 'ping')
        self._pub_sub_manager.publish(self, self._high_freq_topic_rel, 'ping')
        self._pub_sub_manager.publish(self, self._high_freq_topic_rel_bsl, 'ping')
        self._pub_sub_manager.publish(self, self._low_freq_topic_abs1, 'ping')
        self._pub_sub_manager.publish(self, self._high_freq_topic_abs1, 'ping')
        self._pub_sub_manager.publish(self, self._new_event_group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._new_event_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._sleep_stage_topic, 'ping')
        self.checkBox_0.setChecked('0' in self.stages_sel)
        self.checkBox_1.setChecked('1' in self.stages_sel)
        self.checkBox_2.setChecked('2' in self.stages_sel)
        self.checkBox_3.setChecked('3' in self.stages_sel)
        self.checkBox_5.setChecked('5' in self.stages_sel)
        self.checkBox_9.setChecked('9' in self.stages_sel)

        # Activation state
        self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_flatline+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_stft_highfreq+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_glitch_rel+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_glitsh_abs+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_noise+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_60Hz_abs+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_60Hz_rel+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_60Hz_abs1+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_lowpass_bslvar+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_stft_bslvar+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_bslvar+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_bandpadd_muscle_emg+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_resample_muscle_emg+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_stft_muscle_emg+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_muscle_emg+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_bandpadd_muscle_eeg+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_resample_muscle_eeg+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_stft_muscle_eeg+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_muscle_eeg+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_muscle_eeg_1+".get_activation_state", None)


    def on_notch_context_changed(self):
        # Extract the filter (if the notch filter is applied or not)
        self.notch_stopband = self._context_manager[FilterSignalsStep.context_notch]
        self.powerline_checkBox.setChecked(not self.notch_stopband[0])
        self.radioButton_50Hz.setEnabled(not self.notch_stopband[0])
        self.radioButton_60Hz.setEnabled(not self.notch_stopband[0])
        if not self.notch_stopband[0]:
            if '49' in self.notch_stopband[1]:
                self.radioButton_50Hz.setChecked(True)
            elif '59' in self.notch_stopband[1]:
                self.radioButton_60Hz.setChecked(True)


    # Called when the user clic on RUN
    # Message are sent to the publisher       
    def on_apply_settings(self):
        
        # Flatline
        if self.flatline_checkBox.isChecked():
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_flatline\
                +".activation_state_change", ActivationState.ACTIVATED)
        else:
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_flatline\
                +".activation_state_change", ActivationState.BYPASS)
        # high freq noise (glitch)
        if self.highfreq_checkBox.isChecked():
            self._pub_sub_manager.publish(self, self._node_id_stft_highfreq\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_glitch_rel\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_glitsh_abs\
                +".activation_state_change", ActivationState.ACTIVATED)
        else:
            self._pub_sub_manager.publish(self, self._node_id_stft_highfreq\
                +".activation_state_change", ActivationState.BYPASS)   
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_glitch_rel\
                +".activation_state_change", ActivationState.BYPASS)   
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_glitsh_abs\
                +".activation_state_change", ActivationState.BYPASS)   

        # Persistent noise
        if self.persistent_checkBox.isChecked():
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_noise\
                +".activation_state_change", ActivationState.ACTIVATED)
        else:
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_noise\
                +".activation_state_change", ActivationState.BYPASS)            

        # Send the 50 of 60 Hz information to setup properly the power line detector
        if self.powerline_checkBox.isChecked():
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_60Hz_abs\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_60Hz_rel\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_60Hz_abs1\
                +".activation_state_change", ActivationState.ACTIVATED)            
            if self.radioButton_60Hz.isChecked():
                self._pub_sub_manager.publish(self, self._low_freq_topic_abs, str(59))
                self._pub_sub_manager.publish(self, self._high_freq_topic_abs, str(61))
                self._pub_sub_manager.publish(self, self._low_freq_topic_rel, str(59))
                self._pub_sub_manager.publish(self, self._high_freq_topic_rel, str(61))
                self._pub_sub_manager.publish(self, self._high_freq_topic_rel_bsl, str(61))
                self._pub_sub_manager.publish(self, self._low_freq_topic_abs1, str(59))
                self._pub_sub_manager.publish(self, self._high_freq_topic_abs1, str(61))
            elif self.radioButton_50Hz.isChecked():
                self._pub_sub_manager.publish(self, self._low_freq_topic_abs, str(49))
                self._pub_sub_manager.publish(self, self._high_freq_topic_abs, str(51))
                self._pub_sub_manager.publish(self, self._low_freq_topic_rel, str(49))
                self._pub_sub_manager.publish(self, self._high_freq_topic_rel, str(51))
                self._pub_sub_manager.publish(self, self._high_freq_topic_rel_bsl, str(51))
                self._pub_sub_manager.publish(self, self._low_freq_topic_abs1, str(49))
                self._pub_sub_manager.publish(self, self._high_freq_topic_abs1, str(51))                
        else:
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_60Hz_abs\
                +".activation_state_change", ActivationState.BYPASS)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_60Hz_rel\
                +".activation_state_change", ActivationState.BYPASS)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_60Hz_abs1\
                +".activation_state_change", ActivationState.BYPASS)   

        # bsl variation
        if self.bslvar_checkBox.isChecked():
            self._pub_sub_manager.publish(self, self._node_id_lowpass_bslvar\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_stft_bslvar\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_bslvar\
                +".activation_state_change", ActivationState.ACTIVATED)
        else:
            self._pub_sub_manager.publish(self, self._node_id_lowpass_bslvar\
                +".activation_state_change", ActivationState.BYPASS)
            self._pub_sub_manager.publish(self, self._node_id_stft_bslvar\
                +".activation_state_change", ActivationState.BYPASS)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_bslvar\
                +".activation_state_change", ActivationState.BYPASS)

        # muscle
        if self.muscle_checkBox.isChecked():
            self._pub_sub_manager.publish(self, self._node_id_bandpadd_muscle_emg\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_resample_muscle_emg\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_stft_muscle_emg\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_muscle_emg\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_bandpadd_muscle_eeg\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_resample_muscle_eeg\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_stft_muscle_eeg\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_muscle_eeg\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_muscle_eeg_1\
                +".activation_state_change", ActivationState.ACTIVATED)
        else:
            self._pub_sub_manager.publish(self, self._node_id_bandpadd_muscle_emg\
                +".activation_state_change", ActivationState.BYPASS)
            self._pub_sub_manager.publish(self, self._node_id_resample_muscle_emg\
                +".activation_state_change", ActivationState.BYPASS)
            self._pub_sub_manager.publish(self, self._node_id_stft_muscle_emg\
                +".activation_state_change", ActivationState.BYPASS)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_muscle_emg\
                +".activation_state_change", ActivationState.BYPASS)
            self._pub_sub_manager.publish(self, self._node_id_bandpadd_muscle_eeg\
                +".activation_state_change", ActivationState.BYPASS)
            self._pub_sub_manager.publish(self, self._node_id_resample_muscle_eeg\
                +".activation_state_change", ActivationState.BYPASS)
            self._pub_sub_manager.publish(self, self._node_id_stft_muscle_eeg\
                +".activation_state_change", ActivationState.BYPASS)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_muscle_eeg\
                +".activation_state_change", ActivationState.BYPASS)
            self._pub_sub_manager.publish(self, self._node_id_SpectralDetector_muscle_eeg_1\
                +".activation_state_change", ActivationState.BYPASS)

        # Common group and name
        if self.common_radioButton.isChecked():
            self._pub_sub_manager.publish(self, self._new_event_group_topic, self.unique_group_lineEdit.text()) 
            self._pub_sub_manager.publish(self, self._new_event_name_topic, self.unique_name_lineEdit.text()) 
        if self.specific_radioButton.isChecked():
            self._pub_sub_manager.publish(self, self._new_event_group_topic, '') 
            self._pub_sub_manager.publish(self, self._new_event_name_topic,  '')    

        # Stages
        self._pub_sub_manager.publish(self, self._sleep_stage_topic, self.stages_sel)       


    # Called when the user changes the 50/60 Hz radio button
    def update_settings_slot(self):
        if self.powerline_checkBox.isChecked():
            self.radioButton_50Hz.setEnabled(True)
            self.radioButton_60Hz.setEnabled(True)
        else:
            self.radioButton_50Hz.setEnabled(False)
            self.radioButton_60Hz.setEnabled(False)


    # Called when the user changes the group/name radio button
    def update_event_label_slot(self):
        if self.common_radioButton.isChecked():
            self.unique_group_lineEdit.setEnabled(True)
            self.unique_name_lineEdit.setEnabled(True)
            self._context_manager[DetectorsStep.context_common_group] = self.unique_group_lineEdit.text()
            self._context_manager[DetectorsStep.context_common_name] = self.unique_name_lineEdit.text()
        if self.specific_radioButton.isChecked():
            self.unique_group_lineEdit.setEnabled(False)
            self.unique_name_lineEdit.setEnabled(False)
            self._context_manager[DetectorsStep.context_common_group] = ''
            self._context_manager[DetectorsStep.context_common_name] = '' 


    def update_stages_slot(self):
        stages_message = []
        if self.checkBox_0.isChecked():
            stages_message.append('0')
        if self.checkBox_1.isChecked():
            stages_message.append('1')
        if self.checkBox_2.isChecked():
            stages_message.append('2')
        if self.checkBox_3.isChecked():
            stages_message.append('3')
        if self.checkBox_5.isChecked():
            stages_message.append('5')
        if self.checkBox_9.isChecked():
            stages_message.append('9')
        self.stages_sel = (','.join(stages_message))


    # To init 
    # Called by a node in response to a ping request. 
    # Ping request are sent whenever we need to know the value of a parameter of a node.
    # Needed to load properly a pipeline saved
    def on_topic_response(self, topic, message, sender):
        if topic == self._low_freq_topic_rel:
            if message == '59':
                self.radioButton_60Hz.setChecked(True)
                self.radioButton_50Hz.setChecked(False)
            if message == '49':
                self.radioButton_50Hz.setChecked(True)
                self.radioButton_60Hz.setChecked(False)
        if topic == self._node_id_SpectralDetector_flatline+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.flatline_checkBox.setChecked(True)
            elif message == ActivationState.BYPASS:
                self.flatline_checkBox.setChecked(False)
        if topic == self._node_id_SpectralDetector_60Hz_abs+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.powerline_checkBox.setChecked(True)
            elif message == ActivationState.BYPASS:
                self.powerline_checkBox.setChecked(False)
        if topic == self._node_id_stft_bslvar+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.bslvar_checkBox.setChecked(True)
            elif message == ActivationState.BYPASS:
                self.bslvar_checkBox.setChecked(False)
        if topic == self._node_id_stft_muscle_eeg+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.muscle_checkBox.setChecked(True)
            elif message == ActivationState.BYPASS:
                self.muscle_checkBox.setChecked(False)
        if topic == self._node_id_stft_highfreq+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.highfreq_checkBox.setChecked(True)
            elif message == ActivationState.BYPASS:
                self.highfreq_checkBox.setChecked(False)
        if topic == self._node_id_SpectralDetector_noise+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.persistent_checkBox.setChecked(True)
            elif message == ActivationState.BYPASS:
                self.persistent_checkBox.setChecked(False)
        if topic == self._new_event_group_topic:
            if message=='':
                self.specific_radioButton.setChecked(True)
                self.unique_group_lineEdit.setEnabled(False)
            else:
                self.common_radioButton.setChecked(True)
                self.unique_group_lineEdit.setEnabled(True)
                self.unique_group_lineEdit.setText(message)
            self._context_manager[DetectorsStep.context_common_group] = message
        if topic == self._new_event_name_topic:
            if message=='':
                self.specific_radioButton.setChecked(True)
                self.unique_name_lineEdit.setEnabled(False)
            else:
                self.common_radioButton.setChecked(True)
                self.unique_name_lineEdit.setEnabled(True)
                self.unique_name_lineEdit.setText(message)
            self._context_manager[DetectorsStep.context_common_name] = message
        if topic == self._sleep_stage_topic:
            self.stages_sel = message


    # Called when a value listened is changed
    # No body asked for the value (no ping), but the value changed and
    # some subscribed to the topic
    def on_topic_update(self, topic, message, sender):
        if topic==self._context_manager.topic:
            if message==FilterSignalsStep.context_notch: # key of the context dict
                self.on_notch_context_changed()


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            # Input nodes ports
            self._pub_sub_manager.unsubscribe(self, self._low_freq_topic_abs)
            self._pub_sub_manager.unsubscribe(self, self._high_freq_topic_abs)
            self._pub_sub_manager.unsubscribe(self, self._low_freq_topic_rel)
            self._pub_sub_manager.unsubscribe(self, self._high_freq_topic_rel)
            self._pub_sub_manager.unsubscribe(self, self._high_freq_topic_rel_bsl)
            self._pub_sub_manager.unsubscribe(self, self._low_freq_topic_abs1)
            self._pub_sub_manager.unsubscribe(self, self._high_freq_topic_abs1)
            self._pub_sub_manager.unsubscribe(self, self._new_event_group_topic)
            self._pub_sub_manager.unsubscribe(self, self._new_event_name_topic)