"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2026
See the file LICENCE for full license details.

Window shown while Snooz starts and loads its packages.
"""
import sys

from qtpy import QtCore, QtGui, QtWidgets

import config
from commons.theme_helpers import SnoozLogo
from Managers.StyleManager import load_tokens


class SplashScreen(QtWidgets.QWidget):
    """ Window shown while Snooz starts.

    Subscribe it to the "loading_package" topic while the packages load: it
    shows the name of each package.
    """

    def __init__(self, parent:QtWidgets.QWidget=None):
        super().__init__(parent, QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint)
        # The style sheet of the application is not active yet: the colors come from the tokens.
        self._tokens = load_tokens(":/themes/light/tokens.json")
        # Round corners need a transparent window, not available on Linux without a compositor.
        self._rounded = not sys.platform.startswith("linux")
        if self._rounded:
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFixedSize(560, 300)

        # The Snooz font, from the same file as MainWindow._init_fonts.
        font = QtGui.QFont()
        try:
            font_id = QtGui.QFontDatabase.addApplicationFont(
                config.app_context.get_resource("fonts/Roboto/Roboto-Regular.ttf"))
            if font_id >= 0:
                font = QtGui.QFont(QtGui.QFontDatabase.applicationFontFamilies(font_id)[0])
        except FileNotFoundError:
            pass
        font.setPointSize(12)
        self.setFont(font)
        small_font = QtGui.QFont(font)
        small_font.setPointSize(10)

        on_primary = self._tokens.get("on_primary", "#ffffff")
        self.setStyleSheet(
            f"QLabel {{ color: {on_primary}; background-color: transparent; }}"
            "QProgressBar { background-color: rgba(255, 255, 255, 60); border: 0px;"
            " border-radius: 3px; padding: 0px; }"
            f"QProgressBar::chunk {{ background-color: {on_primary}; border-radius: 3px; }}")

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 30)
        layout.addWidget(SnoozLogo(260, white=True), 0, QtCore.Qt.AlignHCenter)
        layout.addSpacing(8)
        # The fonts are set on each label: the inherited font is lost when the
        # application style changes while the packages load.
        tagline_label = QtWidgets.QLabel("Open-source toolbox for sleep PSG analysis")
        tagline_label.setFont(font)
        layout.addWidget(tagline_label, 0, QtCore.Qt.AlignHCenter)
        layout.addStretch(1)

        self._progress = QtWidgets.QProgressBar()
        self._progress.setRange(0, 100)
        self._progress.setTextVisible(False)
        self._progress.setFixedHeight(6)
        layout.addWidget(self._progress)

        status_layout = QtWidgets.QHBoxLayout()
        self._status_label = QtWidgets.QLabel()
        self._status_label.setFont(small_font)
        self._status_label.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        status_layout.addWidget(self._status_label, 1)
        version_label = QtWidgets.QLabel("Development version" if config.is_dev else f"Version {config.version}")
        version_label.setFont(small_font)
        status_layout.addWidget(version_label)
        layout.addLayout(status_layout)

        self.show_message("Starting…", 5)

        # Centered on the screen
        screen = QtGui.QGuiApplication.primaryScreen()
        if screen is not None:
            geometry = self.frameGeometry()
            geometry.moveCenter(screen.availableGeometry().center())
            self.move(geometry.topLeft())

    def on_topic_update(self, topic, message, sender):
        if topic == "loading_package":
            # The number of packages is not known in advance: each one fills part of what is left.
            value = self._progress.value()
            self.show_message(f"Loading packages…  {message}", value + (85 - value) * 0.3)

    def show_message(self, message:str, progress:float):
        """ Show a message and the progress (0 to 100), immediately. """
        self._status_label.setText(message)
        self._progress.setValue(int(progress))
        # Repainted now: the event loop is busy while Snooz starts.
        self.repaint()

    def finish(self):
        self.close()
        self.deleteLater()

    def paintEvent(self, event):
        # Dark blue, like the menu bar
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtGui.QColor(self._tokens.get("chrome", "#12306b")))
        radius = 16 if self._rounded else 0
        painter.drawRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
