"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
import gc
import json
import os
import platform
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
            return False

        package_version = package.get_package_version(package_version_number)

        if package_version is not None:
            package.active_version = package_version
            self._add_to_sys_path(package_version.root_path)
        else:
            self._managers.pub_sub_manager.publish(self, "show_error_message", f"activate_package: Package version not found {package_name} {package_version_number}")
            return False
        return True

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

            # Validate if the package items has a valid api version.
            valid_package = self._validate_package_api_version(package_description_file)
            if not valid_package:
                message = f"This package uses an outdated or unsupported API version. Please update it to match the current Snooz API version ({config.settings.active_api_version})."
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

    def _validate_package_api_version(self, description_file_path):
        """
        Validates if the package API version in the description file matches with the active API version of Snooz.

        Do note that the description file's path has already been validated prior to entering this method.

        Parameters:
        -----------
        description_file_path : str
            The absolute path to the package description file

        Returns:
        --------
            bool: True if every versions matches, False if there is a mismatch.
        """
        # We already make sure the description file exists before going into this method.
        with open(description_file_path, 'r') as f:
            data = json.load(f)
    
            def check_integer(version) -> int:
                version_parts = list(map(int, version.split(".")))
                return version_parts[0]

            current_version = check_integer(config.settings.active_api_version)
            package_version = check_integer(data.get("package_api_version"))

            return package_version >= current_version 
                        
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
        loaded from memory. However, we must be careful not to remove C++ extension modules
        like PyTorch, as they cannot be safely reimported in the same Python process.
        """
        if self._modules_reference is None:
            return
       
        modules = list(sys.modules)
        new_modules = [module for module in modules if module not in self._modules_reference]
       
        # List of C++ extension modules that should NOT be removed from sys.modules
        # during execution as they cannot be safely reimported
        protected_modules = config.memory_config.PROTECTED_DURING_EXECUTION
       
        for m in new_modules:
            # Check if this module or any of its parent modules are protected
            should_protect = False
            for protected in protected_modules:
                if m == protected or m.startswith(protected + '.'):
                    should_protect = True
                    break
           
            if not should_protect:
                del sys.modules[m]
            # else:
            #     print(f"Protected module from reset: {m}")  # Debug info

    def _force_memory_cleanup(self):
        """
        Force aggressive memory cleanup using cross-platform techniques.
        
        This method attempts to release virtual memory back to the OS using
        platform-specific techniques that work on Windows, macOS, and Linux.
        """
        # First, do multiple aggressive garbage collection cycles
        for _ in range(5):  # Increased from 3 to 5 for shutdown
            gc.collect()
        
        # Platform-specific memory management
        try:
            if platform.system() == "Windows":
                self._windows_memory_cleanup()
            elif platform.system() == "Darwin":  # macOS
                self._macos_memory_cleanup()
            elif platform.system() == "Linux":
                self._linux_memory_cleanup()
        except Exception as e:
            # Silent failure - memory cleanup is best effort
            pass
    
    def _windows_memory_cleanup(self):
        """Windows-specific memory cleanup using ctypes."""
        try:
            import ctypes
            from ctypes import wintypes
            
            # Get current process handle
            kernel32 = ctypes.windll.kernel32
            current_process = kernel32.GetCurrentProcess()
            
            # More aggressive Windows cleanup for shutdown
            # Empty working set - forces Windows to page out unused memory
            kernel32.SetProcessWorkingSetSize(current_process, -1, -1)
            kernel32.EmptyWorkingSet(current_process)
            
            # Additional aggressive cleanup for shutdown
            # Try to trim the working set to minimum
            kernel32.SetProcessWorkingSetSize(current_process, 0x100000, 0x200000)  # 1-2MB range
            kernel32.EmptyWorkingSet(current_process)
            
        except Exception:
            pass
    
    def _macos_memory_cleanup(self):
        """macOS-specific memory cleanup."""
        try:
            import ctypes
            import ctypes.util
            
            # Load libc
            libc_path = ctypes.util.find_library("c")
            if libc_path:
                libc = ctypes.CDLL(libc_path)
                
                # Call malloc_zone_pressure_relief to release memory zones
                if hasattr(libc, 'malloc_zone_pressure_relief'):
                    libc.malloc_zone_pressure_relief(None, 0)
                
                # Also try malloc_zone_try_free_default
                if hasattr(libc, 'malloc_zone_try_free_default'):
                    libc.malloc_zone_try_free_default(None)
                    
        except Exception:
            pass
    
    def _linux_memory_cleanup(self):
        """Linux-specific memory cleanup."""
        try:
            import ctypes
            import ctypes.util
            
            # Load libc
            libc_path = ctypes.util.find_library("c")
            if libc_path:
                libc = ctypes.CDLL(libc_path)
                
                # Call malloc_trim to release unused heap memory back to OS
                if hasattr(libc, 'malloc_trim'):
                    libc.malloc_trim(0)
                    
        except Exception:
            pass

    def cleanup_for_shutdown(self):
        """
        Comprehensive cleanup method to call when shutting down Snooz.
        
        This method should be called when the application is closing to ensure
        maximum memory is released back to the operating system.
        Unlike normal cleanup, this removes ALL modules since we're shutting down.
        """
        # First deactivate all packages normally
        self.deactivate_all_package()
        
        # For shutdown, clear ALL modules that were loaded after startup
        self._cleanup_all_modules_for_shutdown()
        
        # Force aggressive memory cleanup
        self._force_memory_cleanup()
        
        # Final garbage collection
        gc.collect()
    
    # def _cleanup_safe_protected_modules(self):
    #     """
    #     Remove some protected modules that can be safely cleaned up on shutdown.
        
    #     This is more aggressive than _reset_modules but only targets modules
    #     that are known to be safe for removal during application shutdown.
    #     """
    #     if self._modules_reference is None:
    #         return
            
    #     modules = list(sys.modules.keys())
    #     safe_to_remove = set()
        
    #     # Modules that are generally safe to remove during execution
    #     # These are large but don't have C++ extensions that can't be reloaded
    #     safe_patterns = config.memory_config.SAFE_TO_REMOVE_DURING_EXECUTION
        
    #     for module_name in modules:
    #         if module_name not in self._modules_reference:
    #             for pattern in safe_patterns:
    #                 if module_name.startswith(pattern):
    #                     safe_to_remove.add(module_name)
    #                     break
        
    #     # Remove the safe modules
    #     for module_name in safe_to_remove:
    #         try:
    #             if module_name in sys.modules:
    #                 del sys.modules[module_name]
    #         except Exception:
    #             # Silent failure for safety
    #             pass

    def _cleanup_all_modules_for_shutdown(self):
        """
        Remove ALL modules loaded after startup when shutting down Snooz.
        
        This is the most aggressive cleanup - removes everything including
        normally protected modules since we're shutting down the entire application.
        No need to preserve anything for future use.
        
        IMPORTANT: At shutdown, ALL modules are targets for removal.
        The PROTECTED_DURING_EXECUTION list is ignored here because
        we don't need stability after shutdown - we want maximum memory cleanup.
        """
        if self._modules_reference is None:
            return
            
        modules = list(sys.modules.keys())
        modules_to_remove = []
        
        # Identify all modules loaded after Snooz startup
        for module_name in modules:
            if module_name not in self._modules_reference:
                modules_to_remove.append(module_name)
        
        # Remove ALL modules (including previously protected ones)
        removed_count = 0
        for module_name in modules_to_remove:
            try:
                if module_name in sys.modules:
                    del sys.modules[module_name]
                    removed_count += 1
            except Exception:
                # Silent failure - some modules might be in use by Python internals
                pass
        
        # Also try to remove some core modules that are safe to remove on shutdown
        # These include ALL the normally protected modules since we're shutting down
        additional_cleanup_patterns = [
            'numpy', 'scipy', 'sklearn', 'pandas', 'matplotlib',
            'torch', 'numba', 'cv2', 'PIL', 'h5py', 'netCDF4',
            'mne', 'seaborn', 'plotly', 'bokeh', 'statsmodels'
        ]
        
        for pattern in additional_cleanup_patterns:
            modules_to_check = [name for name in sys.modules.keys() if name.startswith(pattern)]
            for module_name in modules_to_check:
                try:
                    if module_name in sys.modules:
                        del sys.modules[module_name]
                        removed_count += 1
                except Exception:
                    # Silent failure
                    pass
        
        print(f"Shutdown cleanup: Removed {removed_count} modules from memory")


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