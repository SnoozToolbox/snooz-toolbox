"""
@ Valorisation Recherche HSCM, Société en Commandite – 2025
See the file LICENCE for full license details.
"""

"""
    This step is used to select the files to score the sleep stages.
"""

from qtpy import QtWidgets, QtCore
from qtpy.QtCore import QTimer

from CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep import InputFilesStep
#from AutomaticSleepScoringTools.AutomaticSleepScoring.InputFilesScoreStep.Ui_InputFilesScoreStep import Ui_InputFilesScoreStep
from commons.BaseStepView import BaseStepView

from widgets.WarningDialog import WarningDialog


class InputFilesScoreStep( InputFilesStep):

    # Overwrite the default values of the base class 
    # (really important to keep :
    #   context_files_view      = "input_files_settings_view")
    psg_reader_identifier = "031201d5-ff93-4be6-90d3-256d2ba689d1"
    valid_stage_mandatory = False    # To verify that all recordings have valid sleep stages
    valid_selected_chan   = True    # To verify if at least one channel is selected
    valid_single_chan     = False   # To verify if only one chan is selected for each file

    """
        InputFileStep
        This step is used to select the files to score the sleep stages.
    """
