"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from Packages.PackageItems.PackageItem import PackageItem

class ProcessPackageItem(PackageItem):
    def __init__(self, package, item_json, item_path, pub_sub_manager):
        super().__init__(package, item_json, item_path, pub_sub_manager)
        self._sanity_check()

        # Add the current package as a dependency.
        package_version = self.get_package_dependency_version(self.package.name)
        if package_version is None:
            # Check if one of the modules requires it.
            for module in self._description["process_params"]["nodes"]:
                if module["package"]["package_name"] == self.package.name:
                    self._description["dependencies"].append({
                        "package_name": self.package.name,
                        "package_version": self.package.version
                    })
                    break
    
    # Properties
    @property
    def nodes(self):
        return self._description["process_params"]["nodes"]
    
    @property
    def subgraph_outputs(self):
        if "subgraph_params" not in self._description["process_params"] or \
            "outputs" not in self._description["process_params"]["subgraph_params"]:
            return {}
        return self._description["process_params"]["subgraph_params"]["outputs"]

    @property
    def deepcopy_outputs(self):
        if "subgraph_params" not in self._description["process_params"] or \
            "deepcopy_outputs" not in self._description["process_params"]["subgraph_params"]:
            return True
        return self._description["process_params"]["subgraph_params"]["deepcopy_outputs"]
    
    @property
    def subgraph_nodes_to_disable(self):
        if "subgraph_params" not in self._description["process_params"] or \
            "node_to_disable" not in self._description["process_params"]["subgraph_params"]:
            return []
        return self._description["process_params"]["subgraph_params"]["node_to_disable"]

    # Public methods
    def activate(self, params = None):
        self._pub_sub_manager.publish(self, "process_activation_request", self)
        # Open the process scene
        # Load the process JSON into the scene
        # Load all dependencies packages into memory (or just when executing)

    def get_module_info_by_id(self, module_id):
        for node in self.nodes:
            if node["identifier"] == module_id:
                return node
        return None

    def get_modules_dependencies(self):
        self._description["dependencies"]

    def get_package_dependency_version(self, package_name):
        for dependency in self._description["dependencies"]:
            if dependency["package_name"] == package_name:
                return dependency["package_version"]
        return None
    
    # Private methods
    def _sanity_check(self):
        if "process_params" not in self._description:
            raise Exception(f"Package item is missing 'process_params' key. File:{self.item_path}")
        
        if "nodes" not in self._description["process_params"]:
            raise Exception(f"Package item is missing 'nodes' key. File:{self.item_path}")
        
        for node in self._description["process_params"]["nodes"]:
            if "package" not in node:
                raise Exception(f"Package item is missing 'package' key. File:{self.item_path}")
            
            if "package_name" not in node["package"]:
                raise Exception(f"Package item is missing 'package_name' key. File:{self.item_path}")
            
            package_name = node["package"]["package_name"]
            if package_name != self.package.name:
                dependencies_package_names = [x["package_name"] for x in self._description["dependencies"]]
                if package_name not in dependencies_package_names:
                    raise Exception(f"Package item is missing a dependency declaration for module {node['module_name']} . File:{self.item_path}")
