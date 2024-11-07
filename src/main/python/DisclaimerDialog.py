from qtpy.QtCore import Qt
from qtpy.QtWidgets import QDialog, QLabel, QVBoxLayout, QCheckBox, QPushButton, QHBoxLayout

from config import settings

class DisclaimerDialog(QDialog):
    def __init__(self, settings_manager):
        super().__init__()
        self._settings_manager = settings_manager
        self.setWindowTitle("BETA Disclaimer")
        self.setWindowModality(Qt.ApplicationModal)  # Block the UI

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint &
                            ~Qt.WindowContextHelpButtonHint)
        self.setFixedSize(440, 225)  # Set the desired width and height

        self.layout = QVBoxLayout()

        self.label = QLabel("Disclaimer: This Application is in Beta Testing")
        font = self.label.font()
        font.setBold(True)
        self.label.setFont(font)
        self.layout.addWidget(self.label)

        self.label2 = QLabel("The software is still undergoing development and may contain bugs or issues that could affect its performance. By using this application, you acknowledge and accept the potential risks associated with beta testing. Feedback and bug reports are welcomed for improvement.")
        self.label2.setWordWrap(True)
        self.layout.addWidget(self.label2)

        self.checkbox = QCheckBox("Do not show again")
        self.layout.addWidget(self.checkbox)

        vlayout = QHBoxLayout()
        vlayout.addStretch()

        self.layout.addStretch()
        self.button = QPushButton("Accept")
        self.button.clicked.connect(self.close_dialog)
        vlayout.addWidget(self.button)
        self.layout.addLayout(vlayout)

        self.setLayout(self.layout)

    def close_dialog(self):
        if self.checkbox.isChecked():
            # Perform action based on checkbox value
            self._settings_manager.set_setting(settings.skip_beta_disclaimer, True)

        self.close()