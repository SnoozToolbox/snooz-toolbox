"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .EventSleepReport import EventSleepReport
from .EventSleepReportSettingsView import EventSleepReportSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .EventSleepReportResultsView import EventSleepReportResultsView
    from .Ui_EventSleepReportResultsView import Ui_EventSleepReportResultsView
    from .Ui_EventSleepReportSettingsView import Ui_EventSleepReportSettingsView
else:
    # Create stub classes for headless mode
    EventSleepReportResultsView = None
    Ui_EventSleepReportResultsView = None
    Ui_EventSleepReportSettingsView = None
