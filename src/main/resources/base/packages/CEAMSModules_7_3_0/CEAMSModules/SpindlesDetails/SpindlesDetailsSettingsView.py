"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    Settings viewer of the SpindlesDetails plugin
"""

from qtpy import QtWidgets

from CEAMSModules.SpindlesDetails.Ui_SpindlesDetailsSettingsView import Ui_SpindlesDetailsSettingsView
from commons.BaseSettingsView import BaseSettingsView

class SpindlesDetailsSettingsView(BaseSettingsView, Ui_SpindlesDetailsSettingsView, QtWidgets.QWidget):
    """
        SpindlesDetailsView set the SpindlesDetails settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._details_filename_topic = f'{self._parent_node.identifier}.details_filename'
        self._pub_sub_manager.subscribe(self, self._details_filename_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._details_filename_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        # Send the settings to the publisher for inputs to SpindlesDetails
        self._pub_sub_manager.publish(self, self._details_filename_topic, str(self.details_filename_lineedit.text()))
        

    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._details_filename_topic:
            self.details_filename_lineedit.setText(message)
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._details_filename_topic)
            return
        

    # Called when the user click on the browse push button
    def browse_slot(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, 
            'Save as TSV file', 
            None, 
            'TSV (*.tsv)')
        if filename != '':
            self.details_filename_lineedit.setText(filename)
