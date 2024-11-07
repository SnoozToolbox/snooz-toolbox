"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
import importlib

from Packages.PackageItems.PackageItem import PackageItem

class AppPackageItem(PackageItem):
    def __init__(self, package, item_json, item_path, managers):
        super().__init__(package, item_json, item_path, managers.pub_sub_manager)
        self._sanity_check()
        self._description['module'] = f"{self.package.name}.{self._description['item_name']}"
        self._managers = managers
    
    # Public methods
    def activate(self, params = None):
        # Load the app into a new tab on the main window.
        self._pub_sub_manager.publish(self, "app_activation_request", params)

    def create_app_view(self, params):
        class_name = f"{self.name}View"
        module_name = f"{self._description['module']}.{class_name}"
        module = importlib.import_module(module_name)
        AppView = getattr(module, class_name)
        app_view = AppView(self._managers, params)
        return app_view
    
    # Private methods
    def _sanity_check(self):
        if "app_params" not in self._description:
            raise Exception(f"Package item is missing 'app_params' key. File:{self.item_path}")

    

