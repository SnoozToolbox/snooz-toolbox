#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    OutputFiles
    Lets the user control where connectivity outputs are saved.
"""

from qtpy import QtWidgets

from CEAMSTools.AnalyzeEEGConnectivity.OutputFiles.Ui_OutputFiles import Ui_OutputFiles
from commons.BaseStepView import BaseStepView

class OutputFiles(BaseStepView, Ui_OutputFiles, QtWidgets.QWidget):
    """
    UI Step for output path selection:
    - If 'Save in input folder' is checked, disables path selection and saves files in the input folder.
    - Otherwise, user can browse and pick a folder for outputs.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # init UI
        self.setupUi(self)

        # --- 1. Set Node IDs for every output node (both branches, all methods) ---
        # Annotation branch
        self._node_id_ConnectivityDetails_wpli = "803b6207-918f-4e3e-b5be-48ad9fc8b01c"
        self._node_id_ConnectivityDetails_dpli = "cc042193-2e41-49e0-b80e-973b1174cdb9"
        self._node_id_ConnectivityDetails_aec = "838795ca-9563-4370-918e-f8f92cc23220"
        self._node_id_NetworkProperties = "02d58c3b-80ec-4e80-8a3c-33d9ee521c18"
        # Sleep-stage branch
        self._node_id_ConnectivityDetails_wpli_sleep = "209980db-ecf3-4d88-9f66-c27373268a3b"
        self._node_id_ConnectivityDetails_dpli_sleep = "82b687e5-9cb4-43bc-80a8-b1cd735ded9b"
        self._node_id_ConnectivityDetails_aec_sleep = "7f93939c-b105-4637-a8e9-eae8fc40ceb1"
        self._node_id_NetworkProperties_sleep = "9b9b5bb5-f0a3-44f4-8d31-b3ee1896f725"

        # All output nodes that must receive the chosen output path.
        self._output_node_ids = [
            self._node_id_ConnectivityDetails_wpli,
            self._node_id_ConnectivityDetails_dpli,
            self._node_id_ConnectivityDetails_aec,
            self._node_id_NetworkProperties,
            self._node_id_ConnectivityDetails_wpli_sleep,
            self._node_id_ConnectivityDetails_dpli_sleep,
            self._node_id_ConnectivityDetails_aec_sleep,
            self._node_id_NetworkProperties_sleep,
        ]

        # --- 2. Connect UI Actions ---
        self.output_path_checkBox.stateChanged.connect(self.toggle_path_selection)
        self.choose_pushButton.clicked.connect(self.choose_folder)

        # --- 3. Set Initial State (set default checked) ---
        self.output_path_checkBox.setChecked(True)
        self.toggle_path_selection()  # This will disable the path UI on startup

    def toggle_path_selection(self):
        """
        Enables/disables path selection based on the checkbox state.
        """
        use_input_folder = self.output_path_checkBox.isChecked()
        self.path_lineEdit.setEnabled(not use_input_folder)
        self.choose_pushButton.setEnabled(not use_input_folder)
        if use_input_folder:
            self.path_lineEdit.clear()
    
    
    def choose_folder(self):
        """
        Opens a dialog for the user to pick a folder, and sets the line edit.
        """
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder:
            self.path_lineEdit.setText(folder)
        
    def load_settings(self):
        """
        Called when the settings view is opened. Can be used to sync UI from backend.
        """
        # You could ping the backend to get the saved path here, if desired.
        self._pub_sub_manager.publish(self, f"{self._node_id_ConnectivityDetails_wpli}.output_path", 'ping')
        #pass

    def on_topic_update(self, topic, message, sender):
        """
        Handles backend responses to our pings. Could update UI here.
        """
        # if topic == self._recording_path_topic:
        #     self.path_lineEdit.setText(message)
        pass

    def on_topic_response(self, topic, message, sender):
        # This will be called as a response to ping request.
        if topic == f"{self._node_id_ConnectivityDetails_wpli}.output_path":
           if message:  # Only update if there's a saved path (not empty)
                self.output_path_checkBox.setChecked(False)  # Uncheck to show custom path is used
                self.path_lineEdit.setEnabled(True)
                self.path_lineEdit.setText(message)
           else:
               self.output_path_checkBox.setChecked(True)
               self.path_lineEdit.setEnabled(False)
               self.path_lineEdit.clear()
        # pass

    def on_apply_settings(self):
        """
        Publishes the output_path to all ConnectivityDetails nodes in the pipeline.
        If the checkbox is checked, output_path is blank (backend nodes should use recording_path as fallback).
        Otherwise, sends the user-selected path.
        """
        use_input_folder = self.output_path_checkBox.isChecked()
        chosen_path = self.path_lineEdit.text() if not use_input_folder else ""

        # Publish the chosen path to every output node in both branches and all
        # methods. Only the active chain runs, so publishing to the inactive ones
        # is harmless.
        for node_id in self._output_node_ids:
            self._pub_sub_manager.publish(self, f"{node_id}.output_path", chosen_path)


    def on_validate_settings(self):
        """
        Ensures user input is valid before applying.
        """
        use_input_folder = self.output_path_checkBox.isChecked()
        if not use_input_folder and not self.path_lineEdit.text():
            QtWidgets.QMessageBox.warning(self, "Missing Path", "Please select an output folder or check the box to use the input file's folder.")
            return False
        return True
