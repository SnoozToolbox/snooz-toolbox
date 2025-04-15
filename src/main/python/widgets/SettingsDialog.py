"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from qtpy import QtCore
from qtpy import QtWidgets
from qtpy.QtWidgets import QMessageBox

from config import settings
from Managers.EndpointManager import MenuEndpointHandler
from ui.Ui_SettingsDialog import Ui_SettingsDialog

class SettingsDialog(QtWidgets.QDialog, Ui_SettingsDialog):
    """
    SettingsDialog
    Contains all user settings for the application.
    Left side is made of a listWidget and is used to select the category of 
    settings. Right side is made of a stackedWidget. When a settings is selected 
    in the listWidget the corresponding stack is shown to the user.
    """

    def __init__(self, managers, main_window, *args, **kwargs):
        super(SettingsDialog, self).__init__(*args, **kwargs)
        self._managers = managers
        self._settings_manager = managers.settings_manager
        self._main_window = main_window

        self.setupUi(self)
        self.packages_treewidget.setHeaderLabels(["Name", "Version", "Type", "Path"])
        self._load_package_list()

    def _load_package_list(self):
        activated_package_items = self._settings_manager.get_setting(settings.activated_package_items, None)

        for package in self._managers.package_manager.packages:
            for package_version in package.package_versions:
                if package_version.name in activated_package_items and package_version.version in activated_package_items[package_version.name]:
                    self._add_package_to_package_ui(package_version, activated_package_items[package_version.name][package_version.version])
                else:
                    self._add_package_to_package_ui(package_version, [])

        self.packages_treewidget.sortByColumn(0, QtCore.Qt.AscendingOrder)

    def plugins_on_add_from_folder(self):
        """"
            plugins_on_add_from_folder
            Ask the user for a package path. Load the package with the package 
            manager and add it to the list of packages if done successfully.
        """
        package_path = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Your Plugin Directory"))

        if package_path is None or package_path == '':
            return
        
        try:
            package_version = self._managers.package_manager.register_package(package_path, is_native=False)
            if package_version is None:
                return
            package_version.register_hooks()
        except Exception as err:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"{err}")
            msg.setWindowTitle("Import package error")
            msg.exec()
            return

        # Update the UI and user settings if the package was loaded successfully
        self._add_package_to_package_ui(package_version, None)
        self._settings_manager.append_setting(settings.packages, package_path)
        
    
    def plugins_on_remove(self):
        for selected_item in self.packages_treewidget.selectedItems():
            self.packages_treewidget.removeItemWidget(selected_item, 1)
            package_name = selected_item.text(0)
            package_version_number = selected_item.text(1)
            package_path = selected_item.text(3)

            # Remove from package manager
            self._managers.package_manager.unregister_package(package_name, package_version_number)

            # Remove from UI
            row_to_remove = self.packages_treewidget.currentIndex().row()
            self.packages_treewidget.takeTopLevelItem(row_to_remove)

            # Remove from user settings
            packages = self._settings_manager.get_setting(settings.packages, [])
            if isinstance(packages, str):
                self._settings_manager.set_setting(settings.packages, [])
            else:
                if package_path in packages:
                    packages.remove(package_path)
                    self._settings_manager.set_setting(settings.packages, packages)
    
    def reset_to_default(self):
        # Show a confirmation dialog
        confirm_dialog = QMessageBox()
        confirm_dialog.setIcon(QMessageBox.Question)
        confirm_dialog.setText("Are you sure you want to reset to default? This will automatically close the settings window.")
        confirm_dialog.setWindowTitle("Reset to Default")
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_dialog.setDefaultButton(QMessageBox.No)
        confirm_result = confirm_dialog.exec()

        # If the user confirms, clear the settings
        if confirm_result == QMessageBox.Yes:
            # list of settings to reset
            self._settings_manager.set_setting(settings.packages, [])
            self._settings_manager.set_setting(settings.skip_beta_disclaimer, None)
            self._settings_manager.set_setting(settings.recent_files, [])
            #self._settings_manager.set_setting(settings.activated_package_items, None)
            self._settings_manager.set_setting(settings.activated_package_items, [])

            # Update the current packages
            # TODO Need to properly handle the case when a tool or module is in used when we 
            # remove its package.
            self._managers.package_manager.deactivate_all_package()
            self._managers.package_manager.unregister_all_packages()

            self._managers.endpoint_manager.get_handler(MenuEndpointHandler.ENDPOINT_NAME).clear()
            self._managers.package_manager.activate_latest_packages()
            self._managers.package_manager.activate_packages_from_settings()
            # Remove from package manager

            # TODO instead of closing the settings dialog which can be confusing to the user, update it all
            # with default values while keeping it open.
            self.close()

    def apply_package_changes(self):
        # For each item within the tree^, check if it's checked.
        activated_package_items = {}
        for i in range(self.packages_treewidget.topLevelItemCount()):
            top_item = self.packages_treewidget.topLevelItem(i)
            package_name = top_item.text(0)
            package_version = top_item.text(1)

            selected_items = []
            for j in range(top_item.childCount()):
                tree_item = top_item.child(j)
                item_name = tree_item.text(0)
                check_state = tree_item.checkState(0)
                if check_state == QtCore.Qt.CheckState.Checked:
                    selected_items.append(item_name)

            if len(selected_items) > 0:
                # Strip any keyword after the package name like (pre-installed)
                package_name = package_name.split(" ")[0]
                if package_name not in activated_package_items:
                    activated_package_items[package_name] = {}

                activated_package_items[package_name][package_version] = selected_items
        
        self._settings_manager.set_setting(settings.activated_package_items, activated_package_items)
        
        self._managers.endpoint_manager.get_handler(MenuEndpointHandler.ENDPOINT_NAME).clear()
        self._managers.module_manager.unregister_all_modules()
        self._managers.package_manager.activate_packages_from_settings()
            
    def _add_package_to_package_ui(self, package_version, activated_items):
        '''
            Add a package to the UI

            Parameters:
                package_description (object): The package description object.

            Returns:
        '''
        # check if the package version is already loaded.
        package_name = package_version.name
        package_version_number = package_version.version
        package_path = package_version.package_path
        is_native = package_version.is_native

        # Add the package to the list
        if is_native:
            package_name = package_name + " (pre-installed)"
            package_item = QtWidgets.QTreeWidgetItem([package_name, package_version_number, None, package_path])
            package_item.setFlags(package_item.flags() | QtCore.Qt.ItemIsAutoTristate | QtCore.Qt.ItemIsUserCheckable)
        else:
            package_item = QtWidgets.QTreeWidgetItem([package_name, package_version_number, None, package_path])
            package_item.setFlags(package_item.flags() | QtCore.Qt.ItemIsAutoTristate | QtCore.Qt.ItemIsUserCheckable)

        # Add each of its module as children.
        for item in package_version.items:
            item_name = item.name
            item_type = item.description["item_type"].capitalize()
            item_version = item.version
            
            module_item = QtWidgets.QTreeWidgetItem([item_name, item_version, item_type, None])
            module_item.setFlags(module_item.flags() | QtCore.Qt.ItemIsAutoTristate | QtCore.Qt.ItemIsUserCheckable)

            if activated_items is not None and item.name in activated_items:
                module_item.setCheckState(0, QtCore.Qt.Checked)
            else:
                module_item.setCheckState(0, QtCore.Qt.Unchecked)

            module_item.setData(0, QtCore.Qt.UserRole, item)
            package_item.addChild(module_item)

        # Add the package item to the tree
        self.packages_treewidget.addTopLevelItems([package_item])