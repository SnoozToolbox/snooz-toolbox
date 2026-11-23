"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
from .IRASAYASA import IRASAYASA
from .IRASAYASASettingsView import IRASAYASASettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .IRASAYASAResultsView import IRASAYASAResultsView
    from .Ui_IRASAYASAResultsView import Ui_IRASAYASAResultsView
    from .Ui_IRASAYASASettingsView import Ui_IRASAYASASettingsView
else:
    # Create stub classes for headless mode
    IRASAYASAResultsView = None
    Ui_IRASAYASAResultsView = None
    Ui_IRASAYASASettingsView = None
