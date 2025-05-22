"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    A7Settings
    Config Page in the spindle detection interface to define A7 settings.
"""
from qtpy import QtWidgets
from qtpy.QtCore import QRegularExpression
from qtpy.QtGui import QRegularExpressionValidator

from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState
from CEAMSTools.SpindleDetectionA7.A7Settings.Ui_A7Settings import Ui_A7Settings


class A7Settings( BaseStepView,  Ui_A7Settings, QtWidgets.QWidget):
    """
        A7Settings
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform modules of the A7 spindle detector settings.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Set input validators
        # Create a QRegularExpressionValidator with the desired regular expression
        # Regular expression for alphanumeric, space, dash, and latin1 (ISO/CEI 8859-1) characters
        regex = QRegularExpression(r'^[a-zA-Z0-9ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ\s-_]*$')
        validator = QRegularExpressionValidator(regex)

        # Set the validator for the QLineEdit
        self.name_lineEdit.setValidator(validator)
        self.name_lineEdit.setMaxLength(64)
        self.group_lineEdit.setValidator(validator)
        self.group_lineEdit.setMaxLength(64)

        # Define modules and nodes to talk to
        self._node_id_SpindleDetails_det = "0e3df2c0-7c41-4fa5-89bb-f6601ef8831a" # provide the spindle_parameters when spindles are detected
        self._node_id_SpindleDetails_anal = "28929dd9-a992-4e7b-be6b-9e0a6053ae4e" # provide the spindle_parameters when spindles are analyzed only
        self._node_id_SpindleA7 = "72b146ad-eca2-41b5-9994-87177883020e" # provide the spindle_parameters to detect spindles
        self._node_id_constant_group = "53dc47dd-b65b-41d9-8534-c1d85c79363a" # provide event group 
        self._node_id_constant_name = "73b79daf-92e6-46e1-9ff3-cceacbf273f3" # provide event name 

        # Subscribe to context manager for each node you want to talk to
        self._thresholds_a7_topic = f'{self._node_id_SpindleA7}.thresholds'
        self._pub_sub_manager.subscribe(self, self._thresholds_a7_topic)
        self._group_topic = f'{self._node_id_constant_group}.constant'
        self._pub_sub_manager.subscribe(self, self._group_topic)
        self._name_topic = f'{self._node_id_constant_name}.constant'
        self._pub_sub_manager.subscribe(self, self._name_topic)
        self._spindle_param_a7_det_topic = f'{self._node_id_SpindleDetails_det}.spindle_sel_param'
        self._pub_sub_manager.subscribe(self, self._spindle_param_a7_det_topic)
        self._spindle_param_a7_anal_topic = f'{self._node_id_SpindleDetails_anal}.spindle_sel_param'
        self._pub_sub_manager.subscribe(self, self._spindle_param_a7_anal_topic)

        self._spindle_a7_param = {}
        self._spindle_a7_param['spindle_name'] = 'a7'
        self._spindle_a7_param['thresh_abs_sigma_pow_uv2'] = 1.25
        self._spindle_a7_param['thresh_rel_sigma_pow_z'] = 1.6
        self._spindle_a7_param['thresh_sigma_cov_z'] = 1.3
        self._spindle_a7_param['thresh_sigma_cor_perc'] = 69
    

    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._thresholds_a7_topic, 'ping')
        self._pub_sub_manager.publish(self, self._group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._spindle_param_a7_det_topic, 'ping')


    def on_apply_settings(self):
        # Send the settings to the publisher
        self._pub_sub_manager.publish(self, self._group_topic, self.group_lineEdit.text())
        self._pub_sub_manager.publish(self, self._name_topic, self.name_lineEdit.text())

        # Init the _spindle_param_gen_topic and send the dict
        self._spindle_a7_param['spindle_name'] = self.name_lineEdit.text()
        self._spindle_a7_param['thresh_abs_sigma_pow_uv2'] = self.doubleSpinBox_absSigma.value()
        self._spindle_a7_param['thresh_rel_sigma_pow_z'] = self.doubleSpinBox_relSigma.value()
        self._spindle_a7_param['thresh_sigma_cov_z'] = self.doubleSpinBox_sigmaCov.value()
        self._spindle_a7_param['thresh_sigma_cor_perc'] = self.doubleSpinBox_sigmaCor.value()
        self._pub_sub_manager.publish(self, self._thresholds_a7_topic, self._spindle_a7_param)
        self._pub_sub_manager.publish(self, self._spindle_param_a7_det_topic, self._spindle_a7_param)
        self._pub_sub_manager.publish(self, self._spindle_param_a7_anal_topic, self._spindle_a7_param)
        

    def on_topic_response(self, topic, message, sender):
        if topic == self._name_topic:
            self.name_lineEdit.setText(message)      
        if topic == self._thresholds_a7_topic:
            if isinstance(message, str) and not message == '':
                message = eval(message)
            elif isinstance(message, dict):
                self._spindle_a7_param = message


    # Called when a value listened is changed
    # No body asked for the value (no ping), but the value changed and
    # some subscribed to the topic
    def on_topic_update(self, topic, message, sender):
        pass


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._group_topic)
            self._pub_sub_manager.unsubscribe(self, self._name_topic)
            self._pub_sub_manager.unsubscribe(self, self._spindle_param_a7_det_topic)
            self._pub_sub_manager.unsubscribe(self, self._spindle_param_a7_anal_topic)