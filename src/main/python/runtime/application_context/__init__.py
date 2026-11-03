"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.


This file was highly inspired from the fbs library. It contains the necessary implementation to run the application without needing
a pro version of fbs, thus making it possible for developers without the pro version of fbs to be able to create tools for Snooz.

Although the logic remains the same, some methods were optimized as the purpose of the file is only to run the application, not to create
installers or packaging the application. If there is a need to create such entities, the user will have to obtain a pro version of fbs.
"""
from functools import cached_property

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

import config
from runtime.application_context.base import BaseResourceApplicationContext
from runtime.platform import is_mac


class ApplicationContext(BaseResourceApplicationContext):
    def __init__(self):
        self.app # Initialization of the QApplication
        if self.app_icon is not None:
            self.app.setWindowIcon(self.app_icon)
    
    @cached_property
    def app(self):
        result = QApplication([])
        result.setApplicationName(config.app_name)
        result.setApplicationVersion(str(config.version))

        return result

    @cached_property
    def app_icon(self):
        """
        The icon of every window (main window, dialogs and message boxes), as with fbs.
        Not available on Mac because app icons are handled by the OS there.
        """
        if is_mac():
            return None
        try:
            return QIcon(self.get_resource('Icon.ico'))
        except (FileNotFoundError, RuntimeError):
            return None # The icon is optional: it must not prevent the application from starting
