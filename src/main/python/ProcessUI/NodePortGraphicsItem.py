"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
""" TODO all comments and reorder function logically """
from collections import OrderedDict

from qtpy import QtCore
from qtpy import QtGui
from qtpy import QtWidgets

from config import Z

DEBUG = False

class SocketGraphicsItem(QtWidgets.QGraphicsItem):
    def __init__(self, parent, style_manager):
        super().__init__(parent=parent)
        self.parent_port = parent
        self._style_manager = style_manager
        self._socket_size = 10
        self.setZValue(Z.SOCKET)
        self.setFlags(QtWidgets.QGraphicsItem.ItemIsSelectable)
        self.init_assets()

    def boundingRect(self):
        half_size = self._socket_size/2
        return QtCore.QRectF(-half_size, -half_size, self._socket_size, 
            self._socket_size)

    def paint(self, painter, option, widget=None):
        painter.setPen(self._pen)
        painter.setBrush(self._brush)

        half_size = self._socket_size/2
        socket = QtCore.QRectF(-half_size, -half_size, self._socket_size, 
            self._socket_size)
        painter.drawEllipse(socket)

    def init_assets(self):
        style = self._style_manager.get_current_style()
        self._pen = QtGui.QPen(style.palette.node_socket_border)
        self._pen.setWidthF(1.0)
        self._brush = QtGui.QBrush(style.palette.node_socket_background)

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
        style = self._style_manager.get_current_style()

        painter.setPen(style.palette.node_text)
        font = painter.font()
        font.setPointSize(8)
        painter.setFont(font)

        if self.is_input_port:
            painter.drawText(
                -self._value_width-self._socket_size,
                int(-self._label_height/2),
                self._value_width, 
                self._label_height, 
                QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter, 
                str(self._value))

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
