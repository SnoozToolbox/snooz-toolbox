"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

from qtpy import QtWidgets

class WarningDialog():
    """ Create a warning dialog class based on QtWidgets.QMessageBox """

    # Define the constructor of the class.
    def __init__(self, message:str, *args, **kwargs):
        log_msg = QtWidgets.QMessageBox()
        log_msg.setWindowTitle("Warning")
        log_msg.setText(message)
        log_msg.setIcon(QtWidgets.QMessageBox.Warning)
        log_msg.exec_()

