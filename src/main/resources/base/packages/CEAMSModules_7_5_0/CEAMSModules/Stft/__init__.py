"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .Stft import Stft
from .StftSettingsView import StftSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .StftResultsView import StftResultsView
    from .Ui_StftResultsView import Ui_StftResultsView
    from .Ui_StftSettingsView import Ui_StftSettingsView
else:
    # Create stub classes for headless mode
    StftResultsView = None
    Ui_StftResultsView = None
    Ui_StftSettingsView = None
