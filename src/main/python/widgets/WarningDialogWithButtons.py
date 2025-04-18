"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

from qtpy import QtWidgets

class WarningDialogWithButtons():
    """ Create a warning dialog class with OK and Cancel buttons based on QtWidgets.QMessageBox """

    def __init__(self, message: str, *args, **kwargs):
        """
        Initialize a warning dialog with OK and Cancel buttons.
        Args:
            message (str): The warning message to display
        """
        self.log_msg = QtWidgets.QMessageBox()
        self.log_msg.setWindowTitle("Warning")
        self.log_msg.setText(message)
        self.log_msg.setIcon(QtWidgets.QMessageBox.Warning)
        
        # Add OK and Cancel buttons
        self.log_msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        self.log_msg.setDefaultButton(QtWidgets.QMessageBox.Ok)
        
        # Store the result when dialog is shown
        self.result = self.log_msg.exec_()

    @staticmethod
    def show_warning(message: str) -> bool:
        """
        Show a warning dialog with OK and Cancel buttons.
        Args:
            message (str): The warning message to display
        Returns:
            bool: True if user clicked OK, False if user clicked Cancel
        """
        dialog = QtWidgets.QMessageBox()
        dialog.setWindowTitle("Warning")
        dialog.setText(message)
        dialog.setIcon(QtWidgets.QMessageBox.Warning)
        dialog.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        dialog.setDefaultButton(QtWidgets.QMessageBox.Ok)
        result = dialog.exec_()
        return result == QtWidgets.QMessageBox.Ok 