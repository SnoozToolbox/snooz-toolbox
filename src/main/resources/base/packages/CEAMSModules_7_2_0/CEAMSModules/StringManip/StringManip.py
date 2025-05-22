"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    This plugin allows string manipulaiton.

    Parameters
    -----------
        input         : String 
            Input string to manipulate
        prefix         : String
            String added at the beginnig of the input string.
        suffix        : String
            String added to the end of the input string.
        filename_rm   : bool
            True to remove the filename after the path from the input string. 
        path_rm       : bool
            True to remove the path from the input string. 
            Remove any chars before the last \ (including the last \).     
        file_ext_rm   : bool
            True to remove the file ext (ex .edf) from the input string.

    Returns
    -----------    
        output   : String
            Output string manipulated
"""

from scipy import signal

from flowpipe import SciNode, InputPlug, OutputPlug
import os

DEBUG = False

class StringManip(SciNode):
    """
        String manipulaiton.

        Parameters
        -----------
            input         : String 
                Input string to manipulate
            prefix         : String
                String added at the beginnig of the input string.
            suffix        : String
                String added to the end of the input string.
            filename_rm   : String of int
                '1' to remove the filename after the path from the input string.                 
            path_rm       : String of int
                '1' to remove the path from the input string. 
                Remove any chars before the last \ (including the last \). 
            file_ext_rm    : String of int
                '1' to remove the file ext (ex .edf) from the input string.

        Returns
        -----------    
            output   : String
                Output string manipulated
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('StringManip.__init__')
        InputPlug('input', self)
        InputPlug('prefix', self)
        InputPlug('suffix', self)
        InputPlug('filename_rm', self)
        InputPlug('path_rm', self)
        InputPlug('file_ext_rm', self)
        OutputPlug('output', self)


    def subscribe_topics(self):
        pass


    def compute(self, input, prefix, suffix, filename_rm, path_rm, file_ext_rm):
        """
            String manipulaiton.

            Parameters
            -----------
                input         : String 
                    Input string to manipulate
                prefix         : String
                    String added at the beginnig of the input string.
                suffix        : String
                    String added to the end of the input string.
                filename_rm   : String of int
                    '1' to remove the filename after the path from the input string.                 
                path_rm       : String of int
                    '1' to remove the path from the input string. 
                    Remove any chars before the last \ (including the last \). 
                file_ext_rm    : String of int
                    '1' to remove the file ext (ex .edf) from the input string.

            Returns
            -----------    
                output   : String
                    Output string manipulated
        """
        if DEBUG: print('StringManip.compute')
        folder, filename = os.path.split(input)
        filename, file_extension = os.path.splitext(filename)
        if int(filename_rm):
            filename = ''
        # Remove the file path
        if int(path_rm):
            folder = ''
        # Remove the file ext
        if int(file_ext_rm):
            file_extension = ''
        # Add prefix
        if len(prefix):
            # Verify if the user add a sub folder
            prefix_folder, prefix_filename = os.path.split(prefix)
            if len(prefix_folder)>1:
                folder = folder + prefix_folder
                filename = prefix_filename + filename
            else:
                filename = prefix + filename
        # Add suffix
        if len(suffix):
            filename = filename + suffix
        # Add the extension
        filename = filename + file_extension
        # Create the complete path
        output = os.path.join(folder, filename)
        # Log message for the Logs tab
        self._log_manager.log(self.identifier, f"{output} in process...")        
        
        return {
            'output': output
        }
