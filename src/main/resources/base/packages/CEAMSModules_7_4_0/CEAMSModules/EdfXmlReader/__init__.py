"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .EdfXmlReader import EdfXmlReader
from .EdfXmlReaderSettingsView import EdfXmlReaderSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .EdfXmlReaderResultsView import EdfXmlReaderResultsView
    from .Ui_EdfXmlReaderResultsView import Ui_EdfXmlReaderResultsView
    from .Ui_EdfXmlReaderSettingsView import Ui_EdfXmlReaderSettingsView
else:
    # Create stub classes for headless mode
    EdfXmlReaderResultsView = None
    Ui_EdfXmlReaderResultsView = None
    Ui_EdfXmlReaderSettingsView = None
