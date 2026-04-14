"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .IcaRestore import IcaRestore
from .IcaRestoreSettingsView import IcaRestoreSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .IcaRestoreResultsView import IcaRestoreResultsView
    from .Ui_IcaRestoreResultsView import Ui_IcaRestoreResultsView
    from .Ui_IcaRestoreSettingsView import Ui_IcaRestoreSettingsView
else:
    # Create stub classes for headless mode
    IcaRestoreResultsView = None
    Ui_IcaRestoreResultsView = None
    Ui_IcaRestoreSettingsView = None
