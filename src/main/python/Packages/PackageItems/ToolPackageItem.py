"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
from Packages.PackageItems.ProcessPackageItem import ProcessPackageItem
from Managers.ToolManager import ToolManager

class ToolPackageItem(ProcessPackageItem):
    def __init__(self, package, item_json, item_path, pub_sub_manager):
        super().__init__(package, item_json, item_path, pub_sub_manager)
        self._sanity_check()
        self._activation_params = None

    # Properties
    @property
    def activation_params(self):
        return self._activation_params

    @property
    def steps(self):
        return self._description["tool_params"]["steps"]

    # Public methods
    def activate(self, params = None):
        self._activation_params = params
        self._pub_sub_manager.publish(self, ToolManager.ACTIVATION_TOPIC, self)
    
    # Private methods
    def _sanity_check(self):
        if "tool_params" not in self._description:
            raise Exception(f"Package item is missing 'tool_params' key. File:{self.item_path}")
        
        if "steps" not in self._description["tool_params"]:
            raise Exception(f"Package item is missing 'steps' key. File:{self.item_path}")
        