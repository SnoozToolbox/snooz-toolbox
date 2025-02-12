"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    MissingPackagesDialog
"""
from qtpy import QtWidgets

from ui.Ui_MissingPackagesDialog import Ui_MissingPackagesDialog

class MissingPackagesDialog(QtWidgets.QDialog, Ui_MissingPackagesDialog):
    def __init__(self, missing_packages, package_manager, *args, **kwargs):
        super(MissingPackagesDialog, self).__init__(*args, **kwargs)
        self._package_manager = package_manager
        self._missing_packages = missing_packages

        self.setupUi(self)
        self._init_ui()

    def _init_ui(self):
        #self.missing_packages_tablewidget.clear()
        self.missing_packages_tablewidget.setRowCount(len(self._missing_packages))
        for idx, package in enumerate(self._missing_packages):
            self.missing_packages_tablewidget.setItem(idx,0, QtWidgets.QTableWidgetItem(package["package_name"]))
            self.missing_packages_tablewidget.setItem(idx,1, QtWidgets.QTableWidgetItem(package["package_version"]))
