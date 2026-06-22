from .EventReader import EventReader
from .EventReaderSettingsView import EventReaderSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .EventReaderResultsView import EventReaderResultsView
    from .Ui_EventReaderResultsView import Ui_EventReaderResultsView
    from .Ui_EventReaderSettingsView import Ui_EventReaderSettingsView
else:
    # Create stub classes for headless mode
    EventReaderResultsView = None
    Ui_EventReaderResultsView = None
    Ui_EventReaderSettingsView = None
