"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    ExpertAnnotSel
    Step in the CompareEventsFromPSG tool to select annotations for the gold standard.
    This step is really similar to NonValidEventStep in the PowerSpectralAnalysis tool
    but we warn when a file has no annotation selected and allow the user to continue.
    So, we inherit from NonValidEventStep and add the function validate the annotation selection.
        Doc to open and read to understand : 
        Model and item : QAbstractItemModel -> QStandardItemModel -> QStandardItem
        View : QAbstractItemView -> QTreeView
"""

from pandas import DataFrame
from qtpy.QtWidgets import QDialog

from widgets.WarningDialog import WarningDialog
from widgets.TableDialog import TableDialog
from CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep import NonValidEventStep

class ExpertAnnotSel( NonValidEventStep ):

    node_id_ResetSignalArtefact_0 = None
    annotation_type = 'expert'
    node_id_Dictionary_group = "f56c85a8-529b-44f5-9a23-c4be67fc8742" # select the list of group for the current filename
    node_id_Dictionary_name = "c98b07ef-a32d-44e5-9ca0-72bb271c108d" # select the list of name for the current filename

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.match_event_channels_checkBox.setChecked(True)

    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # Missing files block execution; missing annotations require confirmation.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if len(self.group_dict)==0 or len(self.name_dict)==0:
            WarningDialog("Add files in step '1-PSG Input Files'")
            return False

        files_without_annotations = dict.fromkeys(
            file
            for annotation_dict in (self.group_dict, self.name_dict)
            for file, annotations in annotation_dict.items()
            if annotations == 'None'
        )
        if files_without_annotations:
            dialog = TableDialog(
                df=DataFrame(list(files_without_annotations), columns=["PSG file"]),
                title="Missing annotations",
                message=(
                    f"{len(files_without_annotations)} file(s) have no "
                    f"{self.annotation_type} annotation selected.\n"
                    "Do you want to continue the analysis anyway?\n"
                    "Click OK to continue or Cancel to review the selection."
                ),
                showConfirmationButtons=True,
            )
            return dialog.exec_() == QDialog.Accepted
        return True