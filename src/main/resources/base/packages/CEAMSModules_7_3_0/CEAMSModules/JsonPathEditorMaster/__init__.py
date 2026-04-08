"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
from .JsonPathEditorMaster import JsonPathEditorMaster
from .JsonPathEditorMasterSettingsView import JsonPathEditorMasterSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .JsonPathEditorMasterResultsView import JsonPathEditorMasterResultsView
    from .Ui_JsonPathEditorMasterResultsView import Ui_JsonPathEditorMasterResultsView
    from .Ui_JsonPathEditorMasterSettingsView import Ui_JsonPathEditorMasterSettingsView
else:
    # Create stub classes for headless mode
    JsonPathEditorMasterResultsView = None
    Ui_JsonPathEditorMasterResultsView = None
    Ui_JsonPathEditorMasterSettingsView = None
