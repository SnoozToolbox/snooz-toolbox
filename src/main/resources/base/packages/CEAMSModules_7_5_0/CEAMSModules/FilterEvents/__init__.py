"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .FilterEvents import FilterEvents
from .FilterEventsSettingsView import FilterEventsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .FilterEventsResultsView import FilterEventsResultsView
    from .Ui_FilterEventsSettingsView import Ui_FilterEventsSettingsView
else:
    # Create stub classes for headless mode
    FilterEventsResultsView = None
    Ui_FilterEventsSettingsView = None
