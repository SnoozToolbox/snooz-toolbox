"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the SleepStageEvents plugin
"""

from qtpy import QtWidgets

from CEAMSModules.FilterEvents.Ui_FilterEventsSettingsView import Ui_FilterEventsSettingsView
from commons.BaseSettingsView import BaseSettingsView

class FilterEventsSettingsView( BaseSettingsView,  Ui_FilterEventsSettingsView, QtWidgets.QWidget):
    """
        FilterEventsSettingsView displays the settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        # Subscribe to the proper topics to send/get data from the node
        self._stages_topic = f'{self._parent_node.identifier}.stages_selection'
        self._pub_sub_manager.subscribe(self, self._stages_topic)
        self._group_topic = f'{self._parent_node.identifier}.group_selection'
        self._pub_sub_manager.subscribe(self, self._group_topic)
        self._name_topic = f'{self._parent_node.identifier}.name_selection'
        self._pub_sub_manager.subscribe(self, self._name_topic)


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._stages_topic, 'ping')
        self._pub_sub_manager.publish(self, self._group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._name_topic, 'ping')


    # Called when user check or uncheck NREM
    def on_event_nrem_changed(self):
        if self.nrem_checkBox.isChecked():
            self.stage1_checkBox.setChecked(True)
            self.stage2_checkBox.setChecked(True)
            self.stage3_checkBox.setChecked(True)
            self.stage4_checkBox.setChecked(True)
        else :
            self.stage1_checkBox.setChecked(False)
            self.stage2_checkBox.setChecked(False)
            self.stage3_checkBox.setChecked(False)
            self.stage4_checkBox.setChecked(False)
        # To update the sleep stages selected line edit
        self.on_event_stages_changed()


    # Called when user check or uncheck "Asleep stages"
    def on_event_nwake_changed(self):
        if self.nwake_checkBox.isChecked():
            self.wake_checkBox.setChecked(False)
            self.stage1_checkBox.setChecked(True)
            self.stage2_checkBox.setChecked(True)
            self.stage3_checkBox.setChecked(True)
            self.stage4_checkBox.setChecked(True)
            self.rem_checkBox.setChecked(True)
            self.movementtime_checkBox.setChecked(False)
            self.technicaltime_checkBox.setChecked(False)
            self.undetermined_checkBox.setChecked(False)

            self.nrem_checkBox.setChecked(True)
        else :
            self.wake_checkBox.setChecked(False)
            self.stage1_checkBox.setChecked(False)
            self.stage2_checkBox.setChecked(False)
            self.stage3_checkBox.setChecked(False)
            self.stage4_checkBox.setChecked(False)
            self.rem_checkBox.setChecked(False)
            self.movementtime_checkBox.setChecked(False)
            self.technicaltime_checkBox.setChecked(False)
            self.undetermined_checkBox.setChecked(False)
            
            self.nrem_checkBox.setChecked(False)
        # To update the sleep stages selected line edit
        self.on_event_stages_changed()


    # Called when user checks stages bodes
    def on_event_stages_changed(self):
        stages_message = []
        if self.wake_checkBox.isChecked():
            stages_message.append('0')
        if self.stage1_checkBox.isChecked():
            stages_message.append('1')
        if self.stage2_checkBox.isChecked():
            stages_message.append('2')
        if self.stage3_checkBox.isChecked():
            stages_message.append('3')
        if self.stage4_checkBox.isChecked():
            stages_message.append('4')
        if self.rem_checkBox.isChecked():
            stages_message.append('5')
        if self.movementtime_checkBox.isChecked():
            stages_message.append('6')
        if self.technicaltime_checkBox.isChecked():
            stages_message.append('7')
        if self.undetermined_checkBox.isChecked():
            stages_message.append('9')
        self.stages_lineEdit.setText(','.join(stages_message))


    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._stages_topic, \
            str(self.stages_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._group_topic, \
            str(self.group_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._name_topic, \
            str(self.name_lineEdit.text()))


    def on_topic_update(self, topic, message, sender):
        pass


    # Called by the publisher to display settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._stages_topic:
            self.stages_lineEdit.setText(str(message))
            # Check appropriate boxes
            all_selected_stage = message.split(',')
            for stage in all_selected_stage:
                if stage=='0':
                    self.wake_checkBox.setChecked(True)
                if stage=='1':
                    self.stage1_checkBox.setChecked(True)
                if stage=='2':
                    self.stage2_checkBox.setChecked(True)
                if stage=='3':
                    self.stage3_checkBox.setChecked(True)
                if stage=='4':
                    self.stage4_checkBox.setChecked(True)
                if stage=='5':
                    self.rem_checkBox.setChecked(True)
                if stage=='6':
                    self.movementtime_checkBox.setChecked(True)
                if stage=='7':
                    self.technicaltime_checkBox.setChecked(True)
                if stage=='9':
                    self.undetermined_checkBox.setChecked(True)
        if topic == self._group_topic:
            self.group_lineEdit.setText(str(message))
        if topic == self._name_topic:
            self.name_lineEdit.setText(str(message))


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._stages_topic)  
            self._pub_sub_manager.unsubscribe(self, self._group_topic)  
            self._pub_sub_manager.unsubscribe(self, self._name_topic)  