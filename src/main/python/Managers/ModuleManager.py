"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
from Managers.Manager import Manager

class ModuleManager(Manager):
    """ ModuleManager is a manager for modules.
    
    ModuleManager is used within the process tab to handle which modules are currently
    available to a process and to load their dependencies.

    Note:
    A package is a generic term for a collection of modules.
    A package version is a specific version of a package that contains specific modules.

    """

    def __init__(self, managers):
        """ Init the ModuleManager."""
        super().__init__(managers)
        self._packages = {}

    def initialize(self):
        """ Initialize the ModuleManager. """
        pass

    def unload_all_modules_dependencies(self):
        """ Unload all modules dependencies. """
        self._managers.package_manager.deactivate_all_package()

    def load_latest_modules_dependencies(self):
        """ Load dependencies of the latest version of all modules. """
        for package_name in self._packages.keys():
            version_number = self._packages[package_name][0]['package_version']
            self._managers.package_manager.activate_package(package_name, version_number)

    def register_module(self,module_item):
        """ Register a module. 
        
        Add the module to the list of modules that will be 
        shown in the process window.

        Parameters
        ----------
        module_item : dict
            The module to register
        """
        mn = module_item["item_name"]
        mv = module_item["item_version"]
        pn = module_item["package_name"]
        pv = module_item["package_version"]
        label = module_item["parameters"]["module_label"]
        category = module_item["parameters"]["module_category"]
        
        if pn not in self._packages:
            self._packages[pn] = []
        
        package_version = self._get_package_version(pn, pv)
        
        if package_version is None:
            package_version = {
            "modules": [],
            "package_version": pv
            }
            self._packages[pn].append(package_version)
            self._packages[pn].sort(key=self._version_to_int, reverse=True)

        if (mn, mv) not in package_version["modules"]:
            module = {
                "module_name": mn,
                "module_version": mv,
                "module_label": label,
                "module_category": category,
                "package_name": pn,
                "package_version": pv
            }
            package_version["modules"].append(module)

    def unregister_all_modules(self):
        """ Unregister all modules. """
        self._packages = {}

    def unregister_module(self, hook):
        """ Unregister a module.

        Remove the module from the list of modules that will be 
        shown in the process window.
        
        Parameters
        ----------
        hook : dict
            The module to unregister
        """
        mn = hook["item_name"]
        mv = hook["item_version"]
        pn = hook["package_name"]
        pv = hook["package_version"]
        
        if pn in self._packages:
            package_versions = self._packages[pn]
            for package_version in package_versions:
                if package_version["package_version"] == pv:
                    for module in package_version["modules"]:
                        if module["module_name"] == mn and module["module_version"] == mv:
                            package_version["modules"].remove(module)
                    
                    if len(package_version["modules"]) == 0:
                        package_versions.remove(package_version)
            
            if len(package_versions) == 0:
                del self._packages[pn]


    def get_package_modules(self, package_name:str, package_version_number:str):
        """ Get the modules of a package.
        
        Parameters
        ----------
        package_name : str
            The name of the package
        package_version_number : str
            The version number of the package

        Returns
        -------
        modules : list
            The list of modules of the package
        """
        package_version = self._get_package_version(package_name, package_version_number)
        if package_version is None:
            return []
        return package_version["modules"]

    def _get_package_version(self, package_name:str, package_version:str):
        """ Get the package version. 
        
        Parameters
        ----------
        package_name : str
            The name of the package
        package_version : str
            The version number of the package

        Returns
        -------
        package_version : dict
            The specific version of this package
        """
        if package_name not in self._packages:
            return None
        
        package_versions = self._packages[package_name]
        for pv in package_versions:
            if pv["package_version"] == package_version:
                return pv

        return None
    
    def _version_to_int(self, package_version):
        """
        Convert from a string representation of a version: 0.1.1 to an int: 11
        examples:
        0.0.1 -> 1
        0.1.0 -> 10
        1.0.0 -> 100
        1.1 -> 110
        1 -> 100

        Parameters
        ----------
            package_version (PackageVersion): The PackageVersion that will be sorted

        Returns
        -------
            v_int (int): An int representation of the PackageVersion's version.
        """
        v = package_version["package_version"].split(".")
        while len(v) < 3:
            v.append("0")

        v_string = ''.join(v)
        v_int = int(v_string)

        return v_int