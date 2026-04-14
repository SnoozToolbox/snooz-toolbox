#! /usr/bin/env python3
"""
    InputFiles
    Step to open files to detect spindles.
"""

from qtpy import QtWidgets

from CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep import InputFilesStep
from widgets.WarningDialog import WarningDialog

class InputFilesArtStep( InputFilesStep):

    # Overwrite the default values of the base class 
    # (really important to keep :
    #   context_files_view      = "input_files_settings_view")
    psg_reader_identifier = "64feff16-15d2-4acf-b2e5-195412e476ba"
    valid_stage_mandatory = False   # To verify that all recordings have valid sleep stages
    valid_selected_chan   = True    # To verify if at least one channel is selected
    valid_single_chan     = False   # To verify if only one chan is selected for each file

    """
        InputFileStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform PSGReader of the files to open and propagate the events included in the files.
    """

    # Overwrite the on_validate_settings function of the base class to add specific validation for the artifact detection tool
    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
       
        if ((self.valid_selected_chan or self.valid_stage_mandatory) or self.valid_single_chan ):
            file_list = self.my_PsgReaderSettingsView.get_files_list(self.my_PsgReaderSettingsView.files_model)

        # If the file list is empty -> open a warning dialog
        # If none of the channels is selected for a subject -> open a warning dialog
        if self.valid_selected_chan : 
            channels_info_df = self.my_PsgReaderSettingsView.channels_table_model.get_data()
            # For each subject
            if len(file_list)>0:
                for file in file_list:
                    chans_used = channels_info_df[(channels_info_df['Filename']==file) & (channels_info_df['Use']==True)]
                    if len(chans_used)==0:
                        WarningDialog(f"At least one recording has no channel selected, start looking at {file} in step '1 - Input Files'.")
                        return False
            else:
                WarningDialog(f"Add files in step '1 - Input Files'.")    
                return False

        # If the tool needs that all recordings have valid sleep stages
        # This class is also used in the spindle and SW detection tool
        if self.valid_stage_mandatory :
            # Return False if any of the recordings has no valid sleep staging
            for file in file_list:
                if not self.my_PsgReaderSettingsView.is_stages_scored(file, self.my_PsgReaderSettingsView.files_model):
                    WarningDialog(f"At least one recording has no valid sleep stage, start looking at {file} in the step '1- Input Files'.")
                    return False

        # If the tool needs that all recordings have only one channel
        # This class is also used in the Oxygen Saturation Report tool
        if self.valid_single_chan :
            # Return False if any of the recordings has more than one channel selected
            for file in file_list:
                chans_used = channels_info_df[(channels_info_df['Filename'] == file) & (channels_info_df['Use'] == True)]
                if len(chans_used) > 1:
                    WarningDialog(f"At least one recording has more than one channel selected, start looking at {file} in step '1 - Input Files'.")
                    return False

        # Extract the alias
        alias = self.my_PsgReaderSettingsView.get_alias()
        if len(alias)>0:
            for key, val in alias.items():
                if val==['']:
                    WarningDialog(f"The alias '{key}' from the Input File Step is empty. You must define the {key} channels. If not applicable, set the alias manually to 'NA'.")
                    return False
                
            # If none of the EEG channels is selected for a subject
            # Check if there is a key named EEG in the alias
            if 'EEG' in alias.keys():
                eeg_chan_alias = alias['EEG']
                channels_info_df = self.my_PsgReaderSettingsView.channels_table_model.get_data()
                # For each subject
                file_list = channels_info_df['Filename'].unique()
                for file in file_list:
                    chans_used = channels_info_df[(channels_info_df['Filename']==file) & (channels_info_df['Use']==True) & channels_info_df['Channel'].isin(eeg_chan_alias)]
                    if len(chans_used)==0:
                        WarningDialog(f"At least one recording has no EEG channel (defined in EEG Alias) selected, start looking at {file} in step '1 - Input Files'.")
                        return False 

        return True   

# For the other functions see CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep