"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the IcaRestore plugin
"""

import numpy as np
from qtpy import QtWidgets

from CEAMSModules.IcaRestore.Ui_IcaRestoreSettingsView import Ui_IcaRestoreSettingsView
from commons.BaseSettingsView import BaseSettingsView

class IcaRestoreSettingsView( BaseSettingsView,  Ui_IcaRestoreSettingsView, QtWidgets.QWidget):
    """
        IcaRestoreView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        
    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        pass        

    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        pass
        
    def on_topic_update(self, topic, message, sender):
        pass

    # Called by the publisher to display settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        pass
     
    # Called when the user delete an instance of the plugin
    def __del__(self):
        pass
 