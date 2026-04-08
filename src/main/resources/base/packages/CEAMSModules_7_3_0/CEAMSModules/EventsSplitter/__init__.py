"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .EventsSplitter import EventsSplitter
from .EventsSplitterSettingsView import EventsSplitterSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .EventsSplitterResultsView import EventsSplitterResultsView
    from .Ui_EventsSplitterResultsView import Ui_EventsSplitterResultsView
    from .Ui_EventsSplitterSettingsView import Ui_EventsSplitterSettingsView
else:
    # Create stub classes for headless mode
    EventsSplitterResultsView = None
    Ui_EventsSplitterResultsView = None
    Ui_EventsSplitterSettingsView = None
