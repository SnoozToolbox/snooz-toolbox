"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .Hypnogram import Hypnogram
from .HypnogramSettingsView import HypnogramSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .HypnogramResultsView import HypnogramResultsView
    from .Ui_HypnogramResultsView import Ui_HypnogramResultsView
    from .Ui_HypnogramSettingsView import Ui_HypnogramSettingsView
else:
    # Create stub classes for headless mode
    HypnogramResultsView = None
    Ui_HypnogramResultsView = None
    Ui_HypnogramSettingsView = None
