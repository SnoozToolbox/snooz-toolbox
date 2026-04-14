"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .StringManip import StringManip
from .StringManipSettingsView import StringManipSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .StringManipResultsView import StringManipResultsView
    from .Ui_StringManipResultsView import Ui_StringManipResultsView
    from .Ui_StringManipSettingsView import Ui_StringManipSettingsView
else:
    # Create stub classes for headless mode
    StringManipResultsView = None
    Ui_StringManipResultsView = None
    Ui_StringManipSettingsView = None
