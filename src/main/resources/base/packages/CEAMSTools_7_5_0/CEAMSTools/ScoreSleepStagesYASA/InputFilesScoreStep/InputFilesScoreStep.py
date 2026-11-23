"""
@ Valorisation Recherche HSCM, Société en Commandite – 2025
See the file LICENCE for full license details.
"""

"""
    This step is used to select the files to score the sleep stages.
"""

from qtpy import QtWidgets, QtCore
from qtpy.QtCore import QTimer

from CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep import InputFilesStep

from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog


class InputFilesScoreStep( InputFilesStep):

    # Overwrite the default values of the base class 
    # (really important to keep :
    #   context_files_view      = "input_files_settings_view")
    psg_reader_identifier = "031201d5-ff93-4be6-90d3-256d2ba689d1"
    valid_stage_mandatory = False    # To verify that all recordings have valid sleep stages
    valid_selected_chan   = True    # To verify if at least one channel is selected
    valid_single_chan     = False   # To verify if only one chan is selected for each file

    """
        InputFileStep
        This step is used to select the files to score the sleep stages.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Note: setupUi is already called in parent __init__, 
        # but we need to call it again for this specific UI
        # self.setupUi(self)  # Uncomment if this class has its own UI file
    
    # Get the alias values from PSGReaderSettingsView
    def get_aliases(self):
        """
        Get the alias values configured in the PSGReaderSettingsView.
        
        Returns
        -------
        dict
            Dictionary with alias names as keys and lists of channel names as values.
            Example: {'EOG': ['LOC-A2', 'ROC-A1'], 'EMG': ['Chin1-Chin2']}
        """
        if hasattr(self, 'my_PsgReaderSettingsView') and self.my_PsgReaderSettingsView is not None:
            return self.my_PsgReaderSettingsView.get_alias()
        else:
            return {}


    # Get channels for a specific alias
    def get_alias_channels(self, alias_name):
        """
        Get the list of channels for a specific alias.
        
        Parameters
        ----------
        alias_name : str
            Name of the alias (e.g., 'EOG', 'EMG', 'EEG')
            
        Returns
        -------
        list
            List of channel names for the specified alias, empty list if not found
        """
        aliases = self.get_aliases()
        return aliases.get(alias_name, [])
    

    def on_validate_settings(self):
        if ((self.valid_selected_chan or self.valid_stage_mandatory) or self.valid_single_chan ):
            file_list = self.my_PsgReaderSettingsView.get_files_list(self.my_PsgReaderSettingsView.files_model)

        # If the file list is empty -> open a warning dialog
        # If none of the channels is selected for a subject -> open a warning dialog
                            # Check alias configurations for EOG, EMG, and EEG
        all_aliases = self.get_aliases()
        eog_alias_channels = self.get_alias_channels('EOG')
        emg_alias_channels = self.get_alias_channels('EMG')
        eeg_alias_channels = self.get_alias_channels('EEG')
        if not (eog_alias_channels or emg_alias_channels or eeg_alias_channels):
            WarningDialog(f"Configure the aliases corresponding to the selected channels: EOG, EMG, and EEG.")
            return False
        if self.valid_selected_chan:
            channels_info_df = self.my_PsgReaderSettingsView.channels_table_model.get_data()
            # For each subject
            if len(file_list)>0:
                for file in file_list:
                    EEG_alias_counter = 0
                    EOG_alias_counter = 0
                    EMG_alias_counter = 0
                    All_alias_counter = 0
                    chans_used = channels_info_df[(channels_info_df['Filename']==file) & (channels_info_df['Use']==True)]
                    if list(chans_used['Channel']):
                        for chan in list(chans_used['Channel']):
                            if chan in eeg_alias_channels:
                                EEG_alias_counter += 1
                            if chan in eog_alias_channels:
                                EOG_alias_counter += 1
                            if chan in emg_alias_channels:
                                EMG_alias_counter += 1
                    else:
                        WarningDialog(f"At least one recording has no channel selected, start looking at {file} in step '1 - Input Files'.")
                        return False
                    All_alias_counter = EEG_alias_counter + EOG_alias_counter + EMG_alias_counter
                    if All_alias_counter != len(list(chans_used['Channel'])):
                        WarningDialog(f"At least one recording has a missing alias corresponding to the selected channels, start looking at {file} in step '1 - Input Files'.")
                        return False
                    # Check if EEG alias is missing
                    if EEG_alias_counter == 0:
                        WarningDialog(f"EEG channel is not selected or EEG alias is not configured. Please add the missing EEG alias or channel for proper functioning of the algorithm, start looking at {file} in step '1 - Input Files'.")
                        return False
                    
                    if EEG_alias_counter > 4:
                        WarningDialog(f"EEG channels are exceeding the maximum number of EEG channels allowed for this tool. "
                                    f"Consider using up to four EEG channels for proper functioning of the algorithm, start looking at {file} in step '1 - Input Files'.")
                        return False
                    # Check if EOG has more than one channel
                    if EOG_alias_counter > 1:
                        WarningDialog(f"EOG channels are exceeding the maximum number of EOG channels allowed for this tool. "
                                    f"Consider using only one EOG channel for proper functioning of the algorithm, start looking at {file} in step '1 - Input Files'.")
                        return False
                    
                    # Check if EMG has more than one channel  
                    if EMG_alias_counter > 1:
                        WarningDialog(f"EMG channels are exceeding the maximum number of EMG channels allowed for this tool. "
                                    f"Consider using only one EMG channel for proper functioning of the algorithm, start looking at {file} in step '1 - Input Files'.")
                        return False
            else:
                WarningDialog(f"Add files in step '1 - Input Files'.")    
                return False
        
        # Note: EEG can have multiple channels, so no check for multiple EEG channels
        
        # If alias validation passes, continue with parent validation
        return super().on_validate_settings()