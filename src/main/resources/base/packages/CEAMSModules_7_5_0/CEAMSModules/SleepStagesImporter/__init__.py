"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from .SleepStagesImporter import SleepStagesImporter
from .SleepStagesImporterSettingsView import SleepStagesImporterSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .SleepStagesImporterResultsView import SleepStagesImporterResultsView
    #from .Ui_SleepStagesImporterResultsView import Ui_SleepStagesImporterResultsView
    from .Ui_SleepStagesImporterSettingsView import Ui_SleepStagesImporterSettingsView
else:
    # Create stub classes for headless mode
    SleepStagesImporterResultsView = None
    Ui_SleepStagesImporterResultsView = None
    Ui_SleepStagesImporterSettingsView = None
