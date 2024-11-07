"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    SleepReportDoc
    TODO CLASS DESCRIPTION
"""

from qtpy import QtWidgets

from CEAMSTools.SleepReport.SleepReportDoc.Ui_SleepReportDoc import Ui_SleepReportDoc
from commons.BaseStepView import BaseStepView

class SleepReportDoc( BaseStepView,  Ui_SleepReportDoc, QtWidgets.QWidget):
    """
        SleepReportDoc
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
