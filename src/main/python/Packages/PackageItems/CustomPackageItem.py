"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
from Packages.PackageItems.PackageItem import PackageItem

class CustomPackageItem(PackageItem):
    def __init__(self, package, item_json, item_path, pub_sub_manager):
        super().__init__(package, item_json, item_path, pub_sub_manager)
    
    def activate(self, params = None):
        pass
