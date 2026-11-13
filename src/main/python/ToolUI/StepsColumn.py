"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2026
See the file LICENCE for full license details.
"""
"""
    Column of the steps of a tool (left of StepsWidget).

    The steps are listed in order, each one with a numbered circle, joined by a
    line. The current step is open in place: its description and the links to its
    sub-steps are shown under its name. A step shows whether it was already visited
    and, after Run, whether its settings have to be fixed (red).

    The colors come from the style sheet (qproperty-accentColor...).
"""
from qtpy import QtCore, QtGui, QtWidgets
from qtpy.QtCore import Property

from commons.fonts import set_text_style, text_style_font

# Look of a step, also the "stepState" property of its row and labels (style sheet)
CURRENT = "current"
VISITED = "visited"
TODO = "todo"
ERROR = "error"

# Object names used by the style sheet
ROW_NAME = "step_row"
NAME_LABEL_NAME = "step_name"
COUNT_LABEL_NAME = "step_count"
ERROR_LABEL_NAME = "step_error_note"

ERROR_NOTE = "Check the settings of this step"


def _set_state_property(widget, state):
    """ Set the stepState property of a widget and apply the style sheet again. """
    if widget.property("stepState") != state:
        widget.setProperty("stepState", state)
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.update()


class _StepMarker(QtWidgets.QWidget):
    """ Circle of a step (its number, "i" for the page of the tool, "!" when its
    settings have to be fixed) and the line joining it to the steps above and below.
    """
    WIDTH = 34
    SIZE = 24
    # Center of the circle from the top of the row: on the first line of the name
    CENTER_Y = 20

    def __init__(self, column, index, text):
        super().__init__()
        self._column = column
        self._index = index
        self._text = text
        self.setFixedWidth(self.WIDTH)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)

    def paintEvent(self, event):
        column = self._column
        state = column.step_state(self._index)
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        cx, cy, r = self.width() / 2, self.CENTER_Y, self.SIZE / 2

        # Lines to the steps above and below: in the accent color between steps
        # already reached
        reached = column.step_reached
        for draw, other, y0, y1 in ((self._index > 0, self._index - 1, 0, cy - r - 2),
                                    (self._index < column.count() - 1, self._index + 1, cy + r + 2, self.height())):
            if draw and y1 > y0:
                color = column.accentColor if reached(self._index) and reached(other) else column.lineColor
                painter.setPen(QtGui.QPen(color, 2))
                painter.drawLine(QtCore.QPointF(cx, y0), QtCore.QPointF(cx, y1))

        circle = QtCore.QRectF(cx - r, cy - r, 2 * r, 2 * r).adjusted(1, 1, -1, -1)
        text = self._text
        if state == ERROR:
            pen, brush, text_color, text = QtGui.QPen(column.errorColor, 2), column.errorColor, column.onAccentColor, "!"
        elif state == CURRENT:
            pen, brush, text_color = QtGui.QPen(column.accentColor, 2), column.accentColor, column.onAccentColor
        elif state == VISITED:
            pen, brush, text_color = QtGui.QPen(column.accentColor, 2), column.surfaceColor, column.accentColor
        else:
            pen, brush, text_color = QtGui.QPen(column.lineColor, 1.5), column.surfaceColor, column.mutedColor
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawEllipse(circle)
        font = text_style_font("small")
        font.setWeight(QtGui.QFont.Weight.DemiBold)
        painter.setFont(font)
        painter.setPen(text_color)
        painter.drawText(circle, QtCore.Qt.AlignmentFlag.AlignCenter, text)


class _StepRow(QtWidgets.QFrame):
    """ A step in the column: its circle, its name and, when it is the current step,
    its details (description, sub-steps). Clicking it opens the step.
    """
    clicked = QtCore.Signal(int)

    def __init__(self, column, index, name, details, number):
        super().__init__()
        self.setObjectName(ROW_NAME)
        self.setAccessibleName(name)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_Hover)
        self.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self._index = index
        self.details = details
        self.name = name

        layout = QtWidgets.QHBoxLayout(self)
        # No margin above and below: the line of the circles runs from row to row
        layout.setContentsMargins(4, 0, 8, 0)
        layout.setSpacing(8)
        self.marker = _StepMarker(column, index, "i" if number is None else str(number))
        layout.addWidget(self.marker)

        texts = QtWidgets.QVBoxLayout()
        texts.setContentsMargins(0, 6, 0, 6)
        texts.setSpacing(4)
        self.name_label = QtWidgets.QLabel(name)
        self.name_label.setObjectName(NAME_LABEL_NAME)
        self.name_label.setWordWrap(True)
        self.name_label.setMinimumHeight(28)
        texts.addWidget(self.name_label)
        # Where the user is in the tool: written under the name of the tool
        self.count_label = None
        if number is None:
            self.count_label = QtWidgets.QLabel()
            self.count_label.setObjectName(COUNT_LABEL_NAME)
            set_text_style(self.count_label, "small")
            self.count_label.hide()
            texts.addWidget(self.count_label)
        self.error_label = QtWidgets.QLabel(ERROR_NOTE)
        self.error_label.setObjectName(ERROR_LABEL_NAME)
        self.error_label.setWordWrap(True)
        set_text_style(self.error_label, "small")
        self.error_label.hide()
        texts.addWidget(self.error_label)
        if details is not None:
            details.setParent(self)
            details.hide()
            texts.addWidget(details)
        layout.addLayout(texts, 1)
        self._is_tool_page = number is None

    def refresh(self, state, is_current):
        """ Show the row in the look of its step. """
        _set_state_property(self, CURRENT if is_current else state)
        _set_state_property(self.name_label, state)
        # Bold: the page of the tool, the current step and a step to fix
        bold = self._is_tool_page or is_current or state == ERROR
        set_text_style(self.name_label, "h3" if bold else "body")
        self.error_label.setVisible(state == ERROR)
        if self.details is not None:
            self.details.setVisible(is_current)
        self.setCursor(QtCore.Qt.CursorShape.ArrowCursor if is_current
                       else QtCore.Qt.CursorShape.PointingHandCursor)
        self.marker.update()

    def mousePressEvent(self, event):
        # Accepted: the row gets the release
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            event.accept()
        else:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton and self.rect().contains(event.pos()):
            self.clicked.emit(self._index)
        else:
            super().mouseReleaseEvent(event)

    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key.Key_Space, QtCore.Qt.Key.Key_Return, QtCore.Qt.Key.Key_Enter):
            self.clicked.emit(self._index)
        else:
            super().keyPressEvent(event)


class StepsColumn(QtWidgets.QScrollArea):
    """ The steps of a tool, in order, the current one open in place.

    Same use as the QToolBox it replaces: count, currentIndex, setCurrentIndex,
    currentWidget, widget and the currentChanged signal.
    """
    currentChanged = QtCore.Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._rows = []
        self._current = -1
        self._visited = set()
        self._errors = set()
        self._accent_color = QtGui.QColor("#2f5a93")
        self._line_color = QtGui.QColor("#9daec4")
        self._error_color = QtGui.QColor("#dc2626")
        self._surface_color = QtGui.QColor("#ffffff")
        self._muted_color = QtGui.QColor("#5b6b82")
        self._on_accent_color = QtGui.QColor("#ffffff")

        self.setWidgetResizable(True)
        self.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        content = QtWidgets.QWidget()
        content.setObjectName("steps_column_content")
        self._layout = QtWidgets.QVBoxLayout(content)
        self._layout.setContentsMargins(8, 10, 8, 10)
        self._layout.setSpacing(0)
        self._layout.addStretch(1)
        self.setWidget(content)

    # Colors, set by the style sheet (qproperty-accentColor...)
    def _getter(name):
        return lambda self: getattr(self, name)

    def _setter(name):
        def set_color(self, color):
            setattr(self, name, QtGui.QColor(color))
            for row in self._rows:
                row.marker.update()
        return set_color

    accentColor = Property(QtGui.QColor, _getter("_accent_color"), _setter("_accent_color"))
    lineColor = Property(QtGui.QColor, _getter("_line_color"), _setter("_line_color"))
    errorColor = Property(QtGui.QColor, _getter("_error_color"), _setter("_error_color"))
    surfaceColor = Property(QtGui.QColor, _getter("_surface_color"), _setter("_surface_color"))
    mutedColor = Property(QtGui.QColor, _getter("_muted_color"), _setter("_muted_color"))
    onAccentColor = Property(QtGui.QColor, _getter("_on_accent_color"), _setter("_on_accent_color"))
    del _getter, _setter

    # Steps
    def add_step(self, name, details=None, number=None):
        """ Add a step: its name, the widget shown under it when it is the current step
        (description, sub-steps) and its number (None for the page of the tool).
        """
        index = len(self._rows)
        row = _StepRow(self, index, name, details, number)
        row.clicked.connect(self.setCurrentIndex)
        self._layout.insertWidget(index, row)
        self._rows.append(row)
        if self._current < 0:
            self._current = 0
            self._visited.add(0)
        self._refresh()
        return index

    def count(self):
        return len(self._rows)

    def currentIndex(self):
        return self._current

    def setCurrentIndex(self, index):
        if not 0 <= index < len(self._rows) or index == self._current:
            return
        self._current = index
        self._visited.add(index)
        self._refresh()
        self.ensureWidgetVisible(self._rows[index], 0, 0)
        self.currentChanged.emit(index)

    def currentWidget(self):
        return self.widget(self._current)

    def widget(self, index):
        """ The details widget of a step. """
        if 0 <= index < len(self._rows):
            return self._rows[index].details
        return None

    def step_name(self, index):
        return self._rows[index].name

    # Steps to fix (Run)
    def set_error(self, index):
        """ The settings of a step have to be fixed: it is shown in red until
        clear_errors (next Run). """
        if 0 <= index < len(self._rows):
            self._errors.add(index)
            self._refresh()

    def clear_errors(self):
        if self._errors:
            self._errors.clear()
            self._refresh()

    # State of the steps (circles)
    def step_state(self, index):
        if index in self._errors:
            return ERROR
        if index == self._current:
            return CURRENT
        if index in self._visited:
            return VISITED
        return TODO

    def step_reached(self, index):
        """ Whether the user already opened a step (or has to fix it). """
        return index in self._visited or index in self._errors

    def _refresh(self):
        numbered = [row for row in self._rows if not row._is_tool_page]
        for index, row in enumerate(self._rows):
            row.refresh(self.step_state(index), index == self._current)
            if row.count_label is not None and numbered:
                current_row = self._rows[self._current] if self._current >= 0 else None
                if current_row in numbered:
                    text = f"Step {numbered.index(current_row) + 1} of {len(numbered)}"
                else:
                    text = f"{len(numbered)} steps"
                row.count_label.setText(text)
                row.count_label.show()
