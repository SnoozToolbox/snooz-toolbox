"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the Stft plugin
"""

from qtpy import QtWidgets

from CEAMSModules.Stft.Ui_StftSettingsView import Ui_StftSettingsView
from commons.BaseSettingsView import BaseSettingsView

class StftSettingsView( BaseSettingsView,  Ui_StftSettingsView, QtWidgets.QWidget):
    """
        StftView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        self._settings = {
            f'{parent_node.identifier}.win_len_sec': self.window_len_lineedit,
            f'{parent_node.identifier}.win_step_sec': self.window_step_lineedit,
            f'{parent_node.identifier}.zeros_pad': self.zero_padding_checkbox,
            f'{parent_node.identifier}.window_name': self.window_combobox,
            f'{parent_node.identifier}.rm_mean': self.remove_means_checkbox,
            f'{parent_node.identifier}.norm': self.norm_combobox,
            f'{parent_node.identifier}.filename': self.filename_lineEdit,
        }
        for topic in self._settings:
            self._pub_sub_manager.subscribe(self, topic)
        
    def on_choose(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, 
            'Save as Python file', 
            None, 
            'Python (*.npy)')
        if filename != '':
            self.filename_lineEdit.setText(filename)

    def load_settings(self):
        for topic in self._settings:
            self._pub_sub_manager.publish(self, topic, 'ping')

    def on_apply_settings(self):
        for topic, widget in self._settings.items():
            if isinstance(widget, QtWidgets.QCheckBox):
                value = widget.isChecked()
            elif isinstance(widget, QtWidgets.QComboBox):
                value = widget.currentText()
            else:
                value = widget.text()
            self._pub_sub_manager.publish(self, topic, value)

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        widget = self._settings[topic]
        if isinstance(widget, QtWidgets.QCheckBox):
            if isinstance(message, str):
                value = message.strip().lower()
                if value not in ('true', 'false', '1', '0'):
                    raise ValueError(f'Invalid boolean value for {topic}: {message!r}')
                message = value in ('true', '1')
            elif isinstance(message, (bool, int)) and message in (0, 1):
                message = bool(message)
            else:
                raise ValueError(f'Invalid boolean value for {topic}: {message!r}')
            widget.setChecked(message)
        elif isinstance(widget, QtWidgets.QComboBox):
            widget.setCurrentText(str(message))
        else:
            widget.setText(str(message))
