"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    Settings viewer of the TSVValidatorMaster plugin
"""

from qtpy import QtWidgets, QtCore, QtGui

from CEAMSModules.TSVValidatorMaster.Ui_TSVValidatorMasterSettingsView import Ui_TSVValidatorMasterSettingsView
from commons.BaseSettingsView import BaseSettingsView

class TSVValidatorMasterSettingsView(BaseSettingsView, Ui_TSVValidatorMasterSettingsView, QtWidgets.QWidget):
    """
        TSVValidatorMasterView set the TSVValidatorMaster settings
    """
    # To send a signal each time the self.files_model is modified
    # It allows to define QtCore.Slot() to do action each time the self.files_model is modified
    model_updated_signal = QtCore.Signal()
    
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_choose)
        self.pushButton_2.clicked.connect(self.listWidget.clear)
        self.pushButton_2.clicked.connect(self.clear_list_slot)

        # Subscribe to the proper topics to send/get data from the node
        self._files_topic = f'{self._parent_node.identifier}.files'
        self._pub_sub_manager.subscribe(self, self._files_topic)
        self.files_model = QtGui.QStandardItemModel(0,1)

    def load_files_from_data(self, data):
        self.listWidget.clear()
        self.files_model = QtGui.QStandardItemModel(0,1) 
        for filename in data:
            # Add files to listView
            self.listWidget.addItem(filename)
            # tree item : parent=file, child=name
            item = QtGui.QStandardItem(filename)
            self.files_model.appendRow(item) 
        # Generate a signal to inform that self.files_model has been updated
        self.model_updated_signal.emit()

    def clear_list_slot(self):
        self.listWidget.clear()
        # Clear the model
        # Important to remove the last row first since the model is updated after each removeRow
        # we dont want to change file index.
        for row in range(self.files_model.rowCount()-1,-1,-1):
            self.files_model.removeRow(row)
        # Generate a signal to inform that self.files_model has been updated
        self.model_updated_signal.emit() 

    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._files_topic, 'ping')
        


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to TSVValidatorMaster
        items = []
        for x in range(self.listWidget.count()):
            items.append(self.listWidget.item(x).text())
        self._pub_sub_manager.publish(self, self._files_topic, items)
        #self._pub_sub_manager.publish(self, self._files_topic, str(self.listWidget.currentItem().text()))


    # Slot called when user wants to add files
    def on_choose(self):
        filenames_add, _ = QtWidgets.QFileDialog.getOpenFileNames(
            None, 
            'Open CSV, TSV or TXT file', 
            None, 
            'CSV TSV (*.csv *.tsv *.txt)')
        if filenames_add != '':
            # Fill the QListWidget
            for filename in filenames_add:
                self.listWidget.addItem(filename)
                # tree item : parent=file, child=name
                item = QtGui.QStandardItem(filename)
                self.files_model.appendRow(item) 
            # Generate a signal to inform that self.files_model has been updated
            self.model_updated_signal.emit() 


    def on_topic_update(self, topic, message, sender):
        """ Only used in a custom step of a tool, you can ignore it.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._files_topic:
            self.load_files_from_data(message)
        


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._files_topic)
            