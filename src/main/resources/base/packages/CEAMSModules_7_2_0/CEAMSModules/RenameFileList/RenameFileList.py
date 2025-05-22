"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    RenameFileList
    Renames files based on intput parameters such as prefix, suffix, pattern to remove, number of characters to keep.
"""
import os
import shutil

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = False

class RenameFileList(SciNode):
    """
    Renames files based on intput parameters such as prefix, suffix, pattern to remove, number of characters to keep.

    Parameters
    ----------
        file_list: List of strings
            List of file names to potentially rename
        prefix: string
            String added at the beginnig of the file name
        suffix: String
            String added to the end of the file name
        n_char_to_keep: int
            Number of characters to keep
        pattern_to_rem: string
            Pattern to remove from the original file name
        ext_selection: string
            Extension to select the file to rename
        keep_original_file : int
            1 to keep the original file name, else to rename

    Returns
    -------
        ren_file_list: List of strings
            List of renamed file names
        
    """
    def __init__(self, **kwargs):
        """ Initialize module RenameFileList """
        super().__init__(**kwargs)
        if DEBUG: print('RenameFileList.__init__')

        # Input plugs
        InputPlug('file_list',self)
        InputPlug('prefix',self)
        InputPlug('suffix',self)
        InputPlug('n_char_to_keep',self)
        InputPlug('pattern_to_rem',self)
        InputPlug('ext_selection',self)
        InputPlug('keep_original_file',self)
        
        # Output plugs
        OutputPlug('ren_file_list',self)

        self._is_master = False 
    

    def compute(self, file_list,prefix,suffix,n_char_to_keep,pattern_to_rem,ext_selection,keep_original_file):
        """
        Renames files based on intput parameters such as prefix, suffix, pattern to remove, number of characters to keep.

        Parameters
        ----------
            file_list: List of strings
                List of file names to potentially rename
            prefix: string
                String added at the beginnig of the file name
            suffix: String
                String added to the end of the file name
            n_char_to_keep: int
                Number of characters to keep
            pattern_to_rem: string
                Pattern to remove from the original file name
            ext_selection: string
                Extension to select the file to rename
            keep_original_file : int
                1 to keep the original file name, else to rename

        Returns
        -------
            ren_file_list: List of strings
                List of renamed file names

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if isinstance(file_list, str) and not file_list=='':
            file_list = eval(file_list)
        if not isinstance(file_list, list):
            raise NodeInputException(self.identifier, "file_list", \
                f"RenameFileList input of wrong type. Expected: <class 'list'> received: {type(file_list)}")

        if isinstance(n_char_to_keep, str) and not n_char_to_keep=='':
            n_char_to_keep = eval(n_char_to_keep)
        if not isinstance(n_char_to_keep, int):
            raise NodeInputException(self.identifier, "n_char_to_keep", \
                f"RenameFileList input of wrong type. Expected: <class 'int'> received: {type(n_char_to_keep)}")

        if isinstance(keep_original_file, str) and not keep_original_file=='':
            keep_original_file = eval(keep_original_file)
        if not isinstance(keep_original_file, int):
            raise NodeInputException(self.identifier, "keep_original_file", \
                f"RenameFileList input of wrong type. Expected: <class 'int'> received: {type(keep_original_file)}")

        # Loop in the list of files and rename them
        ori_file_list_to_ren = []
        ren_file_list = []
        for file in file_list:
            # Select the file to rename based on the extension if any was defined
            if (len(ext_selection)>0 and file.endswith(ext_selection)) or ext_selection=='':
                # Separate the file path, name and extension
                folder, filename = os.path.split(file)
                filename_no_ext, file_ext = os.path.splitext(filename)
                # Remove pattern from the file name
                if pattern_to_rem != '':
                    filename_no_ext = filename_no_ext.replace(pattern_to_rem,'')
                # Keep only n_char_to_keep characters
                if n_char_to_keep > 0:
                    filename_no_ext = filename_no_ext[0:n_char_to_keep]
                # Add prefix if any
                if prefix != '':
                    filename_no_ext = prefix + filename_no_ext
                # Add suffix if any
                if suffix != '':
                    filename_no_ext = filename_no_ext + suffix

                # Add the new file name to the list
                ori_file_list_to_ren.append(folder+'/'+filename)
                ren_file_list.append(folder+'/'+filename_no_ext+file_ext)

        # For each file in ori_file_list_to_ren check if it exists
        for file in ori_file_list_to_ren:
            if not os.path.exists(file):
                raise NodeRuntimeException(self.identifier, "file_list", \
                    f"The file {file} does not exist.")
            else:
                if keep_original_file:
                    try:
                        # Copy the original file to the new name
                        shutil.copy(file, ren_file_list[ori_file_list_to_ren.index(file)])
                        # Log message for the Logs tab
                        self._log_manager.log(self.identifier, f"{file} copied to {ren_file_list[ori_file_list_to_ren.index(file)]}.")
                    except Exception:
                        raise NodeRuntimeException(self.identifier, "file_list", \
                            f"The file {file} could not be copied to {ren_file_list[ori_file_list_to_ren.index(file)]}.")
                else:
                    try:
                        # Rename the file
                        os.rename(file, ren_file_list[ori_file_list_to_ren.index(file)])
                        # Log message for the Logs tab
                        self._log_manager.log(self.identifier, f"{file} renamed to {ren_file_list[ori_file_list_to_ren.index(file)]}.")
                    except Exception:
                        raise NodeRuntimeException(self.identifier, "file_list", \
                            f"The file {file} could not be renamed to {ren_file_list[ori_file_list_to_ren.index(file)]}. Check if it already exists.")                    

        # Write to the cache to use the data in the resultTab
        cache = {}
        cache['ren_file_list'] = ren_file_list
        self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'ren_file_list': None
        }