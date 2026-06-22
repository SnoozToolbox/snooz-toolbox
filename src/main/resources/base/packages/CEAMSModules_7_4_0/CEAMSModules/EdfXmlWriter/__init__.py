"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .EdfXmlWriter import EdfXmlWriter
from .EdfXmlWriterSettingsView import EdfXmlWriterSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .EdfXmlWriterResultsView import EdfXmlWriterResultsView
    from .Ui_EdfXmlWriterResultsView import Ui_EdfXmlWriterResultsView
    from .Ui_EdfXmlWriterSettingsView import Ui_EdfXmlWriterSettingsView
else:
    # Create stub classes for headless mode
    EdfXmlWriterResultsView = None
    Ui_EdfXmlWriterResultsView = None
    Ui_EdfXmlWriterSettingsView = None
