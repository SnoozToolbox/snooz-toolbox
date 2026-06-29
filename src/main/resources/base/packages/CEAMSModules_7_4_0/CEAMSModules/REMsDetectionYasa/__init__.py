"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
from .REMsDetectionYasa import REMsDetectionYasa
from .REMsDetectionYasaSettingsView import REMsDetectionYasaSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .REMsDetectionYasaResultsView import REMsDetectionYasaResultsView
    from .Ui_REMsDetectionYasaResultsView import Ui_REMsDetectionYasaResultsView
    from .Ui_REMsDetectionYasaSettingsView import Ui_REMsDetectionYasaSettingsView
else:
    # Create stub classes for headless mode
    REMsDetectionYasaResultsView = None
    Ui_REMsDetectionYasaResultsView = None
    Ui_REMsDetectionYasaSettingsView = None
