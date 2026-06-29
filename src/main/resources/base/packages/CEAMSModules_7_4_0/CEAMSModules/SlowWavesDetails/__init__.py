"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .SlowWavesDetails import SlowWavesDetails
from .SlowWavesDetailsSettingsView import SlowWavesDetailsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .SlowWavesDetailsResultsView import SlowWavesDetailsResultsView
    from .Ui_SlowWavesDetailsResultsView import Ui_SlowWavesDetailsResultsView
    from .Ui_SlowWavesDetailsSettingsView import Ui_SlowWavesDetailsSettingsView
else:
    # Create stub classes for headless mode
    SlowWavesDetailsResultsView = None
    Ui_SlowWavesDetailsResultsView = None
    Ui_SlowWavesDetailsSettingsView = None
