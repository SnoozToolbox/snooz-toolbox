"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .SpindlesDetails import SpindlesDetails
from .SpindlesDetailsSettingsView import SpindlesDetailsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .SpindlesDetailsResultsView import SpindlesDetailsResultsView
    from .Ui_SpindlesDetailsResultsView import Ui_SpindlesDetailsResultsView
    from .Ui_SpindlesDetailsSettingsView import Ui_SpindlesDetailsSettingsView
else:
    # Create stub classes for headless mode
    SpindlesDetailsResultsView = None
    Ui_SpindlesDetailsResultsView = None
    Ui_SpindlesDetailsSettingsView = None
