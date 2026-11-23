"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
from .InvertSignals import InvertSignals
from .InvertSignalsSettingsView import InvertSignalsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .InvertSignalsResultsView import InvertSignalsResultsView
    from .Ui_InvertSignalsResultsView import Ui_InvertSignalsResultsView
    from .Ui_InvertSignalsSettingsView import Ui_InvertSignalsSettingsView
else:
    # Create stub classes for headless mode
    InvertSignalsResultsView = None
    Ui_InvertSignalsResultsView = None
    Ui_InvertSignalsSettingsView = None
