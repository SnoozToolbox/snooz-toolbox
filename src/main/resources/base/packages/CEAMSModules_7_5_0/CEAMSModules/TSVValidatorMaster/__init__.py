"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
from .TSVValidatorMaster import TSVValidatorMaster
from .TSVValidatorMasterSettingsView import TSVValidatorMasterSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .TSVValidatorMasterResultsView import TSVValidatorMasterResultsView
    from .Ui_TSVValidatorMasterResultsView import Ui_TSVValidatorMasterResultsView
    from .Ui_TSVValidatorMasterSettingsView import Ui_TSVValidatorMasterSettingsView
else:
    # Create stub classes for headless mode
    TSVValidatorMasterResultsView = None
    Ui_TSVValidatorMasterResultsView = None
    Ui_TSVValidatorMasterSettingsView = None
