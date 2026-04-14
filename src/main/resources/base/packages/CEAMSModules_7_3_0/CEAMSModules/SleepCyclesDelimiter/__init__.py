"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .SleepCyclesDelimiter import SleepCyclesDelimiter
from .SleepCyclesDelimiterSettingsView import SleepCyclesDelimiterSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .SleepCyclesDelimiterResultsView import SleepCyclesDelimiterResultsView
    from .Ui_SleepCyclesDelimiterResultsView import Ui_SleepCyclesDelimiterResultsView
    from .Ui_SleepCyclesDelimiterSettingsView import Ui_SleepCyclesDelimiterSettingsView
else:
    # Create stub classes for headless mode
    SleepCyclesDelimiterResultsView = None
    Ui_SleepCyclesDelimiterResultsView = None
    Ui_SleepCyclesDelimiterSettingsView = None
