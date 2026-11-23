"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.

    Settings viewer of the SleepStagingExportResults plugin
"""

from qtpy import QtWidgets

from CEAMSModules.SleepStagingExportResults.Ui_SleepStagingExportResultsSettingsView import Ui_SleepStagingExportResultsSettingsView
from commons.BaseSettingsView import BaseSettingsView

class SleepStagingExportResultsSettingsView(BaseSettingsView, Ui_SleepStagingExportResultsSettingsView, QtWidgets.QWidget):
    """
        SleepStagingExportResultsView set the SleepStagingExportResults settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._ResultsDataframe_topic = f'{self._parent_node.identifier}.ResultsDataframe'
        self._pub_sub_manager.subscribe(self, self._ResultsDataframe_topic)
        self._Additional_topic = f'{self._parent_node.identifier}.info'
        self._pub_sub_manager.subscribe(self, self._Additional_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._ResultsDataframe_topic, 'ping')
        self._pub_sub_manager.publish(self, self._Additional_topic, 'ping')
        


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to SleepStagingExportResults
        self._pub_sub_manager.publish(self, self._ResultsDataframe_topic, str(self.ResultsDataframe_lineedit.text()))
        self._pub_sub_manager.publish(self, self._Additional_topic, str(self.Additional_lineedit.text()))
        


    def on_topic_update(self, topic, message, sender):
        """ Only used in a custom step of a tool, you can ignore it.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._ResultsDataframe_topic:
            self.ResultsDataframe_lineedit.setText(message)
        if topic == self._Additional_topic:
            self.Additional_lineedit.setText(message)
        


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._ResultsDataframe_topic)
            self._pub_sub_manager.unsubscribe(self, self._Additional_topic)
            