"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    This plugin reads the header and data from an EEG file.

    Inputs:
        filename

    Ouputs:
        signals
        signal_headers
        file_header

    Format supported: EDF
"""

import json

from qtpy import QtCore
from qtpy import QtGui
from qtpy import QtWidgets

class ModulesTreeItem(QtWidgets.QTreeWidgetItem):
    """ Item representing a plugin in the plugin list """
    def __init__(self, module, parent=None):
        super().__init__([module.label, module.version]) 
        self.module = module

class ModulesTreeWidget(QtWidgets.QTreeWidget):
    """ PluginTreeWidget handles the loading and visual of the plugin library.
    """
    # Widths of the library when a process opens (pixels)
    _MINIMUM_WIDTH = 260
    _MAXIMUM_WIDTH = 420

    def __init__(self, parent=None):
        super().__init__(parent)

        """ Initialise the visual of the plugin library widget. """
        self.setSortingEnabled(True)
        self.sortByColumn(0,QtCore.Qt.AscendingOrder)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.setDragEnabled(True)
        # Words of the search box (lower case): only the modules matching all of them are shown
        self._filter_words = []

    def _find_active_modules(self, managers):
        active_modules = []
        for package in managers.package_manager.packages:
            if package.active_version is not None:
                package_name = package.name
                package_version = package.active_version.version
                modules = managers.module_manager.get_package_modules(package_name, package_version)
                active_modules.extend(modules)
        return active_modules
            

    def update_modules_library(self, managers):
        """ Add all plugins to the panel
        """
        self.clear()
        categories = {}
        active_modules = list(self._find_active_modules(managers))
        version_color = QtGui.QBrush(managers.style_manager.get_current_style().palette.node_text_muted)
        category_font = QtGui.QFont(self.font())
        category_font.setWeight(QtGui.QFont.DemiBold)

        for module in active_modules:
            category = module["module_category"]
            label = module["module_label"]
            version = module["module_version"]

            if not category:
                category = 'Uncategorized'

            if category not in categories:
                category_item = QtWidgets.QTreeWidgetItem(self, [category])
                flags=category_item.flags()
                flags=flags & ~QtCore.Qt.ItemFlag.ItemIsDragEnabled
                category_item.setFlags(flags)
                category_item.setFont(0, category_font)

                self.addTopLevelItem(category_item)
                # The name of a category spans the version column
                category_item.setFirstColumnSpanned(True)
                categories[category] = category_item

            category_item = categories[category]

            item = QtWidgets.QTreeWidgetItem(category_item)
            # Set user data to the module
            item.setData(0, QtCore.Qt.UserRole, module)
            item.setText(0, label)
            item.setText(1, version)
            item.setForeground(1, version_color)
            # Whole name, when the column is too narrow for it
            item.setToolTip(0, label)

        # Expand all top level items
        for i in range(self.topLevelItemCount()):
            self.topLevelItem(i).setExpanded(True)

        # Versions keep their width at the right; names take the rest and end
        # with "..." when the library is narrow.
        header = self.header()
        header.setStretchLastSection(False)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self._apply_filter()

    def set_filter(self, text):
        """ Show only the modules whose name, or the name of their category, contains
        all the words of a text (case ignored). An empty text shows all the modules.
        """
        self._filter_words = text.casefold().split()
        self._apply_filter()

    def _apply_filter(self):
        words = self._filter_words
        for i in range(self.topLevelItemCount()):
            category = self.topLevelItem(i)
            shown_count = 0
            for j in range(category.childCount()):
                item = category.child(j)
                module = item.data(0, QtCore.Qt.UserRole) or {}
                searched = " ".join((item.text(0), str(module.get("module_name", "")),
                                     category.text(0))).casefold()
                shown = all(word in searched for word in words)
                item.setHidden(not shown)
                shown_count += shown
            category.setHidden(shown_count == 0)
            if words and shown_count:
                category.setExpanded(True)

    def preferred_width(self):
        """ Width showing the whole names and versions of the modules, within limits. """
        versions = max(self.sizeHintForColumn(1), self.header().sectionSizeHint(1))
        margins = self.contentsMargins()
        width = self.sizeHintForColumn(0) + versions + margins.left() + margins.right() \
            + self.verticalScrollBar().sizeHint().width() + 8
        return max(self._MINIMUM_WIDTH, min(self._MAXIMUM_WIDTH, width))

    def startDrag(self, *args, **kwargs):
        """ Event called when the user start dragging a module item.
        
        In order to be able to transmit the module information to the scene,
        a MimeData is filled with the model of the module. 
        """
        item = self.currentItem()
        module = item.data(0, QtCore.Qt.UserRole)
        drag = QtGui.QDrag(self)
        mime_data = QtCore.QMimeData()
        mime_data.setText(json.dumps(module))
    
        drag.setMimeData(mime_data)

        drag.exec_(QtCore.Qt.MoveAction)
