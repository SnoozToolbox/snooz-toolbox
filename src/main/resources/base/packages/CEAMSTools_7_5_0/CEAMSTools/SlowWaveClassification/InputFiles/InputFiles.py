#! /usr/bin/env python3
"""
    InputFiles
    TODO CLASS DESCRIPTION
"""

from qtpy import QtWidgets

from CEAMSTools.SlowWaveClassification.InputFiles.Ui_InputFiles import Ui_InputFiles
from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog

class InputFiles(BaseStepView, Ui_InputFiles, QtWidgets.QWidget):
    """
        InputFiles
        TODO CLASS DESCRIPTION
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        self.tableWidget_char_files.setColumnCount(1)
        self.tableWidget_char_files.setHorizontalHeaderLabels(['Filenames'])
        self.tableWidget_char_files.horizontalHeader().setStretchLastSection(True)
        self._files = []
        self.tableWidget_stage_files.setColumnCount(1)
        self.tableWidget_stage_files.setHorizontalHeaderLabels(['Filenames'])
        self.tableWidget_stage_files.horizontalHeader().setStretchLastSection(True)
        self._stages_files = []
        
        # You need to look into your process.json file to know the ID of the node
        # you are interest in, this is just an example value:
        identifier = "d59d94d1-11dc-4e06-9716-f749a3647843" 
        self._files_topic = identifier + ".sw_char_files" # Change some_input for the name of the input your are looking for.
        self._cohort_topic = identifier + ".sw_cohort_file" # Change some_input for the name of the input your are looking for.
        self._stages_topic = identifier + ".sw_stages_files" # Change some_input for the name of the input your are looking for.
        

    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        self._pub_sub_manager.publish(self, self._files_topic, 'ping')
        self._pub_sub_manager.publish(self, self._cohort_topic, 'ping')
        self._pub_sub_manager.publish(self, self._stages_topic, 'ping')

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

        if topic == self._files_topic:
            if not message == '':
                self._files = eval(message)
            else:
                self._files = []
            self.tableWidget_char_files.setRowCount(len(self._files))
            for row, filename in enumerate(self._files):
                self.tableWidget_char_files.setItem(row, 0, QtWidgets.QTableWidgetItem(filename))

        if topic == self._stages_topic:
            if not message == '':
                self._stages_files = eval(message)
            else:
                self._stages_files = []
            self.tableWidget_stage_files.setRowCount(len(self._stages_files))
            for row, filename in enumerate(self._stages_files):
                self.tableWidget_stage_files.setItem(row, 0, QtWidgets.QTableWidgetItem(filename))

        if topic == self._cohort_topic:
            self.lineEdit_cohort_file.setText(message)


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" 
        """
        # Send the settings to the publisher for inputs to EdfXmlReaderMaster
        self._pub_sub_manager.publish(self, self._files_topic, str(self._files))
        self._pub_sub_manager.publish(self, self._stages_topic, str(self._stages_files))
        self._pub_sub_manager.publish(self, self._cohort_topic, str(self.lineEdit_cohort_file.text()))


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if len(self._files)==0:
            WarningDialog(f"Add a slow wave characteristics file in the step '1-Input Files'")
            return False   
        if len(self._stages_files)==0:
            WarningDialog(f"Add a sleep stages file in the step '1-Input Files'")
            return False                   
        if len(self.lineEdit_cohort_file.text())==0:
            WarningDialog(f"Add a cohort file in the step '1-Input Files'")
            return False
        return True    


    def choose_slot(self):
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(
            None, 
            'Open .tsv files', 
            None, 
            '.tsv files (*.tsv *.TSV)')
        self._files = files
        if files != '':
            self.tableWidget_char_files.setRowCount(len(self._files))
            for row, filename in enumerate(files):
                self.tableWidget_char_files.setItem(row, 0, QtWidgets.QTableWidgetItem(filename))
            

    def clear_slot(self):
        self.tableWidget_char_files.clearContents()
        self._files = []


    def choose_cohort_slot(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, 
            'Open .tsv file', 
            None, 
            '.tsv (*.tsv, *.TSV)')
        if filename != '':
            self.lineEdit_cohort_file.setText(filename)

    
    # the slot to clear the stages file list
    def clear_stage_slot(self):
        self.tableWidget_stage_files.clearContents()
        self._stages_files = []


    def choose_stage_slot(self):
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(
            None, 
            'Open .tsv files', 
            None, 
            '.tsv files (*.tsv *.TSV)')
        self._stages_files = files
        if files != '':
            self.tableWidget_stage_files.setRowCount(len(self._stages_files))
            for row, filename in enumerate(files):
                self.tableWidget_stage_files.setItem(row, 0, QtWidgets.QTableWidgetItem(filename))
