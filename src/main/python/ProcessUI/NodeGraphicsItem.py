"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
""" TODO all comments and reorder function logically """
from collections import OrderedDict
import importlib
import traceback

from qtpy import QtWidgets
from qtpy import QtGui
from qtpy import QtCore

from flowpipe.ActivationState import ActivationState
from ProcessUI.BaseNodeView import BaseNodeView
from ProcessUI.ProcessSceneUtils import compute_box_width
from ProcessUI.NodePortGraphicsItem import NodePortGraphicsItem
from config import Z

DEBUG = False

class NodeGraphicsItem(QtWidgets.QGraphicsItem):

    def __init__(self, scene, module_item, managers, connection_manager, parent=None):
        super().__init__(parent)
        self._proxy = None
        self._scene = scene
        self._module_item = module_item
        self._connection_manager = connection_manager
        self._managers = managers
        self._inputs = OrderedDict()
        self._outputs = OrderedDict()
        self._state = 'is_waiting'
        self._is_valid = True
        #self._activation_state = None

        self._init_ui()
        self.setZValue(Z.NODE)

    # @property
    # def activation_state(self):
    #     return self._activation_state
    
    # @activation_state.setter
    # def activation_state(self, value):
    #     if self._activation_state != value:
    #         self._activation_state = value
    #         self._scene.update()

    def __del__(self):
        if self._managers is not None:
            self.unsubscribe_all_topics()

    @property
    def module_description(self):
        return self._module_description
    
    @property
    def inputs(self):
        return self._inputs
    
    @property
    def identifier(self):
        return self._module_description["identifier"]

    def subscribe_all_topics(self):
        self.state_change_topic = f"{self.identifier}.state_change" # Running, waiting, ...
        self.activation_state_change_topic = f"{self.identifier}.activation_state_change" # To change to Activate, By-pass
        self.get_activation_state_topic = f"{self.identifier}.get_activation_state" # To get the activation state : Activate, By-pass

        self._managers.pub_sub_manager.subscribe(self, self.state_change_topic)
        self._managers.pub_sub_manager.subscribe(self, self.activation_state_change_topic)
        self._managers.pub_sub_manager.subscribe(self, self.get_activation_state_topic)

    def unsubscribe_all_topics(self):
        self._managers.pub_sub_manager.unsubscribe(self, self.state_change_topic)
        self._managers.pub_sub_manager.unsubscribe(self, self.activation_state_change_topic)
        self._managers.pub_sub_manager.unsubscribe(self, self.get_activation_state_topic)

        # unsubscribe all topics from the sockes
        for port_name, port in self._inputs.items():
            self._inputs[port_name].unsubscribe_all_topics()

        for port_name, port in self._outputs.items():
            self._outputs[port_name].unsubscribe_all_topics()

    def _init_assets(self):
        style = self._managers.style_manager.get_current_style()

        self._pen_default = QtGui.QPen(style.palette.node_border)
        self._pen_default.setWidthF(1.0)

        self._pen_selected = QtGui.QPen(style.palette.node_selection)
        self._pen_selected.setWidthF(2.0)

        self._pen_invalid = QtGui.QPen(QtGui.QColor(255,0,0))
        self._pen_invalid.setWidthF(3.0)

        self._bg_brush = {
            ActivationState.ACTIVATED:  QtGui.QBrush(style.palette.node_background_activated),
            ActivationState.DEACTIVATED:QtGui.QBrush(style.palette.node_background_deactivated),
            ActivationState.BYPASS:QtGui.QBrush(style.palette.node_background_bypass)
        }

        self._state_brush = {
            'is_waiting':QtGui.QBrush(QtGui.QColor(230,230,230)),
            'is_running':QtGui.QBrush(QtGui.QColor(255,255,0)),
            'is_done':QtGui.QBrush(QtGui.QColor(0,255,0)),
            'is_failed':QtGui.QBrush(QtGui.QColor(255,0,0))
        }

    def serialize(self):
        inputs = OrderedDict()
        for port_name, port in self._inputs.items():
            inputs[port_name] = port.serialize()
            
        outputs = OrderedDict()
        for port_name, port in self._outputs.items():
            outputs[port_name] = port.serialize()

        serialized_data = self._module_description.copy()
        del serialized_data["module_version"]
        serialized_data["pos_x"] = self.x()
        serialized_data["pos_y"] = self.y()
        serialized_data['inputs'] = inputs
        serialized_data['outputs'] = outputs
        serialized_data[ActivationState.KEY] = self._activation_state
        serialized_data['package'] = {"package_name":self._module_description["package"]["package_name"]}

        return serialized_data

    def deserialize(self, module_description):
        try:
            self._module_description = module_description
            
            self.setPos(module_description["pos_x"], module_description["pos_y"])
            # if 'pos_x' in module_description: self.setPos(module_description["pos_x"], module_description["pos_y"])

            self._activation_state = module_description["activation_state"]

            # Compute width based on the text size of the inputs and outputs
            computed_width = compute_box_width(module_description)
            self._width = max(130, computed_width)

            # ## Options button
            if 'module_options' in self._module_description:
                self._options = self._module_description['module_options']
            else:
                self._options = None

            # # Add options button
            options_bouton = QtWidgets.QPushButton(text="")
            options_bouton.setFlat(True)
            options_bouton.setIconSize(QtCore.QSize(16, 16))
            options_bouton.setAccessibleName("node_option_push_button")
            font = options_bouton.font()
            font.setPointSize(8)
            options_bouton.setFont(font)
            options_bouton.clicked.connect(self._on_options_clicked)
            self.options_bouton_proxy = self._scene.addWidget(options_bouton)
            self.options_bouton_proxy.setParentItem(self)
            x = self._width - self.options_bouton_proxy.size().width()
            self.options_bouton_proxy.setPos(x+6,-6)

            # Add title        
            self._title_item.setPlainText(module_description["module_label"])
            self._title_item.setTextWidth(x)

            # # Add itself to the node manager, self.identifier must be done first
            # self._node_manager.add_node(self)

            padding = self._title_item.boundingRect().height() - 6
            self._version_item.setPos(0, padding)
            self._version_item.setPlainText(self._module_item.version)
            
            padding = padding + self._version_item.boundingRect().height() + 8
            spacing = 15

            if 'inputs' not in self._module_description: 
                if DEBUG: print("WARNING NodeGraphicsItem::deserialize attr inputs not found")
            else:
                inputs_count = 0
                for i, (key, value) in enumerate(self._module_description['inputs'].items()):
                    input_port = NodePortGraphicsItem(is_input_port=True, 
                        pub_sub_manager=self._managers.pub_sub_manager, style_manager=self._managers.style_manager,
                        parent=self)
                    input_port.set_connection_manager(self._connection_manager)
                    input_port.setPos(0, padding+i*spacing)
                    input_port.deserialize(value)
                    self._inputs[input_port.name] = input_port

                    # Do after adding the port to self._inputs
                    input_port.register_all_connections()
                    inputs_count = inputs_count + 1

            outputs_count = 0
            
            if 'outputs' not in self._module_description: 
                if DEBUG: print("WARNING NodeGraphicsItem::deserialize attr inputs not found")
            else:
                for i, (key, value) in enumerate(self._module_description['outputs'].items()):
                    output_port = NodePortGraphicsItem(is_input_port=False, 
                        pub_sub_manager=self._managers.pub_sub_manager, style_manager=self._managers.style_manager,
                        parent=self)
                    output_port.set_connection_manager(self._connection_manager)
                    output_port.setPos(self._width, padding+i*spacing)
                    output_port.deserialize(value)
                    self._outputs[output_port.name] = output_port

                    # Do after adding the port to self._outputs
                    output_port.register_all_connections()
                    outputs_count = outputs_count + 1

            self._height = padding + 20 + max(inputs_count,outputs_count) * 15

            self.subscribe_all_topics()
        except Exception as e:
            message = f"Couldn't deserialize the node. Exception: {e.args[0]}"
            self._managers.pub_sub_manager.publish(self, "show_error_message", message)
            return False
        return True
   
    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'NodeGraphicsItem.on_topic_update:{topic}:{message}')

        if topic == self.state_change_topic:  # Running, waiting, ...
            self._state = message
            self._scene.update()
        if topic == self.activation_state_change_topic: # To change to Activate, By-pass
            self._activation_state = message
            self._scene.update()
        if topic == self.get_activation_state_topic:  # To get the activation state : Activate, By-pass
            sender.on_topic_response(topic, self._activation_state, self)
    
    def get_output_port_position(self, port_name):
        pos = self._outputs[port_name].scenePos()
        return (pos.x(),pos.y())

    def get_input_port_position(self, port_name):
        pos = self._inputs[port_name].scenePos()
        return (pos.x(),pos.y())
    
    def create_settings_view(self, custom_params = None):
        class_name = f"{self._module_description['name']}SettingsView"
        module_name = f"{self._module_description['module']}.{class_name}"
        module = importlib.import_module(module_name)
        SettingsView = getattr(module, class_name)
        settings_view = SettingsView(custom_params=custom_params,
            parent_node=self, 
            pub_sub_manager=self._managers.pub_sub_manager, 
            options=self._options)
        return settings_view
    
    def create_results_view(self, custom_params = None):
        class_name = f"{self._module_description['name']}ResultsView"
        module_name = f"{self._module_description['module']}.{class_name}"
        module = importlib.import_module(module_name)
        ResultsView = getattr(module, class_name)

        results_view = ResultsView(self, self._managers.cache_manager,
                                   self._managers.pub_sub_manager)
        return results_view
    
    def _init_ui(self):
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        self.setAcceptHoverEvents(True)

        self._init_sizes()
        self._init_title()
        self._init_assets()

    def _init_title(self):
        self._title_item = QtWidgets.QGraphicsTextItem(parent=self)
        self._version_item = QtWidgets.QGraphicsTextItem(parent=self)
        self._version_item.setPos(0, 20)

    def _init_sizes(self):
        self._width = 160
        self._height = 160
        self._edge_roundness = 0
        self._edge_padding = 2
        self._state_size = 10
        self._state_padding = 5

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(0,0,self._width,self._height).normalized()

    def paint(self, painter, style, widget=None):
        path_outline = QtGui.QPainterPath()
        path_outline.addRoundedRect(0, 0, self._width, self._height, 
            self._edge_roundness, self._edge_roundness)
        painter.setBrush(self._bg_brush[self._activation_state])
        if self._is_valid:
            painter.setPen(self._pen_selected if self.isSelected() else self._pen_default)
        else:
            painter.setPen(self._pen_invalid)
        painter.drawPath(path_outline.simplified())

        painter.setBrush(self._state_brush[self._state])
        painter.setPen(self._pen_default)

        x = int(0 + self._state_padding)
        y = int(self._height - self._state_size - self._state_padding)

        painter.drawEllipse(x, y, self._state_size, self._state_size)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        self._connection_manager.update_connections()

    def mouseDoubleClickEvent(self, event):
        if self._proxy is not None:
            self._proxy.setVisible(not self._proxy.isVisible())
            return

        #base_view = BaseNodeView(self)#, self._cache_manager, self._pub_sub_manager, self._log_manager)
        base_view = BaseNodeView(self, 
                                 self._managers.cache_manager, 
                                 self._managers.pub_sub_manager, 
                                 self._managers.log_manager)

        padding = 10
        self._proxy = self._scene.addWidget(base_view, QtCore.Qt.Window)
        self._proxy.setZValue(Z.NODE_VIEW)
        self._proxy.setPos(self.x() + self._width + padding, self.y())
        self._proxy.visibleChanged.connect(base_view.on_visible_changed)

        try:
            settings_view = self.create_settings_view()

            # Add the settings module to the base view
            base_view.set_settings_view(settings_view)
        except:
            print(f"WARNING Could not load plugin settings view:{self._module_description['name']}")
            print(traceback.format_exc())

        # Load the results module of the plugin if it exist
        try:
            results_view = self.create_results_view()

            # Add the results module to the base view
            base_view.set_results_view(results_view)
        except:
            print(f"WARNING Could not load plugin results view")
            print(traceback.format_exc())

        # # Manually call the visibleChanged event because it wouldn't be called 
        # # the first time the proxy is shown in the scene.
        base_view.on_visible_changed()
            
    def _on_options_clicked(self):
        d = QtWidgets.QDialog()
        d.setWindowTitle("Options")

        layout = QtWidgets.QVBoxLayout()
        d.setLayout(layout)
        self.activation_state_combobox = QtWidgets.QComboBox()
        self.activation_state_combobox.addItem(ActivationState.ACTIVATED)
        self.activation_state_combobox.addItem(ActivationState.DEACTIVATED)
        self.activation_state_combobox.addItem(ActivationState.BYPASS)
        self.activation_state_combobox.setCurrentText(self._activation_state)
        layout.addWidget(self.activation_state_combobox)

        self.options_lineedits = {}
        if self._options is not None:
            for option in self._options:
                line_layout = QtWidgets.QHBoxLayout()
                
                label = QtWidgets.QLabel(option)
                line_layout.addWidget(label)

                line_edit = QtWidgets.QLineEdit()
                if 'tooltip' in self._options[option]:
                    line_edit.setToolTip(self._options[option]['tooltip'])

                if self._options[option]['value'] is not None:
                    line_edit.setText(self._options[option]['value'])
                line_layout.addWidget(line_edit)

                layout.addLayout(line_layout)

                self.options_lineedits[option] = line_edit
        
        layout.addStretch(1)
        button_layout = QtWidgets.QHBoxLayout()
        save_button = QtWidgets.QPushButton('Save')
        save_button.clicked.connect(lambda x:[self._on_save_options(),d.done(0)])
        cancel_button = QtWidgets.QPushButton('Cancel')
        cancel_button.clicked.connect(lambda x:[d.done(0)])
        
        button_layout.addWidget(cancel_button)
        button_layout.addStretch(1)
        button_layout.addWidget(save_button)

        layout.addLayout(button_layout)
        
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()
    
    def _on_save_options(self):
        self._activation_state = self.activation_state_combobox.currentText()
        for option in self.options_lineedits:
            self._options[option]['value'] = self.options_lineedits[option].text()