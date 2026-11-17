"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
""" TODO all comments and reorder function logically """
from collections import OrderedDict

from qtpy import QtCore
from qtpy import QtGui
from qtpy import QtWidgets

from commons.fonts import text_style_font
from flowpipe.ActivationState import ActivationState
from config import Z

DEBUG = False


def _port_highlighted(port):
    """ Whether the port is at an end of a highlighted connection (process scene). """
    port_highlighted = getattr(port.scene(), "port_highlighted", None)
    return port_highlighted is not None and port_highlighted(port)


class SocketGraphicsItem(QtWidgets.QGraphicsItem):
    def __init__(self, parent, style_manager):
        super().__init__(parent=parent)
        self.parent_port = parent
        self._style_manager = style_manager
        self._socket_size = 10
        self.setZValue(Z.SOCKET)
        self.setFlags(QtWidgets.QGraphicsItem.ItemIsSelectable)
        self.init_assets()

    # Room around the socket for the ring of the socket under a dragged connection
    _HALO = 2

    def boundingRect(self):
        half_size = self._socket_size/2 + self._HALO
        return QtCore.QRectF(-half_size, -half_size, 2*half_size, 2*half_size)

    def shape(self):
        # Picked by the mouse as before the ring: the square of the socket
        half_size = self._socket_size/2
        path = QtGui.QPainterPath()
        path.addRect(QtCore.QRectF(-half_size, -half_size, self._socket_size, self._socket_size))
        return path

    def paint(self, painter, option, widget=None):
        half_size = self._socket_size/2
        socket = QtCore.QRectF(-half_size, -half_size, self._socket_size,
            self._socket_size)

        # While a new connection is dragged: where it starts, where it can be
        # dropped (under the mouse), and the sockets it can not be dropped on.
        # Otherwise: filled at the ends of the highlighted connections.
        scene = self.scene()
        socket_drag_state = getattr(scene, "socket_drag_state", None)
        state = socket_drag_state(self) if socket_drag_state is not None else None
        if state is None and _port_highlighted(self.parent_port):
            state = "origin"
        if state == "dimmed":
            painter.setOpacity(0.3)
        elif state == "target":
            painter.setPen(self._pen_target)
            painter.setBrush(self._brush_target)
            painter.drawEllipse(socket.adjusted(0.25, 0.25, -0.25, -0.25))
            return
        elif state in ("hovered", "origin"):
            if state == "hovered":
                painter.setPen(QtCore.Qt.NoPen)
                painter.setBrush(self._brush_halo)
                painter.drawEllipse(socket.adjusted(-self._HALO, -self._HALO, self._HALO, self._HALO))
            painter.setPen(self._pen_target)
            painter.setBrush(self._pen_target.color())
            painter.drawEllipse(socket.adjusted(0.25, 0.25, -0.25, -0.25))
            return

        if self.parent_port.parent_node._activation_state == ActivationState.DEACTIVATED:
            painter.setPen(self._pen_deactivated)
            painter.setBrush(self._brush_deactivated)
        else:
            painter.setPen(self._pen)
            painter.setBrush(self._brush)
        painter.drawEllipse(socket)

    def init_assets(self):
        style = self._style_manager.get_current_style()
        self._pen = QtGui.QPen(style.palette.node_socket_border)
        self._pen.setWidthF(1.2)
        self._brush = QtGui.QBrush(style.palette.node_socket_background)
        # In the colors of a deactivated node
        self._pen_deactivated = QtGui.QPen(style.palette.node_border_deactivated)
        self._pen_deactivated.setWidthF(1.2)
        self._brush_deactivated = QtGui.QBrush(style.palette.node_background_deactivated)
        self._pen_target = QtGui.QPen(style.palette.node_selection)
        self._pen_target.setWidthF(1.5)
        self._brush_target = QtGui.QBrush(style.palette.node_socket_target_background)
        halo = QtGui.QColor(style.palette.node_selection)
        halo.setAlpha(70)
        self._brush_halo = QtGui.QBrush(halo)

    def mouseDoubleClickEvent(self, event):
        self.parent_port.onDoubleClick(event)
            

class NodePortGraphicsItem(QtWidgets.QGraphicsItem):
    def __init__(self, is_input_port, pub_sub_manager, style_manager, parent):
        super().__init__(parent=parent)
        self.parent_node = parent
        self._pub_sub_manager = pub_sub_manager
        self._style_manager = style_manager
        self._socket_size = 10
        self._label_width = 150
        self._label_height = 15
        self._value_width = 350
        self._value = None
        self.setZValue(Z.PORT)
        self.is_input_port = is_input_port

        self.socket = SocketGraphicsItem(self, style_manager)

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if self._value != value:
            self._value = value
            self.update(self.boundingRect())

    def boundingRect(self):
        if self.is_input_port:
            return QtCore.QRectF(
                -self._socket_size-self._value_width,
                int(-self._label_height/2), 
                self._value_width+self._label_width+self._socket_size, 
                self._label_height)
        else:
            return QtCore.QRectF(
                -self._socket_size-self._label_width,
                int(-self._label_height/2), 
                self._label_width+self._socket_size+self._value_width,
                self._label_height)

    def paint(self, painter, option, widget=None):
        palette = self._style_manager.get_current_style().palette
        painter.setFont(text_style_font("node"))

        if self.is_input_port:
            # Value of the input, left of the node, quieter than the port names
            painter.setPen(palette.node_text_muted)
            painter.drawText(
                -self._value_width-self._socket_size,
                int(-self._label_height/2),
                self._value_width, 
                self._label_height, 
                QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter, 
                str(self._value))

        # Name: semibold in the accent color at an end of a highlighted connection
        # (the widest names still keep 10 px between the inputs and the outputs)
        if _port_highlighted(self):
            font = text_style_font("node")
            font.setWeight(QtGui.QFont.Weight.DemiBold)
            painter.setFont(font)
            painter.setPen(palette.node_selection)
        elif self.parent_node._activation_state == ActivationState.DEACTIVATED:
            painter.setPen(palette.node_text_deactivated)
        else:
            painter.setPen(palette.node_text)
        if self.is_input_port:
                painter.drawText(
                self._socket_size,
                int(-self._label_height/2),
                self._label_width, 
                self._label_height, 
                QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, 
                str(self.name))
        else:
            painter.drawText(
                -self._socket_size-self._label_width,
                int(-self._label_height/2),
                self._label_width, 
                self._label_height, 
                QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter, 
                str(self.name))
            
    def set_connection_manager(self, connection_manager):
        self._connection_manager = connection_manager
        
    def register_all_connections(self):
        source_identifier = self.parent_node.identifier
        source_name = self.name

        if not self.is_input_port:
            for i, (key, values) in enumerate(self._connections.items()):
                for value in values:
                    sink_identifier = key
                    sink_name = value
                    self._connection_manager.add_connection(
                        source_identifier=source_identifier, 
                        source_name=source_name, 
                        sink_identifier=sink_identifier,
                        sink_name=sink_name)

    def get_topic_name(self):
        return f'{self.parent_node.identifier}.{self.name}'

    def deserialize(self, data):
        self.name = data['name']
        self._value = data['value']
        self._sub_plugs = data['sub_plugs']
        self._connections = data['connections']
        self._pub_sub_manager.subscribe(self, self.get_topic_name())

    def unsubscribe_all_topics(self):
        self._pub_sub_manager.unsubscribe(self, self.get_topic_name())

    def serialize(self):
        c_dict = OrderedDict()

        if self.is_input_port:
            # Get all connection for this port
            connection = self._connection_manager.find_connection(
                sink_identifier=self.parent_node.identifier, 
                sink_name=self.name)
            if connection is not None:
                c_dict[connection.source.identifier] = connection.source.name
        else:
            connections = self._connection_manager.find_connection(
                source_identifier=self.parent_node.identifier, 
                source_name=self.name)

            for connection in connections:
                if connection.sink.identifier not in c_dict:
                    c_dict[connection.sink.identifier] = []
                c_dict[connection.sink.identifier].append(connection.sink.name)

        return OrderedDict(
            name=self.name,
            value=self._value,
            sub_plugs=self._sub_plugs,
            connections=c_dict)

    def __str__(self):
        return f'NodePortGraphicsItem {self.name}:{self._value}'
                
    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'NodePortGraphicsItem.on_topic_update:{topic}{message}')
        if message == 'ping':
            try:
                sender.on_topic_response(self.get_topic_name(), self._value, sender)
            except Exception as e:
                print(f'NodePortGraphicsItem.on_topic_update exception in on_topic_response function: {self.get_topic_name()}')
                print(f'full exception message: {e.args[0]}')

        else:
            self._value=message
            self.update(self.boundingRect())
