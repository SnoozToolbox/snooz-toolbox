"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .AliasSignals import AliasSignals
from .AliasSignalsSettingsView import AliasSignalsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .AliasSignalsResultsView import AliasSignalsResultsView
    from .Ui_AliasSignalsResultsView import Ui_AliasSignalsResultsView
    from .Ui_AliasSignalsSettingsView import Ui_AliasSignalsSettingsView
else:
    # Create stub classes for headless mode
    AliasSignalsResultsView = None
    Ui_AliasSignalsResultsView = None
    Ui_AliasSignalsSettingsView = None
