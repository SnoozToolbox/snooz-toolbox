"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2026
See the file LICENCE for full license details.

The font of Snooz: Inter, bundled in resources/base/fonts/Inter.

Every widget uses the application font set here: forms and code must not set a
font family. Sizes are in pixels so the text has the same size on every
operating system (12pt was 16 px on Windows but 12 px on macOS).

The text sizes of the toolbox are all in TEXT_STYLES. To use one of them:
    text_label("Recent files", "h2")    a new label
    set_text_style(widget, "mono")      an existing widget
    text_style_font("node")             a text painted in code
    font-size: @font_body;              a rule of the style sheet

Forms made in Qt Designer do not use them: a heading is a text made bold in the
text editor of the label.
"""
import struct

from qtpy import QtCore, QtGui, QtWidgets

import config

FAMILY = "Inter"

# The text styles of Snooz: size in pixels and weight.
TEXT_STYLES = {
    "body": (16, 400),
    "h1": (24, 700),
    "h2": (20, 700),
    "h3": (16, 700),
    "small": (13, 400),
    "mono": (14, 400),
    # Headers of the tables of the process editor
    "table_header": (12, 400),
    # Labels painted on the nodes of the process editor
    "node": (11, 400),
}
# Fonts of the "mono" style, the first one installed is used: Windows, macOS, Linux.
_MONO_FAMILIES = ("Consolas", "Menlo", "DejaVu Sans Mono", "monospace")
_TEXT_STYLE_PROPERTY = "textStyle"

_STYLES = ("Regular", "Italic", "Medium", "MediumItalic", "SemiBold", "SemiBoldItalic", "Bold", "BoldItalic")

# Underline, in em. Inter's own underline (0.07 em thick) is drawn by Qt as a
# 2 px bar stuck to the letters: Snooz keeps the thin underline of Roboto, its
# previous font (Qt on Windows places the underline from its thickness).
_UNDERLINE_POSITION = -0.073
_UNDERLINE_THICKNESS = 0.049

# Fonts named by older forms (packages released before Inter, Qt Designer
# defaults): they are shown in Inter. A name only takes effect on the computers
# where this font is not installed.
_LEGACY_FAMILIES = ("Roboto", "Roboto-Regular", "MS Shell Dlg 2", "Segoe UI", "Helvetica Neue", "Lato", "Aptos")

_application_font = None


def application_font():
    """ The font of the application: Inter, body size.

    The font files are registered the first time.
    """
    global _application_font
    if _application_font is None:
        for style in _STYLES:
            try:
                path = config.app_context.get_resource(f"fonts/{FAMILY}/{FAMILY}-{style}.ttf")
            except FileNotFoundError:
                print(f"fonts: {FAMILY}-{style}.ttf not found")
                continue
            with open(path, "rb") as font_file:
                data = _with_snooz_underline(font_file.read())
            if QtGui.QFontDatabase.addApplicationFontFromData(QtCore.QByteArray(data)) < 0:
                print(f"fonts: could not load {path}")
        for family in _LEGACY_FAMILIES:
            QtGui.QFont.removeSubstitutions(family)
            QtGui.QFont.insertSubstitution(family, FAMILY)
        _application_font = QtGui.QFont(FAMILY)
        _application_font.setPixelSize(TEXT_STYLES["body"][0])
    return QtGui.QFont(_application_font)


def _with_snooz_underline(data):
    """ The data of a font file with the underline of Snooz (post table). """
    data = bytearray(data)
    tables = {}
    for record in range(12, 12 + 16 * struct.unpack_from(">H", data, 4)[0], 16):
        tag, _, offset, length = struct.unpack_from(">4sIII", data, record)
        tables[tag] = (record, offset, length)
    units_per_em = struct.unpack_from(">H", data, tables[b"head"][1] + 18)[0]
    record, offset, length = tables[b"post"]
    struct.pack_into(">hh", data, offset + 8,
        round(_UNDERLINE_POSITION * units_per_em), round(_UNDERLINE_THICKNESS * units_per_em))
    # The checksum of a table is the sum of its 32-bit words
    table = bytes(data[offset:offset + length]) + bytes(-length % 4)
    struct.pack_into(">I", data, record + 4, sum(struct.unpack(f">{len(table) // 4}I", table)) & 0xFFFFFFFF)
    return bytes(data)


def apply_application_font():
    """ Make the Snooz font the font of every widget.

    Call it again after each change of the application style or style sheet:
    on Windows, they give the menus and message boxes the system font back.
    """
    QtWidgets.QApplication.setFont(application_font())


def _families(name):
    return _MONO_FAMILIES if name == "mono" else (FAMILY,)


def text_style_rules(name):
    """ The declarations of a text style, for a style sheet. """
    size, weight = TEXT_STYLES[name]
    families = ", ".join(f'"{family}"' for family in _families(name))
    return f"font-family: {families}; font-size: {size}px; font-weight: {weight};"


def set_text_style(widget, name):
    """ Show the text of a widget in a text style.

    The style is set on the widget itself because the application style sheet
    cannot do it: a form-level font rule, such as 'font: 16px "Inter";' on the
    main window, has priority over it whatever the selector. The selector on
    the property keeps the style off the children of the widget, such as the
    context menu of a text box.
    """
    widget.setProperty(_TEXT_STYLE_PROPERTY, name)
    widget.setStyleSheet(f'*[{_TEXT_STYLE_PROPERTY}="{name}"] {{ {text_style_rules(name)} }}')


def text_label(text, name, parent=None):
    """ A label showing a text in a text style. """
    label = QtWidgets.QLabel(text, parent)
    set_text_style(label, name)
    return label


def text_style_font(name):
    """ The font of a text style, for a text painted in code. """
    size, weight = TEXT_STYLES[name]
    font = application_font()
    font.setFamilies(list(_families(name)))
    font.setPixelSize(size)
    font.setWeight(QtGui.QFont.Weight(weight))
    return font


def font_tokens():
    """ The sizes of the text styles, as tokens of the style sheet: @font_body... """
    return {f"font_{name}": f"{size}px" for name, (size, _) in TEXT_STYLES.items()}
