# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file ''
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ScoringCompletenessSettingsView(object):
    def setupUi(self, ScoringCompletenessSettingsView):
        if not ScoringCompletenessSettingsView.objectName():
            ScoringCompletenessSettingsView.setObjectName(u"ScoringCompletenessSettingsView")
        ScoringCompletenessSettingsView.resize(425, 292)
        self.verticalLayout = QVBoxLayout(ScoringCompletenessSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.output_file_label = QLabel(ScoringCompletenessSettingsView)
        self.output_file_label.setObjectName(u"output_file_label")

        self.horizontalLayout.addWidget(self.output_file_label)

        self.output_file_lineedit = QLineEdit(ScoringCompletenessSettingsView)
        self.output_file_lineedit.setObjectName(u"output_file_lineedit")
        self.output_file_lineedit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.output_file_lineedit)

        self.chosse_button = QPushButton(ScoringCompletenessSettingsView)
        self.chosse_button.setObjectName(u"chosse_button")

        self.horizontalLayout.addWidget(self.chosse_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 240, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ScoringCompletenessSettingsView)
        self.chosse_button.clicked.connect(ScoringCompletenessSettingsView.on_choose)

        QMetaObject.connectSlotsByName(ScoringCompletenessSettingsView)
    # setupUi

    def retranslateUi(self, ScoringCompletenessSettingsView):
        ScoringCompletenessSettingsView.setWindowTitle(QCoreApplication.translate("ScoringCompletenessSettingsView", u"Form", None))
        self.output_file_label.setText(QCoreApplication.translate("ScoringCompletenessSettingsView", u"Output file", None))
#if QT_CONFIG(tooltip)
        self.output_file_lineedit.setToolTip(QCoreApplication.translate("ScoringCompletenessSettingsView", u"Define the output file where the summary of the completeness of the scoring will be wrtiten. ", None))
#endif // QT_CONFIG(tooltip)
        self.output_file_lineedit.setText("")
        self.output_file_lineedit.setPlaceholderText(QCoreApplication.translate("ScoringCompletenessSettingsView", u"Define the output file.", None))
#if QT_CONFIG(tooltip)
        self.chosse_button.setToolTip(QCoreApplication.translate("ScoringCompletenessSettingsView", u"Open the file explorer to choose the location and the name of the output file.", None))
#endif // QT_CONFIG(tooltip)
        self.chosse_button.setText(QCoreApplication.translate("ScoringCompletenessSettingsView", u"Choose", None))
    # retranslateUi

