# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_REMsDetectionYasaSettingsView.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_REMsDetectionYasaSettingsView(object):
    def setupUi(self, REMsDetectionYasaSettingsView):
        if not REMsDetectionYasaSettingsView.objectName():
            REMsDetectionYasaSettingsView.setObjectName(u"REMsDetectionYasaSettingsView")
        REMsDetectionYasaSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        REMsDetectionYasaSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(REMsDetectionYasaSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signal_horizontalLayout = QHBoxLayout()
        self.signal_horizontalLayout.setObjectName(u"signal_horizontalLayout")
        self.signal_label = QLabel(REMsDetectionYasaSettingsView)
        self.signal_label.setObjectName(u"signal_label")

        self.signal_horizontalLayout.addWidget(self.signal_label)

        self.signal_lineedit = QLineEdit(REMsDetectionYasaSettingsView)
        self.signal_lineedit.setObjectName(u"signal_lineedit")

        self.signal_horizontalLayout.addWidget(self.signal_lineedit)


        self.verticalLayout.addLayout(self.signal_horizontalLayout)

        self.events_horizontalLayout = QHBoxLayout()
        self.events_horizontalLayout.setObjectName(u"events_horizontalLayout")
        self.events_label = QLabel(REMsDetectionYasaSettingsView)
        self.events_label.setObjectName(u"events_label")

        self.events_horizontalLayout.addWidget(self.events_label)

        self.events_lineedit = QLineEdit(REMsDetectionYasaSettingsView)
        self.events_lineedit.setObjectName(u"events_lineedit")

        self.events_horizontalLayout.addWidget(self.events_lineedit)


        self.verticalLayout.addLayout(self.events_horizontalLayout)

        self.sleepstages_horizontalLayout = QHBoxLayout()
        self.sleepstages_horizontalLayout.setObjectName(u"sleepstages_horizontalLayout")
        self.sleepstages_label = QLabel(REMsDetectionYasaSettingsView)
        self.sleepstages_label.setObjectName(u"sleepstages_label")

        self.sleepstages_horizontalLayout.addWidget(self.sleepstages_label)

        self.sleepstages_lineedit = QLineEdit(REMsDetectionYasaSettingsView)
        self.sleepstages_lineedit.setObjectName(u"sleepstages_lineedit")

        self.sleepstages_horizontalLayout.addWidget(self.sleepstages_lineedit)


        self.verticalLayout.addLayout(self.sleepstages_horizontalLayout)

        self.thresholds_horizontalLayout = QHBoxLayout()
        self.thresholds_horizontalLayout.setObjectName(u"thresholds_horizontalLayout")
        self.thresholds_label = QLabel(REMsDetectionYasaSettingsView)
        self.thresholds_label.setObjectName(u"thresholds_label")

        self.thresholds_horizontalLayout.addWidget(self.thresholds_label)

        self.thresholds_lineedit = QLineEdit(REMsDetectionYasaSettingsView)
        self.thresholds_lineedit.setObjectName(u"thresholds_lineedit")

        self.thresholds_horizontalLayout.addWidget(self.thresholds_lineedit)


        self.verticalLayout.addLayout(self.thresholds_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(REMsDetectionYasaSettingsView)

        QMetaObject.connectSlotsByName(REMsDetectionYasaSettingsView)
    # setupUi

    def retranslateUi(self, REMsDetectionYasaSettingsView):
        REMsDetectionYasaSettingsView.setWindowTitle(QCoreApplication.translate("REMsDetectionYasaSettingsView", u"Form", None))
        self.signal_label.setText(QCoreApplication.translate("REMsDetectionYasaSettingsView", u"signal", None))
        self.events_label.setText(QCoreApplication.translate("REMsDetectionYasaSettingsView", u"events", None))
        self.sleepstages_label.setText(QCoreApplication.translate("REMsDetectionYasaSettingsView", u"sleepstages", None))
        self.thresholds_label.setText(QCoreApplication.translate("REMsDetectionYasaSettingsView", u"thresholds", None))
    # retranslateUi

