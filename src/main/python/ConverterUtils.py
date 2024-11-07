import copy
import json
import os
from qtpy import QtWidgets

_modules = {}
_tools = {}

def convert_package_to_v100(self):
    # Open folder
    folder_path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select folder to save converted files")
    if not folder_path:
        return
    
    # get the description.json file in it
    description_filepath = os.path.join(folder_path, 'description.json')
    if not os.path.exists(description_filepath):
        return
    
    with open(description_filepath, 'r') as f:
        package_description = json.load(f)
    # Get folder name
    folder_name = os.path.basename(folder_path)
    
    # For each subfolders
    subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]
    for subfolder in subfolders:

        # get the description.json file in it
        description_filepath = os.path.join(subfolder, 'description.json')
        if os.path.exists(description_filepath):
            with open(description_filepath, 'r') as f:
                data = json.load(f)
                description = convert_file(data, package_description)

            if description is not None:
                new_filepath = os.path.join(subfolder, f"{description['item_name']}.json")
                #if description_filepath != new_filepath:
                    # delete file
                #    os.remove(description_filepath)

                with open(new_filepath, 'w') as f:
                    json.dump(description, f, indent=4)
    
    # Convert the description.json to v1.0.0. Must be done last.
    new_description_filepath = os.path.join(folder_path, f"{folder_name}.json")
    new_package_description = _convert_package_to_v100(package_description)

    with open(new_description_filepath, 'w') as f:
        json.dump(new_package_description, f, indent=4)

def convert_beta_to_v100(self):
    filepath = QtWidgets.QFileDialog.getOpenFileName(None, "Open tool JSON", "", "Tool JSON (*.json)")[0]
    if not filepath:
        return

    with open(filepath, 'r') as f:
        data = json.load(f)
        description = convert_file(data)

    if description is not None:
        # Get the folder path
        folder_path = os.path.dirname(filepath)
        new_filepath = os.path.join(folder_path, f"{description['item_name']}.json")
        if filepath != new_filepath:
            # delete file
            os.remove(filepath)

        with open(new_filepath, 'w') as f:
            json.dump(description, f, indent=4)

def convert_file(data, package_description):
    if _is_version_module_beta(data):
        module = _convert_module_to_v100(data, package_description["package_name"])
        _modules[module["item_name"]] = module
        return module
    elif _is_version_tool_beta(data):
        tool = _convert_tool_to_v100(data, package_description)
        _tools[tool["item_name"]] = (tool, data["tool_description"])
        return tool
    return None

def _is_version_tool_beta(data):
    if "api_version" not in data and "tool_description" in data:
        return True
    else:
        return False

def _is_version_module_beta(data):
    if "api_version" not in data and "module_name" in data:
        return True
    else:
        return False
    
def _convert_package_to_v100(data):
    new_data = {   
        "package_name": data["package_name"],
        "package_version": data["package_version"],
        "package_author": data["package_author"],
        "package_url": data["package_url"],
        "package_description": data["package_description"],
        "package_api_version": "1.0.0",
        "items":[]
    }

    if "package_modules" in data:
        for package_module in data["package_modules"]:
            item = {
                "item_name":package_module["module_name"],
                "item_type": "module",
                "item_version": package_module["module_version"],
                "item_hooks": [{
                        "endpoint_name": "module_endpoint", 
                        "parameters": {
                            "module_category":_modules[package_module["module_name"]]["module_params"]["module_category"],
                            "module_label":_modules[package_module["module_name"]]["module_params"]["module_label"]
                        }
                    }]
            }   
            new_data["items"].append(item)

    if "package_tools" in data:
        for package_tool in data["package_tools"]:
            item = {
                "item_name":package_tool["tool_name"],
                "item_type": "tool",
                "item_version": _tools[package_tool["tool_name"]][1]["tool_version"],
                "item_hooks": [{
                        "endpoint_name": "menu_endpoint", 
                        "parameters": {
                            "menu_category":_tools[package_tool["tool_name"]][1]["tool_category"],
                            "menu_label":_tools[package_tool["tool_name"]][0]["tool_params"]["tool_label"]
                        }
                    }]
            }   
            new_data["items"].append(item) 
        
    return new_data

def _convert_module_to_v100(data, package_name):
    new_data = {   
        "item_name": data["module_name"],
        "item_type": "module",
        "item_api_version": "1.0.0",
        "item_url":data["module_url"],
        "item_author":data["module_author"],
        "item_description":data["module_description"],
        "dependencies": [],
        "module_params":_convert_module_params_to_v100(data, package_name)
    }
    return new_data

def _convert_module_params_to_v100(data, package_name):
    module_params = {
        "cls": data["module_name"],
        "name": data["module_name"],
        "metadata":{},
        "file_location":"",
        "module_label":data["module_label"],
        "module_category":data["module_category"],
        "module_options": copy.deepcopy(data["module_options"]),
        "inputs": copy.deepcopy(data["module_inputs"]),
        "outputs": copy.deepcopy(data["module_outputs"]),
        "module": f"{package_name}.{data['module_name']}"
    }
    if "identifier" in data:
        module_params["identifier"] = copy.deepcopy(data["identifier"])
        module_params["pos_x"] = data["pos_x"]
        module_params["pos_y"] = data["pos_y"]
        module_params["activation_state"] = data["activation_state"]
        module_params["package"] = copy.deepcopy(data["package"])

    return module_params
    
def _convert_tool_to_v100(data, package_description):
    new_data = {
        "item_name": data["tool_description"]["tool_name"],
        "item_type": "tool",
        "item_api_version": "1.0.0",
        "item_url":data["tool_description"]["tool_url"],
        "item_author":data["tool_description"]["tool_author"],
        "item_description":data["tool_description"]["tool_description"],
        "tool_params": {
            "tool_label": data["tool_description"]["tool_label"],
            "tool_category": data["tool_description"]["tool_category"],
            "asset_directory": data["asset_directory"] if "asset_directory" in data else "",
            "package_name": data["tool_description"]["package_name"],
            "steps":copy.deepcopy(data["steps_description"]),
        },
        "dependencies": copy.deepcopy(data["dependencies"]),
        "process_params": {
            "subgraph_params": {},
            "nodes": [
            ]
        }
    }

    new_data["dependencies"].append({
        "package_name": package_description["package_name"],
        "package_version": package_description["package_version"]
    })

    for node in data["nodes"]:
        new_data["process_params"]["nodes"].append(_convert_module_params_to_v100(node, node["package"]["package_name"]))
    return new_data
