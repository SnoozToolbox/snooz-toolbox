"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
import base64
import certifi
import platform
import ssl
import urllib.request
from qtpy import QtWidgets
from qtpy.QtCore import QUrl
from qtpy.QtGui import QPixmap, QDesktopServices

import config
if not config.is_dev:
    from fbs_runtime import PUBLIC_SETTINGS
from ui.Ui_AboutDialog import Ui_AboutDialog
from widgets.WarningDialog import WarningDialog

class AboutDialog(QtWidgets.QDialog, Ui_AboutDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self._load_embedded_image()
        
        self.url = 'https://f004.backblazeb2.com/file/snooz-release/about_notes.txt'
        
        # Developers who create the installer needs to use FBS pro.
        if not config.is_dev:
            version = PUBLIC_SETTINGS['version']
            self.snooz_version_label.setText(f"The version currently installed : <b>beta-{version}</b>")
        else:
            self.snooz_version_label.setText("<b>You are using the dev environment, no updates required.</b>")

        os_name = platform.system()
        if os_name=="Darwin":
            try:
                # Create an SSL context with certifi's CA bundle (provided by Mozilla’s CA Bundle)
                # macOS requires to specify the path to the CA certificates file for SSL connections.
                context = ssl.create_default_context(cafile=certifi.where())
                with urllib.request.urlopen(self.url, context=context) as response:
                    content = response.read().decode('utf-8')
            except:
                WarningDialog(f"The file {self.url} cannot be read properly. Can be the certifi's CA bundle or the url access.")
        else:
            try:
                with urllib.request.urlopen(self.url) as response:
                    content = response.read().decode('utf-8')   
            except:
                WarningDialog(f"The file {self.url} cannot be read properly. Can be the certifi's CA bundle or the url access.")         
        
        # For example, let's assume the file content has three lines we want to assign to variables
        lines = content.split('\n')
        self.snooz_released_version = self._get_content(lines, 0)
        self.windows_link = self._get_content(lines, 1)
        self.MAC_link = self._get_content(lines, 2)
        self.linux_link = self._get_content(lines, 3)
        self.mac_arm_link = self._get_content(lines, 4)

        # Update push button activation
        self.pushButton_windows.setDisabled(self.windows_link=='disabled' or self.windows_link=="")
        self.pushButton_mac_intel.setDisabled(self.MAC_link=='disabled' or self.MAC_link=="")
        self.pushButton_linux.setDisabled(self.linux_link=='disabled' or self.linux_link=="")
        self.pushButton_mac_arm.setDisabled(self.mac_arm_link=='disabled' or self.mac_arm_link=="")

        # Update label
        self.label_released_version.setText(str(self.snooz_released_version))


    def _load_embedded_image(self):
        """Load the embedded base64 image data into snooz_label."""
        from ui.assets.art_image_data import SNOOZ_LOGO_IMAGE_BASE64
        
        image_bytes = base64.b64decode(SNOOZ_LOGO_IMAGE_BASE64)
        pixmap = QPixmap()
        pixmap.loadFromData(image_bytes)
        self.snooz_label.setPixmap(pixmap)


    # Called when the user clicks on the download windows button
    def download_windows_slot(self):
        # Specify the URL you want to open
        if not self.windows_link == 'disabled':
            url = QUrl(self.windows_link)
            QDesktopServices.openUrl(url)


    # Called when the user clicks on the download windows button
    def download_MAC_slot(self):
        # Specify the URL you want to open
        if not self.MAC_link == 'disabled':
            url = QUrl(self.MAC_link)
            QDesktopServices.openUrl(url)


    # Called when the user clicks on the download windows button
    def download_Linux_slot(self):
        # Specify the URL you want to open
        if not self.linux_link == 'disabled':
            url = QUrl(self.linux_link)
            QDesktopServices.openUrl(url)

    def download_mac_arm_slot(self):
        
        if not self.mac_arm_link == 'disabled':
            url = QUrl(self.mac_arm_link)
            QDesktopServices.openUrl(url)

    def _get_content(self, lines, index):
        return lines[index] if len(lines) > index else ""