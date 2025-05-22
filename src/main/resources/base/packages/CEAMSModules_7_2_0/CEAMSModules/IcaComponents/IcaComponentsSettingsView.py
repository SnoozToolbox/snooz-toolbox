"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the IcaComponents plugin
"""

from qtpy import QtWidgets

from CEAMSModules.IcaComponents.Ui_IcaComponentsSettingsView import Ui_IcaComponentsSettingsView
from commons.BaseSettingsView import BaseSettingsView

class IcaComponentsSettingsView( BaseSettingsView,  Ui_IcaComponentsSettingsView, QtWidgets.QWidget):
    """
        IcaComponentsView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._parameters_topic = f'{self._parent_node.identifier}.parameters'
        self._pub_sub_manager.subscribe(self, self._parameters_topic)

    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._parameters_topic, 'ping') 
        self.update_parameters()

    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        self.update_parameters()
        self._pub_sub_manager.publish(self, self._parameters_topic, self.parameters)

    def on_topic_update(self, topic, message, sender):
        pass

    def random_state_changed(self):
        if self.random_state_checkBox.isChecked():
            self.random_state_spinBox.setEnabled(False)
        else:
            self.random_state_spinBox.setEnabled(True)

    def update_parameters(self):
        if self.random_state_checkBox.isChecked():
            random_state = None
        else:
            random_state = self.random_state_spinBox.value()

        ICA_algo = "infomax"
        if self.radioButton_fastICA.isChecked():
            ICA_algo = "fastICA"

        self.parameters = {'ICA_algo': ICA_algo,
                           'algorithm': self.algorithm_comboBox.currentText(),
                           'whiten': self.whiten_comboBox.currentText(),
                           'fun': self.fun_comboBox.currentText(),
                           'max_iter': self.max_iter_spinBox.value(),
                           'tol': self.tol_doubleSpinBox.value(),
                           'random_state': random_state}


    # Called by the publisher to display settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._parameters_topic:
            if isinstance(message, str) and (not message==''):
                message = eval(message)
            if isinstance(message, dict):
                if message['ICA_algo']=='fastICA':
                    self.radioButton_fastICA.setChecked(True)
                if message['ICA_algo']=='infomax':
                    self.radioButton_infomax.setChecked(True)
                
                self.algorithm_comboBox.setCurrentText(message['algorithm'])
                self.whiten_comboBox.setCurrentText(message['whiten'])
                self.fun_comboBox.setCurrentText(message['fun'])
                self.max_iter_spinBox.setValue(message['max_iter'])
                self.tol_doubleSpinBox.setValue(message['tol'])
                if not message['random_state']==None:
                    self.random_state_checkBox.setChecked(False)
                    self.random_state_spinBox.setValue(message['random_state'])
                else:
                    self.random_state_checkBox.setChecked(True)
                    self.random_state_spinBox.setValue(0)
            else:
                # Default values
                self.radioButton_infomax.setChecked(True)
                self.algorithm_comboBox.setCurrentText('deflation')
                self.whiten_comboBox.setCurrentText('arbitrary-variance')
                self.fun_comboBox.setCurrentText('cube')
                self.max_iter_spinBox.setValue(1000)
                self.tol_doubleSpinBox.setValue(0.0001)
                self.random_state_spinBox.setValue(0)
            self.ICA_algorithms_slot()


    # The radio buttons to select the algo for ICA turn on/off the settings for the fast ICA.
    def ICA_algorithms_slot(self):
        if self.radioButton_fastICA.isChecked():
            self.algorithm_comboBox.setEnabled(True)
            self.whiten_comboBox.setEnabled(True)
            self.fun_comboBox.setEnabled(True)
            self.max_iter_spinBox.setEnabled(True)
            self.tol_doubleSpinBox.setEnabled(True)
            self.random_state_spinBox.setEnabled(True)
            self.random_state_checkBox.setEnabled(True)
        if self.radioButton_infomax.isChecked():
            self.algorithm_comboBox.setEnabled(False)
            self.whiten_comboBox.setEnabled(False)
            self.fun_comboBox.setEnabled(False)
            self.max_iter_spinBox.setEnabled(False)
            self.tol_doubleSpinBox.setEnabled(False)
            self.random_state_spinBox.setEnabled(False)
            self.random_state_checkBox.setEnabled(False)


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._parameters_topic)