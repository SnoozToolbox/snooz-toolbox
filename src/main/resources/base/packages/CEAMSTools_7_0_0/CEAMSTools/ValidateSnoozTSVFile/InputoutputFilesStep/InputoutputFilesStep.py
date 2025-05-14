#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    InputoutputFilesStep
    InputoutputFilesStep is the second step of the ValidateSnoozTSVFile tool.
    It allows the user to select input files and an output directory for the validation reports.
"""

from qtpy import QtWidgets, QtCore, QtGui
from PySide6.QtCore import *

from CEAMSTools.ValidateSnoozTSVFile.InputoutputFilesStep.Ui_InputoutputFilesStep import Ui_InputoutputFilesStep
from commons.BaseStepView import BaseStepView

from widgets.WarningDialogWithButtons import WarningDialogWithButtons
from widgets.WarningDialog import WarningDialog

class InputoutputFilesStep(BaseStepView, Ui_InputoutputFilesStep, QtWidgets.QWidget):
    """
    InputoutputFilesStep
    InputoutputFilesStep is the second step of the ValidateSnoozTSVFile tool.
    It allows the user to select input files and an output directory for the validation reports.
    """
    model_updated_signal = QtCore.Signal()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_add)
        self.pushButton_2.clicked.connect(self.listWidget.clear)
        self.pushButton_2.clicked.connect(self.clear_list_slot)

        self.lineEdit.setPlaceholderText(QCoreApplication.translate("OutputFiles", u"Select a folder where the validation reports are supposed to be saved", None))
        # Connect the browse push button to the on_choose function
        self.pushButton_3.clicked.connect(self.on_choose)
        # Subscribe to the proper topics to send/get data from the node
        node_id_writer = "b54b5cc7-3364-475c-9500-366c601dc935"
        self._files_topic = f'{node_id_writer}.files'
        self._pub_sub_manager.subscribe(self, self._files_topic)

        self._log_path_topic = f'{node_id_writer}.log_path'
        self._pub_sub_manager.subscribe(self, self._log_path_topic)

        self.files_model = QtGui.QStandardItemModel(0,1)


    # Called when the user clicks on the browse push button
    def on_choose(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            None, 
            'Select Directory', 
            '', 
            QtWidgets.QFileDialog.ShowDirsOnly | QtWidgets.QFileDialog.DontResolveSymlinks)
        if directory:
            if not directory.endswith('/') and not directory.endswith('\\'):
                directory += '/'
            self.lineEdit.setText(directory)


    def load_files_from_data(self, data):
        self.listWidget.clear()
        self.files_model = QtGui.QStandardItemModel(0,1) 
        for filename in data:
            # Add files to listView
            self.listWidget.addItem(filename)
            # tree item : parent=file, child=name
            item = QtGui.QStandardItem(filename)
            self.files_model.appendRow(item) 
        # Generate a signal to inform that self.files_model has been updated
        self.model_updated_signal.emit()

    def clear_list_slot(self):
        self.listWidget.clear()
        # Clear the model
        # Important to remove the last row first since the model is updated after each removeRow
        # we dont want to change file index.
        for row in range(self.files_model.rowCount()-1,-1,-1):
            self.files_model.removeRow(row)
        # Generate a signal to inform that self.files_model has been updated
        self.model_updated_signal.emit()

    # Slot called when user wants to add files
    def on_add(self):
        filenames_add, _ = QtWidgets.QFileDialog.getOpenFileNames(
            None, 
            'Open CSV, TSV or TXT file', 
            None, 
            'CSV TSV (*.csv *.tsv *.txt)')
        if filenames_add != '':
            # Fill the QListWidget
            for filename in filenames_add:
                self.listWidget.addItem(filename)
                # tree item : parent=file, child=name
                item = QtGui.QStandardItem(filename)
                self.files_model.appendRow(item) 
            # Generate a signal to inform that self.files_model has been updated
            self.model_updated_signal.emit()

    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._files_topic, 'ping')
        self._pub_sub_manager.publish(self, self._log_path_topic, 'ping')
        


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to TSVValidatorMaster
        items = []
        for x in range(self.listWidget.count()):
            items.append(self.listWidget.item(x).text())
        self._pub_sub_manager.publish(self, self._files_topic, items)
        self._pub_sub_manager.publish(self, self._log_path_topic, self.lineEdit.text())
        #self._pub_sub_manager.publish(self, self._files_topic, str(self.listWidget.currentItem().text()))


    def on_topic_update(self, topic, message, sender):
        """ Only used in a custom step of a tool, you can ignore it.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._files_topic:
            self.load_files_from_data(message)
        elif topic == self._log_path_topic:
            self.lineEdit.setText(message)

            #self.load_files_from_data(message)
            #self.listWidget.addItem(message)
            #self.files_model.appendRow(message) 
            # Generate a signal to inform that self.files_model has been updated
            #self.model_updated_signal.emit()
        


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._files_topic)
            self._pub_sub_manager.unsubscribe(self, self._log_path_topic)
            


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if len(self.lineEdit.text())==0:
            WarningDialog(f"You need to define the output destination in step '2 - Input/output Files.")
            return False

        if self.listWidget.count() == 0:
            WarningDialog(f"You need to define at least one input file in step '2 - Input/output Files.")
            return False
        
        return True
