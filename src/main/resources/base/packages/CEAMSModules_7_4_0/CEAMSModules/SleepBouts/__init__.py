"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .SleepBouts import SleepBouts
from .SleepBoutsSettingsView import SleepBoutsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .SleepBoutsResultsView import SleepBoutsResultsView
    from .Ui_SleepBoutsResultsView import Ui_SleepBoutsResultsView
    from .Ui_SleepBoutsSettingsView import Ui_SleepBoutsSettingsView
else:
    # Create stub classes for headless mode
    SleepBoutsResultsView = None
    Ui_SleepBoutsResultsView = None
    Ui_SleepBoutsSettingsView = None
