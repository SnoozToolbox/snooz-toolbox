"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the SleepStageEvents plugin
"""

from qtpy import QtWidgets

from CEAMSModules.SleepStageEvents.Ui_SleepStageEventsSettingsView import Ui_SleepStageEventsSettingsView
from commons.BaseSettingsView import BaseSettingsView

class SleepStageEventsSettingsView( BaseSettingsView,  Ui_SleepStageEventsSettingsView, QtWidgets.QWidget):
    """
        SleepStageEventsView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        # Subscribe to the proper topics to send/get data from the node
        self._stages_topic = f'{self._parent_node.identifier}.stages'
        self._pub_sub_manager.subscribe(self, self._stages_topic)
        self._merge_events_topic = f'{self._parent_node.identifier}.merge_events'
        self._pub_sub_manager.subscribe(self, self._merge_events_topic)
        self._new_event_name_topic = f'{self._parent_node.identifier}.new_event_name'
        self._pub_sub_manager.subscribe(self, self._new_event_name_topic)
        self._exclude_REMP_topic = f'{self._parent_node.identifier}.exclude_remp'
        self._pub_sub_manager.subscribe(self, self._exclude_REMP_topic)
        self._exclude_NREMP_topic = f'{self._parent_node.identifier}.exclude_nremp'
        self._pub_sub_manager.subscribe(self, self._exclude_NREMP_topic)
        self._in_cycle_topic = f'{self._parent_node.identifier}.in_cycle'
        self._pub_sub_manager.subscribe(self, self._in_cycle_topic)


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._stages_topic, 'ping')
        self._pub_sub_manager.publish(self, self._merge_events_topic, 'ping')
        self._pub_sub_manager.publish(self, self._new_event_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._exclude_REMP_topic, 'ping')
        self._pub_sub_manager.publish(self, self._exclude_NREMP_topic, 'ping')
        self._pub_sub_manager.publish(self, self._in_cycle_topic, 'ping')


    def on_event_nrem_changed(self):
        if not self.nwake_checkBox.isChecked():
            if self.nrem_checkBox.isChecked():
                self.stage1_checkBox.setChecked(True)
                self.stage1_checkBox.setEnabled(False)
                self.stage2_checkBox.setChecked(True)
                self.stage2_checkBox.setEnabled(False)
                self.stage3_checkBox.setChecked(True)
                self.stage3_checkBox.setEnabled(False)
                self.stage4_checkBox.setChecked(True)
                self.stage4_checkBox.setEnabled(False)
                self.nwake_checkBox.setChecked(False)
                self.nwake_checkBox.setEnabled(False)
            else :
                self.stage1_checkBox.setEnabled(True)
                self.stage1_checkBox.setChecked(False)
                self.stage2_checkBox.setEnabled(True)
                self.stage2_checkBox.setChecked(False)
                self.stage3_checkBox.setEnabled(True)
                self.stage3_checkBox.setChecked(False)
                self.stage4_checkBox.setEnabled(True)
                self.stage4_checkBox.setChecked(False)
                self.nwake_checkBox.setChecked(False)
                self.nwake_checkBox.setEnabled(True)
        self.on_event_stages_changed()


    def on_event_nwake_changed(self):
        if not self.nrem_checkBox.isChecked():
            if self.nwake_checkBox.isChecked():
                self.stage1_checkBox.setChecked(True)
                self.stage1_checkBox.setEnabled(False)
                self.stage2_checkBox.setChecked(True)
                self.stage2_checkBox.setEnabled(False)
                self.stage3_checkBox.setChecked(True)
                self.stage3_checkBox.setEnabled(False)
                self.stage4_checkBox.setChecked(True)
                self.stage4_checkBox.setEnabled(False)
                self.rem_checkBox.setChecked(True)
                self.rem_checkBox.setEnabled(False)
                self.movementtime_checkBox.setChecked(True)
                self.movementtime_checkBox.setEnabled(False)
                self.technicaltime_checkBox.setChecked(True)
                self.technicaltime_checkBox.setEnabled(False)
                self.undetermined_checkBox.setChecked(True)
                self.undetermined_checkBox.setEnabled(False)
                self.wake_checkBox.setChecked(False)
                self.wake_checkBox.setEnabled(False)
                self.nrem_checkBox.setChecked(False)
                self.nrem_checkBox.setEnabled(False)
            else :
                self.stage1_checkBox.setEnabled(True)
                self.stage1_checkBox.setChecked(False)
                self.stage2_checkBox.setEnabled(True)
                self.stage2_checkBox.setChecked(False)
                self.stage3_checkBox.setEnabled(True)
                self.stage3_checkBox.setChecked(False)
                self.stage4_checkBox.setEnabled(True)
                self.stage4_checkBox.setChecked(False)
                self.rem_checkBox.setEnabled(True)
                self.rem_checkBox.setChecked(False)
                self.movementtime_checkBox.setEnabled(True)
                self.movementtime_checkBox.setChecked(False)
                self.technicaltime_checkBox.setEnabled(True)
                self.technicaltime_checkBox.setChecked(False)
                self.undetermined_checkBox.setEnabled(True)
                self.undetermined_checkBox.setChecked(False)
                self.wake_checkBox.setChecked(False)
                self.wake_checkBox.setEnabled(True)
                self.nrem_checkBox.setChecked(False)
                self.nrem_checkBox.setEnabled(True)
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
        self._pub_sub_manager.publish(self, self._merge_events_topic, \
            str(int(self.merge_events_checkBox.isChecked())))
        self._pub_sub_manager.publish(self, self._new_event_name_topic, \
            str(self.newname_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._exclude_REMP_topic, \
            str(int(self.excl_remp_checkBox_2.isChecked())))
        self._pub_sub_manager.publish(self, self._exclude_NREMP_topic, \
            str(int(self.excl_nremp_checkBox.isChecked())))
        self._pub_sub_manager.publish(self, self._in_cycle_topic, \
            str(int(self.evt_in_cycle_checkBox.isChecked())))

    def on_topic_update(self, topic, message, sender):
        pass


    # Called by the publisher to display settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._stages_topic:
            self.stages_lineEdit.setText(str(message))
        if topic == self._merge_events_topic:
            self.merge_events_checkBox.setChecked(int(message))
        if topic == self._new_event_name_topic:
            self.newname_lineEdit.setText(str(message))
        if topic == self._exclude_REMP_topic:
            self.excl_remp_checkBox_2.setChecked(int(message))
        if topic == self._exclude_NREMP_topic:
            self.excl_nremp_checkBox.setChecked(int(message))
        if topic == self._in_cycle_topic:
            self.evt_in_cycle_checkBox.setChecked(int(message))


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._stages_topic)  
            self._pub_sub_manager.unsubscribe(self, self._merge_events_topic)  
            self._pub_sub_manager.unsubscribe(self, self._new_event_name_topic)  
            self._pub_sub_manager.unsubscribe(self, self._exclude_REMP_topic)  
            self._pub_sub_manager.unsubscribe(self, self._exclude_NREMP_topic)  
            self._pub_sub_manager.unsubscribe(self, self._in_cycle_topic)  