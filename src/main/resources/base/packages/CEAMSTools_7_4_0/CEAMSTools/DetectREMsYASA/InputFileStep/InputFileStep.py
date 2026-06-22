#! /usr/bin/env python3
"""
    InputFilesStep
    Step to select the input files for the REMs detection.
    It inherits from InputFilesStep and is used to select the input files for the REMs detection.
"""

from qtpy import QtWidgets, QtCore
from qtpy.QtCore import QTimer

from CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep import InputFilesStep
#from AutomaticSleepScoringTools.ScoreSleepStagesYASA.InputFilesScoreStep.Ui_InputFilesScoreStep import Ui_InputFilesScoreStep
from commons.BaseStepView import BaseStepView

from widgets.WarningDialog import WarningDialog


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
