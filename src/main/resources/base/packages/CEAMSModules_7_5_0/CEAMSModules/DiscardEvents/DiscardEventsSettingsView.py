"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the DiscardEvents plugin
"""

from qtpy import QtWidgets

from CEAMSModules.DiscardEvents.Ui_DiscardEventsSettingsView import Ui_DiscardEventsSettingsView
from commons.BaseSettingsView import BaseSettingsView

class DiscardEventsSettingsView( BaseSettingsView,  Ui_DiscardEventsSettingsView, QtWidgets.QWidget):
    """
        DiscardEventsView set the DiscardEvents settings
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
        self._min_len_sec_topic = f'{self._parent_node.identifier}.min_len_sec'
        self._pub_sub_manager.subscribe(self, self._min_len_sec_topic)
        self._max_len_sec_topic = f'{self._parent_node.identifier}.max_len_sec'
        self._pub_sub_manager.subscribe(self, self._max_len_sec_topic)
        self._artefact_free_topic = f'{self._parent_node.identifier}.artefact_free'
        self._pub_sub_manager.subscribe(self, self._artefact_free_topic)
        self._artefact_group_topic = f'{self._parent_node.identifier}.artefact_group'
        self._pub_sub_manager.subscribe(self, self._artefact_group_topic)
        self._artefact_name_topic = f'{self._parent_node.identifier}.artefact_name'
        self._pub_sub_manager.subscribe(self, self._artefact_name_topic)


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._event_group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._min_len_sec_topic, 'ping')
        self._pub_sub_manager.publish(self, self._max_len_sec_topic, 'ping')
        self._pub_sub_manager.publish(self, self._artefact_free_topic, 'ping')
        self._pub_sub_manager.publish(self, self._artefact_group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._artefact_name_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        # Send the settings to the publisher for inputs to DiscardEvents
        self._pub_sub_manager.publish(self, self._event_group_topic, str(self.event_group_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._event_name_topic, str(self.event_name_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._min_len_sec_topic, str(self.min_len_sec_lineedit.text()))
        self._pub_sub_manager.publish(self, self._max_len_sec_topic, str(self.max_len_sec_lineedit.text()))
        self._pub_sub_manager.publish(self, self._artefact_free_topic, str(int(self.artefact_free_checkBox.isChecked())))
        self._pub_sub_manager.publish(self, self._artefact_group_topic, str(self.artefact_group_lineedit.text()))
        self._pub_sub_manager.publish(self, self._artefact_name_topic, str(self.artefact_name_lineedit.text()))
        

    def on_artefact_free_check(self):
        """ Called when the user checked or unchecked artefact free checkbox.
        """        
        if self.artefact_free_checkBox.isChecked():
            self.artefact_group_lineedit.setEnabled(True)
            self.artefact_name_lineedit.setEnabled(True)
        else:
            self.artefact_group_lineedit.setEnabled(False)
            self.artefact_name_lineedit.setEnabled(False)            


    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._event_group_topic:
            self.event_group_lineEdit.setText(message)
        if topic == self._event_name_topic:
            self.event_name_lineEdit.setText(message)
        if topic == self._min_len_sec_topic:
            self.min_len_sec_lineedit.setText(message)
        if topic == self._max_len_sec_topic:
            self.max_len_sec_lineedit.setText(message)
        if topic == self._artefact_free_topic:
            self.artefact_free_checkBox.setChecked(int(message))
        if topic == self._artefact_group_topic:
            self.artefact_group_lineedit.setText(message)
        if topic == self._artefact_name_topic:
            self.artefact_name_lineedit.setText(message)
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._event_group_topic)
            self._pub_sub_manager.unsubscribe(self, self._event_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._min_len_sec_topic)
            self._pub_sub_manager.unsubscribe(self, self._max_len_sec_topic)
            self._pub_sub_manager.unsubscribe(self, self._artefact_free_topic)
            self._pub_sub_manager.unsubscribe(self, self._artefact_group_topic)
            self._pub_sub_manager.unsubscribe(self, self._artefact_name_topic)
            