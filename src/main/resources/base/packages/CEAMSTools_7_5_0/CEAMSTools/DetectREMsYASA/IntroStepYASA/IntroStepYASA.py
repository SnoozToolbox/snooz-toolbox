#! /usr/bin/env python3
"""
    IntroStep
    Step to introduce the REMs detection tool.
"""
from commons.BaseStepView import BaseStepView

from CEAMSTools.DetectREMsYASA.IntroStepYASA.Ui_IntroStepYASA import Ui_IntroStepYASA

from qtpy import QtWidgets

class IntroStepYASA(BaseStepView, Ui_IntroStepYASA, QtWidgets.QWidget):
    """
        IntroStep
        Step to introduce the REMs detection tool.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass
