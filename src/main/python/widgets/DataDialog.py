"""
@ Valorisation Recherche HSCM, Societe en Commandite - 2025
See the file LICENCE for full license details.
"""

from qtpy.QtCore import QUrl
from qtpy.QtGui import QDesktopServices
from qtpy import QtWidgets

from Managers.StyleManager import is_dark_theme, theme_tokens
from ui.Ui_DataDialog import Ui_DataDialog

class DataDialog(QtWidgets.QDialog, Ui_DataDialog):
    def __init__(self, *args, **kwargs):
        super(DataDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        if is_dark_theme():
            # The form gives the text its light blue box of the light theme
            tokens = theme_tokens()
            self.textBrowser.setStyleSheet(
                "QTextBrowser {"
                f" background-color: {tokens['surface_alt']}; color: {tokens['text']};"
                f" border: 1px solid {tokens['border']}; padding: 5px; }}")