# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EpochSignalSettingsView.ui'
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

class Ui_EpochSignalSettingsView(object):
    def setupUi(self, EpochSignalSettingsView):
        if not EpochSignalSettingsView.objectName():
            EpochSignalSettingsView.setObjectName(u"EpochSignalSettingsView")
        EpochSignalSettingsView.resize(711, 333)
        EpochSignalSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(EpochSignalSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.epoch_length_sec_horizontalLayout = QHBoxLayout()
        self.epoch_length_sec_horizontalLayout.setObjectName(u"epoch_length_sec_horizontalLayout")
        self.epoch_length_sec_label = QLabel(EpochSignalSettingsView)
        self.epoch_length_sec_label.setObjectName(u"epoch_length_sec_label")

        self.epoch_length_sec_horizontalLayout.addWidget(self.epoch_length_sec_label)

        self.epoch_length_sec_lineedit = QLineEdit(EpochSignalSettingsView)
        self.epoch_length_sec_lineedit.setObjectName(u"epoch_length_sec_lineedit")

        self.epoch_length_sec_horizontalLayout.addWidget(self.epoch_length_sec_lineedit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.epoch_length_sec_horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.epoch_length_sec_horizontalLayout)

        self.overlap_sec_horizontalLayout = QHBoxLayout()
        self.overlap_sec_horizontalLayout.setObjectName(u"overlap_sec_horizontalLayout")
        self.overlap_sec_label = QLabel(EpochSignalSettingsView)
        self.overlap_sec_label.setObjectName(u"overlap_sec_label")

        self.overlap_sec_horizontalLayout.addWidget(self.overlap_sec_label)

        self.overlap_sec_lineedit = QLineEdit(EpochSignalSettingsView)
        self.overlap_sec_lineedit.setObjectName(u"overlap_sec_lineedit")

        self.overlap_sec_horizontalLayout.addWidget(self.overlap_sec_lineedit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.overlap_sec_horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.overlap_sec_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(EpochSignalSettingsView)

        QMetaObject.connectSlotsByName(EpochSignalSettingsView)
    # setupUi

    def retranslateUi(self, EpochSignalSettingsView):
        EpochSignalSettingsView.setWindowTitle(QCoreApplication.translate("EpochSignalSettingsView", u"Form", None))
        self.epoch_length_sec_label.setText(QCoreApplication.translate("EpochSignalSettingsView", u"epoch_length_sec", None))
        self.overlap_sec_label.setText(QCoreApplication.translate("EpochSignalSettingsView", u"overlap_sec", None))
    # retranslateUi

