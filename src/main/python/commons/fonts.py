"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2026
See the file LICENCE for full license details.

The font of Snooz: Inter, bundled in resources/base/fonts/Inter.

Every widget uses the application font set here: forms and code must not set a
font family. Sizes are in pixels so the text has the same size on every
operating system (12pt was 16 px on Windows but 12 px on macOS).
"""
import struct

from qtpy import QtCore, QtGui, QtWidgets

import config

FAMILY = "Inter"
# Body text, in pixels (12pt on Windows).
BODY_PIXEL_SIZE = 16

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
        _application_font.setPixelSize(BODY_PIXEL_SIZE)
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
