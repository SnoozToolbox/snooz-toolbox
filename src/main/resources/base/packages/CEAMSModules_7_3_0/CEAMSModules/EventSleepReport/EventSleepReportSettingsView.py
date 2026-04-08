"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the EventSleepReport plugin
"""

from qtpy import QtWidgets

from CEAMSModules.EventSleepReport.Ui_EventSleepReportSettingsView import Ui_EventSleepReportSettingsView
from commons.BaseSettingsView import BaseSettingsView

class EventSleepReportSettingsView( Ui_EventSleepReportSettingsView,  BaseSettingsView, QtWidgets.QWidget):
    """
        EventSleepReportView set the EventSleepReport settings
    """
    def __init__(self, parent_node, pub_sub_manager, *args, options=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._html_report_topic = f'{self._parent_node.identifier}.html_report'
        self._pub_sub_manager.subscribe(self, self._html_report_topic)
        self._csv_report_topic = f'{self._parent_node.identifier}.csv_report'
        self._pub_sub_manager.subscribe(self, self._csv_report_topic)
        self._save_events_topic = f'{self._parent_node.identifier}.save_events_report'
        self._pub_sub_manager.subscribe(self, self._save_events_topic)
        self._output_prefix_topic = f'{self._parent_node.identifier}.output_prefix'
        self._pub_sub_manager.subscribe(self, self._output_prefix_topic)
        self._output_directory_topic = f'{self._parent_node.identifier}.output_directory'
        self._pub_sub_manager.subscribe(self, self._output_directory_topic)
        

    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._html_report_topic, 'ping')
        self._pub_sub_manager.publish(self, self._csv_report_topic, 'ping')
        self._pub_sub_manager.publish(self, self._save_events_topic, 'ping')
        self._pub_sub_manager.publish(self, self._output_prefix_topic, 'ping')
        self._pub_sub_manager.publish(self, self._output_directory_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        # Send the settings to the publisher for inputs to EventSleepReport
        self._pub_sub_manager.publish(self, self._html_report_topic, str(int(self.html_checkBox.isChecked())))
        self._pub_sub_manager.publish(self, self._csv_report_topic, str(int(self.csv_report_checkBox.isChecked())))
        self._pub_sub_manager.publish(self, self._save_events_topic, str(int(self.save_events_report_checkBox.isChecked())))
        self._pub_sub_manager.publish(self, self._output_prefix_topic, str(self.output_prefix_lineedit.text()))
        self._pub_sub_manager.publish(self, self._output_directory_topic, str(self.output_directory_lineEdit.text()))


    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._html_report_topic:
            self.html_checkBox.setChecked(int(message))
        if topic == self._csv_report_topic:
            self.csv_report_checkBox.setChecked(int(message))
        if topic == self._output_prefix_topic:
            self.output_prefix_lineedit.setText(message)
        if topic == self._output_directory_topic:
            self.output_directory_lineEdit.setText(message)
        