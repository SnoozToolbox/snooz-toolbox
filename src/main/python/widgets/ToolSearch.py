"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2026
See the file LICENCE for full license details.

Search of the tools on the home page: a search box and, while it holds a text, the
list of the matching tools and apps (name, menu, version, description). A click or
Enter opens the tool, as its menu item does.
Its look is in the HOME PAGE section of the style sheet.
"""
from qtpy import QtCore, QtGui, QtWidgets

from commons.fonts import set_text_style, text_label
from commons.theme_helpers import glyph_pixmap
from Endpoints.EndpointHandlers.MenuEndpointHandler import MenuEndpointHandler

# Tools listed at most: the user types more letters to see the others
_MAX_RESULTS = 8
_MAX_WIDTH = 760


class _ToolRow(QtWidgets.QFrame):
    """ A tool found: its name, its menu and version, its description. """
    clicked = QtCore.Signal(int)
    hovered = QtCore.Signal(int)

    def __init__(self, index:int, item:dict, parent:QtWidgets.QWidget=None):
        super().__init__(parent)
        self.setObjectName("home_tool_row")
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_Hover)
        self._index = index

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 8, 12, 8)
        layout.setSpacing(2)
        header = QtWidgets.QHBoxLayout()
        header.setSpacing(10)
        name = text_label(item["label"], "h3")
        name.setObjectName("home_tool_name")
        header.addWidget(name)
        header.addStretch(1)
        category = QtWidgets.QLabel(item["category"])
        category.setObjectName("home_tool_chip")
        set_text_style(category, "small")
        header.addWidget(category)
        version = QtWidgets.QLabel(f"v{item['version']}")
        version.setObjectName("home_muted")
        set_text_style(version, "small")
        header.addWidget(version)
        layout.addLayout(header)
        if item["description"]:
            description = QtWidgets.QLabel(item["description"])
            description.setObjectName("home_muted")
            description.setWordWrap(True)
            layout.addWidget(description)

    def set_selected(self, selected:bool):
        if self.property("selected") != selected:
            self.setProperty("selected", selected)
            self.style().unpolish(self)
            self.style().polish(self)
            self.update()

    def enterEvent(self, event):
        super().enterEvent(event)
        self.hovered.emit(self._index)

    def mousePressEvent(self, event):
        # Accepted, so the release comes back to the row.
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            event.accept()
        else:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton and self.rect().contains(event.position().toPoint()):
            self.clicked.emit(self._index)
        else:
            super().mouseReleaseEvent(event)


class ToolSearch(QtWidgets.QWidget):
    """ Search box of the tools and the list of the tools found. """

    def __init__(self, managers, parent:QtWidgets.QWidget=None):
        super().__init__(parent)
        self._managers = managers
        self._items = []
        self._rows = []
        self._selected = -1
        self.setMaximumWidth(_MAX_WIDTH)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)

        self.search_box = QtWidgets.QLineEdit()
        self.search_box.setObjectName("home_search")
        self.search_box.setAccessibleName("Search a tool")
        self.search_box.setPlaceholderText("Search a tool: spindle, EDF, report...")
        self.search_box.setClearButtonEnabled(True)
        self.search_box.addAction(
            QtGui.QIcon(glyph_pixmap("search", self.palette().placeholderText().color(), 16)),
            QtWidgets.QLineEdit.ActionPosition.LeadingPosition)
        self.search_box.textChanged.connect(self._update_results)
        # Up, Down, Enter and Escape in the search box act on the list
        self.search_box.installEventFilter(self)
        layout.addWidget(self.search_box)

        self._results = QtWidgets.QFrame()
        self._results.setObjectName("home_search_results")
        self._results_layout = QtWidgets.QVBoxLayout(self._results)
        self._results_layout.setContentsMargins(6, 6, 6, 6)
        self._results_layout.setSpacing(0)
        self._results.hide()
        layout.addWidget(self._results)

    def refresh(self):
        """ The menus changed: search again. """
        if self.search_box.text().strip():
            self._update_results()

    def results(self):
        """ The labels of the tools listed. """
        return [item["label"] for item in self._items]

    def selected_index(self):
        return self._selected

    def eventFilter(self, watched, event):
        if watched is self.search_box and event.type() == QtCore.QEvent.Type.KeyPress:
            key = event.key()
            if key == QtCore.Qt.Key.Key_Down:
                self._select(self._selected + 1)
                return True
            if key == QtCore.Qt.Key.Key_Up:
                self._select(self._selected - 1)
                return True
            if key in (QtCore.Qt.Key.Key_Return, QtCore.Qt.Key.Key_Enter):
                self._open(self._selected)
                return True
            if key == QtCore.Qt.Key.Key_Escape and self.search_box.text():
                self.search_box.clear()
                return True
        return super().eventFilter(watched, event)

    def _menu_items(self):
        handler = self._managers.endpoint_manager.get_handler(MenuEndpointHandler.ENDPOINT_NAME)
        return handler.menu_items() if handler is not None else []

    def _update_results(self, *args):
        text = self.search_box.text().strip()
        words = text.lower().split()
        while self._results_layout.count():
            widget = self._results_layout.takeAt(0).widget()
            if widget is not None:
                # Taken out now: deleteLater alone leaves it drawn until Qt deletes it
                widget.hide()
                widget.setParent(None)
                widget.deleteLater()
        self._items, self._rows, self._selected = [], [], -1
        if not words:
            self._results.hide()
            return

        # The tools whose name holds all the words first, then those whose menu or
        # description does; in the order of the menus.
        found = []
        for item in self._menu_items():
            label = item["label"].lower()
            titles = f"{label} {item['category'].lower()}"
            everything = f"{titles} {item['description'].lower()}"
            for rank, searched in enumerate((label, titles, everything)):
                if all(word in searched for word in words):
                    found.append((rank, len(found), item))
                    break
        found.sort(key=lambda entry: entry[:2])
        self._items = [item for _, _, item in found[:_MAX_RESULTS]]

        for index, item in enumerate(self._items):
            row = _ToolRow(index, item)
            row.clicked.connect(self._open)
            row.hovered.connect(self._select)
            self._results_layout.addWidget(row)
            self._rows.append(row)
        note = None
        if not found:
            note = f"No tool found for \"{text}\". The menus above list all the tools."
        elif len(found) > _MAX_RESULTS:
            more = len(found) - _MAX_RESULTS
            note = f"{more} more tool{'s' if more > 1 else ''}: type more letters to see {'them' if more > 1 else 'it'}."
        if note:
            label = QtWidgets.QLabel(note)
            label.setObjectName("home_muted")
            label.setWordWrap(True)
            label.setContentsMargins(12, 8, 12, 8)
            self._results_layout.addWidget(label)
        self._results.show()
        self._select(0)

    def _select(self, index:int):
        if not self._rows:
            return
        self._selected = max(0, min(index, len(self._rows) - 1))
        for row_index, row in enumerate(self._rows):
            row.set_selected(row_index == self._selected)

    def _open(self, index:int):
        if not 0 <= index < len(self._items):
            return
        action = self._items[index]["action"]
        self.search_box.clear()
        action.trigger()
