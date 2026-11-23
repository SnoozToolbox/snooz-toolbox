"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    JsonPathEditorMaster
    This module is designed to edit JSON files by replacing paths within the JSON structure.
    It takes a list of JSON files, a mapping of old paths to new paths, and saves the modified JSON files to a specified directory.
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

import os
import json
import re
import ast

DEBUG = False

class JsonPathEditorMaster(SciNode):
    """
    This module is designed to edit JSON files by replacing paths within the JSON structure.
    It takes a list of JSON files, a mapping of old paths to new paths, and saves the modified JSON files to a specified directory.

    Parameters
    ----------
        files: input json files
        path_mapping: a dictionary mapping old paths to new paths
        newfilespath: the directory where the modified JSON files will be saved
        suffix: a suffix to be added to the modified JSON file names
        

    Returns
    -------
        newfiles: the modified JSON files saved in the specified directory (It is not used in the current implementation)
        
    """
    def __init__(self, **kwargs):
        """ Initialize module JsonPathEditorMaster """
        super().__init__(**kwargs)
        if DEBUG: print('JsonPathEditorMaster.__init__')

         # The iteration over a list of files is not complete yet
        self.is_done = False
        # Allow iteration over a list of files
        self.is_master = True
        # Input plugs
        InputPlug('files',self)
        InputPlug('path_mapping',self)
        InputPlug('newfilespath',self)
        InputPlug('suffix',self)
        

        # Output plugs
        OutputPlug('newfiles',self)
        
    
    def compute(self, files, path_mapping, newfilespath, suffix):
        """
        This module is designed to edit JSON files by replacing paths within the JSON structure.
        It takes a list of JSON files, a mapping of old paths to new paths, and saves the modified JSON files to a specified directory.

        Parameters
        ----------
            files: input json files
            path_mapping: a dictionary mapping old paths to new paths
            newfilespath: the directory where the modified JSON files will be saved
            suffix: a suffix to be added to the modified JSON file names
            

        Returns
        -------
            newfiles: the modified JSON files saved in the specified directory (It is not used in the current implementation)
            
        Raises (To be added)
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        if DEBUG: print('JsonPathEditorMaster.compute')
        # Check if the input parameters are valid
        self.clear_cache() # It  makes the cache=None  

        if files == '' or files is None or len(files) == 0:
            raise NodeInputException(self.identifier, "files", \
                "Json path editor input files parameter must be set.")
    
        filename = files[self._iteration_counter]
        # Set the iteration_identifier in case there is a problem during the process.
        # This will be used to identify the problematic file.
        self.iteration_identifier = filename

        if self._iteration_counter + 1 >= len(files):
            self.is_done = True

        if filename is not None:
            '''if not isinstance(files, list) or not all(isinstance(f, str) for f in files):
                raise NodeInputException("Invalid input: 'files' must be a list of strings.")
            if not isinstance(newpaths, list) or not all(isinstance(p, str) for p in newpaths):
                raise NodeInputException("Invalid input: 'newpaths' must be a list of strings.")
            if not isinstance(newfilespath, str):
                raise NodeInputException("Invalid input: 'newfilespath' must be a string.")'''

            self.update_json_paths_interactive(filename, path_mapping, suffix, newfilespath)

            # Log message for the Logs tab
        self._log_manager.log(self.identifier, "This module changes the paths to the desired path inside a Json file.")

        return {
            'newfiles': None
        }

    def replace_paths_in_json(self, data, path_mapping):
        """
        Recursively replace folder paths in JSON structure, including inside stringified lists/dicts.
        Preserves formatting (i.e., stringified structures stay strings).
        Also replaces direct folder matches (not only their contents).
        """
        if isinstance(data, dict):
            return {
                self.replace_paths_in_json(k, path_mapping): self.replace_paths_in_json(v, path_mapping)
                for k, v in data.items()
            }

        elif isinstance(data, list):
            return [self.replace_paths_in_json(item, path_mapping) for item in data]

        elif isinstance(data, str):
            normalized = data.replace('\\', '/')

            # Step 1: Try parsing stringified list/dict
            try:
                parsed = ast.literal_eval(normalized)
                if isinstance(parsed, (list, dict)):
                    replaced = self.replace_paths_in_json(parsed, path_mapping)
                    return str(replaced)
            except (ValueError, SyntaxError):
                pass  # Not a stringified structure

            # Step 2: Check direct full-folder path replacement
            for old_folder, new_folder in path_mapping.items():
                old_folder_norm = old_folder.replace('\\', '/')
                if normalized == old_folder_norm:
                    return new_folder.replace('\\', '/')

            # Step 3: Try replacing parent folder of the file
            folder_path = os.path.dirname(normalized)
            for old_folder, new_folder in path_mapping.items():
                old_folder_norm = old_folder.replace('\\', '/')
                if folder_path == old_folder_norm:
                    filename = os.path.basename(normalized)
                    return os.path.join(new_folder, filename).replace('\\', '/')

            return data  # No match

        else:
            return data


    def update_json_paths_interactive(self, input_json_path, path_mapping, suffix, newfilespath):
        # Load original JSON
        with open(input_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Replace paths
        file_path_mapping = path_mapping[input_json_path]
        updated_data = self.replace_paths_in_json(data, file_path_mapping)

        # Save to output
        output_json_path = os.path.join(newfilespath, os.path.basename(input_json_path).replace('.json', f'_{suffix}.json'))
        # Check if the output directory exists, if not create it
        with open(output_json_path, 'w', encoding='utf-8') as f:
            json.dump(updated_data, f, indent=4)

        #print(f"\nUpdated JSON saved to: {os.path.abspath(output_json_path)}")