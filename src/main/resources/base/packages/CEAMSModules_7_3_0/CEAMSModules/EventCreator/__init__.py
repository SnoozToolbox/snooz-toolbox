"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .EventCreator import EventCreator
from .EventCreatorSettingsView import EventCreatorSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .EventCreatorResultsView import EventCreatorResultsView
    from .Ui_EventCreatorResultsView import Ui_EventCreatorResultsView
    from .Ui_EventCreatorSettingsView import Ui_EventCreatorSettingsView
else:
    # Create stub classes for headless mode
    EventCreatorResultsView = None
    Ui_EventCreatorResultsView = None
    Ui_EventCreatorSettingsView = None
