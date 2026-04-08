"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .PSGWriter import PSGWriter
from .PSGWriterSettingsView import PSGWriterSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .PSGWriterResultsView import PSGWriterResultsView
    from .Ui_PSGWriterResultsView import Ui_PSGWriterResultsView
    from .Ui_PSGWriterSettingsView import Ui_PSGWriterSettingsView
else:
    # Create stub classes for headless mode
    PSGWriterResultsView = None
    Ui_PSGWriterResultsView = None
    Ui_PSGWriterSettingsView = None
