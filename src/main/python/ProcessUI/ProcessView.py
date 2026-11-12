"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
import copy
import json
import uuid

from qtpy import QtWidgets, QtCore, QtGui

from ui.Ui_ProcessView import Ui_ProcessView
from ProcessUI.NodeGraphicsItem import NodeGraphicsItem
from ProcessUI.ProcessGraphicsView import ProcessGraphicsView
from ProcessUI.ProcessGraphicsScene import ProcessGraphicsScene
from ProcessUI.ConnectionManager import ConnectionManager
from ProcessUI.ModuleSettingsDialog import ModuleSettingsDialog
from commons.fonts import set_text_style
from commons.theme_helpers import glyph_pixmap


class _SearchBox(QtWidgets.QLineEdit):
    """ Search box of the module library: Escape empties it. """
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape and self.text():
            self.clear()
            return
        super().keyPressEvent(event)


class ProcessView(QtWidgets.QWidget, Ui_ProcessView):
    # Delay after the last change of the canvas before checking whether the process
    # has unsaved changes (milliseconds): the check writes the whole process in memory
    _UNSAVED_CHECK_DELAY = 400

    def __init__(self, managers, *args, **kwargs):
        super(ProcessView, self).__init__(*args, **kwargs)

        self._managers = managers
        self._managers.pub_sub_manager.subscribe(self, "change_process_title")
        # init UI
        self.setupUi(self)
        palette = self._managers.style_manager.get_current_style().palette
        self._process_graphics_view = ProcessGraphicsView()
        self._process_graphics_view.set_palette(palette)
        self._process_graphics_scene = ProcessGraphicsScene()
        self._process_graphics_view.setScene(self._process_graphics_scene)

        self.process_view_verticalLayout.addLayout(self._create_title_row(palette))
        self.process_view_verticalLayout.addWidget(self._process_graphics_view)
        # Same spacing as the module library, so the canvas and the list start level
        self.process_view_verticalLayout.setSpacing(self.verticalLayout_3.spacing())
        self.label.setAccessibleName("module_library_title")
        self.verticalLayout_3.insertWidget(1, self._create_search_box(palette))

        self._connection_manager = ConnectionManager(self, self._managers.style_manager)
        self._process_graphics_scene.connection_manager = self._connection_manager

        self.module_treeWidget.update_modules_library(self._managers)
        self._process_graphics_scene.signal_drop.connect(self.module_drop)

        # The process opens fitted in the canvas (the nodes are created before the
        # view is shown)
        self._process_graphics_view.fit_when_shown()

        # Mark of unsaved changes next to the name of the process
        self._unsaved_timer = QtCore.QTimer(self)
        self._unsaved_timer.setSingleShot(True)
        self._unsaved_timer.setInterval(self._UNSAVED_CHECK_DELAY)
        self._unsaved_timer.timeout.connect(self._update_unsaved_mark)
        self._process_graphics_scene.changed.connect(self._schedule_unsaved_check)
        self._process_graphics_scene.signal_snapshot.connect(self._update_unsaved_mark)

        # The module library opens wide enough to read the names and versions of the
        # modules; the canvas takes the rest of the width (also when the window is
        # resized). The user can still drag the splitter.
        self.splitter.setStretchFactor(0, 1)
        self.splitter.setStretchFactor(1, 0)
        library_width = self._library_width()
        self.splitter.setSizes([max(1, self.splitter.width() - library_width), library_width])

    def _create_title_row(self, palette):
        """ The name of the process file in a box above the canvas, as tall as the
        Options button of the module library: the canvas and the library start at the
        same height.
        """
        box = QtWidgets.QFrame()
        box.setAccessibleName("process_title")
        layout = QtWidgets.QHBoxLayout(box)
        layout.setContentsMargins(8, 0, 12, 0)
        layout.setSpacing(6)
        icon = QtWidgets.QLabel()
        icon.setPixmap(glyph_pixmap("file", palette.node_text_muted, 16))
        layout.addWidget(icon)
        self._title = QtWidgets.QLabel()
        self._title.setAccessibleName("process_title_text")
        layout.addWidget(self._title)
        # Shown while the process has changes that are not saved
        self._unsaved = QtWidgets.QWidget()
        self._unsaved.setToolTip("The process has changes that are not saved")
        unsaved_layout = QtWidgets.QHBoxLayout(self._unsaved)
        unsaved_layout.setContentsMargins(4, 0, 0, 0)
        unsaved_layout.setSpacing(5)
        dot = QtWidgets.QLabel()
        dot.setAccessibleName("process_unsaved_dot")
        dot.setFixedSize(8, 8)
        unsaved_layout.addWidget(dot)
        unsaved_text = QtWidgets.QLabel("Unsaved")
        unsaved_text.setAccessibleName("process_unsaved_text")
        set_text_style(unsaved_text, "small")
        unsaved_layout.addWidget(unsaved_text)
        self._unsaved.hide()
        layout.addWidget(self._unsaved)
        box.setFixedHeight(self.library_options_pushButton.sizeHint().height())

        row = QtWidgets.QHBoxLayout()
        row.addWidget(box)
        row.addStretch(1)
        return row

    def _create_search_box(self, palette):
        """ Search box above the module library: shows only the matching modules. """
        search = _SearchBox()
        search.setAccessibleName("module_search")
        search.setPlaceholderText("Search modules")
        search.setClearButtonEnabled(True)
        search.addAction(QtGui.QIcon(glyph_pixmap("search", palette.node_text_muted, 16)),
                         QtWidgets.QLineEdit.LeadingPosition)
        search.setFixedHeight(self.library_options_pushButton.sizeHint().height())
        search.textChanged.connect(self.module_treeWidget.set_filter)
        self._module_search = search
        return search

    def _schedule_unsaved_check(self, *args):
        # Checked once the canvas stops changing (while a node is dragged, for example)
        self._unsaved_timer.start()

    def _update_unsaved_mark(self):
        scene = self._process_graphics_scene
        if scene is None:
            return
        self._unsaved.setVisible(scene.is_dirty())

    def _library_width(self):
        """ Width of the panel of the module library when the process opens. """
        tree = self.module_treeWidget
        return tree.preferred_width() + self.rightPanel.layout().contentsMargins().left() \
            + self.rightPanel.layout().contentsMargins().right()

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

    def cleanup(self):
        # Unsubscribe all node topics first
        self.destroyed.disconnect()

        for conn in getattr(self, "_connections", []):
            conn._process_view = None
            conn.source = None
            conn.sink = None
        self._process_graphics_scene.cleanup()
        self._process_graphics_scene = None