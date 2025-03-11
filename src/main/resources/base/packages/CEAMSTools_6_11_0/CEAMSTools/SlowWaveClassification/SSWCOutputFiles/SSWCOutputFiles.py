#! /usr/bin/env python3

"""
    Settings viewer of the step Output Files of the tool SlowWaveClassification
"""
from CEAMSTools.SlowWaveClassification.SSWCOutputFiles.Ui_SSWCOutputFiles import Ui_SSWCOutputFiles
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState
from widgets.WarningDialog import WarningDialog

from qtpy import QtWidgets

class SSWCOutputFiles( BaseStepView,  Ui_SSWCOutputFiles, QtWidgets.QWidget):
    """
        SSWCOutputFiles
        File links the Settings Views of the plugin to the plugin itself.

    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules and nodes to talk to
        self._node_id_SW_class = "d59d94d1-11dc-4e06-9716-f749a3647843" 

        # Subscribe to the proper topics to send/get data from the node
        self._foldername_topic = f'{self._node_id_SW_class}.output_dir'
        self._pub_sub_manager.subscribe(self, self._foldername_topic)
        self._n_division_topic = f'{self._node_id_SW_class}.num_divisions'
        self._pub_sub_manager.subscribe(self, self._n_division_topic)


    # Called when user push "Choose" button
    def on_choose(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        folder_name = file_dialog.getExistingDirectory()
        if folder_name != '':
            if folder_name[-1] != '/':
                folder_name = folder_name + '/'
            self.foldername_lineEdit.setText(folder_name)


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._foldername_topic, 'ping')
        self._pub_sub_manager.publish(self, self._n_division_topic, 'ping')
        

    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._foldername_topic, \
            str(self.foldername_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._n_division_topic, \
            str(self.spinBox_n_division.value()))


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.

        # Return False if the output file is not defined
        if len(self.foldername_lineEdit.text())==0:
            WarningDialog(f"The output folder is not defined in step '3-Output Files.")
            return False     
        return True


    # Called by the publisher to display settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._foldername_topic:
            self.foldername_lineEdit.setText(message)
        if topic == self._n_division_topic:
            self.spinBox_n_division.setValue(int(message))


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._foldername_topic)
            self._pub_sub_manager.unsubscribe(self, self._n_division_topic)
            