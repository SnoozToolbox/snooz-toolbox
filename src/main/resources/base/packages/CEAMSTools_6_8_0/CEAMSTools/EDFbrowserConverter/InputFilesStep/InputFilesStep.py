#! /usr/bin/env python3
"""
    InputFilesStep
    TODO CLASS DESCRIPTION
"""

from qtpy import QtWidgets, QtCore

from CEAMSTools.EDFbrowserConverter.Commons import ContextConstants
from CEAMSTools.EDFbrowserConverter.InputFilesStep.Ui_InputFilesStep import Ui_InputFilesStep
from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog

class InputFilesStep(BaseStepView, Ui_InputFilesStep, QtWidgets.QWidget):
    """
        InputFilesStep
        Allows the opening of the file
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules and nodes to talk to
        self._csv_reader_master_identifier = "663cd8ee-9ca5-4956-9a4f-82561c6adadf"

        # To use the SettingsView of a plugin and interract with its fonctions
        module = self.process_manager.get_node_by_id(self._csv_reader_master_identifier)
        if module is None:
            print(f'ERROR module_id isn\'t found in the process:{self._csv_reader_master_identifier}')
        else:
            # To extract the SettingsView and add it to our Layout in the preset
            self.my_CsvReaderSettingsView = module.create_settings_view()
            self.verticalLayout.addWidget(self.my_CsvReaderSettingsView)
            # _context_manager is inherited from the BaseStepView
            # it allows to share information between steps in the step-by-step interface
            # ContextManager is a dictionary that publish an update through the 
            # PubSubManager whenever a value is modified.
            self._context_manager[ContextConstants.context_files_event_names] = self.my_CsvReaderSettingsView
            self.my_CsvReaderSettingsView.model_updated_signal.connect(self.on_model_modified)


    # Slot created to receive the signal emitted from PSGReaderSettingsView when the files_model is modified
    @QtCore.Slot()
    def on_model_modified(self):
        self._context_manager[ContextConstants.context_files_event_names] = self.my_CsvReaderSettingsView     


    def load_settings(self):
        pass


    # Called when the user clic on RUN
    # Message are sent to the publisher   
    def on_apply_settings(self):
        pass


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if self.my_CsvReaderSettingsView.fileListWidget.count()==0:
            WarningDialog(f"Add a file to convert in the step '1-Input Files'")
            return False       
        return True      


    # Called when a value listened is changed
    # No body asked for the value (no ping), but the value changed and
    # some subscribed to the topic
    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        pass


    # Called when the user delete an instance of the plugin
    def __del__(self):
        pass

