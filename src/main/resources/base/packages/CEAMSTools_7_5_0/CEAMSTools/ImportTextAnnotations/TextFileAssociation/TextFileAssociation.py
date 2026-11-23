#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    TextFileAssociation
    Class to define the association between a text file and a PSG file.
"""

from qtpy import QtWidgets

from CEAMSTools.ImportTextAnnotations.TextFileAssociation.Ui_TextFileAssociation import Ui_TextFileAssociation
from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog

class TextFileAssociation(BaseStepView, Ui_TextFileAssociation, QtWidgets.QWidget):
    """
        TextFileAssociation
        Class to define the association between a text file and a PSG file.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        self._string_man_id = "351e5f9f-d4ee-4347-b554-230b558d2034" 
        # Subscribe to the proper topics to send/get data from the node
        self._prefix_topic = f'{self._string_man_id}.prefix'
        self._pub_sub_manager.subscribe(self, self._prefix_topic)
        self._suffix_topic = f'{self._string_man_id}.suffix'
        self._pub_sub_manager.subscribe(self, self._suffix_topic)
        

    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        self._pub_sub_manager.publish(self, self._prefix_topic, 'ping')
        self._pub_sub_manager.publish(self, self._suffix_topic, 'ping')


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
        if topic == self._prefix_topic:
           self.lineEdit_prefix.setText(message)
        if topic == self._suffix_topic:
           # Extract the extension after the last dot
           self.lineEdit_ext.setText(message.split('.')[-1])
           self.lineEdit_suffix.setText(message.split('.')[0])


    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._prefix_topic, \
            str(self.lineEdit_prefix.text()))
        suffix = self.lineEdit_suffix.text() + '.' + self.lineEdit_ext.text()
        self._pub_sub_manager.publish(self, self._suffix_topic, suffix)


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.

        # Make sure the extension is specified
        if self.lineEdit_ext.text() == '':
            WarningDialog("Please specify the extension of the text file")
            return False
        if (self.lineEdit_ext.text().lower() != "tsv" and self.lineEdit_ext.text().lower() != "txt" and self.lineEdit_ext.text().lower() != "csv"):
            WarningDialog("Unsupported extension. Please specify 'tsv', 'txt' or 'csv'")
            return False
        return True
