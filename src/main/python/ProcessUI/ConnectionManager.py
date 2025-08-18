"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    Handles the connections between the nodes
"""
from qtpy import QtWidgets
from qtpy import QtGui
from qtpy.QtCore import Qt

from config import Z

class ConnectionManager():
    """ Handles the connections between the nodes """
    
    def __init__(self, process_view, style_manager):
        """ TODO """
        self._connections = []
        self._dragging_connection = None
        self._process_view = process_view
        self._style_manager = style_manager
        self._scene = process_view.scene
        self.is_dragging_new_connection = False

    def add_connection(self, source_identifier, source_name, sink_identifier, 
                        sink_name):
        """ TODO """
        self.find_and_remove_connection(None, None, sink_identifier, sink_name)

        connection = ConnectionGraphicsItem(self._process_view, self._style_manager)
        connection.set_source(source_identifier, source_name)
        connection.set_sink(sink_identifier, sink_name)
        connection.update_position()

        self._connections.append(connection)
        self._scene.addItem(connection)
        
    def find_and_remove_connection(self, source_identifier, source_name, 
                                    sink_identifier, sink_name):
        """ TODO """
        connection = self.find_connection(source_identifier, 
            source_name, 
            sink_identifier, 
            sink_name)
        if connection is not None:
            self.remove_connection(connection)

    def remove_connection(self, connection):
        """ TODO """
        
        self._connections.remove(connection)
        self._scene.removeItem(connection)
        connection.setParentItem(None)
        connection.source = None
        connection.sink = None

    def clear(self):
        """ TODO """
        for connection in self._connections:
            self._scene.removeItem(connection)
        self._connections.clear()

    def find_connection(self, source_identifier=None, source_name=None, 
                        sink_identifier=None, sink_name=None):
        """ TODO """
        if source_identifier is not None and sink_identifier is not None:
            for connection in self._connections:
                # Find a connection that goes to a specific sink from a 
                # specific source
                if connection.source.identifier == source_identifier and \
                    connection.source.name == source_name and \
                    connection.sink.identifier == sink_identifier and \
                    connection.sink.name == sink_name:
                    return connection
            return None
        elif sink_identifier is not None:
            for connection in self._connections:
                # Find any connection that goes to a specific sink
                if connection.sink.identifier == sink_identifier and \
                    connection.sink.name == sink_name:
                    return connection
            return None
        elif source_identifier is not None:
            connections = []
            
            for connection in self._connections:
                # Find any connection that goes from a specific source
                if connection.source.identifier == source_identifier and \
                    connection.source.name == source_name:
                    connections.append(connection)
            return connections
    
    def remove_hanging_connections(self):
        """ TODO """
        i=len(self._connections)-1
        while i >= 0:
            connection = self._connections[i]
            if connection.is_hanging():
                self._scene.removeItem(connection)
                self._connections.pop(i)
            i = i - 1

    def update_connections(self):
        """ TODO """
        for connection in self._connections:
            connection.update_position()

    def update_dragging_new_connection(self, position):
        """ TODO """
        if self._dragging_connection.sink is not None:
            self._dragging_connection.update_position(
                overwrite_source_pos=(position.x(), position.y()))
        elif self._dragging_connection.source is not None:
            self._dragging_connection.update_position(
                overwrite_sink_pos=(position.x(), position.y()))

    def start_dragging_new_connection(self, node_identifier, port_name, is_input_port):
        """ TODO """
        self.is_dragging_new_connection = True
        self._dragging_connection = ConnectionGraphicsItem(self._process_view, self._style_manager)
        self._dragging_connection.is_dragged = True
        if is_input_port:
            self._dragging_connection.set_sink(node_identifier, port_name)
        else:
            self._dragging_connection.set_source(node_identifier, port_name)

        self._scene.addItem(self._dragging_connection)

    def cancel_dragging_new_connection(self):
        """ TODO """
        self.is_dragging_new_connection = False
        if self._dragging_connection is not None:
            self._scene.removeItem(self._dragging_connection)
            self._dragging_connection.setParentItem(None)
            self._dragging_connection.deleteLater()
            self._dragging_connection = None

    def complete_dragging_new_connection(self, 
        node_identifier, 
        port_name, 
        is_input_port):
        """ TODO """
        self.is_dragging_new_connection = False

        # If started dragging from a sink (input)
        if self._dragging_connection.sink is not None:
            if is_input_port:
                self.cancel_dragging_new_connection()
                return

            if self._dragging_connection.sink.identifier == node_identifier:
                self.cancel_dragging_new_connection()
                return

            self._dragging_connection.set_source(node_identifier, port_name)
            

        # If started dragging from a source (input)
        elif self._dragging_connection.source is not None:
            if not is_input_port:
                self.cancel_dragging_new_connection()
                return

            if self._dragging_connection.source.identifier == node_identifier:
                self.cancel_dragging_new_connection()
                return

            self._dragging_connection.set_sink(node_identifier, port_name)

        self.find_and_remove_connection(None, 
            None, 
            self._dragging_connection.sink.identifier, 
            self._dragging_connection.sink.name)
        self._dragging_connection.is_dragged = False
        self._dragging_connection.update_position()    
        self._connections.append(self._dragging_connection)
        self._dragging_connection = None

    def print_connections(self):
        """ TODO """
        for connection in self._connections:
            print(f'Connection {connection}')


class ConnectionGraphicsItem(QtWidgets.QGraphicsLineItem):
    """ TODO """
    def __init__(self, process_view, style_manager):
        super().__init__(parent=None)
        self._process_view = process_view
        self._style_manager = style_manager
        self.source = None
        self.sink = None
        self.is_dragged = False
        self.setZValue(Z.CONNECTION)
        
        self.init_ui()
        self.init_assets()
        
    def init_ui(self):
        """ TODO """
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, False)

    def init_assets(self):
        """ TODO """
        style = self._style_manager.get_current_style()
        self._pen_default = QtGui.QPen(style.palette.node_border)
        self._pen_default.setWidthF(1.0)

        self._pen_selected = QtGui.QPen(style.palette.node_selection)
        self._pen_selected.setWidthF(2.0)

        self._pen_dragged = QtGui.QPen(style.palette.node_selection)
        self._pen_dragged.setWidthF(2.0)
        self._pen_dragged.setStyle(Qt.DashLine)

    def is_hanging(self):
        """ TODO """
        if self.source is None or self.sink is None:
            return True
        elif self._process_view.get_node_by_id(self.source.identifier) is None:
            return True
        elif self._process_view.get_node_by_id(self.sink.identifier) is None:
            return True

    def set_source(self, identifier, name):
        """ TODO """
        self.source = ConnectionEdge(identifier, name)

    def set_sink(self, identifier, name):
        """ TODO """
        self.sink = ConnectionEdge(identifier, name)

    def update_position(self, 
        overwrite_source_pos=None, 
        overwrite_sink_pos=None):
        """ TODO """
        if overwrite_source_pos is not None:
            source_port_pos = overwrite_source_pos
        else:
            source_node = self._process_view.get_node_by_id(self.source.identifier)
            if source_node is None:
                source_port_pos = (0,0)
            else:
                source_port_pos = source_node.get_output_port_position(self.source.name)

        if overwrite_sink_pos is not None:
            sink_port_pos = overwrite_sink_pos
        else:
            sink_node = self._process_view.get_node_by_id(self.sink.identifier)
            if sink_node is None:
                sink_port_pos = (0,0)
            else:
                sink_port_pos = sink_node.get_input_port_position(self.sink.name)
        
        self.setLine(*source_port_pos, *sink_port_pos)

    def paint(self, painter, option, widget=None):
        """ TODO """
        if self.is_dragged:
            self.setPen(self._pen_dragged)
        elif self.isSelected():
            self.setPen(self._pen_selected)
        else:
            self.setPen(self._pen_default)
        super().paint(painter, option, widget)

    def __str__(self):
        """ TODO """
        source_name = self.source.name
        source_id = f'{self.source.identifier[0:3]}...{self.source.identifier[-3:]}'
        sink_name = self.sink.name
        sink_id = f'{self.sink.identifier[0:3]}...{self.sink.identifier[-3:]}'
        return f'{source_id}:{source_name}->{sink_id}:{sink_name}'

class ConnectionEdge():
    """ TODO """
    def __init__(self, identifier, name):
        """ TODO """
        self.identifier = identifier
        self.name = name