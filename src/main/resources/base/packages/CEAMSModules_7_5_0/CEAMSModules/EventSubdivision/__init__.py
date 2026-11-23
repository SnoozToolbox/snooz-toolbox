"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
from .EventSubdivision import EventSubdivision
from .EventSubdivisionSettingsView import EventSubdivisionSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .EventSubdivisionResultsView import EventSubdivisionResultsView
    from .Ui_EventSubdivisionResultsView import Ui_EventSubdivisionResultsView
    from .Ui_EventSubdivisionSettingsView import Ui_EventSubdivisionSettingsView
else:
    # Create stub classes for headless mode
    EventSubdivisionResultsView = None
    Ui_EventSubdivisionResultsView = None
    Ui_EventSubdivisionSettingsView = None
