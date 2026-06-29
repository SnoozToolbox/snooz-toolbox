"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .SubtractSignals import SubtractSignals
from .SubtractSignalsSettingsView import SubtractSignalsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .SubtractSignalsResultsView import SubtractSignalsResultsView
    from .Ui_SubtractSignalsResultsView import Ui_SubtractSignalsResultsView
    from .Ui_SubtractSignalsSettingsView import Ui_SubtractSignalsSettingsView
else:
    # Create stub classes for headless mode
    SubtractSignalsResultsView = None
    Ui_SubtractSignalsResultsView = None
    Ui_SubtractSignalsSettingsView = None
