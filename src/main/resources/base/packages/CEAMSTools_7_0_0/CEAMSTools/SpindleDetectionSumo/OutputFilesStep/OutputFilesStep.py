#! /usr/bin/env python3
"""
    OutputFilesStep
    Step to select the path and name of the spindle events details.
"""
from .Ui_OutputFilesStep import Ui_OutputFilesStep
from ..SpindleDetectorSelStep.SpindleDetectorSelStep import SpindleDetectorSelStep
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState
from widgets.WarningDialog import WarningDialog

from qtpy import QtWidgets

class OutputFilesStep(BaseStepView, Ui_OutputFilesStep, QtWidgets.QWidget):
    """
        OutputFilesStep
        Step to select the path and name of the spindle events details.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        # Define modules and nodes to talk to
        self._node_id_spindle_details_det = "0e3df2c0-7c41-4fa5-89bb-f6601ef8831a" # provide filename of spindle details when spindles are detected
        self._node_id_SpindleDetails_anal = "28929dd9-a992-4e7b-be6b-9e0a6053ae4e" # provide the spindle_parameters when spindles are analyzed only

        # Subscribe to context manager for each node you want to talk to
        self._cohort_file_det_topic = f'{self._node_id_spindle_details_det}.cohort_filename'
        self._cohort_file_anal_topic = f'{self._node_id_SpindleDetails_anal}.cohort_filename'
        self._export_spindles_det_topic = f'{self._node_id_spindle_details_det}.export_spindles'
        self._export_spindles_anal_topic = f'{self._node_id_SpindleDetails_anal}.export_spindles'
        
        self.generate_details = [1, 0]
        

    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        self._pub_sub_manager.publish(self, self._cohort_file_det_topic, 'ping')
        self._pub_sub_manager.publish(self, self._export_spindles_det_topic, 'ping')
        self._pub_sub_manager.publish(self, self._node_id_spindle_details_det+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_SpindleDetails_anal+".get_activation_state", None)


    def on_topic_response(self, topic, message, sender):
        # The response to a ping
        if topic == self._cohort_file_det_topic:
            self.cohort_lineedit.setText(message)
            if message=='':
                self.checkBox_cohort_file.setChecked(False)
            else:
                self.checkBox_cohort_file.setChecked(True)
            self.enable_cohort_slot()
        if topic == self._export_spindles_det_topic:
            self.checkBox_spindle_file.setChecked(eval(message))       
            self.enable_spindle_slot()
        if topic == self._node_id_spindle_details_det+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.generate_details[0] = 1
            else:
                self.generate_details[0] = 0
        if topic == self._node_id_SpindleDetails_anal+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.generate_details[1] = 1
            else:
                self.generate_details[1] = 0


    # Called when a value listened is changed
    # No body asked for the value (no ping), but the value changed and
    # some subscribed to the topic
    def on_topic_update(self, topic, message, sender):
        if topic==self._context_manager.topic:
            # If the context_per_cycle is checked from MartinSettings 
            #   -> check the computation of the thresh per cycle (the opposite is not true)            
            if message==SpindleDetectorSelStep.context_spindle_det: # key of the context dict
                # Need to select only in cycle to compute threshold per cycle (the opposite is not true)
                if self._context_manager[SpindleDetectorSelStep.context_spindle_det]==True: 
                    self.generate_details = [1, 0] # the SpindleDetails for detection must be activated
                else:
                    self.generate_details = [0, 1] # the SpindleDetails for analysing must be activated


    def on_apply_settings(self):
        
        # If no file is generated, neither the spindle one nor the cohort one.
        if (not self.checkBox_cohort_file.isChecked()) and (not self.checkBox_spindle_file.isChecked()):
            self.generate_details = [0, 0]

        if self.generate_details[0]==1:
            self._pub_sub_manager.publish(self, self._node_id_spindle_details_det+\
                ".activation_state_change", ActivationState.ACTIVATED)
        else:
            self._pub_sub_manager.publish(self, self._node_id_spindle_details_det+\
                ".activation_state_change", ActivationState.DEACTIVATED)
        if self.generate_details[1]==1:
            self._pub_sub_manager.publish(self, self._node_id_SpindleDetails_anal+\
                ".activation_state_change", ActivationState.ACTIVATED)
        else:
            self._pub_sub_manager.publish(self, self._node_id_SpindleDetails_anal+\
                ".activation_state_change", ActivationState.DEACTIVATED)
        self._pub_sub_manager.publish(self, self._cohort_file_det_topic, self.cohort_lineedit.text())
        self._pub_sub_manager.publish(self, self._cohort_file_anal_topic, self.cohort_lineedit.text())
        self._pub_sub_manager.publish(self, self._export_spindles_det_topic, str(self.checkBox_spindle_file.isChecked()))
        self._pub_sub_manager.publish(self, self._export_spindles_anal_topic, str(self.checkBox_spindle_file.isChecked()))
        

    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if self.checkBox_cohort_file.isChecked():
            if len(self.cohort_lineedit.text())==0:
                WarningDialog(f"The output file for the cohort has to be defined by the user, see step '4-Output Files'.")
                return False
        elif (self._context_manager[SpindleDetectorSelStep.context_spindle_det]==False and self.checkBox_spindle_file.isChecked()==False):
            WarningDialog(f"Nothing to process, no spindle detection in step '3-Detection Settings' and not file to generate in step '4-Output Files'.")
            return False
        return True   


    # Called when the user click on the browse push button
    def browse_cohort_slot(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, 
            'Save as TSV file', 
            None, 
            'TSV (*.tsv)',\
            options = QtWidgets.QFileDialog.DontConfirmOverwrite)
        if filename != '':
            if not ".tsv" in filename:
                filename = filename + ".tsv"
            self.cohort_lineedit.setText(filename)


    # Called when the user checks/unchecks the checkbox to save the cohort file
    def enable_cohort_slot(self):
        self.cohort_lineedit.setEnabled(self.checkBox_cohort_file.isChecked())
        self.pushButton_cohort.setEnabled(self.checkBox_cohort_file.isChecked())
        if self.checkBox_cohort_file.isChecked():
            # To know which SpindlesDetails to activate
            if self._context_manager[SpindleDetectorSelStep.context_spindle_det]==True:
                self.generate_details = [1, 0] # the SpindleDetails for detection must be activated
            else:
                self.generate_details = [0, 1] # the SpindleDetails for analyzing must be activated
        else:
            self.cohort_lineedit.setText('')


    # Called when the user checks/unchecks the checkbox to save the spindle characteristics file
    def enable_spindle_slot(self):
        if self.checkBox_cohort_file.isChecked():
            # TODO export_spindles
            # To know which SpindlesDetails to activate
            if self._context_manager[SpindleDetectorSelStep.context_spindle_det]==True:
                self.generate_details = [1, 0] # the SpindleDetails for detection must be activated
            else:
                self.generate_details = [0, 1] # the SpindleDetails for analyzing must be activated
