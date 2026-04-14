"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .DropRenameEvents import DropRenameEvents
from .DropRenameEventsSettingsView import DropRenameEventsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .DropRenameEventsResultsView import DropRenameEventsResultsView
    from .Ui_DropRenameEventsSettingsView import Ui_DropRenameEventsSettingsView
else:
    # Create stub classes for headless mode
    DropRenameEventsResultsView = None
    Ui_DropRenameEventsSettingsView = None
