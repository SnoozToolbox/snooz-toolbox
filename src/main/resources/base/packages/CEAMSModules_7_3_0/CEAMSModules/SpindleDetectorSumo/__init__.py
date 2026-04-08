"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
from .SpindleDetectorSumo import SpindleDetectorSumo
from .SpindleDetectorSumoSettingsView import SpindleDetectorSumoSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .SpindleDetectorSumoResultsView import SpindleDetectorSumoResultsView
    from .Ui_SpindleDetectorSumoResultsView import Ui_SpindleDetectorSumoResultsView
    from .Ui_SpindleDetectorSumoSettingsView import Ui_SpindleDetectorSumoSettingsView
else:
    # Create stub classes for headless mode
    SpindleDetectorSumoResultsView = None
    Ui_SpindleDetectorSumoResultsView = None
    Ui_SpindleDetectorSumoSettingsView = None
