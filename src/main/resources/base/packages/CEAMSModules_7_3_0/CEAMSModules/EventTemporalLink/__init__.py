"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .EventTemporalLink import EventTemporalLink
from .EventTemporalLinkSettingsView import EventTemporalLinkSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .EventTemporalLinkResultsView import EventTemporalLinkResultsView
    from .Ui_EventTemporalLinkResultsView import Ui_EventTemporalLinkResultsView
    from .Ui_EventTemporalLinkSettingsView import Ui_EventTemporalLinkSettingsView
else:
    # Create stub classes for headless mode
    EventTemporalLinkResultsView = None
    Ui_EventTemporalLinkResultsView = None
    Ui_EventTemporalLinkSettingsView = None
