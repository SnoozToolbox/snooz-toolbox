"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from .SlowWavePicsGenerator import SlowWavePicsGenerator
from .SlowWavePicsGeneratorSettingsView import SlowWavePicsGeneratorSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .SlowWavePicsGeneratorResultsView import SlowWavePicsGeneratorResultsView
    from .Ui_SlowWavePicsGeneratorResultsView import Ui_SlowWavePicsGeneratorResultsView
    from .Ui_SlowWavePicsGeneratorSettingsView import Ui_SlowWavePicsGeneratorSettingsView
else:
    # Create stub classes for headless mode
    SlowWavePicsGeneratorResultsView = None
    Ui_SlowWavePicsGeneratorResultsView = None
    Ui_SlowWavePicsGeneratorSettingsView = None