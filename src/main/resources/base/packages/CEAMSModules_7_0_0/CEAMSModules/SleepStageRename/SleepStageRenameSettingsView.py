"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the SleepStageRename plugin
"""

from qtpy import QtWidgets

from CEAMSModules.SleepStageRename.Ui_SleepStageRenameSettingsView import Ui_SleepStageRenameSettingsView
from commons.BaseSettingsView import BaseSettingsView
from ..PSGReader import commons

class SleepStageRenameSettingsView( BaseSettingsView,  Ui_SleepStageRenameSettingsView, QtWidgets.QWidget):
    """
        SleepStageRenameSettingsView display the settings for SleepStageRename.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        
        # Dict to keep track of the fixed keys.
        # Extract keys as a list
        self.default_keys = list(commons.sleep_stages_name.keys())
        # Conversion LUT : load the default values
        self.default_LUT_stage_name = commons.sleep_stages_name
        # Dict to fill line edit for the original names
        self.ori_stage_names = {}
        for key in self.default_LUT_stage_name.keys():
            self.ori_stage_names[key] = key
        # Dict to fill line edit for the new names
        self.new_stage_names = self.default_LUT_stage_name
        # Dict to rename the event group
        self.group = {}
        self.group[commons.sleep_stages_group] = commons.sleep_stages_group

        # Fill the line edit from the dict
        self.fill_lineEdit_group()
        self.fill_ori_lineEdit()
        self.fill_new_lineEdit()     

        # Subscribe to the proper topics to send/get data from the node
        # stages_names dict converted into a string
        self._group_lut_topic = f'{self._parent_node.identifier}.group_lut'
        self._pub_sub_manager.subscribe(self, self._group_lut_topic)        
        self._ori_stage_names_topic = f'{self._parent_node.identifier}.original_name'
        self._pub_sub_manager.subscribe(self, self._ori_stage_names_topic)
        self._new_stage_names_topic = f'{self._parent_node.identifier}.new_name'
        self._pub_sub_manager.subscribe(self, self._new_stage_names_topic)


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._group_lut_topic, 'ping')
        self._pub_sub_manager.publish(self, self._ori_stage_names_topic, 'ping')
        self._pub_sub_manager.publish(self, self._new_stage_names_topic, 'ping')


    # Called when the user clicks on "Apply"
    def on_apply_settings(self):

        self.group = {}
        self.group[str(self.lineEdit_group_ori.text())] = str(self.lineEdit_group_new.text())

        # ori_stage_names is the dict to maintain the lineEdit_ori and
        # send a string of the dict to the SleepStageRename plugin
        self.ori_stage_names[self.default_keys[0]] = str(self.lineEdit_ori_0.text())
        self.ori_stage_names[self.default_keys[1]] = str(self.lineEdit_ori_1.text())
        self.ori_stage_names[self.default_keys[2]] = str(self.lineEdit_ori_2.text())
        self.ori_stage_names[self.default_keys[3]] = str(self.lineEdit_ori_3.text())
        self.ori_stage_names[self.default_keys[4]] = str(self.lineEdit_ori_4.text())
        self.ori_stage_names[self.default_keys[5]] = str(self.lineEdit_ori_5.text())
        self.ori_stage_names[self.default_keys[6]] = str(self.lineEdit_ori_6.text())
        self.ori_stage_names[self.default_keys[7]] = str(self.lineEdit_ori_7.text())
        self.ori_stage_names[self.default_keys[9]] = str(self.lineEdit_ori_9.text())

        # new_stage_names is the dict to maintain the lineEdit_new and
        # send a string of the dict to the SleepStageRename plugin
        self.new_stage_names[self.default_keys[0]] = str(self.lineEdit_new_0.text())
        self.new_stage_names[self.default_keys[1]] = str(self.lineEdit_new_1.text())    
        self.new_stage_names[self.default_keys[2]] = str(self.lineEdit_new_2.text())
        self.new_stage_names[self.default_keys[3]] = str(self.lineEdit_new_3.text()) 
        self.new_stage_names[self.default_keys[4]] = str(self.lineEdit_new_4.text())
        self.new_stage_names[self.default_keys[5]] = str(self.lineEdit_new_5.text()) 
        self.new_stage_names[self.default_keys[6]] = str(self.lineEdit_new_6.text())
        self.new_stage_names[self.default_keys[7]] = str(self.lineEdit_new_7.text()) 
        self.new_stage_names[self.default_keys[9]] = str(self.lineEdit_new_9.text()) 

        # Messages are sent to the publisher
        self._pub_sub_manager.publish(self, self._group_lut_topic, \
            str(self.group))        
        self._pub_sub_manager.publish(self, self._ori_stage_names_topic, \
            str(self.ori_stage_names))
        self._pub_sub_manager.publish(self, self._new_stage_names_topic, \
            str(self.new_stage_names))


    def on_topic_update(self, topic, message, sender):
        pass


    # Called by the publisher to display settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._group_lut_topic:
            self.group = eval(message)
            self.fill_lineEdit_group()
        if topic == self._ori_stage_names_topic:
            self.ori_stage_names = eval(message)
            self.fill_ori_lineEdit()         
        if topic == self._new_stage_names_topic:
            self.new_stage_names = eval(message)
            self.fill_new_lineEdit()


    # To fill the line edit in the settings view from the dictionary
    def fill_ori_lineEdit(self):
        self.lineEdit_ori_0.setText(str(self.ori_stage_names[self.default_keys[0]])) 
        self.lineEdit_ori_1.setText(str(self.ori_stage_names[self.default_keys[1]])) 
        self.lineEdit_ori_2.setText(str(self.ori_stage_names[self.default_keys[2]])) 
        self.lineEdit_ori_3.setText(str(self.ori_stage_names[self.default_keys[3]])) 
        self.lineEdit_ori_4.setText(str(self.ori_stage_names[self.default_keys[4]])) 
        self.lineEdit_ori_5.setText(str(self.ori_stage_names[self.default_keys[5]])) 
        self.lineEdit_ori_6.setText(str(self.ori_stage_names[self.default_keys[6]])) 
        self.lineEdit_ori_7.setText(str(self.ori_stage_names[self.default_keys[7]])) 
        self.lineEdit_ori_9.setText(str(self.ori_stage_names[self.default_keys[9]]))         


    # To fill the line edit in the settings view from the dictionary
    def fill_new_lineEdit(self):
        self.lineEdit_new_0.setText(str(self.new_stage_names[self.default_keys[0]]))
        self.lineEdit_new_1.setText(str(self.new_stage_names[self.default_keys[1]]))
        self.lineEdit_new_2.setText(str(self.new_stage_names[self.default_keys[2]])) 
        self.lineEdit_new_3.setText(str(self.new_stage_names[self.default_keys[3]])) 
        self.lineEdit_new_4.setText(str(self.new_stage_names[self.default_keys[4]])) 
        self.lineEdit_new_5.setText(str(self.new_stage_names[self.default_keys[5]])) 
        self.lineEdit_new_6.setText(str(self.new_stage_names[self.default_keys[6]])) 
        self.lineEdit_new_7.setText(str(self.new_stage_names[self.default_keys[7]]))    
        self.lineEdit_new_9.setText(str(self.new_stage_names[self.default_keys[9]]))      


    def fill_lineEdit_group(self):
        # Extract the original and new group 
        group_ori = list(self.group.keys())[0]
        group_new = list(self.group.values())[0]            
        self.lineEdit_group_ori.setText(str(group_ori))
        self.lineEdit_group_new.setText(str(group_new))


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._ori_stage_names_topic)  
            self._pub_sub_manager.unsubscribe(self, self._new_stage_names_topic)  