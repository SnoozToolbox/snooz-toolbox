"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
from qtpy import QtWidgets

from Managers.LogManager import LogManager
from ui.Ui_LogsDialog import Ui_LogsDialog

class LogsDialog(QtWidgets.QDialog, Ui_LogsDialog):
    """ Create a logs dialog class based on QtWidgets.QDialog and Ui_LogsDialog """

     # Define the constructor of the class.
    def __init__(self, log_manager:LogManager, *args, **kwargs):
        super(LogsDialog, self).__init__(*args, **kwargs)
        self._log_manager = log_manager
        self.setupUi(self)
        self._update_logs()

    # Define a method to clear the log entries.
    def on_clear(self):
        self._log_manager.timeline_logs.clear()
        self._update_logs()

    # Define a private method to update the contents of the logs_textedit widget.
    def _update_logs(self):
        logs_text = ""
        for (identifier, entry) in self._log_manager.timeline_logs:
            if "-----" not in entry:
                logs_text = logs_text + identifier + "\t" + entry + "\n"
        self.logs_textedit.setPlainText(logs_text)
