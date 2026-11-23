"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
from .CreateTuple import CreateTuple
from .CreateTupleSettingsView import CreateTupleSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .CreateTupleResultsView import CreateTupleResultsView
    from .Ui_CreateTupleResultsView import Ui_CreateTupleResultsView
    from .Ui_CreateTupleSettingsView import Ui_CreateTupleSettingsView
else:
    # Create stub classes for headless mode
    CreateTupleResultsView = None
    Ui_CreateTupleResultsView = None
    Ui_CreateTupleSettingsView = None
