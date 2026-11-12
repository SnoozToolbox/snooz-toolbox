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
from ProcessUI.NodeWindowProxy import NodeWindowProxy
from commons.fonts import text_style_font
from commons.theme_helpers import frame_pictures, paint_glyph
from commons.tooltip_help_decorator import decorate_tooltip_help_marks
from config import Z

DEBUG = False


class _OptionsButton(QtWidgets.QGraphicsItem):
    """ Button in the top right corner of a node, opening its options. Its icon is
    drawn as lines, so it stays sharp at any zoom.
    """
    SIZE = QtCore.QSizeF(28, 24)
    _ICON_SIZE = 16

    def __init__(self, palette, on_click, parent):
        super().__init__(parent)
        self._palette = palette
        self._on_click = on_click
        self._hovered = False
        self._pressed = False
        self.setAcceptHoverEvents(True)
        self.setAcceptedMouseButtons(QtCore.Qt.MouseButton.LeftButton)
        self.setToolTip("Options")

    def boundingRect(self):
        return QtCore.QRectF(QtCore.QPointF(0, 0), self.SIZE)

    def paint(self, painter, option, widget=None):
        rect = self.boundingRect()
        # Pressed: only while the mouse is still over the button
        if self._hovered:
            painter.setPen(QtGui.QPen(self._palette.control_pressed, 1.0))
            painter.setBrush(self._palette.control_pressed if self._pressed else self._palette.control_hover)
            painter.drawRoundedRect(rect.adjusted(0.5, 0.5, -0.5, -0.5), 6, 6)
        icon = QtCore.QRectF(0, 0, self._ICON_SIZE, self._ICON_SIZE)
        icon.moveCenter(rect.center())
        node = self.parentItem()
        if self._hovered:
            color = self._palette.node_selection
        elif getattr(node, "failed", False):
            # On the red band of a module that failed
            color = self._palette.node_version_failed
        elif getattr(node, "_activation_state", None) == ActivationState.ACTIVATED:
            # On the accent band of a running node
            color = self._palette.node_version_activated
        else:
            color = self._palette.node_text_muted
        paint_glyph(painter, "tool", icon, color)

    def _set_state(self, hovered, pressed):
        if (hovered, pressed) != (self._hovered, self._pressed):
            self._hovered = hovered
            self._pressed = pressed
            self.update()

    def hoverEnterEvent(self, event):
        self._set_state(True, self._pressed)

    def hoverLeaveEvent(self, event):
        self._set_state(False, False)

    def mousePressEvent(self, event):
        # Accepted: the node is neither selected nor moved
        event.accept()
        self._set_state(True, True)

    def mouseDoubleClickEvent(self, event):
        # Not a double click on the node, which would open its window
        self.mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self._set_state(self.boundingRect().contains(event.pos()), True)

    def mouseReleaseEvent(self, event):
        clicked = self._pressed and self.boundingRect().contains(event.pos())
        self._set_state(False, False)
        if clicked:
            # Once the scene is done with the click: the options are a modal dialog
            QtCore.QTimer.singleShot(0, self._on_click)


class NodeGraphicsItem(QtWidgets.QGraphicsItem):
    # Words written at the bottom of the nodes that do not run normally
    _ACTIVATION_BADGES = {
        ActivationState.DEACTIVATED: "Deactivated",
        ActivationState.BYPASS: "Bypassed",
    }
    # Word written at the bottom of a module that failed during the last run
    _FAILED_BADGE = "Failed"
    # Opacity of a bypassed node (the data passes through it): box, texts and ports
    _BYPASS_OPACITY = 0.45

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
        # Failed during the last run (on any file): red until the next run
        self._failed = False
        self._activation_value = ActivationState.ACTIVATED
        self._is_valid = True
        self._hovered = False
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
    def _activation_state(self):
        return self._activation_value

    @_activation_state.setter
    def _activation_state(self, value):
        self._activation_value = value
        self._refresh_activation_look()
        self.update()

    @property
    def failed(self):
        """ Whether the module failed during the last run, on any of its files (red
        until the next run).
        """
        return self._failed

    def clear_failed(self):
        """ A new run starts: the module is no longer drawn as failed. """
        if self._failed:
            self._failed = False
            self._refresh_activation_look()
            self.update()

    @property
    def module_description(self):
        return self._module_description
    
    @property
    def inputs(self):
        return self._inputs

    @property
    def outputs(self):
        return self._outputs

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
        palette = self._managers.style_manager.get_current_style().palette
        self._palette = palette

        self._pen_default = QtGui.QPen(palette.node_border)
        self._pen_default.setWidthF(1.0)

        self._pen_hover = QtGui.QPen(palette.node_selection)
        self._pen_hover.setWidthF(1.0)

        self._pen_selected = QtGui.QPen(palette.node_selection)
        self._pen_selected.setWidthF(2.0)

        # Soft ring around a selected node
        halo = QtGui.QColor(palette.node_selection)
        halo.setAlpha(60)
        self._pen_halo = QtGui.QPen(halo)
        self._pen_halo.setWidthF(3.0)

        self._pen_invalid = QtGui.QPen(palette.state_failed)
        self._pen_invalid.setWidthF(2.0)

        self._pen_separator = QtGui.QPen(palette.node_separator)
        self._pen_separator.setWidthF(1.0)

        self._pen_deactivated = QtGui.QPen(palette.node_border_deactivated)
        self._pen_deactivated.setWidthF(1.0)

        # Module that failed during the last run: red box, band and outline
        self._pen_failed = QtGui.QPen(palette.node_header_failed)
        self._pen_failed.setWidthF(1.5)
        self._failed_bg_brush = QtGui.QBrush(palette.node_background_failed)
        self._failed_header_brush = QtGui.QBrush(palette.node_header_failed)

        # A bypassed node keeps a dashed outline, also when it is hovered or selected
        self._dashed_pens = {}
        for pen in (self._pen_default, self._pen_hover, self._pen_selected, self._pen_failed):
            dashed = QtGui.QPen(pen)
            dashed.setStyle(QtCore.Qt.PenStyle.DashLine)
            self._dashed_pens[id(pen)] = dashed

        self._shadow_brush = QtGui.QBrush(palette.node_shadow)

        # A bypassed node is drawn as a running one, see-through (paint)
        self._bg_brush = {
            ActivationState.ACTIVATED:  QtGui.QBrush(palette.node_background_activated),
            ActivationState.DEACTIVATED:QtGui.QBrush(palette.node_background_deactivated),
            ActivationState.BYPASS:QtGui.QBrush(palette.node_background_activated)
        }
        # The band of a running node is in the accent color: it shows the node runs
        self._header_brushes = {
            ActivationState.ACTIVATED: QtGui.QBrush(palette.node_header_activated),
            ActivationState.DEACTIVATED: QtGui.QBrush(palette.node_header_deactivated),
            ActivationState.BYPASS: QtGui.QBrush(palette.node_header_bypass)
        }

        self._state_colors = {
            'is_waiting': palette.state_waiting,
            'is_running': palette.state_running,
            'is_done': palette.state_done,
            'is_failed': palette.state_failed
        }

    def _refresh_activation_look(self):
        """ Title, version and ports in the look of the activation state: light on the
        accent band of a running node, grey on a deactivated node, see-through on a
        bypassed node. A module that failed is drawn red, in full (also bypassed).
        """
        failed = self.failed
        if failed:
            title_color = self._palette.node_title_activated
            version_color = self._palette.node_version_failed
        elif self._activation_value == ActivationState.ACTIVATED:
            title_color = self._palette.node_title_activated
            version_color = self._palette.node_version_activated
        elif self._activation_value == ActivationState.DEACTIVATED:
            title_color = version_color = self._palette.node_text_deactivated
        else:
            title_color = self._palette.node_text
            version_color = self._palette.node_text_muted
        self._title_item.setDefaultTextColor(title_color)
        self._version_item.setDefaultTextColor(version_color)
        see_through = self._activation_value == ActivationState.BYPASS and not failed
        opacity = self._BYPASS_OPACITY if see_through else 1.0
        for child in self.childItems():
            child.setOpacity(opacity)
            # The options button is drawn in the colors of the band
            child.update()

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

            # Options button, inside the top right corner of the node
            self._options_button = _OptionsButton(self._palette, self._on_options_clicked, parent=self)
            x = self._width - self._options_button.SIZE.width()
            self._options_button.setPos(x - 4, 4)

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
            # The band of the title and the version ends just above the first port
            self._header_height = round(padding - 9)

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
            # Again, for the ports and the options button created above
            self._refresh_activation_look()

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
            if message == 'is_failed' and not self._failed:
                # Red until the next run, also when the run goes on with the next
                # file and the module works on it
                self._failed = True
                self._refresh_activation_look()
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
        decorate_tooltip_help_marks(settings_view)
        frame_pictures(settings_view)
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
        self._header_height = 0
        self._edge_roundness = 6
        self._edge_padding = 2
        self._state_size = 10
        self._state_padding = 5

    def boundingRect(self) -> QtCore.QRectF:
        # Room around the box for its shadow and the ring of the selection
        return QtCore.QRectF(0,0,self._width,self._height).normalized().adjusted(-3, -3, 3, 4)

    def shape(self):
        path = QtGui.QPainterPath()
        path.addRoundedRect(QtCore.QRectF(0, 0, self._width, self._height),
            self._edge_roundness, self._edge_roundness)
        return path

    def paint(self, painter, style, widget=None):
        rect = QtCore.QRectF(0, 0, self._width, self._height)
        radius = self._edge_roundness
        outline = QtGui.QPainterPath()
        outline.addRoundedRect(rect, radius, radius)

        state = self._activation_state
        bypassed = state == ActivationState.BYPASS
        deactivated = state == ActivationState.DEACTIVATED
        # A module that failed during the last run is red, in full also when bypassed:
        # the user finds it at a glance
        failed = self.failed
        see_through = bypassed and not failed

        # Soft shadow below the box (none below a see-through bypassed node)
        if not see_through:
            painter.setPen(QtCore.Qt.PenStyle.NoPen)
            painter.setBrush(self._shadow_brush)
            painter.drawRoundedRect(rect.translated(0, 1.5), radius, radius)

        # Box, with a band behind the title and the version of the module. A
        # deactivated node is darker grey; a bypassed node, see-through (the canvas
        # shows through it), the data passes by
        painter.save()
        if see_through:
            painter.setOpacity(self._BYPASS_OPACITY)
        painter.setPen(QtCore.Qt.PenStyle.NoPen)
        painter.setBrush(self._failed_bg_brush if failed else self._bg_brush[state])
        painter.drawPath(outline)
        header = QtCore.QRectF(0, 0, self._width, self._header_height)
        painter.save()
        painter.setClipPath(outline)
        painter.fillRect(header, self._failed_header_brush if failed else self._header_brushes[state])
        painter.restore()
        # The pale band of a bypassed node needs a line below it
        if see_through:
            painter.setPen(self._pen_separator)
            line_y = self._header_height + 0.5
            painter.drawLine(QtCore.QPointF(1, line_y), QtCore.QPointF(self._width - 1, line_y))
        painter.restore()

        # Outline
        painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
        if not self._is_valid:
            pen = self._pen_invalid
        elif self.isSelected():
            pen = self._pen_selected
            painter.setPen(self._pen_halo)
            painter.drawRoundedRect(rect.adjusted(-1.5, -1.5, 1.5, 1.5), radius + 1.5, radius + 1.5)
        elif self._hovered:
            pen = self._pen_hover
        elif failed:
            pen = self._pen_failed
        elif deactivated:
            pen = self._pen_deactivated
        else:
            pen = self._pen_default
        if bypassed:
            pen = self._dashed_pens.get(id(pen), pen)
        painter.setPen(pen)
        inset = pen.widthF() / 2
        painter.drawRoundedRect(rect.adjusted(inset, inset, -inset, -inset), radius - inset, radius - inset)

        # Run state: an empty circle while waiting, then colored (red once failed)
        run_state = 'is_failed' if failed else self._state
        color = self._state_colors[run_state]
        dot = QtCore.QRectF(self._state_padding + 0.5,
            self._height - self._state_size - self._state_padding + 0.5,
            self._state_size - 1, self._state_size - 1)
        if run_state == 'is_waiting':
            painter.setBrush(self._bg_brush[state])
            painter.setPen(QtGui.QPen(self._palette.node_border_deactivated if deactivated else color, 1.0))
        else:
            painter.setBrush(color)
            painter.setPen(QtGui.QPen(color.darker(125), 1.0))
        painter.drawEllipse(dot)

        # Written in full opacity, also on a bypassed node
        font = text_style_font("node")
        if failed:
            badge = self._FAILED_BADGE
            font.setWeight(QtGui.QFont.Weight.DemiBold)
            color = self._palette.node_text_failed
        else:
            badge = self._ACTIVATION_BADGES.get(state)
            color = self._palette.node_text_deactivated if deactivated else self._palette.node_text_muted
        if badge is not None:
            painter.setFont(font)
            painter.setPen(color)
            painter.drawText(QtCore.QRectF(0, self._height - 20, self._width - 8, 20),
                QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter, badge)

    def _set_hovered(self, hovered):
        self._hovered = hovered
        self.update()
        # Its connections are highlighted (process scene)
        set_hovered_node = getattr(self.scene(), "set_hovered_node", None)
        if set_hovered_node is not None:
            set_hovered_node(self, hovered)

    def hoverEnterEvent(self, event):
        self._set_hovered(True)
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self._set_hovered(False)
        super().hoverLeaveEvent(event)

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
        # Window in the colors of the theme, its title band level with the top of the node
        self._proxy = NodeWindowProxy(self._palette, subtitle=self._module_item.version)
        self._proxy.setWidget(base_view)
        self._scene.addItem(self._proxy)
        self._proxy.setZValue(Z.NODE_VIEW)
        self._proxy.setPos(self.x() + self._width + padding, self.y() + NodeWindowProxy.title_height())
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