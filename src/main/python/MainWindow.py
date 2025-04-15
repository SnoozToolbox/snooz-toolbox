"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    MainWindow of Snooz

    This is the main window of the software. It initializes and handles the 
    menus, the managers, the main view, etc.
"""

from qtpy import QtWidgets
from qtpy import QtCore
from qtpy import QtGui
from qtpy.QtCore import QUrl
from qtpy.QtGui import QDesktopServices

import config
from DisclaimerDialog import DisclaimerDialog
from ui.Ui_MainWindow import Ui_MainWindow
from Managers.Managers import Managers
from Managers.EndpointManager import MenuEndpointHandler
from Managers.EndpointManager import FileMenuEndpointHandler
from Managers.StyleManager import Palette, Style
from ConverterUtils import convert_package_to_v100
from widgets.LogsDialog import LogsDialog
from widgets.AboutDialog import AboutDialog
from widgets.SettingsDialog import SettingsDialog
from widgets.RecentWidget import RecentWidget

import Snooz_logo_rc

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    """Main Window."""
    def __init__(self, *args, **kwargs):
        r"""Entry point of the user interface """
        super(MainWindow, self).__init__(*args, **kwargs)

        # Setup the Ui_MainWindow generated by QtDesigner
        self.setupUi(self)
        self.content_tabWidget.setTabVisible(0, False)
        self.content_tabWidget.setTabVisible(1, False)
        self.content_tabWidget.setTabVisible(2, False)
        self.content_tabWidget.setTabVisible(3, False)

        # Init all managers. Managers are the brain of the software. Most of the
        # responsibilities are in the managers. Look into each of them to learn more.
        self._managers = Managers(self)
        self._managers.initialize()

        # Init the UI
        font = self._init_fonts()
        self._init_themes()
        self._init_homepage(font)

        # Warn the user this is a beta version
        self._display_disclaimer()

        # Most information and error messages are handled here.
        self._managers.pub_sub_manager.subscribe(self, "show_error_message")
        self._managers.pub_sub_manager.subscribe(self, "show_info_message")
        self._managers.pub_sub_manager.subscribe(self, "maximize")
        self._managers.pub_sub_manager.subscribe(self, "minimize")
        
        self._managers.navigation_manager.show_home()

    # UI callbacks
    def preferences_clicked(self):
        """ Preferences button clicked, open the settings dialog """
        settings = SettingsDialog(self._managers, self)
        settings.exec_()

    def run_clicked(self):
        """ Run button clicked, execute the current process """
        self._managers.process_manager.run_current_process()

    def new_process_clicked(self):
        """ New process button clicked, create a new process """
        self._managers.process_manager.new_process()
        self._managers.navigation_manager.show_process()

    def open_process_clicked(self):
        """ Open process button clicked, open a process """
        self._managers.process_manager.open_process()
        self._managers.navigation_manager.show_process()

    def close_process_clicked(self):
        """ Close process button clicked, close the current process """
        self._managers.process_manager.close_process()
        self._managers.navigation_manager.show_home()

    def save_process_clicked(self):
        """ Save process button clicked, save the current process """
        self._managers.process_manager.save_process()

    def save_process_as_clicked(self):
        """ Save process as button clicked, save the current process as """
        self._managers.process_manager.save_process_as()

    def load_workspace_clicked(self):
        """ Load workspace button clicked, load the current workspace """
        success = self._managers.tool_manager.load_workspace()
        if success:
            self._managers.navigation_manager.show_tool()

    def convert_file_clicked(self):
        """ Convert file button clicked, convert the current file """
        convert_package_to_v100(self)
        QtWidgets.QMessageBox.information(self, "Info", "Conversion done")

    def logs_clicked(self):
        """ Logs button clicked, open the logs dialog """
        about = LogsDialog(self._managers.log_manager)
        about.exec_()

    def about_clicked(self):
        """ About button clicked, open the about dialog """
        about = AboutDialog()
        about.exec_()

    def documentation_clicked(self):
        """ Documentation button clicked, open the documentation """
        QDesktopServices.openUrl(QUrl(config.DOCUMENTATION_URL))


    def home_clicked(self):
        """ Home button clicked, open the home page """
        self._managers.navigation_manager.show_home()
    
    def app_clicked(self):
        """ App button clicked, open the app page """
        self._managers.navigation_manager.show_app()

    def close_app_clicked(self):
        """ App close button clicked, close the current app """
        self._managers.app_manager.close_app()
        self._managers.navigation_manager.show_home()

    def tool_clicked(self):
        """ Tool button clicked, open the tool page """
        self._managers.navigation_manager.show_tool()

    def process_clicked(self):
        """ Process button clicked, open the process page """
        self._managers.navigation_manager.show_process()

    def open_clicked(self):
        """ Open button clicked, open a file.
        
        The file menu handler will open the file if there is an APP that is hooked to it.
        """
        handler = self._managers.endpoint_manager.get_handler(FileMenuEndpointHandler.ENDPOINT_NAME)
        handler.open_file()

    def on_topic_update(self, topic, message, sender):
        if topic == "show_error_message":
            message = f"Error: {message}"
            QtWidgets.QMessageBox.critical(self, "Error", message)
        elif topic == "show_info_message":
            message = f"{message}"
            QtWidgets.QMessageBox.information(self, "Info", message)
        elif topic == "minimize":
            self.showMinimized()
        elif topic == "maximize":
            self.showNormal()

    # Private functions
    def _init_themes(self):
        """ Init the themes """
        light_style_name = "Light"
        light_palette = Palette()
        light_palette.grid_background = QtGui.QColor(247, 250, 251)
        light_palette.grid_line = QtGui.QColor(181,196,201)
        light_palette.node_selection = QtGui.QColor(30, 129, 169)
        light_palette.node_background_activated = QtGui.QColor(195, 211, 217)
        light_palette.node_background_deactivated = QtGui.QColor(102,102,102)
        light_palette.node_background_bypass = QtGui.QColor(247,250,251)
        light_palette.node_border = QtGui.QColor(102, 102, 102)
        light_palette.node_text = QtGui.QColor(31,31,31)
        light_palette.node_socket_border = QtGui.QColor(102, 102, 102)
        light_palette.node_socket_background = QtGui.QColor(206, 208, 209)

        light_style = Style(light_style_name, light_palette, ":/themes/light/stylesheet.qss")
        self._managers.style_manager.register_style(light_style)
        self._managers.style_manager.set_default_style(light_style_name)
        self._managers.style_manager.load_user_style()

    def _init_homepage(self, font):
        """ Init the homepage """
        # Define the style as Roboto-Regular.ttf
        #font = QtGui.QFont("Roboto-Regular", 10)
        # Define the label
        snooz_label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(snooz_label.sizePolicy().hasHeightForWidth())
        snooz_label.setSizePolicy(sizePolicy)
        snooz_label.setMinimumSize(QtCore.QSize(0, 0))
        snooz_label.setMaximumSize(QtCore.QSize(250, 125))
        snooz_label.setPixmap(QtGui.QPixmap(u":/Snooz_logo/Snooz_logo.png"))
        snooz_label.setScaledContents(True)
        snooz_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        snooz_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        getting_started_label = QtWidgets.QLabel("<h1>Hello Snooz user!</h1><h2>Start by navigating the menu.</h2><p>The tools installed within Snooz are divided into three categories:</p><ol><li><strong>Preprocessing:</strong>&nbsp;Includes importers/converters/extractors and the artifact detection tool.</li><li><strong>Processing:</strong>&nbsp;Includes sleep stages analyses, event detectors, and power spectral analysis.</li><li><strong>Postprocessing:</strong>&nbsp;Includes secondary analyses such as performance evaluation of detectors,<br />transposition of cohort reports, and slow wave events analysis.</li></ol><p>If you are new to Snooz, we recommend beginning with the Preprocessing category.<br />The Preprocessing category includes importers, converters, extractors, and the artifact detection tool.</p><p>Once your PSG files are compatible with Snooz, proceed to the Processing category.<br />The Processing category includes sleep analyses, event detectors, and power spectral analysis.</p><p>The Postprocessing category includes secondary analyses, such as performance evaluation of detectors,<br />transposition of cohort reports, and slow wave events analysis.</p><p><strong>Viewers</strong></p><p>The only available Viewer is the Oximeter, which allows you to select bad sections to generate <br />a valid Oxygen Saturation Report. The Oximeter is an application that operates within Snooz.</p><h2>To update Snooz</h2><p>Navigate to Help -&gt; About Snooz</p><p>(macOS) Navigate to Snooz -&gt; About</p>")
        getting_started_label.setFont(font)
        self.right_pane_layout.addWidget(snooz_label)
        self.right_pane_layout.addWidget(getting_started_label)
        self.right_pane_layout.addStretch()

        # Init the recently used widget
        self._recent_widget = RecentWidget(self._managers)
        self.left_pane_layout.addWidget(self._recent_widget)
        self.left_pane_layout.addStretch(1)

    def _init_fonts(self):
        fonts = [
            "fonts/Roboto/Roboto-Regular.ttf"
        ]
        # Load fonts
        for font_path in fonts:
            release_notes_path = config.app_context.get_resource(font_path)
            fontId = QtGui.QFontDatabase.addApplicationFont(release_notes_path)
            if fontId < 0:
                print('font not loaded')
        
        families = QtGui.QFontDatabase.applicationFontFamilies(0)
        font = QtGui.QFont(families[0])
        font.setPointSize(config.font_size)
        QtWidgets.QApplication.setFont(font)
        return font


    def _display_disclaimer(self):
        """ Display the beta version disclaimer """
        skip = self._managers.settings_manager.get_setting(config.settings.skip_beta_disclaimer, None)
        if skip is None:
            disclaimer_dialog = DisclaimerDialog(self._managers.settings_manager)
            disclaimer_dialog.exec_()


# Notes to update the home page for Snooz

# <h1>Hello Snooz user!</h1>
# <h2>Start by navigating the menu.</h2>
# <p>The tools installed within Snooz are divided into three categories:</p>
# <ol>
# <li><strong>Preprocessing:</strong>&nbsp;Includes importers/converters/extractors and the artifact detection tool.</li>
# <li><strong>Processing:</strong>&nbsp;Includes sleep stages analyses, event detectors, and power spectral analysis.</li>
# <li><strong>Postprocessing:</strong>&nbsp;Includes secondary analyses such as performance evaluation of detectors,<br />transposition of cohort reports, and slow wave events analysis.</li>
# </ol>
# <p>If you are new to Snooz, we recommend beginning with the Preprocessing category.<br />The Preprocessing category includes importers, converters, extractors, and the artifact detection tool.</p>
# <p>Once your PSG files are compatible with Snooz, proceed to the Processing category.<br />The Processing category includes sleep analyses, event detectors, and power spectral analysis.</p>
# <p>The Postprocessing category includes secondary analyses, such as performance evaluation of detectors,<br />transposition of cohort reports, and slow wave events analysis.</p>
# <p><strong>Viewers</strong></p>
# <p>The only available Viewer is the Oximeter, which allows you to select bad sections to generate <br />a valid Oxygen Saturation Report. The Oximeter is an application that operates within Snooz.</p>
# <h2>To update Snooz</h2>
# <p>Navigate to Help -&gt; About Snooz</p>
# <p>(macOS)Navigate to Snooz -&gt; About Snooz</p>