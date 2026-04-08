"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .SlowWaveDetector import SlowWaveDetector
from .SlowWaveDetectorSettingsView import SlowWaveDetectorSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .SlowWaveDetectorResultsView import SlowWaveDetectorResultsView
    from .Ui_SlowWaveDetectorSettingsView import Ui_SlowWaveDetectorSettingsView
else:
    # Create stub classes for headless mode
    SlowWaveDetectorResultsView = None
    Ui_SlowWaveDetectorSettingsView = None
