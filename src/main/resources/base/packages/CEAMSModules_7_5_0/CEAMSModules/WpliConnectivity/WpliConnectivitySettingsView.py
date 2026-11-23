"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.

    Settings viewer of the WpliConnectivity plugin
"""

from qtpy import QtWidgets

from CEAMSModules.WpliConnectivity.Ui_WpliConnectivitySettingsView import Ui_WpliConnectivitySettingsView
from commons.BaseSettingsView import BaseSettingsView

class WpliConnectivitySettingsView(BaseSettingsView, Ui_WpliConnectivitySettingsView, QtWidgets.QWidget):
    """
        WpliConnectivityView set the WpliConnectivity settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._signals_topic = f'{self._parent_node.identifier}.signals'
        self._pub_sub_manager.subscribe(self, self._signals_topic)
        self._events_topic = f'{self._parent_node.identifier}.events'
        self._pub_sub_manager.subscribe(self, self._events_topic)
        self._num_surr_topic = f'{self._parent_node.identifier}.num_surr'
        self._pub_sub_manager.subscribe(self, self._num_surr_topic)
        self._p_value_topic = f'{self._parent_node.identifier}.p_value'
        self._pub_sub_manager.subscribe(self, self._p_value_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        
        self._pub_sub_manager.publish(self, self._signals_topic, 'ping')
        self._pub_sub_manager.publish(self, self._events_topic, 'ping')
        self._pub_sub_manager.publish(self, self._num_surr_topic, 'ping')
        self._pub_sub_manager.publish(self, self._p_value_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        
        # Send the settings to the publisher for inputs to WpliConnectivity
        # self._pub_sub_manager.publish(self, self._signals_topic, str(self.signals_lineedit.text()))
        # self._pub_sub_manager.publish(self, self._events_topic, str(self.events_lineedit.text()))
        self._pub_sub_manager.publish(self, self._num_surr_topic, str(self.num_surr_lineedit.text()))
        self._pub_sub_manager.publish(self, self._p_value_topic, str(self.p_value_lineedit.text()))
        

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """

        # if topic == self._signals_topic:
        #     self.signals_lineedit.setText(message)
        # if topic == self._events_topic:
        #     self.events_lineedit.setText(message)
        if topic == self._num_surr_topic:
            self.num_surr_lineedit.setText(message)
        if topic == self._p_value_topic:
            self.p_value_lineedit.setText(message)
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._signals_topic)
            self._pub_sub_manager.unsubscribe(self, self._events_topic)
            self._pub_sub_manager.unsubscribe(self, self._num_surr_topic)
            self._pub_sub_manager.unsubscribe(self, self._p_value_topic)
            