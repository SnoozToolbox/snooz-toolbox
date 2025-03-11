"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    FileErrorDialog
"""

from qtpy import QtWidgets, QtCore
from CEAMSTools.SleepReport.Commons.EventItem import EventItem

from CEAMSTools.SleepReport.Commons.Ui_FileErrorDialog import Ui_FileErrorDialog

class FileErrorDialog(QtWidgets.QDialog, Ui_FileErrorDialog):
    """
        FileErrorDialog
    """
    def __init__(self, files, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        self._files = files

        self.files_listwidget.addItems(self._files)
        