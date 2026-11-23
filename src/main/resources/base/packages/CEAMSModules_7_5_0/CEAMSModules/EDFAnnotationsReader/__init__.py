"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from .EDFAnnotationsReader import EDFAnnotationsReader
from .EDFAnnotationsReaderSettingsView import EDFAnnotationsReaderSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .EDFAnnotationsReaderResultsView import EDFAnnotationsReaderResultsView
    from .Ui_EDFAnnotationsReaderResultsView import Ui_EDFAnnotationsReaderResultsView
    from .Ui_EDFAnnotationsReaderSettingsView import Ui_EDFAnnotationsReaderSettingsView
else:
    # Create stub classes for headless mode
    EDFAnnotationsReaderResultsView = None
    Ui_EDFAnnotationsReaderResultsView = None
    Ui_EDFAnnotationsReaderSettingsView = None
