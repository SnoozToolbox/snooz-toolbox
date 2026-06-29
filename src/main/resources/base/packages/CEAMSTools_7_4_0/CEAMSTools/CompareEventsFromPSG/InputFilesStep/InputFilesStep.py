#! /usr/bin/env python3
"""
    InputFiles
    Step to open files to detect spindles.
"""

from qtpy import QtWidgets, QtCore

from CEAMSTools.CompareEventsFromPSG.InputFilesStep.Ui_InputFilesStep import Ui_InputFilesStep
from commons.BaseStepView import BaseStepView


class InputFilesStep( BaseStepView,  Ui_InputFilesStep, QtWidgets.QWidget):
    
    # Key for the context shared with other step of the preset
    context_files_view = "input_files_settings_view"
    psg_reader_identifier = "9011a426-1d8c-4ab4-abdf-d98a927cf533"

    """
        InputFilesStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform PSGReader of the files to open and propagate the events included in the files.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        # Define modules and nodes to talk to
        self._psg_reader_identifier = self.psg_reader_identifier

        # To use the SettingsView of a plugin and interract with its fonctions
        module = self.process_manager.get_node_by_id(self._psg_reader_identifier)
        if module is None:
            print(f'ERROR module_id isn\'t found in the process:{self._psg_reader_identifier}')
        else:
            # To extract the SettingsView and add it to our Layout in the preset
            self.my_PsgReaderSettingsView = module.create_settings_view()
            self.verticalLayout.addWidget(self.my_PsgReaderSettingsView)
            # _context_manager is inherited from the BaseStepView
            # it allows to share information between steps in the step-by-step interface
            # ContextManager is a dictionary that publish an update through the 
            # PubSubManager whenever a value is modified.
            self._context_manager[self.context_files_view] = self.my_PsgReaderSettingsView
            self.my_PsgReaderSettingsView.model_updated_signal.connect(self.on_model_modified)


    # Slot created to receive the signal emitted from PSGReaderSettingsView when the files_model is modified
    @QtCore.Slot()
    def on_model_modified(self):
        self._context_manager[self.context_files_view] = self.my_PsgReaderSettingsView


    # To ping specific nodes
    def load_settings(self):
        pass


    # Called when the user clic on RUN
    # Message are sent to the publisher   
    def on_apply_settings(self):
        pass


    # Called when a value listened is changed
    # No body asked for the value (no ping), but the value changed and
    # some subscribed to the topic
    def on_topic_update(self, topic, message, sender):
        pass


    # Response to a ping
    def on_topic_response(self, topic, message, sender):
        pass


    # Called when the user delete an instance of the plugin
    def __del__(self):
        pass

