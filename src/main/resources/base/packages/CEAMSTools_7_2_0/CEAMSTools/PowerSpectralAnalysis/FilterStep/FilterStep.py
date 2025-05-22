#! /usr/bin/env python3
"""
    FilterStep
    Step to define the filter settings
    Class to activate or not the filtering plugins and feed the inputs if needed.
"""

from qtpy import QtWidgets

from CEAMSTools.PowerSpectralAnalysis.FilterStep.Ui_FilterStep import Ui_FilterStep
from CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep import InputFilesStep
from flowpipe.ActivationState import ActivationState
from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog

class FilterStep(BaseStepView, Ui_FilterStep, QtWidgets.QWidget):
    """
        FilterStep
        Step to define the filter settings
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # If necessary, init the context. The context is a memory space shared by 
        # all steps of a tool. It is used to share and notice other steps whenever
        # the value in it changes. It's very useful when the parameter within a step
        # must have an impact in another step.
        #self._context_manager["context_FilterStep"] = {"the_data_I_want_to_share":"some_data"}

        self._node_id_bandpass_filter = "b36768be-9cab-41f9-850f-22edf97b1c13"
        self._node_id_notch_filter = "8f7c9ad5-7790-45bb-bcf0-03a5c125954a"
        # Input node topic
        self._low_high_cutoff_topic = f'{self._node_id_bandpass_filter}.cutoff'
        self._pub_sub_manager.subscribe(self, self._low_high_cutoff_topic)
        self._notch_cutoff_topic = f'{self._node_id_notch_filter}.cutoff'
        self._pub_sub_manager.subscribe(self, self._notch_cutoff_topic)

        # Definition : Notch activated (True) and cutoff frequencies
        self.notch_stopband = [False, "59 61"] # Default cutoff init for the notch
        self.min_fs = None

        
    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        self._pub_sub_manager.publish(self, self._low_high_cutoff_topic, 'ping')
        self._pub_sub_manager.publish(self, self._notch_cutoff_topic, 'ping')
        # Activation state
        self._pub_sub_manager.publish(self, self._node_id_bandpass_filter+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_notch_filter+".get_activation_state", None) 


    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.
        
        if topic == self._context_manager.topic:
            # The message will be the KEY of the value that's been updated inside the context.
            # If it's the one you are looking for, we can then take the updated value and use it.
            if message == InputFilesStep.context_files_view:
                self.reader_settings_view = self._context_manager[InputFilesStep.context_files_view]
                channels_info_df = self.reader_settings_view.channels_table_model.get_data()
                chans_used = channels_info_df[channels_info_df['Use']==True]
                if len(chans_used)>0:
                    self.min_fs = float(min(chans_used['Sample rate'].to_list()) )
                else:
                    self.min_fs = 256 # Default value when no channels are selected


    # Called by a node in response to a ping request. 
    # Ping request are sent whenever we need to know the value of a parameter of a node.
    def on_topic_response(self, topic, message, sender):
        if topic == self._low_high_cutoff_topic:
            cutoff = message.split(' ')
            if len(cutoff)>0:
                self.low_cutoff_lineEdit.setText(cutoff[0])
            if len(cutoff)>1:
                self.high_cutoff_lineEdit.setText(cutoff[1])
        if topic == self._notch_cutoff_topic:
            self.notch_stopband[1] = message
            if message=="49 51":
                self.radioButton_50Hz.setChecked(True)
            elif message=="59 61":
                self.radioButton_60Hz.setChecked(True)
        if topic == self._node_id_bandpass_filter+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.bp_checkBox.setChecked(True)
            elif message == ActivationState.BYPASS:
                self.bp_checkBox.setChecked(False)
            self.update_filter_settings_slot()
        if topic == self._node_id_notch_filter+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.notch_checkBox.setChecked(True)
                self.notch_stopband[0] = True
            elif message == ActivationState.BYPASS:
                self.notch_checkBox.setChecked(False)
                self.notch_stopband[0] = False
            self.update_filter_settings_slot()


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if float(self.high_cutoff_lineEdit.text())>(self.min_fs/2):
            message = f'The high frequency cutoff ({self.high_cutoff_lineEdit.text()}Hz) '\
                + f'of the band pass filter is higher than the Nyquist frequency ({self.min_fs/2}Hz)'\
                    + f'\n\nIn step 3- Filter Settings : lower the high frequency cutoff of the band '\
                        + f'pass below the Nyquist frequency of {self.min_fs/2}Hz.'
            WarningDialog(message) 
            return False
        return True


    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._low_high_cutoff_topic, \
            str(self.low_cutoff_lineEdit.text()) + ' ' + self.high_cutoff_lineEdit.text())
        self._pub_sub_manager.publish(self, self._notch_cutoff_topic, \
            str( self.notch_stopband[1]) )
        # Activate the notch filter and by-pass the power line detectors
        if self.notch_checkBox.isChecked():
            self._pub_sub_manager.publish(self, self._node_id_notch_filter\
                +".activation_state_change", ActivationState.ACTIVATED)
        # By-pass the notch filter and activate the power line detectors
        else:
            self._pub_sub_manager.publish(self, self._node_id_notch_filter\
                +".activation_state_change", ActivationState.BYPASS)
        # Activate the bandpass filter
        if self.bp_checkBox.isChecked():
            self._pub_sub_manager.publish(self, self._node_id_bandpass_filter\
                +".activation_state_change", ActivationState.ACTIVATED)
        # By-pass the bandpass filter
        else:
            self._pub_sub_manager.publish(self, self._node_id_bandpass_filter\
                +".activation_state_change", ActivationState.BYPASS)


    # Called when the user clic on the checkbox of the radio button
    def update_filter_settings_slot(self):
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


    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._low_high_cutoff_topic)
            self._pub_sub_manager.unsubscribe(self, self._notch_cutoff_topic)