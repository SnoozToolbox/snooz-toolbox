"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the EventTemporalLink plugin
"""

from qtpy import QtWidgets

from CEAMSModules.EventTemporalLink.Ui_EventTemporalLinkSettingsView import Ui_EventTemporalLinkSettingsView
from commons.BaseSettingsView import BaseSettingsView

class EventTemporalLinkSettingsView( Ui_EventTemporalLinkSettingsView,  BaseSettingsView, QtWidgets.QWidget):
    """
        EventTemporalLinkView set the EventTemporalLink settings
    """
    def __init__(self, parent_node, pub_sub_manager, *args, options=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._event_reports_topic = f'{self._parent_node.identifier}.event_reports'
        self._pub_sub_manager.subscribe(self, self._event_reports_topic)
        self._record_info_topic = f'{self._parent_node.identifier}.record_info'
        self._pub_sub_manager.subscribe(self, self._record_info_topic)
        self._window_size_topic = f'{self._parent_node.identifier}.window_size'
        self._pub_sub_manager.subscribe(self, self._window_size_topic)
        self._temporal_links_topic = f'{self._parent_node.identifier}.temporal_links'
        self._pub_sub_manager.subscribe(self, self._temporal_links_topic)
        self._html_report_topic = f'{self._parent_node.identifier}.html_report'
        self._pub_sub_manager.subscribe(self, self._html_report_topic)
        self._html_report_config_topic = f'{self._parent_node.identifier}.html_report_config'
        self._pub_sub_manager.subscribe(self, self._html_report_config_topic)
        self._csv_report_topic = f'{self._parent_node.identifier}.csv_report'
        self._pub_sub_manager.subscribe(self, self._csv_report_topic)
        self._base_output_fullpath_topic = f'{self._parent_node.identifier}.base_output_fullpath'
        self._pub_sub_manager.subscribe(self, self._base_output_fullpath_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        
        self._pub_sub_manager.publish(self, self._event_reports_topic, 'ping')
        self._pub_sub_manager.publish(self, self._record_info_topic, 'ping')
        self._pub_sub_manager.publish(self, self._window_size_topic, 'ping')
        self._pub_sub_manager.publish(self, self._temporal_links_topic, 'ping')
        self._pub_sub_manager.publish(self, self._html_report_topic, 'ping')
        self._pub_sub_manager.publish(self, self._html_report_config_topic, 'ping')
        self._pub_sub_manager.publish(self, self._csv_report_topic, 'ping')
        self._pub_sub_manager.publish(self, self._base_output_fullpath_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        
        # Send the settings to the publisher for inputs to EventTemporalLink
        self._pub_sub_manager.publish(self, self._event_reports_topic, str(self.event_reports_lineedit.text()))
        self._pub_sub_manager.publish(self, self._record_info_topic, str(self.record_info_lineedit.text()))
        self._pub_sub_manager.publish(self, self._window_size_topic, str(self.window_size_lineedit.text()))
        self._pub_sub_manager.publish(self, self._temporal_links_topic, str(self.temporal_links_lineedit.text()))
        self._pub_sub_manager.publish(self, self._html_report_topic, str(self.html_report_lineedit.text()))
        self._pub_sub_manager.publish(self, self._html_report_config_topic, str(self.html_report_config_lineedit.text()))
        self._pub_sub_manager.publish(self, self._csv_report_topic, str(self.csv_report_lineedit.text()))
        self._pub_sub_manager.publish(self, self._base_output_fullpath_topic, str(self.base_output_fullpath_lineedit.text()))
        

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """

        if topic == self._event_reports_topic:
            self.event_reports_lineedit.setText(message)
        if topic == self._record_info_topic:
            self.record_info_lineedit.setText(message)
        if topic == self._window_size_topic:
            self.window_size_lineedit.setText(message)
        if topic == self._temporal_links_topic:
            self.temporal_links_lineedit.setText(message)
        if topic == self._html_report_topic:
            self.html_report_lineedit.setText(message)
        if topic == self._html_report_config_topic:
            self.html_report_config_lineedit.setText(message)
        if topic == self._csv_report_topic:
            self.csv_report_lineedit.setText(message)
        if topic == self._base_output_fullpath_topic:
            self.base_output_fullpath_lineedit.setText(message)
        