"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
from .ExtendEvents import ExtendEvents
from .ExtendEventsSettingsView import ExtendEventsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .ExtendEventsResultsView import ExtendEventsResultsView
    from .Ui_ExtendEventsResultsView import Ui_ExtendEventsResultsView
    from .Ui_ExtendEventsSettingsView import Ui_ExtendEventsSettingsView
else:
    # Create stub classes for headless mode
    ExtendEventsResultsView = None
    Ui_ExtendEventsResultsView = None
    Ui_ExtendEventsSettingsView = None
