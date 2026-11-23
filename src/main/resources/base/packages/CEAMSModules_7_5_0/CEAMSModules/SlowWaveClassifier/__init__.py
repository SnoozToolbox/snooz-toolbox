"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .SlowWaveClassifier import SlowWaveClassifier
from .SlowWaveClassifierSettingsView import SlowWaveClassifierSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .SlowWaveClassifierResultsView import SlowWaveClassifierResultsView
    from .Ui_SlowWaveClassifierResultsView import Ui_SlowWaveClassifierResultsView
    from .Ui_SlowWaveClassifierSettingsView import Ui_SlowWaveClassifierSettingsView
else:
    # Create stub classes for headless mode
    SlowWaveClassifierResultsView = None
    Ui_SlowWaveClassifierResultsView = None
    Ui_SlowWaveClassifierSettingsView = None
