"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .AmplitudeVarDetector import AmplitudeVarDetector
from .AmplitudeVarDetectorSettingsView import AmplitudeVarDetectorSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .AmplitudeVarDetectorResultsView import AmplitudeVarDetectorResultsView
    from .Ui_AmplitudeVarDetectorResultsView import Ui_AmplitudeVarDetectorResultsView
    from .Ui_AmplitudeVarDetectorSettingsView import Ui_AmplitudeVarDetectorSettingsView
else:
    # Create stub classes for headless mode
    AmplitudeVarDetectorResultsView = None
    Ui_AmplitudeVarDetectorResultsView = None
    Ui_AmplitudeVarDetectorSettingsView = None
