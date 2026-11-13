"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2026
See the file LICENCE for full license details.

Window shown while a process runs: the file being analysed and how many there are,
the module that is running, the time elapsed and an estimate of the time left.

The process runs in the thread of the interface, so the window is kept up to date
by hand: when a module starts (state topic of its node) and when a file is done
(progression_update), the texts are changed and the pending paint events are
processed. The clicks and the keys are left out, nothing else can start meanwhile.
Its look is in the RUN PROGRESS section of the style sheet.
"""
import time

from qtpy.QtCore import QCoreApplication, QEventLoop, Qt
from qtpy.QtWidgets import QDialog, QHBoxLayout, QLabel, QProgressBar, QVBoxLayout

from commons.fonts import set_text_style, text_label

# Message of a node when one of its modules starts (flowpipe/node.py)
_RUNNING = "is_running"
# The window is painted again at most this often (seconds) while modules start
_REFRESH_PERIOD = 0.1
_WIDTH = 480


def duration_text(seconds):
    """ A duration as the user reads it: "45 s", "3 min 05 s", "2 h 10 min". """
    seconds = max(0, int(round(seconds)))
    if seconds < 60:
        return f"{seconds} s"
    minutes, seconds = divmod(seconds, 60)
    if minutes < 60:
        return f"{minutes} min {seconds:02d} s"
    hours, minutes = divmod(minutes, 60)
    return f"{hours} h {minutes:02d} min"


class _ElidedLabel(QLabel):
    """ Label showing its text on one line, cut at the end when it is too long. """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._full_text = ""
        self.setMinimumWidth(1)

    def set_full_text(self, text):
        self._full_text = text
        self._elide()

    def full_text(self):
        return self._full_text

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._elide()

    def _elide(self):
        self.setText(self.fontMetrics().elidedText(self._full_text, Qt.TextElideMode.ElideRight, self.width()))


class ProgressDialog(QDialog):
    """ Window shown while a process runs.

    Parameters
    ----------
    module_labels : dict, optional
        The name of the module of each node of the process, by node identifier: the
        window shows the one that is running.
    pub_sub_manager : PubSubManager, optional
        To be told when a module starts.
    """

    def __init__(self, module_labels=None, pub_sub_manager=None):
        super().__init__()
        self._module_labels = dict(module_labels or {})
        self._pub_sub_manager = pub_sub_manager
        self._topics = {f"{identifier}.state_change": label
                        for identifier, label in self._module_labels.items()}
        self._start_time = time.monotonic()
        self._done = 0
        self._total = None
        self._last_refresh = 0.0
        self._closing = False

        self.setObjectName("run_progress")
        self.setWindowTitle("Process running")
        self.setWindowModality(Qt.WindowModality.ApplicationModal)  # Block the UI
        # No close button: the window closes when the process is done
        self.setWindowFlags((self.windowFlags() | Qt.WindowType.CustomizeWindowHint)
                            & ~Qt.WindowType.WindowCloseButtonHint
                            & ~Qt.WindowType.WindowContextHelpButtonHint)
        self.setFixedWidth(_WIDTH)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 20, 24, 18)
        layout.setSpacing(0)

        self.label = text_label("Running the process...", "h2")
        layout.addWidget(self.label)
        layout.addSpacing(6)
        self.module_label = _ElidedLabel()
        self.module_label.setObjectName("run_progress_module")
        self.module_label.set_full_text("Starting...")
        layout.addWidget(self.module_label)
        layout.addSpacing(14)

        self.progress_bar = QProgressBar()
        self.progress_bar.setObjectName("run_progress_bar")
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setFixedHeight(10)
        layout.addWidget(self.progress_bar)
        layout.addSpacing(8)

        details = QHBoxLayout()
        self.progress_text = QLabel("")
        self.progress_text.setObjectName("run_progress_muted")
        set_text_style(self.progress_text, "small")
        details.addWidget(self.progress_text)
        details.addStretch(1)
        self.time_label = QLabel("")
        self.time_label.setObjectName("run_progress_muted")
        set_text_style(self.time_label, "small")
        details.addWidget(self.time_label)
        layout.addLayout(details)
        layout.addSpacing(14)

        note = QLabel("Snooz is busy until the process is completed. "
                      "The time of a file depends on its length and on the modules.")
        note.setObjectName("run_progress_muted")
        note.setWordWrap(True)
        set_text_style(note, "small")
        layout.addWidget(note)

        self._update_time()
        if self._pub_sub_manager is not None:
            for topic in self._topics:
                self._pub_sub_manager.subscribe(self, topic)

    def show(self):
        """ Show the window and paint it before the process starts. """
        super().show()
        self._refresh(force=True)

    def close(self):
        """ Close the window: the process is done. """
        self._closing = True
        return super().close()

    def closeEvent(self, event):
        if not self._closing:
            # Alt+F4...: the window stays until the process is done
            event.ignore()
            return
        self._unsubscribe()
        super().closeEvent(event)

    def reject(self):
        # Escape does not close the window while the process runs
        if self._closing:
            super().reject()

    def progression_update(self, total_count, counter):
        """ counter files out of total_count are done. """
        self._total = max(1, int(total_count))
        self._done = max(0, min(int(counter), self._total))
        self.progress_bar.setValue(int(self._done / self._total * 100))
        self.label.setText(f"Analysing file {min(self._done + 1, self._total)} of {self._total}")
        self.progress_text.setText(f"{self._done} of {self._total} files done")
        self._update_time()
        self._refresh(force=True)

    def on_topic_update(self, topic, message, sender):
        """ A module starts: show its name. """
        if message != _RUNNING or topic not in self._topics:
            return
        label = self._topics[topic]
        self.module_label.set_full_text(f"Module: {label}" if label else "Running a module...")
        self._update_time()
        self._refresh()

    def _update_time(self):
        elapsed = time.monotonic() - self._start_time
        text = f"Elapsed: {duration_text(elapsed)}"
        if self._total and 0 < self._done < self._total:
            left = elapsed / self._done * (self._total - self._done)
            text += f"  ·  About {duration_text(left)} left"
        self.time_label.setText(text)

    def _refresh(self, force=False):
        """ Paint the window now: the process keeps the interface busy. """
        now = time.monotonic()
        if not force and now - self._last_refresh < _REFRESH_PERIOD:
            return
        self._last_refresh = now
        if self.isVisible():
            QCoreApplication.processEvents(QEventLoop.ProcessEventsFlag.ExcludeUserInputEvents)

    def _unsubscribe(self):
        if self._pub_sub_manager is not None:
            for topic in self._topics:
                self._pub_sub_manager.unsubscribe(self, topic)
            self._pub_sub_manager = None
