#! /usr/bin/env python3
"""
    OutputFileStep
    Step to define the activity to export (Total, per hour or per sleep cycle),  
    the output file format and the directory to save the PSA cohort review file.
    The output format can be as the input or transposed to have 1 subject per row.
"""
from CEAMSTools.PSACohortReview.InputFiles.InputFiles import InputFiles
from CEAMSTools.PSACohortReview.OutputFileStep.Ui_OutputFileStep import Ui_OutputFileStep
from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog

import pandas as pd
from qtpy import QtWidgets

class OutputFileStep(BaseStepView, Ui_OutputFileStep, QtWidgets.QWidget):
    """
        OutputFileStep
        Step to define the activity to export (Total, per hour or per sleep cycle),  
        the output file format and the directory to save the PSA cohort review file.
        The output format can be as the input or transposed to have 1 subject per row.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        # Define modules and nodes to talk to
        self._PSA_review_identifier = "8df6ac98-9c6c-4f97-a579-5464ba4b6fe1"
        self._label_topic = f'{self._PSA_review_identifier}.activity_label'
        self._pub_sub_manager.subscribe(self, self._label_topic)               
        self._clean_topic = f'{self._PSA_review_identifier}.PSA_clean_flag'
        self._pub_sub_manager.subscribe(self, self._clean_topic)          
        self._transposed_topic = f'{self._PSA_review_identifier}.PSA_transposed_flag'
        self._pub_sub_manager.subscribe(self, self._transposed_topic)   
        self._output_topic = f'{self._PSA_review_identifier}.output_dir'
        self._pub_sub_manager.subscribe(self, self._output_topic)   

        # Populate the comboBox (add choices)
        self.activity_label = ['Total', 'Distribution per hour', 'Distribution per sleep cycle', 'Distribution per annotation']
        for label in self.activity_label:
            self.activity_comboBox.addItem(label)
        self.activity_comboBox.setCurrentText(self.activity_label[0])

        self.filenames = [] # will be defined with context manager from the step InputFiles.
        self.PSA_df = pd.DataFrame() # Will be updated when the context information is modified
        

    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        self._pub_sub_manager.publish(self, self._label_topic, 'ping')
        self._pub_sub_manager.publish(self, self._clean_topic, 'ping')
        self._pub_sub_manager.publish(self, self._transposed_topic, 'ping')
        self._pub_sub_manager.publish(self, self._output_topic, 'ping')


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._label_topic:
            self.activity_comboBox.setCurrentText(message)
        if topic == self._clean_topic:
            self.export_raw_checkBox.setChecked(int(message))
        if topic == self._transposed_topic:
            self.export_transpose_checkBox.setChecked(int(message))
            self.export_transposed_checkbox_slot()
        if topic == self._output_topic:
            self.filename_lineEdit.setText(message)


    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.
        if topic == self._context_manager.topic:
            # The message will be the KEY of the value that's been updated inside the context.
            # If it's the one you are looking for, we can then take the updated value and use it.
            if message == InputFiles.context_InputFiles:
                self.filenames = self._context_manager[InputFiles.context_InputFiles]
                self.PSA_df = pd.DataFrame() # Will be updated when the context information is modified
                self.read_header_filename(self.filenames)
                # Update the possibility on the comboBox
                self.activity_comboBox.clear()
                # Look for PSA on sleep stage
                activity_2_export = "total_"
                if any(self.PSA_df.columns.str.contains(activity_2_export,regex=True)):
                    self.activity_comboBox.addItem(self.activity_label[0])
                    activity_2_export = "hour\d_"
                    if any(self.PSA_df.columns.str.contains(activity_2_export,regex=True)):
                        self.activity_comboBox.addItem(self.activity_label[1])
                    activity_2_export = "cyc\d_"
                    if any(self.PSA_df.columns.str.contains(activity_2_export,regex=True)):
                        self.activity_comboBox.addItem(self.activity_label[2])
                # Look for a PSAOnEvents
                else:
                    activity_2_export = "act_"
                    if any(self.PSA_df.columns.str.contains(activity_2_export,regex=True)):
                        self.activity_comboBox.addItem(self.activity_label[3])           


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.

        # Make sure at least one expert is checked
        if not self.export_raw_checkBox.isChecked() and not self.export_transpose_checkBox.isChecked():
            WarningDialog(f"Select at least one export in the step '3-Output File'")
            return False            
        # Make sure the output file is chosen
        if len(self.filename_lineEdit.text())==0:
            WarningDialog(f"Choose to filename to save the exported files in the step '3-Output File'")
            return False
        return True


    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        # Send the settings to the publisher for inputs to PSACohortReview
        self._pub_sub_manager.publish(self, self._label_topic, self.activity_comboBox.currentText())
        self._pub_sub_manager.publish(self, self._clean_topic, str(int(self.export_raw_checkBox.isChecked())))
        self._pub_sub_manager.publish(self, self._transposed_topic, str(int(self.export_transpose_checkBox.isChecked())))
        if len(self.filename_lineEdit.text())==0: # TODO : this will eventually be obsolete (when error message for the users will be upgrated)
            WarningDialog(f'The filename to save the exported files is not defined.  Edit the filename at the "Output File" step.')
        else: 
            self._pub_sub_manager.publish(self, self._output_topic, self.filename_lineEdit.text())


    def choose_button_slot(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, 
            'Save TSV file', 
            None, 
            'TSV (*.tsv)',\
             options = QtWidgets.QFileDialog.DontConfirmOverwrite)
        if filename != '':
            self.filename_lineEdit.setText(filename)


    # Called when the user checked/unchecked the "export transposed PSA file"
    def export_transposed_checkbox_slot(self):
        self.activity_comboBox.setEnabled(self.export_transpose_checkBox.isChecked())


    # Read the list of filenames and init self.PSA_df
    def read_header_filename(self, filenames):
        for filename in filenames:
            # Read the csv file and convert the content into a Data Frame
            PSA_df = pd.read_csv(filename, delimiter='\t', header=0, encoding='utf-8', nrows=1)
            self.PSA_df = pd.concat([self.PSA_df, PSA_df])