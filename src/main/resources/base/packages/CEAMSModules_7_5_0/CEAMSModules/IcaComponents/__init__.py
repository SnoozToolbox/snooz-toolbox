"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .IcaComponents import IcaComponents
from .IcaComponentsSettingsView import IcaComponentsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .IcaComponentsResultsView import IcaComponentsResultsView
    from .Ui_IcaComponentsResultsView import Ui_IcaComponentsResultsView
    from .Ui_IcaComponentsSettingsView import Ui_IcaComponentsSettingsView
else:
    # Create stub classes for headless mode
    IcaComponentsResultsView = None
    Ui_IcaComponentsResultsView = None
    Ui_IcaComponentsSettingsView = None
