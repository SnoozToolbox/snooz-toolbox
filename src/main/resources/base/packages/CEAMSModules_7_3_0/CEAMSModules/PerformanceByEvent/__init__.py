"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .PerformanceByEvent import PerformanceByEvent
from .PerformanceByEventSettingsView import PerformanceByEventSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .PerformanceByEventResultsView import PerformanceByEventResultsView
    from .Ui_PerformanceByEventResultsView import Ui_PerformanceByEventResultsView
    from .Ui_PerformanceByEventSettingsView import Ui_PerformanceByEventSettingsView
else:
    # Create stub classes for headless mode
    PerformanceByEventResultsView = None
    Ui_PerformanceByEventResultsView = None
    Ui_PerformanceByEventSettingsView = None
