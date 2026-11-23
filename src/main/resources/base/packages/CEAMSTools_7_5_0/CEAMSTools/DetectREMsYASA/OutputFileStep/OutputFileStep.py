#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    OutputFileStep
    TODO CLASS DESCRIPTION
"""

from qtpy import QtWidgets

from CEAMSTools.DetectREMsYASA.OutputFileStep.Ui_OutputFileStep import Ui_OutputFileStep
from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog
from CEAMSTools.DetectREMsYASA.DetectorStep.DetectorStep import DetectorStep

class OutputFileStep(BaseStepView, Ui_OutputFileStep, QtWidgets.QWidget):
    """
        OutputFileStep
        TODO CLASS DESCRIPTION
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        self.pushButton_CohortFilename.clicked.connect(self.browse_cohort_slot)

        # If necessary, init the context. The context is a memory space shared by 
        # all steps of a tool. It is used to share and notice other steps whenever
        # the value in it changes. It's very useful when the parameter within a step
        # must have an impact in another step.
        #self._context_manager["context_OutputFileStep"] = {"the_data_I_want_to_share":"some_data"}
        self._node_id_REMsDetails = "d1489e58-7c3d-490e-9c36-f830c8dc596e"
        self._cohort_file_topic = f'{self._node_id_REMsDetails}.cohort_filename'
        self._pub_sub_manager.subscribe(self, self._cohort_file_topic)

        self._node_id_REMsDetection = "5b36c10e-696e-40d2-be30-12548a806e0c"
        self._save_directory_topic = f'{self._node_id_REMsDetection}.save_directory'
        self._pub_sub_manager.subscribe(self, self._save_directory_topic)
        
    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.

        # You need to look into your process.json file to know the ID of the node
        # you are interest in, this is just an example value:
        #identifier = "ea6060df-a4da-4ec1-a75c-399ece7a3c1b" 
        #self._somevalue_topic = identifier + ".some_input" # Change some_input for the name of the input your are looking for.
        #self._pub_sub_manager.publish(self, self._somevalue_topic, 'ping')
        self._pub_sub_manager.publish(self, self._cohort_file_topic, 'ping')
        self._pub_sub_manager.publish(self, self._save_directory_topic, 'ping')

    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.
        super().on_topic_update(topic, message, sender)

        if topic==self._context_manager.topic:
            # PSA section selection changed
            if message==DetectorStep.context_REM_Report_selection: # key of the context dict
                bool_flag = True if self._context_manager[DetectorStep.context_REM_Report_selection]==1 else False
                self.enable_widgets(bool_flag)

    def on_topic_response(self, topic, message, sender):
        # This will be called as a response to ping request.
        #if topic == self._somevalue_topic:
        #    self._somevalue = message
        if topic == self._cohort_file_topic:
            self.lineEdit_CohortFilename.setText(message)
        if topic == self._save_directory_topic:
            self.lineEdit_CohortFilename.setText(message)

    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._cohort_file_topic, self.lineEdit_CohortFilename.text())
        self._pub_sub_manager.publish(self, self._save_directory_topic, self.lineEdit_CohortFilename.text())

    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if len(self.lineEdit_CohortFilename.text())==0 and self._context_manager[DetectorStep.context_REM_Report_selection]==1:
            WarningDialog("Define a file to write the detailed events report for the cohort. In step '4- Output File'")
            return False
        return True
    
    # Called when the user press the browse button to define where to save the cohort report
    def browse_cohort_slot(self):
        # define the option to disable the warning dialog when overwriting an existing file
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, 
            'Save as TSV file', 
            None, 
            'TSV (*.tsv)',
            options = QtWidgets.QFileDialog.DontConfirmOverwrite)
        if filename != '':
            self.lineEdit_CohortFilename.setText(filename)

    def enable_widgets(self, bool_flag):
        self.gridLayout.setEnabled(bool_flag)
        self.label_2.setEnabled(bool_flag)
        self.label_3.setEnabled(bool_flag)
        self.lineEdit_CohortFilename.setEnabled(bool_flag)
        self.pushButton_CohortFilename.setEnabled(bool_flag)