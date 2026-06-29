"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
from .YasaSleepStaging import YasaSleepStaging
from .YasaSleepStagingSettingsView import YasaSleepStagingSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .YasaSleepStagingResultsView import YasaSleepStagingResultsView
    from .Ui_YasaSleepStagingResultsView import Ui_YasaSleepStagingResultsView
    from .Ui_YasaSleepStagingSettingsView import Ui_YasaSleepStagingSettingsView
else:
    # Create stub classes for headless mode
    YasaSleepStagingResultsView = None
    Ui_YasaSleepStagingResultsView = None
    Ui_YasaSleepStagingSettingsView = None