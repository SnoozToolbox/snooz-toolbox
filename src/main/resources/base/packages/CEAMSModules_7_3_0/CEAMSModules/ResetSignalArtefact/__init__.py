"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .ResetSignalArtefact import ResetSignalArtefact
from .ResetSignalArtefactSettingsView import ResetSignalArtefactSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .ResetSignalArtefactResultsView import ResetSignalArtefactResultsView
    from .Ui_ResetSignalArtefactResultsView import Ui_ResetSignalArtefactResultsView
    from .Ui_ResetSignalArtefactSettingsView import Ui_ResetSignalArtefactSettingsView
else:
    # Create stub classes for headless mode
    ResetSignalArtefactResultsView = None
    Ui_ResetSignalArtefactResultsView = None
    Ui_ResetSignalArtefactSettingsView = None
