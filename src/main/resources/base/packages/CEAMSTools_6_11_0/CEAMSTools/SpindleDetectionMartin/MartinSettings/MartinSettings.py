"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    MartinSettings
    Config Page in the spindle detection interface to define Martin settings.
"""
from qtpy import QtWidgets
from qtpy.QtCore import QRegExp
from qtpy.QtGui import QRegExpValidator

from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState
from CEAMSTools.SpindleDetectionMartin.MartinSettings.Ui_MartinSettings import Ui_MartinSettings
from CEAMSTools.SpindleDetectionMartin.Commons import ContextConstants


class MartinSettings( BaseStepView,  Ui_MartinSettings, QtWidgets.QWidget):
    """
        MartinSettings
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform modules of the Martin spindle detector settings.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Set input validators
        # Create a QRegExpValidator with the desired regular expression
        # Regular expression for alphanumeric, space, dash, and latin1 (ISO/CEI 8859-1) characters
        regex = QRegExp(r'^[a-zA-Z0-9ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ\s-_]*$')
        validator = QRegExpValidator(regex)

        # Set the validator for the QLineEdit
        self.name_lineEdit.setValidator(validator)
        self.name_lineEdit.setMaxLength(64)
        self.group_lineEdit.setValidator(validator)
        self.group_lineEdit.setMaxLength(64)

        # Define modules and nodes to talk to
        self._node_id_SpindleDetails_det = "0e3df2c0-7c41-4fa5-89bb-f6601ef8831a" # provide the spindle_parameters when spindles are detected
        self._node_id_SpindleDetails_anal = "28929dd9-a992-4e7b-be6b-9e0a6053ae4e" # provide the spindle_parameters when spindles are analyzed only
        self._node_id_thres_comput = "ae29d9c1-d46a-452b-bae2-d2caee253e39" # provide threshold value and behavior
        self._node_id_PreciseEvents = "28e85302-3f3a-4f98-83d9-4c688ea363be" # provide length limit (test again after precision) and event group/name 
        self._node_id_constant_group = "53dc47dd-b65b-41d9-8534-c1d85c79363a" # provide event group 
        self._node_id_constant_name = "73b79daf-92e6-46e1-9ff3-cceacbf273f3" # provide event name 

        # Subscribe to context manager for each node you want to talk to
        self._thres_def_topic = f'{self._node_id_thres_comput}.threshold_definition'
        self._pub_sub_manager.subscribe(self, self._thres_def_topic)
        self._thres_scope_topic = f'{self._node_id_thres_comput}.threshold_scope'
        self._pub_sub_manager.subscribe(self, self._thres_scope_topic)   
        self._group_topic = f'{self._node_id_constant_group}.constant'
        self._pub_sub_manager.subscribe(self, self._group_topic)
        self._name_topic = f'{self._node_id_constant_name}.constant'
        self._pub_sub_manager.subscribe(self, self._name_topic)     
        self._spindle_param_a4_det_topic = f'{self._node_id_SpindleDetails_det}.spindle_sel_param'
        self._pub_sub_manager.subscribe(self, self._spindle_param_a4_det_topic)    
        self._spindle_param_a4_anal_topic = f'{self._node_id_SpindleDetails_anal}.spindle_sel_param'
        self._pub_sub_manager.subscribe(self, self._spindle_param_a4_anal_topic)    

        

        self._context_manager[ContextConstants.context_per_cycle] = True

        self._spindle_a4_param = {}
     

    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._thres_def_topic, 'ping')
        self._pub_sub_manager.publish(self, self._thres_scope_topic, 'ping')
        self._pub_sub_manager.publish(self, self._group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._node_id_PreciseEvents+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._spindle_param_a4_det_topic, 'ping')


    def on_apply_settings(self):
        # Activate ResetSignalArtefact module if the excluded events signal is reset
        if self.precise_checkBox.isChecked():
            self._pub_sub_manager.publish(self, self._node_id_PreciseEvents+\
                ".activation_state_change", ActivationState.ACTIVATED)
        else:
            self._pub_sub_manager.publish(self, self._node_id_PreciseEvents+\
                ".activation_state_change", ActivationState.BYPASS)
        if self.threshold_cycle_checkBox.isChecked():
            self._pub_sub_manager.publish(self, self._thres_scope_topic, '1')
            #self._context_manager[MartinSettings.context_per_cycle] = True
        else:
            self._pub_sub_manager.publish(self, self._thres_scope_topic, '2')
            #self._context_manager[MartinSettings.context_per_cycle] = False
        self._pub_sub_manager.publish(self, self._thres_def_topic, self.threshold_lineEdit.text())
        self._pub_sub_manager.publish(self, self._group_topic, self.group_lineEdit.text())
        self._pub_sub_manager.publish(self, self._name_topic, self.name_lineEdit.text())

        # Init the _spindle_param_gen_topic and send the dict
        self._spindle_a4_param['spindle_name'] = self.name_lineEdit.text()
        self._spindle_a4_param['threshold'] = float(self.threshold_lineEdit.text())
        self._spindle_a4_param['threshold_per_cycle'] = int(self.threshold_cycle_checkBox.isChecked())
        self._spindle_a4_param['precision_on'] = int(self.precise_checkBox.isChecked())
        self._pub_sub_manager.publish(self, self._spindle_param_a4_det_topic, str(self._spindle_a4_param))
        self._pub_sub_manager.publish(self, self._spindle_param_a4_anal_topic, str(self._spindle_a4_param))
        

    def on_topic_response(self, topic, message, sender):
        if topic == self._thres_def_topic:
            self.threshold_lineEdit.setText(message)
        if topic == self._thres_scope_topic:
            if message == '1':
                self.threshold_cycle_checkBox.setChecked(True)
                self._context_manager[ContextConstants.context_per_cycle] = True
            else:
                self.threshold_cycle_checkBox.setChecked(False)
                self._context_manager[ContextConstants.context_per_cycle] = False
        if topic == self._group_topic:
            self.group_lineEdit.setText(message)
        if topic == self._name_topic:
            self.name_lineEdit.setText(message)
        if topic == self._node_id_PreciseEvents+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.precise_checkBox.setChecked(True)
            if message == ActivationState.BYPASS:
                self.precise_checkBox.setChecked(False)        
        if topic == self._spindle_param_a4_det_topic:
            if not message=='':
                self._spindle_a4_param = eval(message)


    # Called when user check/uncheck thresh_per_cycle checkbox
    def thresh_per_cycle_slot(self):
        self._context_manager[ContextConstants.context_per_cycle] = self.threshold_cycle_checkBox.isChecked()


    # Called when a value listened is changed
    # No body asked for the value (no ping), but the value changed and
    # some subscribed to the topic
    def on_topic_update(self, topic, message, sender):
        if topic==self._context_manager.topic:
            # If the in_sleep_cycle is unchecked from SpindleDetectorSelStep 
            #   -> remove the computation of the thresh per cycle (the opposite is not true)
            if message==ContextConstants.context_in_cycle: # key of the context dict
                if self._context_manager[ContextConstants.context_in_cycle]==False:
                    self.threshold_cycle_checkBox.setChecked(False)
                    self._context_manager[ContextConstants.context_per_cycle] = False


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._thres_def_topic)
            self._pub_sub_manager.unsubscribe(self, self._thres_scope_topic)
            self._pub_sub_manager.unsubscribe(self, self._group_topic)
            self._pub_sub_manager.unsubscribe(self, self._name_topic)
            self._pub_sub_manager.unsubscribe(self, self._spindle_param_a4_det_topic)
            self._pub_sub_manager.unsubscribe(self, self._spindle_param_a4_anal_topic)