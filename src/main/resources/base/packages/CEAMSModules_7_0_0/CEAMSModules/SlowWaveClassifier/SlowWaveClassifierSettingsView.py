"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    Settings viewer of the SlowWaveClassifier plugin
"""

from qtpy import QtWidgets

from CEAMSModules.SlowWaveClassifier.Ui_SlowWaveClassifierSettingsView import Ui_SlowWaveClassifierSettingsView
from commons.BaseSettingsView import BaseSettingsView

class SlowWaveClassifierSettingsView( BaseSettingsView,  Ui_SlowWaveClassifierSettingsView, QtWidgets.QWidget):
    """
        SlowWaveClassifierView set the SlowWaveClassifier settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._automatic_classification_topic = f'{self._parent_node.identifier}.automatic_classification'
        self._pub_sub_manager.subscribe(self, self._automatic_classification_topic)
        self._num_categories_topic = f'{self._parent_node.identifier}.num_categories'
        self._pub_sub_manager.subscribe(self, self._num_categories_topic)
        

    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        
        self._pub_sub_manager.publish(self, self._automatic_classification_topic, 'ping')
        self._pub_sub_manager.publish(self, self._num_categories_topic, 'ping')


    # Slot called when user changes the checkbox to activate age or sex parameters
    def on_input_format_changed(self, int):
        if self.automatic_classification_checkBox.isChecked():
            self.num_categories_spinBox.setEnabled(False)
            self.categories_label.setEnabled(False)
        else:
            self.num_categories_spinBox.setEnabled(True)
            self.categories_label.setEnabled(True)


    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        
        # Send the settings to the publisher for inputs to SlowWaveClassifier
        self._pub_sub_manager.publish(self, self._automatic_classification_topic, str(self.automatic_classification_checkBox.isChecked()))
        self._pub_sub_manager.publish(self, self._num_categories_topic, str(self.num_categories_spinBox.value()))
        

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """

        if topic == self._automatic_classification_topic:
            self.automatic_classification_checkBox.setChecked(eval(message))
        if topic == self._num_categories_topic:
            self.num_categories_spinBox.setValue(int(message))
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._automatic_classification_topic)
            self._pub_sub_manager.unsubscribe(self, self._num_categories_topic)
            