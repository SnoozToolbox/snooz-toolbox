"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from Packages.PackageItems.AppPackageItem import AppPackageItem
from Packages.PackageItems.CustomPackageItem import CustomPackageItem
from Packages.PackageItems.ModulePackageItem import ModulePackageItem
from Packages.PackageItems.ProcessPackageItem import ProcessPackageItem
from Packages.PackageItems.ToolPackageItem import ToolPackageItem

class PackageItemFactory():
    def create_item(package, item_json, item_path, managers):
        item_type = item_json["item_type"]

        if item_type == "app":
            return AppPackageItem(package, item_json, item_path, managers)
        elif item_type == "tool":
            return ToolPackageItem(package, item_json, item_path, managers.pub_sub_manager)
        elif item_type == "process":
            return ProcessPackageItem(package, item_json, item_path, managers.pub_sub_manager)
        elif item_type == "custom":
            return CustomPackageItem(package, item_json, item_path, managers.pub_sub_manager)
        elif item_type == "module":
            return ModulePackageItem(package, item_json, item_path, managers.pub_sub_manager)
        else:
            raise Exception(f"Unknown item type: {item_type}")