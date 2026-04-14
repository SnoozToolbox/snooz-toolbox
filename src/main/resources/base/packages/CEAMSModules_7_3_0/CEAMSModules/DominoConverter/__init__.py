"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .DominoConverter import DominoConverter
from .DominoConverterSettingsView import DominoConverterSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .DominoConverterResultsView import DominoConverterResultsView
    from .Ui_DominoConverterResultsView import Ui_DominoConverterResultsView
    from .Ui_DominoConverterSettingsView import Ui_DominoConverterSettingsView
else:
    # Create stub classes for headless mode
    DominoConverterResultsView = None
    Ui_DominoConverterResultsView = None
    Ui_DominoConverterSettingsView = None
