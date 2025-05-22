"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the WindowsToSamples plugin
"""

from qtpy import QtWidgets

from CEAMSModules.WindowsToSamples.Ui_WindowsToSamplesSettingsView import Ui_WindowsToSamplesSettingsView
from commons.BaseSettingsView import BaseSettingsView

class WindowsToSamplesSettingsView( BaseSettingsView,  Ui_WindowsToSamplesSettingsView, QtWidgets.QWidget):
    """
        WindowsToSamplesView set the WindowsToSamples settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._win_step_sec_topic = f'{self._parent_node.identifier}.win_step_sec'
        self._pub_sub_manager.subscribe(self, self._win_step_sec_topic)
        

    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._win_step_sec_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        # Send the settings to the publisher for inputs to WindowsToSamples
        self._pub_sub_manager.publish(self, self._win_step_sec_topic, str(self.win_step_sec_lineedit.text()))
        

    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._win_step_sec_topic:
            self.win_step_sec_lineedit.setText(message)
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._win_step_sec_topic)
            