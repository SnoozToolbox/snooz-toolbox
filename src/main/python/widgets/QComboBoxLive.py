"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from qtpy import QtWidgets

DEBUG = False

class QComboBoxLive(QtWidgets.QComboBox):
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
        self.currentTextChanged.connect(self.on_text_changed)
        # Call ping to request the value to be published by NodePortGraphicsItem
        self._pub_sub_manager.publish(self, self._topic, 'ping')

    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'QComboBoxLive.on_topic_update:{topic}{message}')

    def on_topic_response(self, topic, message, sender):
        if DEBUG: print(f'QComboBoxLive.on_topic_response:{topic}{message}')
        if message:
            self.currentTextChanged.disconnect(self.on_text_changed)
            super().setCurrentText(message)
            self.currentTextChanged.connect(self.on_text_changed)

    def on_text_changed(self, text):
        if DEBUG: print(f'QComboBoxLive.on_text_changed:{text}')
        if self._pub_sub_manager is not None:
            pass
            self._pub_sub_manager.publish(self, self._topic, text)
        
        

