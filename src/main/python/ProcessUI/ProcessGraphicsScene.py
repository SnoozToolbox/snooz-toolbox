"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
"""
    Handles the process scene.
"""
import json
from collections import OrderedDict

from qtpy import QtCore
from qtpy import QtGui
from qtpy import QtWidgets
from qtpy.QtCore import Qt

import config
from ProcessUI.NodeGraphicsItem import NodeGraphicsItem
from ProcessUI.NodePortGraphicsItem import SocketGraphicsItem
from ProcessUI.ConnectionManager import ConnectionGraphicsItem

class ProcessGraphicsScene(QtWidgets.QGraphicsScene):
    # signal drop
    signal_drop = QtCore.Signal(dict, QtCore.QPointF)

    """
        Handles the process scene.
            Adding/removing/drawing nodes
    """
    def __init__(self):
        super().__init__()
        self._data = None
        self._init_data()
        self.setSceneRect(-5000, -5000, 10000, 10000)
        self._snapshots = []

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value

    @property
    def connection_manager(self):
        return self._connection_manager
    
    @connection_manager.setter
    def connection_manager(self, value):
        self._connection_manager = value

    @property
    def nodes(self):
        nodes = []
        for item in self.items():
            if isinstance(item, NodeGraphicsItem):
                nodes.append(item)
        return nodes
    
    def is_dirty(self):
        if len(self._snapshots) == 0:
            # If there is no snapshot, it means we start from an empty process
            # so it's considered dirty only if a node as been added.
            return len(self.items()) > 0
        else:
            current_snapshot = json.dumps(self.serialize())
            last_snapshot = self._snapshots[-1]
            return current_snapshot != last_snapshot
        
    def _init_data(self):
        self._data = OrderedDict(
            item_name='',
            item_type='process',
            process_params={
                "process_label":"",
                "nodes":[]
            },
            compatibility_version='1.0.0',
            dependencies=[])

    def dragEnterEvent(self, event):
        """ dragEnterEvent : simply accept the drag enter event """
        event.accept()

    def dragMoveEvent(self, event):
        """ dragMoveEvent : simply accept the drag move event """
        event.accept()

    def dropEvent(self, event):
        """ dropEvent Create a new NodeGraphicsItem and add it to the scene."""
        event.accept()
        module_description = json.loads(event.mimeData().text())
        self.signal_drop.emit(module_description, event.scenePos())

    def mousePressEvent(self, event):
        """ Handles mouse press event
            Middle button is used to show debug information in the console.
            Left button is used to start a connection.
        """
        if event.button() == Qt.MiddleButton:
            self._connection_manager.print_connections()
            self._node_manager.print_nodes()

        elif event.button() == Qt.LeftButton:
            items = self.items(event.scenePos(), 
                deviceTransform=QtGui.QTransform())
            item = self._contains_node_graphics_item(items)

            if item is not None:
                self._connection_manager.start_dragging_new_connection(
                    item.parent_port.parent_node.identifier,
                    item.parent_port.name, 
                    item.parent_port.is_input_port)
            else:
                super().mousePressEvent(event)
            
    def mouseReleaseEvent(self, event):
        """ Handles mouse release event
            Connect a new connection if the user is currently dragging a new 
            connection and the release event is done over a socket.
            Cancel the dragging of a new connection if not.
        """
        super().mouseReleaseEvent(event)

        if self._connection_manager.is_dragging_new_connection:
            items = self.items(event.scenePos(), 
                deviceTransform=QtGui.QTransform())
            item = self._contains_node_graphics_item(items)
            if item is not None:
                self._connection_manager.complete_dragging_new_connection(
                    item.parent_port.parent_node.identifier, 
                    item.parent_port.name, 
                    item.parent_port.is_input_port)
            else:
                self._connection_manager.cancel_dragging_new_connection()

    def mouseMoveEvent(self, event):
        """ Handles mouse move event
            If the user is dragging a new connection, update its position to
            make it follow the mouse.
        """
        if self._connection_manager.is_dragging_new_connection:
            self._connection_manager.update_dragging_new_connection(
                event.scenePos())
        else:
            super().mouseMoveEvent(event)

    def keyPressEvent(self, event):
        super(ProcessGraphicsScene, self).keyPressEvent(event)
        """ Handles all keypresses over the scene """
        if event.key() == Qt.Key_Delete and self.focusItem() is None:
            for item in self.selectedItems():
                if isinstance(item, NodeGraphicsItem):
                    self.removeItem(item)
                    item.unsubscribe_all_topics()
                elif isinstance(item, ConnectionGraphicsItem):
                    self._connection_manager.remove_connection(item)
                    
            self._connection_manager.remove_hanging_connections()

    def take_snapshot(self):
        data = json.dumps(self.serialize())
        self._snapshots.append(data)
        
    def update_dependency(self):
        to_remove = []
        # Clean up all previous dependencies except the ones that are not deleteable.
        # Undeleteable dependencies are used in tools to always keep a dependency toward the
        # package that contains the tool itself instead of the modules of its process.
        for dependency in self._data["dependencies"]:
            if "deleteable" in dependency and dependency["deleteable"] == False:
                continue
            to_remove.append(dependency)

        for dependency in to_remove:
            self._data["dependencies"].remove(dependency)

        # Update all dependencies from all modules used in the process.
        for item in self.items():
            if isinstance(item, NodeGraphicsItem):
                package_name =item.module_description["package"]["package_name"]
                package = self._find_dependency(package_name)
                if package is None:
                    package_version = item.module_description["package"]["package_version"]
                    package = {
                        "package_name": package_name,
                        "package_version": package_version}
                    self._data["dependencies"].append(package)

    def _find_dependency(self, package_name):
        for dependency in self._data["dependencies"]:
            if dependency["package_name"] == package_name:
                return dependency
        return None

    def serialize(self):
        """ Serialize the process """
        data = self._data
        nodes = []
        for item in self.items():
            if isinstance(item, NodeGraphicsItem):
                nodes.append(item.serialize())
        #data['nodes'] = nodes
        data["process_params"]["nodes"] = nodes

        return data

    def _contains_node_graphics_item(self, items):
        for item in items:
            if isinstance(item, SocketGraphicsItem):
                return item
        return None