#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    EditPathsInSnoozWorkspaceSettingStep
    Setup the EditPathsInSnoozWorkspacePathEditorSettingsView in the step.
"""

from qtpy import QtWidgets, QtCore, QtGui
from PySide6.QtCore import *

from CEAMSTools.EditPathsInSnoozWorkspace.EditPathsInSnoozWorkspaceSettingStep.Ui_EditPathsInSnoozWorkspaceSettingStep import Ui_EditPathsInSnoozWorkspaceSettingStep
from commons.BaseStepView import BaseStepView

from widgets.WarningDialogWithButtons import WarningDialogWithButtons
from widgets.WarningDialog import WarningDialog
import json

class EditPathsInSnoozWorkspaceSettingStep(BaseStepView, Ui_EditPathsInSnoozWorkspaceSettingStep, QtWidgets.QWidget):
    
    
    context_files_view      = "input_files_settings_view"
    SnoozWorkspace_Path_Editor_identifier   = "a6e7fca0-3df9-4385-9730-d12fa5327523"
    """
        EditPathsInSnoozWorkspaceSettingStep
        Setup the EditPathsInSnoozWorkspaceSettingsView in the step.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules and nodes to talk to
        self._SnoozWorkspace_Path_Editor_identifier = self.SnoozWorkspace_Path_Editor_identifier

        # To use the SettingsView of a plugin and interract with its fonctions
        module = self.process_manager.get_node_by_id(self._SnoozWorkspace_Path_Editor_identifier)
        if module is None:
            print(f'ERROR module_id isn\'t found in the process:{self._SnoozWorkspace_Path_Editor_identifier}')
        else:
            # To extract the SettingsView and add it to our Layout in the preset
            self.my_SnoozWorkspacePathEditorSettingsView = module.create_settings_view()
            self.verticalLayout.addWidget(self.my_SnoozWorkspacePathEditorSettingsView)
            # _context_manager is inherited from the BaseStepView
            # it allows to share information between steps in the step-by-step interface
            # ContextManager is a dictionary that publish an update through the 
            # PubSubManager whenever a value is modified.
            self._context_manager[self.context_files_view] = self.my_SnoozWorkspacePathEditorSettingsView
            self.my_SnoozWorkspacePathEditorSettingsView.model_updated_signal.connect(self.on_model_modified)

        self._emit_timer = QTimer()
        self._emit_timer.setSingleShot(True)
        self._emit_timer.timeout.connect(self._emit_timeout_reached)


    # Slot created to receive the signal emitted from SnoozWorkspacePathEditorSettingsView when the files_model is modified
    @QtCore.Slot()
    def on_model_modified(self):
        # Add a timer delay to accumulate all the channel selection change before update the context
        self._emit_timer.start(3)


    # Called when the timout is reached
    @QtCore.Slot()
    def _emit_timeout_reached(self):
        self._context_manager[self.context_files_view] = self.my_SnoozWorkspacePathEditorSettingsView

        # If necessary, init the context. The context is a memory space shared by 
        # all steps of a tool. It is used to share and notice other steps whenever
        # the value in it changes. It's very useful when the parameter within a step
        # must have an impact in another step.
        #self._context_manager["context_SnoozWorkspaceDescriptionStep"] = {"the_data_I_want_to_share":"some_data"}
        
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
        pass

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
        #if topic == self._somevalue_topic:
        #    self._somevalue = message
        pass

    def on_apply_settings(self):
        pass

    def on_validate_settings(self):

        if not self.my_SnoozWorkspacePathEditorSettingsView.files_model or self.my_SnoozWorkspacePathEditorSettingsView.files_model.rowCount() == 0:
            WarningDialog(f"You need to select at least one Snooz workspace in step '1 - Setting Step.")
            return False
        if self.my_SnoozWorkspacePathEditorSettingsView.files_model.rowCount() >= 1:
            selected_indexes = self.my_SnoozWorkspacePathEditorSettingsView.Files_listView.selectedIndexes()
            if not selected_indexes:
                WarningDialog("You need to select at least one Snooz workspace to modify its path in step '1 - Setting Step'.")
                return False
        if len(self.my_SnoozWorkspacePathEditorSettingsView.Suffix_lineEdit.text())==0:
            WarningDialog(f"You need to define a suffix for the new Snooz workspaces in step '1 - Setting Step.")
            return False
        if len(self.my_SnoozWorkspacePathEditorSettingsView.New_files_lineEdit.text())==0:
            WarningDialog(f"You need to define a destination to save the new Snooz workspaces in step '1 - Setting Step.")
            return False        
        if self.my_SnoozWorkspacePathEditorSettingsView.validate_all_paths():
            if WarningDialogWithButtons.show_warning(f"Some file paths do not exist. Please verify.\nDetails:\n{json.dumps(self.my_SnoozWorkspacePathEditorSettingsView.validate_all_paths(), indent=2)}"):
                return True
            else:
                return False

        return True