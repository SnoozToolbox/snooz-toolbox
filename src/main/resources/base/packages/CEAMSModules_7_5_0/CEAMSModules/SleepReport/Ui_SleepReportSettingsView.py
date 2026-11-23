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

class Ui_SleepReportSettingsView(object):
    def setupUi(self, SleepReportSettingsView):
        if not SleepReportSettingsView.objectName():
            SleepReportSettingsView.setObjectName(u"SleepReportSettingsView")
        SleepReportSettingsView.resize(415, 224)
        self.verticalLayout = QVBoxLayout(SleepReportSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(SleepReportSettingsView)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.output_file_lineedit = QLineEdit(SleepReportSettingsView)
        self.output_file_lineedit.setObjectName(u"output_file_lineedit")

        self.horizontalLayout.addWidget(self.output_file_lineedit)

        self.choose_file_pushbutton = QPushButton(SleepReportSettingsView)
        self.choose_file_pushbutton.setObjectName(u"choose_file_pushbutton")

        self.horizontalLayout.addWidget(self.choose_file_pushbutton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SleepReportSettingsView)
        self.choose_file_pushbutton.clicked.connect(SleepReportSettingsView.on_choose_ouput_file)

        QMetaObject.connectSlotsByName(SleepReportSettingsView)
    # setupUi

    def retranslateUi(self, SleepReportSettingsView):
        SleepReportSettingsView.setWindowTitle(QCoreApplication.translate("SleepReportSettingsView", u"Form", None))
        self.label.setText(QCoreApplication.translate("SleepReportSettingsView", u"Output file", None))
        self.choose_file_pushbutton.setText(QCoreApplication.translate("SleepReportSettingsView", u"Choose file", None))
    # retranslateUi

