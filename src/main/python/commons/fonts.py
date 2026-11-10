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

Forms made in Qt Designer do not use them: a heading is a text made bigger or
bold in the Font panel of the widget or in the text editor of the label. Sizes
in points are converted to pixels when the widget is shown (12pt = 16 px, 18pt
= 24 px), so they are the same on every operating system. The forms of the
toolbox (main window, steps, dialogs) only set the family of the font: a font
rule with a size in a style sheet would hide the sizes of the forms.

Forms made before Inter, such as the ones of the packages already released, give
sizes in points, name other fonts and save bold as the weight 600 (Qt 5
Designer); their links are the pure blue of Qt Designer. The application style
converts them when a widget is polished, before it is shown, see
harmonize_widget_text.
"""
import math
import re
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
    cannot do it: a form-level font rule, such as the family set on the main
    window, has priority over it whatever the selector. The selector on the
    property keeps the style off the children of the widget, such as the
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


# ----- Forms made before Inter -----

# Monospaced fonts named by forms: they are shown in the fonts of the "mono" style.
_MONOSPACED_NAMES = {"consolas", "menlo", "dejavu sans mono", "monospace", "courier", "courier new",
                     "courier 10 pitch", "lucida console", "monaco", "liberation mono", "source code pro"}
# A font declaration of a style sheet: name, colon, value.
_SHEET_DECLARATION = re.compile(r"(?<![-\w])(font(?:-size|-family|-weight)?)(\s*:\s*)([^;}]*)", re.IGNORECASE)
# The value of the font shorthand: style and weight, size, families.
_SHORTHAND = re.compile(r"^((?:(?:italic|oblique|normal|small-caps|bold|bolder|lighter|\d+)\s+)*)"
                        r"(\d+(?:\.\d+)?)(pt|px)\b\s*(.*)$", re.IGNORECASE | re.DOTALL)
_POINTS = re.compile(r"^(\d+(?:\.\d+)?)pt$", re.IGNORECASE)
# Declarations of rich text (style attributes, families in single quotes).
_RICH_SIZE = re.compile(r"(font-size\s*:\s*)(\d+(?:\.\d+)?)pt", re.IGNORECASE)
_RICH_FAMILY = re.compile(r"(\s*)font-family\s*:\s*((?:'[^']*'|[^;\"'<>])*)(;?)", re.IGNORECASE)
_RICH_SEMI_BOLD = re.compile(r"(font-weight\s*:\s*)600\b", re.IGNORECASE)
# Links: Qt Designer colors them pure blue, they take the link color of the theme.
_DESIGNER_LINK_BLUE = "#0000ff"
_DESIGNER_LINK_COLOR = re.compile(r"(color\s*:\s*)#0000ff\b", re.IGNORECASE)
_ANCHOR = re.compile(r"(<a\b[^>]*>)(.*?)(</a>)", re.IGNORECASE | re.DOTALL)
# Revision of a text box document when its formats were last converted.
_DOCUMENT_REVISION_PROPERTY = "_snoozFontRevision"
_SEMI_BOLD = 600
_BOLD = 700


def harmonize_widget_text(widget):
    """ Show a widget of a form made before Inter in the fonts and link color of Snooz.

    Called by the application style when the widget is polished, before it is
    shown (theme_helpers.SnoozStyle). It converts the font declarations of the
    style sheet of the widget, the font set on it (Font panel of Qt Designer), the
    rich text of a label or text box and its tooltip:
    - sizes in points become pixels, their size on Windows and Linux (12pt = 16 px;
      macOS gave 12 px),
    - other fonts become Inter, and monospaced ones the fonts of the "mono" style,
    - the weight 600 becomes 700: Qt 5 Designer saved bold as 600, which Inter
      shows semi-bold,
    - links in the pure blue of Qt Designer take the link color of the theme.
    Settings already in the fonts of Snooz are left as they are.
    """
    sheet = widget.styleSheet()
    if "font" in sheet:
        new_sheet = _harmonized_sheet(sheet)
        if new_sheet != sheet:
            # Qt gives the new style sheet to the children only when the widget is
            # polished: a form can be polished when it is placed, before it is shown
            # (process editor), and its children would keep the old font.
            widget.ensurePolished()
            if widget.styleSheet() == sheet:  # Not converted while it was polished
                widget.setStyleSheet(new_sheet)
    _harmonize_own_font(widget)
    if isinstance(widget, QtWidgets.QLabel):
        text = widget.text()
        if _has_old_rich_text_style(text) and _is_rich_text(text, widget.textFormat()):
            new_text = _harmonized_html(text)
            if new_text != text:
                widget.setText(new_text)
    elif isinstance(widget, QtWidgets.QTextEdit):
        _harmonize_text_box(widget)
    tip = widget.toolTip()
    if _has_old_rich_text_style(tip) and _is_rich_text(tip):
        new_tip = _harmonized_html(tip)
        if new_tip != tip:
            widget.setToolTip(new_tip)


def _pixels(points):
    """ A size in points, in pixels: its size on Windows and Linux (96 dpi), rounded like Qt. """
    return max(1, math.floor(points * 96 / 72 + 0.5))


def _family_names(value):
    """ The fonts of a list such as 'Roboto','sans-serif'. """
    return [name.strip().strip("'\"").strip() for name in value.split(",") if name.strip().strip("'\"").strip()]


def _snooz_families(names):
    """ The fonts of Snooz for fonts named by a form: Inter, or the monospaced fonts. """
    if any(name.lower() in _MONOSPACED_NAMES for name in names):
        return list(_MONO_FAMILIES)
    return [FAMILY]


def _is_rich_text(text, text_format=None):
    # The default is read here, not at import: headless mode replaces Qt with stubs
    if text_format is None:
        text_format = QtCore.Qt.TextFormat.AutoText
    return text_format == QtCore.Qt.TextFormat.RichText or (
        text_format == QtCore.Qt.TextFormat.AutoText and QtGui.Qt.mightBeRichText(text))


def _harmonized_sheet(sheet):
    return _SHEET_DECLARATION.sub(_harmonized_declaration, sheet)


def _harmonized_declaration(match):
    name, colon, value = match.groups()
    current = value.strip()
    kind = name.lower()
    if kind == "font":
        new = _harmonized_shorthand(current)
    elif kind == "font-size":
        points = _POINTS.match(current)
        new = f"{_pixels(float(points.group(1)))}px" if points else current
    elif kind == "font-family":
        new = _harmonized_families(current)
    else:
        new = "700" if current.lower() in ("600", "demibold") else current
    if new == current:
        return match.group(0)
    return f"{name}{colon}{value.replace(current, new, 1)}"


def _harmonized_shorthand(value):
    parts = _SHORTHAND.match(value)
    if parts is None:
        return value
    style_and_weight, size, unit, families = parts.groups()
    style_and_weight = " ".join("700" if token == "600" else token for token in style_and_weight.split())
    if unit.lower() == "pt":
        size, unit = _pixels(float(size)), "px"
    families = _harmonized_families(families) if families else ""
    return " ".join(part for part in (style_and_weight, f"{size}{unit}", families) if part)


def _harmonized_families(value):
    names = _family_names(value)
    families = _snooz_families(names)
    if names == families:
        return value
    return ", ".join(f'"{family}"' for family in families)


def _has_old_rich_text_style(text):
    """ True when rich text may set fonts or color its links in the blue of Qt Designer. """
    return "font-" in text or _DESIGNER_LINK_COLOR.search(text) is not None


def _harmonized_html(html):
    html = _RICH_SIZE.sub(lambda match: f"{match.group(1)}{_pixels(float(match.group(2)))}px", html)
    html = _RICH_FAMILY.sub(_harmonized_rich_families, html)
    html = _RICH_SEMI_BOLD.sub(r"\g<1>700", html)
    return _with_theme_links(html)


def _with_theme_links(html):
    """ The links of rich text in the link color of the theme instead of the blue of Qt Designer. """
    if _DESIGNER_LINK_COLOR.search(html) is None:
        return html
    link = QtGui.QGuiApplication.palette().color(QtGui.QPalette.ColorRole.Link).name()
    return _ANCHOR.sub(lambda match: match.group(1) + _DESIGNER_LINK_COLOR.sub(
        lambda color: color.group(1) + link, match.group(2)) + match.group(3), html)


def _harmonized_rich_families(match):
    space, value, end = match.groups()
    names = _family_names(value)
    if not names:
        return match.group(0)
    families = _snooz_families(names)
    if families == [FAMILY]:
        return ""  # The text takes the font of its widget
    listed = ",".join(f"'{family}'" for family in families)
    return f"{space}font-family:{listed}{end}"


def _harmonize_own_font(widget):
    """ The font set on the widget itself (Font panel of Qt Designer, setFont), or a
    size in points it got from its form.

    The font of Snooz is in pixels, so a size in points inside a window comes from
    a form: the font of a group box or a spin box given to the widgets inside it...
    The parent is converted when it is polished, but Qt does not pass its new font
    to the widgets polished before it (process editor: the widgets of a module view
    are polished when the view is placed in its tab): they would keep the size in
    points, smaller on macOS. Windows are left out: without a font of their own,
    they follow the font of the application.
    """
    font = widget.font()
    in_points = font.pixelSize() <= 0 and font.pointSizeF() > 0
    if not widget.testAttribute(QtCore.Qt.WidgetAttribute.WA_SetFont) and (not in_points or widget.isWindow()):
        return
    changed = False
    if in_points:
        font.setPixelSize(_pixels(font.pointSizeF()))
        changed = True
    names = list(font.families()) or [font.family()]
    families = _snooz_families(names)
    if names != families:
        font.setFamilies(families)
        changed = True
    if font.weight() == QtGui.QFont.Weight(_SEMI_BOLD):
        font.setWeight(QtGui.QFont.Weight(_BOLD))
        changed = True
    if changed:
        widget.setFont(font)


def _harmonize_text_box(text_edit):
    """ The character formats of a text box, like the rich text of a label. """
    document = text_edit.document()
    if document.property(_DOCUMENT_REVISION_PROPERTY) == document.revision():
        return
    changes = []
    block = document.begin()
    while block.isValid():
        # The format of a block gives the height of an empty line
        char_format = _harmonized_char_format(block.charFormat())
        if char_format is not None:
            changes.append((block.position(), None, char_format))
        for text_format in block.textFormats():
            char_format = _harmonized_char_format(text_format.format)
            if char_format is not None:
                start = block.position() + text_format.start
                changes.append((start, start + text_format.length, char_format))
        block = block.next()
    if changes:
        modified = document.isModified()
        undo_steps = document.availableUndoSteps()
        # The text does not change: no textChanged for the code of the form
        signals_blocked = text_edit.blockSignals(True)
        try:
            cursor = QtGui.QTextCursor(document)
            cursor.beginEditBlock()
            for start, end, char_format in changes:
                cursor.setPosition(start)
                if end is None:
                    cursor.setBlockCharFormat(char_format)
                else:
                    cursor.setPosition(end, QtGui.QTextCursor.MoveMode.KeepAnchor)
                    cursor.setCharFormat(char_format)
            cursor.endEditBlock()
            document.setModified(modified)
            if undo_steps == 0:
                document.clearUndoRedoStacks()
        finally:
            text_edit.blockSignals(signals_blocked)
    document.setProperty(_DOCUMENT_REVISION_PROPERTY, document.revision())


def _harmonized_char_format(char_format):
    """ A character format in the fonts and link color of Snooz, None if it already is. """
    new = QtGui.QTextCharFormat(char_format)
    changed = False
    if char_format.hasProperty(QtGui.QTextFormat.Property.FontPointSize):
        new.clearProperty(QtGui.QTextFormat.Property.FontPointSize)
        new.setProperty(QtGui.QTextFormat.Property.FontPixelSize,
                        _pixels(char_format.doubleProperty(QtGui.QTextFormat.Property.FontPointSize)))
        changed = True
    if char_format.hasProperty(QtGui.QTextFormat.Property.FontFamilies) or char_format.hasProperty(QtGui.QTextFormat.Property.FontFamily):
        names = list(char_format.fontFamilies() or []) or [char_format.fontFamily()]
        families = _snooz_families(names)
        if families == [FAMILY]:
            # The text takes the font of its text box
            new.clearProperty(QtGui.QTextFormat.Property.FontFamilies)
            new.clearProperty(QtGui.QTextFormat.Property.FontFamily)
            changed = True
        elif names != families:
            new.setFontFamilies(families)
            changed = True
    if char_format.hasProperty(QtGui.QTextFormat.Property.FontWeight) and \
            char_format.intProperty(QtGui.QTextFormat.Property.FontWeight) == _SEMI_BOLD:
        new.setFontWeight(_BOLD)
        changed = True
    if char_format.isAnchor() and char_format.hasProperty(QtGui.QTextFormat.Property.ForegroundBrush) and \
            char_format.foreground().color() == QtGui.QColor(_DESIGNER_LINK_BLUE):
        new.setForeground(QtGui.QGuiApplication.palette().link())
        changed = True
    return new if changed else None
