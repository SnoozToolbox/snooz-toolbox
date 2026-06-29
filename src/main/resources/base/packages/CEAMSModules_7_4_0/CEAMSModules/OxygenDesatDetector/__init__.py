"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .OxygenDesatDetector import OxygenDesatDetector
from .OxygenDesatDetectorSettingsView import OxygenDesatDetectorSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .OxygenDesatDetectorResultsView import OxygenDesatDetectorResultsView
    from .Ui_OxygenDesatDetectorResultsView import Ui_OxygenDesatDetectorResultsView
    from .Ui_OxygenDesatDetectorSettingsView import Ui_OxygenDesatDetectorSettingsView
else:
    # Create stub classes for headless mode
    OxygenDesatDetectorResultsView = None
    Ui_OxygenDesatDetectorResultsView = None
    Ui_OxygenDesatDetectorSettingsView = None
