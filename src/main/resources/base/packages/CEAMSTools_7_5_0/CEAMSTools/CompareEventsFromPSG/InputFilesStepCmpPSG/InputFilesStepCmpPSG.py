#! /usr/bin/env python3
"""
    InputFiles
    Step to open files to detect spindles.
"""
from CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep import InputFilesStep

class InputFilesStepCmpPSG( InputFilesStep):

    # Overwrite the default values of the base class 
    # (really important to keep :
    #   context_files_view      = "input_files_settings_view")
    psg_reader_identifier = "9011a426-1d8c-4ab4-abdf-d98a927cf533"
    valid_stage_mandatory = True    # To verify that all recordings have valid sleep stages
    valid_selected_chan   = False   # To verify if at least one channel is selected
    valid_single_chan     = False   # To verify if only one chan is selected for each file

    """
        InputFileStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform PSGReader of the files to open and propagate the events included in the files.
    """

# For the other functions see CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep

