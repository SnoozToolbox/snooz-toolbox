"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the StringManip plugin
"""

from qtpy import QtWidgets

from CEAMSModules.StringManip.Ui_StringManipSettingsView import Ui_StringManipSettingsView
from commons.BaseSettingsView import BaseSettingsView

DEBUG = True

class StringManipSettingsView( BaseSettingsView,  Ui_StringManipSettingsView, QtWidgets.QWidget):
    """
        StringManipView set the StringManip settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        # Subscribe to the proper topics to send/get data from the node
        self._prefix_topic = f'{self._parent_node.identifier}.prefix'
        self._pub_sub_manager.subscribe(self, self._prefix_topic)
        self._suffix_topic = f'{self._parent_node.identifier}.suffix'
        self._pub_sub_manager.subscribe(self, self._suffix_topic)
        self._file_rm_topic = f'{self._parent_node.identifier}.filename_rm'
        self._pub_sub_manager.subscribe(self, self._file_rm_topic)
        self._path_rm_topic = f'{self._parent_node.identifier}.path_rm'
        self._pub_sub_manager.subscribe(self, self._path_rm_topic)
        self._file_ext_rm_topic = f'{self._parent_node.identifier}.file_ext_rm'
        self._pub_sub_manager.subscribe(self, self._file_ext_rm_topic)
        

    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._prefix_topic, 'ping')
        self._pub_sub_manager.publish(self, self._suffix_topic, 'ping')
        self._pub_sub_manager.publish(self, self._file_rm_topic, 'ping')
        self._pub_sub_manager.publish(self, self._path_rm_topic, 'ping')
        self._pub_sub_manager.publish(self, self._file_ext_rm_topic, 'ping')


    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        # Send the settings to the publisher for inputs to CsvReaderMaster
        self._pub_sub_manager.publish(self, self._prefix_topic, \
            str(self.prefix_lineedit.text()))
        self._pub_sub_manager.publish(self, self._suffix_topic, \
            str(self.suffix_lineedit.text()))
        self._pub_sub_manager.publish(self, self._file_rm_topic, \
            str(int(self.filename_rm_checkBox.isChecked())))
        self._pub_sub_manager.publish(self, self._path_rm_topic, \
            str(int(self.path_rm_checkBox.isChecked())))
        self._pub_sub_manager.publish(self, self._file_ext_rm_topic, \
            str(int(self.ext_rm_checkBox.isChecked())))

    def on_topic_update(self, topic, message, sender):
        pass

    # Called by the publisher to init settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if DEBUG: print(f'CsvReaderMasterSettingsView.on_topic_update:{topic} message:{message}')
        if topic == self._prefix_topic:
            self.prefix_lineedit.setText(message)
        if topic == self._suffix_topic:
            self.suffix_lineedit.setText(message)
        if topic == self._file_rm_topic:
            self.filename_rm_checkBox.setChecked(int(message))
        if topic == self._path_rm_topic:
            self.path_rm_checkBox.setChecked(int(message))
        if topic == self._file_ext_rm_topic:
            self.ext_rm_checkBox.setChecked(int(message))


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._prefix_topic)
            self._pub_sub_manager.unsubscribe(self, self._suffix_topic)
            self._pub_sub_manager.unsubscribe(self, self._file_rm_topic)
            self._pub_sub_manager.unsubscribe(self, self._path_rm_topic)
            self._pub_sub_manager.unsubscribe(self, self._file_ext_rm_topic)