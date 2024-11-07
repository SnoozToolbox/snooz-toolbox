"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the SleepReport plugin
"""

from qtpy import QtWidgets

from CEAMSModules.SleepReport.Ui_SleepReportSettingsView import Ui_SleepReportSettingsView
from commons.BaseSettingsView import BaseSettingsView

DEBUG = False

class SleepReportSettingsView( BaseSettingsView,  Ui_SleepReportSettingsView, QtWidgets.QWidget):
    """
        SleepReportView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        
        self.output_filename_topic = f'{self._parent_node.identifier}.output_filename'
        self._pub_sub_manager.subscribe(self, self.output_filename_topic)

        # init UI
        self.setupUi(self)

    def load_settings(self):
        self._pub_sub_manager.publish(self, self.output_filename_topic, 'ping')

    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self.output_filename_topic, \
            self.output_file_lineedit.text())

    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'SleepReportSettingsView.on_topic_update {topic}:{message}')

    def on_topic_response(self, topic, message, sender):
        if topic == self.output_filename_topic:
            self.output_file_lineedit.setText(message)

    def on_choose_ouput_file(self):
        name, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Output File', "", "CSV (*.csv)")
        if name:
            self.output_file_lineedit.setText(name)
        
