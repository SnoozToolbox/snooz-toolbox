"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
from .CreateListofGroupName import CreateListofGroupName
from .CreateListofGroupNameSettingsView import CreateListofGroupNameSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .CreateListofGroupNameResultsView import CreateListofGroupNameResultsView
    from .Ui_CreateListofGroupNameResultsView import Ui_CreateListofGroupNameResultsView
    from .Ui_CreateListofGroupNameSettingsView import Ui_CreateListofGroupNameSettingsView
else:
    # Create stub classes for headless mode
    CreateListofGroupNameResultsView = None
    Ui_CreateListofGroupNameResultsView = None
    Ui_CreateListofGroupNameSettingsView = None
