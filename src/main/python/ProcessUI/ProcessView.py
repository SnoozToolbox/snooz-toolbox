"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
import copy
import json
import uuid

from qtpy import QtWidgets, QtCore

from ui.Ui_ProcessView import Ui_ProcessView
from ProcessUI.NodeGraphicsItem import NodeGraphicsItem
from ProcessUI.ProcessGraphicsView import ProcessGraphicsView
from ProcessUI.ProcessGraphicsScene import ProcessGraphicsScene
from ProcessUI.ConnectionManager import ConnectionManager
from ProcessUI.ModuleSettingsDialog import ModuleSettingsDialog

class ProcessView(QtWidgets.QWidget, Ui_ProcessView):
    def __init__(self, managers, *args, **kwargs):
        super(ProcessView, self).__init__(*args, **kwargs)

        self._managers = managers
        self._managers.pub_sub_manager.subscribe(self, "change_process_title")
        # init UI
        self.setupUi(self)
        self._title = QtWidgets.QLabel()
        self._process_graphics_view = ProcessGraphicsView()
        self._process_graphics_scene = ProcessGraphicsScene()
        self._process_graphics_view.setScene(self._process_graphics_scene)
        
        self.process_view_verticalLayout.addWidget(self._title)
        self.process_view_verticalLayout.addWidget(self._process_graphics_view)

        self._connection_manager = ConnectionManager(self, self._managers.style_manager)
        self._process_graphics_scene.connection_manager = self._connection_manager

        self.module_treeWidget.update_modules_library(self._managers)
        self._process_graphics_scene.signal_drop.connect(self.module_drop)

    @property
    def scene(self):
        return self._process_graphics_scene
    
    @property
    def connection_manager(self):
        return self._connection_manager

    @property
    def nodes(self):
        return self._process_graphics_scene.nodes

    @QtCore.Slot()
    def module_drop(self, module, pos:QtCore.QPointF):
        package_name = module["package_name"]
        package_version = module["package_version"]
        module_name = module["module_name"]

        module_item = self._managers.package_manager.get_package_item(package_name, package_version, module_name)
        description = copy.deepcopy(module_item.description["module_params"])

        # Add attributes needed when a module is integrated into a process
        description["identifier"] = '{0}'.format(uuid.uuid4())
        description["activation_state"] = "activated"
        description["package"] = {
             "package_name": package_name,
             "package_version": package_version
        }
        description["pos_x"] = pos.x()
        description["pos_y"] = pos.y()
        description["module_version"] = module_item.version

        conflicts = self._is_module_valid(description)
        if conflicts:
            message = f"There's a package conflict with the following modules:"

            for conflict in conflicts:
                message += f"\n - {conflict}"

            self._managers.pub_sub_manager.publish(self, "show_error_message", message)
            return
        self.create_node(module_item, description)
        self.scene.update_dependency()

    def on_topic_update(self, topic, message, sender):
        if topic == "change_process_title":
            self._title.setText(message)

    def unsubscribe_all_topics(self):
        self._managers.pub_sub_manager.unsubscribe(self, "change_process_title")

        for item in self._process_graphics_scene.items():
            if isinstance(item, NodeGraphicsItem):
                item.unsubscribe_all_topics()

    def library_options_clicked(self):
        module_settings = ModuleSettingsDialog(self._managers)
        module_settings.exec_()
        self.module_treeWidget.update_modules_library(self._managers)

    def create_node(self, module_item, node_json):
        item = NodeGraphicsItem(self._process_graphics_scene, module_item, self._managers, self._connection_manager)
        
        success = item.deserialize(node_json)
        if success:
            self._process_graphics_scene.addItem(item)

    def get_node_by_id(self, identifier):
        for node in self.nodes:
            if node.identifier == identifier:
                return node
        return None

    def _is_module_valid(self, module_description):
        """ Check if the dependencies of the module in the process conflicts with 
        the module we are trying to add.

        Parameters
        ----------
        module_description : dict
            Module description

        Returns
        -------
        list
            List of modules name that conflict with the module we are trying to add
        """
        package_name = module_description["package"]["package_name"]
        package_version = module_description["package"]["package_version"]

        conflicts = []
        for item in self._process_graphics_scene.items():
            if isinstance(item, NodeGraphicsItem):
                if item.module_description["package"]["package_name"] == package_name and \
                    item.module_description["package"]["package_version"] != package_version:

                    conflicts.append(item.module_description["name"])
        return conflicts
