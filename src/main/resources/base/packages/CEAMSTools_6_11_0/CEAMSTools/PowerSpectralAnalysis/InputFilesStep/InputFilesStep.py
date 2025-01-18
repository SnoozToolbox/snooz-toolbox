#! /usr/bin/env python3
"""
    InputFiles
    Step to open files to detect spindles.
"""

from qtpy import QtWidgets, QtCore
from qtpy.QtCore import QTimer

from CEAMSTools.PowerSpectralAnalysis.InputFilesStep.Ui_InputFilesStep import Ui_InputFilesStep
from commons.BaseStepView import BaseStepView

from widgets.WarningDialog import WarningDialog

class InputFilesStep( BaseStepView,  Ui_InputFilesStep, QtWidgets.QWidget):
    

    context_files_view      = "input_files_settings_view"
    psg_reader_identifier   = "377e68c9-e26d-4b06-972e-d88e12ecb208"
    valid_stage_mandatory   = False # The PSA can be performed on unscored data
    valid_selected_chan     = True # The PSA cannot be performed without selected channels
    valid_single_chan       = False # The PSA can be performed on many channels

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

        self._emit_timer = QTimer()
        self._emit_timer.setSingleShot(True)
        self._emit_timer.timeout.connect(self._emit_timeout_reached)


    # Slot created to receive the signal emitted from PSGReaderSettingsView when the files_model is modified
    @QtCore.Slot()
    def on_model_modified(self):
        # Add a timer delay to accumulate all the channel selection change before update the context
        self._emit_timer.start(3)


    # Called when the timout is reached
    @QtCore.Slot()
    def _emit_timeout_reached(self):
        self._context_manager[self.context_files_view] = self.my_PsgReaderSettingsView


    # To ping specific nodes to call on_topic_response
    def load_settings(self):
        pass


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
       
        if ((self.valid_selected_chan or self.valid_stage_mandatory) or self.valid_single_chan ):
            file_list = self.my_PsgReaderSettingsView.get_files_list(self.my_PsgReaderSettingsView.files_model)

        # If the file list is empty -> open a warning dialog
        # If none of the channels is selected for a subject -> open a warning dialog
        if self.valid_selected_chan : 
            channels_info_df = self.my_PsgReaderSettingsView.channels_table_model.get_data()
            # For each subject
            if len(file_list)>0:
                for file in file_list:
                    chans_used = channels_info_df[(channels_info_df['Filename']==file) & (channels_info_df['Use']==True)]
                    if len(chans_used)==0:
                        WarningDialog(f"At least one recording has no channel selected, start looking at {file} in step '1 - Input Files'.")
                        return False
            else:
                WarningDialog(f"Add files in step '1 - Input Files'.")    
                return False

        # If the tool needs that all recordings have valid sleep stages
        # This class is also used in the spindle and SW detection tool
        if self.valid_stage_mandatory :
            # Return False if any of the recordings has no valid sleep staging
            for file in file_list:
                if not self.my_PsgReaderSettingsView.is_stages_scored(file, self.my_PsgReaderSettingsView.files_model):
                    WarningDialog(f"At least one recording has no valid sleep stage, start looking at {file} in the step '1- Input Files'.")
                    return False

        # If the tool needs that all recordings have only one channel
        # This class is also used in the Oxygen Saturation Report tool
        if self.valid_single_chan :
            # Return False if any of the recordings has more than one channel selected
            for file in file_list:
                chans_used = channels_info_df[(channels_info_df['Filename'] == file) & (channels_info_df['Use'] == True)]
                if len(chans_used) > 1:
                    WarningDialog(f"At least one recording has more than one channel selected, start looking at {file} in step '1 - Input Files'.")
                    return False
        return True   


    # Called when the user clic on RUN
    # Message are sent to the publisher   
    def on_apply_settings(self):
        pass


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