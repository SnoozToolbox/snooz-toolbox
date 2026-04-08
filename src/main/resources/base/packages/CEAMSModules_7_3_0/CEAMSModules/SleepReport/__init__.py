"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .SleepReport import SleepReport
from .SleepReportDoc import write_doc_file
from .SleepReportSettingsView import SleepReportSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .SleepReportResultsView import SleepReportResultsView
    from .Ui_SleepReportResultsView import Ui_SleepReportResultsView
    from .Ui_SleepReportSettingsView import Ui_SleepReportSettingsView
else:
    # Create stub classes for headless mode
    SleepReportResultsView = None
    Ui_SleepReportResultsView = None
    Ui_SleepReportSettingsView = None
