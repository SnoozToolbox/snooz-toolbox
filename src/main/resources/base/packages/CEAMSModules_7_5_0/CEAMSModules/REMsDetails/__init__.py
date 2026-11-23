"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
from .REMsDetails import REMsDetails
from .REMsDetailsSettingsView import REMsDetailsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .REMsDetailsResultsView import REMsDetailsResultsView
    from .Ui_REMsDetailsResultsView import Ui_REMsDetailsResultsView
    from .Ui_REMsDetailsSettingsView import Ui_REMsDetailsSettingsView
else:
    # Create stub classes for headless mode
    REMsDetailsResultsView = None
    Ui_REMsDetailsResultsView = None
    Ui_REMsDetailsSettingsView = None

