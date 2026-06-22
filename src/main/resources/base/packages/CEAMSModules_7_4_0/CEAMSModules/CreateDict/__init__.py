"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
from .CreateDict import CreateDict
from .CreateDictSettingsView import CreateDictSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .CreateDictResultsView import CreateDictResultsView
    from .Ui_CreateDictResultsView import Ui_CreateDictResultsView
    from .Ui_CreateDictSettingsView import Ui_CreateDictSettingsView
else:
    # Create stub classes for headless mode
    CreateDictResultsView = None
    Ui_CreateDictResultsView = None
    Ui_CreateDictSettingsView = None
