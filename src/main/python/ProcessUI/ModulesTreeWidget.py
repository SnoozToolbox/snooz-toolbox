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
    def __init__(self, parent=None):
        super().__init__(parent)

        """ Initialise the visual of the plugin library widget. """
        self.setSortingEnabled(True)
        self.sortByColumn(0,QtCore.Qt.AscendingOrder)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.setDragEnabled(True)

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

                self.addTopLevelItem(category_item)
                categories[category] = category_item

            category_item = categories[category]

            item = QtWidgets.QTreeWidgetItem(category_item)
            # Set user data to the module
            item.setData(0, QtCore.Qt.UserRole, module)
            item.setText(0, label)
            item.setText(1, version)
      
        # Expand all top level items
        for i in range(self.topLevelItemCount()):
            self.topLevelItem(i).setExpanded(True)

        self.resizeColumnToContents(0)
        self.resizeColumnToContents(1)

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
