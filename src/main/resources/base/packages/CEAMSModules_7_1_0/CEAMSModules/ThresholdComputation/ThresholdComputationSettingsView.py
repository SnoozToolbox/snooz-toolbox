"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the ThresholdComputation plugin
"""

from re import L
from qtpy import QtWidgets

from CEAMSModules.ThresholdComputation.Ui_ThresholdComputationSettingsView import Ui_ThresholdComputationSettingsView
from commons.BaseSettingsView import BaseSettingsView

class ThresholdComputationSettingsView( BaseSettingsView,  Ui_ThresholdComputationSettingsView, QtWidgets.QWidget):
    """
        ThresholdComputationView set the ThresholdComputation settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._threshold_definition_topic = f'{self._parent_node.identifier}.threshold_definition'
        self._pub_sub_manager.subscribe(self, self._threshold_definition_topic)
        self._threshold_metric_topic = f'{self._parent_node.identifier}.threshold_metric'
        self._pub_sub_manager.subscribe(self, self._threshold_metric_topic)
        self._threshold_scope_topic = f'{self._parent_node.identifier}.threshold_scope'
        self._pub_sub_manager.subscribe(self, self._threshold_scope_topic)

        self._threshold_scope = '0'


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._threshold_definition_topic, 'ping')
        self._pub_sub_manager.publish(self, self._threshold_metric_topic, 'ping')
        self._pub_sub_manager.publish(self, self._threshold_scope_topic, 'ping')


    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        # Send the settings to the publisher for inputs to ThresholdComputation
        self._pub_sub_manager.publish(self, self._threshold_definition_topic, \
            str(self.threshold_definition_lineedit.text()))
        self._pub_sub_manager.publish(self, self._threshold_metric_topic, \
            str(self.unit_comboBox.currentText()))
        self._pub_sub_manager.publish(self, self._threshold_scope_topic, \
            str(self._threshold_scope))


    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._threshold_definition_topic:
            self.threshold_definition_lineedit.setText(message)
        if topic == self._threshold_metric_topic:
            self.unit_comboBox.setCurrentText(message)
        if topic == self._threshold_scope_topic:
            self._threshold_scope = message
            if message=='0':
                self.thresh_signal_radioButton.setChecked(True)
            elif message=='1':
                self.thresh_cycle_radioButton.setChecked(True)
            elif message=='2':
                self.thresh_channel_radioButton.setChecked(True)


    # Called when the user touch the radio button
    def on_settings_changed(self):
        if self.thresh_signal_radioButton.isChecked():
            self._threshold_scope = '0'
        elif self.thresh_cycle_radioButton.isChecked():
            self._threshold_scope = '1'            
        elif self.thresh_channel_radioButton.isChecked():
            self._threshold_scope = '2'   


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._threshold_definition_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_metric_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_scope_topic)
