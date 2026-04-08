"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .Constant import Constant
from .ConstantSettingsView import ConstantSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .ConstantResultsView import ConstantResultsView
    from .Ui_ConstantResultsView import Ui_ConstantResultsView
    from .Ui_ConstantSettingsView import Ui_ConstantSettingsView
else:
    # Create stub classes for headless mode
    ConstantResultsView = None
    Ui_ConstantResultsView = None
    Ui_ConstantSettingsView = None
