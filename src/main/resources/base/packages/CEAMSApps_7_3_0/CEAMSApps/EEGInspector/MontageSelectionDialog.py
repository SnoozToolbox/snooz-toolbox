"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QDialog, QTableWidgetItem, QCheckBox
from CEAMSApps.EEGInspector.ui.Ui_MontageSelection import Ui_MontageSelection

# Subclass QMainWindow to customize your application's main window
class MontageSelectionDialog(QDialog, Ui_MontageSelection):
    def __init__(self, channels, selected_montage:int):
        super().__init__()
        self.setupUi(self)
        self._previous_selected_montage = selected_montage
        self._channels = channels
        self._montage_selection = None

        #For each key value in _channels
        for montage_name, channels in self._channels.items():
            self.montages_comboBox.addItem(montage_name)

        if self._previous_selected_montage is not None:
            self.montages_comboBox.setCurrentIndex(self._previous_selected_montage)
            self.montage_name = self.montages_comboBox.currentText()
        else:
            self.montage_name = self.montages_comboBox.currentText()
        self.montages_comboBox.currentIndexChanged.connect(self.montage_change)
        self.montage_change(None)

    # Properties
    @property
    def montage_selection(self):
        return self._montage_selection
    
        
    def montage_change(self, _):
        self.montage_name = self.montages_comboBox.currentText()

    def accept(self):
        self._montage_selection = self.montages_comboBox.currentIndex()
        super().accept()
