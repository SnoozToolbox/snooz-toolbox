"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    DetectorAnnotSel
    Step in the CompareEventsFromPSG tool to select annotations from the detector.
    Doc to open and read to understand : 
        Model and item : QAbstractItemModel -> QStandardItemModel -> QStandardItem
        View : QAbstractItemView -> QTreeView
"""
from CEAMSTools.CompareEventsFromPSG.ExpertAnnotSel.ExpertAnnotSel import ExpertAnnotSel

class DetectorAnnotSel( ExpertAnnotSel):

    annotation_type = 'detector'
    node_id_Dictionary_group = "039503fc-2f2c-4c6f-a379-4dfc72211dec" # select the list of group for the current filename
    node_id_Dictionary_name = "fee1a35b-9990-4332-86a7-7528e038c706" # select the list of name for the current filename

    """
        DetectorAnnotSel
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform the filter events (the dictionary before the filter event) which events have been selected bu the user.
    """
    # For the other functions see CEAMSTools.CompareEventsFromPSG.ExpertAnnotSel.ExpertAnnotSel
