"""
@ Valorisation Recherche HSCM, Société en Commandite – 2025
See the file LICENCE for full license details.
"""

"""
    The itroduction step of the tool
"""

from qtpy import QtWidgets

from CEAMSTools.ScoreSleepStagesYASA.AlgoIntroStep.Ui_AlgoIntroStep import Ui_AlgoIntroStep
from commons.BaseStepView import BaseStepView

class AlgoIntroStep( BaseStepView, Ui_AlgoIntroStep, QtWidgets.QWidget):
    """
        AlgoIntroStep describes the tool and the details of the alogrithm.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass