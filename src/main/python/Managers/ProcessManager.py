"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
import copy
import datetime as dt
import gc
import json
import pandas as pd
import os
import time

from qtpy import QtCore
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QMessageBox
from qtpy.QtWidgets import QFileDialog
from qtpy.QtWidgets import QProgressDialog

import config
from commons.NodeRuntimeException import NodeRuntimeException
from flowpipe import Graph
from flowpipe.ActivationState import ActivationState
from flowpipe.utilities import import_class 
from Managers.Manager import Manager
from ProcessWorker import ProcessWorker
from ProcessUI.ProcessView import ProcessView
from ProcessUI.ProgressDialog import ProgressDialog
from widgets.TableDialog import TableDialog
from widgets.MissingPackagesDialog import MissingPackagesDialog

class processState:
    LOADED_FROM_FILE = "loaded_from_file"
    LOADED_FROM_PACKAGE = "LOADED_FROM_PACKAGE"
    NEW_PROCESS = "new_process"
    NONE = "none"

class ProcessManager(Manager):
    graph_outputs = QtCore.Signal(dict)

    def __init__(self, managers):
        super().__init__(managers)
        self._current_state = processState.NONE
        self._is_loaded = False
        self._load_from_package = False
        self._current_filepath = None
        self._current_package_item = None
        self._progress_dialog = None

        # WARNING Multithreading currently does not work well with our libraries that use PyBind11.
        # See this for more information: https://pybind11.readthedocs.io/en/stable/advanced/misc.html#global-interpreter-lock-gil
        self._use_multithread = False

    def initialize(self):
        self._managers.pub_sub_manager.subscribe(self, "process_activation_request")

    # Properties
    @property
    def use_multithread(self):
        return self._use_multithread
    
    @use_multithread.setter
    def use_multithread(self, value):
        self._use_multithread = value

    @property
    def current_state(self):
        return self._current_state
    
    @current_state.setter
    def current_state(self, value):
        self._current_state = value

    # Slots
    @QtCore.Slot()
    def progression_update(self, total_count, counter):
        if self._progress_dialog is not None:
            self._progress_dialog.progression_update(total_count, counter)
    
    @QtCore.Slot()
    def process_finished(self, outputs, interruptions):
        if self._progress_dialog is not None:
            self._progress_dialog.close()
        # If there's been any iteration interruption during the process, show
        # a message with the list of interruptions to warn the user.
        if interruptions is not None and len(interruptions) > 0:
            self._show_iteration_interruption_dialog(interruptions)
        else:
            self._managers.pub_sub_manager.publish(self, 'show_info_message', 'The process completed successfully. See the logs for more details.')

        self.graph_outputs.emit(outputs)

    @QtCore.Slot()
    def process_interrupted(self, outputs, interruptions):
        if self._progress_dialog is not None:
            self._progress_dialog.close()

        self._is_running = False
        self._managers.pub_sub_manager.publish(self, 'show_error_message', 'An exception interrupted the process. See the logs for more details.')
        self._show_iteration_interruption_dialog(interruptions)

    # Public functions    
    def save_scene_to_file(self, filepath):
        with open(filepath, 'w') as f:
            json.dump(self._process_view.scene.serialize(), f, indent=4)

    def process_activation_request(self, sender):
        # Ask the permission to load content, the content manager will ask the user if
        # there is something to be saved.
        is_allowed = self._managers.content_manager.ask_permission_to_load_process()
        if not is_allowed:
            return False
        
        self._open_loading_dialog()
        # Unload the content of any process or tool if needed, the content manager will
        # figure out if it's necessary or not.
        self._managers.content_manager.unload_process_content()
        self._managers.content_manager.unload_tool_content()

        with open(sender.item_description_file, 'r') as f:
            data = json.load(f)

            missing_packages = self._managers.package_manager.check_missing_packages(data["dependencies"])
            if len(missing_packages) > 0:
                missing_package_dialog = MissingPackagesDialog(missing_packages, 
                                                               self._managers.package_manager)
                missing_package_dialog.exec_()
                raise False

            success = self.load_dependencies_from_description(data)
            if not success:
                message = f"ProcessManager could not load process"
                self._managers.pub_sub_manager.publish(self, "show_error_message", message)
                self._close_loading_dialog()
                return False

            success = self.load_content_from_file(data, sender.item_description_file)
            if not success:
                message = f"ProcessManager could not load process"
                self._managers.pub_sub_manager.publish(self, "show_error_message", message)
                self._managers.content_manager.unload_process_content()
                self._managers.content_manager.unload_tool_content()
                self._close_loading_dialog()
                return False

            self._load_from_package = True
            self._current_package_item = sender
            self._current_state = processState.LOADED_FROM_PACKAGE
            
            filename = os.path.basename(sender.item_description_file)
            self._managers.pub_sub_manager.publish(self, "change_process_title", filename)
            self._close_loading_dialog()
        return True

    def new_process(self):
        # Ask the permission to load content, the content manager will ask the user if
        # there is something to be saved.
        is_allowed = self._managers.content_manager.ask_permission_to_load_process()
        if not is_allowed:
            return
        
        # Unload the content of any process or tool if needed, the content manager will
        # figure out if it's necessary or not.
        self._open_loading_dialog()
        self._managers.content_manager.unload_process_content()
        self._managers.content_manager.unload_tool_content()
        self._managers.module_manager.load_latest_modules_dependencies()
        
        self._process_view = ProcessView(self._managers)
        self._managers.content_manager.load_process_content(self._process_view)
        self._is_loaded = True
        self._load_from_package = False
        self._current_filepath = None
        self._current_state = processState.NEW_PROCESS

        title = f"New process"
        self._managers.pub_sub_manager.publish(self, "change_process_title", title)
        self._close_loading_dialog()

        self._managers.navigation_manager.show_process_button()
        
    def open_process_file(self, filepath):
        # Unload the content of any process or tool if needed, the content manager will
        # figure out if it's necessary or not.
        self._open_loading_dialog()
        self._managers.content_manager.unload_process_content()
        self._managers.content_manager.unload_tool_content()
        
        with open(filepath, 'r') as f:
            data = json.load(f)

            success = self.load_dependencies_from_description(data)
            if not success:
                message = f"ProcessManager could load process"
                self._managers.pub_sub_manager.publish(self, "show_error_message", message)
                self._close_loading_dialog()
                return False

            success = self.load_content_from_file(data, filepath)
            if not success:
                message = f"ProcessManager could load process"
                self._managers.pub_sub_manager.publish(self, "show_error_message", message)
                self._managers.content_manager.unload_process_content()
                self._managers.content_manager.unload_tool_content()
                self._close_loading_dialog()
                return False
            self._current_filepath = filepath
            self._load_from_package = False
            self._current_package_item = None
            self._current_state = processState.LOADED_FROM_FILE

            # Get filename from path
            filename = os.path.basename(filepath)
            self._managers.pub_sub_manager.publish(self, "change_process_title", filename)

        self._managers.pub_sub_manager.publish(self, "file_opened", filepath)
        self._close_loading_dialog()
        return True
    
    def open_process(self):
        # Ask the permission to load content, the content manager will ask the user if
        # there is something to be saved.
        is_allowed = self._managers.content_manager.ask_permission_to_load_process()
        if not is_allowed:
            return False

        filepath, _ = QFileDialog.getOpenFileName(
            None, 
            "Open Process JSON File",
            None, 
            "JSON Files (*.json)")
        if not filepath:
            return False
        
        return self.open_process_file(filepath)
    
    def save_process(self):
        if self._current_state == processState.NEW_PROCESS:
            self.save_process_as()
        else:
            self._save_process()

    def save_process_as(self):
        self._current_filepath, _ = QFileDialog.getSaveFileName(None, 'Save process as', filter='*.json')
        if self._current_filepath == '':
            self._current_filepath = None
            return
        if not self._current_filepath.endswith(".json"):
            self._current_filepath = self._current_filepath + ".json"

        graph = self._process_view.scene.serialize()

        # Save JSON to file
        with open(self._current_filepath, 'w') as f:
            json.dump(graph, f, indent=4)

        self._process_view.scene.take_snapshot()
        message = f"Process saved"
        self._managers.pub_sub_manager.publish(self, "show_info_message", message)
        self._current_state = processState.LOADED_FROM_FILE

        filename = os.path.basename(self._current_filepath)
        self._managers.pub_sub_manager.publish(self, "change_process_title", filename)
        self._managers.pub_sub_manager.publish(self, "file_opened", self._current_filepath)
    
    def close_process(self):
        # Ask the permission to load content, the content manager will ask the user if
        # there is something to be saved.
        is_allowed = self._managers.content_manager.ask_permission_to_load_process()
        if not is_allowed:
            return
        
        # Unload the content of any process or tool if needed, the content manager will
        # figure out if it's necessary or not.
        self._managers.content_manager.unload_process_content()
        self._managers.content_manager.unload_tool_content()
        self._current_state = processState.NONE
    
    def run_current_process(self):
        if self._is_loaded:
            graph_json = self._process_view.scene.serialize()
            self.run(graph_json)

    def on_topic_update(self, topic, message, sender):
        if topic == "process_activation_request":
            self.process_activation_request(sender)

    def ask_unsaved(self):
        if not self._is_loaded:
            return True
        
        if not self._process_view.scene.is_dirty():
            return True
        
        # TODO Check if dirty and ask the user for save
        # Ask yes no answer
        dialog = QMessageBox()
        dialog.setWindowTitle("Unsaved work")
        dialog.setText("The current process has unsaved changes, do you want to save them before closing the process?")
        dialog.setStandardButtons(QMessageBox.Cancel |QMessageBox.Yes | QMessageBox.No)
        dialog.setDefaultButton(QMessageBox.No)
        result = dialog.exec_()
        if result == QMessageBox.Yes:
            self._save_process()
        return result != QMessageBox.Cancel

    def unload_content(self):
        if self._is_loaded:
            if self._process_view is not None:
                self._process_view.unsubscribe_all_topics()
            self._managers.pub_sub_manager.clear_temp_topics()

            self._unload_dependencies()
            self._current_package_item = None
            self._process_view.deleteLater()
            self._process_view = None
            self._is_loaded = False

            self._managers.navigation_manager.hide_process_button()

    def load_content_from_file(self, description, filepath):
        self._process_view = ProcessView(self._managers)
        self._process_view.scene.data = copy.deepcopy(description)
        self._process_view.scene.data["process_params"]["nodes"] = []

        # Add nodes to scenes
        for node in description["process_params"]["nodes"]:
            # Find the module item in its package
            module_name = node["name"]
            package_name = node["package"]["package_name"]
            package_version = self._get_package_version(description, package_name)

            module_item = self._managers.package_manager.get_package_item(package_name, package_version, module_name)
            if module_item is None:
                message = f"ProcessManager could not find module {module_name} in package {package_name}"
                self._managers.pub_sub_manager.publish(self, "show_error_message", message)
                return False
            
            node["package"]["package_version"] = package_version
            node["module_version"] = module_item.version
            self._process_view.create_node(module_item, node)
        
        self._process_view.connection_manager.update_connections()
        self._process_view.scene.take_snapshot()
        self._managers.content_manager.load_process_content(self._process_view)

        filename = os.path.basename(filepath)
        self._managers.pub_sub_manager.publish(self, "change_process_title", filename)

        self._is_loaded = True
        self._managers.navigation_manager.show_process_button()

        return True

    def load_dependencies_from_description(self, description):
        for package in description["dependencies"]:
            package_name = package["package_name"]
            package_version = package["package_version"]
            self._managers.package_manager.activate_package(package_name, package_version)
        return True
    
    def get_node_by_id(self, identifier):
        return self._process_view.get_node_by_id(identifier)
    
    def run(self, graph_json):

        if len(graph_json["process_params"]["nodes"]) == 0:
            message = f"Nothing to run."
            self._managers.pub_sub_manager.publish(self, 'show_info_message', message)
            return

        if self._load_from_package:
            self.worker = ProcessWorker(graph_json, 
                                        self._current_package_item.deepcopy_outputs, 
                                        self._managers, self._use_multithread)
        else:
            self.worker = ProcessWorker(graph_json, False, self._managers, self._use_multithread)

        self.worker.finished.connect(self.process_finished)
        self.worker.progression_update.connect(self.progression_update)
        self.worker.interrupted.connect(self.process_interrupted)

        # TODO Avoid showing the progress dialog when called from the console
        self._progress_dialog = ProgressDialog()
        self._progress_dialog.show()
        self._managers.pub_sub_manager.publish(self, "minimize", None)
 
        if self._use_multithread:
            self.thread = QtCore.QThread()
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.worker.interrupted.connect(self.thread.quit)
            self.worker.interrupted.connect(self.worker.deleteLater)
            self.worker.interrupted.connect(self.process_interrupted)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()
        else:
            self.worker.run()

        self._managers.pub_sub_manager.publish(self, "maximize", None)

    # Private functions
    def _open_loading_dialog(self):
        self._progress = QProgressDialog("Loading ...", None, 0, 1)
        self._progress.setWindowModality(Qt.ApplicationModal)
        self._progress.setMinimumDuration(0) # Settings a minimum time greater than 0 makes the UI update slower
        self._progress.show()

    def _close_loading_dialog(self):
        if self._progress is not None:
            self._progress.setValue(1)
            self._progress.close()
            self._progress = None

    def _show_iteration_interruption_dialog(self, interruptions):
        # create DataFrame from a list of dictionary
        interruption_df = pd.DataFrame(interruptions)
        
        if len(interruptions) > 0:
            # create a pandas DataFrame with only the selected columns
            columns = list(interruptions[0].keys())
            interruption_df = pd.DataFrame(interruptions, columns=columns)
            
            interruption_dialog = TableDialog(interruption_df,
                "WARNING!",
                "The process could not be completed for these iterations:",
                True)
            interruption_dialog.exec_()

    def _save_process(self):
        # We only allow to save over a package item if the user is in dev mode. We do not want regular
        # user to change the package items.
        if self._current_state == processState.LOADED_FROM_PACKAGE and not config.is_dev:
            message = f"ToolManager could save process"
            self._managers.pub_sub_manager.publish(self, "show_error_message", message)
            return

        if not self._process_view.scene.is_dirty():
            return
        else:
            
            graph = self._process_view.scene.serialize()

            if self._current_state == processState.LOADED_FROM_PACKAGE:
                self._current_filepath = self._current_package_item.item_description_file
            elif self._current_state == processState.NEW_PROCESS:
                self._current_filepath, _ = QFileDialog.getSaveFileName(None, 'Save process', filter='*.json')
                if self._current_filepath == '':
                    self._current_filepath = None
                    return
                if not self._current_filepath.endswith(".json"):
                    self._current_filepath = self._current_filepath + ".json"
                self._current_state = processState.LOADED_FROM_FILE

            # Save JSON to file
            with open(self._current_filepath, 'w') as f:
                json.dump(graph, f, indent=4)

            self._process_view.scene.take_snapshot()
            message = f"Process saved"
            self._managers.pub_sub_manager.publish(self, "show_info_message", message)

    def _unload_dependencies(self):
        self._managers.module_manager.unload_all_modules_dependencies()

    def _get_package_version(self, description, package_name):
        for package in description["dependencies"]:
            if package["package_name"] == package_name:
                return package["package_version"]
        return None