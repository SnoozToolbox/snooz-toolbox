"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    Settings viewer of the EventSubdivision plugin
"""

from qtpy import QtWidgets

from CEAMSModules.EventSubdivision.Ui_EventSubdivisionSettingsView import Ui_EventSubdivisionSettingsView
from commons.BaseSettingsView import BaseSettingsView

class EventSubdivisionSettingsView(BaseSettingsView, Ui_EventSubdivisionSettingsView, QtWidgets.QWidget):
    """
        EventSubdivisionView set the EventSubdivision settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._events_names_topic = f'{self._parent_node.identifier}.events_names'
        self._pub_sub_manager.subscribe(self, self._events_names_topic)
        self._window_sec_topic = f'{self._parent_node.identifier}.window_sec'
        self._pub_sub_manager.subscribe(self, self._window_sec_topic)
        self._n_window_topic = f'{self._parent_node.identifier}.n_window'
        self._pub_sub_manager.subscribe(self, self._n_window_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._events_names_topic, 'ping')
        self._pub_sub_manager.publish(self, self._window_sec_topic, 'ping')
        self._pub_sub_manager.publish(self, self._n_window_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        
        self._pub_sub_manager.publish(self, self._events_names_topic, \
            str(self.events_names_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._window_sec_topic, \
            self.win_time_spinbox.value())
        self._pub_sub_manager.publish(self, self._n_window_topic, \
            self.n_window_spinBox.value())
        

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """

        if topic == self._events_names_topic:
            self.events_names_lineEdit.setText(str(message))
        if topic == self._window_sec_topic:
            self.win_time_spinbox.setValue(int(message))
        if topic == self._n_window_topic:
            self.n_window_spinBox.setValue(int(message))
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._events_names_topic)
            self._pub_sub_manager.unsubscribe(self, self._window_sec_topic)
            self._pub_sub_manager.unsubscribe(self, self._n_window_topic)
            
            return
        