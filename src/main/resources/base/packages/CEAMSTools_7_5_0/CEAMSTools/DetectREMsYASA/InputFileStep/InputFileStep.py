#! /usr/bin/env python3
"""
    InputFilesStep
    Step to select the input files for the REMs detection.
    It inherits from InputFilesStep and is used to select the input files for the REMs detection.
"""

import os

from CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep import InputFilesStep
from CEAMSTools.DetectREMsYASA.DetectorStep.DetectorStep import DetectorStep
from widgets.WarningDialogWithButtons import WarningDialogWithButtons


class InputFileStep( InputFilesStep):

    # Overwrite the default values of the base class 
    # (really important to keep :
    #   context_files_view      = "input_files_settings_view")
    psg_reader_identifier = "c3e6adf4-0698-4655-b2a5-e0cf102bf224"
    valid_stage_mandatory = False    # To verify that all recordings have valid sleep stages
    valid_selected_chan   = True    # To verify if at least one channel is selected
    valid_single_chan     = False   # To verify if only one chan is selected for each file

    """
        InputFileStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform PSGReader of the files to open and propagate the events included in the files.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

    def _get_files_without_annotation(self):
        """
        Return recording filenames whose sleep stages are only '9' (no annotation file).

        This matches the EventSubdivision.events input, which receives PSGReader sleep stages.
        """
        files_without_annotation = []
        files_model = self.my_PsgReaderSettingsView.files_model
        file_list = self.my_PsgReaderSettingsView.get_files_list(files_model)

        for file_path in file_list:
            if not self.my_PsgReaderSettingsView.is_stages_scored(file_path, files_model):
                files_without_annotation.append(os.path.basename(file_path))

        return files_without_annotation

    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if not super().on_validate_settings():
            return False

        # Unscored mode does not require an annotation file.
        if self._context_manager.get(DetectorStep.context_REM_Report_selection, 1) != 1:
            return True

        files_without_annotation = self._get_files_without_annotation()
        if not files_without_annotation:
            return True

        files_list_msg = "\n".join(f"- {filename}" for filename in files_without_annotation)
        msg = (
            "The following recording(s) have no annotation file:\n"
            f"{files_list_msg}\n\n"
            "If you selected 'Scored' in step '2 - Detector Step', REMs detection is "
            "performed only on the REM sleep stage and you need to provide an annotation file with sleep stages included.\n"
            "If you selected 'Unscored', REMs detection is performed without considering "
            "sleep stages and an annotation file is not required.\n\n"
            "Do you want to continue?"
        )
        if WarningDialogWithButtons.show_warning(msg):
            return True
        return False
