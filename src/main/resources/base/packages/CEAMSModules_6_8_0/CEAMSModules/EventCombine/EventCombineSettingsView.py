"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the EventCombine plugin
"""

from qtpy import QtWidgets

from CEAMSModules.EventCombine.Ui_EventCombineSettingsView import Ui_EventCombineSettingsView
from commons.BaseSettingsView import BaseSettingsView

class EventCombineSettingsView( BaseSettingsView,  Ui_EventCombineSettingsView, QtWidgets.QWidget):
    """
        EventCombineSettingsView displays the list of events.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._event1_name_topic = f'{self._parent_node.identifier}.event1_name'
        self._pub_sub_manager.subscribe(self, self._event1_name_topic)
        self._event2_name_topic = f'{self._parent_node.identifier}.event2_name'
        self._pub_sub_manager.subscribe(self, self._event2_name_topic)
        self._channel1_name_topic = f'{self._parent_node.identifier}.channel1_name'
        self._pub_sub_manager.subscribe(self, self._channel1_name_topic)
        self._channel2_name_topic = f'{self._parent_node.identifier}.channel2_name'
        self._pub_sub_manager.subscribe(self, self._channel2_name_topic)
        self._new_event_group_topic = f'{self._parent_node.identifier}.new_event_group'
        self._pub_sub_manager.subscribe(self, self._new_event_group_topic)
        self._new_event_name_topic = f'{self._parent_node.identifier}.new_event_name'
        self._pub_sub_manager.subscribe(self, self._new_event_name_topic)
        self._new_event_chan_topic = f'{self._parent_node.identifier}.new_event_chan'
        self._pub_sub_manager.subscribe(self, self._new_event_chan_topic)
        self._behavior_topic = f'{self._parent_node.identifier}.behavior'
        self._pub_sub_manager.subscribe(self, self._behavior_topic)


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._event1_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event2_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._channel1_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._channel2_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._new_event_group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._new_event_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._new_event_chan_topic, 'ping')
        self._pub_sub_manager.publish(self, self._behavior_topic, 'ping')


    # Called when the user clicks on "Apply"
    # Information is taken from the interface to the publisher
    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._event1_name_topic, \
            str(self.event1_name_lineedit.text()))
        self._pub_sub_manager.publish(self, self._event2_name_topic, \
            str(self.event2_name_lineedit.text()))
        self._pub_sub_manager.publish(self, self._channel1_name_topic, \
            str(self.channel1_lineedit.text()))
        self._pub_sub_manager.publish(self, self._channel2_name_topic, \
            str(self.channel2_lineedit.text()))
        self._pub_sub_manager.publish(self, self._new_event_group_topic, \
            str(self.new_event_group_lineedit.text()))
        self._pub_sub_manager.publish(self, self._new_event_name_topic, \
            str(self.new_event_name_lineedit.text()))
        self._pub_sub_manager.publish(self, self._new_event_chan_topic, \
            str(self.event_channel_lineedit.text()))
        self._pub_sub_manager.publish(self, self._behavior_topic, \
            str(self.behavior_comboBox.currentText()))

    
    # Called when the use check/uncheck channel_wise checkbox
    def on_chan_wise_checkbox(self,int):
        if not self.chan_wise_checkBox.isChecked():
            behavior = 'append'
            self.behavior_comboBox.clear()
            self.behavior_comboBox.addItem(behavior)
            self.behavior_comboBox.setCurrentText(behavior)
            self.channel1_lineedit.setText('')
            self.channel1_lineedit.setEnabled(False)
            self.channel2_lineedit.setText('')
            self.channel2_lineedit.setEnabled(False)
        else:
            self.behavior_comboBox.clear()
            self.behavior_comboBox.addItem("union")
            self.behavior_comboBox.addItem("union without concurrent events")
            self.behavior_comboBox.addItem("intersection")      
            self.channel1_lineedit.setEnabled(True)
            self.channel2_lineedit.setEnabled(True)


    # Called when user check or uncheck the modify the event checkbox
    def on_modify_checkbox(self):
        if self.rename_checkBox.isChecked():
            self.new_event_group_lineedit.setEnabled(True)
            self.new_event_name_lineedit.setEnabled(True)
            self.event_channel_lineedit.setEnabled(True)
        else:
            self.new_event_group_lineedit.setText('')
            self.new_event_group_lineedit.setEnabled(False)
            self.new_event_name_lineedit.setText('')
            self.new_event_name_lineedit.setEnabled(False)
            self.event_channel_lineedit.setText('')
            self.event_channel_lineedit.setEnabled(False)


    # To listen to any modification not only when you ask (ping)
    def on_topic_update(self, topic, message, sender):
        pass


    # Called by the publisher to display settings in the SettingsView
    # Information is taken from the publisher to the interface
    def on_topic_response(self, topic, message, sender):
        if topic == self._event1_name_topic:
            self.event1_name_lineedit.setText(message)
        if topic == self._event2_name_topic:
            self.event2_name_lineedit.setText(message)
        if topic == self._channel1_name_topic:
            self.channel1_lineedit.setText(message)
        if topic == self._channel2_name_topic:
            self.channel2_lineedit.setText(message)
        if topic == self._new_event_group_topic:
            if len(message)>0:
                self.rename_checkBox.setChecked(True)
                self.new_event_group_lineedit.setText(message)
        if topic == self._new_event_name_topic:
            if len(message)>0:
                self.rename_checkBox.setChecked(True)
                self.new_event_name_lineedit.setText(message)
        if topic == self._new_event_chan_topic:
            if len(message)>0:
                self.rename_checkBox.setChecked(True)
                self.event_channel_lineedit.setText(message) 
        if topic == self._behavior_topic:
            if message == 'append':
                self._channel_wise = False
                self.chan_wise_checkBox.setChecked(False)
            else:
                self.chan_wise_checkBox.setChecked(True)
            self.on_chan_wise_checkbox()
            self.behavior_comboBox.setCurrentText(message)


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._event1_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._event2_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._channel1_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._channel2_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._new_event_group_topic)
            self._pub_sub_manager.unsubscribe(self, self._new_event_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._new_event_chan_topic)
            self._pub_sub_manager.unsubscribe(self, self._behavior_topic)

