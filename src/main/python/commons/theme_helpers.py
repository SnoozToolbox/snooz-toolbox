"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2026
See the file LICENCE for full license details.

Parts of the Snooz look that a style sheet cannot do: the navigation icons, the
logo, the round corners of the drop-down menus and tooltips, the cards around the
pictures of the tools and the color of the Windows title bar. Colors come from the
theme tokens (ui/themes/light/tokens.json).
"""
import base64
import functools
import math
import sys

from qtpy import QtCore, QtGui, QtSvg, QtWidgets

from commons.fonts import harmonize_widget_text
from ui.assets.art_image_data import SNOOZ_LOGO_SVG_BASE64

# Icons are drawn at this scale so they stay sharp on high resolution screens.
_IMAGE_SCALE = 3

# Windows 11 title bar attributes (DwmSetWindowAttribute).
_DWMWA_CAPTION_COLOR = 35
_DWMWA_TEXT_COLOR = 36

# Round corners of menus and tooltips need a transparent window: not on Linux, where
# the corners would be black without a compositing window manager.
_TRANSLUCENT_POPUPS = not sys.platform.startswith("linux")

# Padding + border of the QLabel[snoozPicture="true"] rule of the style sheet.
_PICTURE_FRAME = 7
# Images smaller than this (pixels) in both directions are icons, not pictures.
_MINIMUM_PICTURE_SIZE = 96
# QWIDGETSIZE_MAX of Qt (no maximum size), not available through qtpy.
_NO_MAXIMUM_SIZE = 16777215


# Navigation glyphs, thin lines on a 24 x 24 grid.
def _home_glyph(path):
    path.moveTo(3.5, 10.5)
    path.lineTo(12, 3.5)
    path.lineTo(20.5, 10.5)
    path.moveTo(5.5, 9)
    path.lineTo(5.5, 20.5)
    path.lineTo(18.5, 20.5)
    path.lineTo(18.5, 9)
    path.moveTo(10, 20.5)
    path.lineTo(10, 15)
    path.lineTo(14, 15)
    path.lineTo(14, 20.5)


def _tool_glyph(path):
    # Sliders: the settings of a tool.
    for y, knob in ((6, 15), (12, 8), (18, 13)):
        path.moveTo(3.5, y)
        path.lineTo(knob - 2.5, y)
        path.moveTo(knob + 2.5, y)
        path.lineTo(20.5, y)
        path.addEllipse(QtCore.QPointF(knob, y), 2.5, 2.5)


def _process_glyph(path):
    # Two connected nodes: the process editor.
    path.addRoundedRect(QtCore.QRectF(3.5, 3.5, 7, 7), 1.8, 1.8)
    path.addRoundedRect(QtCore.QRectF(13.5, 13.5, 7, 7), 1.8, 1.8)
    path.moveTo(7, 10.5)
    path.lineTo(7, 15)
    path.quadTo(7, 17, 9, 17)
    path.lineTo(13.5, 17)


def _app_glyph(path):
    # Signal trace: the viewer apps.
    path.moveTo(2.5, 12)
    path.lineTo(6, 12)
    path.lineTo(9, 4.5)
    path.lineTo(15, 19.5)
    path.lineTo(18, 12)
    path.lineTo(21.5, 12)


_GLYPHS = {
    "home": _home_glyph,
    "tool": _tool_glyph,
    "process": _process_glyph,
    "app": _app_glyph,
}


def nav_icon(glyph, tokens, size=22):
    """ Icon of a navigation button: a thin glyph, dark blue when the button is
    checked (the current page) and muted when it is not.
    """
    icon = QtGui.QIcon()
    for state, color in ((QtGui.QIcon.Off, tokens["text_muted"]), (QtGui.QIcon.On, tokens["chrome"])):
        icon.addPixmap(_glyph_pixmap(glyph, color, size), QtGui.QIcon.Normal, state)
    return icon


def _glyph_pixmap(glyph, color, size):
    pixels = size * _IMAGE_SCALE
    image = QtGui.QImage(pixels, pixels, QtGui.QImage.Format_ARGB32_Premultiplied)
    image.fill(QtCore.Qt.transparent)
    painter = QtGui.QPainter(image)
    painter.setRenderHint(QtGui.QPainter.Antialiasing)
    painter.scale(pixels / 24, pixels / 24)
    path = QtGui.QPainterPath()
    _GLYPHS[glyph](path)
    painter.setBrush(QtCore.Qt.NoBrush)
    painter.setPen(QtGui.QPen(QtGui.QColor(color), 1.75, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
    painter.drawPath(path)
    painter.end()

    pixmap = QtGui.QPixmap.fromImage(image)
    pixmap.setDevicePixelRatio(_IMAGE_SCALE)
    return pixmap


def _logo_renderer():
    """ Renderer of the vector image of the Snooz logo (ui/assets/Snooz_logo.svg). """
    return QtSvg.QSvgRenderer(QtCore.QByteArray(base64.b64decode(SNOOZ_LOGO_SVG_BASE64)))


@functools.lru_cache(maxsize=None)
def _logo_drawing_rect():
    """ The part of the view box of the logo covered by its drawing, plus a small
    margin for the antialiased edges (view box units).
    """
    renderer = _logo_renderer()
    view = renderer.viewBoxF()
    # One pixel per unit of the view box
    image = QtGui.QImage(math.ceil(view.width()), math.ceil(view.height()),
                         QtGui.QImage.Format_ARGB32_Premultiplied)
    image.fill(QtCore.Qt.transparent)
    painter = QtGui.QPainter(image)
    renderer.render(painter, QtCore.QRectF(0, 0, view.width(), view.height()))
    painter.end()
    drawing = QtGui.QRegion(QtGui.QBitmap.fromImage(image.createAlphaMask())).boundingRect()
    return QtCore.QRectF(drawing.translated(view.topLeft().toPoint())).adjusted(-2, -2, 2, 2)


def snooz_logo(width, white=False, ratio=1.0, margins=False):
    """ The Snooz logo, in its colors or in white (dark backgrounds), drawn from its
    vector image so it stays sharp at any size.

    The logo is cropped to its drawing, unless margins is True (whole image of the logo).
    The pixmap has the device pixel ratio given: drawn on a screen with this ratio,
    it is not scaled again (see SnoozLogo).
    """
    renderer = _logo_renderer()
    view = renderer.viewBoxF()
    source = view if margins else _logo_drawing_rect()
    scale = width * ratio / source.width()
    image = QtGui.QImage(round(width * ratio), round(source.height() * scale),
                         QtGui.QImage.Format_ARGB32_Premultiplied)
    image.fill(QtCore.Qt.transparent)
    painter = QtGui.QPainter(image)
    # The whole view box, placed so that the source part fills the image
    renderer.render(painter, QtCore.QRectF((view.x() - source.x()) * scale, (view.y() - source.y()) * scale,
                                           view.width() * scale, view.height() * scale))
    if white:
        painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceIn)
        painter.fillRect(image.rect(), QtCore.Qt.white)
    painter.end()
    pixmap = QtGui.QPixmap.fromImage(image)
    pixmap.setDevicePixelRatio(ratio)
    return pixmap


class SnoozLogo(QtWidgets.QWidget):
    """ The Snooz logo, drawn for the pixel ratio of its screen so it stays sharp. """

    def __init__(self, width, white=False, parent=None):
        super().__init__(parent)
        self._width = width
        self._white = white
        self._pixmap = snooz_logo(width, white, self.devicePixelRatioF())
        size = self._pixmap.deviceIndependentSize()
        self.setFixedSize(math.ceil(size.width()), math.ceil(size.height()))

    def paintEvent(self, event):
        ratio = self.devicePixelRatioF()
        # Drawn again when the window moves to a screen with another pixel ratio
        if self._pixmap.devicePixelRatio() != ratio:
            self._pixmap = snooz_logo(self._width, self._white, ratio)
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self._pixmap)
        painter.end()


class SnoozStyle(QtWidgets.QProxyStyle):
    """ The Fusion style, with transparent tooltip windows so they show the round
    corners of the QToolTip rule of the style sheet.

    It also shows every widget in the fonts and link color of Snooz when it is
    polished, before it is shown: the forms made before Inter, such as the ones of
    the packages, give sizes in points and other fonts, and links in the pure blue of
    Qt Designer (fonts.harmonize_widget_text).
    """

    def __init__(self):
        super().__init__("Fusion")

    def polish(self, *args):
        # The three overloads of polish (widget, application, palette) go to Fusion.
        result = super().polish(*args)
        widget = args[0]
        if isinstance(widget, QtWidgets.QWidget):
            try:
                harmonize_widget_text(widget)
            except Exception as error:  # A font must never prevent a page from showing
                print(f"fonts: the text of a {type(widget).__name__} was not converted: {error}")
        if _TRANSLUCENT_POPUPS and isinstance(widget, QtWidgets.QWidget) and widget.inherits("QTipLabel"):
            # A tooltip is polished when it is created, before its window exists. Like the
            # menus, it must be frameless: on Windows, the transparent pixels of a window
            # with a native frame are shown in black.
            widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            widget.setWindowFlags(widget.windowFlags() | QtCore.Qt.FramelessWindowHint
                                  | QtCore.Qt.NoDropShadowWindowHint)
        return result


def frame_pictures(root):
    """ Show the pictures of a page (QLabel with an image) in white cards.

    The white background of most pictures then belongs to the card instead of
    standing out from the page (QLabel[snoozPicture="true"] rule of the style sheet).
    The card goes around the picture, which keeps its own size: the layout of the
    page does not change (see _PictureCard).
    """
    for label in root.findChildren(QtWidgets.QLabel):
        pixmap = label.pixmap()
        if label.property("snoozPicture") or pixmap.isNull():
            continue
        if pixmap.width() < _MINIMUM_PICTURE_SIZE and pixmap.height() < _MINIMUM_PICTURE_SIZE:
            continue  # An icon, not a picture
        if not label.hasScaledContents():
            # The card goes around the picture: a maximum size set in Qt Designer grows with it.
            if label.maximumWidth() < _NO_MAXIMUM_SIZE:
                label.setMaximumWidth(label.maximumWidth() + 2 * _PICTURE_FRAME)
            if label.maximumHeight() < _NO_MAXIMUM_SIZE:
                label.setMaximumHeight(label.maximumHeight() + 2 * _PICTURE_FRAME)
        label.setProperty("snoozPicture", True)
        label.style().unpolish(label)
        label.style().polish(label)
        _PictureCard(label)


def _fitted(size, bounds):
    """ The size, made smaller to fit in the bounds if needed, keeping its proportions. """
    if size.width() <= bounds.width() and size.height() <= bounds.height():
        return size
    return size.scaled(bounds, QtCore.Qt.KeepAspectRatio)


def _layout_with(layout, widget):
    """ The layout holding the widget: the given layout or one of its nested layouts. """
    if layout.indexOf(widget) >= 0:
        return layout
    for index in range(layout.count()):
        child = layout.itemAt(index).layout()
        if child is not None:
            found = _layout_with(child, widget)
            if found is not None:
                return found
    return None


class _PictureCard(QtCore.QObject):
    """ Paints the picture of a label in its card (see frame_pictures).

    The picture is scaled once for the pixels of the screen, smoothly, so lines
    stay even. A label filling its area with its picture (scaled contents in Qt
    Designer) keeps doing so. The other ones are not wider than their picture,
    in the middle of their layout cell, and show it with its proportions.
    """

    def __init__(self, label):
        super().__init__(label)
        self._designer_maximum = label.maximumSize()
        self._fills = label.hasScaledContents()
        self._pixmap_key = None
        self._scaled = None
        self._scaled_key = None
        if not self._fills:
            label.setAlignment(QtCore.Qt.AlignCenter)
            parent = label.parentWidget()
            layout = _layout_with(parent.layout(), label) if parent is not None and parent.layout() is not None else None
            if layout is not None:
                alignment = layout.itemAt(layout.indexOf(label)).alignment()
                if not alignment & QtCore.Qt.AlignHorizontal_Mask:
                    layout.setAlignment(label, alignment | QtCore.Qt.AlignHCenter)
            self._update_width(label)
        label.installEventFilter(self)

    def _update_width(self, label):
        """ The card goes around the picture: the label is not wider than it. """
        pixmap = label.pixmap()
        self._pixmap_key = pixmap.cacheKey()
        frame = 2 * (_PICTURE_FRAME + label.margin())
        size = _fitted(pixmap.deviceIndependentSize().toSize(), self._designer_maximum - QtCore.QSize(frame, frame))
        label.setMaximumWidth(size.width() + frame)

    def eventFilter(self, label, event):
        if event.type() == QtCore.QEvent.Paint and not label.pixmap().isNull():
            if not self._fills and label.pixmap().cacheKey() != self._pixmap_key:
                self._update_width(label)  # The page shows another picture
            self._paint(label)
            return True
        return super().eventFilter(label, event)

    def _paint(self, label):
        pixmap = label.pixmap()
        margin = label.margin()
        rect = label.contentsRect().adjusted(margin, margin, -margin, -margin)
        if self._fills:
            size = rect.size()
        else:
            size = _fitted(pixmap.deviceIndependentSize().toSize(), rect.size())
        if size.isEmpty():
            return
        ratio = label.devicePixelRatioF()
        key = (pixmap.cacheKey(), size.width(), size.height(), ratio, label.isEnabled())
        if key != self._scaled_key:
            # Scaled once for the pixels of the screen, smoothly: lines stay even.
            self._scaled = pixmap.scaled(round(size.width() * ratio), round(size.height() * ratio),
                                         QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
            self._scaled.setDevicePixelRatio(ratio)
            if not label.isEnabled():
                option = QtWidgets.QStyleOption()
                option.initFrom(label)
                self._scaled = label.style().generatedIconPixmap(QtGui.QIcon.Disabled, self._scaled, option)
            self._scaled_key = key
        position = QtWidgets.QStyle.alignedRect(label.layoutDirection(), label.alignment(), size, rect).topLeft()
        painter = QtGui.QPainter(label)
        painter.drawPixmap(position, self._scaled)
        painter.end()


def round_menu_corners(menu):
    """ Let a drop-down menu show the round corners of the style sheet (QMenu rules). """
    if not _TRANSLUCENT_POPUPS:
        return
    menu.setWindowFlags(menu.windowFlags() | QtCore.Qt.FramelessWindowHint
                        | QtCore.Qt.NoDropShadowWindowHint)
    menu.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    menu.setProperty("snoozRounded", True)


def set_title_bar_color(window, background, text):
    """ Color the title bar of a window. Windows 11 only, ignored elsewhere. """
    if sys.platform != "win32":
        return
    try:
        import ctypes
        from ctypes import wintypes
        set_attribute = ctypes.windll.dwmapi.DwmSetWindowAttribute
        hwnd = wintypes.HWND(int(window.winId()))
        for attribute, color in ((_DWMWA_CAPTION_COLOR, background), (_DWMWA_TEXT_COLOR, text)):
            qcolor = QtGui.QColor(color)
            # COLORREF: 0x00BBGGRR
            value = wintypes.DWORD(qcolor.red() | qcolor.green() << 8 | qcolor.blue() << 16)
            set_attribute(hwnd, wintypes.DWORD(attribute), ctypes.byref(value), ctypes.sizeof(value))
    except (AttributeError, OSError):
        pass
