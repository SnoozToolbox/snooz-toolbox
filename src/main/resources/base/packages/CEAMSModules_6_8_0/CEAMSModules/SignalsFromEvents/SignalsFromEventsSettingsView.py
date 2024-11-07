"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the SignalsFromEvents plugin
"""

from qtpy import QtWidgets

from CEAMSModules.SignalsFromEvents.Ui_SignalsFromEventsSettingsView import Ui_SignalsFromEventsSettingsView
from commons.BaseSettingsView import BaseSettingsView

class SignalsFromEventsSettingsView( BaseSettingsView,  Ui_SignalsFromEventsSettingsView, QtWidgets.QWidget):
    """
        SignalsFromEventsView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        # Subscribe to the proper topics to send/get data from the node
        self._events_names_topic = f'{self._parent_node.identifier}.events_names'
        self._pub_sub_manager.subscribe(self, self._events_names_topic)


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._events_names_topic, 'ping')
        

    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._events_names_topic, \
            str(self.events_names_lineEdit.text()))


    def on_topic_update(self, topic, message, sender):
        pass


    # Called by the publisher to display settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._events_names_topic:
            self.events_names_lineEdit.setText(message)


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._events_names_topic)  
