"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .EdfXmlReaderMaster import EdfXmlReaderMaster
from .EdfXmlReaderMasterSettingsView import EdfXmlReaderMasterSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .EdfXmlReaderMasterResultsView import EdfXmlReaderMasterResultsView
    from .Ui_EdfXmlReaderMasterResultsView import Ui_EdfXmlReaderMasterResultsView
    from .Ui_EdfXmlReaderMasterSettingsView import Ui_EdfXmlReaderMasterSettingsView
else:
    # Create stub classes for headless mode
    EdfXmlReaderMasterResultsView = None
    Ui_EdfXmlReaderMasterResultsView = None
    Ui_EdfXmlReaderMasterSettingsView = None
