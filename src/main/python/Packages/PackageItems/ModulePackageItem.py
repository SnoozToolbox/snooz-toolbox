"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from Packages.PackageItems.PackageItem import PackageItem

class ModulePackageItem(PackageItem):
    def __init__(self, package, item_json, item_path, pub_sub_manager):
        super().__init__(package, item_json, item_path, pub_sub_manager)
        
    def activate(self, params = None):
        pass

    def get_module_info(self):
        return {
            "name": self.name,
            "module_version": self.version,
            "package_name": self.package.name,
            "package_version": self.package.version
        }