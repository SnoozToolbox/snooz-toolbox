"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the EventCreator plugin
"""

from qtpy import QtWidgets

from CEAMSModules.EventCreator.Ui_EventCreatorSettingsView import Ui_EventCreatorSettingsView
from commons.BaseSettingsView import BaseSettingsView

class EventCreatorSettingsView( BaseSettingsView,  Ui_EventCreatorSettingsView, QtWidgets.QWidget):
    """
        EventCreatorView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        self._settings = {
            f'{parent_node.identifier}.event_name': self.event_name_lineedit,
            f'{parent_node.identifier}.start_time': self.start_time_lineedit,
            f'{parent_node.identifier}.duration': self.duration_lineedit,
            f'{parent_node.identifier}.group_name': self.group_name_lineedit,
            f'{parent_node.identifier}.channels': self.channels_lineedit,
        }
        for topic in self._settings:
            self._pub_sub_manager.subscribe(self, topic)


    def load_settings(self):
        for topic in self._settings:
            self._pub_sub_manager.publish(self, topic, 'ping')

    def on_apply_settings(self):
        for topic, widget in self._settings.items():
            self._pub_sub_manager.publish(self, topic, widget.text())

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        self._settings[topic].setText(str(message))

    def __del__(self):
        if self._pub_sub_manager is not None:
            for topic in self._settings:
                self._pub_sub_manager.unsubscribe(self, topic)