"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
from .SignalStats import SignalStats
from .SignalStatsSettingsView import SignalStatsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .SignalStatsResultsView import SignalStatsResultsView
    from .Ui_SignalStatsResultsView import Ui_SignalStatsResultsView
    from .Ui_SignalStatsSettingsView import Ui_SignalStatsSettingsView
else:
    # Create stub classes for headless mode
    SignalStatsResultsView = None
    Ui_SignalStatsResultsView = None
    Ui_SignalStatsSettingsView = None
