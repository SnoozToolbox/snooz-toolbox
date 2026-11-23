"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .SignalsFromEvents import SignalsFromEvents
from .SignalsFromEventsSettingsView import SignalsFromEventsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .SignalsFromEventsResultsView import SignalsFromEventsResultsView
    from .Ui_SignalsFromEventsResultsView import Ui_SignalsFromEventsResultsView
    from .Ui_SignalsFromEventsSettingsView import Ui_SignalsFromEventsSettingsView
else:
    # Create stub classes for headless mode
    SignalsFromEventsResultsView = None
    Ui_SignalsFromEventsResultsView = None
    Ui_SignalsFromEventsSettingsView = None
