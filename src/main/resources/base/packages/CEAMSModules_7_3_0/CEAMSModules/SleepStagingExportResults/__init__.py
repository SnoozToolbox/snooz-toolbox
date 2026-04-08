"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
from .SleepStagingExportResults import SleepStagingExportResults
from .SleepStagingExportResultsSettingsView import SleepStagingExportResultsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .SleepStagingExportResultsResultsView import SleepStagingExportResultsResultsView
    from .Ui_SleepStagingExportResultsResultsView import Ui_SleepStagingExportResultsResultsView
    from .Ui_SleepStagingExportResultsSettingsView import Ui_SleepStagingExportResultsSettingsView
else:
    # Create stub classes for headless mode
    SleepStagingExportResultsResultsView = None
    Ui_SleepStagingExportResultsResultsView = None
    Ui_SleepStagingExportResultsSettingsView = None