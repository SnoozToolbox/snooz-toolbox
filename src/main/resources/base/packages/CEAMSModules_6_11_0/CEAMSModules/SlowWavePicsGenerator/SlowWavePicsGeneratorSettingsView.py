"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.

    Settings viewer of the SlowWavePicsGenerator plugin
"""

from qtpy import QtWidgets

from CEAMSModules.SlowWavePicsGenerator.Ui_SlowWavePicsGeneratorSettingsView import Ui_SlowWavePicsGeneratorSettingsView
from commons.BaseSettingsView import BaseSettingsView

class SlowWavePicsGeneratorSettingsView(BaseSettingsView, Ui_SlowWavePicsGeneratorSettingsView, QtWidgets.QWidget):
    """
        SlowWavePicsGeneratorView set the SlowWavePicsGenerator settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._files_topic = f'{self._parent_node.identifier}.files'
        self._pub_sub_manager.subscribe(self, self._files_topic)
        self._file_group_topic = f'{self._parent_node.identifier}.file_group'
        self._pub_sub_manager.subscribe(self, self._file_group_topic)
        self._sw_char_folder_topic = f'{self._parent_node.identifier}.sw_char_folder'
        self._pub_sub_manager.subscribe(self, self._sw_char_folder_topic)
        self._pics_param_topic = f'{self._parent_node.identifier}.pics_param'
        self._pub_sub_manager.subscribe(self, self._pics_param_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        
        self._pub_sub_manager.publish(self, self._files_topic, 'ping')
        self._pub_sub_manager.publish(self, self._file_group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._sw_char_folder_topic, 'ping')
        self._pub_sub_manager.publish(self, self._pics_param_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        
        # Send the settings to the publisher for inputs to SlowWavePicsGenerator
        self._pub_sub_manager.publish(self, self._files_topic, str(self.files_lineedit.text()))
        self._pub_sub_manager.publish(self, self._file_group_topic, str(self.file_group_lineedit.text()))
        self._pub_sub_manager.publish(self, self._sw_char_folder_topic, str(self.sw_char_folder_lineedit.text()))
        self._pub_sub_manager.publish(self, self._pics_param_topic, str(self.pics_param_lineedit.text()))
        

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """

        if topic == self._files_topic:
            self.files_lineedit.setText(message)
        if topic == self._file_group_topic:
            self.file_group_lineedit.setText(message)
        if topic == self._sw_char_folder_topic:
            self.sw_char_folder_lineedit.setText(message)
        if topic == self._pics_param_topic:
            self.pics_param_lineedit.setText(message)
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._files_topic)
            self._pub_sub_manager.unsubscribe(self, self._file_group_topic)
            self._pub_sub_manager.unsubscribe(self, self._sw_char_folder_topic)
            self._pub_sub_manager.unsubscribe(self, self._pics_param_topic)
            