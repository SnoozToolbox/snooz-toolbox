#! /usr/bin/env python3
"""
    InputFiles
    TODO CLASS DESCRIPTION
"""
from CEAMSTools.PSACohortReview.InputFiles.Ui_InputFiles import Ui_InputFiles
from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog

from qtpy import QtCore, QtWidgets

class InputFiles(BaseStepView, Ui_InputFiles, QtWidgets.QWidget):
    """
        InputFiles
        Settings viewer of the PSACohortReview plugin are loaded.
        The settings viewer allows to select and rename channels and add ROIs.
    """
    # Key for the context shared with other step of the preset
    context_InputFiles = "context_filenames"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # The context is a memory space shared by all steps of a tool. 
        # It is used to share and notice other steps whenever the value in it changes. 
        # It's very useful when the parameter within a step must have an impact in another step.
        self._context_manager[self.context_InputFiles] = {"filenames":[]}

        # Define modules and nodes to talk to
        self._PSA_review_identifier = "8df6ac98-9c6c-4f97-a579-5464ba4b6fe1"

        # To use the SettingsView of a plugin and interract with its fonctions
        module = self.process_manager.get_node_by_id(self._PSA_review_identifier)
        if module is None:
            print(f'ERROR module_id isn\'t found in the process:{self._PSA_review_identifier}')
        else:
            # To extract the SettingsView and add it to our Layout in the preset
            self.my_SettingsView = module.create_settings_view()
            self.verticalLayout.addWidget(self.my_SettingsView)   
            self.my_SettingsView.filenames_updated_signal.connect(self.filenames_modified_slot)
        

    def load_settings(self):
        pass


    def on_topic_update(self, topic, message, sender):
        pass


    def on_apply_settings(self):
        pass


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.

        # Make sure at least one PSA file is added
        if len(self.my_SettingsView.filenames)==0:
            WarningDialog(f"Add a PSA file in the step '1-Input Files'")
            return False
        
        # Detect subjects with no channel and no ROI selected.
        subjects_without_selection = []
        for subject in self.my_SettingsView.subject_chans_label.keys():
            # Dictionary to keep original and modified channel name to apply the change to self.PSA_df
            # Keys are the subjects
            #   each item is a list of 3 elements [original chan label, modified chan label, bool selection flag]
            chan_subject_used = self.my_SettingsView.subject_chans_label[subject][self.my_SettingsView.chan_state_col]
            has_channel_selected = sum(chan_subject_used) > 0
            # Dict to manage the ROI at the subject level
            #   keys are the subjects
            #   Each item is a list of n_ROIs with its selection label  [ROI#1 label, bool selection flag]
            #                                                           [ROI#2 label, bool selection flag]
            #                                                               ...
            has_roi_selected = False
            if subject in self.my_SettingsView.ROIs_subjects.keys():
                # Compute  only if the ROI is checked for the current subject
                all_ROIs_subject = self.my_SettingsView.ROIs_subjects[subject]
                # For each ROI available in the current subject
                for ROI_label, ROI_sel in all_ROIs_subject:
                    if ROI_sel:
                        has_roi_selected = True
                        break

            if not has_channel_selected and not has_roi_selected:
                subjects_without_selection.append(subject)

        if subjects_without_selection:
            subjects_as_text = "\n".join(f"- {subject}" for subject in subjects_without_selection)

            confirmation = QtWidgets.QMessageBox(self)
            confirmation.setIcon(QtWidgets.QMessageBox.Warning)
            confirmation.setWindowTitle("Subjects With No Selection")
            confirmation.setText(
                "Some subjects have no selected channel or ROI."
            )
            confirmation.setInformativeText(
                "These subjects will be skipped during analysis:"
            )
            confirmation.setMinimumWidth(680)

            # Keep the dialog size manageable while allowing long subject lists.
            subjects_preview = QtWidgets.QPlainTextEdit(confirmation)
            subjects_preview.setReadOnly(True)
            subjects_preview.setPlainText(subjects_as_text)
            subjects_preview.setMinimumHeight(160)
            subjects_preview.setMaximumHeight(260)
            subjects_preview.setMinimumWidth(500)
            subjects_preview.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
            subjects_preview.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)

            confirmation_layout = confirmation.layout()
            confirmation_layout.addWidget(
                subjects_preview,
                confirmation_layout.rowCount(),
                0,
                1,
                confirmation_layout.columnCount(),
            )

            confirmation.setStandardButtons(
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel
            )
            confirmation.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            confirmation.button(QtWidgets.QMessageBox.Yes).setText("Run anyway")
            confirmation.button(QtWidgets.QMessageBox.Cancel).setText("Cancel the run")

            if confirmation.exec() != QtWidgets.QMessageBox.Yes:
                return False

        return True


    # Slot created to receive the signal emitted from PSACohortReviewSettingsView when the filenames is modified
    @QtCore.Slot()
    def filenames_modified_slot(self):
        self._context_manager[self.context_InputFiles] = self.my_SettingsView.filenames