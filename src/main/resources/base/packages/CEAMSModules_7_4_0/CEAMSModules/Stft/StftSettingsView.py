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
        self.window_len_lineedit.init(self._parent_node.identifier, 'win_len_sec', self._pub_sub_manager)
        self.window_step_lineedit.init(self._parent_node.identifier, 'win_step_sec', self._pub_sub_manager)
        self.zero_padding_checkbox.init(self._parent_node.identifier, 'zeros_pad', self._pub_sub_manager)
        self.window_combobox.init(self._parent_node.identifier, 'window_name', self._pub_sub_manager)
        self.remove_means_checkbox.init(self._parent_node.identifier, 'rm_mean', self._pub_sub_manager)
        self.norm_combobox.init(self._parent_node.identifier, 'norm', self._pub_sub_manager)
        self.filename_lineEdit.init(self._parent_node.identifier, 'filename', self._pub_sub_manager)
        
    def on_choose(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, 
            'Save as Python file', 
            None, 
            'Python (*.npy)')
        if filename != '':
            self.filename_lineEdit.setText(filename)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass

