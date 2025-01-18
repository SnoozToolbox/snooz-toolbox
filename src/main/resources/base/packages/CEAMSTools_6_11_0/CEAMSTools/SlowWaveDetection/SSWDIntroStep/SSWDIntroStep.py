#! /usr/bin/env python3
"""
    SSWDIntroStep
    Settings viewer of the intro plugin for the Slow Wave Detector tool
"""

from qtpy import QtWidgets

from CEAMSTools.SlowWaveDetection.SSWDIntroStep.Ui_SSWDIntroStep import Ui_SSWDIntroStep
from commons.BaseStepView import BaseStepView

class SSWDIntroStep( BaseStepView,  Ui_SSWDIntroStep, QtWidgets.QWidget):
    """
        IntrSSWDIntroStepoStep
        Displays the functionnalities of the slow wave detector.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass
