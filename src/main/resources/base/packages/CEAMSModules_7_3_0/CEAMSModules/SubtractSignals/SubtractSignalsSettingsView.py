"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the SubtractSignals plugin
"""

from qtpy import QtWidgets

from CEAMSModules.SubtractSignals.Ui_SubtractSignalsSettingsView import Ui_SubtractSignalsSettingsView
from commons.BaseSettingsView import BaseSettingsView

class SubtractSignalsSettingsView( BaseSettingsView,  Ui_SubtractSignalsSettingsView, QtWidgets.QWidget):
    """
        SubtractSignalsView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        # Subscribe to the proper topics to send/get data from the node
        self._channel_topic = f'{self._parent_node.identifier}.channel'
        self._pub_sub_manager.subscribe(self, self._channel_topic)
        self._channel_to_sub_topic = f'{self._parent_node.identifier}.channel_to_sub'
        self._pub_sub_manager.subscribe(self, self._channel_to_sub_topic)
        self._new_chan_name_topic = f'{self._parent_node.identifier}.new_channel_name'
        self._pub_sub_manager.subscribe(self, self._new_chan_name_topic)


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._channel_topic, 'ping')
        self._pub_sub_manager.publish(self, self._channel_to_sub_topic, 'ping')
        self._pub_sub_manager.publish(self, self._new_chan_name_topic, 'ping')


    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._channel_topic, \
            str(self.channel_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._channel_to_sub_topic, \
            str(self.channel_to_sub_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._new_chan_name_topic, \
            str(self.new_chan_name_lineEdit.text()))


    def on_topic_update(self, topic, message, sender):
        pass


    # Called by the publisher to display settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._channel_topic:
            self.channel_lineEdit.setText(str(message))
        if topic == self._channel_to_sub_topic:
            self.channel_to_sub_lineEdit.setText(str(message))
        if topic == self._new_chan_name_topic:
            self.new_chan_name_lineEdit.setText(str(message))


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._channel_topic)
            self._pub_sub_manager.unsubscribe(self, self._channel_to_sub_topic)
            self._pub_sub_manager.unsubscribe(self, self._new_chan_name_topic)