"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    Settings viewer of the CreateTuple plugin
"""

from qtpy import QtWidgets

from CEAMSModules.CreateTuple.Ui_CreateTupleSettingsView import Ui_CreateTupleSettingsView
from commons.BaseSettingsView import BaseSettingsView

class CreateTupleSettingsView(BaseSettingsView, Ui_CreateTupleSettingsView, QtWidgets.QWidget):
    """
        CreateTupleView set the CreateTuple settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._Idx0_topic = f'{self._parent_node.identifier}.Idx0'
        self._pub_sub_manager.subscribe(self, self._Idx0_topic)
        self._Idx1_topic = f'{self._parent_node.identifier}.Idx1'
        self._pub_sub_manager.subscribe(self, self._Idx1_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._Idx0_topic, 'ping')
        self._pub_sub_manager.publish(self, self._Idx1_topic, 'ping')
        


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to CreateTuple
        self._pub_sub_manager.publish(self, self._Idx0_topic, str(self.Idx0_lineedit.text()))
        self._pub_sub_manager.publish(self, self._Idx1_topic, str(self.Idx1_lineedit.text()))
        


    def on_topic_update(self, topic, message, sender):
        """ Only used in a custom step of a tool, you can ignore it.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._Idx0_topic:
            self.Idx0_lineedit.setText(message)
        if topic == self._Idx1_topic:
            self.Idx1_lineedit.setText(message)
        


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._Idx0_topic)
            self._pub_sub_manager.unsubscribe(self, self._Idx1_topic)
            