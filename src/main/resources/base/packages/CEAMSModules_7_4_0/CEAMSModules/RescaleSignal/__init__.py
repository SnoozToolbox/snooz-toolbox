"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .RescaleSignal import RescaleSignal
from .RescaleSignalSettingsView import RescaleSignalSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .RescaleSignalResultsView import RescaleSignalResultsView
    from .Ui_RescaleSignalResultsView import Ui_RescaleSignalResultsView
    from .Ui_RescaleSignalSettingsView import Ui_RescaleSignalSettingsView
else:
    # Create stub classes for headless mode
    RescaleSignalResultsView = None
    Ui_RescaleSignalResultsView = None
    Ui_RescaleSignalSettingsView = None
