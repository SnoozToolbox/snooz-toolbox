"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .FilterSignal import FilterSignal
from .FilterSignalSettingsView import FilterSignalSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .FilterSignalResultsView import FilterSignalResultsView
    from .Ui_FilterSignalResultsView import Ui_FilterSignalResultsView
    from .Ui_FilterSignalSettingsView import Ui_FilterSignalSettingsView
else:
    # Create stub classes for headless mode
    FilterSignalResultsView = None
    Ui_FilterSignalResultsView = None
    Ui_FilterSignalSettingsView = None
