"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
import json
from qtpy import QtCore
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QMessageBox, QFileDialog

from Managers.Manager import Manager
from ToolUI.StepsWidget import StepsWidget

class ToolManager(Manager):
    ACTIVATION_TOPIC = "tool_activation_request"

    def __init__(self, managers):
        super().__init__(managers)
        self._current_package_item = None
        self._waiting_package_item = None
        self._is_loaded = False
        self._activation_params = None
        self._step_widget = None
        
    def initialize(self):
        self._managers.pub_sub_manager.subscribe(self, ToolManager.ACTIVATION_TOPIC)

    # Slots
    @QtCore.Slot()
    def process_finished(self, outputs):
        if self._activation_params is not None:
            if "result_topic" in self._activation_params:
                self._managers.pub_sub_manager.publish(self, self._activation_params["result_topic"], outputs)
        # send the ouptput to the correct app who made the call

    # Public functions
    def on_topic_update(self, topic, message, sender):
        if topic == ToolManager.ACTIVATION_TOPIC:
            success = self._managers.process_manager.process_activation_request(sender)
            if not success:
                message = f"ToolManager could not load process"
                self._managers.pub_sub_manager.publish(self, "show_error_message", message)
                return
            
            # Load the content of the tool
            package_name = sender.package.name
            package_version = sender.package.version
            self._managers.package_manager.activate_package(package_name, package_version)
            self._current_package_item = sender

            # If activation params is set, disable all nodes from the node_to_disable list.
            self._activation_params = self._current_package_item.activation_params
            if self._activation_params is not None:
                self._managers.process_manager.graph_outputs.connect(self.process_finished)
                
            success = self._load_content(sender.description, sender.item_path)
            if not success:
                message = f"ToolManager could load tool content"
                self._managers.pub_sub_manager.publish(self, "show_error_message", message)
                self._managers.content_manager.unload_process_content()
                self._managers.content_manager.unload_tool_content()
                return

    def load_workspace(self):
        is_allowed = self._managers.content_manager.ask_permission_to_load_process()
        if not is_allowed:
            return False
        
        filepath, _ = QFileDialog.getOpenFileName(
            None, 
            "Open Workspace JSON File",
            None, 
            "JSON Files (*.json)")
        if not filepath:
            return False

        try: 
            self.load_workspace_from_file(filepath)
        except Exception as e:
            message = f"ToolManager could not load process: {e}"
            self._managers.pub_sub_manager.publish(self, "show_error_message", message)
            return False
        return True

    def load_workspace_from_file(self, filepath):
        success = self._managers.process_manager.open_process_file(filepath)
        if not success:
            message = f"ToolManager could not load process"
            self._managers.pub_sub_manager.publish(self, "show_error_message", message)
            return
        
        with open(filepath, 'r') as f:
            description = json.load(f)

            # Load the content of the tool
            for package in description["dependencies"]:
                package_name = package["package_name"]
                package_version = package["package_version"]
                self._managers.package_manager.activate_package(package_name, package_version)

            success = self._load_content(description, None)
            if not success:
                message = f"ToolManager could not load tool content"
                self._managers.pub_sub_manager.publish(self, "show_error_message", message)
                self._managers.content_manager.unload_process_content()
                self._managers.content_manager.unload_tool_content()
                return

    def ask_unsaved(self):
        return True

    def unload_content(self):
        self._is_loaded = False
        # If activation params is set, disconnect the signal that was set before.
        if self._activation_params is not None:
            self._managers.process_manager.graph_outputs.disconnect(self.process_finished)
            self._activation_params = None
        
        if self._step_widget:
            self._step_widget.unsubscribe_all_topics()
            #self._step_widget = None
            self._step_widget.deleteLater()
        self._step_widget = None
        self._managers.navigation_manager.hide_tool_button()
    
    def _load_content(self, description, tool_filepath=None):
        self._open_loading_dialog()

        try :
            self._step_widget = StepsWidget(self._managers, description, self._activation_params, tool_filepath)
            self._managers.content_manager.load_tool_content(self._step_widget)
            self._is_loaded = True

        except Exception as e:
            message = f"ToolManager could not load tool content: {e}"
            self._managers.pub_sub_manager.publish(self, "show_error_message", message)
            self._close_loading_dialog()
            return False

        self._managers.navigation_manager.show_tool_button()
        self._close_loading_dialog()
        return True


    # Private functions
    def _open_loading_dialog(self):
        self._progress = QMessageBox()
        self._progress.setText("Loading ...\nPlease wait a moment.")
        self._progress.setWindowTitle("Loading ... Please wait a moment.      ")
        self._progress.setStandardButtons(QMessageBox.NoButton)
        self._progress.show()

    def _close_loading_dialog(self):
        if self._progress is not None:
            self._progress.close()
            self._progress = None