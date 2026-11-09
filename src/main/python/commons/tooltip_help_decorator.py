"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2026
See the file LICENCE for full license details.

Automatically show a small "?" cue on widgets that expose a tooltip.

Placement strategy (content-aware, not full-width):
1. If the control lives in a QFormLayout, put the cue after the row label.
2. Else if the control is compact/small and a label follows it in the same
   row (e.g. alias ">" + channel name), put the cue after that label text.
3. Else if the control is compact/small, put the cue outside above/left of it
   so the control and neighboring text stay visible.
4. Else if it is a label, checkbox or radio with text, put the cue just after
   that text.
5. Else put the cue on the control using a content-sized width anchor so
   expanding fields do not push it to the far end of the line.

A cue after a text gets room of its own: the widget is made wider (a
right-aligned label gets an indent instead), so the cue never covers the
text, whatever the font.
"""
from qtpy import QtCore, QtGui, QtWidgets

from commons.fonts import text_style_rules

try:
    import shiboken6
except ImportError:  # pragma: no cover - non-PySide6 runtimes
    shiboken6 = None

_OPT_OUT_PROPERTY = "snoozNoHelpIcon"
# Set on push buttons showing the cue, the style sheet keeps their text clear of it.
_HAS_MARK_PROPERTY = "snoozHasHelpMark"
_MARK_OBJECT_NAME = "snoozTooltipHelpMark"
_MARK_ATTR = "_snooz_help_mark"
_WATCHED_ATTR = "_snooz_help_watch"
_MARK_SIZE = 14
_MARK_GAP = 3
_COMPACT_THRESHOLD = 28
# Expanding editors: keep the cue near the usable field area, not line-end.
_MAX_FIELD_ANCHOR = 220

_MARK_STYLE = f"""
QLabel#snoozTooltipHelpMark {{
    color: #b0b0b0;
    background-color: #f7f7f7;
    border: 1px solid #c8c8c8;
    border-radius: 7px;
    {text_style_rules("small")}
    font-weight: 700;
    font-style: normal;
    padding: 1px 0px 0px 0px; /* centers the "?" of the Snooz font in the circle */
}}
"""

# Prefer concrete slider type: QAbstractSlider also matches transient QScrollBars.
_HELPABLE_TYPES = (
    QtWidgets.QAbstractButton,
    QtWidgets.QSlider,
    QtWidgets.QAbstractSpinBox,
    QtWidgets.QComboBox,
    QtWidgets.QLineEdit,
    QtWidgets.QKeySequenceEdit,
    QtWidgets.QLabel,
)


def _widget_alive(widget):
    """True when the Python wrapper still owns a live Qt C++ object."""
    if widget is None:
        return False
    if shiboken6 is not None:
        return shiboken6.isValid(widget)
    try:
        widget.objectName()
        return True
    except RuntimeError:
        return False


class _TooltipHelpFilter(QtCore.QObject):
    """Reposition marks and decorate widgets created after the first pass."""

    def __init__(self, root):
        super().__init__(root)
        self._root = root
        self._marks = {}
        self._pending_scan = False

    def eventFilter(self, watched, event):
        event_type = event.type()

        if event_type == QtCore.QEvent.Type.ChildAdded:
            child = event.child()
            # Alias UIs rebuild often; ignore transient scrollbars/marks.
            if (
                isinstance(child, QtWidgets.QWidget)
                and not isinstance(child, QtWidgets.QScrollBar)
                and _widget_alive(child)
                and child.objectName() != _MARK_OBJECT_NAME
            ):
                self._watch(child)
                self._schedule_scan()
            return False

        mark = self._marks.get(id(watched))
        if mark is None:
            return False
        if not _widget_alive(mark):
            self._marks.pop(id(watched), None)
            return False

        if event_type in (
            QtCore.QEvent.Type.Resize,
            QtCore.QEvent.Type.Move,
            QtCore.QEvent.Type.Show,
        ):
            _reposition_help_mark(mark)
        elif event_type == QtCore.QEvent.Type.Hide:
            mark.hide()
        elif event_type == QtCore.QEvent.Type.Destroy:
            self._marks.pop(id(watched), None)
            target = getattr(mark, "_snooz_target", None)
            if (
                _widget_alive(target)
                and getattr(target, _MARK_ATTR, None) is mark
            ):
                setattr(target, _MARK_ATTR, None)
            if _widget_alive(mark):
                mark.deleteLater()
        return False

    def _watch(self, widget):
        if not _widget_alive(widget):
            return
        if widget.objectName() == _MARK_OBJECT_NAME:
            return
        if isinstance(widget, QtWidgets.QScrollBar):
            return
        if getattr(widget, _WATCHED_ATTR, False):
            return
        setattr(widget, _WATCHED_ATTR, True)
        widget.installEventFilter(self)
        for child in widget.findChildren(QtWidgets.QWidget):
            if not _widget_alive(child):
                continue
            if child.objectName() == _MARK_OBJECT_NAME:
                continue
            if isinstance(child, QtWidgets.QScrollBar):
                continue
            if getattr(child, _WATCHED_ATTR, False):
                continue
            setattr(child, _WATCHED_ATTR, True)
            child.installEventFilter(self)

    def _schedule_scan(self):
        if self._pending_scan:
            return
        self._pending_scan = True
        QtCore.QTimer.singleShot(0, self._run_pending_scan)

    def _run_pending_scan(self):
        self._pending_scan = False
        if _widget_alive(self._root):
            _scan_and_decorate(self._root, self)


def decorate_tooltip_help_marks(root):
    """Attach a small "?" mark to every helpable descendant that has a tooltip.

    Safe to call more than once: already decorated widgets are skipped.
    Opt out with ``widget.setProperty("snoozNoHelpIcon", True)``.
    Late-created widgets under ``root`` are picked up automatically.
    """
    if not _widget_alive(root) or not isinstance(root, QtWidgets.QWidget):
        return

    filter_obj = getattr(root, "_snooz_help_filter", None)
    if not isinstance(filter_obj, _TooltipHelpFilter):
        filter_obj = _TooltipHelpFilter(root)
        root._snooz_help_filter = filter_obj

    filter_obj._watch(root)
    _scan_and_decorate(root, filter_obj)


def _scan_and_decorate(root, filter_obj):
    if not _widget_alive(root):
        return
    widgets = [root]
    widgets.extend(root.findChildren(QtWidgets.QWidget))
    for widget in widgets:
        try:
            if _should_decorate(widget):
                _attach_help_mark(widget, filter_obj)
        except RuntimeError:
            # Widget deleted while alias UI / layouts were rebuilding.
            continue


def _should_decorate(widget):
    if not _widget_alive(widget):
        return False
    if not isinstance(widget, _HELPABLE_TYPES):
        return False
    if widget.objectName() == _MARK_OBJECT_NAME:
        return False
    if widget.property(_OPT_OUT_PROPERTY):
        return False
    if getattr(widget, _MARK_ATTR, None) is not None:
        return False

    tip = widget.toolTip()
    if tip is None or not str(tip).strip():
        return False
    return True


def _is_compact_widget(widget):
    """True when an in-widget cue would cover the control (alias ">" etc.)."""
    max_w = widget.maximumWidth()
    max_h = widget.maximumHeight()
    if 0 < max_w <= _COMPACT_THRESHOLD or 0 < max_h <= _COMPACT_THRESHOLD:
        return True

    width = widget.width() if widget.width() > 0 else widget.sizeHint().width()
    height = widget.height() if widget.height() > 0 else widget.sizeHint().height()
    if width <= _COMPACT_THRESHOLD or height <= _COMPACT_THRESHOLD:
        return True

    if isinstance(widget, QtWidgets.QAbstractButton) and not isinstance(
        widget, (QtWidgets.QCheckBox, QtWidgets.QRadioButton)
    ):
        text = (widget.text() or "").strip()
        if len(text) <= 2:
            return True
    return False


def _attach_help_mark(widget, filter_obj):
    if getattr(widget, _MARK_ATTR, None) is not None:
        return

    tip = str(widget.toolTip()).strip()
    host, outside = _resolve_mark_host(widget)
    mark = QtWidgets.QLabel("?", host)
    mark.setObjectName(_MARK_OBJECT_NAME)
    mark.setFixedSize(_MARK_SIZE, _MARK_SIZE)
    mark.setAlignment(QtCore.Qt.AlignCenter)
    mark.setToolTip(tip)
    mark.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
    mark.setFocusPolicy(QtCore.Qt.NoFocus)
    mark.setStyleSheet(_MARK_STYLE)
    mark._snooz_target = widget
    mark._snooz_host = host
    mark._snooz_outside = outside
    mark.raise_()

    if isinstance(widget, QtWidgets.QLineEdit) and host is widget and not outside:
        margins = widget.textMargins()
        widget.setTextMargins(
            margins.left(),
            margins.top(),
            max(margins.right(), _MARK_SIZE + 2),
            margins.bottom(),
        )

    if isinstance(widget, QtWidgets.QPushButton) and host is widget and not outside:
        # The style sheet gives these buttons room for the cue; polish again
        # so the new property is taken into account.
        widget.setProperty(_HAS_MARK_PROPERTY, True)
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.updateGeometry()

    setattr(widget, _MARK_ATTR, mark)
    filter_obj._marks[id(widget)] = mark
    if not getattr(widget, _WATCHED_ATTR, False):
        setattr(widget, _WATCHED_ATTR, True)
        widget.installEventFilter(filter_obj)

    if host is not widget:
        filter_obj._marks[id(host)] = mark
        if not getattr(host, _WATCHED_ATTR, False):
            setattr(host, _WATCHED_ATTR, True)
            host.installEventFilter(filter_obj)

    _reposition_help_mark(mark)
    mark.show()


def _resolve_mark_host(widget):
    """Choose where the cue lives. Returns (host, outside_widget)."""
    label = _form_label_for(widget)
    if isinstance(label, QtWidgets.QLabel):
        return label, False

    if _is_compact_widget(widget):
        # Alias rows are "> + channel name + line edit". Prefer the channel
        # label so the cue reads as "EEG ?" instead of covering the name.
        sibling_label = _following_label_sibling(widget)
        if isinstance(sibling_label, QtWidgets.QLabel):
            return sibling_label, False
        parent = widget.parentWidget()
        if parent is not None:
            return parent, True

    return widget, False


def _following_label_sibling(widget): # Take care of this function, there would be some special cases later that might need to be handled here.
    """Return the QLabel that follows ``widget`` in the same layout row, if any."""
    parent = widget.parentWidget()
    if parent is None or parent.layout() is None:
        return None
    return _following_label_in_layout(parent.layout(), widget)


def _following_label_in_layout(layout, widget):
    if layout is None:
        return None

    for index in range(layout.count()):
        item = layout.itemAt(index)
        if item is None:
            continue
        if item.widget() is widget:
            for next_index in range(index + 1, layout.count()):
                next_item = layout.itemAt(next_index)
                if next_item is None:
                    continue
                next_widget = next_item.widget()
                if isinstance(next_widget, QtWidgets.QLabel):
                    return next_widget
                if next_widget is not None:
                    return None
            return None
        child_layout = item.layout()
        if child_layout is not None:
            found = _following_label_in_layout(child_layout, widget)
            if found is not None:
                return found
    return None


def _form_label_for(widget):
    parent = widget.parentWidget()
    while parent is not None:
        label = _label_for_field_in_layout(parent.layout(), widget)
        if label is not None:
            return label
        parent = parent.parentWidget()
    return None


def _label_for_field_in_layout(layout, widget):
    if layout is None:
        return None
    if isinstance(layout, QtWidgets.QFormLayout):
        label = layout.labelForField(widget)
        if label is not None:
            return label
    for index in range(layout.count()):
        item = layout.itemAt(index)
        if item is None:
            continue
        child_layout = item.layout()
        if child_layout is not None:
            label = _label_for_field_in_layout(child_layout, widget)
            if label is not None:
                return label
    return None


def _reposition_help_mark(mark):
    if not _widget_alive(mark):
        return
    widget = getattr(mark, "_snooz_target", None)
    host = getattr(mark, "_snooz_host", None)
    if not _widget_alive(widget) or not _widget_alive(host):
        return

    if mark.parentWidget() is not host:
        mark.setParent(host)

    x, y = _content_anchor(widget, host, getattr(mark, "_snooz_outside", False))
    x = max(0, min(x, max(0, host.width() - _MARK_SIZE)))
    y = max(0, min(y, max(0, host.height() - _MARK_SIZE)))
    mark.setFixedSize(_MARK_SIZE, _MARK_SIZE)
    mark.move(x, y)
    mark.raise_()
    if widget.isVisible():
        mark.show()


def _content_anchor(widget, host, outside):
    """Return mark top-left in host coordinates."""
    if outside and host is not widget:
        top_left = widget.mapTo(host, QtCore.QPoint(0, 0))
        # Prefer above the control so we do not cover the next sibling text.
        x = top_left.x() + max(0, (widget.width() - _MARK_SIZE) // 2)
        y = top_left.y() - _MARK_SIZE - _MARK_GAP
        if y < 0:
            # Fall back to the left of the control.
            x = top_left.x() - _MARK_SIZE - _MARK_GAP
            y = top_left.y() + max(0, (widget.height() - _MARK_SIZE) // 2)
        return x, y

    if isinstance(host, QtWidgets.QLabel) and host.text().strip():
        # The label of a field, or the label carrying the tooltip: the cue goes
        # right after its text (a label showing a picture has no text).
        return _after_label_text(host)

    if isinstance(widget, (QtWidgets.QCheckBox, QtWidgets.QRadioButton)) and widget.text():
        option = QtWidgets.QStyleOptionButton()
        option.initFrom(widget)
        option.text = widget.text()
        if isinstance(widget, QtWidgets.QCheckBox):
            element = QtWidgets.QStyle.SubElement.SE_CheckBoxContents
        else:
            element = QtWidgets.QStyle.SubElement.SE_RadioButtonContents
        contents = widget.style().subElementRect(element, option, widget)
        text = widget.text().split("\n")[0].rstrip()
        x = contents.left() + widget.fontMetrics().horizontalAdvance(text) + _MARK_GAP
        _make_room(widget, x + _MARK_SIZE)
        y = max(0, (widget.height() - _MARK_SIZE) // 2)
        return x, y

    if widget.width() <= _MAX_FIELD_ANCHOR:
        anchor_width = widget.width()
    else:
        hint = max(widget.minimumSizeHint().width(), 96)
        if isinstance(widget, QtWidgets.QAbstractButton) and widget.text():
            hint = max(hint, widget.fontMetrics().horizontalAdvance(widget.text()) + 24)
        anchor_width = min(widget.width(), max(hint, _MAX_FIELD_ANCHOR))

    x = max(0, anchor_width - _MARK_SIZE - 2)
    y = 2
    return x, y


def _make_room(widget, width):
    """Make the widget at least ``width`` wide, beyond a maximum set in Qt Designer if needed."""
    if widget.minimumWidth() < width:
        widget.setMinimumWidth(width)
    if widget.maximumWidth() < width:
        widget.setMaximumWidth(width)


def _after_label_text(label):
    """Cue position right after the text of a label (first line), with room made for it."""
    needed = _MARK_GAP + _MARK_SIZE
    end, middle, room = _label_text_end(label)
    if room < needed and not label.wordWrap():
        alignment = QtWidgets.QStyle.visualAlignment(label.layoutDirection(), label.alignment())
        if alignment & QtCore.Qt.AlignRight:
            # The text stays against the right edge: indent it from there.
            label.setIndent(_effective_indent(label) + needed - room)
        else:
            missing = needed - room
            if alignment & QtCore.Qt.AlignHCenter:
                missing *= 2
            _make_room(label, label.width() + missing)
        end, middle, room = _label_text_end(label)
    x = round(end) + _MARK_GAP
    y = round(middle - _MARK_SIZE / 2)
    return x, y


def _effective_indent(label):
    """Indent of the text of a label, as QLabel computes it when none is set."""
    if label.indent() >= 0:
        return label.indent()
    if label.frameWidth() > 0:
        return max(0, label.fontMetrics().horizontalAdvance("x") // 2 - label.margin())
    return 0


def _label_text_end(label):
    """Where the visible text of a label ends on its first line.

    Returns the x after the last character (trailing spaces excluded), the middle
    of the line and the room left between that x and the right edge of the text area.
    """
    margin = label.margin()
    rect = label.contentsRect().adjusted(margin, margin, -margin, -margin)
    text = label.text()
    rich = label.textFormat() == QtCore.Qt.RichText or (
        label.textFormat() == QtCore.Qt.AutoText and QtCore.Qt.mightBeRichText(text)
    )
    if rich or label.wordWrap():
        document = QtGui.QTextDocument()
        document.setDefaultFont(label.font())
        document.setDocumentMargin(0)
        if rich:
            document.setHtml(text)
        else:
            document.setPlainText(text)
        if label.wordWrap():
            document.setTextWidth(rect.width())
        text_height = document.size().height()  # lays the text out
        line = document.firstBlock().layout().lineAt(0)
        width = visible = line.naturalTextWidth()
        line_height = line.height()
    else:
        lines = text.split("\n")
        metrics = label.fontMetrics()
        width = metrics.horizontalAdvance(lines[0])
        visible = metrics.horizontalAdvance(lines[0].rstrip())
        line_height = metrics.height()
        text_height = metrics.lineSpacing() * (len(lines) - 1) + metrics.height()

    alignment = QtWidgets.QStyle.visualAlignment(label.layoutDirection(), label.alignment())
    indent = _effective_indent(label)
    right = rect.right() + 1
    if alignment & QtCore.Qt.AlignRight:
        left = right - indent - width
    elif alignment & QtCore.Qt.AlignHCenter:
        left = rect.left() + (rect.width() - width) / 2
    else:
        left = rect.left() + indent
    if alignment & QtCore.Qt.AlignTop:
        top = rect.top()
    elif alignment & QtCore.Qt.AlignBottom:
        top = rect.bottom() + 1 - text_height
    else:
        top = rect.top() + (rect.height() - text_height) / 2
    end = left + visible
    return end, top + line_height / 2, right - end
