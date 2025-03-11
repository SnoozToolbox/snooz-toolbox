"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the A4PreciseEvents plugin
"""

from qtpy import QtWidgets

from CEAMSModules.A4PreciseEvents.Ui_A4PreciseEventsSettingsView import Ui_A4PreciseEventsSettingsView
from commons.BaseSettingsView import BaseSettingsView

class A4PreciseEventsSettingsView( BaseSettingsView,  Ui_A4PreciseEventsSettingsView, QtWidgets.QWidget):
    """
        A4PreciseEventsView set the A4PreciseEvents settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._win_len_sec_topic = f'{self._parent_node.identifier}.win_len_sec'
        self._pub_sub_manager.subscribe(self, self._win_len_sec_topic)
        self._len_adjust_sec_topic = f'{self._parent_node.identifier}.len_adjust_sec'
        self._pub_sub_manager.subscribe(self, self._len_adjust_sec_topic)

        self._event_group_topic = f'{self._parent_node.identifier}.event_group'
        self._pub_sub_manager.subscribe(self, self._event_group_topic)
        self._event_name_topic = f'{self._parent_node.identifier}.event_name'
        self._pub_sub_manager.subscribe(self, self._event_name_topic)

        self._min_len_sec_topic = f'{self._parent_node.identifier}.min_len_sec'
        self._pub_sub_manager.subscribe(self, self._min_len_sec_topic)
        self._max_len_sec_topic = f'{self._parent_node.identifier}.max_len_sec'
        self._pub_sub_manager.subscribe(self, self._max_len_sec_topic)
        
        
    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._win_len_sec_topic, 'ping')
        self._pub_sub_manager.publish(self, self._len_adjust_sec_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event_group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._min_len_sec_topic, 'ping')
        self._pub_sub_manager.publish(self, self._max_len_sec_topic, 'ping')        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        # Send the settings to the publisher for inputs to A4PreciseEvents
        self._pub_sub_manager.publish(self, self._win_len_sec_topic, str(self.win_len_sec_lineedit.text()))
        self._pub_sub_manager.publish(self, self._len_adjust_sec_topic, str(self.len_adjust_sec_lineedit.text()))
        self._pub_sub_manager.publish(self, self._event_group_topic, str(self.group_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._event_name_topic, str(self.name_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._min_len_sec_topic, str(self.min_dur_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._max_len_sec_topic, str(self.max_dur_lineEdit.text()))
        

    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._win_len_sec_topic:
            self.win_len_sec_lineedit.setText(message)
        if topic == self._len_adjust_sec_topic:
            self.len_adjust_sec_lineedit.setText(message)
        if topic == self._event_group_topic:
            self.group_lineEdit.setText(message)
        if topic == self._event_name_topic:
            self.name_lineEdit.setText(message)
        if topic == self._min_len_sec_topic:
            self.min_dur_lineEdit.setText(message)
        if topic == self._max_len_sec_topic:
            self.max_dur_lineEdit.setText(message)
                

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._win_len_sec_topic)
            self._pub_sub_manager.unsubscribe(self, self._len_adjust_sec_topic)
            self._pub_sub_manager.unsubscribe(self, self._event_group_topic)
            self._pub_sub_manager.unsubscribe(self, self._event_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._min_len_sec_topic)
            self._pub_sub_manager.unsubscribe(self, self._max_len_sec_topic)            