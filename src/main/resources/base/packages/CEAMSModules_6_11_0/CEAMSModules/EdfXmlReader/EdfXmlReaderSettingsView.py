"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the EdfXmlReader plugin
"""

from qtpy import QtWidgets

from CEAMSModules.EdfXmlReader.Ui_EdfXmlReaderSettingsView import Ui_EdfXmlReaderSettingsView
from commons.BaseSettingsView import BaseSettingsView

class EdfXmlReaderSettingsView( BaseSettingsView,  Ui_EdfXmlReaderSettingsView, QtWidgets.QWidget):
    """
        EdfXmlReaderView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
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
    

    def on_choose(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, 
            'Open .XML file', 
            None, 
            '.XML (*.xml)')
        if filename != '':
            self.filename_lineedit.setText(filename)


    def load_settings(self):
        self._pub_sub_manager.publish(self, self._filename_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event_name_topic, 'ping')


    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._filename_topic:
            self.filename_lineedit.setText(message)
        if topic == self._event_name_topic:
            self.event_name_lineEdit.setText(message)


    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        # Send the settings to the publisher for inputs to EdfXmlReaderMaster
        self._pub_sub_manager.publish(self, self._filename_topic, str(self.filename_lineedit.text()))
        self._pub_sub_manager.publish(self, self._event_name_topic, str(self.event_name_lineEdit.text()))