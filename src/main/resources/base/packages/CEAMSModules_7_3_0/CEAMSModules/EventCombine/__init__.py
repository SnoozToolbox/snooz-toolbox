"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .EventCombine import EventCombine
from .EventCombineSettingsView import EventCombineSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .EventCombineResultsView import EventCombineResultsView
    from .Ui_EventCombineSettingsView import Ui_EventCombineSettingsView
else:
    # Create stub classes for headless mode
    EventCombineResultsView = None
    Ui_EventCombineSettingsView = None
