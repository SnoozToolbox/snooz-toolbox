"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    FilterSignalsStep
    Settings viewer of the filters (artefact rejection)
    This custom step is usefull to use context with filters.
"""

from qtpy import QtWidgets

from commons.BaseStepView import BaseStepView
import config
from flowpipe.ActivationState import ActivationState

from widgets.WarningDialog import WarningDialog

from CEAMSTools.PowerSpectralAnalysis.SelectionStep.Ui_SelectionStep import Ui_SelectionStep

class SelectionStep( BaseStepView,  Ui_SelectionStep, QtWidgets.QWidget):
    """
        Filtering
        Settings viewer of the filters (PSA)
        This custom step is usefull to use context with filters.
    """

    # Key for the context shared with other step of the preset
    context_PSA_annot_selection = "annotation_selection"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules and nodes to talk to
        self._node_id_SleepCycleDelimiter = "86d696d6-7dfa-43e8-8c16-7aad297478ab" # to activate when PSA is performed on stages 
        self._node_id_SleepStageEvent = "137420bc-d6ce-4928-a040-7121ba024020" # provide in which sleep stage and periods we analyse the spectral power
        self._node_id_SignalsFromEvents = "90827a66-36fb-494c-8f90-d67d8e19a703"  # to activate when PSA is performed on stages 
        self._node_id_ResetSignalArtefact = "1211ee97-72e4-45da-9850-44d4aa249c78"  # to activate when PSA is performed on stages 
        self._node_id_STFT_std = "159bfdad-5000-474b-ae38-8e95ff4142b2"  # to activate when PSA is performed on stages 
        self._node_id_PSA_Compilation_std = "4bb8c9ac-64e8-4cec-9c2c-5a00c80b4eae" # to activate when PSA is performed on stages

        # Define modules to activate or bypass
        self._node_id_SignalsFromEvents_Annot = "d3620a6b-03f5-444f-b93e-e3ca23983b56" # To activate for PSA on annot
        self._node_id_STFT_Annot = "ea31a87d-038c-4e24-a9c2-66b54aaca483" # To activate for PSA on annot
        self._node_id_ResetSignal_art = "83092505-93c5-4688-acc7-208d00a72ba0" # To activate for PSA on annot
        self._node_id_PSA_Annot = "9dfbe6b9-1887-452a-ac3b-33f1235f9b0a"  # provide the band width to the PSA on Events 

        self._context_manager[SelectionStep.context_PSA_annot_selection] = 0

        # Input node topic
        # Sleep stage and cycle selection
        self._stages_topic = f'{self._node_id_SleepStageEvent}.stages'
        self._pub_sub_manager.subscribe(self, self._stages_topic)
        self._exclude_nremp_topic = f'{self._node_id_SleepStageEvent}.exclude_nremp'
        self._pub_sub_manager.subscribe(self, self._exclude_nremp_topic)
        self._exclude_remp_topic = f'{self._node_id_SleepStageEvent}.exclude_remp'
        self._pub_sub_manager.subscribe(self, self._exclude_remp_topic)
        self._in_cycle_topic = f'{self._node_id_SleepStageEvent}.in_cycle'    


    def load_settings(self):
        self._pub_sub_manager.publish(self, self._stages_topic, 'ping')
        self._pub_sub_manager.publish(self, self._exclude_nremp_topic, 'ping')
        self._pub_sub_manager.publish(self, self._exclude_remp_topic, 'ping')
        self._pub_sub_manager.publish(self, self._in_cycle_topic, 'ping')

        # To activate the PSA on sleep stage or annotations branch
        self._pub_sub_manager.publish(self, self._node_id_SleepCycleDelimiter+".get_activation_state", None)
        self.NREM_stages_and_periods_slot()
        self.REM_stages_and_periods_slot()


    # Called when the user clic on RUN
    # Message are sent to the publisher
    def on_apply_settings(self):
        # Get the selected stages
        stages_str = self.get_stages()
        self._pub_sub_manager.publish(self, self._stages_topic, str(stages_str))
        self._pub_sub_manager.publish(self, self._exclude_nremp_topic, self.excl_nremp_checkBox.isChecked())
        self._pub_sub_manager.publish(self, self._exclude_remp_topic, self.excl_remp_checkBox.isChecked())
        self._pub_sub_manager.publish(self, self._in_cycle_topic, self.in_cycle_checkBox.isChecked())   

        if self.radioButton_sleep.isChecked():

            # Activate the modules needed to run on sleep stages
            self._pub_sub_manager.publish(self, self._node_id_SleepCycleDelimiter\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SleepStageEvent\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SignalsFromEvents\
                +".activation_state_change", ActivationState.ACTIVATED)       
            self._pub_sub_manager.publish(self, self._node_id_ResetSignalArtefact\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_STFT_std\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_Compilation_std\
                +".activation_state_change", ActivationState.ACTIVATED)    

            # Deactivate the modules needed to run on annotations
            self._pub_sub_manager.publish(self, self._node_id_SignalsFromEvents_Annot\
                +".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_STFT_Annot\
                +".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_ResetSignal_art\
                +".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_Annot\
                +".activation_state_change",ActivationState.DEACTIVATED)        

        if self.radioButton_annotations.isChecked():

            # Activate the modules needed to run on annotations
            self._pub_sub_manager.publish(self, self._node_id_SignalsFromEvents_Annot\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_STFT_Annot\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_ResetSignal_art\
                +".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_Annot\
                +".activation_state_change",ActivationState.ACTIVATED)

            # Deactivate the modules needed to run on sleep stages
            self._pub_sub_manager.publish(self, self._node_id_SleepCycleDelimiter\
                +".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SleepStageEvent\
                +".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SignalsFromEvents\
                +".activation_state_change", ActivationState.DEACTIVATED)       
            self._pub_sub_manager.publish(self, self._node_id_ResetSignalArtefact\
                +".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_STFT_std\
                +".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSA_Compilation_std\
                +".activation_state_change", ActivationState.DEACTIVATED)            


    # Called by a node in response to a ping request. 
    # Ping request are sent whenever we need to know the value of a parameter of a node.
    def on_topic_response(self, topic, message, sender):
        if topic == self._stages_topic:
            stages_lst = message.split(',')
            self.n1_checkBox.setChecked('1' in stages_lst)
            self.n2_checkBox.setChecked('2' in stages_lst)
            self.n3_checkBox.setChecked('3' in stages_lst)
            self.nrem_checkBox.setChecked(('1' in stages_lst) and ('2' in stages_lst) and ('3' in stages_lst))
            self.s4_checkBox.setChecked('4' in stages_lst)
            self.r_checkBox.setChecked('5' in stages_lst)
            self.w_checkBox.setChecked('0' in stages_lst)
            self.unscored_checkBox.setChecked('9' in stages_lst)
        if topic == self._exclude_nremp_topic:
            self.excl_nremp_checkBox.setChecked(int(message))
        if topic == self._exclude_remp_topic:
            self.excl_remp_checkBox.setChecked(int(message))
        if topic == self._in_cycle_topic:
            self.in_cycle_checkBox.setChecked(int(message))
        if topic == self._node_id_SleepCycleDelimiter+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.radioButton_sleep.setChecked(True)
            else:
                self.radioButton_annotations.setChecked(True)
            self.update_section_selection_slot()


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._stages_topic)
            self._pub_sub_manager.unsubscribe(self, self._exclude_nremp_topic)
            self._pub_sub_manager.unsubscribe(self, self._exclude_remp_topic)
            self._pub_sub_manager.unsubscribe(self, self._in_cycle_topic)


    # Called when the user changes the radio button of the section selection
    # Sleep stages and cycles versus annotations
    def update_section_selection_slot(self):
        if self.radioButton_sleep.isChecked():
            self._enable_widgets(True)
        else:
            self._enable_widgets(False)
        self._context_manager[SelectionStep.context_PSA_annot_selection] = 1 if self.radioButton_annotations.isChecked() else 0


    # Called when the user changes the stages or period selection
    #  The NREM stages selection desables the NREM period exclusion
    def NREM_stages_and_periods_slot(self):
        nrem_stages_selection = self.nrem_checkBox.isChecked() or self.n2_checkBox.isChecked() or self.n3_checkBox.isChecked()
        if nrem_stages_selection:
            self.excl_nremp_checkBox.setChecked(False)
            self.excl_nremp_checkBox.setEnabled(False)
        else:
            self.excl_nremp_checkBox.setEnabled(True)


    # Called when the user changes the stages or period selection
    #  The R stage selection desables the REM period exclusion
    def REM_stages_and_periods_slot(self):
        rem_stages_selection = self.r_checkBox.isChecked()
        if rem_stages_selection:
            self.excl_remp_checkBox.setChecked(False)
            self.excl_remp_checkBox.setEnabled(False)
        else:
            self.excl_remp_checkBox.setEnabled(True)


    def _enable_widgets(self, bool_flag):
        # Disable all the widgets to make sure the user does not check/uncheck them
        self.unscored_checkBox.setEnabled(bool_flag)
        self.n1_checkBox.setEnabled(bool_flag)
        self.n2_checkBox.setEnabled(bool_flag)
        self.n3_checkBox.setEnabled(bool_flag)
        self.nrem_checkBox.setEnabled(bool_flag)
        self.r_checkBox.setEnabled(bool_flag)
        self.w_checkBox.setEnabled(bool_flag)
        self.excl_nremp_checkBox.setEnabled(bool_flag)
        self.excl_remp_checkBox.setEnabled(bool_flag)
        self.in_cycle_checkBox.setEnabled(bool_flag)
        self.label_2.setEnabled(bool_flag)
        self.label_3.setEnabled(bool_flag)
        self.label_4.setEnabled(bool_flag)
        self.label_5.setEnabled(bool_flag)
        self.label_7.setEnabled(bool_flag)
        self.plainTextEdit.setEnabled(bool_flag)
        self.plainTextEdit_2.setEnabled(bool_flag)
        # If the PSA is performed on annotations
        # Select all stages and do not exclude period
        if not bool_flag:
            self.unscored_checkBox.setChecked(True)
            self.n1_checkBox.setChecked(True)
            self.n2_checkBox.setChecked(True)
            self.n3_checkBox.setChecked(True)
            self.nrem_checkBox.setChecked(True)
            self.r_checkBox.setChecked(True)
            self.w_checkBox.setChecked(True)
            self.excl_nremp_checkBox.setChecked(False)
            self.excl_remp_checkBox.setChecked(False)
            self.in_cycle_checkBox.setChecked(False)


    # Called when the user check/uncheck the NREM checkbox
    def NREM_checkbox_slot(self):
        self.n1_checkBox.setChecked(self.nrem_checkBox.isChecked())
        self.n2_checkBox.setChecked(self.nrem_checkBox.isChecked())
        self.n3_checkBox.setChecked(self.nrem_checkBox.isChecked())


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        stages_str = self.get_stages()
        if len(stages_str)==0:
            WarningDialog(f"At least one stage must be selected, see step '4-Section Selection'.")
            return False
        return True   


    def get_stages(self):
        # Convert the sleep stage selection for the input plugin
        stages_str = ''
        if self.n1_checkBox.isChecked():
            if len(stages_str)==0:
                stages_str = '1'
            else:
                stages_str = stages_str+',1'
        if self.n2_checkBox.isChecked():
            if len(stages_str)==0:
                stages_str = '2'
            else:
                stages_str = stages_str+',2'
        if self.n3_checkBox.isChecked():
            if len(stages_str)==0:
                stages_str = '3'
            else:
                stages_str = stages_str+',3'
        if self.s4_checkBox.isChecked():
            if len(stages_str)==0:
                stages_str = '4'
            else:
                stages_str = stages_str+',4'       
        if self.r_checkBox.isChecked():
            if len(stages_str)==0:
                stages_str = '5'
            else:
                stages_str = stages_str+',5'
        if self.w_checkBox.isChecked():
            if len(stages_str)==0:
                stages_str = '0'
            else:
                stages_str = stages_str+',0'     
        if self.unscored_checkBox.isChecked():
            if len(stages_str)==0:
                stages_str = '9'
            else:
                stages_str = stages_str+',9'     
        return stages_str