"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
import json
import os
import sys

from qtpy.QtWidgets import QMessageBox

import config
from config import settings
from Managers.Manager import Manager
from Packages.Package import Package
from Packages.PackageVersion import PackageVersion
from Packages.PackageItems.PackageItem import PackageItem

class PackageManager(Manager):
    """ Package manager. 
    
    In Snooz, all modules, tools and apps are contained within packages. The package 
    manager is responsible for handling the life cycle of those packages.

    Native packages are the one that are loaded from the resources folder of the 
    application. They are included with the installation of the software.

    An active package is a package which its path is in the sys.path variable. This
    allows the application to find its content. Loading a depencency is done by activating the package.

    A package item is a module, tool or app contained within a package.
    """
    def __init__(self, managers):
        """ Init the package manager. 

        Parameters
        ----------
            managers : Managers
                The managers
        """
        super().__init__(managers)
        self._packages = []
        self._modules_reference = None
        self._loaded_dependencies_paths = []

    @property
    def packages(self):
        return self._packages

    # Public functions
    def initialize(self):
        """ Initialize the package manager. """
        self._record_modules_reference()
        self._register_native_packages()
        self._register_user_packages()
        activated_package_items = self._managers.settings_manager.get_setting(settings.activated_package_items, None)

        # If it's the first time the app is launched, activate all items from all latest version of the packages
        if isinstance(activated_package_items, list) and len(activated_package_items) == 0:
            self.activate_latest_packages()
        elif activated_package_items is None:
            self.activate_latest_packages()
        self.activate_packages_from_settings()

    def activate_latest_packages(self):
        activated_package_items = {}
        for package in self._packages:
            package_version = package.latest_version

            if package.name not in activated_package_items:
                activated_package_items[package.name] = {package_version.version:[]}

            for item in package_version.items:
                activated_package_items[package.name][package_version.version].append(item.name)
            
        self._managers.settings_manager.set_setting(settings.activated_package_items, activated_package_items)

    def activate_package(self, package_name, package_version_number):
        """ Activate a specific version of a package.
        
        Activating means adding the root path of the package to the sys.path variable.
        This allows the application to find its content.

        Parameters
        ----------
        package_name : str
            The name of the package
        package_version_number : str
            The version number of the package
        """
        package = self.get_package(package_name)
        if package is None:
            self._managers.pub_sub_manager.publish(self, "show_error_message", f"activate_package: Package not found {package_name}")
            return

        package_version = package.get_package_version(package_version_number)

        if package_version is not None:
            package.active_version = package_version
            self._add_to_sys_path(package_version.root_path)
        else:
            self._managers.pub_sub_manager.publish(self, "show_error_message", f"activate_package: Package version not found {package_name} {package_version_number}")
            return

    def deactivate_all_package(self):
        """ Deactivate all packages. 
        
        Deactivating means removing the root path of the package from the sys.path variable.
        """
        for package in self._packages:
            if package.active_version is not None:
                self._remove_from_sys_path(package.active_version.root_path)
                package.active_version = None
        self._reset_modules()

    def _get_package_version(self, package_name:str, package_version:str) -> PackageVersion:
        """ Get the package version.

        Parameters
        ----------
        package_name : str
            The name of the package
        package_version : str
            The version number of the package

        Returns
        -------
        package_version : PackageVersion
            The specific version of this package
        """
        package = self.get_package(package_name)

        if package is None:
            return None
        
        return package.get_package_version(package_version)

    def get_package(self, name) -> Package:
        """ Get the package.

        Parameters
        ----------
        name : str
            The name of the package

        Returns
        -------
        package : Package
            The package
        """
        for package in self._packages:
            if package.name == name:
                return package
        return None
    
    def get_package_item(self, package_name:str, package_version:str, item_name:str) -> PackageItem:
        """ Get the package item.

        Parameters
        ----------
        package_name : str
            The name of the package
        package_version : str
            The version number of the package
        item_name : str
            The name of the item

        Returns
        -------
        package_item : PackageItem
            The package item
        """
        package_version = self._get_package_version(package_name, package_version)

        if package_version is None:
            return None

        return package_version.get_item(item_name)
        
    def register_package(self, package_path:str, is_native=False):
        """ Register a package.

        Parameters
        ----------
        package_path : str
            The path of the package
        is_native : bool
            Whether the package is native or not
        """
        try:

            # find the description file of the package within the path
            # we assume the name of the file is the same as the package folder
            # with a json extension
            package_name = os.path.basename(package_path)

            package_description_file = os.path.join(package_path, f"{package_name}.json")
            if not os.path.exists(package_description_file):
                message = f"Package description file not found: {package_description_file}"
                self._managers.pub_sub_manager.publish(self, "show_error_message", message)
                return None
            
            # Check if the package is already registered, if not create it. The Package object is
            # just a shell that contains different versions of the package.
            package = self.get_package(package_name)
            if package is None:
                package = Package(package_name, self._managers)

            # Check if the package version is already registered
            package_version_number = self._read_package_version(package_description_file)
            package_version = package.get_package_version(package_version_number)
            if package_version is not None:
                message = f"Package version already registered: {package_name} - {package_version_number}"
                self._managers.pub_sub_manager.publish(self, "show_error_message", message)
                return None

            package.load_package_version(package_path, is_native)
            
        except Exception as e:
            message = f"Failed to load package. {e} File:{package_path}"
            self._managers.pub_sub_manager.publish(self, "show_error_message", message)
            return None
        
        if package not in self._packages:
            self._packages.append(package)

        package_version = package.get_package_version(package_version_number)
        return package_version
    
    def unregister_all_packages(self):
        """ Unregister all packages. """
        package_to_remove = []
        for package in self._packages:
            package_versions_to_remove = []
            for package_version in package.package_versions:
                if not package_version.is_native:
                    package_version.unregister_hooks()
                    package_versions_to_remove.append(package_version)

            for package_version in package_versions_to_remove:
                self.unregister_package(package.name, package_version.version)

            # if len(package.package_versions) == 0:
            #     package_to_remove.append(package)

        ## the package has been removed in self.unregister_package
        # for package in package_to_remove:
        #     self._packages.remove(package)

    def unregister_package(self, package_name, package_version_number):
        """ Unregister a package.
        
        Parameters
        ----------
        package_name : str
            The name of the package
        package_version_number : str
            The version number of the package

        """
        package = self.get_package(package_name)
        if package is None:
            return

        package_version = package.get_package_version(package_version_number)
        if package_version is None:
            return

        package_version.unregister_hooks()
        package.package_versions.remove(package_version)

        if len(package.package_versions) == 0:
            self._packages.remove(package)

        return package_version
    
    def check_missing_packages(self, packages):
        missing_packages = []
        for package_description in packages:
            package_version = package_description["package_version"]
            package_name = package_description["package_name"]
            p = self._find_package(package_name, package_version)
            if p is None:
                missing_packages.append(package_description)

        return missing_packages
    
    def _find_package(self, package_name, package_version):
        for package in self._packages:
            if package.name == package_name:
                package = package.get_package_version(package_version)
                if package is not None:
                    return package
        return None

    def _register_native_packages(self):
        """ Register the native packages. 
        
        Native packages are the ones that are included with the installation of the software.
        They are loaded from the resources folder of the application."""
        try:
            native_package_path = config.app_context.get_resource('packages')
            subfolders = [f.path for f in os.scandir(native_package_path) if f.is_dir()]
            for subfolder in subfolders:
                subsubfolders = [f.path for f in os.scandir(subfolder) if f.is_dir()]
                for subsubfolder in subsubfolders:
                    try:
                        self.register_package(subsubfolder, is_native=True)
                    except (Exception, FileNotFoundError) as err:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText(f"{err}")
                        msg.setWindowTitle("Import package error")
                        msg.exec()
        except FileNotFoundError:
            message = f"Native package path not found: {native_package_path}"
            self._managers.pub_sub_manager.publish(self, "show_error_message", message)
    
    def _register_user_packages(self):
        # Load package settings
        packages = self._managers.settings_manager.get_setting(settings.packages, [])

        # This is a hack. When we record a setting with a list of str but with only 1 
        # element in the list. QSettings will convert it automatically to a string.
        # This converts it back into a list.
        if isinstance(packages, str):
            packages = [packages]
            
        if packages is None:
            self._managers.settings_manager.set_setting(settings.packages, [])
        else:
            packages_to_remove = []
            for package_path in packages:
                if not os.path.isdir(package_path):
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Package not found.")
                    msg.setInformativeText(f"The package was not found and has been removed from your settings: {package_path}")
                    msg.setWindowTitle("Package not found.")
                    msg.exec()
                    packages_to_remove.append(package_path)
                else:
                    try:
                        self.register_package(package_path)
                    except:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("Package not found.")
                        msg.setInformativeText(f"The package was not found and has been removed from your settings: {package_path}")
                        msg.setWindowTitle("Package not found.")
                        msg.exec()
                        packages_to_remove.append(package_path)

            # Clean up missing packages
            if len(packages_to_remove) > 0:
                for package_path in packages_to_remove:
                    packages.remove(package_path)
                self._managers.settings_manager.set_setting(settings.packages, packages)

    def activate_packages_from_settings(self):
        activated_package_items = self._managers.settings_manager.get_setting(settings.activated_package_items, None)

        for package_name, package_versions in activated_package_items.items():
            for package_version_number, package_items in package_versions.items():
                for package_item_name in package_items:
                    package = self.get_package(package_name)
                    if package is not None:
                        package_version = package.get_package_version(package_version_number)
                        if package_version is not None:
                            package_item = package_version.get_item(package_item_name)
                            for hook in package_item.hooks:
                                self._managers.endpoint_manager.register_hook(hook)


    def _add_to_sys_path(self, path):
        """ Add a path to the sys.path variable. 
        
        Parameters
        ----------
        path : str
            The path to add
        """
        if path not in sys.path:
            sys.path.append(path)
            self._loaded_dependencies_paths.append(path)

    def _remove_from_sys_path(self, path):
        """ Remove a path from the sys.path variable. 
        
        Parameters
        ----------
        path : str
            The path to remove
        """
        if path in sys.path:
            sys.path.remove(path)
            self._loaded_dependencies_paths.remove(path)

    # Private functions
    def _record_modules_reference(self):
        """ Record the reference of the modules. 
        
        sys.modules contains all the modules that have been imported in python. When an
        object is created, Python looks into this list to find the module to load from memory
        instead of loading it from disk.

        Since Snooz use the concept of version package. The same python class can point to
        different versions on disk. This reference allow us to get back to a blank state
        whenever we change package version.        
        """
        self._modules_reference = list(sys.modules)

    def _reset_modules(self):
        """ Reset the modules.
        
        When we change package version, we need to remove all the modules that have been
        loaded from memory. """
        if self._modules_reference is None:
            return
        
        modules = list(sys.modules)
        new_modules = [module for module in modules if module not in self._modules_reference]
        for m in new_modules:
            del sys.modules[m]

    def _read_package_version(self, package_description_file):
        """ Read the package version.

        Parameters
        ----------
        package_description_file : str
            The path to the package description file

        Returns
        -------
        package_version : str
            The package version
        """
        # Read the json to get the package_version
        with open(package_description_file, "r") as f:
            description = json.load(f)
            if "package_version" not in description:
                return None
            return description["package_version"]