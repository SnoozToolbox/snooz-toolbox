"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the EventCompare plugin
"""

from qtpy import QtWidgets

from CEAMSModules.EventCompare.Ui_EventCompareSettingsView import Ui_EventCompareSettingsView
from commons.BaseSettingsView import BaseSettingsView

DEBUG = False

class EventCompareSettingsView( BaseSettingsView,  Ui_EventCompareSettingsView, QtWidgets.QWidget):
    """
        EventCompareView displays the performance evaluation.
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
        self._label_topic = f'{self._parent_node.identifier}.label'
        self._pub_sub_manager.subscribe(self, self._label_topic)
        self._event1_name_topic = f'{self._parent_node.identifier}.event1_name'
        self._pub_sub_manager.subscribe(self, self._event1_name_topic)
        self._event2_name_topic = f'{self._parent_node.identifier}.event2_name'
        self._pub_sub_manager.subscribe(self, self._event2_name_topic)
        self._channel1_name_topic = f'{self._parent_node.identifier}.channel1_name'
        self._pub_sub_manager.subscribe(self, self._channel1_name_topic)    
        self._channel2_name_topic = f'{self._parent_node.identifier}.channel2_name'
        self._pub_sub_manager.subscribe(self, self._channel2_name_topic)       
        self._jaccord_thresh_topic = f'{self._parent_node.identifier}.jaccord_thresh'
        self._pub_sub_manager.subscribe(self, self._jaccord_thresh_topic)        


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._filename_topic, 'ping')
        self._pub_sub_manager.publish(self, self._label_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event1_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event2_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._channel1_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._channel2_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._jaccord_thresh_topic, 'ping')


    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        # Send the settings to the publisher for an input to EventCompare
        self._pub_sub_manager.publish(self, self._filename_topic, self.filename_lineEdit.text())
        self._pub_sub_manager.publish(self, self._label_topic, self.label_lineEdit.text())
        self._pub_sub_manager.publish(self, self._event1_name_topic, self.event1_name_lineedit.text())
        self._pub_sub_manager.publish(self, self._event2_name_topic, self.event2_name_lineedit.text())
        self._pub_sub_manager.publish(self, self._channel1_name_topic, self.channel1_lineedit.text())
        self._pub_sub_manager.publish(self, self._channel2_name_topic, self.channel2_lineedit.text())
        self._pub_sub_manager.publish(self, self._jaccord_thresh_topic, self.jaccord_lineEdit.text())


    # Slot called when the user wants to write the filename
    def on_choose(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, 
            'Save CSV file', 
            None, 
            'CSV (*.csv)')
        if filename != '':
            self.filename_lineEdit.setText(filename)

    def on_topic_update(self, topic, message, sender):
        pass

    # Called by the publisher to init settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if DEBUG: print(f'EventCompareSettingsView.on_topic_update:{topic} message:{message}')
        if topic == self._filename_topic:
            self.filename_lineEdit.setText(message)
        if topic == self._label_topic:
            self.label_lineEdit.setText(message)
        if topic == self._event1_name_topic:
            self.event1_name_lineedit.setText(message)
        if topic == self._event2_name_topic:
            self.event2_name_lineedit.setText(message)
        if topic == self._channel1_name_topic:
            self.channel1_lineedit.setText(message)
        if topic == self._channel2_name_topic:
            self.channel2_lineedit.setText(message)
        if topic == self._jaccord_thresh_topic:
            self.jaccord_lineEdit.setText(message)


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._filename_topic)
            self._pub_sub_manager.unsubscribe(self, self._label_topic)
            self._pub_sub_manager.unsubscribe(self, self._event1_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._event2_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._channel1_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._channel2_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._jaccord_thresh_topic)