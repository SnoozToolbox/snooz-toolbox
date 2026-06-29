"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the AmplitudeDetector plugin
"""

from qtpy import QtWidgets

from CEAMSModules.AmplitudeDetector.Ui_AmplitudeDetectorSettingsView import Ui_AmplitudeDetectorSettingsView
from commons.BaseSettingsView import BaseSettingsView

class AmplitudeDetectorSettingsView( BaseSettingsView,  Ui_AmplitudeDetectorSettingsView, QtWidgets.QWidget):
    """
        AmplitudeDetectorView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        # Subscribe to the proper topics to send/get data from the node
        self._group_topic = f'{self._parent_node.identifier}.event_group'
        self._pub_sub_manager.subscribe(self, self._group_topic)
        self._name_topic = f'{self._parent_node.identifier}.event_name'
        self._pub_sub_manager.subscribe(self, self._name_topic)
        self._pad_sec_topic = f'{self._parent_node.identifier}.pad_sec'
        self._pub_sub_manager.subscribe(self, self._pad_sec_topic)
        self._threshold_val_topic = f'{self._parent_node.identifier}.threshold_val'
        self._pub_sub_manager.subscribe(self, self._threshold_val_topic)
        self._threshold_unit_topic = f'{self._parent_node.identifier}.threshold_unit'
        self._pub_sub_manager.subscribe(self, self._threshold_unit_topic)
        self._threshold_behavior_topic = f'{self._parent_node.identifier}.threshold_behavior'
        self._pub_sub_manager.subscribe(self, self._threshold_behavior_topic)
        self._baseline_win_len_topic = f'{self._parent_node.identifier}.baseline_win_len'
        self._pub_sub_manager.subscribe(self, self._baseline_win_len_topic)
        self._channel_dbg_topic = f'{self._parent_node.identifier}.channel_dbg'
        self._pub_sub_manager.subscribe(self, self._channel_dbg_topic)


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._name_topic, 'ping')   
        self._pub_sub_manager.publish(self, self._pad_sec_topic, 'ping')
        self._pub_sub_manager.publish(self, self._threshold_val_topic, 'ping') 
        self._pub_sub_manager.publish(self, self._threshold_unit_topic, 'ping')
        self._pub_sub_manager.publish(self, self._threshold_behavior_topic, 'ping') 
        self._pub_sub_manager.publish(self, self._baseline_win_len_topic, 'ping')
        self._pub_sub_manager.publish(self, self._channel_dbg_topic, 'ping') 


    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        # Send the settings to the publisher for inputs to AmplitudeDetector
        self._pub_sub_manager.publish(self, self._group_topic, \
            str(self.group_lineedit.text()))
        self._pub_sub_manager.publish(self, self._name_topic, \
            str(self.event_name_lineedit.text()))
        self._pub_sub_manager.publish(self, self._pad_sec_topic, \
            str(self.pad_length_lineedit.text()))
        self._pub_sub_manager.publish(self, self._threshold_val_topic, \
            str(self.tresholdval_lineedit.text()))
        self._pub_sub_manager.publish(self, self._channel_dbg_topic, \
            str(self.chan_det_info_lineedit.text()))
        self._pub_sub_manager.publish(self, self._threshold_unit_topic, \
            str(self.threshUnit_comboBox.currentText()))
        self._pub_sub_manager.publish(self, self._threshold_behavior_topic, \
            str(self.threshBeha_comboBox.currentText()))

    def on_topic_update(self, topic, message, sender):
        pass

    # Called by the publisher to init settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._group_topic:
            self.group_lineedit.setText(message)
        if topic == self._name_topic:
            self.event_name_lineedit.setText(message)
        if topic == self._pad_sec_topic:
            self.pad_length_lineedit.setText(message)
        if topic == self._threshold_val_topic:
            self.tresholdval_lineedit.setText(message)
        if topic == self._channel_dbg_topic:
            self.chan_det_info_lineedit.setText(message)
        if topic == self._threshold_unit_topic:
            self.threshUnit_comboBox.setCurrentText(message)
        if topic == self._threshold_behavior_topic:
            self.threshBeha_comboBox.setCurrentText(message)  


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._group_topic)
            self._pub_sub_manager.unsubscribe(self, self._name_topic)            
            self._pub_sub_manager.unsubscribe(self, self._pad_sec_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_val_topic)
            self._pub_sub_manager.unsubscribe(self, self._channel_dbg_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_unit_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_behavior_topic)