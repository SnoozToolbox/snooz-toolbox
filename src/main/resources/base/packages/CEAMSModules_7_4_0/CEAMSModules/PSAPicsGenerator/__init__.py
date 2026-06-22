"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
from .PSAPicsGenerator import PSAPicsGenerator
from .PSAPicsGeneratorSettingsView import PSAPicsGeneratorSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .PSAPicsGeneratorResultsView import PSAPicsGeneratorResultsView
    from .Ui_PSAPicsGeneratorResultsView import Ui_PSAPicsGeneratorResultsView
    from .Ui_PSAPicsGeneratorSettingsView import Ui_PSAPicsGeneratorSettingsView
else:
    # Create stub classes for headless mode
    PSAPicsGeneratorResultsView = None
    Ui_PSAPicsGeneratorResultsView = None
    Ui_PSAPicsGeneratorSettingsView = None