"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2026
See the file LICENCE for full license details.

Home page of Snooz: the logo, the analysis workflow, the recent files and the help links.
Its look is in the HOME PAGE section of the style sheet.
"""
from qtpy import QtCore, QtGui, QtWidgets

import config
from commons.fonts import text_label
from commons.theme_helpers import SnoozLogo
from widgets.RecentWidget import RecentWidget

# Steps of the analysis workflow: title of the menu category and description.
_WORKFLOW_STEPS = (
    ("Preprocessing", "Inspect, import, convert and extract your PSG files. "
                      "Includes the automated sleep staging and the artifact detection."),
    ("Processing", "Sleep stage analyses, event detectors and power spectral analysis."),
    ("Postprocessing", "Performance evaluation of detectors, transposition of cohort reports "
                       "and slow wave events analysis."),
)
_FEEDBACK_URL = "https://form.jotform.com/240234589570258"
# The content is centered and not wider than this on large screens.
_MAX_CONTENT_WIDTH = 1200
_SIDE_MARGIN = 24


class HomeWidget(QtWidgets.QScrollArea):
    """ Home page of Snooz. """

    def __init__(self, managers, main_window, parent:QtWidgets.QWidget=None):
        super().__init__(parent)
        self._managers = managers
        self._main_window = main_window
        self._workflow_steps = []

        self.setObjectName("home_scroll_area")
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setWidgetResizable(True)

        page = QtWidgets.QWidget()
        page.setObjectName("home_page")
        self._page_layout = QtWidgets.QVBoxLayout(page)
        self._page_layout.setContentsMargins(_SIDE_MARGIN, 20, _SIDE_MARGIN, 24)
        self._page_layout.setSpacing(0)

        self._page_layout.addLayout(self._create_header())
        self._page_layout.addSpacing(28)
        self._page_layout.addWidget(text_label("Your analysis workflow", "h1"))
        self._page_layout.addSpacing(4)
        self._page_layout.addWidget(_muted_label(
            "New to Snooz? Start with Preprocessing to make your PSG files compatible with Snooz, "
            "then run your analyses in Processing."))
        self._page_layout.addSpacing(12)
        self._page_layout.addWidget(self._create_workflow())
        self._page_layout.addSpacing(32)
        self._page_layout.addLayout(self._create_lists())
        self._page_layout.addStretch(1)

        self.setWidget(page)
        self._managers.pub_sub_manager.subscribe(self, "menus_changed")

    def on_topic_update(self, topic, message, sender):
        if topic == "menus_changed":
            self.refresh()

    def showEvent(self, event):
        super().showEvent(event)
        self.refresh()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        side = max(_SIDE_MARGIN, (self.viewport().width() - _MAX_CONTENT_WIDTH) // 2)
        margins = self._page_layout.contentsMargins()
        if side != margins.left():
            self._page_layout.setContentsMargins(side, margins.top(), side, margins.bottom())

    def refresh(self):
        """ Update the number of tools of the workflow steps. """
        for step in self._workflow_steps:
            step.refresh()

    def _create_header(self):
        """ The logo and the main actions. """
        layout = QtWidgets.QHBoxLayout()
        layout.setSpacing(10)
        title_layout = QtWidgets.QVBoxLayout()
        title_layout.setSpacing(8)
        title_layout.addWidget(SnoozLogo(240))
        title_layout.addWidget(_muted_label(
            f"Open-source toolbox for sleep PSG analysis  ·  {_version_text()}", wrap=False))
        layout.addLayout(title_layout)
        layout.addStretch(1)
        for text, primary, callback in (
                ("Load a workspace", True, self._main_window.load_workspace_clicked),
                ("Documentation", False, self._main_window.documentation_clicked)):
            button = QtWidgets.QPushButton(text)
            button.setObjectName("home_header_button")
            if primary:
                button.setProperty("variant", "primary")
            button.setCursor(QtCore.Qt.PointingHandCursor)
            button.clicked.connect(lambda checked=False, callback=callback: callback())
            layout.addWidget(button, 0, QtCore.Qt.AlignVCenter)
        return layout

    def _create_workflow(self):
        """ The three steps of the workflow, in one card. """
        card = QtWidgets.QFrame()
        card.setObjectName("home_card")
        layout = QtWidgets.QHBoxLayout(card)
        layout.setContentsMargins(24, 20, 24, 18)
        layout.setSpacing(16)
        for number, (title, description) in enumerate(_WORKFLOW_STEPS, start=1):
            step = _WorkflowStep(number, title, description, self._main_window.menuBar)
            self._workflow_steps.append(step)
            layout.addWidget(step, 1)
            if number < len(_WORKFLOW_STEPS):
                arrow = QtWidgets.QLabel("➜")
                arrow.setObjectName("home_arrow")
                layout.addWidget(arrow)
        return card

    def _create_lists(self):
        """ The recent files and the help links, side by side. """
        layout = QtWidgets.QHBoxLayout()
        layout.setSpacing(48)

        recent_layout = QtWidgets.QVBoxLayout()
        recent_widget = RecentWidget(self._managers)
        recent_widget.layout().setContentsMargins(0, 0, 0, 0)
        recent_layout.addWidget(recent_widget)
        recent_layout.addStretch(1)
        layout.addLayout(recent_layout, 1)

        help_layout = QtWidgets.QVBoxLayout()
        help_layout.setSpacing(10)
        help_layout.addWidget(text_label("Learn and get help", "h2"))
        for title, description, callback in (
                ("Example data", "Download example PSG files to try the tools.",
                 self._main_window.data_clicked),
                ("Give feedback", "Report a problem or suggest an improvement.",
                 self._open_feedback),
                ("Check for updates", "See the installed version and download the latest one.",
                 self._main_window.about_clicked)):
            link = _HelpLink(title, description)
            link.clicked.connect(callback)
            help_layout.addWidget(link)
        help_layout.addStretch(1)
        layout.addLayout(help_layout, 1)
        return layout

    def _open_feedback(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(_FEEDBACK_URL))


class _WorkflowStep(QtWidgets.QWidget):
    """ Step of the analysis workflow: a menu category and its number of tools. """

    def __init__(self, number:int, title:str, description:str, menu_bar:QtWidgets.QMenuBar,
                 parent:QtWidgets.QWidget=None):
        super().__init__(parent)
        self._title = title
        self._menu_bar = menu_bar
        self.setMinimumWidth(180)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        header_layout = QtWidgets.QHBoxLayout()
        badge = QtWidgets.QLabel(str(number))
        badge.setObjectName("home_badge")
        badge.setFixedSize(34, 34)
        badge.setAlignment(QtCore.Qt.AlignCenter)
        header_layout.addWidget(badge)
        header_layout.addSpacing(6)
        header_layout.addWidget(text_label(title, "h2"), 1)
        layout.addLayout(header_layout)
        layout.addWidget(_muted_label(description))
        layout.addStretch(1)

        footer_layout = QtWidgets.QHBoxLayout()
        self._count_label = QtWidgets.QLabel()
        self._count_label.setObjectName("home_chip")
        footer_layout.addWidget(self._count_label)
        footer_layout.addStretch(1)
        self._browse_button = QtWidgets.QPushButton("Browse tools  ›")
        self._browse_button.setObjectName("home_browse_button")
        self._browse_button.setCursor(QtCore.Qt.PointingHandCursor)
        self._browse_button.clicked.connect(self._show_menu)
        footer_layout.addWidget(self._browse_button)
        layout.addLayout(footer_layout)
        self.refresh()

    def refresh(self):
        """ Show the number of tools of the menu category. """
        menu = self._menu()
        count = _count_items(menu) if menu is not None else 0
        self._count_label.setText("1 tool" if count == 1 else f"{count} tools")
        self._browse_button.setEnabled(count > 0)

    def _menu(self):
        for action in self._menu_bar.actions():
            if action.menu() is not None and action.text() == self._title:
                return action.menu()
        return None

    def _show_menu(self):
        menu = self._menu()
        if menu is not None:
            menu.popup(self._browse_button.mapToGlobal(QtCore.QPoint(0, self._browse_button.height())))


class _HelpLink(QtWidgets.QFrame):
    """ Clickable item of the help list: a title above a description. """
    clicked = QtCore.Signal()

    def __init__(self, title:str, description:str, parent:QtWidgets.QWidget=None):
        super().__init__(parent)
        self.setCursor(QtCore.Qt.PointingHandCursor)
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        title_label = QtWidgets.QLabel(f"{title}  ›")
        title_label.setObjectName("home_link_title")
        layout.addWidget(title_label)
        layout.addWidget(_muted_label(description))

    def mousePressEvent(self, event):
        # Accepted, so the release comes back to the link.
        if event.button() == QtCore.Qt.LeftButton:
            event.accept()
        else:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.rect().contains(event.position().toPoint()):
            self.clicked.emit()
        else:
            super().mouseReleaseEvent(event)


def _muted_label(text:str, wrap:bool=True):
    label = QtWidgets.QLabel(text)
    label.setObjectName("home_muted")
    label.setWordWrap(wrap)
    return label


def _count_items(menu:QtWidgets.QMenu):
    """ Number of items of a menu, submenus included. """
    count = 0
    for action in menu.actions():
        if action.menu() is not None:
            count += _count_items(action.menu())
        elif not action.isSeparator():
            count += 1
    return count


def _version_text():
    if config.is_dev:
        return "development version"
    if config.release_label:
        return f"version {config.version} ({config.release_label})"
    return f"version {config.version}"
