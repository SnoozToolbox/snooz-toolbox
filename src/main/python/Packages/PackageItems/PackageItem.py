"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
import os
import json
from Managers.PubSubManager import PubSubManager

class PackageItem(object):
    def __init__(self, package, item_json, item_path, pub_sub_manager:PubSubManager):
        self._package = package
        self._item_description_file = None
        self._description = self._load_item_description(item_path)
        self._hooks = item_json["item_hooks"]
        self._item_version = item_json["item_version"]
        self._item_path = item_path
        self._pub_sub_manager = pub_sub_manager

    # Properties
    @property
    def item_description_file(self):
        return self._item_description_file
    
    @property
    def package(self):
        return self._package

    @property
    def item_path(self):
        return self._item_path

    @property
    def description(self):
        return self._description
    
    @property
    def name(self):
        if "item_name" not in self._description:
            raise Exception(f"Package item is missing 'item_name' key. File:{self._description}")
        return self._description["item_name"]
    
    @property
    def version(self):
        return self._item_version
    
    @property
    def hooks(self):
        return self._hooks
    
    # Public Functions
    def activate(self, params = None):
        raise NotImplementedError
    
    def get_dependencies(self):
        return self._description["dependencies"]

    # Private Functions
    def _load_item_description(self, item_path):
        name = os.path.basename(item_path)
        self._item_description_file = os.path.join(item_path, f"{name}.json" )
        if not os.path.exists(self._item_description_file):
            raise Exception(f"Package item description file does not exist. File:{self._item_description_file}")
        
        with open(self._item_description_file, "r") as f:
            return json.load(f)

        