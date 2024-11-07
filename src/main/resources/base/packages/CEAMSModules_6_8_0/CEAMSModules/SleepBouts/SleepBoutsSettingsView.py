"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the SleepBouts plugin
"""
from CEAMSModules.SleepBouts.Ui_SleepBoutsSettingsView import Ui_SleepBoutsSettingsView
from commons.BaseSettingsView import BaseSettingsView
from widgets.WarningDialog import WarningDialog

from qtpy import QtWidgets

DEBUG = False

class SleepBoutsSettingsView( BaseSettingsView,  Ui_SleepBoutsSettingsView, QtWidgets.QWidget):
    """
        SleepBoutsView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        
        self.output_filename_topic = f'{self._parent_node.identifier}.output_filename'
        self._pub_sub_manager.subscribe(self, self.output_filename_topic)

        self.export_in_seconds_topic = f'{self._parent_node.identifier}.export_in_seconds'
        self._pub_sub_manager.subscribe(self, self.export_in_seconds_topic)

        # init UI
        self.setupUi(self)


    def load_settings(self):
        self._pub_sub_manager.publish(self, self.output_filename_topic, 'ping')
        self._pub_sub_manager.publish(self, self.export_in_seconds_topic, 'ping')


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if len(self.output_file_lineedit.text())==0:
            WarningDialog("Define the output filename")
            return False
        return True


    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self.output_filename_topic, \
            self.output_file_lineedit.text())

        if self.export_seconds_radiobutton.isChecked():
            self._pub_sub_manager.publish(self, self.export_in_seconds_topic, "1")
        else:
            self._pub_sub_manager.publish(self, self.export_in_seconds_topic, "0")


    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'SleepBoutsSettingsView.on_topic_update {topic}:{message}')


    def on_topic_response(self, topic, message, sender):
        if topic == self.output_filename_topic:
            self.output_file_lineedit.setText(message)
        elif topic == self.export_in_seconds_topic:
            if message == "1":
                self.export_seconds_radiobutton.setChecked(True)
            else:
                self.export_epochs_radiobutton.setChecked(True)


    def on_choose_ouput_file(self):
        name, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Output File', "",\
             "CSV (*.csv)", options = QtWidgets.QFileDialog.DontConfirmOverwrite)
        if name:
            self.output_file_lineedit.setText(name)
        
