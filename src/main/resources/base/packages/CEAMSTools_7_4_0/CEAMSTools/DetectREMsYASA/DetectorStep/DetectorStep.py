#! /usr/bin/env python3
"""
    DetectorStep
    Step to set the thresholds for the REMs detection using YASA algorithm.
"""

from qtpy import QtWidgets, QtCore
from qtpy.QtCore import QTimer
from PySide6.QtCore import *

from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState
from widgets.WarningDialog import WarningDialog


from CEAMSTools.DetectREMsYASA.DetectorStep.Ui_DetectorStep import Ui_DetectorStep

from qtpy import QtWidgets

class DetectorStep(BaseStepView, Ui_DetectorStep, QtWidgets.QWidget):
    """
        DetectorStep
        Step to set the thresholds for the REMs detection using YASA algorithm.
        This step is used to set the parameters for the YASA algorithm.
        The parameters are:
        - relative prominence: the minimum relative prominence of the peaks to be detected.
        - remove outliers: whether to remove outliers from the data.
        - REMs event name: the name of the REMs event.
        - REMs event group: the group of the REMs event.
        - Sleep stages: Which sleep stages to include in the analysis. Default: 5 (REM)
        - AmpIdx0: the minimum amplitude.
        - AmpIdx1: the maximum amplitude.
        - DurIdx0: the minum duration of REMs.
        - DurIdx1: the maximum duration of REMs.
        - FreqIdx0: the minimum frequency of the REMs.
        - FreqIdx1: the maximum frequency of the REMs.

    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # set the spinbox values
        self.doubleSpinBox_2.setValue(0.8)
        self.spinBox_2.setValue(50)
        self.spinBox.setValue(325)
        self.doubleSpinBox_6.setValue(0.3)
        self.doubleSpinBox_5.setValue(1.5)
        self.doubleSpinBox.setValue(0.5)
        self.doubleSpinBox_3.setValue(5.0)

        # Connect checkBox_2 signal to handle frame enabling/disabling
        self.checkBox_2.setChecked(True)
        self.checkBox_2.stateChanged.connect(self.on_checkBox_2_changed)
        self.pushButton_CohortFilename.clicked.connect(self.browse_cohort_slot)

        # If necessary, init the context. The context is a memory space shared by 
        # all steps of a tool. It is used to share and notice other steps whenever
        # the value in it changes. It's very useful when the parameter within a step
        # must have an impact in another step.
        #self._context_manager["context_OutputFiles"] = {"the_data_I_want_to_share":"some_data"}

        # description.json file to know the ID of the node
        node_id_REMsDetectionYASA = "559de2e5-dc78-4449-8582-cc9f3fdd9697"
        self._relative_prominence_topic = f'{node_id_REMsDetectionYASA}.relative_prominence'
        self._pub_sub_manager.subscribe(self, self._relative_prominence_topic)

        self._remove_outliers_topic = f'{node_id_REMsDetectionYASA}.remove_outliers'
        self._pub_sub_manager.subscribe(self, self._remove_outliers_topic)

        self._rems_event_name_topic = f'{node_id_REMsDetectionYASA}.rems_event_name'
        self._pub_sub_manager.subscribe(self, self._rems_event_name_topic)

        self._rems_event_group_topic = f'{node_id_REMsDetectionYASA}.rems_event_group'
        self._pub_sub_manager.subscribe(self, self._rems_event_group_topic)

        self._include_topic = f'{node_id_REMsDetectionYASA}.include'
        self._pub_sub_manager.subscribe(self, self._include_topic)

        node_id_AmpTuple = "e00964ea-3df6-4aaa-8403-e2b75137a539"
        self._AmpIdx0_topic = f'{node_id_AmpTuple}.Idx0'
        self._pub_sub_manager.subscribe(self, self._AmpIdx0_topic)

        node_id_AmpTuple = "e00964ea-3df6-4aaa-8403-e2b75137a539"
        self._AmpIdx1_topic = f'{node_id_AmpTuple}.Idx1'
        self._pub_sub_manager.subscribe(self, self._AmpIdx1_topic)

        node_id_DurTuple = "a064ba35-38d6-4d11-a54c-9758044fb9bf"
        self._DurIdx0_topic = f'{node_id_DurTuple}.Idx0'
        self._pub_sub_manager.subscribe(self, self._DurIdx0_topic)

        node_id_DurTuple = "a064ba35-38d6-4d11-a54c-9758044fb9bf"
        self._DurIdx1_topic = f'{node_id_DurTuple}.Idx1'
        self._pub_sub_manager.subscribe(self, self._DurIdx1_topic)

        node_id_FreqTuple = "be8b0065-d6f1-4dea-82ee-eda181f655ab"
        self._FreqIdx0 = f'{node_id_FreqTuple}.Idx0'
        self._pub_sub_manager.subscribe(self, self._FreqIdx0)

        node_id_FreqTuple = "be8b0065-d6f1-4dea-82ee-eda181f655ab"
        self._FreqIdx1 = f'{node_id_FreqTuple}.Idx1'
        self._pub_sub_manager.subscribe(self, self._FreqIdx1)

        self._node_id_REMsDetails = "d1489e58-7c3d-490e-9c36-f830c8dc596e"
        self._det_param_topic = f'{self._node_id_REMsDetails}.rems_det_param'
        self._pub_sub_manager.subscribe(self, self._det_param_topic)
        self._cohort_file_topic = f'{self._node_id_REMsDetails}.cohort_filename'
        self._pub_sub_manager.subscribe(self, self._cohort_file_topic)

    def on_checkBox_2_changed(self):
        """Handle the state change of checkBox_2"""
        is_checked = self.checkBox_2.isChecked()
        self.label_16.setEnabled(is_checked)
        self.frame_8.setEnabled(is_checked)


    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        self._pub_sub_manager.publish(self, self._relative_prominence_topic, 'ping')
        self._pub_sub_manager.publish(self, self._remove_outliers_topic, 'ping')
        self._pub_sub_manager.publish(self, self._rems_event_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._rems_event_group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._include_topic, 'ping')
        self._pub_sub_manager.publish(self, self._AmpIdx0_topic, 'ping')
        self._pub_sub_manager.publish(self, self._AmpIdx1_topic, 'ping')
        self._pub_sub_manager.publish(self, self._DurIdx0_topic, 'ping')
        self._pub_sub_manager.publish(self, self._DurIdx1_topic, 'ping')
        self._pub_sub_manager.publish(self, self._FreqIdx0, 'ping')
        self._pub_sub_manager.publish(self, self._FreqIdx1, 'ping')
        self._pub_sub_manager.publish(self, self._cohort_file_topic, 'ping')
        

    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.

            # The message will be the KEY of the value that's been updated inside the context.
            # If it's the one you are looking for, we can then take the updated value and use it.
            #if message == "context_some_other_step":
                #updated_value = self._context_manager["context_some_other_step"]
        pass


    def on_topic_response(self, topic, message, sender):
        # This will be called as a response to ping request.
        if topic == self._relative_prominence_topic:
           self.doubleSpinBox_2.setValue(message)
        if topic == self._remove_outliers_topic:
           self.checkBox.setChecked(message)
        if topic == self._rems_event_name_topic:
            self.lineEdit_2.setText(message)
        if topic == self._rems_event_group_topic:
            self.lineEdit.setText(message)
        if topic == self._include_topic:
            self.lineEdit_3.setText(message)
        if topic == self._AmpIdx0_topic:
            self.spinBox_2.setValue(message)
        if topic == self._AmpIdx1_topic:
            self.spinBox.setValue(message)
        if topic == self._DurIdx0_topic:
            self.doubleSpinBox_6.setValue(message)
        if topic == self._DurIdx1_topic:
            self.doubleSpinBox_5.setValue(message)
        if topic == self._FreqIdx0:
            self.doubleSpinBox.setValue(message)
        if topic == self._FreqIdx1:
            self.doubleSpinBox_3.setValue(message)
        if topic == self._cohort_file_topic:
            self.lineEdit_CohortFilename.setText(message)

    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._relative_prominence_topic, self.doubleSpinBox_2.value())
        self._pub_sub_manager.publish(self, self._remove_outliers_topic, self.checkBox.isChecked())
        self._pub_sub_manager.publish(self, self._rems_event_name_topic, self.lineEdit_2.text())
        self._pub_sub_manager.publish(self, self._rems_event_group_topic, self.lineEdit.text())
        self._pub_sub_manager.publish(self, self._include_topic, self.lineEdit_3.text())
        self._pub_sub_manager.publish(self, self._AmpIdx0_topic, self.spinBox_2.value())
        self._pub_sub_manager.publish(self, self._AmpIdx1_topic, self.spinBox.value())
        self._pub_sub_manager.publish(self, self._DurIdx0_topic, self.doubleSpinBox_6.value())
        self._pub_sub_manager.publish(self, self._DurIdx1_topic, self.doubleSpinBox_5.value())
        self._pub_sub_manager.publish(self, self._FreqIdx0, self.doubleSpinBox.value())
        self._pub_sub_manager.publish(self, self._FreqIdx1, self.doubleSpinBox_3.value())
        self._pub_sub_manager.publish(self, self._cohort_file_topic, self.lineEdit_CohortFilename.text())
        
        # Build the dictionary of section selection to run detector and the detector parameters
        if len(self.lineEdit_3.text()) > 1:
            stage_sel = self.lineEdit_3.text().strip('[]')
        elif len(self.lineEdit_3.text()) == 1:
            stage_sel = str(self.lineEdit_3.text())
        else:
            stage_sel = ''
        det_param = {}
        det_param["stage_sel"] = stage_sel
        det_param["rems_event_name"] = str(self.lineEdit_2.text())

        self._pub_sub_manager.publish(self, self._det_param_topic, str(det_param))
    # Slot called when the user wants to write the filename
    def on_choose(self):
        pass

    def on_active_validation(self):
        pass

    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if len(self.lineEdit_CohortFilename.text())==0:
            WarningDialog("Define a file to write the detailed events report for the cohort. In step '3-Detector Step'")
            return False
        return True

    # Called when the user delete an instance of the plugin
    def __del__(self):
        pass

    # Called when the user press the browse button to define where to save the cohort report
    def browse_cohort_slot(self):
        # define the option to disable the warning dialog when overwriting an existing file
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, 
            'Save as TSV file', 
            None, 
            'TSV (*.tsv)',
            options = QtWidgets.QFileDialog.DontConfirmOverwrite)
        if filename != '':
            self.lineEdit_CohortFilename.setText(filename)
