"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .WindowsToSamples import WindowsToSamples
from .WindowsToSamplesSettingsView import WindowsToSamplesSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .WindowsToSamplesResultsView import WindowsToSamplesResultsView
    from .Ui_WindowsToSamplesResultsView import Ui_WindowsToSamplesResultsView
    from .Ui_WindowsToSamplesSettingsView import Ui_WindowsToSamplesSettingsView
else:
    # Create stub classes for headless mode
    WindowsToSamplesResultsView = None
    Ui_WindowsToSamplesResultsView = None
    Ui_WindowsToSamplesSettingsView = None
