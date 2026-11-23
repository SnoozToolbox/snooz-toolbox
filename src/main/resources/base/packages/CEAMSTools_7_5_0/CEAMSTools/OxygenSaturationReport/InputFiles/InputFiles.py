#! /usr/bin/env python3
"""
    InputFileStep
    Step to open files to detect SW.
"""

from qtpy import QtWidgets

from CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep import InputFilesStep

class InputFiles( InputFilesStep):

    # Overwrite the default values of the base class 
    # (really important to keep :
    #   context_files_view      = "input_files_settings_view")
    psg_reader_identifier = "c7d4e030-fb0b-4070-b17c-ddb3eaac0583"
    valid_stage_mandatory   = True  # The Oxygen desaturation can be performed on unscored data
    valid_selected_chan     = True  # The Oxygen desaturation cannot be performed without selected channels
    valid_single_chan       = True  # The Oxygen desaturation cannot be performed on more than one channel.

    """
        InputFileStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform PSGReader of the files to open and propagate the events included in the files.
    """

# For the other functions see CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep