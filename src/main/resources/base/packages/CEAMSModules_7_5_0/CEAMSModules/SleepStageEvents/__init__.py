"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .SleepStageEvents import SleepStageEvents
from .SleepStageEventsSettingsView import SleepStageEventsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .Ui_SleepStageEventsSettingsView import Ui_SleepStageEventsSettingsView
else:
    # Create stub classes for headless mode
    Ui_SleepStageEventsSettingsView = None
