"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .PSAOnEvents import PSAOnEvents
from .PSAOnEventsSettingsView import PSAOnEventsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .PSAOnEventsResultsView import PSAOnEventsResultsView
    from .Ui_PSAOnEventsResultsView import Ui_PSAOnEventsResultsView
else:
    # Create stub classes for headless mode
    PSAOnEventsResultsView = None
    Ui_PSAOnEventsResultsView = None
