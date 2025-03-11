"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the EventCreator plugin
"""

from qtpy import QtWidgets

from CEAMSModules.EventCreator.Ui_EventCreatorSettingsView import Ui_EventCreatorSettingsView
from commons.BaseSettingsView import BaseSettingsView

class EventCreatorSettingsView( BaseSettingsView,  Ui_EventCreatorSettingsView, QtWidgets.QWidget):
    """
        EventCreatorView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        self.event_name_lineedit.init(self._parent_node.identifier, 'event_name', 
                                        self._pub_sub_manager)
        self.start_time_lineedit.init(self._parent_node.identifier, 'start_time',
                                        self._pub_sub_manager)
        self.duration_lineedit.init(self._parent_node.identifier, 'duration',
                                        self._pub_sub_manager)
        self.group_name_lineedit.init(self._parent_node.identifier, 'group_name',
                                        self._pub_sub_manager)
        self.channels_lineedit.init(self._parent_node.identifier, 'channels',
                                        self._pub_sub_manager)


    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass