#! /usr/bin/env python3
"""
    SSWDCriterias
    Settings viewer of the save files plugin for the Slow Wave Detector tool
"""

from qtpy import QtWidgets
from qtpy.QtCore import QRegExp
from qtpy.QtGui import QRegExpValidator

from CEAMSTools.SlowWaveDetection.SSWDCriterias.Ui_SSWDCriterias import Ui_SSWDCriterias
from commons.BaseStepView import BaseStepView

class SSWDCriterias( BaseStepView,  Ui_SSWDCriterias, QtWidgets.QWidget):
    """
        SSWDCriterias
        Displays the next steps for the selection of the files.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Set input validators
        # Create a QRegExpValidator with the desired regular expression
        # Regular expression for alphanumeric, space, dash, and latin1 (ISO/CEI 8859-1) characters
        regex = QRegExp(r'^[a-zA-Z0-9ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ\s-_]*$')
        validator = QRegExpValidator(regex)

        # Set the validator for the QLineEdit
        self.event_name_lineedit.setValidator(validator)
        self.event_name_lineedit.setMaxLength(64)
        self.group_lineedit.setValidator(validator)
        self.group_lineedit.setMaxLength(64)
        
        # Define modules and nodes to talk to
        self._node_id_SlowWaveDetector = "b96c5849-1c9c-4b54-8965-c63ecf2fb2b6"
        self._node_id_SleepStageEvents = "724a65d7-444b-4fe2-b62b-e8004906da4a"
        self._node_id_discard_events1 = "c0153cbd-cab8-4c43-8555-3585b48f7248"
        self._node_id_discard_events2 = "0b3bd08b-6b82-4c72-8968-a0c33552e5fb"
        self._node_id_SWDetails = "0308c274-4216-4642-9093-0ac919e9a0de"

        self._stages_topic = f'{self._node_id_SleepStageEvents}.stages'
        self._exclude_remp_topic = f'{self._node_id_SleepStageEvents}.exclude_remp'
        self._pub_sub_manager.subscribe(self, self._exclude_remp_topic)
        self._group_topic = f'{self._node_id_SlowWaveDetector}.event_group'
        self._pub_sub_manager.subscribe(self, self._group_topic)
        self._name_topic = f'{self._node_id_SlowWaveDetector}.event_name'
        self._pub_sub_manager.subscribe(self, self._name_topic)
        self._f_min_topic = f'{self._node_id_SlowWaveDetector}.f_min'
        self._pub_sub_manager.subscribe(self, self._f_min_topic)
        self._f_max_topic = f'{self._node_id_SlowWaveDetector}.f_max'
        self._pub_sub_manager.subscribe(self, self._f_max_topic)
        self._th_PaP_topic = f'{self._node_id_SlowWaveDetector}.th_PaP'
        self._pub_sub_manager.subscribe(self, self._th_PaP_topic)
        self._th_Neg_topic = f'{self._node_id_SlowWaveDetector}.th_Neg'
        self._pub_sub_manager.subscribe(self, self._th_Neg_topic)
        self._min_tNe_topic = f'{self._node_id_SlowWaveDetector}.min_tNe'
        self._pub_sub_manager.subscribe(self, self._min_tNe_topic)
        self._max_tNe_topic = f'{self._node_id_SlowWaveDetector}.max_tNe'
        self._pub_sub_manager.subscribe(self, self._max_tNe_topic)
        self._min_tPo_topic = f'{self._node_id_SlowWaveDetector}.min_tPo'
        self._pub_sub_manager.subscribe(self, self._min_tPo_topic)
        self._max_tPo_topic = f'{self._node_id_SlowWaveDetector}.max_tPo'
        self._pub_sub_manager.subscribe(self, self._max_tPo_topic)
        self._age_criterion_topic = f'{self._node_id_SlowWaveDetector}.age_criterion'
        self._pub_sub_manager.subscribe(self, self._age_criterion_topic)
        self._years_topic = f'{self._node_id_SlowWaveDetector}.years'
        self._pub_sub_manager.subscribe(self, self._years_topic)
        self._months_topic = f'{self._node_id_SlowWaveDetector}.months'
        self._pub_sub_manager.subscribe(self, self._months_topic)
        self._sex_criterion_topic = f'{self._node_id_SlowWaveDetector}.sex_criterion'
        self._pub_sub_manager.subscribe(self, self._sex_criterion_topic)
        self._sex_topic = f'{self._node_id_SlowWaveDetector}.sex'
        self._pub_sub_manager.subscribe(self, self._sex_topic)

        self._det_param_topic = f'{self._node_id_SWDetails}.slow_wave_det_param'
        self._pub_sub_manager.subscribe(self, self._det_param_topic)

        self._group1_topic = f'{self._node_id_discard_events1}.event_group'
        self._pub_sub_manager.subscribe(self, self._group1_topic)
        self._name1_topic = f'{self._node_id_discard_events1}.event_name'
        self._pub_sub_manager.subscribe(self, self._name1_topic)
        self._group2_topic = f'{self._node_id_discard_events2}.event_group'
        self._pub_sub_manager.subscribe(self, self._group2_topic)
        self._name2_topic = f'{self._node_id_discard_events2}.event_name'
        self._pub_sub_manager.subscribe(self, self._name2_topic)


    def on_input_format_changed(self, int):
        if self.checkBox_age.isChecked():
            self.spinBox_years.setEnabled(True)
            self.label_years.setEnabled(True)
            self.spinBox_months.setEnabled(True)
            self.label_months.setEnabled(True)
        else:
            self.spinBox_years.setEnabled(False)
            self.label_years.setEnabled(False)
            self.spinBox_months.setEnabled(False)
            self.label_months.setEnabled(False)

        if self.checkBox_sex.isChecked():
            self.comboBox_sex.setEnabled(True)
        else:
            self.comboBox_sex.setEnabled(False)

        if self.carrier_radioButton.isChecked():
            self.doubleSpinBox_f_min.setValue(0.16)
            self.doubleSpinBox_f_min.setEnabled(False)
            self.doubleSpinBox_f_max.setValue(4.0)
            self.doubleSpinBox_f_max.setEnabled(False)
            self.doubleSpinBox_PaP_amp.setValue(75.0)
            self.doubleSpinBox_PaP_amp.setEnabled(False)
            self.doubleSpinBox_neg_amp.setValue(40.0)
            self.doubleSpinBox_neg_amp.setEnabled(False)
            self.spinBox_min_neg.setValue(125)
            self.spinBox_min_neg.setEnabled(False)
            self.spinBox_max_neg.setValue(1500)
            self.spinBox_max_neg.setEnabled(False)
            self.spinBox_min_pos.setValue(0)
            self.spinBox_min_pos.setEnabled(False)
            self.spinBox_max_pos.setValue(1000)
            self.spinBox_max_pos.setEnabled(False)
        
        if self.personalized_radioButton.isChecked():
            self.doubleSpinBox_f_min.setEnabled(True)
            self.doubleSpinBox_f_max.setEnabled(True)
            self.doubleSpinBox_PaP_amp.setEnabled(True)
            self.doubleSpinBox_neg_amp.setEnabled(True)
            self.spinBox_min_neg.setEnabled(True)
            self.spinBox_max_neg.setEnabled(True)
            self.spinBox_min_pos.setEnabled(True)
            self.spinBox_max_pos.setEnabled(True)


    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._stages_topic, 'ping')
        self._pub_sub_manager.publish(self, self._exclude_remp_topic, 'ping')
        self._pub_sub_manager.publish(self, self._group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._f_min_topic, 'ping')
        self._pub_sub_manager.publish(self, self._f_max_topic, 'ping')
        self._pub_sub_manager.publish(self, self._th_PaP_topic, 'ping')
        self._pub_sub_manager.publish(self, self._th_Neg_topic, 'ping') 
        self._pub_sub_manager.publish(self, self._min_tNe_topic, 'ping')
        self._pub_sub_manager.publish(self, self._max_tNe_topic, 'ping')
        self._pub_sub_manager.publish(self, self._min_tPo_topic, 'ping') 
        self._pub_sub_manager.publish(self, self._max_tPo_topic, 'ping')
        self._pub_sub_manager.publish(self, self._age_criterion_topic, 'ping') 
        self._pub_sub_manager.publish(self, self._years_topic, 'ping')
        self._pub_sub_manager.publish(self, self._months_topic, 'ping')
        self._pub_sub_manager.publish(self, self._sex_criterion_topic, 'ping')
        self._pub_sub_manager.publish(self, self._sex_topic, 'ping')


    def on_apply_settings(self):
        # Sleep stage selection to send to the "Sleep Stage Events" plugin
        stages_str = ''
        if self.checkBox_n1.isChecked():
            if len(stages_str)==0:
                stages_str = '1'
            else:
                stages_str = stages_str+',1'
        if self.checkBox_n2.isChecked():
            if len(stages_str)==0:
                stages_str = '2'
            else:
                stages_str = stages_str+',2'
        if self.checkBox_n3.isChecked():
            if len(stages_str)==0:
                stages_str = '3'
            else:
                stages_str = stages_str+',3'   
        if self.checkBox_r.isChecked():
            if len(stages_str)==0:
                stages_str = '5'
            else:
                stages_str = stages_str+',5'                
        self._pub_sub_manager.publish(self, self._stages_topic, str(stages_str))
        self._pub_sub_manager.publish(self, self._exclude_remp_topic, str(int(self.checkBox_excl_remp.isChecked())))
        # Send the settings to the publisher for inputs to SlowWaveDetector
        self._pub_sub_manager.publish(self, self._group_topic, \
            str(self.group_lineedit.text()))
        self._pub_sub_manager.publish(self, self._name_topic, \
            str(self.event_name_lineedit.text()))            
        self._pub_sub_manager.publish(self, self._f_min_topic, \
            str(self.doubleSpinBox_f_min.value()))
        self._pub_sub_manager.publish(self, self._f_max_topic, \
            str(self.doubleSpinBox_f_max.value()))
        self._pub_sub_manager.publish(self, self._th_PaP_topic, \
            str(self.doubleSpinBox_PaP_amp.value()))
        self._pub_sub_manager.publish(self, self._th_Neg_topic, \
            str(self.doubleSpinBox_neg_amp.value()))
        self._pub_sub_manager.publish(self, self._min_tNe_topic, \
            str(self.spinBox_min_neg.value()))
        self._pub_sub_manager.publish(self, self._max_tNe_topic, \
            str(self.spinBox_max_neg.value()))
        self._pub_sub_manager.publish(self, self._min_tPo_topic, \
            str(self.spinBox_min_pos.value()))
        self._pub_sub_manager.publish(self, self._max_tPo_topic, \
            str(self.spinBox_max_pos.value()))
        self._pub_sub_manager.publish(self, self._age_criterion_topic, \
            str(self.checkBox_age.isChecked()))
        self._pub_sub_manager.publish(self, self._years_topic, \
            str(self.spinBox_years.value()))
        self._pub_sub_manager.publish(self, self._months_topic, \
            str(self.spinBox_months.value()))
        self._pub_sub_manager.publish(self, self._sex_criterion_topic, \
            str(self.checkBox_sex.isChecked()))
        self._pub_sub_manager.publish(self, self._sex_topic, \
            str(self.comboBox_sex.currentText()))

        # Build the dictionary of section selection to run detector and the detector parameters
        det_param = {}
        det_param["stage_sel"] = stages_str
        det_param["detect_excl_remp"] = int(self.checkBox_excl_remp.isChecked())
        det_param["sw_event_name"] = str(self.event_name_lineedit.text())
        det_param['filt_low_Hz'] = self.doubleSpinBox_f_min.value()
        det_param['filt_high_Hz'] = self.doubleSpinBox_f_max.value()
        det_param['min_amp_pkpk_uV'] = self.doubleSpinBox_PaP_amp.value()
        det_param['min_neg_amp_uV'] = self.doubleSpinBox_neg_amp.value()
        det_param['min_neg_ms'] = self.spinBox_min_neg.value()
        det_param['max_neg_ms'] = self.spinBox_max_neg.value()
        det_param['min_pos_ms'] = self.spinBox_min_pos.value()
        det_param['max_pos_ms'] = self.spinBox_max_pos.value()

        self._pub_sub_manager.publish(self, self._det_param_topic, str(det_param))

        # To discard events during artifact 
        # (even if ther are resetted before the detection,
        # because we see uge artifact causing problems
        self._pub_sub_manager.publish(self, self._group1_topic, \
            str(self.group_lineedit.text()))
        self._pub_sub_manager.publish(self, self._name1_topic, \
            str(self.event_name_lineedit.text()))  
        self._pub_sub_manager.publish(self, self._group2_topic, \
            str(self.group_lineedit.text()))
        self._pub_sub_manager.publish(self, self._name2_topic, \
            str(self.event_name_lineedit.text()))          

    # Called by the publisher to init settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._stages_topic:
            stages_lst = message.split(',')
            self.checkBox_n1.setChecked('1' in stages_lst)
            self.checkBox_n2.setChecked('2' in stages_lst)
            self.checkBox_n3.setChecked('3' in stages_lst)
            self.checkBox_r.setChecked('5' in stages_lst)
        if topic == self._exclude_remp_topic:
            self.checkBox_excl_remp.setChecked(int(message))
        if topic == self._group_topic:
            self.group_lineedit.setText(str(message))
        if topic == self._name_topic:
            self.event_name_lineedit.setText(str(message))
        if topic == self._f_min_topic:
            self.doubleSpinBox_f_min.setValue(float(message))
        if topic == self._f_max_topic:
            self.doubleSpinBox_f_max.setValue(float(message))
        if topic == self._th_PaP_topic:
            self.doubleSpinBox_PaP_amp.setValue(float(message))
        if topic == self._th_Neg_topic:
            self.doubleSpinBox_neg_amp.setValue(float(message))
        if topic == self._min_tNe_topic:
            self.spinBox_min_neg.setValue(int(message))
        if topic == self._max_tNe_topic:
            self.spinBox_max_neg.setValue(int(message))
        if topic == self._min_tPo_topic:
            self.spinBox_min_pos.setValue(int(message)) 
        if topic == self._max_tPo_topic:
            self.spinBox_max_pos.setValue(int(message)) 
        if topic == self._age_criterion_topic:
            self.checkBox_age.setChecked(eval(message))
        if topic == self._years_topic:
            self.spinBox_years.setValue(int(message))
        if topic == self._months_topic:
            self.spinBox_months.setValue(int(message))
        if topic == self._sex_criterion_topic:
            self.checkBox_sex.setChecked(eval(message))
        if topic == self._sex_topic:
            self.comboBox_sex.setCurrentText(message)


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._stages_topic)
            self._pub_sub_manager.unsubscribe(self, self._exclude_remp_topic)  
            self._pub_sub_manager.unsubscribe(self, self._group_topic)   
            self._pub_sub_manager.unsubscribe(self, self._name_topic)   
            self._pub_sub_manager.unsubscribe(self, self._f_min_topic)
            self._pub_sub_manager.unsubscribe(self, self._f_max_topic)
            self._pub_sub_manager.unsubscribe(self, self._th_PaP_topic)
            self._pub_sub_manager.unsubscribe(self, self._th_Neg_topic)
            self._pub_sub_manager.unsubscribe(self, self._min_tNe_topic)
            self._pub_sub_manager.unsubscribe(self, self._max_tNe_topic)
            self._pub_sub_manager.unsubscribe(self, self._min_tPo_topic)
            self._pub_sub_manager.unsubscribe(self, self._max_tPo_topic)
            self._pub_sub_manager.unsubscribe(self, self._age_criterion_topic)
            self._pub_sub_manager.unsubscribe(self, self._years_topic)
            self._pub_sub_manager.unsubscribe(self, self._months_topic)
            self._pub_sub_manager.unsubscribe(self, self._sex_criterion_topic)
            self._pub_sub_manager.unsubscribe(self, self._sex_topic)
            self._pub_sub_manager.unsubscribe(self, self._det_param_topic)
            self._pub_sub_manager.unsubscribe(self, self._group1_topic)   
            self._pub_sub_manager.unsubscribe(self, self._name1_topic)  
            self._pub_sub_manager.unsubscribe(self, self._group2_topic)   
            self._pub_sub_manager.unsubscribe(self, self._name2_topic)  
            
