"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .SpectralDetector import SpectralDetector
from .SpectralDetectorSettingsView import SpectralDetectorSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .SpectralDetectorResultsView import SpectralDetectorResultsView
    from .Ui_SpectralDetectorResultsView import Ui_SpectralDetectorResultsView
    from .Ui_SpectralDetectorSettingsView import Ui_SpectralDetectorSettingsView
else:
    # Create stub classes for headless mode
    SpectralDetectorResultsView = None
    Ui_SpectralDetectorResultsView = None
    Ui_SpectralDetectorSettingsView = None
