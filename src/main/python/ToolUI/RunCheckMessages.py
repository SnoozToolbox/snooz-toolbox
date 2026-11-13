"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2026
See the file LICENCE for full license details.
"""
"""
    Messages of the steps of a tool while Run checks their settings.

    A step whose settings are not valid tells why in a message box, then Run shows
    the general error: two pop-ups for one problem. While Run checks the settings,
    the message boxes with a single button (nothing for the user to choose) are held
    back and Run writes their text under the general error, in one pop-up. A message
    box with a choice (OK and Cancel...) is still shown: the answer of the user
    decides whether the run goes on.

    The message boxes of the steps (WarningDialog, QMessageBox.warning, the
    show_error_message topic...) all come from QMessageBox: its exec and its static
    message functions are replaced for the time of the check, then put back. Nothing
    changes in the packages.
"""
from qtpy import QtCore, QtGui, QtWidgets

# exec_ (qtpy) calls exec: replaced as well, in case another qtpy does not
_EXEC_NAMES = ("exec", "exec_")
# Static functions of QMessageBox that show a message with only an OK button by default
_STATIC_MESSAGES = ("critical", "warning", "information")
# Written by the main window before the text of an error (show_error_message)
_ERROR_PREFIX = "Error: "
_MISSING = object()


def _plain_text(text, text_format):
    """ The text of a message as the user reads it (a rich text without its tags). """
    formats = QtCore.Qt.TextFormat
    if text_format == formats.RichText or \
            (text_format == formats.AutoText and QtGui.Qt.mightBeRichText(text)):
        document = QtGui.QTextDocument()
        document.setHtml(text)
        return document.toPlainText()
    return text


def _has_one_button(message_box):
    """ Whether a message box leaves nothing to choose: one button (OK), no check box. """
    return len(message_box.buttons()) <= 1 and message_box.checkBox() is None


def _is_ok_only(buttons):
    """ Whether the buttons of a static message function show only OK. """
    standard = QtWidgets.QMessageBox.StandardButton
    return buttons == standard.Ok or buttons == standard.NoButton


class _DialogWatcher(QtCore.QObject):
    """ Notes that a dialog is shown while the settings are checked (a question, a
    table of files). """

    def __init__(self, messages):
        super().__init__()
        self._messages = messages

    def eventFilter(self, watched, event):
        if event.type() == QtCore.QEvent.Type.Show and \
                isinstance(watched, QtWidgets.QDialog) and watched.isWindow():
            self._messages.dialog_shown = True
        return False


class RunCheckMessages:
    """ Holds back the single-button messages of the steps while Run checks their
    settings: with RunCheckMessages() as messages: ...

    The settings views are checked one after the other: begin_view before each one,
    show_held after a view whose settings are valid (its messages are shown as
    before). For the view whose settings are not valid, texts are its held messages
    and dialog_shown tells whether it showed a dialog of its own (a question, a table).
    """

    def __init__(self):
        # (text, function showing the message as it would have been) of the view checked
        self._held = []
        self.dialog_shown = False
        self._replaced = {}
        self._watcher = None

    @property
    def texts(self):
        """ The texts of the held messages of the view checked. """
        texts = []
        for text, _ in self._held:
            text = text.strip()
            # The general error already starts with it
            if text.startswith(_ERROR_PREFIX):
                text = text[len(_ERROR_PREFIX):].strip()
            if text:
                texts.append(text)
        return texts

    def begin_view(self):
        """ A settings view is about to be checked. """
        self._held = []
        self.dialog_shown = False

    def show_held(self):
        """ Show the held messages, as they would have been shown. """
        held, self._held = self._held, []
        for _, show in held:
            show()

    def __enter__(self):
        message_box = QtWidgets.QMessageBox
        # The functions of Qt, to show a message as usual
        real_exec = message_box.exec
        ok = message_box.StandardButton.Ok
        ok_result = getattr(ok, "value", ok)

        def exec_(box, *args, **kwargs):
            if _has_one_button(box):
                text = "\n\n".join(_plain_text(part, box.textFormat())
                                   for part in (box.text(), box.informativeText()) if part)
                self._held.append((text, lambda: real_exec(box)))
                return ok_result
            return real_exec(box, *args, **kwargs)

        def static_message(real):
            def message(*args, **kwargs):
                buttons = kwargs.get("buttons", args[3] if len(args) > 3 else None)
                if buttons is None or _is_ok_only(buttons):
                    text = str(kwargs.get("text", args[2] if len(args) > 2 else ""))
                    self._held.append((_plain_text(text, QtCore.Qt.TextFormat.AutoText),
                                       lambda: real(*args, **kwargs)))
                    return ok
                return real(*args, **kwargs)
            return message

        replacements = {name: exec_ for name in _EXEC_NAMES if hasattr(message_box, name)}
        for name in _STATIC_MESSAGES:
            replacements[name] = staticmethod(static_message(getattr(message_box, name)))
        for name, replacement in replacements.items():
            self._replaced[name] = message_box.__dict__.get(name, _MISSING)
            setattr(message_box, name, replacement)

        self._watcher = _DialogWatcher(self)
        QtWidgets.QApplication.instance().installEventFilter(self._watcher)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        message_box = QtWidgets.QMessageBox
        for name, original in self._replaced.items():
            if original is _MISSING:
                delattr(message_box, name)
            else:
                setattr(message_box, name, original)
        self._replaced = {}
        QtWidgets.QApplication.instance().removeEventFilter(self._watcher)
        self._watcher = None
        if exc_type is not None:
            # The check stopped on an exception: the messages are shown as before
            self.show_held()
        return False
