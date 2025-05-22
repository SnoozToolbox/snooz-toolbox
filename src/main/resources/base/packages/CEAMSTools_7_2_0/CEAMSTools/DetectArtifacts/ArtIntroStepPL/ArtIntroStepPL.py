"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the Intro plugin
"""

from qtpy import QtWidgets

from CEAMSTools.DetectArtifacts.ArtIntroStepPL.Ui_ArtIntroStepPL import Ui_ArtIntroStepPL
from commons.BaseStepView import BaseStepView

class ArtIntroStepPL( BaseStepView,  Ui_ArtIntroStepPL, QtWidgets.QWidget):
    """
        ArtIntroStepPL displays the a few examples of artifact and describes the tool.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass