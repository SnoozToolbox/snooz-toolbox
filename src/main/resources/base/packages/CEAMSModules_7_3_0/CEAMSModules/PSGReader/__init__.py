"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .PSGReader import PSGReader
from .PSGReaderSettingsView import PSGReaderSettingsView
from .ChannelsProxyModel import ChannelsProxyModel
from .ChannelsTableModel import ChannelsTableModel
from .MontagesProxyModel import MontagesProxyModel
from .MontagesTableModel import MontagesTableModel

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .PSGReaderResultsView import PSGReaderResultsView
    from .Ui_PSGReaderResultsView import Ui_PSGReaderResultsView
    from .Ui_PSGReaderSettingsView import Ui_PSGReaderSettingsView
else:
    # Create stub classes for headless mode
    PSGReaderResultsView = None
    Ui_PSGReaderResultsView = None
    Ui_PSGReaderSettingsView = None
