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
    # A snapshot of the process was taken (the process was opened or saved)
    signal_snapshot = QtCore.Signal()

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
        # While a new connection is dragged: the socket where it starts, and the
        # socket under the mouse when the connection can be dropped on it
        self._drag_origin = None
        self._drag_target = None
        # Highlighted connections (see update_highlights) and the ports at their ends
        self._hovered_node = None
        self._hovered_connection = None
        self._recent_connection = None
        self._highlighted_ports = set()
        self.selectionChanged.connect(self.update_highlights)

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
        # The connection just made stays highlighted until the next click
        recent = self._recent_connection
        self._recent_connection = None

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
                self._drag_origin = item
                # The sockets show where the connection can be dropped
                self.update()
                self.update_highlights()
                return
            else:
                super().mousePressEvent(event)
        if recent is not None:
            self.update_highlights()
            
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
                # Highlighted: the user sees which ports it connects
                self._recent_connection = self._connection_manager.complete_dragging_new_connection(
                    item.parent_port.parent_node.identifier,
                    item.parent_port.name,
                    item.parent_port.is_input_port)
            else:
                self._connection_manager.cancel_dragging_new_connection()
            self._drag_target = None
            self._drag_origin = None
            self.update()
            # The node under the mouse now (the node hovered when the drag started
            # otherwise stays hovered until the mouse moves again)
            self._hovered_node = self._node_at(event.scenePos())
            self.update_highlights()

    def mouseMoveEvent(self, event):
        """ Handles mouse move event
            If the user is dragging a new connection, update its position to
            make it follow the mouse.
        """
        if self._connection_manager.is_dragging_new_connection:
            self._connection_manager.update_dragging_new_connection(
                event.scenePos())
            self._set_drag_target(self._contains_node_graphics_item(
                self.items(event.scenePos(), deviceTransform=QtGui.QTransform())))
        else:
            super().mouseMoveEvent(event)

    def _can_drop_on(self, socket):
        """ Whether the connection being dragged can be dropped on a socket. """
        port = socket.parent_port
        return self._connection_manager.can_connect_to(port.parent_node.identifier, port.is_input_port)

    def _set_drag_target(self, socket):
        if socket is not None and not self._can_drop_on(socket):
            socket = None
        if socket is not self._drag_target:
            for changed in (self._drag_target, socket):
                if changed is not None:
                    changed.update()
            self._drag_target = socket

    def socket_drag_state(self, socket):
        """ How a socket looks while a new connection is dragged: "origin" (where the
        connection starts), "hovered" (under the mouse, the connection can be dropped
        on it), "target" (the connection can be dropped on it) or "dimmed" (it can
        not). None when no connection is dragged.
        """
        manager = getattr(self, "_connection_manager", None)
        if manager is None or not manager.is_dragging_new_connection:
            return None
        if socket is self._drag_origin:
            return "origin"
        if socket is self._drag_target:
            return "hovered"
        return "target" if self._can_drop_on(socket) else "dimmed"

    def set_hovered_node(self, node, hovered):
        """ The mouse entered (hovered) or left a node. """
        if hovered:
            self._hovered_node = node
        elif self._hovered_node is node:
            self._hovered_node = None
        else:
            return
        self.update_highlights()

    def set_hovered_connection(self, connection, hovered):
        """ The mouse entered (hovered) or left a connection. """
        if hovered:
            self._hovered_connection = connection
        elif self._hovered_connection is connection:
            self._hovered_connection = None
        else:
            return
        self.update_highlights()

    def update_highlights(self):
        """ Highlight the connections of the node under the mouse and of the selected
        nodes, the connection under the mouse, the selected connections and the
        connection just made, and the ports at their ends: the user sees what is
        connected to what.
        """
        manager = getattr(self, "_connection_manager", None)
        if manager is None:
            return
        # Forget the items taken out of the canvas (deleted)
        if self._hovered_node is not None and self._hovered_node.scene() is not self:
            self._hovered_node = None
        if self._hovered_connection is not None and self._hovered_connection.scene() is not self:
            self._hovered_connection = None
        if self._recent_connection is not None and self._recent_connection.scene() is not self:
            self._recent_connection = None

        node_ids = {item.identifier for item in self.selectedItems() if isinstance(item, NodeGraphicsItem)}
        # Not while a new connection is dragged: the sockets show where it can go
        if self._hovered_node is not None and not manager.is_dragging_new_connection:
            node_ids.add(self._hovered_node.identifier)
        highlighted = []
        for connection in manager.connections:
            ends = [edge.identifier for edge in (connection.source, connection.sink) if edge is not None]
            is_highlighted = connection is self._hovered_connection \
                or connection is self._recent_connection \
                or connection.isSelected() \
                or any(identifier in node_ids for identifier in ends)
            connection.set_highlighted(is_highlighted)
            if is_highlighted:
                highlighted.append(connection)

        ports = set()
        if highlighted:
            nodes = {node.identifier: node for node in self.nodes}
            for connection in highlighted:
                for edge, is_input in ((connection.source, False), (connection.sink, True)):
                    node = nodes.get(edge.identifier) if edge is not None else None
                    if node is not None:
                        port = (node.inputs if is_input else node.outputs).get(edge.name)
                        if port is not None:
                            ports.add(port)
        for port in ports.symmetric_difference(self._highlighted_ports):
            port.update()
            port.socket.update()
        self._highlighted_ports = ports

    def _node_at(self, position):
        """ The node hovered at a position of the scene (its box, ports or texts), or
        None (no node there, or a node window over it).
        """
        for item in self.items(position, deviceTransform=QtGui.QTransform()):
            node = item
            while node is not None and not isinstance(node, NodeGraphicsItem):
                node = node.parentItem()
            if node is not None:
                return node
            if item.acceptHoverEvents():
                return None
        return None

    def port_highlighted(self, port):
        """ Whether a port is at an end of a highlighted connection. """
        return port in self._highlighted_ports

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
            self.update_highlights()

    def take_snapshot(self):
        data = json.dumps(self.serialize())
        self._snapshots.append(data)
        self.signal_snapshot.emit()
        
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

    def cleanup(self):
        # Not called while the items are deleted
        try:
            self.selectionChanged.disconnect(self.update_highlights)
        except (RuntimeError, TypeError):
            pass
        self._hovered_node = None
        self._hovered_connection = None
        self._recent_connection = None
        self._highlighted_ports = set()

        if hasattr(self, "_connection_manager") and self._connection_manager:
            self._connection_manager.clear()
            self._connection_manager = None

        try:
            self.signal_drop.disconnect()
        except TypeError:
            pass
            
        self.clear()

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
    