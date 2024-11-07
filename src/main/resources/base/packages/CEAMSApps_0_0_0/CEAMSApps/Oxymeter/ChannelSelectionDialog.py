"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QDialog, QTableWidgetItem, QCheckBox
from CEAMSApps.Oxymeter.ui.Ui_ChannelSelection import Ui_ChannelSelection

# Subclass QMainWindow to customize your application's main window
class ChannelSelectionDialog(QDialog, Ui_ChannelSelection):
    def __init__(self, channels:dict, selected_montage:int, selected_oxymeter:str):
        super().__init__()
        self.setupUi(self)
        self._previous_selected_montage = selected_montage
        self._previous_selected_oxymeter = selected_oxymeter
        self._channels = channels
        self._montage_selection = None
        self._oxymeter_selection = None
        self._channels_selection = []

        #For each key value in _channels
        for montage_name, channels in self._channels.items():
            self.montages_comboBox.addItem(montage_name)

        if self._previous_selected_montage is not None:
            self.montages_comboBox.setCurrentIndex(self._previous_selected_montage)
            montage_name = self.montages_comboBox.currentText()
            channels = self._channels[montage_name]
        else:
            montage_name = self.montages_comboBox.currentText()
            channels = self._channels[montage_name]
        self.montages_comboBox.currentIndexChanged.connect(self.montage_change)
        self.montage_change(None)

    # Properties
    @property
    def montage_selection(self):
        return self._montage_selection
    
    @property
    def oxymeter_selection(self):
        return self._oxymeter_selection
        
    def montage_change(self, _):
        montage_name = self.montages_comboBox.currentText()
        channels = self._channels[montage_name]
        self._update_oxy_channel(channels)

    def accept(self):
        self._montage_selection = self.montages_comboBox.currentIndex()

        if self.oxy_channel_comboBox.currentText() == "None":
            self._oxymeter_selection = None
        else:
            self._oxymeter_selection = self.oxy_channel_comboBox.currentText()

        super().accept()

    def _update_oxy_channel(self, channels):
        self.oxy_channel_comboBox.clear()
        self.oxy_channel_comboBox.addItem("None")
        for channel in channels:
            self.oxy_channel_comboBox.addItem(channel.name)

        # Automatic default selection
        known_oxymeter_channels = ["spo2", "oxy", "osat", "oxymetre"]
        for channel in channels:
            if channel.name.lower() in known_oxymeter_channels:
                self.oxy_channel_comboBox.setCurrentText(channel.name)
                break
        
        # If it's the previously selected montage, select what was selected.
        if self._previous_selected_montage == self.montages_comboBox.currentText():
            if self._previous_selected_oxymeter is not None:
                self.oxy_channel_comboBox.setCurrentText(self._previous_selected_oxymeter)
                
