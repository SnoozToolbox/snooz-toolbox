"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    Settings viewer of the EdfXmlReaderMaster plugin
"""

from qtpy import QtWidgets

from CEAMSModules.EdfXmlReaderMaster.Ui_EdfXmlReaderMasterSettingsView import Ui_EdfXmlReaderMasterSettingsView
from commons.BaseSettingsView import BaseSettingsView

class EdfXmlReaderMasterSettingsView(BaseSettingsView, Ui_EdfXmlReaderMasterSettingsView, QtWidgets.QWidget):
    """
        EdfXmlReaderMasterView set the EdfXmlReaderMaster settings
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
        self._event_name_topic = f'{self._parent_node.identifier}.event_name'
        self._pub_sub_manager.subscribe(self, self._event_name_topic)
        

    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._filename_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event_name_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        # Send the settings to the publisher for inputs to EdfXmlReaderMaster
        self._pub_sub_manager.publish(self, self._filename_topic, str(self.filename_lineedit.text()))
        self._pub_sub_manager.publish(self, self._event_name_topic, str(self.event_name_lineEdit.text()))
        

    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._filename_topic:
            if not message=='':
                self.filename_lineedit.setText(message)
        if topic == self._event_name_topic:
            self.event_name_lineEdit.setText(message)
        

    def on_choose(self):
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(
            None, 
            'Open .XML files', 
            None, 
            '.XML (*.xml)')
        if files != '':
            self.filename_lineedit.setText(str(files))


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._filename_topic)
            self._pub_sub_manager.unsubscribe(self, self._event_name_topic)
            