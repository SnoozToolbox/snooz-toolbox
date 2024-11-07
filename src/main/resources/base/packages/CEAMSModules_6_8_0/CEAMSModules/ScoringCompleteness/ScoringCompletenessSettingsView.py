"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    Settings viewer of the ScoringCompleteness plugin
"""

from qtpy import QtWidgets

from CEAMSModules.ScoringCompleteness.Ui_ScoringCompletenessSettingsView import Ui_ScoringCompletenessSettingsView
from commons.BaseSettingsView import BaseSettingsView

class ScoringCompletenessSettingsView( BaseSettingsView,  Ui_ScoringCompletenessSettingsView, QtWidgets.QWidget):
    """
        ScoringCompletenessView set the ScoringCompleteness settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._output_file_topic = f'{self._parent_node.identifier}.output_file'
        self._pub_sub_manager.subscribe(self, self._output_file_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._output_file_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        # Send the settings to the publisher for inputs to ScoringCompleteness
        self._pub_sub_manager.publish(self, self._output_file_topic, str(self.output_file_lineedit.text()))
        

    def on_choose(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, 
            'Save as tsv file', 
            None, 
            'Tab Separated Values (*.tsv)')
        if filename != '':
            self.output_file_lineedit.setText(filename)


    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._output_file_topic:
            self.output_file_lineedit.setText(message)
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._output_file_topic)
            