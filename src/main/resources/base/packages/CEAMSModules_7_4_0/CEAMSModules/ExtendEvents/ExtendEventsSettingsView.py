"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    Settings viewer of the ExtendEvents plugin
"""

from qtpy import QtWidgets

from CEAMSModules.ExtendEvents.Ui_ExtendEventsSettingsView import Ui_ExtendEventsSettingsView
from commons.BaseSettingsView import BaseSettingsView

class ExtendEventsSettingsView(BaseSettingsView, Ui_ExtendEventsSettingsView, QtWidgets.QWidget):
    """
        ExtendEventsView set the ExtendEvents settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._events_topic = f'{self._parent_node.identifier}.events'
        self._pub_sub_manager.subscribe(self, self._events_topic)
        self._per_side_exten_percent_topic = f'{self._parent_node.identifier}.per_side_exten_percent'
        self._pub_sub_manager.subscribe(self, self._per_side_exten_percent_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._events_topic, 'ping')
        self._pub_sub_manager.publish(self, self._per_side_exten_percent_topic, 'ping')
        


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to ExtendEvents
        self._pub_sub_manager.publish(self, self._events_topic, str(self.events_lineedit.text()))
        self._pub_sub_manager.publish(self, self._per_side_exten_percent_topic, str(self.per_side_exten_percent_lineedit.text()))
        


    def on_topic_update(self, topic, message, sender):
        """ Only used in a custom step of a tool, you can ignore it.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._events_topic:
            self.events_lineedit.setText(message)
        if topic == self._per_side_exten_percent_topic:
            self.per_side_exten_percent_lineedit.setText(message)
        


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._events_topic)
            self._pub_sub_manager.unsubscribe(self, self._per_side_exten_percent_topic)
            