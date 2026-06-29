"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .MutualInfo import MutualInfo
from .MutualInfoSettingsView import MutualInfoSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .MutualInfoResultsView import MutualInfoResultsView
    from .Ui_MutualInfoResultsView import Ui_MutualInfoResultsView
    from .Ui_MutualInfoSettingsView import Ui_MutualInfoSettingsView
else:
    # Create stub classes for headless mode
    MutualInfoResultsView = None
    Ui_MutualInfoResultsView = None
    Ui_MutualInfoSettingsView = None
