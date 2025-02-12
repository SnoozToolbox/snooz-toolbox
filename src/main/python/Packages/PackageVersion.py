"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
import json
import os

from Packages.PackageItems.PackageItemFactory import PackageItemFactory
from Packages.PackageItems.PackageItem import PackageItem

class PackageVersion(object):
    def __init__(self, package_path, managers, is_native = False):
        super().__init__()
        self._managers = managers
        self._path = package_path
        package_name = os.path.basename(package_path)
        self._filename = os.path.join(package_path, f"{package_name}.json")
        self._root_path = os.path.dirname(package_path.rstrip(os.sep))
        self._hooks_description = []
        self._description = None
        self._items = []
        self._is_native = is_native
        self._read_description(self._filename)
        self._create_package_items()

    # Properties
    @property
    def items(self):
        return self._items

    @property
    def root_path(self):
        return self._root_path

    @property
    def package_path(self):
        return self._path

    @property
    def name(self):
        if "package_name" not in self._description:
            raise Exception(f"Package is missing 'package_name' key. File:{self._description}")
        return self._description["package_name"]
    
    @property
    def version(self):
        if "package_version" not in self._description:
            raise Exception(f"Package is missing 'package_version' key. File:{self._description}")
        return self._description["package_version"]

    @property
    def is_native(self):
        return self._is_native

    # Public methods
    def get_item(self, item_name) -> PackageItem:
        for item in self._items:
            if item.name == item_name:
                return item

    def register_hooks(self):
        for item in self._items:
            for hook in item.hooks:
                try:
                    self._managers.endpoint_manager.register_hook(hook)
                
                except Exception as e:
                    raise Exception(f"Failed to load package item. {e}")


    def unregister_hooks(self):
        for item in self._items:
            for hook in item.hooks:
                self._managers.endpoint_manager.unregister_hook(hook)

    # Private methods
    def _read_description(self, filename):
        # parse the filename and transform the JSON text into an dict.
        with open(filename, "r") as f:
            self._description = json.load(f)

            if "items" not in self._description:
                raise Exception(f"Package description file is missing 'items' key. File:{filename}")
            if "package_name" not in self._description:
                raise Exception(f"Package description file is missing 'package_name' key. File:{filename}")
            if "package_version" not in self._description:
                raise Exception(f"Package description file is missing 'package_version' key. File:{filename}")

    def _create_package_items(self):
        # Format check before doing anything
        for item in self._description["items"]:
            if "item_hooks" not in item:
                raise Exception(f"Package description file is missing 'item_hooks' key. File:{self._filename}")
        
        for item_json in self._description["items"]:
            item_path = os.path.join(self.package_path, item_json["item_name"])
            item = PackageItemFactory.create_item(self, item_json, 
                                                  item_path, self._managers)
            
            for hook in item.hooks:
                hook["item_version"] = item.version
                hook["item_name"] = item.name
                hook["package_name"] = self.name
                hook["package_version"] = self.version

            self._items.append(item)