"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .SleepStageRename import SleepStageRename
from .SleepStageRenameSettingsView import SleepStageRenameSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .SleepStageRenameResultsView import SleepStageRenameResultsView
    from .Ui_SleepStageRenameResultsView import Ui_SleepStageRenameResultsView
    from .Ui_SleepStageRenameSettingsView import Ui_SleepStageRenameSettingsView
else:
    # Create stub classes for headless mode
    SleepStageRenameResultsView = None
    Ui_SleepStageRenameResultsView = None
    Ui_SleepStageRenameSettingsView = None
