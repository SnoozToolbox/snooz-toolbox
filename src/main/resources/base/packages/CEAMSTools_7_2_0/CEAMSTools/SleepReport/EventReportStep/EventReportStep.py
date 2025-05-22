"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    EventReportStep
"""

from qtpy import QtWidgets, QtGui, QtCore
import copy

from commons.BaseStepView import BaseStepView
from CEAMSTools.SleepReport.Commons import ContextConstants
from CEAMSTools.SleepReport.Commons.EventsModel import EventsModel
from CEAMSTools.SleepReport.Commons.GroupItem import GroupItem
from CEAMSTools.SleepReport.Commons.EventItem import EventItem
from CEAMSTools.SleepReport.Commons.FileErrorDialog import FileErrorDialog
from CEAMSTools.SleepReport.EventReportStep.Ui_EventReportStep import Ui_EventReportStep
from CEAMSTools.SleepReport.InputFilesStep.InputFilesStep import InputFilesStep
from CEAMSTools.SleepReport.EventReportStep.CombineEventsDialog import CombineEventsDialog
from CEAMSTools.SleepReport.EventReportStep.ModifyCriteriaDialog import ModifyCriteriaDialog



class EventReportStep( BaseStepView,  Ui_EventReportStep, QtWidgets.QWidget):
    """
        EventReportStep
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        #
        self.file_tableview.setStyleSheet(u"QTableView::item:selected{ background-color: #0078d7 }")
        self.event_treewidget.setStyleSheet(u"QTreeWidget::item:selected{ background-color: #0078d7 }")
        self.report_listview.setStyleSheet(u"QListView::item:selected{ background-color: #0078d7 }")

        self.reset_criteria_labels()
        self._add_default_report()
        # init variables
        self._error_dialog = None
        self._current_filename = None
        self._event_groups = None
        self._item_selected = None
        self._event_report_dict_identifier = '8bf274d1-06bf-440d-893a-03816d737ebb'
        self._event_report_dict_topic = f"{self._event_report_dict_identifier}.dictionary"

        self._event_report_identifier = 'a164115e-d659-43eb-8890-350819ff66a0'
        self._event_report_csv_report_topic = f"{self._event_report_identifier}.csv_report"
        self._save_events_list_topic = f"{self._event_report_identifier}.save_events_report"

        self._report_names = {}
        self._context_manager[ContextConstants.context_event_report_list] = self._report_names
        
    # Called when the sleep report tool is opened
    def load_settings(self):
        self.update_report_list()
        self._pub_sub_manager.publish(self, self._event_report_dict_topic, "ping")
        self._pub_sub_manager.publish(self, self._event_report_csv_report_topic, "ping")
        self._pub_sub_manager.publish(self, self._save_events_list_topic, "ping")
        

    def on_topic_response(self, topic, message, sender):
        if topic == self._event_report_csv_report_topic:
            self.csv_report_checkbox.setChecked(message)
        if topic == self._save_events_list_topic:
            self.events_list_checkBox.setChecked(message)
        if topic == self._event_report_dict_topic:
            model = self.file_tableview.model()
            for filename, reports in message.items():
                for report in reports:
                    self._add_report(filename, report, report['group_name'], report['event_name'])
            model.update_reports_count()
            

    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._event_report_csv_report_topic, self.csv_report_checkbox.isChecked())
        self._pub_sub_manager.publish(self, self._save_events_list_topic, self.events_list_checkBox.isChecked())

        # Fill input files data
        files = {}
        model = self.file_tableview.model()
        for idx in range(model.rowCount(QtCore.QModelIndex())): # for each file loaded
            filename = model.files[idx].full_filename
            file_item = model.get_file_item_by_name(filename)
            reports = []
            for i in range(len(file_item.events_model.items)): # for each group of the current file
                group_item = file_item.events_model.items[i] # current group of the current file "RIGHT GROUP ITEM"
                for report in group_item.reports_model.reports:
                    rep = copy.deepcopy(report)
                    reports.append(rep)
                
                for j in range(group_item.childCount()): # for each event name included in the current group
                    event_item = group_item.child(j)
                    for report in event_item.reports_model.reports:
                        rep = copy.deepcopy(report)
                        reports.append(rep)
                    

            files[filename] = reports
        self._pub_sub_manager.publish(self, self._event_report_dict_topic, files)


    def on_topic_update(self, topic, message, sender):
        if topic == self._context_manager.topic:
            if message == ContextConstants.context_input_files:
                self.context = self._context_manager[ContextConstants.context_input_files]
                model = self.context["model"]
                model.dataChanged.connect(self.on_files_change)
                self.file_tableview.setModel(model)
                self.file_tableview.setColumnHidden(1, True)
                self.file_tableview.resizeColumnsToContents()

    def on_files_change(self, index1, index2):
        self.reset_event_list()
        self.reset_report_list()

    def on_file_selected(self):
        model = self.file_tableview.model()
        index = self.file_tableview.currentIndex()
        event_model = model.get_events_model(index.row())

        self.reset_event_list()
        self.event_treewidget.addTopLevelItems(event_model.items)

        self._current_filename = model.files[index.row()].full_filename

    def on_event_selected(self):
        self.reset_criteria_labels()

        selected_item = self.event_treewidget.currentItem()
        self.report_listview.setModel(selected_item.reports_model)

        self.report_criteria_mapper = QtWidgets.QDataWidgetMapper(self)
        self.report_criteria_mapper.setModel(selected_item.reports_model)
        self.report_criteria_mapper.addMapping(self.report_name_label,0,b"text")
        self.report_criteria_mapper.addMapping(self.duration_min_label,1,b"text")
        self.report_criteria_mapper.addMapping(self.duration_max_label,2,b"text")
        self.report_criteria_mapper.addMapping(self.interval_min_label,3,b"text")
        self.report_criteria_mapper.addMapping(self.interval_max_label,4,b"text")
        self.report_criteria_mapper.addMapping(self.min_count_label,5,b"text")
        self.report_criteria_mapper.addMapping(self.end_period_label,6,b"text")
        self.report_criteria_mapper.addMapping(self.resp_event_asso_min_label,7,b"text")
        self.report_criteria_mapper.addMapping(self.resp_event_asso_max_label,8,b"text")
        self.report_criteria_mapper.addMapping(self.analysis_period_label,9,b"text")
        self.report_criteria_mapper.addMapping(self.graphic_label,10,b"text")

        index = selected_item.reports_model.index(0,0)
        self.report_listview.selectionModel().select( index, QtCore.QItemSelectionModel.Select )
        self.report_criteria_mapper.toFirst()

    def reset_event_list(self):
        for i in reversed(range(self.event_treewidget.topLevelItemCount())):
            self.event_treewidget.takeTopLevelItem(i)

    def reset_report_list(self):
        self.report_listview.setModel(None)

    def reset_criteria_labels(self):
        self.duration_min_label.setText("---")
        self.duration_max_label.setText("---")
        self.interval_min_label.setText("---")
        self.interval_max_label.setText("---")
        self.min_count_label.setText("---")
        self.end_period_label.setText("---")
        self.resp_event_asso_min_label.setText("---")
        self.resp_event_asso_max_label.setText("---")
        self.analysis_period_label.setText("---")
        self.graphic_label.setText("---")

    def on_combine_events(self):
        model = self.file_tableview.model()
        file_item = model.get_file_item_by_name(self.get_current_filename())
        d = CombineEventsDialog(file_item=file_item, parent=None)
        d.on_add_group_signal.connect(self.on_add_group)
        d.on_add_group_to_all_signal.connect(self.on_add_group_to_all)
        d.exec_()

    def _add_group(self, filename, group_data, events):
        # Get the file_item based on the filename
        file_item  = self._get_file_item_by_filename(filename)

        # Check if the group already exist
        group_item = file_item.events_model.find_group_by_name(group_data['name'])
        if group_item is not None:
            return False

        # TODO Update the count for all events
        total_count = 0
        for event in events:
            original_group_name = event['original_group_name']
            group_item = file_item.events_model.find_group_by_name(original_group_name)
            if group_item is None:
                return False

            event_item = file_item.events_model.find_event_by_name(group_item, event['name'])
            if event_item is None:
                return False
                
            event['count'] = event_item.event_count
            total_count = total_count + event['count']
        group_data['count'] = total_count

        # Add the group item to the file item
        file_item.events_model.add_group(group_data, events)

        return True
        
    def on_add_group(self, group_data, events):
        # Get the current filename
        filename = self.get_current_filename()
        if filename is None:
            return
        self._add_group(filename, group_data, events)

        # Update the group/event tree
        file_item  = self._get_file_item_by_filename(filename)
        self.reset_event_list()
        self.event_treewidget.addTopLevelItems(file_item.events_model.items)
        
    def on_add_group_to_all(self, group_data, events):
        # Add the report to all files
        error_files = []
        model = self.file_tableview.model()
        for i in range(len(model.files)):
            # Get the file full name
            filename = model.files[i].full_filename
            
            # Add the report
            success = self._add_group(filename, group_data, events)

            if not success:
                error_files.append(filename)

        # Update the group/event tree
        filename = self.get_current_filename()
        file_item  = self._get_file_item_by_filename(filename)
        self.reset_event_list()
        self.event_treewidget.addTopLevelItems(file_item.events_model.items)

        if len(error_files) > 0:
            if self._error_dialog is not None:
                self._error_dialog.close()

            self._error_dialog = FileErrorDialog(error_files)
            self._error_dialog.show()

    def on_combine_done(self):
        # Update the event list
        model = self.file_tableview.model()
        index = self.file_tableview.currentIndex()
        event_model = model.get_events_model(index.row())
        self.reset_event_list()
        self.event_treewidget.addTopLevelItems(event_model.items)
        
    def on_report_selected(self):
        self.report_criteria_mapper.setCurrentIndex(self.report_listview.currentIndex().row())
        
    def get_current_filename(self):
        return self._current_filename

    def on_add_to_all(self):
        "Add the selected report to all files"
        # Get the report we want to add.
        report_name = self.report_combobox.currentText()
        report_to_add = None
        for report in self._default_reports:
            if report['name'] ==  report_name:
                report_to_add = report.copy()
                break
        
        # Get the group name and event name on which to add the event
        event_tree_item = self.event_treewidget.currentItem()
        if event_tree_item is None:
            return

        group_name = event_tree_item.group_name
        if isinstance(event_tree_item, EventItem):
            event_name = event_tree_item.event_name
        else:
            event_name = None
        
        # Add the report to all files
        error_files = []
        model = self.file_tableview.model()
        for i in range(len(model.files)):
            # Get the file full name
            filename = model.files[i].full_filename
            
            # Add the report
            success = self._add_report(filename, report_to_add, group_name, event_name)

            if not success:
                error_files.append(filename)

        if len(error_files) > 0:

            if self._error_dialog is not None:
                self._error_dialog.close()

            self._error_dialog = FileErrorDialog(error_files)
            self._error_dialog.show()

        # Update the list information like the report counts
        model = self.file_tableview.model()
        model.update_reports_count()

    def _get_file_item_by_filename(self, filename):
        '''Get a file item by its filename'''
        model = self.file_tableview.model()

        for i in range(len(model.files)):
            if filename == model.files[i].full_filename:
                return model.files[i]
        return None

    def _add_report(self, filename, report, group_name, event_name):
        '''Add a report to group or event for a file '''
        # Get file_item by filename
        file_item = self._get_file_item_by_filename(filename)

        # Find the report model for the group_name/event_name combinaison
        events_model = file_item.events_model
        group_item = events_model.find_group_by_name(group_name)

        if group_item is None:
            return False
        
        if event_name is not None:
            event_item = events_model.find_event_by_name(group_item, event_name)
            if event_item is None:
                return False
            event_tree_item = event_item
        else:
            event_tree_item = group_item

        # Check if this report already exist for this combinaison of group/event
        if event_tree_item.find_report_by_name(report['name']) is not None:
            return True

        # Add the report
        event_tree_item.add_report(report)

        # Add the report label to the context
        self._add_report_label_to_context(filename, report, event_tree_item)
        return True

    def _add_report_label_to_context(self, filename, report, event_tree_item):
        report_label = self._get_report_label(report["name"], event_tree_item)
        
        if filename not in self._report_names:
            self._report_names[filename] = []

        if report_label not in self._report_names[filename]:
            self._report_names[filename].append(report_label)

        self._context_manager[ContextConstants.context_event_report_list] = self._report_names
    
    def _remove_report_label_to_context(self, filename, report, event_tree_item, previous_name):
        report_label = self._get_report_label(previous_name, event_tree_item)

        self._report_names[filename].remove(report_label)
        self._context_manager[ContextConstants.context_event_report_list] = self._report_names

    def _get_report_label(self, report_name, event_tree_item):
        # Add the report label to the context
        if isinstance(event_tree_item, EventItem):
            report_label = report_name + " - " + event_tree_item.group_name + " - " + event_tree_item.event_name
        else:
            report_label = report_name + " - " + event_tree_item.group_name
        return report_label

    def on_add(self):
        # Get the current file item on which to add the report
        filename = self.get_current_filename()
        if filename is None:
            return

        # Get the report we want to add.
        report_name = self.report_combobox.currentText()
        report_to_add = None
        for report in self._default_reports:
            if report['name'] ==  report_name:
                report_to_add = report.copy()
                break
        
        # Get the group name and event name on which to add the event
        event_tree_item = self.event_treewidget.currentItem()
        if event_tree_item is None:
            return

        group_name = event_tree_item.group_name
        if isinstance(event_tree_item, EventItem):
            event_name = event_tree_item.event_name
        else:
            event_name = None
            
        # Add the report
        success = self._add_report(filename, report_to_add, group_name, event_name)

        if success:
            # Update the list information like the report counts
            model = self.file_tableview.model()
            model.update_reports_count()
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText(f"Error, failed to add a report to the file:{filename}")
            msgBox.setWindowTitle("Add report error")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec()
        return

    def on_remove_to_all(self):
        "Add the selected report to all files"
        # Get the report we want to remove.
        report_index = self.report_listview.currentIndex() # report name to remove
        try:
            report_name = report_index.data()
        except:
            # Hack to prevent a problem when removing when nothing is selected.
            return
        
        # Get the group name and event name on which to add the event
        event_tree_item = self.event_treewidget.currentItem()
        if event_tree_item is None:
            return

        group_name = event_tree_item.group_name
        if isinstance(event_tree_item, EventItem):
            event_name = event_tree_item.event_name
        else:
            event_name = None
        
        # Remove the report to all files
        model = self.file_tableview.model()
        for i in range(len(model.files)):
            # Get the file full name
            filename = model.files[i].full_filename
            
            # Remove the report
            self._remove_report(filename, report_name, group_name, event_name)

        # Update the list information like the report counts
        model = self.file_tableview.model()
        model.update_reports_count()

    def _remove_report(self, filename, report_name, group_name, event_name):
        '''Remove a report to group or event for a file '''
        # Get file_item by filename
        file_item = self._get_file_item_by_filename(filename)

        # Find the report model for the group_name/event_name combinaison
        events_model = file_item.events_model
        group_item = events_model.find_group_by_name(group_name)

        if group_item is None:
            return False
        
        if event_name is not None:
            event_item = events_model.find_event_by_name(group_item, event_name)
            if event_item is None:
                return False
            event_tree_item = event_item
        else:
            event_tree_item = group_item

        # Check if this report exist for this combinaison of group/event, if it
        # doesn't we just return, there's nothing to remove.
        report_to_remove = event_tree_item.find_report_by_name(report_name)
        if report_to_remove is None:
            return True

        # Remove the report
        event_tree_item.remove_report(report_name)

        # Remove the report label to the context
        report_label = self._get_report_label(report_to_remove["name"], event_tree_item)
        
        if filename not in self._report_names:
            self._report_names[filename] = []

        if report_label in self._report_names[filename]:
            self._report_names[filename].remove(report_label)
            if len(self._report_names[filename]) ==  0:
                del self._report_names[filename]

        self._context_manager[ContextConstants.context_event_report_list] = self._report_names
        return True

    def on_remove(self):
        # Get the current file item on which to remove the report
        filename = self.get_current_filename()
        if filename is None:
            return

        # Get the report we want to remove.
        report_index = self.report_listview.currentIndex() # report name to remove
        try:
            report_name = report_index.data()
        except:
            # Hack to prevent a problem when removing when nothing is selected.
            return
        
        # Get the group name and event name on which to remove the event
        event_tree_item = self.event_treewidget.currentItem()
        if event_tree_item is None:
            return

        group_name = event_tree_item.group_name
        if isinstance(event_tree_item, EventItem):
            event_name = event_tree_item.event_name
        else:
            event_name = None
            
        # Remove the report
        success = self._remove_report(filename, report_name, group_name, event_name)

        if success:
            # Update the list information like the report counts
            model = self.file_tableview.model()
            model.update_reports_count()
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText(f"Error, failed to remove a report from the file:{filename}")
            msgBox.setWindowTitle("Add report error")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec()
        return

    def on_clear_all(self):
        # Remove the report to all files
        model = self.file_tableview.model()
        for i in range(len(model.files)):
            file_item = model.files[i]
            file_item.events_model.clear()

        self._report_names = {}
        self._context_manager[ContextConstants.context_event_report_list] = self._report_names

        # Update the list information like the report counts
        model.update_reports_count()

        self.reset_report_list()
        self.reset_event_list()

    # To update the combo list of predefined reports - called when the sleep report tool is opened - modify for specific predefined reports
    def update_report_list(self):
        self.report_combobox.blockSignals(True)
        self.report_combobox.clear()
        for report in self._default_reports:
            self.report_combobox.addItem(report['name'])
        self.report_combobox.blockSignals(False)

    def on_modify(self):
        selected_item =self.event_treewidget.currentItem()
        report_index = self.report_listview.currentIndex()
        if report_index.row() >= 0:
            previous_name = self.report_listview.model().itemData(report_index)[0]
            d = ModifyCriteriaDialog(
                    event_tree_item=selected_item,
                    row=report_index.row(),
                    previous_name=previous_name,
                    parent=None)
            d.on_ok_signal.connect(self.on_modify_file)
            d.on_ok_to_all_signal.connect(self.on_modify_to_all)
            d.exec_()

    def on_create(self):
        selected_item = self.event_treewidget.currentItem()
        if selected_item is None:
            return

        d = ModifyCriteriaDialog(
                event_tree_item=selected_item,
                row=None,
                previous_name=None,
                parent=None)
        d.on_ok_signal.connect(self._on_create)
        d.on_ok_to_all_signal.connect(self._on_create_to_all)
        d.exec_()

    def _modify_report(self, filename, group_name, event_name, report, previous_name):
        # Find the event tree item (GroupItem or EventItem) on which to add the report
        file_item = self._get_file_item_by_filename(filename)
        group_item = file_item.events_model.find_group_by_name(group_name)

        if group_item is None:
            return False

        if event_name is not None:
            event_tree_item = file_item.events_model.find_event_by_name(group_item, event_name)
            if event_tree_item is None:
                return False
        else:
            event_tree_item = group_item

        # Add the report
        event_tree_item.reports_model.modify_report(report, previous_name)

        # Update the report label to the context
        self._remove_report_label_to_context(filename, report, event_tree_item, previous_name)
        self._add_report_label_to_context(filename, report, event_tree_item)

        # Update the list information like the report counts
        model = self.file_tableview.model()
        model.update_reports_count()

    def on_modify_file(self, group_name, event_name, report, previous_name):
        # Get the current file item on which to add the report
        filename = self.get_current_filename()
        if filename is None:
            return

        self._modify_report(filename, group_name, event_name, report, previous_name)

    def on_modify_to_all(self, group_name, event_name, report, previous_name):
        model = self.file_tableview.model()
        for i in range(len(model.files)):
            # Get the file full name
            filename = model.files[i].full_filename
            self._modify_report(filename, group_name, event_name, report, previous_name)

    def _on_create(self, group_name, event_name, report, previous_name):
        # Get the current file item on which to add the report
        filename = self.get_current_filename()
        if filename is None:
            return

        self._create_report(filename, group_name, event_name, report)

    def _on_create_to_all(self, group_name, event_name, report, previous_name):
        # Remove the report to all files
        error_files = []
        model = self.file_tableview.model()
        for i in range(len(model.files)):
            # Get the file full name
            filename = model.files[i].full_filename
            success = self._create_report(filename, group_name, event_name, report)
            if not success:
                error_files.append(filename)

        if len(error_files) > 0:

            if self._error_dialog is not None:
                self._error_dialog.close()

            self._error_dialog = FileErrorDialog(error_files)
            self._error_dialog.show()


    def _create_report(self, filename, group_name, event_name, report):
        # Find the event tree item (GroupItem or EventItem) on which to add the report
        file_item = self._get_file_item_by_filename(filename)
        group_item = file_item.events_model.find_group_by_name(group_name)

        if group_item is None:
            return False

        if event_name is not None:
            event_tree_item = file_item.events_model.find_event_by_name(group_item, event_name)
            if event_tree_item is None:
                return False
        else:
            event_tree_item = group_item

         # Check if this report already exist for this combinaison of group/event
        if event_tree_item.find_report_by_name(report['name']) is not None:
            return False

        # Add the report
        event_tree_item.add_report(report)

        # Add the report label to the context
        self._add_report_label_to_context(filename, report, event_tree_item)

        # Update the list information like the report counts
        model = self.file_tableview.model()
        model.update_reports_count()
        return True
    
    def _add_default_report(self):
         # Init default report criteria
        reports = []
        report = self.create_report("Arousals Report")
        report["min_duration"] = 3
        report["max_duration"] = 30
        reports.append(report)
        report = self.create_report("Bruxism Report")
        report["min_duration"] = 0.5
        report["max_duration"] = 100
        report["events_section"] = "Recording time"
        reports.append(report)
        report = self.create_report("PLMS Report-sleep only")
        report["min_duration"] = 0.5
        report["max_duration"] = 10
        report["min_interval"] = 5
        report["max_interval"] = 90
        report["min_count"] = 4
        report["end_period_delay"] = 15
        report["sleep_event_association_min"] = -3.5
        report["sleep_event_association_max"] = 8
        report["events_section"] = "Sleep only"       
        reports.append(report)
        report = self.create_report("PLM Total Report-recording time")
        report["min_duration"] = 0.5
        report["max_duration"] = 10
        report["min_interval"] = 5
        report["max_interval"] = 90
        report["min_count"] = 4
        report["end_period_delay"] = 20
        report["sleep_event_association_min"] = -3.5
        report["sleep_event_association_max"] = 8
        report["events_section"] = "Recording time"       
        reports.append(report)
        report = self.create_report("PLM Report-awake in sleep period")
        report["min_duration"] = 0.5
        report["max_duration"] = 10
        report["min_interval"] = 5
        report["max_interval"] = 90
        report["min_count"] = 4
        report["end_period_delay"] = 15
        report["sleep_event_association_min"] = -3.5
        report["sleep_event_association_max"] = 8
        report["events_section"] = "Awake in sleep period"       
        reports.append(report)
        report = self.create_report("PLM Report-before sleep onset")
        report["min_duration"] = 0.5
        report["max_duration"] = 10
        report["min_interval"] = 5
        report["max_interval"] = 90
        report["min_count"] = 4
        report["end_period_delay"] = 15
        report["sleep_event_association_min"] = -3.5
        report["sleep_event_association_max"] = 8
        report["events_section"] = "Before sleep onset"       
        reports.append(report)
        report = self.create_report("Respiratory Events Report")
        report["min_duration"] = 10
        reports.append(report)
        report = self.create_report("Snoring report")
        report["min_duration"] = 1
        reports.append(report)        
        report = self.create_report("Events report without criteria-sleep only")
        reports.append(report)                
        self._default_reports = reports

    def create_report(self, report_name):
        return {
            "name":report_name,
            "min_duration":0,
            "max_duration":0,
            "min_interval":0,
            "max_interval":0,
            "min_count":0,
            "end_period_delay":0,
            "sleep_event_association_min":0,
            "sleep_event_association_max":0,
            "events_section":"Sleep only", # Sleep Only, Recording time, Awake in sleep period, Before sleep onset
            "graphics":None
        }