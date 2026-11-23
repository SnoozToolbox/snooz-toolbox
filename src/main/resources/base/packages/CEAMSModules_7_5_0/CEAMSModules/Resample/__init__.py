"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .Resample import Resample
from .ResampleSettingsView import ResampleSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .ResampleResultsView import ResampleResultsView
    from .Ui_ResampleResultsView import Ui_ResampleResultsView
    from .Ui_ResampleSettingsView import Ui_ResampleSettingsView
else:
    # Create stub classes for headless mode
    ResampleResultsView = None
    Ui_ResampleResultsView = None
    Ui_ResampleSettingsView = None
