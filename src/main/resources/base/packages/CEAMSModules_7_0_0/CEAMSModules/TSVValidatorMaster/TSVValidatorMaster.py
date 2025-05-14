"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    TSVValidatorMaster
    This module validates TSV files by checking their encoding and structure.
    It checks if the files are UTF-8 encoded and if they contain the expected columns and data types.
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import os
import pandas as pd
from CEAMSModules.PSGReader.commons import sleep_stages_name
DEBUG = False

class TSVValidatorMaster(SciNode):
    """
    This module validates TSV files by checking their encoding and structure.
    It checks if the files are UTF-8 encoded and if they contain the expected columns and data types.

    Parameters
    ----------
        files: input TSV files
            A list of TSV files to be validated.
        log_path: the directory where the validation logs will be saved
        

    Returns
    -------
        output_logs: the validation logs in a text file saved in the specified directory
        
    """
    def __init__(self, **kwargs):
        """ Initialize module TSVValidatorMaster """
        super().__init__(**kwargs)
        if DEBUG: print('TSVValidatorMaster.__init__')

         # The iteration over a list of files is not complete yet
        self.is_done = False
        # Allow iteration over a list of files
        self.is_master = True
        # Input plugs
        InputPlug('files',self)
        InputPlug('log_path',self)

        # Output plugs
        OutputPlug('output_logs',self)
        
    
    def compute(self, files, log_path):
        """
   
        This module validates TSV files by checking their encoding and structure.
        It checks if the files are UTF-8 encoded and if they contain the expected columns and data types.

        Parameters
        ----------
            files: input TSV files
                A list of TSV files to be validated.
            log_path: the directory where the validation logs will be saved
            

        Returns
        -------
            output_logs: the validation logs in a text file saved in the specified directory
                

        Raises (To be added)
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        if DEBUG: print('TSVValidatorMaster.compute')
        # Check if the input is valid. This is done by checking the type of the input.
        # If the input is not valid, raise a NodeInputException. This will stop the process
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None    

        if files == '' or files is None or len(files) == 0:
            raise NodeInputException(self.identifier, "files", \
                "TSV Validator input files parameter must be set.")
        
        filename = files[self._iteration_counter]

        # Set the iteration_identifier in case there is a problem during the process.
        # This will be used to identify the problematic file.
        self.iteration_identifier = filename

        if self._iteration_counter + 1 >= len(files):
            self.is_done = True

        if filename is not None:
            errors = []

            # Generate log file path
            base_name = os.path.basename(filename)
            name_without_ext = os.path.splitext(base_name)[0]
            log_file_path = os.path.join(log_path, f"{name_without_ext}_validation_log.txt")

            # Check UTF-8 encoding
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    f.read()
            except UnicodeDecodeError:
                errors.append("File encoding is not UTF-8.")
                with open(log_file_path, 'w', encoding='utf-8') as log_file:
                    for error in errors:
                        log_file.write(error + '\n')
                return False

            # Manual TSV structure check
            expected_columns = ['group', 'name', 'start_sec', 'duration_sec', 'channels']
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    header = lines[0].rstrip('\n').split('\t')
                    expected_col_count = len(expected_columns)

                    if header != expected_columns:
                        errors.append(f"Header mismatch. Expected {expected_columns}, but got {header}")

                    for i, line in enumerate(lines[1:], start=2):  # start=2 for line numbers
                        if line.strip():  # skip blank lines
                            fields = line.rstrip('\n').split('\t')
                            if len(fields) != expected_col_count:
                                errors.append(f"Line {i}: Expected {expected_col_count} columns, but found {len(fields)} → Possible missing value or tab")

            except Exception as e:
                errors.append(f"File could not be read during line check: {str(e)}")

            # Only continue if structure is valid
            if not errors:
                try:
                    df = pd.read_csv(filename, sep='\t', encoding='utf-8', na_values=[''], keep_default_na=False)

                    has_stage_group = False
                    invalid_stage_names = set()
                    uses_stage_4 = False

                    for idx, row in df.iterrows():
                        for col in expected_columns:
                            val = row[col]
                            if pd.isna(val) or (isinstance(val, str) and val.strip() == ''):
                                errors.append(f"Row {idx}: Empty or missing value in column '{col}'")
                                continue
                            
                        if not pd.isna(row['group']) and not isinstance(row['group'], str):
                            errors.append(f"Row {idx}: 'group' should be str, got {type(row['group']).__name__}")
                        if not pd.isna(row['name']) and not isinstance(row['name'], (str, int)):
                            errors.append(f"Row {idx}: 'name' should be int or str, got {type(row['name']).__name__}")
                        if not pd.isna(row['start_sec']) and not isinstance(row['start_sec'], (float, int)):
                            errors.append(f"Row {idx}: 'start_sec' should be float or int, got {type(row['start_sec']).__name__}")
                        if not pd.isna(row['duration_sec']) and not isinstance(row['duration_sec'], (float, int)):
                            errors.append(f"Row {idx}: 'duration_sec' should be float or int, got {type(row['duration_sec']).__name__}")
                        if not pd.isna(row['channels']) and not isinstance(row['channels'], str):
                            errors.append(f"Row {idx}: 'channels' should be str, got {type(row['channels']).__name__}")

                        # Sleep staging validation
                        if row['group'].strip().lower() == 'stage':
                            has_stage_group = True
                            stage_name = str(row['name']).strip()

                            if stage_name == '4' or stage_name == 4:
                                uses_stage_4 = True

                            if stage_name not in sleep_stages_name.values():
                                invalid_stage_names.add(stage_name)

                    if not has_stage_group:
                        errors.append("No 'stage' group found — this recording may lack sleep staging annotations.")

                    if invalid_stage_names:
                        errors.append(f"Invalid stage values found (not in {list(sleep_stages_name.values())}): {sorted(invalid_stage_names)}")

                    if uses_stage_4:
                        errors.append("Detected stage value = 4. Please consider renaming stages using the preprocessing tool → Edit Annotations.")

                except Exception as e:
                    errors.append(f"File could not be read or processed: {str(e)}")

            # Write log file
            with open(log_file_path, 'w', encoding='utf-8') as log_file:
                if errors:
                    log_file.write("Validation failed. Issues found:\n")
                    for idx, error in enumerate(errors):
                        log_file.write(f"{idx+1}: {error}\n")
                else:
                    log_file.write("Validation successful. No issues found.")

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "This module validates the TSV files by checking their encoding and structure.")

        return {
            'output_logs': None
        }