"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .DefineEventGroup import DefineEventGroup
from .DefineEventGroupSettingsView import DefineEventGroupSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .DefineEventGroupResultsView import DefineEventGroupResultsView
    from .Ui_DefineEventGroupResultsView import Ui_DefineEventGroupResultsView
    from .Ui_DefineEventGroupSettingsView import Ui_DefineEventGroupSettingsView
else:
    # Create stub classes for headless mode
    DefineEventGroupResultsView = None
    Ui_DefineEventGroupResultsView = None
    Ui_DefineEventGroupSettingsView = None
