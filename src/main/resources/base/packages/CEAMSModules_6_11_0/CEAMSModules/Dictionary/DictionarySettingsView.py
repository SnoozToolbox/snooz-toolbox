"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the Dictionary plugin
"""

from qtpy import QtWidgets

from CEAMSModules.Dictionary.Ui_DictionarySettingsView import Ui_DictionarySettingsView
from commons.BaseSettingsView import BaseSettingsView

class DictionarySettingsView( Ui_DictionarySettingsView,  BaseSettingsView, QtWidgets.QWidget):
    """
        DictionaryView set the Dictionary settings
    """
    def __init__(self, parent_node, pub_sub_manager, *args, options=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._key_topic = f'{self._parent_node.identifier}.key'
        self._pub_sub_manager.subscribe(self, self._key_topic)
        self._dictionary_topic = f'{self._parent_node.identifier}.dictionary'
        self._pub_sub_manager.subscribe(self, self._dictionary_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        
        self._pub_sub_manager.publish(self, self._key_topic, 'ping')
        self._pub_sub_manager.publish(self, self._dictionary_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        
        # Send the settings to the publisher for inputs to Dictionary
        self._pub_sub_manager.publish(self, self._key_topic, str(self.key_lineedit.text()))
        self._pub_sub_manager.publish(self, self._dictionary_topic, str(self.dictionary_lineedit.text()))
        

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """

        if topic == self._key_topic:
            self.key_lineedit.setText(message)
        if topic == self._dictionary_topic:
            self.dictionary_lineedit.setText(message)
        