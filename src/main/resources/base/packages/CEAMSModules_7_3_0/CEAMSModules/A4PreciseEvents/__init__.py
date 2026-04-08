"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .A4PreciseEvents import A4PreciseEvents
from .A4PreciseEventsSettingsView import A4PreciseEventsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .A4PreciseEventsResultsView import A4PreciseEventsResultsView
    from .Ui_A4PreciseEventsResultsView import Ui_A4PreciseEventsResultsView
    from .Ui_A4PreciseEventsSettingsView import Ui_A4PreciseEventsSettingsView
else:
    # Create stub classes for headless mode
    A4PreciseEventsResultsView = None
    Ui_A4PreciseEventsResultsView = None
    Ui_A4PreciseEventsSettingsView = None
