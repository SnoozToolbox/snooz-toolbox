"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from .RenameFileList import RenameFileList
from .RenameFileListSettingsView import RenameFileListSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .RenameFileListResultsView import RenameFileListResultsView
    from .Ui_RenameFileListResultsView import Ui_RenameFileListResultsView
    from .Ui_RenameFileListSettingsView import Ui_RenameFileListSettingsView
else:
    # Create stub classes for headless mode
    RenameFileListResultsView = None
    Ui_RenameFileListResultsView = None
    Ui_RenameFileListSettingsView = None
