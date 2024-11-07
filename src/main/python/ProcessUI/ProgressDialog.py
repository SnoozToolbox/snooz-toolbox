from qtpy.QtCore import Qt
from qtpy.QtWidgets import QDialog, QVBoxLayout, QLabel, QProgressBar

class ProgressDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.resize(400, 20)
        self.setWindowTitle("Please wait until the process is completed...")
        self.setWindowModality(Qt.ApplicationModal)  # Block the UI
        # Add the close button, it wont work until the process is done
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)

        self.layout = QVBoxLayout()

        self.label = QLabel("Running process...")
        self.layout.addWidget(self.label)
        self.progress_text = QLabel("")
        self.layout.addWidget(self.progress_text)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.layout.addWidget(self.progress_bar)

        self.setLayout(self.layout)

    def progression_update(self, total_count, counter):
            self.progress_text.setText(f"{counter} of {total_count}...")
            self.progress_bar.setValue(counter / total_count * 100)
            