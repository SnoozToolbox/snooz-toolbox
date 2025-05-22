"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    SleepCycleDoc
    TODO CLASS DESCRIPTION
"""

from qtpy import QtWidgets

from CEAMSTools.SleepCycleExport.SleepCycleDoc.Ui_SleepCycleDoc import Ui_SleepCycleDoc
from commons.BaseStepView import BaseStepView

class SleepCycleDoc( BaseStepView,  Ui_SleepCycleDoc, QtWidgets.QWidget):
    """
        SleepCycleDoc
        TODO CLASS DESCRIPTION
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass
