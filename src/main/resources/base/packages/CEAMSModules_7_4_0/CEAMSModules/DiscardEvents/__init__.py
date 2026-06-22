"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .DiscardEvents import DiscardEvents
from .DiscardEventsSettingsView import DiscardEventsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .DiscardEventsResultsView import DiscardEventsResultsView
    from .Ui_DiscardEventsResultsView import Ui_DiscardEventsResultsView
    from .Ui_DiscardEventsSettingsView import Ui_DiscardEventsSettingsView
else:
    # Create stub classes for headless mode
    DiscardEventsResultsView = None
    Ui_DiscardEventsResultsView = None
    Ui_DiscardEventsSettingsView = None
