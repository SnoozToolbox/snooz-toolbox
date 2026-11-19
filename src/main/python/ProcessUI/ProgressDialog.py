"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2026
See the file LICENCE for full license details.

Window shown while a process runs: the file being analysed and how many there are,
the module that is running, the start time, the files processed with their time and
the expected end of the run.

The process runs in the thread of the interface: while a module runs, the window is
not painted again. So the times are static, written when a file is done
(progression_update), instead of counters that would look stuck during a long
module: the time taken by the files processed, and the clock time at which the run
should end (the average time of the files processed, times the files left). Until
the first file is done, the end is being estimated.
The module that starts (state topic of its node) is painted at once: it may keep the
interface busy for a long time. The other pending paint events are processed at most
every _REFRESH_PERIOD; the clicks and the keys are left out, nothing else can start.
Its look is in the RUN PROGRESS section of the style sheet.
"""
import time
from datetime import datetime, timedelta

from qtpy.QtCore import QCoreApplication, QEventLoop, Qt
from qtpy.QtWidgets import QDialog, QHBoxLayout, QLabel, QProgressBar, QVBoxLayout

from commons.fonts import set_text_style, text_label

# Message of a node when one of its modules starts (flowpipe/node.py)
_RUNNING = "is_running"
# The pending events are processed at most this often (seconds) while modules start
_REFRESH_PERIOD = 0.1
_WIDTH = 480
ESTIMATING_TEXT = "Expected end: estimating..."
# Space between the lines of the note, in percent of the font height
_NOTE_LINE_HEIGHT = 135


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


def clock_text(moment, start_day):
    """ A clock time as the user reads it: "14:32" on the day the run started,
    "tomorrow 02:10" the day after, "Mon 21 Nov 09:15" later. """
    if moment.date() == start_day:
        return f"{moment:%H:%M}"
    if moment.date() == start_day + timedelta(days=1):
        return f"tomorrow {moment:%H:%M}"
    return f"{moment:%a %d %b %H:%M}"


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
    parent : QWidget, optional
        The window it is shown over (the main window).
    """

    def __init__(self, module_labels=None, pub_sub_manager=None, parent=None):
        super().__init__(parent)
        self._module_labels = dict(module_labels or {})
        self._pub_sub_manager = pub_sub_manager
        self._topics = {f"{identifier}.state_change": label
                        for identifier, label in self._module_labels.items()}
        self._start_time = time.monotonic()
        self._started_at = datetime.now()
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
        layout.setContentsMargins(28, 24, 28, 24)
        layout.setSpacing(0)

        self.label = text_label("Running the process...", "h2")
        layout.addWidget(self.label)
        layout.addSpacing(8)
        self.module_label = _ElidedLabel()
        self.module_label.setObjectName("run_progress_module")
        self.module_label.set_full_text("Starting...")
        layout.addWidget(self.module_label)
        layout.addSpacing(20)

        self.progress_bar = QProgressBar()
        self.progress_bar.setObjectName("run_progress_bar")
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setFixedHeight(10)
        layout.addWidget(self.progress_bar)
        layout.addSpacing(10)

        # Files processed and their time (left), start time (right)
        counts = QHBoxLayout()
        self.progress_text = QLabel("")
        self.progress_text.setObjectName("run_progress_muted")
        set_text_style(self.progress_text, "small")
        counts.addWidget(self.progress_text)
        counts.addStretch(1)
        self.started_label = QLabel(f"Started at {self._started_at:%H:%M}")
        self.started_label.setObjectName("run_progress_muted")
        set_text_style(self.started_label, "small")
        counts.addWidget(self.started_label)
        layout.addLayout(counts)
        layout.addSpacing(8)
        # Expected end of the run
        self.time_label = QLabel(ESTIMATING_TEXT)
        self.time_label.setObjectName("run_progress_muted")
        set_text_style(self.time_label, "small")
        layout.addWidget(self.time_label)
        layout.addSpacing(26)

        note = QLabel(f'<p style="line-height:{_NOTE_LINE_HEIGHT}%">Snooz is busy until the process '
                      'is completed and does not respond while a long module runs. The times are '
                      'updated after each file.</p>')
        note.setTextFormat(Qt.TextFormat.RichText)
        note.setObjectName("run_progress_muted")
        note.setWordWrap(True)
        set_text_style(note, "small")
        layout.addWidget(note)

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
        """ counter files out of total_count are done: the counts and the times are
        written, they stay until the next file is done. """
        self._total = max(1, int(total_count))
        self._done = max(0, min(int(counter), self._total))
        self.progress_bar.setValue(int(self._done / self._total * 100))
        self.label.setText(f"Analysing file {min(self._done + 1, self._total)} of {self._total}")
        if self._done:
            elapsed = time.monotonic() - self._start_time
            self.progress_text.setText(
                f"{self._done} of {self._total} files processed in {duration_text(elapsed)}")
            # Average time of the files processed, for the files left
            left = elapsed / self._done * (self._total - self._done)
            end = datetime.now() + timedelta(seconds=left)
            self.time_label.setText(f"Expected end around {clock_text(end, self._started_at.date())}")
        self._refresh(force=True)

    def on_topic_update(self, topic, message, sender):
        """ A module starts: show its name. """
        if message != _RUNNING or topic not in self._topics:
            return
        label = self._topics[topic]
        self.module_label.set_full_text(f"Module: {label}" if label else "Running a module...")
        # Painted now, not at the next processing of the events: this module may keep
        # the interface busy for a long time, and the events are processed at most every
        # _REFRESH_PERIOD (the previous module could have started just before).
        if self.module_label.isVisible():
            self.module_label.repaint()
        self._refresh()

    def _refresh(self, force=False):
        """ Process the pending paint events now: the process keeps the interface busy. """
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
