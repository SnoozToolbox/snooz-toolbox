"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the Resample plugin
"""

from qtpy import QtWidgets

from CEAMSModules.Resample.Ui_ResampleSettingsView import Ui_ResampleSettingsView
from commons.BaseSettingsView import BaseSettingsView

class ResampleSettingsView( BaseSettingsView,  Ui_ResampleSettingsView, QtWidgets.QWidget):
    """
        ResampleView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        self._sample_rate_topic = f'{self._parent_node.identifier}.sample_rate'
        self._pub_sub_manager.subscribe(self, self._sample_rate_topic)

    def load_settings(self):
        self._pub_sub_manager.publish(self, self._sample_rate_topic, 'ping')

    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._sample_rate_topic, self.target_sample_rate_lineedit.text())

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        if topic == self._sample_rate_topic:
            self.target_sample_rate_lineedit.setText(str(message))

    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._sample_rate_topic)