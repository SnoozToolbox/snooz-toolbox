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
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_SleepBoutsSettingsView(object):
    def setupUi(self, SleepBoutsSettingsView):
        if not SleepBoutsSettingsView.objectName():
            SleepBoutsSettingsView.setObjectName(u"SleepBoutsSettingsView")
        SleepBoutsSettingsView.resize(415, 224)
        SleepBoutsSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(SleepBoutsSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(SleepBoutsSettingsView)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.output_file_lineedit = QLineEdit(SleepBoutsSettingsView)
        self.output_file_lineedit.setObjectName(u"output_file_lineedit")

        self.horizontalLayout.addWidget(self.output_file_lineedit)

        self.choose_file_pushbutton = QPushButton(SleepBoutsSettingsView)
        self.choose_file_pushbutton.setObjectName(u"choose_file_pushbutton")

        self.horizontalLayout.addWidget(self.choose_file_pushbutton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.export_seconds_radiobutton = QRadioButton(SleepBoutsSettingsView)
        self.export_seconds_radiobutton.setObjectName(u"export_seconds_radiobutton")

        self.verticalLayout.addWidget(self.export_seconds_radiobutton)

        self.export_epochs_radiobutton = QRadioButton(SleepBoutsSettingsView)
        self.export_epochs_radiobutton.setObjectName(u"export_epochs_radiobutton")

        self.verticalLayout.addWidget(self.export_epochs_radiobutton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SleepBoutsSettingsView)
        self.choose_file_pushbutton.clicked.connect(SleepBoutsSettingsView.on_choose_ouput_file)

        QMetaObject.connectSlotsByName(SleepBoutsSettingsView)
    # setupUi

    def retranslateUi(self, SleepBoutsSettingsView):
        SleepBoutsSettingsView.setWindowTitle(QCoreApplication.translate("SleepBoutsSettingsView", u"Form", None))
        self.label.setText(QCoreApplication.translate("SleepBoutsSettingsView", u"Output file", None))
        self.choose_file_pushbutton.setText(QCoreApplication.translate("SleepBoutsSettingsView", u"Choose file", None))
        self.export_seconds_radiobutton.setText(QCoreApplication.translate("SleepBoutsSettingsView", u"Export values in seconds", None))
        self.export_epochs_radiobutton.setText(QCoreApplication.translate("SleepBoutsSettingsView", u"Export values in epochs", None))
    # retranslateUi

