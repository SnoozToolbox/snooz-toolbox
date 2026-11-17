"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2026
See the file LICENCE for full license details.
"""
from qtpy import QtCore, QtGui, QtWidgets

from commons.fonts import text_style_font
from commons.theme_helpers import paint_glyph


class NodeWindowProxy(QtWidgets.QGraphicsProxyWidget):
    """ Window of a node in the canvas of the process editor (double click on the node).

    Qt draws the frame of the windows of a scene like an old title bar (Qt logo,
    class name of the widget, small close button). This frame is drawn in the colors
    of the theme instead: a band with the name and the version of the module and a
    close button, a thin border with round corners and a soft shadow.
    Dragging the band moves the window; dragging the edges resizes it (Qt).
    """
    _TITLE_HEIGHT = 36
    # Outside the border: room for the shadow, also grabbed by the mouse to resize
    _OUTER = 6
    # Inside the border, around the widget: keeps it inside the round corners
    _PADDING = 3
    _RADIUS = 8
    _CLOSE_SIZE = 24
    _ICON_SIZE = 16

    def __init__(self, palette, subtitle="", parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self._palette = palette
        self._subtitle = subtitle
        self._close_hovered = False
        self._close_pressed = False
        self._set_frame_margins()

    @classmethod
    def title_height(cls):
        """ Height of the frame above the widget that is visible (band of the title, border). """
        return cls._TITLE_HEIGHT

    def _set_frame_margins(self):
        side = self._OUTER + 1 + self._PADDING
        self.setWindowFrameMargins(side, self._OUTER + self._TITLE_HEIGHT, side, side)

    def changeEvent(self, event):
        super().changeEvent(event)
        # Qt gives the frame the margins of its style back when the style changes
        if event.type() == QtCore.QEvent.StyleChange:
            self._set_frame_margins()

    def _window_rect(self):
        """ The visible window: the frame without the margin of the shadow. """
        return self.windowFrameRect().adjusted(self._OUTER, self._OUTER, -self._OUTER, -self._OUTER)

    def _close_rect(self):
        window = self._window_rect()
        top = window.top() + (self._TITLE_HEIGHT - self._CLOSE_SIZE) / 2
        return QtCore.QRectF(window.right() - 6 - self._CLOSE_SIZE, top, self._CLOSE_SIZE, self._CLOSE_SIZE)

    def paintWindowFrame(self, painter, option, widget=None):
        palette = self._palette
        window = self._window_rect()
        radius = self._RADIUS
        painter.save()
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        # Soft shadow, a little lower than the window
        painter.setPen(QtCore.Qt.NoPen)
        for spread, alpha in ((5, 0.15), (3.5, 0.3), (2, 0.5), (1, 0.8)):
            color = QtGui.QColor(palette.node_shadow)
            color.setAlphaF(color.alphaF() * alpha)
            painter.setBrush(color)
            painter.drawRoundedRect(window.adjusted(-spread, -spread + 1.5, spread, spread + 1.5),
                                    radius + spread, radius + spread)

        # Window, the band of the title on top
        outline = QtGui.QPainterPath()
        outline.addRoundedRect(window, radius, radius)
        painter.setBrush(palette.window_background)
        painter.drawPath(outline)
        title_band = QtCore.QRectF(window.left(), window.top(), window.width(), self._TITLE_HEIGHT)
        painter.save()
        painter.setClipPath(outline)
        painter.fillRect(title_band, palette.window_title)
        painter.restore()
        painter.setPen(QtGui.QPen(palette.node_separator, 1.0))
        line_y = title_band.bottom() - 0.5
        painter.drawLine(QtCore.QPointF(window.left() + 1, line_y), QtCore.QPointF(window.right() - 1, line_y))
        painter.setBrush(QtCore.Qt.NoBrush)
        painter.setPen(QtGui.QPen(palette.window_border, 1.0))
        painter.drawRoundedRect(window.adjusted(0.5, 0.5, -0.5, -0.5), radius - 0.5, radius - 0.5)

        # Name of the module, then its version
        close = self._close_rect()
        text_rect = QtCore.QRectF(window.left() + 12, title_band.top(), close.left() - 8 - window.left() - 12,
                                  self._TITLE_HEIGHT)
        title_font = text_style_font("body")
        title_font.setWeight(QtGui.QFont.DemiBold)
        title_metrics = QtGui.QFontMetricsF(title_font)
        title = title_metrics.elidedText(self.windowTitle(), QtCore.Qt.ElideRight, text_rect.width())
        painter.setFont(title_font)
        painter.setPen(palette.node_text)
        painter.drawText(text_rect, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, title)
        subtitle_left = title_metrics.horizontalAdvance(title) + 8
        if self._subtitle and subtitle_left < text_rect.width():
            subtitle_font = text_style_font("small")
            subtitle_rect = text_rect.adjusted(subtitle_left, 0, 0, 0)
            subtitle = QtGui.QFontMetricsF(subtitle_font).elidedText(
                self._subtitle, QtCore.Qt.ElideRight, subtitle_rect.width())
            painter.setFont(subtitle_font)
            painter.setPen(palette.node_text_muted)
            painter.drawText(subtitle_rect, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, subtitle)

        # Close button (pressed: only while the mouse is still over it)
        if self._close_hovered:
            painter.setPen(QtGui.QPen(palette.control_pressed, 1.0))
            painter.setBrush(palette.control_pressed if self._close_pressed else palette.control_hover)
            painter.drawRoundedRect(close.adjusted(0.5, 0.5, -0.5, -0.5), 6, 6)
        icon = QtCore.QRectF(0, 0, self._ICON_SIZE, self._ICON_SIZE)
        icon.moveCenter(close.center())
        paint_glyph(painter, "close", icon, palette.node_text if self._close_hovered else palette.node_text_muted)
        painter.restore()

    def _set_close_state(self, hovered, pressed):
        if (hovered, pressed) != (self._close_hovered, self._close_pressed):
            self._close_hovered = hovered
            self._close_pressed = pressed
            self.update(self._close_rect())

    def windowFrameEvent(self, event):
        kind = event.type()
        if kind in (QtCore.QEvent.GraphicsSceneHoverEnter, QtCore.QEvent.GraphicsSceneHoverMove):
            self._set_close_state(self._close_rect().contains(event.pos()), self._close_pressed)
        elif kind == QtCore.QEvent.GraphicsSceneHoverLeave:
            self._set_close_state(False, False)
        elif kind == QtCore.QEvent.GraphicsSceneMousePress and event.button() == QtCore.Qt.LeftButton \
                and self._close_rect().contains(event.pos()):
            # The move and the release come to mouseMoveEvent and mouseReleaseEvent
            self._set_close_state(True, True)
            event.accept()
            return True
        return super().windowFrameEvent(event)

    def mouseMoveEvent(self, event):
        if self._close_pressed:
            inside = self._close_rect().contains(event.pos())
            self._set_close_state(inside, True)
            return
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self._close_pressed:
            inside = self._close_rect().contains(event.pos())
            self._set_close_state(inside, False)
            if inside and event.button() == QtCore.Qt.LeftButton:
                self._set_close_state(False, False)
                self.close()
            return
        super().mouseReleaseEvent(event)
