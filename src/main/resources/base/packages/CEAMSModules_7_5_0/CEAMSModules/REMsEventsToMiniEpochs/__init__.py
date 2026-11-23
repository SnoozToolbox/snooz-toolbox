"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from .REMsEventsToMiniEpochs import REMsEventsToMiniEpochs
from .REMsEventsToMiniEpochsSettingsView import REMsEventsToMiniEpochsSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .REMsEventsToMiniEpochsResultsView import REMsEventsToMiniEpochsResultsView
    from .Ui_REMsEventsToMiniEpochsSettingsView import Ui_REMsEventsToMiniEpochsSettingsView
else:
    # Create stub classes for headless mode
    REMsEventsToMiniEpochsResultsView = None
    Ui_REMsEventsToMiniEpochsSettingsView = None