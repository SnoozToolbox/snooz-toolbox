"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    CombineEventsDialog
"""

from qtpy import QtWidgets, QtCore

from CEAMSTools.SleepReport.EventReportStep.Ui_CombineEventsDialog import Ui_CombineEventsDialog

class CombineEventsDialog(QtWidgets.QDialog, Ui_CombineEventsDialog):
    """
        CombineEventsDialog
    """
    on_add_group_signal = QtCore.Signal(object, object)
    on_add_group_to_all_signal = QtCore.Signal(object, object)

    def __init__(self, file_item, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # init variables
        self._file_item = file_item
        self.update_tree()

    def update_tree(self):
        events_model = self._file_item.events_model
        for group_item_src in events_model.items:
            group_item = QtWidgets.QTreeWidgetItem()
            group_item.setText(0, group_item_src.data(0, QtCore.Qt.DisplayRole))
            group_item.setText(1, str(group_item_src.data(1, QtCore.Qt.DisplayRole)))
            group_item.setCheckState(0, QtCore.Qt.Unchecked)
            self.events_treewidget.addTopLevelItem(group_item)

            for j in range(group_item_src.childCount()):
                event_item_src = group_item_src.child(j)
                event_item = QtWidgets.QTreeWidgetItem()
                event_item.setText(0, event_item_src.data(0, QtCore.Qt.DisplayRole))
                event_item.setText(1, str(event_item_src.data(1, QtCore.Qt.DisplayRole)))
                event_item.setCheckState(0, QtCore.Qt.Unchecked)
                group_item.addChild(event_item)

        self.events_treewidget.resizeColumnToContents(0)

    def on_cancel(self):
        self.close()

    def _get_new_group_data(self, group_name):
        new_group_data = {
            "name":group_name,
            "count":0
        }

        #count = 0
        events = []
        for item in self.events_treewidget.findItems("", QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive):
            print(f"group and name:{item.text(0)} and state:{item.checkState(0)}")
            if item.checkState(0)==QtCore.Qt.CheckState.Checked:
                if item.parent() is not None:
                    group_name = item.parent().text(0)
                    event_name = item.text(0)
                    #count = int(item.text(1))
                    event_data = {
                        "name":event_name,
                        "count": 0,
                        "original_group_name":group_name
                    }
                    events.append(event_data)
                    #new_group_data["count"] = new_group_data["count"] + count

        return new_group_data, events

    def on_add_to_all(self):
        new_group_name = self.new_group_lineedit.text()

        # Error if the name is empty
        if new_group_name == '':
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Error, the group name is empty.")
            msgBox.setWindowTitle("Combine events error")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec()
            return

        # Error if the name is already used
        events_model = self._file_item.events_model
        for group_item_src in events_model.items:
            if group_item_src.data(0, QtCore.Qt.DisplayRole) == new_group_name:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("Error, the group name is already used.")
                msgBox.setWindowTitle("Combine events error")
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msgBox.exec()
                return

        new_group_data, events = self._get_new_group_data(new_group_name)

        self.close()
        self.on_add_group_to_all_signal.emit(new_group_data, events)

    def on_add(self):
        new_group_name = self.new_group_lineedit.text()

        # Error if the name is empty
        if new_group_name == '':
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Error, the group name is empty.")
            msgBox.setWindowTitle("Combine events error")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec()
            return

        # Error if the name is already used
        events_model = self._file_item.events_model
        for group_item_src in events_model.items:
            if group_item_src.data(0, QtCore.Qt.DisplayRole) == new_group_name:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("Error, the group name is already used.")
                msgBox.setWindowTitle("Combine events error")
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msgBox.exec()
                return

        new_group_data, events = self._get_new_group_data(new_group_name)

        #self._file_item.events_model.add_group(new_group_data, events)
        
        self.close()
        self.on_add_group_signal.emit(new_group_data, events)

    def find_event(self, group_name, event_name):
        for group in self._event_groups:
            if group.name == group_name:
                for event in group.events:
                    if event.name == event_name:
                        return event
        return None

    def on_item_checked(self, item):
        self.events_treewidget.blockSignals(True)

        for i in range(item.childCount()):
            item.child(i).setCheckState(0, item.checkState(0))

        if item.parent() is not None:
            is_all_checked = True
            for i in range(item.parent().childCount()):
                if item.parent().child(i).checkState(0) != 2:
                    is_all_checked = False
                    break

            if is_all_checked:
                item.parent().setCheckState(0, 2)
            else:
                item.parent().setCheckState(0, 0)

        self.events_treewidget.blockSignals(False)