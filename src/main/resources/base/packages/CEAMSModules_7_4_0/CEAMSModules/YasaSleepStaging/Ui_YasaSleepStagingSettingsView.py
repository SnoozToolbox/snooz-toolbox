# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_YasaSleepStagingSettingsView.ui'
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

class Ui_YasaSleepStagingSettingsView(object):
    def setupUi(self, YasaSleepStagingSettingsView):
        if not YasaSleepStagingSettingsView.objectName():
            YasaSleepStagingSettingsView.setObjectName(u"YasaSleepStagingSettingsView")
        YasaSleepStagingSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        YasaSleepStagingSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(YasaSleepStagingSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.filename_horizontalLayout = QHBoxLayout()
        self.filename_horizontalLayout.setObjectName(u"filename_horizontalLayout")
        self.filename_label = QLabel(YasaSleepStagingSettingsView)
        self.filename_label.setObjectName(u"filename_label")

        self.filename_horizontalLayout.addWidget(self.filename_label)

        self.filename_lineedit = QLineEdit(YasaSleepStagingSettingsView)
        self.filename_lineedit.setObjectName(u"filename_lineedit")

        self.filename_horizontalLayout.addWidget(self.filename_lineedit)


        self.verticalLayout.addLayout(self.filename_horizontalLayout)

        self.signals_horizontalLayout = QHBoxLayout()
        self.signals_horizontalLayout.setObjectName(u"signals_horizontalLayout")
        self.signals_label = QLabel(YasaSleepStagingSettingsView)
        self.signals_label.setObjectName(u"signals_label")

        self.signals_horizontalLayout.addWidget(self.signals_label)

        self.signals_lineedit = QLineEdit(YasaSleepStagingSettingsView)
        self.signals_lineedit.setObjectName(u"signals_lineedit")

        self.signals_horizontalLayout.addWidget(self.signals_lineedit)


        self.verticalLayout.addLayout(self.signals_horizontalLayout)

        self.sleep_stages_horizontalLayout = QHBoxLayout()
        self.sleep_stages_horizontalLayout.setObjectName(u"sleep_stages_horizontalLayout")
        self.sleep_stages_label = QLabel(YasaSleepStagingSettingsView)
        self.sleep_stages_label.setObjectName(u"sleep_stages_label")

        self.sleep_stages_horizontalLayout.addWidget(self.sleep_stages_label)

        self.sleep_stages_lineedit = QLineEdit(YasaSleepStagingSettingsView)
        self.sleep_stages_lineedit.setObjectName(u"sleep_stages_lineedit")

        self.sleep_stages_horizontalLayout.addWidget(self.sleep_stages_lineedit)


        self.verticalLayout.addLayout(self.sleep_stages_horizontalLayout)

        self.events_horizontalLayout = QHBoxLayout()
        self.events_horizontalLayout.setObjectName(u"events_horizontalLayout")
        self.events_label = QLabel(YasaSleepStagingSettingsView)
        self.events_label.setObjectName(u"events_label")

        self.events_horizontalLayout.addWidget(self.events_label)

        self.events_lineedit = QLineEdit(YasaSleepStagingSettingsView)
        self.events_lineedit.setObjectName(u"events_lineedit")

        self.events_horizontalLayout.addWidget(self.events_lineedit)


        self.verticalLayout.addLayout(self.events_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(YasaSleepStagingSettingsView)

        QMetaObject.connectSlotsByName(YasaSleepStagingSettingsView)
    # setupUi

    def retranslateUi(self, YasaSleepStagingSettingsView):
        YasaSleepStagingSettingsView.setWindowTitle(QCoreApplication.translate("YasaSleepStagingSettingsView", u"Form", None))
        self.filename_label.setText(QCoreApplication.translate("YasaSleepStagingSettingsView", u"filename", None))
        self.signals_label.setText(QCoreApplication.translate("YasaSleepStagingSettingsView", u"signals", None))
        self.sleep_stages_label.setText(QCoreApplication.translate("YasaSleepStagingSettingsView", u"sleep_stages", None))
        self.events_label.setText(QCoreApplication.translate("YasaSleepStagingSettingsView", u"events", None))
    # retranslateUi

