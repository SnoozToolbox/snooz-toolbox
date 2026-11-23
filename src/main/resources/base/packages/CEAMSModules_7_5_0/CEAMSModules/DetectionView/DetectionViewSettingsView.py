"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the DetectionView plugin
"""

from qtpy import QtWidgets

from CEAMSModules.DetectionView.Ui_DetectionViewSettingsView import Ui_DetectionViewSettingsView
from commons.BaseSettingsView import BaseSettingsView

class DetectionViewSettingsView( BaseSettingsView,  Ui_DetectionViewSettingsView, QtWidgets.QWidget):
    """
        DetectionViewSettingsView display the settings needed to show the 
        detection information.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        self._settings = {
            f'{parent_node.identifier}.time_elapsed': self.time_lineedit,
            f'{parent_node.identifier}.win_len_show': self.win_show_lineedit,
            f'{parent_node.identifier}.event_name': self.event_lineEdit,
            f'{parent_node.identifier}.channel': self.channel_lineedit,
            f'{parent_node.identifier}.win_step_sec': self.windet_step_lineedit,
            f'{parent_node.identifier}.threshold': self.thresh_lineedit,
            f'{parent_node.identifier}.threshold_unit': self.threshUnit_comboBox,
            f'{parent_node.identifier}.filename': self.filename_lineedit,
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
            self.filename_lineedit.setText(filename)

    def load_settings(self):
        for topic in self._settings:
            self._pub_sub_manager.publish(self, topic, 'ping')

    def on_apply_settings(self):
        for topic, widget in self._settings.items():
            if isinstance(widget, QtWidgets.QComboBox):
                value = widget.currentText()
            else:
                value = widget.text()
            self._pub_sub_manager.publish(self, topic, value)

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        widget = self._settings[topic]
        if isinstance(widget, QtWidgets.QComboBox):
            widget.setCurrentText(str(message))
        else:
            widget.setText(str(message))

    def __del__(self):
        if self._pub_sub_manager is not None:
            for topic in self._settings:
                self._pub_sub_manager.unsubscribe(self, topic)