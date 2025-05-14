"""
@ Valorisation Recherche HSCM, Societe en Commandite - 2025
See the file LICENCE for full license details.
"""

from qtpy.QtCore import QUrl
from qtpy.QtGui import QDesktopServices
from qtpy import QtWidgets

from ui.Ui_DataDialog import Ui_DataDialog

class DataDialog(QtWidgets.QDialog, Ui_DataDialog):
    def __init__(self, *args, **kwargs):
        super(DataDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)