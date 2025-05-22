#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Société en Commandite – 2025
See the file LICENCE for full license details.
"""

"""
    This step is used to export the results of the sleep staging algorithm.
"""

from qtpy import QtWidgets, QtCore
from qtpy.QtCore import QTimer
from PySide6.QtCore import *

#from CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep import InputFilesStep
from CEAMSTools.ScoreSleepStagesYASA.ExportResultsStep.Ui_ExportResultsStep import Ui_ExportResultsStep
from commons.BaseStepView import BaseStepView

from widgets.WarningDialogWithButtons import WarningDialogWithButtons
from widgets.WarningDialog import WarningDialog


class ExportResultsStep( BaseStepView,  Ui_ExportResultsStep, QtWidgets.QWidget):
    

    """
        ExportResultsStep describes the step to export the results of the sleep staging algorithm.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Set checkbox as checked and disabled
        self.checkBox.setChecked(True)
        self.checkBox.setEnabled(False)
        
        # Disable label_3
        self.label_3.setEnabled(False)
        
        # Connect checkBox_2 signal to handle frame enabling/disabling
        self.checkBox_2.stateChanged.connect(self.on_checkBox_2_changed)
        
        # Initial state of frames based on checkBox_2
        self.on_checkBox_2_changed()

        # description.json file to know the ID of the node
        node_id_writer = "45e14f5d-5a72-4aaf-bf01-644c095979d6"
        self._SavedDestination_topic = f'{node_id_writer}.SavedDestination'
        self._pub_sub_manager.subscribe(self, self._SavedDestination_topic)
        self._Checkbox_topic2 = f'{node_id_writer}.Checkbox'
        self._pub_sub_manager.subscribe(self, self._Checkbox_topic2)

        node_id_YASA = "e58aa07b-4802-45f7-92c2-61f6f19b1818"
        self._stage_group_topic = f'{node_id_YASA}.stage_group'
        self._pub_sub_manager.subscribe(self, self._stage_group_topic)
        self._Checkbox_topic = f'{node_id_YASA}.validation_on'
        self._pub_sub_manager.subscribe(self, self._Checkbox_topic)

        self.lineEdit.setPlaceholderText(QCoreApplication.translate("OutputFiles", u"Select a folder where the exported files are supposed to be saved", None))
        # Connect the browse push button to the browse_slot function
        self.pushButton.clicked.connect(self.browse_slot)


    def on_checkBox_2_changed(self):
        """Handle the state change of checkBox_2"""
        is_checked = self.checkBox_2.isChecked()
        self.frame_6.setEnabled(is_checked)
        self.frame_8.setEnabled(is_checked)
        self.frame_9.setEnabled(is_checked)


    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        self._pub_sub_manager.publish(self, self._SavedDestination_topic, 'ping')
        self._pub_sub_manager.publish(self, self._Checkbox_topic, 'ping')
        self._pub_sub_manager.publish(self, self._stage_group_topic, 'ping')


    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.
        pass


    def on_topic_response(self, topic, message, sender):
        # This will be called as a response to ping request.
        if topic == self._SavedDestination_topic:
           self.lineEdit.setText(message)
        if topic == self._stage_group_topic:
           self.lineEdit_2.setText(str(message))
        if topic == self._Checkbox_topic:
            self.checkBox_2.setChecked(message)
    

    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._SavedDestination_topic, self.lineEdit.text())
        self._pub_sub_manager.publish(self, self._stage_group_topic, self.lineEdit_2.text())
        self._pub_sub_manager.publish(self, self._Checkbox_topic, self.checkBox_2.isChecked())
        self._pub_sub_manager.publish(self, self._Checkbox_topic2, self.checkBox_2.isChecked())


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if len(self.lineEdit.text())==0 and self.checkBox_2.isChecked():
            WarningDialog(f"You need to define the output destination in step '3 - Export Results.")
            return False
        if self.lineEdit_2.text() == 'stage':
            if WarningDialogWithButtons.show_warning(f"If you do not change the group label, the predicted sleep stages group label will be overwritten with 'stage', which is the gold standard."):
                return True
            else:
                return False
        if self.lineEdit_2.text() == '':
            WarningDialog(f"You need to define the group label in step '3 - Export Results.")
            return False
        
        return True
    

    # Called when the user clicks on the browse push button
    def browse_slot(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            None, 
            'Select Directory', 
            '', 
            QtWidgets.QFileDialog.ShowDirsOnly | QtWidgets.QFileDialog.DontResolveSymlinks)
        if directory:
            if not directory.endswith('/') and not directory.endswith('\\'):
                directory += '/'
            self.lineEdit.setText(directory)
