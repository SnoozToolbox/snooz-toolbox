"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
from qtpy import QtWidgets

DEBUG = False

class QCheckBoxLive(QtWidgets.QCheckBox):
    def __init__(self, parent):
        super().__init__(parent)
        self._target_identifier = None
        self._target_field_name = None
        self._topic = None
        self._pub_sub_manager = None

    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._topic)

    def init(self, target_identifier, target_field_name, pub_sub_manager):
        self._target_identifier = target_identifier
        self._target_field_name = target_field_name
        self._topic = f'{self._target_identifier}.{self._target_field_name}'
        self._pub_sub_manager = pub_sub_manager
        self._pub_sub_manager.subscribe(self, self._topic)
        self.stateChanged.connect(self.on_state_changed)
        # Call ping to request the value to be published by NodePortGraphicsItem
        self._pub_sub_manager.publish(self, self._topic, 'ping')

    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'QComboBoxLive.on_topic_update:{topic}{message}')

    def on_topic_response(self, topic, message, sender):
        if DEBUG: print(f'QComboBoxLive.on_topic_response:{topic}{message}')
        if message:
            self.stateChanged.disconnect(self.on_state_changed)
            super().setChecked(message=='True')
            self.stateChanged.connect(self.on_state_changed)

    def on_state_changed(self, state):
        if DEBUG: print(f'QComboBoxLive.on_state_changed:{state}')
        if self._pub_sub_manager is not None:
            pass
            self._pub_sub_manager.publish(self, self._topic, str(bool(state)))
