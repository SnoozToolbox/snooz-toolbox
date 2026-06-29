"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .Dictionary import Dictionary
from .DictionarySettingsView import DictionarySettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .DictionaryResultsView import DictionaryResultsView
    from .Ui_DictionaryResultsView import Ui_DictionaryResultsView
    from .Ui_DictionarySettingsView import Ui_DictionarySettingsView
else:
    # Create stub classes for headless mode
    DictionaryResultsView = None
    Ui_DictionaryResultsView = None
    Ui_DictionarySettingsView = None
