#! /usr/bin/env python3
"""
    InputFiles
    TODO CLASS DESCRIPTION
"""
from CEAMSTools.DetectionsCohortReview.InputFiles.Ui_InputFiles import Ui_InputFiles
from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog

from qtpy import QtCore, QtWidgets

class InputFiles(BaseStepView, Ui_InputFiles, QtWidgets.QWidget):
    """
        InputFiles
        Settings viewer of the DetectionsCohortReview plugin are loaded.
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
        self._det_review_identifier = "52e946b1-c283-426c-a247-1731a9a549cb"

        # To use the SettingsView of a plugin and interract with its fonctions
        module = self.process_manager.get_node_by_id(self._det_review_identifier)
        if module is None:
            print(f'ERROR module_id isn\'t found in the process:{self._det_review_identifier}')
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

        # Make sure at least one det file is added
        if len(self.my_SettingsView.filenames)==0:
            WarningDialog(f"Add a 'detailed events cohort report' file in the step '1-Input Files'")
            return False
        
        # Make sure at least one channel/ROI is selected for each subject
        for subject in self.my_SettingsView.subject_chans_label.keys():
            # Dictionary to keep original and modified channel name to apply the change to self.det_df
            # Keys are the subjects
            #   each item is a list of 3 elements [original chan label, modified chan label, bool selection flag]
            chan_subject_used = self.my_SettingsView.subject_chans_label[subject][self.my_SettingsView.chan_state_col]
            # Dict to manage the ROI at the subject level
            #   keys are the subjects
            #   Each item is a list of n_ROIs with its selection label  [[ROI#1 label, bool selection flag]
            #                                                           [ROI#2 label, bool selection flag]]
            #                                                               ...
            if subject in self.my_SettingsView.ROIs_subjects.keys():
                # Compute  only if the ROI is checked for the current subject
                all_ROIs_subject = self.my_SettingsView.ROIs_subjects[subject]
                # For each ROI available in the current subject
                roi_subject_used = []
                for ROI_label, ROI_sel in all_ROIs_subject:
                    roi_subject_used.append(ROI_sel)
                if sum(chan_subject_used)==0 and all(roi_subject_used):
                    WarningDialog(f"At least one subject has no channel or ROI selected, start looking at {subject} in step '1-Input Files'")
                    return False
            else:
                if sum(chan_subject_used)==0:
                    WarningDialog(f"At least one subject has no channel or ROI selected, start looking at {subject} in step '1-Input Files'")
                    return False                

        return True


    # Slot created to receive the signal emitted from DetectionsCohortReviewSettingsView when the filenames is modified
    @QtCore.Slot()
    def filenames_modified_slot(self):
        self._context_manager[self.context_InputFiles] = self.my_SettingsView.filenames