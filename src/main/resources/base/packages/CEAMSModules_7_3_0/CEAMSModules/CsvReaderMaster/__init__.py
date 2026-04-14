"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .CsvReaderMaster import CsvReaderMaster
from .CsvReaderMasterSettingsView import CsvReaderMasterSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .CsvReaderMasterResultsView import CsvReaderMasterResultsView
    from .Ui_CsvReaderMasterResultsView import Ui_CsvReaderMasterResultsView
    from .Ui_CsvReaderMasterSettingsView import Ui_CsvReaderMasterSettingsView
else:
    # Create stub classes for headless mode
    CsvReaderMasterResultsView = None
    Ui_CsvReaderMasterResultsView = None
    Ui_CsvReaderMasterSettingsView = None
