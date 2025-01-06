"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the RescaleSignal plugin
"""

import numpy as np
from qtpy import QtWidgets

from CEAMSModules.RescaleSignal.Ui_RescaleSignalSettingsView import Ui_RescaleSignalSettingsView
from commons.BaseSettingsView import BaseSettingsView

DEBUG = False

class RescaleSignalSettingsView( BaseSettingsView,  Ui_RescaleSignalSettingsView, QtWidgets.QWidget):
    """
        RescaleSignalView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        # Subscribe to the proper topics to send/get data from the node
        self._scaling_approach_topic = f'{self._parent_node.identifier}.scaling_approach'
        self._pub_sub_manager.subscribe(self, self._scaling_approach_topic)
        self._parameters_topic = f'{self._parent_node.identifier}.parameters'
        self._pub_sub_manager.subscribe(self, self._parameters_topic)
        
    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._scaling_approach_topic, 'ping')
        self._pub_sub_manager.publish(self, self._parameters_topic, 'ping')
        self.on_scaling_approach_choose()
        

    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._scaling_approach_topic, \
            str(self.scaling_approach_comboBox.currentText()))
        self.on_scaling_approach_choose()
        self._pub_sub_manager.publish(self, self._parameters_topic, \
            self.parameters)
        
    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'RescaleSignalSettingsView.on_topic_update:{topic} message:{message}')

    # Called by the publisher to display settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._scaling_approach_topic:
            self.scaling_approach_comboBox.setCurrentText(message)
        if topic == self._parameters_topic:
            if self.scaling_approach_comboBox.currentText() == 'Normalization':
                if message=='':
                    # Default values
                    self.norm_min_doubleSpinBox.setValue(float(0))
                    self.norm_max_doubleSpinBox.setValue(float(1))
                    self.norm_copy_checkBox.setChecked(True)
                    self.norm_clip_checkBox.setChecked(False)                    
                else:
                    self.norm_min_doubleSpinBox.setValue(float(message['min']))
                    self.norm_max_doubleSpinBox.setValue(float(message['max']))
                    self.norm_copy_checkBox.setChecked(bool(message['copy']))
                    self.norm_clip_checkBox.setChecked(bool(message['clip']))

            if self.scaling_approach_comboBox.currentText() == 'Standardization':
                if message=='':
                    # Default values
                    self.stand_copy_checkBox.setChecked(True)
                    self.stand_with_mean_checkBox.setChecked(True)
                    self.stand_with_std_checkBox.setChecked(True)                    
                else:                
                    self.stand_copy_checkBox.setChecked(bool(message['copy']))
                    self.stand_with_mean_checkBox.setChecked(bool(message['with_mean']))
                    self.stand_with_std_checkBox.setChecked(bool(message['with_std']))

            if self.scaling_approach_comboBox.currentText() == 'Discretization':
                if message=='':
                    self.discr_n_bins_spinBox.setValue(5)
                    self.discr_encode_comboBox.setCurrentText('onehot')
                    self.discr_strategy_comboBox.setCurrentText('quantile')
                    self.discr_dtype_comboBox.setCurrentText('None')
                else:
                    self.discr_n_bins_spinBox.setValue(int(message['n_bins']))
                    self.discr_encode_comboBox.setCurrentText(message['encode'])
                    self.discr_strategy_comboBox.setCurrentText(message['strategy'])
                    self.discr_dtype_comboBox.setCurrentText(str(message['dtype']))


    def on_scaling_approach_choose(self):
        if self.scaling_approach_comboBox.currentText() == 'Normalization':
            self.parameters = {'min' : self.norm_min_doubleSpinBox.value(),
                               'max' : self.norm_max_doubleSpinBox.value(),
                               'copy' : self.norm_copy_checkBox.isChecked(),
                               'clip' : self.norm_clip_checkBox.isChecked()
                               }
            self.page_visible()
        if self.scaling_approach_comboBox.currentText() == 'Standardization':
            self.parameters = {'copy' : self.stand_copy_checkBox.isChecked(),
                               'with_mean' : self.stand_with_mean_checkBox.isChecked(),
                               'with_std' : self.stand_with_std_checkBox.isChecked()
                               }
            self.page_visible()

        if self.scaling_approach_comboBox.currentText() == 'Discretization':
            dtype = self.discr_dtype_comboBox.currentText()
            if dtype == 'np.float32':
                dtype = np.float32
            elif dtype == 'np.float64':
                dtype = np.float64
            else:
                dtype = None

            self.parameters = {'n_bins' : self.discr_n_bins_spinBox.value(),
                               'encode' : self.discr_encode_comboBox.currentText(),
                               'strategy' : self.discr_strategy_comboBox.currentText(),
                               'dtype' : dtype
                               }
            self.page_visible()


    def page_visible(self):
        # For each approach
        if self.scaling_approach_comboBox.currentText() == 'Normalization':
            self.stackedWidget.setCurrentIndex(0)
        elif self.scaling_approach_comboBox.currentText() == 'Standardization':
            self.stackedWidget.setCurrentIndex(1)
        elif self.scaling_approach_comboBox.currentText() == 'Discretization':
            self.stackedWidget.setCurrentIndex(2)

    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._scaling_approach_topic)
            self._pub_sub_manager.unsubscribe(self, self._parameters_topic) 
            return