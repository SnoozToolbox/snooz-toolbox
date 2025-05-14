"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the ResetSignalArtefact plugin
"""

from qtpy import QtWidgets

from CEAMSModules.ResetSignalArtefact.Ui_ResetSignalArtefactSettingsView import Ui_ResetSignalArtefactSettingsView
from commons.BaseSettingsView import BaseSettingsView

class ResetSignalArtefactSettingsView( BaseSettingsView,  Ui_ResetSignalArtefactSettingsView, QtWidgets.QWidget):
    """
        ResetSignalArtefactView set the ResetSignalArtefact settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._artefact_group_topic = f'{self._parent_node.identifier}.artefact_group'
        self._pub_sub_manager.subscribe(self, self._artefact_group_topic)
        self._artefact_name_topic = f'{self._parent_node.identifier}.artefact_name'
        self._pub_sub_manager.subscribe(self, self._artefact_name_topic)
        self._signal_values_topic = f'{self._parent_node.identifier}.signal_values'
        self._pub_sub_manager.subscribe(self, self._signal_values_topic)
        

    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._artefact_group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._artefact_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._signal_values_topic, 'ping')


    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        # Send the settings to the publisher for inputs to ResetSignalArtefact
        self._pub_sub_manager.publish(self, self._artefact_group_topic, str(self.artefact_group_lineedit.text()))
        self._pub_sub_manager.publish(self, self._artefact_name_topic, str(self.artefact_name_lineedit.text()))
        self._pub_sub_manager.publish(self, self._signal_values_topic, str(self.signal_value_comboBox.currentText()))
        

    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._artefact_group_topic:
            self.artefact_group_lineedit.setText(message)
        if topic == self._artefact_name_topic:
            self.artefact_name_lineedit.setText(message)
        if topic == self._signal_values_topic:
            self.signal_value_comboBox.setCurrentText(message)


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._artefact_group_topic)
            self._pub_sub_manager.unsubscribe(self, self._artefact_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._signal_values_topic)
            