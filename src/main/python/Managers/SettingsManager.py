"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
import os

from qtpy import QtWidgets
from qtpy import QtCore

import config
from config import settings

class SettingsManager(QtCore.QObject):
    """ Manages the user settings of the application. """

    def __init__(self, managers):
        """ Init the settings manager."""
        super(SettingsManager, self).__init__()
        self._managers = managers
        self._package_manager = self._managers.package_manager
    
    def initialize(self):
        """ Initialize the settings manager. """
        pass

    def append_setting(self, setting_name, value):
        setting = config.app_settings.value(setting_name, [])

        # Settings with a single value are converted to a string, convert it back to
        # a list so you can append a value.
        if not isinstance(setting, list):
            setting = [setting]

        setting.append(value)
        config.app_settings.setValue(setting_name, setting)

    def get_setting(self, setting_name, default_value):
        return config.app_settings.value(setting_name, default_value)

    def set_setting(self, setting_name, value):
        config.app_settings.setValue(setting_name, value)
