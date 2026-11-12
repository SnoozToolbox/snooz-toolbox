import json
import math

from qtpy import QtCore
from qtpy import QtGui
from qtpy import QtWidgets
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QGraphicsScene, QGraphicsView
from qtpy.QtGui import QPainter

from commons.fonts import set_text_style
from commons.theme_helpers import glyph_pixmap


class _ZoomControls(QtWidgets.QFrame):
    """ Small bar in the bottom right corner of the canvas: zoom out, zoom level
    (click: 100 %), zoom in, fit the process in the view.
    """
    _BUTTON_SIZE = 28
    _ICON_SIZE = 16

    def __init__(self, view, palette):
        super().__init__(view)
        self.setAccessibleName("canvas_zoom")
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(0)
        icon_color = palette.node_text_muted

        def button(tooltip, slot, glyph=None):
            widget = QtWidgets.QToolButton(self)
            widget.setFocusPolicy(Qt.NoFocus)
            widget.setToolTip(tooltip)
            widget.setFixedHeight(self._BUTTON_SIZE)
            if glyph is not None:
                widget.setFixedWidth(self._BUTTON_SIZE)
                widget.setIcon(QtGui.QIcon(glyph_pixmap(glyph, icon_color, self._ICON_SIZE)))
                widget.setIconSize(QtCore.QSize(self._ICON_SIZE, self._ICON_SIZE))
            widget.clicked.connect(slot)
            layout.addWidget(widget)
            return widget

        button("Zoom out (Ctrl + minus)", view.zoom_out, "minus")
        self._level = button("Zoom 100 % (Ctrl + 0)", view.reset_zoom)
        self._level.setAccessibleName("canvas_zoom_level")
        set_text_style(self._level, "small")
        # Wide enough for the largest level, so the bar keeps its width
        self._level.setFixedWidth(self._level.fontMetrics().horizontalAdvance("400 %") + 14)
        button("Zoom in (Ctrl + plus)", view.zoom_in, "plus")
        separator = QtWidgets.QFrame(self)
        separator.setAccessibleName("canvas_zoom_separator")
        separator.setFixedSize(1, self._BUTTON_SIZE - 10)
        layout.addSpacing(2)
        layout.addWidget(separator)
        layout.addSpacing(2)
        button("Fit the process in the view (F)", view.fit_to_nodes, "fit")
        self.show_zoom(1.0)

    def show_zoom(self, zoom):
        self._level.setText(f"{round(zoom * 100)} %")


class _EmptyHint(QtWidgets.QWidget):
    """ Text in the middle of an empty canvas: how to start a process. It lets the
    mouse through, so a module can be dropped on it.
    """
    def __init__(self, view):
        super().__init__(view)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)
        title = QtWidgets.QLabel("Drag a module from the Module Library and drop it here", self)
        title.setAccessibleName("canvas_hint_title")
        text = QtWidgets.QLabel("Then connect the modules: drag from a port to the port of another module.", self)
        text.setAccessibleName("canvas_hint_text")
        set_text_style(text, "small")
        for label in (title, text):
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)
        self.hide()


class ProcessGraphicsView(QtWidgets.QGraphicsView):
    # Limits of the zoom (1 = 100 %). The largest processes of the tools need about
    # 17 % to be seen whole on a small laptop screen.
    MINIMUM_ZOOM = 0.1
    MAXIMUM_ZOOM = 4.0
    # Zoom of one step of the mouse wheel (with Ctrl) or of the zoom buttons
    _ZOOM_STEP = 1.25
    # Room around the nodes when the process is fitted in the view (pixels of the scene)
    _FIT_MARGIN = 50
    # Distance of the zoom controls from the corner of the canvas
    _CONTROLS_MARGIN = 10

    def __init__(self, parent=None):
        super(ProcessGraphicsView, self).__init__(parent)

        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        self.setRenderHints(
            QtGui.QPainter.Antialiasing
            | QtGui.QPainter.SmoothPixmapTransform
            | QtGui.QPainter.TextAntialiasing
            | QtGui.QPainter.SmoothPixmapTransform
        )

        self._grid_color = QtGui.QColor(200, 200, 200)
        self._grid_major_color = QtGui.QColor(200, 200, 200)
        self.setBackgroundBrush(Qt.white)
        self.centerOn(0, 0)

        self._zoom_controls = None
        self._empty_hint = _EmptyHint(self)
        # Fit the process in the view when the canvas gets its size, until the user
        # zooms or moves the view
        self._fit_pending = False
        for scroll_bar in (self.horizontalScrollBar(), self.verticalScrollBar()):
            scroll_bar.actionTriggered.connect(self._stop_fit_on_resize)

    def set_palette(self, palette):
        """ Colors of the canvas, from the palette of the current style. """
        self._grid_color = palette.grid_line
        self._grid_major_color = palette.grid_line_major
        self.setBackgroundBrush(palette.grid_background)
        if self._zoom_controls is None:
            self._zoom_controls = _ZoomControls(self, palette)
            self._zoom_controls.show_zoom(self.zoom())
            self._place_overlays()

    def setScene(self, scene):
        if self.scene() is not None:
            try:
                self.scene().changed.disconnect(self._update_empty_hint)
            except (RuntimeError, TypeError):
                pass
        super().setScene(scene)
        if scene is not None:
            scene.changed.connect(self._update_empty_hint)
        self._update_empty_hint()

    # Zoom ------------------------------------------------------------------------

    def zoom(self):
        """ Zoom of the canvas, 1 = 100 %. """
        return self.transform().m11()

    def set_zoom(self, zoom, under_mouse=False):
        """ Zoom the canvas, within the limits. The center of the view stays in place,
        or the point under the mouse (mouse wheel).
        """
        zoom = max(self.MINIMUM_ZOOM, min(self.MAXIMUM_ZOOM, zoom))
        factor = zoom / self.zoom()
        if abs(factor - 1) > 1e-9:
            anchor = self.transformationAnchor()
            if not under_mouse:
                self.setTransformationAnchor(QGraphicsView.AnchorViewCenter)
            self.scale(factor, factor)
            self.setTransformationAnchor(anchor)
        if self._zoom_controls is not None:
            self._zoom_controls.show_zoom(self.zoom())

    def zoom_in(self):
        self._fit_pending = False
        self.set_zoom(self.zoom() * self._ZOOM_STEP)

    def zoom_out(self):
        self._fit_pending = False
        self.set_zoom(self.zoom() / self._ZOOM_STEP)

    def reset_zoom(self):
        self._fit_pending = False
        self.set_zoom(1.0)

    def fit_to_nodes(self):
        """ Zoom and center the view on all the nodes of the process. A small process
        is not enlarged beyond 100 %, a large one not reduced below the minimum zoom.
        """
        scene = self.scene()
        rect = QtCore.QRectF()
        for node in getattr(scene, "nodes", []):
            rect = rect.united(node.sceneBoundingRect())
        if rect.isNull():
            return
        rect.adjust(-self._FIT_MARGIN, -self._FIT_MARGIN, self._FIT_MARGIN, self._FIT_MARGIN)
        viewport = self.viewport().rect()
        zoom = min(viewport.width() / rect.width(), viewport.height() / rect.height(), 1.0)
        self.set_zoom(zoom)
        self.centerOn(rect.center())

    def fit_when_shown(self):
        """ Fit the process in the view as soon as the canvas has its size (opening a
        process), and again when the window is resized, until the user zooms or moves
        the view.
        """
        self._fit_pending = True
        if self.isVisible():
            self.fit_to_nodes()

    def _stop_fit_on_resize(self, *args):
        self._fit_pending = False

    def wheelEvent(self, event):
        # Check if the control key is pressed
        if event.modifiers() & Qt.ControlModifier:
            delta = event.angleDelta().y()
            if delta != 0:
                self._fit_pending = False
                step = self._ZOOM_STEP if delta > 0 else 1 / self._ZOOM_STEP
                self.set_zoom(self.zoom() * step, under_mouse=True)
            event.accept()
        else:
            self._fit_pending = False
            super().wheelEvent(event)

    def keyPressEvent(self, event):
        # Not while a widget of the canvas (the window of a node) takes the keys
        scene = self.scene()
        if scene is not None and scene.focusItem() is None and self._zoom_key(event):
            event.accept()
            return
        super().keyPressEvent(event)

    def _zoom_key(self, event):
        """ F: fit the process in the view. Ctrl + plus, minus, 0: zoom in, out, 100 %. """
        key = event.key()
        modifiers = event.modifiers() & ~(Qt.KeypadModifier | Qt.ShiftModifier)
        if modifiers == Qt.NoModifier and key == Qt.Key_F:
            self._fit_pending = False
            self.fit_to_nodes()
        elif modifiers == Qt.ControlModifier and key in (Qt.Key_Plus, Qt.Key_Equal):
            self.zoom_in()
        elif modifiers == Qt.ControlModifier and key in (Qt.Key_Minus, Qt.Key_Underscore):
            self.zoom_out()
        elif modifiers == Qt.ControlModifier and key == Qt.Key_0:
            self.reset_zoom()
        else:
            return False
        return True

    def mousePressEvent(self, event):
        self._fit_pending = False
        super().mousePressEvent(event)

    # Size and overlays -----------------------------------------------------------

    def showEvent(self, event):
        super().showEvent(event)
        self._place_overlays()
        if self._fit_pending:
            self.fit_to_nodes()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._place_overlays()
        if self._fit_pending and self.isVisible():
            self.fit_to_nodes()

    def _place_overlays(self):
        """ Zoom controls in the bottom right corner of the canvas, the hint of an
        empty canvas in its middle. They are children of the view, not of the
        canvas: the canvas moves its children when it scrolls.
        """
        canvas = self.viewport().geometry()
        if self._zoom_controls is not None:
            size = self._zoom_controls.sizeHint()
            self._zoom_controls.setGeometry(canvas.right() + 1 - self._CONTROLS_MARGIN - size.width(),
                                            canvas.bottom() + 1 - self._CONTROLS_MARGIN - size.height(),
                                            size.width(), size.height())
            self._zoom_controls.raise_()
        hint = self._empty_hint.sizeHint()
        width = min(hint.width(), canvas.width())
        self._empty_hint.setGeometry(canvas.left() + (canvas.width() - width) // 2,
                                     canvas.top() + (canvas.height() - hint.height()) // 2,
                                     width, hint.height())

    def _update_empty_hint(self, *args):
        scene = self.scene()
        empty = scene is not None and not scene.items()
        # isVisibleTo: the canvas itself may not be shown yet (the process is loading)
        if empty != self._empty_hint.isVisibleTo(self):
            self._empty_hint.setVisible(empty)
            if empty:
                self._place_overlays()
                self._empty_hint.raise_()


    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)

        def draw_grid(grid_step):
            window_rect = self.rect()
            top_left = self.mapToScene(window_rect.topLeft())
            bottom_right = self.mapToScene(window_rect.bottomRight())
            left =      math.floor(top_left.x() / grid_step - 0.5)
            right =     math.floor(bottom_right.x() / grid_step + 1.0)
            bottom =    math.floor(top_left.y() / grid_step - 0.5)
            top =       math.floor(bottom_right.y() / grid_step + 1.0)

            # vertical lines
            lines = [
                QtCore.QLineF(xi * grid_step, bottom * grid_step, 
                    xi * grid_step, top * grid_step)
                for xi in range(int(left), int(right) + 1)
            ]

            # horizontal lines
            lines.extend(
                [QtCore.QLineF(left * grid_step, yi * grid_step, 
                    right * grid_step, yi * grid_step)
                 for yi in range(int(bottom), int(top) + 1)
                 ]
            )

            painter.drawLines(lines)

        # Draw grid. Zoomed out, the fine lines would only gray the canvas. Far out,
        # the grid looks as at 100 %, ten times larger.
        zoom = self.transform().m11()
        if zoom >= 0.5:
            fine_pen = QtGui.QPen(self._grid_color, 0.5)
            painter.setPen(fine_pen)
            draw_grid(15)
        elif zoom < 0.2:
            painter.setPen(QtGui.QPen(self._grid_color, 0.5 / zoom))
            draw_grid(150)

        major_step = 150 if zoom >= 0.2 else 1500
        fine_pen = QtGui.QPen(self._grid_major_color, 1.0 if zoom >= 0.2 else 1.0 / zoom)
        painter.setPen(fine_pen)
        draw_grid(major_step)

        # Draw origin circle
        brush = QtGui.QBrush(self._grid_major_color)
        painter.setBrush(brush)
        painter.drawEllipse(QtCore.QPointF(0,0), 3, 3)
