"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .TsvWriter import TsvWriter
from .TsvWriterSettingsView import TsvWriterSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .TsvWriterResultsView import TsvWriterResultsView
    from .Ui_TsvWriterResultsView import Ui_TsvWriterResultsView
    from .Ui_TsvWriterSettingsView import Ui_TsvWriterSettingsView
else:
    # Create stub classes for headless mode
    TsvWriterResultsView = None
    Ui_TsvWriterResultsView = None
    Ui_TsvWriterSettingsView = None
