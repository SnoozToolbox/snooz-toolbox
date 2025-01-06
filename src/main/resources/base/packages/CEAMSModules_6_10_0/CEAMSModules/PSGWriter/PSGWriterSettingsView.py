"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the PSGWriter plugin
"""

from qtpy import QtWidgets

from CEAMSModules.PSGWriter.Ui_PSGWriterSettingsView import Ui_PSGWriterSettingsView
from commons.BaseSettingsView import BaseSettingsView

class PSGWriterSettingsView( BaseSettingsView,  Ui_PSGWriterSettingsView, QtWidgets.QWidget):
    """
        PSGWriterView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        self._in_filename_topic = f'{self._parent_node.identifier}.input_filename'
        self._out_filename_topic = f'{self._parent_node.identifier}.output_filename'
        self._overwrite_evt_topic = f'{self._parent_node.identifier}.overwrite_events'
        self._overwrite_signal_topic = f'{self._parent_node.identifier}.overwrite_signals'

        self._pub_sub_manager.subscribe(self, self._in_filename_topic)
        self._pub_sub_manager.subscribe(self, self._out_filename_topic)
        self._pub_sub_manager.subscribe(self, self._overwrite_evt_topic)
        self._pub_sub_manager.subscribe(self, self._overwrite_signal_topic)


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView
        """
        self._pub_sub_manager.publish(self, self._in_filename_topic, 'ping')
        self._pub_sub_manager.publish(self, self._out_filename_topic, 'ping')
        self._pub_sub_manager.publish(self, self._overwrite_evt_topic, 'ping')
        self._pub_sub_manager.publish(self, self._overwrite_signal_topic, 'ping')


    def on_apply_settings(self):
        """ Called when the user clicks on "Apply"
        """
        # Send the settings to the publisher for inputs to PSGWriter
        self._pub_sub_manager.publish(self, self._in_filename_topic, str(self.lineEdit_input_filename.text()))
        self._pub_sub_manager.publish(self, self._out_filename_topic, str(self.lineEdit_output_filename.text()))
        self._pub_sub_manager.publish(self, self._overwrite_evt_topic, str(self.checkBox_overwrite_events.isChecked()))
        self._pub_sub_manager.publish(self, self._overwrite_signal_topic, str(self.checkBox_overwrite_signals.isChecked()))


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView
        """
        if topic == self._in_filename_topic:
            self.lineEdit_input_filename.setText(message)
        if topic == self._out_filename_topic:
            self.lineEdit_output_filename.setText(message)
        if topic == self._overwrite_evt_topic:
            self.checkBox_overwrite_events.setChecked(eval(message))
        if topic == self._overwrite_signal_topic:
            self.checkBox_overwrite_signals.setChecked(eval(message))