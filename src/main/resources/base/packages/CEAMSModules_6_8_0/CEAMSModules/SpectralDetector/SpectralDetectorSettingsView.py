"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the SpectralDetector plugin
"""

from qtpy import QtWidgets

from CEAMSModules.SpectralDetector.Ui_SpectralDetectorSettingsView import Ui_SpectralDetectorSettingsView
from commons.BaseSettingsView import BaseSettingsView

class SpectralDetectorSettingsView( BaseSettingsView,  Ui_SpectralDetectorSettingsView, QtWidgets.QWidget):
    """
        SpectralDetectorView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        # Subscribe to the proper topics to send/get data from the node
        self._event_group_topic = f'{self._parent_node.identifier}.event_group'
        self._pub_sub_manager.subscribe(self, self._event_group_topic)
        self._event_name_topic = f'{self._parent_node.identifier}.event_name'
        self._pub_sub_manager.subscribe(self, self._event_name_topic)
        self._low_freq_topic = f'{self._parent_node.identifier}.low_freq'
        self._pub_sub_manager.subscribe(self, self._low_freq_topic)
        self._high_freq_topic = f'{self._parent_node.identifier}.high_freq'
        self._pub_sub_manager.subscribe(self, self._high_freq_topic)
        self._bsl_low_freq_topic = f'{self._parent_node.identifier}.bsl_low_freq'
        self._pub_sub_manager.subscribe(self, self._bsl_low_freq_topic)
        self._bsl_high_freq_topic = f'{self._parent_node.identifier}.bsl_high_freq'
        self._pub_sub_manager.subscribe(self, self._bsl_high_freq_topic)
        self._rel_freq_topic = f'{self._parent_node.identifier}.rel_freq'
        self._pub_sub_manager.subscribe(self, self._rel_freq_topic)        
        self._threshold_val_topic = f'{self._parent_node.identifier}.threshold_val'
        self._pub_sub_manager.subscribe(self, self._threshold_val_topic)
        self._threshold_unit_topic = f'{self._parent_node.identifier}.threshold_unit'
        self._pub_sub_manager.subscribe(self, self._threshold_unit_topic)
        self._threshold_behavior_topic = f'{self._parent_node.identifier}.threshold_behavior'
        self._pub_sub_manager.subscribe(self, self._threshold_behavior_topic)
        self._baseline_win_len_topic = f'{self._parent_node.identifier}.baseline_win_len'
        self._pub_sub_manager.subscribe(self, self._baseline_win_len_topic)
        self._channel_dbg_len_topic = f'{self._parent_node.identifier}.channel_dbg'
        self._pub_sub_manager.subscribe(self, self._channel_dbg_len_topic)


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._event_group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._low_freq_topic, 'ping')
        self._pub_sub_manager.publish(self, self._high_freq_topic, 'ping')
        self._pub_sub_manager.publish(self, self._bsl_low_freq_topic, 'ping')
        self._pub_sub_manager.publish(self, self._bsl_high_freq_topic, 'ping')
        self._pub_sub_manager.publish(self, self._rel_freq_topic, 'ping')
        self._pub_sub_manager.publish(self, self._threshold_val_topic, 'ping')
        self._pub_sub_manager.publish(self, self._threshold_unit_topic, 'ping')
        self._pub_sub_manager.publish(self, self._threshold_behavior_topic, 'ping')
        self._pub_sub_manager.publish(self, self._baseline_win_len_topic, 'ping')
        self._pub_sub_manager.publish(self, self._channel_dbg_len_topic, 'ping')


    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        # Send the settings to the publisher for inputs to CsvReaderMaster
        self._pub_sub_manager.publish(self, self._event_group_topic, \
            str(self.group_lineedit.text()))
        self._pub_sub_manager.publish(self, self._event_name_topic, \
            str(self.event_name_lineedit.text()))
        self._pub_sub_manager.publish(self, self._low_freq_topic, \
            str(self.low_frequency_lineedit.text()))
        self._pub_sub_manager.publish(self, self._high_freq_topic, \
            str(self.high_frequency_lineedit.text()))
        self._pub_sub_manager.publish(self, self._bsl_low_freq_topic, \
            str(self.bsl_low_freq_lineedit.text()))
        self._pub_sub_manager.publish(self, self._bsl_high_freq_topic, \
            str(self.bsl_high_freq_lineedit.text()))
        self._pub_sub_manager.publish(self, self._rel_freq_topic, \
            str(int(self.rel_checkBox.isChecked())))
        self._pub_sub_manager.publish(self, self._threshold_val_topic, \
            str(self.tresholdval_lineedit.text()))
        self._pub_sub_manager.publish(self, self._threshold_unit_topic, \
            str(self.threshUnit_comboBox.currentText()))
        self._pub_sub_manager.publish(self, self._threshold_behavior_topic, \
            str(self.threshBeha_comboBox.currentText()))
        self._pub_sub_manager.publish(self, self._baseline_win_len_topic, \
            str(self.baseline_win_len_lineedit.text()))
        self._pub_sub_manager.publish(self, self._channel_dbg_len_topic, \
            str(self.chan_det_info_lineedit.text()))


    # Slot called when user changes the checkbox to activate relative freq band
    def on_input_format_changed(self, int):
        if self.rel_checkBox.isChecked():
            self.bsl_high_freq_lineedit.setEnabled(True)
            self.bsl_low_freq_lineedit.setEnabled(True)
        else:
            self.bsl_high_freq_lineedit.setEnabled(False)
            self.bsl_low_freq_lineedit.setEnabled(False)

    def on_topic_update(self, topic, message, sender):
        pass

    # Called by the publisher to init settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        # All lineEdit
        if topic == self._event_group_topic:
            self.group_lineedit.setText(message)
        if topic == self._event_name_topic:
            self.event_name_lineedit.setText(message)
        if topic == self._low_freq_topic:
            self.low_frequency_lineedit.setText(message)
        if topic == self._high_freq_topic:
            self.high_frequency_lineedit.setText(message)
        if topic == self._bsl_low_freq_topic:
            self.bsl_low_freq_lineedit.setText(message)
        if topic == self._bsl_high_freq_topic:
            self.bsl_high_freq_lineedit.setText(message)
        if topic == self._threshold_val_topic:
            self.tresholdval_lineedit.setText(message)
        if topic == self._baseline_win_len_topic:
            self.baseline_win_len_lineedit.setText(message)
        if topic == self._channel_dbg_len_topic:
            self.chan_det_info_lineedit.setText(message)
        # All checkbox
        if topic == self._rel_freq_topic:
            self.rel_checkBox.setChecked(int(message))
        # All comboBox
        if topic == self._threshold_unit_topic:
            self.threshUnit_comboBox.setCurrentText(message)
        if topic == self._threshold_behavior_topic:
            self.threshBeha_comboBox.setCurrentText(message) 


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._event_group_topic)
            self._pub_sub_manager.unsubscribe(self, self._event_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._low_freq_topic)
            self._pub_sub_manager.unsubscribe(self, self._high_freq_topic)
            self._pub_sub_manager.unsubscribe(self, self._bsl_low_freq_topic)
            self._pub_sub_manager.unsubscribe(self, self._bsl_high_freq_topic)
            self._pub_sub_manager.unsubscribe(self, self._rel_freq_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_val_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_unit_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_behavior_topic)
            self._pub_sub_manager.unsubscribe(self, self._baseline_win_len_topic)
            self._pub_sub_manager.unsubscribe(self, self._channel_dbg_len_topic)
