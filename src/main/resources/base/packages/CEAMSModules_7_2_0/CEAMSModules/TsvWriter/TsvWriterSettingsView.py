"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the TsvWriter plugin
"""

from qtpy import QtWidgets

from CEAMSModules.TsvWriter.Ui_TsvWriterSettingsView import Ui_TsvWriterSettingsView
from commons.BaseSettingsView import BaseSettingsView

class TsvWriterSettingsView( BaseSettingsView,  Ui_TsvWriterSettingsView, QtWidgets.QWidget):
    """
        TsvWriterSettingsView displays the list of events.

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
        self._EDF_annot_topic = f'{self._parent_node.identifier}.EDF_annot'
        self._pub_sub_manager.subscribe(self, self._EDF_annot_topic)
        self._time_elapsed_topic = f'{self._parent_node.identifier}.time_elapsed'
        self._pub_sub_manager.subscribe(self, self._time_elapsed_topic)
        self._append_data_topic = f'{self._parent_node.identifier}.append_data'
        self._pub_sub_manager.subscribe(self, self._append_data_topic)
        self._index_topic = f'{self._parent_node.identifier}.add_index'
        self._pub_sub_manager.subscribe(self, self._index_topic)
        

    def on_choose(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, 
            'Save as TSV file', 
            None, 
            'TSV (*.tsv)')
        if filename != '':
            self.filename_lineedit.setText(filename)


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._filename_topic, 'ping')
        self._pub_sub_manager.publish(self, self._EDF_annot_topic, 'ping')
        self._pub_sub_manager.publish(self, self._time_elapsed_topic, 'ping')
        self._pub_sub_manager.publish(self, self._append_data_topic, 'ping')
        self._pub_sub_manager.publish(self, self._index_topic, 'ping')



    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._filename_topic, \
            str(self.filename_lineedit.text()))
        self._pub_sub_manager.publish(self, self._EDF_annot_topic, \
            str(int(self.EDF_annot_checkBox.isChecked())))
        self._pub_sub_manager.publish(self, self._time_elapsed_topic, \
            str(int(self.add_time_checkBox.isChecked())))
        self._pub_sub_manager.publish(self, self._append_data_topic, \
            str(int(self.append_data_checkBox.isChecked())))
        self._pub_sub_manager.publish(self, self._index_topic, \
            str(int(self.index_checkBox.isChecked())))


    def on_topic_update(self, topic, message, sender):
        pass


    # Called by the publisher to display settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._filename_topic:
            self.filename_lineedit.setText(message)
        if topic == self._EDF_annot_topic:
            self.EDF_annot_checkBox.setChecked(int(message))
        if topic == self._time_elapsed_topic:
            self.add_time_checkBox.setChecked(int(message))
        if topic == self._append_data_topic:
            self.append_data_checkBox.setChecked(int(message))
        if topic == self._index_topic:
            self.index_checkBox.setChecked(int(message))


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._filename_topic)
            self._pub_sub_manager.unsubscribe(self, self._EDF_annot_topic)
            self._pub_sub_manager.unsubscribe(self, self._time_elapsed_topic)
            self._pub_sub_manager.unsubscribe(self, self._append_data_topic)
            self._pub_sub_manager.unsubscribe(self, self._index_topic)