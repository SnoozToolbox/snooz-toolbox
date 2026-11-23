"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    Settings viewer of the REMsEventsToMiniEpochs plugin
"""

from qtpy import QtWidgets

from CEAMSModules.REMsEventsToMiniEpochs.Ui_REMsEventsToMiniEpochsSettingsView import Ui_REMsEventsToMiniEpochsSettingsView
from commons.BaseSettingsView import BaseSettingsView

class REMsEventsToMiniEpochsSettingsView(BaseSettingsView, Ui_REMsEventsToMiniEpochsSettingsView, QtWidgets.QWidget):
    """
        REMsEventsToMiniEpochsView set the REMsEventsToMiniEpochs settings
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
        self.paramters = {'mini_epoch_group': 'DET_MOR', 'mini_epoch_name_Phasic': 'Snooz_MOR_Phasic', 'mini_epoch_name_Tonic': 'Snooz_MOR_Tonic'}

        
    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._parameters_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        self.update_parameters_from_UI()
        # Send the settings to the publisher for inputs to SignalGenerator
        self._pub_sub_manager.publish(self, self._parameters_topic, self.paramters)
            
            
    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView
        """
        if topic == self._parameters_topic:
            if isinstance(message, str) and not message == '':
                message = eval(message)
            if isinstance(message, dict):
                self.paramters = message
                self.update_UI_from_parameters()


    def update_UI_from_parameters(self):
        self.lineEdit_group.setText(self.paramters['mini_epoch_group'])
        self.lineEdit_name_Phasic.setText(self.paramters['mini_epoch_name_Phasic'])
        self.lineEdit_name_Tonic.setText(self.paramters['mini_epoch_name_Tonic'])


    def update_parameters_from_UI(self):
        self.paramters['mini_epoch_group'] = self.lineEdit_group.text()
        self.paramters['mini_epoch_name_Phasic'] = self.lineEdit_name_Phasic.text()
        self.paramters['mini_epoch_name_Tonic'] = self.lineEdit_name_Tonic.text()