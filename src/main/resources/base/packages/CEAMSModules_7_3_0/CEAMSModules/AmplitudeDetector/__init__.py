"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .AmplitudeDetector import AmplitudeDetector
from .AmplitudeDetectorSettingsView import AmplitudeDetectorSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .AmplitudeDetectorResultsView import AmplitudeDetectorResultsView
    from .Ui_AmplitudeDetectorResultsView import Ui_AmplitudeDetectorResultsView
    from .Ui_AmplitudeDetectorSettingsView import Ui_AmplitudeDetectorSettingsView
else:
    # Create stub classes for headless mode
    AmplitudeDetectorResultsView = None
    Ui_AmplitudeDetectorResultsView = None
    Ui_AmplitudeDetectorSettingsView = None
