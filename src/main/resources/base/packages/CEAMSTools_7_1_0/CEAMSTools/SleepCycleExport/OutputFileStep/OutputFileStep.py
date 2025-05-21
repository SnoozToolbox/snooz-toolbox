"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    SleepCycleDoc
    TODO CLASS DESCRIPTION
"""
from CEAMSTools.SleepCycleExport.OutputFileStep.Ui_OutputFileStep import Ui_OutputFileStep
from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog

import os
from qtpy import QtWidgets


class OutputFileStep( BaseStepView,  Ui_OutputFileStep, QtWidgets.QWidget):
    """
        OutputFileStep
        Class to define the filenames of the cycles definition and the hypnogram .png picture.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules, state and nodes to talk to
        self._node_id_StringManip = "a980fb33-ba82-404c-8bfb-81c492652a71"
        self._suffix_hyp_topic = f'{self._node_id_StringManip}.suffix'
        self._pub_sub_manager.subscribe(self, self._suffix_hyp_topic)

        #self._node_id_TSVWriter = "02f542c6-5adf-4b31-9bc7-0761d3d1889d"
        self._node_id_Constante = "d4525793-91f1-4cf8-a659-f05b698a7f31"
        self._filename_topic = f'{self._node_id_Constante}.constant'
        self._pub_sub_manager.subscribe(self, self._filename_topic)


    def choose_slot1(self):
        # Slot called when user wants to add files
        filenames_add, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, 
            'Save TSV or TXT file', 
            None, 
            'TSV TXT(*.tsv *.txt)',\
            options = QtWidgets.QFileDialog.DontConfirmOverwrite)
        filename, file_extension = os.path.splitext(filenames_add)
        if len(file_extension)==0:
            filenames_add = filenames_add + ".tsv"
        self.tsv_file_lineEdit.setText(filenames_add)


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._suffix_hyp_topic, 'ping')
        self._pub_sub_manager.publish(self, self._filename_topic, 'ping')


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if len(self.tsv_file_lineEdit.text())==0:
            WarningDialog("Define the file to save the sleep cycles for the cohort in step '3-Output Files'")
            return False
        # if len(self.Hyp_suffix_lineEdit.text())==0:
        #     WarningDialog("Define the suffix to add to the file saved along the recording in step '3-Output Files'")
        #     return False            
        return True


    # Called when the user clicks on "Apply"
    # Settings defined in the viewer are sent to the pub_sub_manager
    def on_apply_settings(self):
        # If there is no ext -> add .pdf
        # if not ("." in str(self.Hyp_suffix_lineEdit.text())):
        #     self._pub_sub_manager.publish(self, self._suffix_hyp_topic, \
        #         str(self.Hyp_suffix_lineEdit.text())+".pdf")
        # else:
        self._pub_sub_manager.publish(self, self._suffix_hyp_topic, \
            str(self.Hyp_suffix_lineEdit.text()))       

        self._pub_sub_manager.publish(self, self._filename_topic, \
            str(self.tsv_file_lineEdit.text()))


    # To init 
    # Called by a node in response to a ping request. 
    # Ping request are sent whenever we need to know the value of a parameter of a node.
    def on_topic_response(self, topic, message, sender):
        if topic == self._suffix_hyp_topic:
            self.Hyp_suffix_lineEdit.setText(message)   
        if topic == self._filename_topic:
            self.tsv_file_lineEdit.setText(message)     


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._suffix_hyp_topic)
            self._pub_sub_manager.unsubscribe(self, self._filename_topic)