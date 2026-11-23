#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    MiniEpochDefinition
    TODO CLASS DESCRIPTION
"""

import ast

from qtpy import QtWidgets

from CEAMSTools.DetectREMsYASA.MiniEpochDefinition.Ui_MiniEpochDefinition import Ui_MiniEpochDefinition
from commons.BaseStepView import BaseStepView

class MiniEpochDefinition(BaseStepView, Ui_MiniEpochDefinition, QtWidgets.QWidget):
    """
        MiniEpochDefinition
        TODO CLASS DESCRIPTION
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        self.REMs_to_mini_epochcs_identifier = "a65d75b5-b177-4cad-a36f-c9aadb5eabf7"
        self.Event_subdivision_identifier = "aff5dd4e-069f-4c61-819f-779313525b54"

        self._parameters_topic = f'{self.REMs_to_mini_epochcs_identifier}.parameters'
        self._pub_sub_manager.subscribe(self, self._parameters_topic)
        self._window_sec_topic = f'{self.Event_subdivision_identifier}.window_sec'
        self._pub_sub_manager.subscribe(self, self._window_sec_topic)

        
    def load_settings(self):
        # Load the settings of the step and update the UI accordingly.
        # This is called when the step is loaded in the pipeline.
        self._pub_sub_manager.publish(self, self._parameters_topic, 'ping')
        self._pub_sub_manager.publish(self, self._window_sec_topic, 'ping')

    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.
        #if topic == self._context_manager.topic:

            # The message will be the KEY of the value that's been updated inside the context.
            # If it's the one you are looking for, we can then take the updated value and use it.
            #if message == "context_some_other_step":
                #updated_value = self._context_manager["context_some_other_step"]
        pass

    def on_topic_response(self, topic, message, sender):
        # This will be called as a response to ping request.
        if topic == self._parameters_topic:
            if isinstance(message, str) and message != '':
                message = ast.literal_eval(message)
            if isinstance(message, dict):
                self.lineEdit_group.setText(message['mini_epoch_group'])
                self.lineEdit_name_Phasic.setText(message['mini_epoch_name_Phasic'])
                self.lineEdit_name_Tonic.setText(message['mini_epoch_name_Tonic'])
        elif topic == self._window_sec_topic:
            self.comboBox_length.setCurrentText(str(message))

    def on_apply_settings(self):
        parameters = {
            'mini_epoch_group': self.lineEdit_group.text(),
            'mini_epoch_name_Phasic': self.lineEdit_name_Phasic.text(),
            'mini_epoch_name_Tonic': self.lineEdit_name_Tonic.text()
        }
        self._pub_sub_manager.publish(self, self._parameters_topic, str(parameters))
        self._pub_sub_manager.publish(self, self._window_sec_topic, int(self.comboBox_length.currentText()))

    def on_validate_settings(self):
        if self.lineEdit_group.text() == "":
            QtWidgets.QMessageBox.critical(self, "Error", "The group name cannot be empty.")
            return False
        if self.lineEdit_name_Phasic.text() == "":
            QtWidgets.QMessageBox.critical(self, "Error", "The phasic name cannot be empty.")
            return False
        if self.lineEdit_name_Tonic.text() == "":
            QtWidgets.QMessageBox.critical(self, "Error", "The tonic name cannot be empty.")
            return False
        if int(self.comboBox_length.currentText()) == 0:
            QtWidgets.QMessageBox.critical(self, "Error", "The length of the mini-epoch cannot be 0.")
            return False
        return True
