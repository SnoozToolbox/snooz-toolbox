#! /usr/bin/env python3
"""
    OutputFilesStep
    Step in the CompareEventsFromPSG tool to define the output file.
"""

from qtpy import QtWidgets

from flowpipe.ActivationState import ActivationState
from commons.BaseStepView import BaseStepView

from CEAMSTools.CompareEventsFromPSG.OutputFilesStep.Ui_OutputFilesStep import Ui_OutputFilesStep

class OutputFilesStep(BaseStepView, Ui_OutputFilesStep, QtWidgets.QWidget):
    """
        OutputFilesStep
        Step in the CompareEventsFromPSG tool to define the output file.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # If necessary, init the context. The context is a memory space shared by 
        # all steps of a tool. It is used to share and notice other steps whenever
        # the value in it changes. It's very useful when the parameter within a step
        # must have an impact in another step.
        #self._context_manager["context_OutputFilesStep"] = {"the_data_I_want_to_share":"some_data"}

        # You need to look into your process.json file to know the ID of the node you are interest in.
        identifier = "5e16792a-8831-4724-8d24-889de631b2f5" # StringManip to define the output filename
        self._out_suffix_topic = identifier + ".suffix" 
        identifier = "55db0fc9-bb11-4cb8-9286-df8479c3847d" # EventCompare to define the jaccord index threshold
        self._jaccord_topic = identifier + ".jaccord_thresh" 
        identifier = "14e35396-fdc5-4dc0-a24f-3bfa9d72bd7b" # FilterEvents for detections
        self._stage_sel_det_topic = identifier + ".stages_selection" 
        identifier = "6bb6ff63-c4d6-4be3-96dd-f4e9e0d1387b" # FilterEvents for expert events
        self._stage_sel_exp_topic = identifier + ".stages_selection" 
        self._node_id_TP_writer = "54f6830a-80bd-4d3c-acf3-cfa091af1dbf" # TP writer
        self._node_id_FNFP_writer = "5ce84e3c-17f7-4488-9fbd-635c77322495" # FNFP writer
        
        
    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        self._pub_sub_manager.publish(self, self._out_suffix_topic, 'ping')
        self._pub_sub_manager.publish(self, self._jaccord_topic, 'ping')
        self._pub_sub_manager.publish(self, self._stage_sel_exp_topic, 'ping')
        self._pub_sub_manager.publish(self, self._node_id_TP_writer+".get_activation_state", None)      
        self._pub_sub_manager.publish(self, self._node_id_FNFP_writer+".get_activation_state", None)      


    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.
        #if topic == self._context_manager.topic:

            # The message will be the KEY of the value that's been updated inside the context.
            # If it's the one you are looking for, we can then take the updated value and use it.
            #if message == "context_some_other_step":
                #updated_value = self._context_manager["context_some_other_step"]
        pass


    def on_topic_response(self, topic, message, sender):
        # This will be called as a response to ping request.
        if topic == self._out_suffix_topic:
            self.lineEdit_suffix.setText(message)
        if topic == self._jaccord_topic:
            self.lineEdit_jaccord.setText(message)
        if topic == self._stage_sel_exp_topic:
            stages_lst = message.split(',')
            self.checkBox_1.setChecked('1' in stages_lst)
            self.checkBox_2.setChecked('2' in stages_lst)
            self.checkBox_3.setChecked('3' in stages_lst)
            self.checkBox_4.setChecked('4' in stages_lst)
            self.checkBox_R.setChecked('5' in stages_lst)
            self.checkBox_W.setChecked('0' in stages_lst)
                

    # Called when the user clicks on RUN or when the pipeline is saved
    # Message are sent to the publisher   
    def on_apply_settings(self):
        if self.lineEdit_suffix.text()=='':
            self._pub_sub_manager.publish(self, self._out_suffix_topic, '_perf.tsv')
        elif '.tsv' in self.lineEdit_suffix.text():
            self._pub_sub_manager.publish(self, self._out_suffix_topic, self.lineEdit_suffix.text())
        else:
            self._pub_sub_manager.publish(self, self._out_suffix_topic, self.lineEdit_suffix.text()+'.tsv')
        self._pub_sub_manager.publish(self, self._jaccord_topic, self.lineEdit_jaccord.text())
        # Convert the sleep stage selection for the input plugin
        stages_str = ''
        if self.checkBox_1.isChecked():
            if len(stages_str)==0:
                stages_str = '1'
            else:
                stages_str = stages_str+',1'
        if self.checkBox_2.isChecked():
            if len(stages_str)==0:
                stages_str = '2'
            else:
                stages_str = stages_str+',2'
        if self.checkBox_3.isChecked():
            if len(stages_str)==0:
                stages_str = '3'
            else:
                stages_str = stages_str+',3'
        if self.checkBox_4.isChecked():
            if len(stages_str)==0:
                stages_str = '4'
            else:
                stages_str = stages_str+',4'       
        if self.checkBox_R.isChecked():
            if len(stages_str)==0:
                stages_str = '5'
            else:
                stages_str = stages_str+',5'
        if self.checkBox_W.isChecked():
            if len(stages_str)==0:
                stages_str = '0'
            else:
                stages_str = stages_str+',0'     
        self._pub_sub_manager.publish(self, self._stage_sel_det_topic, str(stages_str))
        self._pub_sub_manager.publish(self, self._stage_sel_exp_topic, str(stages_str))
        # To export TP
        if self.checkBox_TP_exp.isChecked():
            self._pub_sub_manager.publish(self, self._node_id_TP_writer\
                +".activation_state_change", ActivationState.ACTIVATED)
        else:
            self._pub_sub_manager.publish(self, self._node_id_TP_writer\
                +".activation_state_change", ActivationState.DEACTIVATED)            
        # To export FNFP
        if self.checkBox_FPFN_exp.isChecked():
            self._pub_sub_manager.publish(self, self._node_id_FNFP_writer \
                +".activation_state_change", ActivationState.ACTIVATED)
        else:
            self._pub_sub_manager.publish(self, self._node_id_FNFP_writer\
                +".activation_state_change", ActivationState.DEACTIVATED)
                