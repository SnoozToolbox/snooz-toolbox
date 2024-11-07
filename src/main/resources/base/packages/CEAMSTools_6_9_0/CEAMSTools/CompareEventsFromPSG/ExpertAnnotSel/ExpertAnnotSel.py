"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    ExpertAnnotSel
    Step in the CompareEventsFromPSG tool to select annotations for the gold standard.
    This step is really similar to NonValidEventStep in the PowerSpectralAnalysis tool
    but we need to validate that at least one annotation is selected.
    So, we inherit from NonValidEventStep and add the function validate the annotation selection.
        Doc to open and read to understand : 
        Model and item : QAbstractItemModel -> QStandardItemModel -> QStandardItem
        View : QAbstractItemView -> QTreeView
"""

from widgets.WarningDialog import WarningDialog
from CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep import NonValidEventStep

class ExpertAnnotSel( NonValidEventStep ):

    node_id_ResetSignalArtefact_0 = None
    annotation_type = 'expert'
    node_id_Dictionary_group = "f56c85a8-529b-44f5-9a23-c4be67fc8742" # select the list of group for the current filename
    node_id_Dictionary_name = "c98b07ef-a32d-44e5-9ca0-72bb271c108d" # select the list of name for the current filename


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if len(self.group_dict)==0 or len(self.name_dict)==0:
            WarningDialog("Add files in step '1-PSG Input Files'")
            return False              
        else:
            for file, group_lst in self.group_dict.items():
                if group_lst=='None':
                    WarningDialog(f"File {file} has no {self.annotation_type} annotation selected'")
                    return False                  
            for file, name_lst in self.name_dict.items():
                if name_lst=='None':
                    WarningDialog(f"File {file} has no {self.annotation_type} annotation selected'")
                    return False     
        return True