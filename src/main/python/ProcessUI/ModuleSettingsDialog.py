"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    ModuleSettingsDialog
"""
from qtpy import QtCore
from qtpy import QtWidgets

from ui.Ui_ModuleSettingsDialog import Ui_ModuleSettingsDialog
from Packages.PackageItems.ModulePackageItem import ModulePackageItem

class ModuleSettingsDialog(QtWidgets.QDialog, Ui_ModuleSettingsDialog):
    def __init__(self, managers, *args, **kwargs):
        super(ModuleSettingsDialog, self).__init__(*args, **kwargs)
        self._managers = managers
        self.setupUi(self)
        self._init_ui()

    def _init_ui(self):
        self.package_treewidget.clear()
        for package in self._managers.package_manager.packages:
            package_item = QtWidgets.QTreeWidgetItem([package.name])

            has_modules = False
            for package_version in package.package_versions:
                if not self._has_modules(package_version):
                    continue
                has_modules = True

                version_item = QtWidgets.QTreeWidgetItem([package_version.version])
                version_item.setFlags(version_item.flags() | QtCore.Qt.ItemIsUserCheckable)
                package_item.addChild(version_item)

                if package_version == package.active_version:
                    version_item.setCheckState(0, QtCore.Qt.Checked)
                else:
                    version_item.setCheckState(0, QtCore.Qt.Unchecked)

                for module in self._get_modules(package_version):
                    module_item = QtWidgets.QTreeWidgetItem([module.name, module.version])
                    version_item.addChild(module_item)
                    
                    self.package_treewidget.expandItem(module_item)

            if has_modules:
                self.package_treewidget.addTopLevelItem(package_item)
                self.package_treewidget.expandItem(package_item)

        self.package_treewidget.resizeColumnToContents(0)
        self.package_treewidget.resizeColumnToContents(1)
        self.package_treewidget.sortByColumn(0, QtCore.Qt.DescendingOrder)

    def apply_clicked(self):
        # Check all active version and add them to the dictionary where
        # we had the reference at start.
        self._managers.module_manager.unload_all_modules_dependencies()

        for i in range(self.package_treewidget.topLevelItemCount()):
            top_item = self.package_treewidget.topLevelItem(i)
            package_name = top_item.text(0)
            for j in range(top_item.childCount()):
                version_item = top_item.child(j)
                package_version = version_item.text(0)
                check_state = version_item.checkState(0)
                if check_state == QtCore.Qt.CheckState.Checked:
                    self._managers.package_manager.activate_package(package_name, package_version)
        self.close()

    def cancel_clicked(self):
        self.close()

    def data_changed(self, item):
        self.package_treewidget.blockSignals(True)
        package_item = item.parent()
        for i in range(package_item.childCount()):
            version_item = package_item.child(i)
            if version_item is not item:
                version_item.setCheckState(0, QtCore.Qt.Unchecked)

        self.package_treewidget.blockSignals(False)

    def _has_modules(self, package_version):
        for item in package_version.items:
            if isinstance(item, ModulePackageItem):
                return True
        return False
    
    def _get_modules(self, package_version):
        modules = []
        for item in package_version.items:
            if isinstance(item, ModulePackageItem):
                modules.append(item)
        return modules
    
    def _has_modules(self, package_version):
        return self._get_modules(package_version) != []
        