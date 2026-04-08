# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SleepStagingExportResultsSettingsView.ui'
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

class Ui_SleepStagingExportResultsSettingsView(object):
    def setupUi(self, SleepStagingExportResultsSettingsView):
        if not SleepStagingExportResultsSettingsView.objectName():
            SleepStagingExportResultsSettingsView.setObjectName(u"SleepStagingExportResultsSettingsView")
        SleepStagingExportResultsSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        SleepStagingExportResultsSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(SleepStagingExportResultsSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ResultsDataframe_horizontalLayout = QHBoxLayout()
        self.ResultsDataframe_horizontalLayout.setObjectName(u"ResultsDataframe_horizontalLayout")
        self.ResultsDataframe_label = QLabel(SleepStagingExportResultsSettingsView)
        self.ResultsDataframe_label.setObjectName(u"ResultsDataframe_label")

        self.ResultsDataframe_horizontalLayout.addWidget(self.ResultsDataframe_label)

        self.ResultsDataframe_lineedit = QLineEdit(SleepStagingExportResultsSettingsView)
        self.ResultsDataframe_lineedit.setObjectName(u"ResultsDataframe_lineedit")

        self.ResultsDataframe_horizontalLayout.addWidget(self.ResultsDataframe_lineedit)


        self.verticalLayout.addLayout(self.ResultsDataframe_horizontalLayout)

        self.Additional_horizontalLayout = QHBoxLayout()
        self.Additional_horizontalLayout.setObjectName(u"Additional_horizontalLayout")
        self.Additional_label = QLabel(SleepStagingExportResultsSettingsView)
        self.Additional_label.setObjectName(u"Additional_label")

        self.Additional_horizontalLayout.addWidget(self.Additional_label)

        self.Additional_lineedit = QLineEdit(SleepStagingExportResultsSettingsView)
        self.Additional_lineedit.setObjectName(u"Additional_lineedit")

        self.Additional_horizontalLayout.addWidget(self.Additional_lineedit)


        self.verticalLayout.addLayout(self.Additional_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SleepStagingExportResultsSettingsView)

        QMetaObject.connectSlotsByName(SleepStagingExportResultsSettingsView)
    # setupUi

    def retranslateUi(self, SleepStagingExportResultsSettingsView):
        SleepStagingExportResultsSettingsView.setWindowTitle(QCoreApplication.translate("SleepStagingExportResultsSettingsView", u"Form", None))
        self.ResultsDataframe_label.setText(QCoreApplication.translate("SleepStagingExportResultsSettingsView", u"ResultsDataframe", None))
        self.Additional_label.setText(QCoreApplication.translate("SleepStagingExportResultsSettingsView", u"Additional", None))
    # retranslateUi

