#! /usr/bin/env python3
"""
    InputFileStep
    Step to open files to edit annotations.
    The class inherits from the InputFilesStep class of the PowerSpectralAnalysis.
"""
from CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep import InputFilesStep

class InputFileAnnotStep( InputFilesStep):

    # Overwrite the default values of the base class 
    # (really important to keep :
    #   context_files_view      = "input_files_settings_view")
    psg_reader_identifier   = "02e7bb3e-6a79-4837-acc2-afc861d3063c"
    valid_stage_mandatory   = False     # To verify that all recordings have valid sleep stages
    valid_selected_chan     = False     # To verify if at leas one chan is selected for each file
    valid_single_chan       = False     # To verify if only one chan is selected for each file

    """
        InputFileStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform PSGReader of the files to open and propagate the events included in the files.
    """

# For the other functions see CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep