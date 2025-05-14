"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    SleepStagesImporter
    Class to import sleep stages from a textfile into the sleep_stages dataframe.
"""
import numpy as np
import os
import pandas as pd
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = False
EPOCH_LENGTH_SEC = 30

class SleepStagesImporter(SciNode):
    """
    Class to import sleep stages from a textfile into the sleep_stages dataframe.

    Parameters
    ----------
        filename : string
            The name of the current PSG file.
        sleep_stages : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
            Original sleep stages list from the PSG file.
        stages_files: list
            List of path and filename of files with sleep stages to read
        file_params : dict
            Parameters of the files to read
                sep : separator of the textfile
                n_rows_hdr : number of rows to skip in the header
                encoding : encoding of the textfile (i.e. utf-8)
                column_stages : column of the textfile containing the sleep stages
                stages_sec : duration of the sleep stage in seconds in the textfile to read
                prefix_filename : prefix to insert before the filename to create the stage filename
                suffix_filename : suffix to append after the filename to create the stage filename
                case_sensitive : True if the filename\prefix_filename\suffix_filename are case sensitive
                rename_values : dictionary of values to rename
                    '0' : 'Original awake label'
                    '1' : 'Original N1 label'
                    '2' : 'Original N2 label'
                    '3' : 'Original N3 label'
                    '5' : 'Original REM label'
                    '6' : 'Original movement label'
                    '7' : 'Original tech label'
                    '9' : 'Original unscored label'

    Returns
    -------
        sleep_stages: TPandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
            Updated sleep stages list from the textfile.
        
    """
    def __init__(self, **kwargs):
        """ Initialize module SleepStagesImporter """
        super().__init__(**kwargs)
        if DEBUG: print('SleepStagesImporter.__init__')

        # Input plugs
        InputPlug('filename',self)
        InputPlug('sleep_stages',self)
        InputPlug('stages_files',self)
        InputPlug('file_params',self)
        # Output plugs
        OutputPlug('sleep_stages',self)

        # The master module is the PSGReader, when the SleepStagesImporter 
        # module is instantiated in a pipeline.
        self._is_master = False 
    

    def compute(self, filename, sleep_stages, stages_files, file_params):
        """
        Import sleep stages from a textfile into the sleep_stages dataframe.

        Parameters
        ----------        
            filename : string
                The name of the current PSG file.
            sleep_stages : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
                Original sleep stages list from the PSG file.
            stages_files: list
                List of path and filename of files with sleep stages to read
            file_params : dict
                Parameters of the files to read
                    sep : separator of the textfile
                    n_rows_hdr : number of rows to skip in the header
                    encoding : encoding of the textfile (i.e. utf-8)
                    column_stages : column of the textfile containing the sleep stages
                    stages_sec : duration of the sleep stage in seconds in the textfile to read
                    prefix_filename : prefix to insert before the filename to create the stage filename
                    suffix_filename : suffix to append after the filename to create the stage filename
                    case_sensitive : True if the filename\prefix_filename\suffix_filename are case sensitive
                    rename_values : dictionary of values to rename
                        '0' : 'Original awake label'
                        '1' : 'Original N1 label'
                        '2' : 'Original N2 label'
                        '3' : 'Original N3 label'
                        '5' : 'Original REM label'
                        '6' : 'Original movement label'
                        '7' : 'Original tech label'
                        '9' : 'Original unscored label'

        Returns
        -------
            sleep_stages: TPandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
                Updated sleep stages list from the textfile.

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if len(filename) == 0:
            raise NodeInputException(self.identifier, "filename", \
                f"SleepStagesImporter the filename parameter must be set.")
        if not isinstance(sleep_stages, pd.DataFrame):
            raise NodeInputException(self.identifier, "sleep_stages", \
                f"SleepStagesImporter the expected type is DataFrame and received {type(sleep_stages)}.")

        if isinstance(stages_files, str) and len(stages_files)==0:
            raise NodeInputException(self.identifier, "stages_files", \
                f"SleepStagesImporter the stages_files parameter must be set.")
        elif isinstance(stages_files, str):
            stages_files = eval(stages_files)
        if not isinstance(stages_files, list):
            raise NodeInputException(self.identifier, "stages_files", \
                f"SleepStagesImporter the expected type is list and received {type(stages_files)}.")
        if len(stages_files) == 0:
            raise NodeInputException(self.identifier, "stages_files", \
                f"SleepStagesImporter the stages_files parameter must contain at least one file.")

        if isinstance(file_params, str) and not len(file_params)==0:
            file_params = eval(file_params)
        if not isinstance(file_params, dict):
            raise NodeInputException(self.identifier, "file_params", \
                f"SleepStagesImporter the expected type is dict and received {type(file_params)}.")

        # Look in the stages_files list for the filename
        stages_read_val = None
        for i in range(0, len(stages_files)):
            # Extract the path and the filename of the current stage file
            stage_file_name = os.path.basename(stages_files[i])
            # Remove the extension from the current stage file
            stage_file_name = stage_file_name.split('.')[0]
            # Extract the file name of the current PSG filename
            PSG_file_name = os.path.basename(filename)
            # Remove the extension from the PSG_file_name
            PSG_file_name = PSG_file_name.split('.')[0]
            # Created stages file name
            created_stages_file = file_params['prefix_filename'] + PSG_file_name + file_params['suffix_filename']
            if file_params['case_sensitive']:
                valid_stages_file = (created_stages_file == stage_file_name)
            else:
                valid_stages_file = (created_stages_file.lower() == stage_file_name.lower())
            if valid_stages_file:
                stage_file_read = stages_files[i]
                # Read the current stage file
                try: 
                    current_stage_file = pd.read_csv(stage_file_read, engine='python', \
                    sep=file_params['sep'], encoding=file_params['encoding'], skiprows=file_params['n_rows_hdr'])
                except:
                    raise NodeRuntimeException(self.identifier, "stages_files", \
                        f"SleepStagesImporter : The sleep stages file {stage_file_read} could not be read.")
                # Extract sleep stage values
                if len(current_stage_file.shape)>1:
                    current_stage_file = current_stage_file.iloc[:,file_params['column_stages']-1]
                else:
                    current_stage_file = current_stage_file
                # Convert the sleep stage column to string
                current_stage_file = current_stage_file.astype(str)
                # Extract sleep stage values
                stages_read_val = current_stage_file.values
                break # When the sleep stage file is found, stop the loop
        
        if stages_read_val is None:
            # Raise the runtime exception if the sleep stage file is not found
            raise NodeRuntimeException(self.identifier, "stages_files", \
                f"SleepStagesImporter : The sleep stages files is not found for the PSG filename {filename}.")

        # Skip rows not aligned with 30 seconds
        # compute the number of rows to skip
        n_rows_to_increment = int(round(EPOCH_LENGTH_SEC/file_params['stages_sec']))
        stages_read_val = stages_read_val[0:len(stages_read_val):n_rows_to_increment]

        # Make sure the array has the correct dimensions
        renamed_stages_read_val = []
        if len(stages_read_val) <= len(sleep_stages):

            # Make sure all the values are included in the file_params[rename_values] dictionary
            unique_values = np.unique(stages_read_val)
            missing_values =[]
            for j in range(0, len(unique_values)):
                if unique_values[j] not in list(file_params['rename_values'].values()):
                    missing_values.append(unique_values[j])
            if len(missing_values)>0:
                raise NodeRuntimeException(self.identifier, "stages_files", \
                    f"SleepStagesImporter : The sleep stages renaming failed for the PSG filename {filename}. Missing values : {missing_values}.")

            # Rename the values of the stages_read_val based on the file_params[rename_values] dictionary
            for i in range(0, len(stages_read_val)):
                # Replace the sleep stage value with the key in the file_params[rename_values] dictionary
                #   The original label is the value of the file_params[rename_values] dictionary
                #   The new label is the key of the file_params[rename_values] dictionary
                #   find the key with the value == stages_read_val[i][0]
                try :
                    renamed_stages_read_val.append(list(file_params['rename_values'].keys())\
                    [list(file_params['rename_values'].values()).index(stages_read_val[i])])
                except :
                    raise NodeRuntimeException(self.identifier, "stages_files", \
                        f"SleepStagesImporter : The sleep stages renaming failed for the PSG filename {filename}. Look in the text file for the original labels.")

            # Replace the sleep stage values in the sleep_stages dataframe
            sleep_stages.iloc[:len(renamed_stages_read_val),1] = np.array(renamed_stages_read_val)
        else:
            # Raise the runtime exception if the sleep stage file is not found
            raise NodeRuntimeException(self.identifier, "stages_files", \
                f"SleepStagesImporter : The sleep stages file includes more sleep stages than the length of the PSG filename {filename}.")            


        # Write to the cache to use the data in the resultTab
        cache = {}
        cache['events'] = sleep_stages
        self._cache_manager.write_mem_cache(self.identifier, cache)

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, f"{stage_file_read} is imported.")

        return {
            'sleep_stages': sleep_stages
        }