#! /usr/bin/env python3

"""
    Settings viewer of the EventReader plugin
"""

from qtpy import QtWidgets

from CEAMSModules.EventReader.Ui_EventReaderSettingsView import Ui_EventReaderSettingsView
from commons.BaseSettingsView import BaseSettingsView

class EventReaderSettingsView( Ui_EventReaderSettingsView,  BaseSettingsView, QtWidgets.QWidget):
    """
        EventReaderSettingsView links the Settings Views of the plugin to the plugin itself.

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
        self._delimiter_topic = f'{self._parent_node.identifier}.delimiter'
        self._pub_sub_manager.subscribe(self, self._delimiter_topic)
        self._nrows_topic = f'{self._parent_node.identifier}.nrows_header'
        self._pub_sub_manager.subscribe(self, self._nrows_topic)
        self._encoding_topic = f'{self._parent_node.identifier}.encoding'
        self._pub_sub_manager.subscribe(self, self._encoding_topic)
        self._input_as_time_topic = f'{self._parent_node.identifier}.input_as_time'
        self._pub_sub_manager.subscribe(self, self._input_as_time_topic) 
        self._group_topic = f'{self._parent_node.identifier}.group_col_i'
        self._pub_sub_manager.subscribe(self, self._group_topic)
        self._group_def_topic = f'{self._parent_node.identifier}.group_def'
        self._pub_sub_manager.subscribe(self, self._group_def_topic)        
        self._event_name_topic = f'{self._parent_node.identifier}.name_col_i'
        self._pub_sub_manager.subscribe(self, self._event_name_topic)
        self._name_def_topic = f'{self._parent_node.identifier}.name_def'
        self._pub_sub_manager.subscribe(self, self._name_def_topic)
        self._onset_topic = f'{self._parent_node.identifier}.onset_col_i'
        self._pub_sub_manager.subscribe(self, self._onset_topic)        
        self._duration_topic = f'{self._parent_node.identifier}.duration_col_i'
        self._pub_sub_manager.subscribe(self, self._duration_topic)    
        self._channel_topic = f'{self._parent_node.identifier}.channels_col_i'
        self._pub_sub_manager.subscribe(self, self._channel_topic)    
        self._sample_rate_topic = f'{self._parent_node.identifier}.sample_rate'
        self._pub_sub_manager.subscribe(self, self._sample_rate_topic)
        self._event_center_topic = f'{self._parent_node.identifier}.event_center'
        self._pub_sub_manager.subscribe(self, self._event_center_topic)
        self._dur_disable_topic = f'{self._parent_node.identifier}.dur_disable'
        self._pub_sub_manager.subscribe(self, self._dur_disable_topic)                
        self._fixed_dur_topic = f'{self._parent_node.identifier}.fixed_dur'
        self._pub_sub_manager.subscribe(self, self._fixed_dur_topic)     
        self._personalized_header_topic = f'{self._parent_node.identifier}.personalized_header' 
        self._pub_sub_manager.subscribe(self, self._personalized_header_topic)     

        self.on_input_format_changed()


    # Called when user push "Choose" button
    def on_choose(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, 
            'Open file', 
            None, 
            "CSV (*.csv);;TSV (*.tsv);;Text files (*.txt)")
        if filename != '':
            self.filename_lineedit.setText(filename)
            extension = filename.split('.')[-1]
            if extension == 'csv':
                self.delimiter_lineedit.setText(',')
            elif extension == 'tsv':
                self.delimiter_lineedit.setText("\\t")


    # Called when user checks Disable duration column
    def on_event_pos_changed(self):

        self.checkBox_define_group.setEnabled(True)
        self.checkBox_define_name.setEnabled(True)
        self.checkBox_define_dur.setEnabled(True)
        #Not supported yet!
        self.checkBox_define_chan.setEnabled(False)

        if self.checkBox_define_group.isChecked():
            self.group_spinbox.setEnabled(True)
            self.group_spinbox.setValue(0)
            self.group_spinbox.setEnabled(False)
            self.group_lineEdit.setEnabled(True)
            #self.checkBox_group_enabled.setChecked(True)
        else:
            self.group_lineEdit.setText('')
            self.group_lineEdit.setEnabled(False)
            self.group_spinbox.setEnabled(True)

        if self.checkBox_define_name.isChecked():
            self.event_name_spinbox.setEnabled(True)
            self.event_name_spinbox.setValue(0)
            self.event_name_spinbox.setEnabled(False)
            self.name_lineEdit.setEnabled(True)
        else:
            self.name_lineEdit.setText('')
            self.name_lineEdit.setEnabled(False)
            self.event_name_spinbox.setEnabled(True)

        if self.checkBox_define_dur.isChecked():
            self.duration_spinbox.setEnabled(True)
            self.duration_spinbox.setValue(0)
            self.duration_spinbox.setEnabled(False)
            self.fixed_dur_lineEdit.setEnabled(True)
        else:
            self.fixed_dur_lineEdit.setText('')
            self.fixed_dur_lineEdit.setEnabled(False)
            self.duration_spinbox.setEnabled(True)

        if self.checkBox_define_chan.isChecked():
            self.channel_spinBox.setEnabled(True)
            self.channel_spinBox.setValue(0)
            self.channel_spinBox.setEnabled(False)
            self.fixed_chan_lineEdit.setEnabled(True)
        else:
            self.fixed_chan_lineEdit.setText('')
            self.fixed_chan_lineEdit.setEnabled(False)
            self.channel_spinBox.setEnabled(True)


    # Called when the user changes the input File Format radio button
    def snooz_event_update_slot(self):
        if self.radioButton_personalized.isChecked():

            self.time_radiobutton.setEnabled(False)
            self.sample_radiobutton.setEnabled(False)
            self.sample_rate_lineedit.setEnabled(False)
            self.lineEdit_time_format.setEnabled(False)

            self.checkBox_group_enabled.setEnabled(False)
            self.group_spinbox.setEnabled(False)
            self.checkBox_define_group.setEnabled(False)
            self.group_lineEdit.setEnabled(False)
            
            self.event_name_spinbox.setEnabled(False)
            self.checkBox_define_name.setEnabled(False)
            self.name_lineEdit.setEnabled(False)

            self.onset_spinbox.setEnabled(False)
            self.center_checkBox.setEnabled(False)

            self.checkBox_dur_enabled.setEnabled(False)
            self.duration_spinbox.setEnabled(False)
            self.checkBox_define_dur.setEnabled(False)
            self.fixed_dur_lineEdit.setEnabled(False)

            self.checkBox_chan_enabled.setEnabled(False)
            self.channel_spinBox.setEnabled(False)
            self.fixed_chan_lineEdit.setEnabled(False)

        else:
            
            self.time_radiobutton.setEnabled(True)
            self.sample_radiobutton.setEnabled(True)
            self.sample_rate_lineedit.setEnabled(True)
            self.lineEdit_time_format.setEnabled(True)

            self.checkBox_group_enabled.setEnabled(True)
            self.group_spinbox.setEnabled(True)
            self.checkBox_define_group.setEnabled(True)
            self.group_lineEdit.setEnabled(True)
            
            self.event_name_spinbox.setEnabled(True)
            self.checkBox_define_name.setEnabled(True)
            self.name_lineEdit.setEnabled(True)

            self.onset_spinbox.setEnabled(True)
            self.center_checkBox.setEnabled(True)

            self.checkBox_dur_enabled.setEnabled(True)
            self.duration_spinbox.setEnabled(True)
            self.checkBox_define_dur.setEnabled(True)
            self.fixed_dur_lineEdit.setEnabled(True)

            self.checkBox_chan_enabled.setEnabled(True)
            self.channel_spinBox.setEnabled(True)
            self.fixed_chan_lineEdit.setEnabled(True)


    # Called when user check Times or Samples
    def on_input_format_changed(self):

        if self.time_radiobutton.isChecked():
            self.sample_rate_lineedit.setEnabled(False)
            self.lineEdit_time_format.setEnabled(True)
        else:
            self.sample_rate_lineedit.setEnabled(True)
            self.lineEdit_time_format.setEnabled(False)

        if self.sample_radiobutton.isChecked():
            self.sample_rate_lineedit.setEnabled(True)
            self.lineEdit_time_format.setEnabled(False)
        else:
            self.sample_rate_lineedit.setEnabled(False)
            self.lineEdit_time_format.setEnabled(True)


    def group_enabled_slot(self):
        if self.checkBox_group_enabled.isChecked():
            self.group_spinbox.setEnabled(True)
            self.checkBox_define_group.setChecked(False)
            self.group_lineEdit.setEnabled(False)
        else:
            self.group_spinbox.setEnabled(True)   
            self.group_spinbox.setValue(0)
            self.group_spinbox.setEnabled(False)   
            self.checkBox_define_group.setEnabled(True)  
            if self.checkBox_define_group.isChecked():
                self.group_lineEdit.setEnabled(True)
            else:
                self.group_lineEdit.setEnabled(False)


    def dur_enabled_slot(self):
        if self.checkBox_dur_enabled.isChecked():
            self.duration_spinbox.setEnabled(True)
            self.checkBox_define_dur.setChecked(False)
            self.fixed_dur_lineEdit.setEnabled(False)
        else:
            self.duration_spinbox.setEnabled(True) 
            self.duration_spinbox.setValue(0)
            self.duration_spinbox.setEnabled(False)          
            self.checkBox_define_dur.setEnabled(True)
            if self.checkBox_define_dur.isChecked():
                self.fixed_dur_lineEdit.setEnabled(True)
            else:
                self.fixed_dur_lineEdit.setEnabled(False)


    def chan_enabled_slot(self):
        if self.checkBox_chan_enabled.isChecked():
            self.channel_spinBox.setEnabled(True)
            #self.checkBox_define_chan.setChecked(False)
            self.fixed_chan_lineEdit.setEnabled(False)
        else:
            self.channel_spinBox.setEnabled(True) 
            self.channel_spinBox.setValue(0)
            self.channel_spinBox.setEnabled(False)    
            # Not supported yet!      
            # self.checkBox_define_chan.setEnabled(True)
            # if self.checkBox_define_chan.isChecked():
            #     self.fixed_chan_lineEdit.setEnabled(True)
            # else:
            #     self.fixed_chan_lineEdit.setEnabled(False)


    # Called when the user change the group spin box value
    def on_group_index_changed(self, spin_value):
        if spin_value==0:
            self.checkBox_group_enabled.setChecked(False)
            self.checkBox_define_group.setEnabled(True)
        else:
            self.checkBox_group_enabled.setChecked(True)
            self.group_lineEdit.setEnabled(False)
            

    # Called when the user change the name spin box value
    def on_name_index_changed(self, spin_value):
        if spin_value==0:
            self.checkBox_define_name.setEnabled(True)
            self.checkBox_define_name.setChecked(True)
            self.name_lineEdit.setEnabled(True)
        else:
            self.name_lineEdit.setEnabled(False)
            self.checkBox_define_name.setChecked(False)


    # Called when the user change the duration spin box value
    def on_duration_index_changed(self, spin_value):
        if spin_value==0:
            self.checkBox_dur_enabled.setChecked(False)
            self.checkBox_define_dur.setEnabled(True)
        else:
            self.checkBox_dur_enabled.setChecked(True)
            self.checkBox_define_dur.setChecked(False)
            

    # Called when the user change the name spin box value
    def on_chan_index_changed(self, spin_value):
        if spin_value==0:
            self.checkBox_chan_enabled.setChecked(False)
            #Not supported yet!
            #self.checkBox_define_chan.setEnabled(True)
        else:
            self.checkBox_chan_enabled.setChecked(True)
            self.fixed_chan_lineEdit.setEnabled(False)
            #Not supported yet!
            # self.checkBox_define_chan.setEnabled(True)
            # self.checkBox_define_chan.setChecked(False)            


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._filename_topic, 'ping')
        self._pub_sub_manager.publish(self, self._delimiter_topic, 'ping')
        self._pub_sub_manager.publish(self, self._nrows_topic, 'ping')
        self._pub_sub_manager.publish(self, self._encoding_topic, 'ping')
        self._pub_sub_manager.publish(self, self._input_as_time_topic, 'ping')
        self._pub_sub_manager.publish(self, self._group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._group_def_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._name_def_topic, 'ping')
        self._pub_sub_manager.publish(self, self._onset_topic, 'ping')
        self._pub_sub_manager.publish(self, self._duration_topic, 'ping')
        self._pub_sub_manager.publish(self, self._channel_topic, 'ping')
        self._pub_sub_manager.publish(self, self._sample_rate_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event_center_topic, 'ping')
        self._pub_sub_manager.publish(self, self._dur_disable_topic, 'ping')
        self._pub_sub_manager.publish(self, self._fixed_dur_topic, 'ping')  
        self._pub_sub_manager.publish(self, self._personalized_header_topic, 'ping')   


    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._filename_topic, \
            str(self.filename_lineedit.text()))
        self._pub_sub_manager.publish(self, self._delimiter_topic, \
            str(self.delimiter_lineedit.text()))
        self._pub_sub_manager.publish(self, self._nrows_topic, self.spinBox_nrows_hdr.value())
        self._pub_sub_manager.publish(self, self._encoding_topic, self.comboBox_encoding.currentText())
        if self.sample_radiobutton.isChecked():
            self._pub_sub_manager.publish(self, self._input_as_time_topic, "samples")
        elif self.lineEdit_time_format.text()=="":
            self._pub_sub_manager.publish(self, self._input_as_time_topic, "seconds")
        else:
            # Extract a specific time format
            self._pub_sub_manager.publish(self, self._input_as_time_topic, self.lineEdit_time_format.text())
        self._pub_sub_manager.publish(self, self._group_topic, \
            str(self.group_spinbox.value()))
        self._pub_sub_manager.publish(self, self._group_def_topic, \
            str(self.group_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._event_name_topic, \
            str(self.event_name_spinbox.value()))
        self._pub_sub_manager.publish(self, self._name_def_topic, \
            str(self.name_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._onset_topic, \
            str(self.onset_spinbox.value()))
        self._pub_sub_manager.publish(self, self._duration_topic, \
            str(self.duration_spinbox.value()))
        self._pub_sub_manager.publish(self, self._channel_topic, \
            str(self.channel_spinBox.value()))            
        self._pub_sub_manager.publish(self, self._sample_rate_topic, \
            str(self.sample_rate_lineedit.text()))
        self._pub_sub_manager.publish(self, self._event_center_topic, \
            str(int(self.center_checkBox.isChecked())))
        self._pub_sub_manager.publish(self, self._dur_disable_topic, \
            str(int(not(self.checkBox_dur_enabled.isChecked()))))
        self._pub_sub_manager.publish(self, self._fixed_dur_topic, \
            str(self.fixed_dur_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._personalized_header_topic, \
            str(int(self.radioButton_personalized.isChecked())))


    def on_topic_update(self, topic, message, sender):
        pass


    # Called by the publisher to display settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._filename_topic:
            self.filename_lineedit.setText(message)
        if topic == self._delimiter_topic:
            self.delimiter_lineedit.setText(message)
        if topic == self._nrows_topic:
            self.spinBox_nrows_hdr.setValue(message)
        if topic == self._encoding_topic:
            self.comboBox_encoding.setCurrentText(message)
        # Exclusive radio button : only check the one checked
        if topic == self._input_as_time_topic:
            if message=='samples':
                self.sample_radiobutton.setChecked(True)
                self.lineEdit_time_format.setText("")
                self.lineEdit_time_format.setEnabled(False)
            elif message=='seconds':
                self.time_radiobutton.setChecked(True)
                self.lineEdit_time_format.setText("")
                self.lineEdit_time_format.setEnabled(True)
            else:
                self.time_radiobutton.setChecked(True)
                self.lineEdit_time_format.setText(message)
                self.lineEdit_time_format.setEnabled(True)                
        if topic == self._group_topic:
            self.group_spinbox.setValue(int(message))
        if topic == self._group_def_topic:
            self.group_lineEdit.setText(message)
        if topic == self._event_name_topic:
            self.event_name_spinbox.setValue(int(message))
        if topic == self._name_def_topic:
            self.name_lineEdit.setText(message)
        if topic == self._onset_topic:
            self.onset_spinbox.setValue(int(message))
        if topic == self._duration_topic:
            self.duration_spinbox.setValue(int(message))
        if topic == self._channel_topic:
            self.channel_spinBox.setValue(int(message))
        if topic == self._sample_rate_topic:
            self.sample_rate_lineedit.setText(message)        
        if topic == self._event_center_topic:
            self.center_checkBox.setChecked(int(message))   
        if topic == self._dur_disable_topic:
            flag = False if int(message)==1 else True
            self.checkBox_dur_enabled.setChecked(flag)   
        if topic == self._fixed_dur_topic:
            self.fixed_dur_lineEdit.setText(message)    
        if topic == self._personalized_header_topic:
            self.radioButton_personalized.setChecked(int(message))    


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._filename_topic)
            self._pub_sub_manager.unsubscribe(self, self._delimiter_topic)
            self._pub_sub_manager.unsubscribe(self, self._nrows_topic)
            self._pub_sub_manager.unsubcribe(self, self._encoding_topic)
            self._pub_sub_manager.unsubscribe(self, self._input_as_time_topic)
            self._pub_sub_manager.unsubscribe(self, self._group_topic)
            self._pub_sub_manager.unsubscribe(self, self._group_def_topic)
            self._pub_sub_manager.unsubscribe(self, self._event_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._name_def_topic)
            self._pub_sub_manager.unsubscribe(self, self._onset_topic)
            self._pub_sub_manager.unsubscribe(self, self._duration_topic)
            self._pub_sub_manager.unsubscribe(self, self._channel_topic)
            self._pub_sub_manager.unsubscribe(self, self._sample_rate_topic)
            self._pub_sub_manager.unsubscribe(self, self._event_center_topic)
            self._pub_sub_manager.unsubscribe(self, self._dur_disable_topic)
            self._pub_sub_manager.unsubscribe(self, self._fixed_dur_topic)  
            self._pub_sub_manager.unsubscribe(self, self._personalized_header_topic)            