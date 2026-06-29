"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .ReplaceEventInSignals import ReplaceEventInSignals
from .ReplaceEventInSignalsSettingsView import ReplaceEventInSignalsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .ReplaceEventInSignalsResultsView import ReplaceEventInSignalsResultsView
    from .Ui_ReplaceEventInSignalsSettingsView import Ui_ReplaceEventInSignalsSettingsView
else:
    # Create stub classes for headless mode
    ReplaceEventInSignalsResultsView = None
    Ui_ReplaceEventInSignalsSettingsView = None
