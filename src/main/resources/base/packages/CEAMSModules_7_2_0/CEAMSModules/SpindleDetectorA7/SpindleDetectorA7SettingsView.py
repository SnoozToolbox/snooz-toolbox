"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    Settings viewer of the SpindleDetectorA7 plugin
    There is no settings in the SpindleDetectorA7 plugin
    The detector is always used in a process and a custom step is used to define the settings
"""

from qtpy import QtWidgets

from CEAMSModules.SpindleDetectorA7.Ui_SpindleDetectorA7SettingsView import Ui_SpindleDetectorA7SettingsView
from commons.BaseSettingsView import BaseSettingsView

class SpindleDetectorA7SettingsView(BaseSettingsView, Ui_SpindleDetectorA7SettingsView, QtWidgets.QWidget):
    """
        SpindleDetectorA7View set the SpindleDetectorA7 settings
        The detector is always used in a process and a custom step is used to define the settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        # init UI
        self.setupUi(self)


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        pass
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        pass
        

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        pass
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        pass