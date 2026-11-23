"""
© 2022 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the SlowWaveDetector plugin
"""

from qtpy import QtWidgets

from CEAMSModules.SlowWaveDetector.Ui_SlowWaveDetectorSettingsView import Ui_SlowWaveDetectorSettingsView
from commons.BaseSettingsView import BaseSettingsView

class SlowWaveDetectorSettingsView( BaseSettingsView,  Ui_SlowWaveDetectorSettingsView, QtWidgets.QWidget):
    """
        SlowWaveDetectorView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        # Subscribe to the proper topics to send/get data from the node
        self._group_topic = f'{self._parent_node.identifier}.event_group'
        self._pub_sub_manager.subscribe(self, self._group_topic)
        self._name_topic = f'{self._parent_node.identifier}.event_name'
        self._pub_sub_manager.subscribe(self, self._name_topic)
        self._f_min_topic = f'{self._parent_node.identifier}.f_min'
        self._pub_sub_manager.subscribe(self, self._f_min_topic)
        self._f_max_topic = f'{self._parent_node.identifier}.f_max'
        self._pub_sub_manager.subscribe(self, self._f_max_topic)
        self._th_PaP_topic = f'{self._parent_node.identifier}.th_PaP'
        self._pub_sub_manager.subscribe(self, self._th_PaP_topic)
        self._th_Neg_topic = f'{self._parent_node.identifier}.th_Neg'
        self._pub_sub_manager.subscribe(self, self._th_Neg_topic)
        self._min_tNe_topic = f'{self._parent_node.identifier}.min_tNe'
        self._pub_sub_manager.subscribe(self, self._min_tNe_topic)
        self._max_tNe_topic = f'{self._parent_node.identifier}.max_tNe'
        self._pub_sub_manager.subscribe(self, self._max_tNe_topic)
        self._min_tPo_topic = f'{self._parent_node.identifier}.min_tPo'
        self._pub_sub_manager.subscribe(self, self._min_tPo_topic)
        self._max_tPo_topic = f'{self._parent_node.identifier}.max_tPo'
        self._pub_sub_manager.subscribe(self, self._max_tPo_topic)
        self._age_criterion_topic = f'{self._parent_node.identifier}.age_criterion'
        self._pub_sub_manager.subscribe(self, self._age_criterion_topic)
        self._years_topic = f'{self._parent_node.identifier}.years'
        self._pub_sub_manager.subscribe(self, self._years_topic)
        self._months_topic = f'{self._parent_node.identifier}.months'
        self._pub_sub_manager.subscribe(self, self._months_topic)
        self._sex_criterion_topic = f'{self._parent_node.identifier}.sex_criterion'
        self._pub_sub_manager.subscribe(self, self._sex_criterion_topic)
        self._sex_topic = f'{self._parent_node.identifier}.sex'
        self._pub_sub_manager.subscribe(self, self._sex_topic)


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
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


    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
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
    
    
    # Slot called when user changes the checkbox to activate age or sex parameters
    def on_input_format_changed(self, int):
        print("on_input_format_changed")
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


    def on_topic_update(self, topic, message, sender):
        print("topic update")
        pass


    # Called by the publisher to init settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._group_topic:
            self.group_lineedit.setText(message)
        if topic == self._name_topic:
            self.event_name_lineedit.setText(message)
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