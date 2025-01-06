"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
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
        self.time_lineedit.init(self._parent_node.identifier, 'time_elapsed', self._pub_sub_manager)
        self.win_show_lineedit.init(self._parent_node.identifier, 'win_len_show', self._pub_sub_manager)
        self.event_lineEdit.init(self._parent_node.identifier, 'event_name', self._pub_sub_manager)
        self.channel_lineedit.init(self._parent_node.identifier, 'channel', self._pub_sub_manager)
        self.windet_step_lineedit.init(self._parent_node.identifier, 'win_step_sec', self._pub_sub_manager)
        self.thresh_lineedit.init(self._parent_node.identifier, 'threshold', self._pub_sub_manager)
        self.threshUnit_comboBox.init(self._parent_node.identifier, 'threshold_unit', self._pub_sub_manager)
        self.filename_lineedit.init(self._parent_node.identifier, 'filename', self._pub_sub_manager)

    def on_choose(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, 
            'Save as Python file', 
            None, 
            'Python (*.npy)')
        if filename != '':
            self.filename_lineedit.setText(filename)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass