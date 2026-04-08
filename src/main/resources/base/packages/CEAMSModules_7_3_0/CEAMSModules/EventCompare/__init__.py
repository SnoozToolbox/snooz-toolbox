"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .EventCompare import EventCompare
from .EventCompareSettingsView import EventCompareSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .EventCompareResultsView import EventCompareResultsView
    from .Ui_EventCompareResultsView import Ui_EventCompareResultsView
    from .Ui_EventCompareSettingsView import Ui_EventCompareSettingsView
else:
    # Create stub classes for headless mode
    EventCompareResultsView = None
    Ui_EventCompareResultsView = None
    Ui_EventCompareSettingsView = None
