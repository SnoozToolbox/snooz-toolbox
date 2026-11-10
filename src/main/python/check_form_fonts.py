"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2026
See the file LICENCE for full license details.

Check the fonts of Qt Designer forms against the form guideline of Snooz.

Snooz shows every form in Inter: the sizes, bold, italic and underline set in Qt
Designer are shown, a font family is not. The check reports, widget by widget:
- a font family, in the font property of the widget or in rich text,
- a font rule in a style sheet: it hides the fonts of the widgets inside,
- a size on the root widget or on a container (page, frame, tab widget...): Snooz
  does not pass it reliably to the widgets inside, and on macOS the layout is
  measured with it before Snooz converts it to pixels.

When Snooz starts from the source code with a window, main.py checks the forms of
the packages added in the settings, in the background once the window is shown,
and prints the result in the terminal. A package can also check its forms without
starting Snooz:
    python check_form_fonts.py <folder> [<folder>...] [--strict]
This module only uses the standard library (no Qt, no config): the scripts of a
package can load it from its file (snooz-package-ceams: main_utils.py, option 7).
"""
from __future__ import annotations

import argparse
import os
import re
import sys
import threading
import xml.etree.ElementTree as ET
from pathlib import Path

GUIDELINE_TITLE = "How Tos - Fonts and colors of forms"
# The page of the developer guide, in the documentation of config.DOCUMENTATION_URL
GUIDELINE_URL = "https://snooz-toolbox-documentation.readthedocs.io/latest/dev_guide/howtos/forms_style_howtos.html"

# Font rules of a style sheet, font family of rich text
_SHEET_FONT_RULE = re.compile(r"(?<![-\w])(font(?:-family|-size|-weight|-style)?)\s*:\s*([^;}]*)", re.IGNORECASE)
_RICH_FAMILY = re.compile(r"(?<![-\w])font-family\s*:\s*([^;\"]*)", re.IGNORECASE)
# Qt Designer writes the font of a text box at the top of its text (<body style=...>):
# it is not a choice of the form, Snooz replaces it.
_RICH_BODY = re.compile(r"<body\b[^>]*>", re.IGNORECASE)
# Blocks of the template language between the elements of a form template
_TEMPLATE_BLOCK = re.compile(r"{%.*?%}", re.DOTALL)
# Copies of released packages, builds and caches: not the forms of the package
_SKIPPED_FOLDERS = {"release", "target", "__pycache__", ".git"}
# Widgets holding other widgets: a size set on them does not reach the widgets inside
_CONTAINER_CLASSES = {"QWidget", "QFrame", "QScrollArea", "QStackedWidget", "QTabWidget", "QSplitter", "QToolBox",
                      "QDockWidget", "QMainWindow", "QDialog", "QMdiArea", "QWizard", "QWizardPage"}
_ADVICE = (
    "Snooz shows every form in Inter, with the sizes, bold, italic and underline set in Qt Designer.",
    "- font family: leave the family of the Font property unset, and do not change the font in the",
    "  rich text editor (paste texts as plain text).",
    "- style sheet font rule: it hides the fonts of the widgets inside; use the Font property.",
    "- size on the root widget or on a container: Snooz does not pass it reliably to the widgets",
    "  inside; set it on each widget showing the text.",
    f"See the developer guide, {GUIDELINE_TITLE}:",
    f"  {GUIDELINE_URL}",
)


def iter_forms(folder):
    """ The forms (.ui) and the form templates (*_template.txt holding a form) under a folder. """
    paths = []
    for current, subfolders, files in os.walk(folder):
        subfolders[:] = [name for name in subfolders if name not in _SKIPPED_FOLDERS]
        paths.extend(Path(current, name) for name in files
                     if name.lower().endswith(".ui") or name.endswith("_template.txt"))
    for path in sorted(paths):
        if path.suffix.lower() != ".ui" and b"<ui" not in path.read_bytes()[:500]:
            continue  # a template of another kind of file
        yield path


def check_form(path):
    """ The font settings of a form that Snooz does not show, or that hide the ones of
    other widgets: one line per widget and setting. """
    try:
        root = _parse_form(Path(path))
    except Exception as exc:
        return [f"could not be read as a form: {exc}"]
    if root.tag != "ui":
        return []
    findings = []
    root_widget = root.find("./widget")
    for widget in root.iter("widget"):
        name = widget.attrib.get("name", "<unnamed>")
        cls = widget.attrib.get("class", "")
        label = f"{name} (root)" if widget is root_widget else name
        family = _text(widget, "./property[@name='font']/font/family")
        if family:
            findings.append(f"{label}: font family {family}")
        size = _text(widget, "./property[@name='font']/font/pointsize")
        if size and widget is root_widget:
            findings.append(f"{label}: font size {size}pt on the root widget")
        elif size and cls in _CONTAINER_CLASSES:
            findings.append(f"{label}: font size {size}pt on a {cls}")
        sheet = _text(widget, "./property[@name='styleSheet']/string")
        for rule, value in _SHEET_FONT_RULE.findall(sheet):
            findings.append(f"{label}: style sheet {rule.lower()}: {value.strip()}")
        rich = set()
        for string in widget.findall("./property/string"):
            html = string.text or ""
            if "<" in html:
                for value in _RICH_FAMILY.findall(_RICH_BODY.sub("", html)):
                    rich.add(f"{label}: rich text font-family: {value.strip()}")
        findings.extend(sorted(rich))
    return findings


def check_folders(folders):
    """ Check the forms under the folders: the number of forms checked, and the
    settings to fix of each form ({path: [lines]}). """
    count = 0
    found = {}
    for folder in folders:
        for path in iter_forms(folder):
            count += 1
            findings = check_form(path)
            if findings:
                found[path] = findings
    return count, found


def report_lines(found, base=None):
    """ The forms to fix with their settings, then the advice. Paths relative to base when given. """
    shown = {(path.relative_to(base) if base is not None else path).as_posix(): findings
             for path, findings in found.items()}
    lines = []
    for name, findings in sorted(shown.items()):  # the same order on every system
        lines.append(f"  {name}")
        lines.extend(f"     - {finding}" for finding in findings)
    if found:
        lines.append("")
        lines.extend(_ADVICE)
    return lines


def check_and_print(folders, strict=False):
    """ Check the forms under the folders and print the result (command line, scripts of
    a package). Returns 1 with strict when a form has settings to fix, 2 for a missing folder. """
    reconfigure = getattr(sys.stdout, "reconfigure", None)
    if reconfigure is not None:
        reconfigure(errors="replace")  # names of forms and fonts on any console
    folders = [Path(folder).resolve() for folder in folders]
    for folder in folders:
        if not folder.is_dir():
            print(f"Folder not found: {folder}")
            return 2
    count, found = check_folders(folders)
    settings = sum(len(findings) for findings in found.values())
    where = ", ".join(str(folder) for folder in folders)
    print(f"Fonts of the forms in {where}: {count} form(s) checked, {len(found)} to fix ({settings} setting(s)).")
    for line in report_lines(found, base=folders[0] if len(folders) == 1 else None):
        print(line)
    return 1 if strict and found else 0


def run_dev_check(folders):
    """ Check the forms of the packages added in the settings and print the result in
    the terminal, in one block (Snooz started from the source code). """
    folders = [Path(folder) for folder in folders if folder and os.path.isdir(folder)]
    count, found = check_folders(folders)
    if count == 0:
        return
    if not found:
        print(f"Fonts of the forms of your packages: {count} form(s) checked, all follow the guideline.", flush=True)
        return
    settings = sum(len(findings) for findings in found.values())
    lines = [f"Fonts of the forms of your packages: {count} form(s) checked, {len(found)} to fix "
             f"({settings} setting(s)):"]
    lines.extend(report_lines(found))
    print("\n".join(lines), flush=True)


def start_dev_check(folders, delay=1.0):
    """ Run run_dev_check in the background after a delay, so Snooz shows its window first. """
    def run():
        try:
            run_dev_check(folders)
        except Exception as exc:  # Only a check: never a reason to stop Snooz
            print(f"Fonts of the forms of your packages: the check failed ({exc}).", flush=True)
    timer = threading.Timer(delay, run)
    timer.daemon = True
    timer.start()
    return timer


def _parse_form(path):
    data = path.read_bytes()
    try:
        return ET.fromstring(data)
    except ET.ParseError:
        if not path.name.endswith("_template.txt"):
            raise
        # A template can hold blocks of the template language between the elements
        return ET.fromstring(_TEMPLATE_BLOCK.sub("", data.decode("utf-8")).encode("utf-8"))


def _text(element, xpath):
    node = element.find(xpath)
    return (node.text or "").strip() if node is not None else ""


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check the fonts of the Qt Designer forms of Snooz packages "
                                                 f"against the form guideline ({GUIDELINE_URL}).")
    parser.add_argument("folders", nargs="*", default=["."], help="Folders to check (default: the current folder)")
    parser.add_argument("--strict", action="store_true", help="Exit with code 1 when a form has settings to fix "
                                                              "(pre-commit hook, automatic check)")
    args = parser.parse_args(argv)
    return check_and_print(args.folders, args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
