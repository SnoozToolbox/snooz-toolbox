"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    Settings viewer of the PSACompilation plugin
"""

from qtpy import QtWidgets

from CEAMSModules.PSACompilation.Ui_PSACompilationSettingsView import Ui_PSACompilationSettingsView
from commons.BaseSettingsView import BaseSettingsView

class PSACompilationSettingsView(BaseSettingsView, Ui_PSACompilationSettingsView, QtWidgets.QWidget):
    """
        PSACompilationView set the PSACompilation settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._filename_topic = f'{self._parent_node.identifier}.filename'
        self._pub_sub_manager.subscribe(self, self._filename_topic)        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._filename_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        # Send the settings to the publisher for inputs to PSACompilation
        self._pub_sub_manager.publish(self, self._filename_topic, str(self.filename_lineedit.text()))
        

    def on_topic_update(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
            at any update, does not necessary answer to a ping.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
            Called after a ping.
        """
        if topic == self._filename_topic:
            self.filename_lineedit.setText(message)
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._filename_topic)
        
        
    # Called when the user press the choose puch button
    def choose_button_slot(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save file as', "", "TSV (*.tsv)")
        if filename is not None and filename:
            if not filename.endswith(".tsv"):
                filename = filename + ".tsv"
            self.filename_lineedit.setText(filename)
        else:
            return
