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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_SpindleDetectorSumoSettingsView(object):
    def setupUi(self, SpindleDetectorSumoSettingsView):
        if not SpindleDetectorSumoSettingsView.objectName():
            SpindleDetectorSumoSettingsView.setObjectName(u"SpindleDetectorSumoSettingsView")
        SpindleDetectorSumoSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        SpindleDetectorSumoSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(SpindleDetectorSumoSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.original_signals_horizontalLayout = QHBoxLayout()
        self.original_signals_horizontalLayout.setObjectName(u"original_signals_horizontalLayout")
        self.original_signals_label = QLabel(SpindleDetectorSumoSettingsView)
        self.original_signals_label.setObjectName(u"original_signals_label")

        self.original_signals_horizontalLayout.addWidget(self.original_signals_label)

        self.original_signals_lineedit = QLineEdit(SpindleDetectorSumoSettingsView)
        self.original_signals_lineedit.setObjectName(u"original_signals_lineedit")

        self.original_signals_horizontalLayout.addWidget(self.original_signals_lineedit)


        self.verticalLayout.addLayout(self.original_signals_horizontalLayout)

        self.cleaned_signals_horizontalLayout = QHBoxLayout()
        self.cleaned_signals_horizontalLayout.setObjectName(u"cleaned_signals_horizontalLayout")
        self.cleaned_signals_label = QLabel(SpindleDetectorSumoSettingsView)
        self.cleaned_signals_label.setObjectName(u"cleaned_signals_label")

        self.cleaned_signals_horizontalLayout.addWidget(self.cleaned_signals_label)

        self.cleaned_signals_lineedit = QLineEdit(SpindleDetectorSumoSettingsView)
        self.cleaned_signals_lineedit.setObjectName(u"cleaned_signals_lineedit")

        self.cleaned_signals_horizontalLayout.addWidget(self.cleaned_signals_lineedit)


        self.verticalLayout.addLayout(self.cleaned_signals_horizontalLayout)

        self.norm_stat_horizontalLayout = QHBoxLayout()
        self.norm_stat_horizontalLayout.setObjectName(u"norm_stat_horizontalLayout")
        self.norm_stat_label = QLabel(SpindleDetectorSumoSettingsView)
        self.norm_stat_label.setObjectName(u"norm_stat_label")

        self.norm_stat_horizontalLayout.addWidget(self.norm_stat_label)

        self.norm_stat_lineedit = QLineEdit(SpindleDetectorSumoSettingsView)
        self.norm_stat_lineedit.setObjectName(u"norm_stat_lineedit")

        self.norm_stat_horizontalLayout.addWidget(self.norm_stat_lineedit)


        self.verticalLayout.addLayout(self.norm_stat_horizontalLayout)

        self.event_group_horizontalLayout = QHBoxLayout()
        self.event_group_horizontalLayout.setObjectName(u"event_group_horizontalLayout")
        self.event_group_label = QLabel(SpindleDetectorSumoSettingsView)
        self.event_group_label.setObjectName(u"event_group_label")

        self.event_group_horizontalLayout.addWidget(self.event_group_label)

        self.event_group_lineedit = QLineEdit(SpindleDetectorSumoSettingsView)
        self.event_group_lineedit.setObjectName(u"event_group_lineedit")

        self.event_group_horizontalLayout.addWidget(self.event_group_lineedit)


        self.verticalLayout.addLayout(self.event_group_horizontalLayout)

        self.event_name_horizontalLayout = QHBoxLayout()
        self.event_name_horizontalLayout.setObjectName(u"event_name_horizontalLayout")
        self.event_name_label = QLabel(SpindleDetectorSumoSettingsView)
        self.event_name_label.setObjectName(u"event_name_label")

        self.event_name_horizontalLayout.addWidget(self.event_name_label)

        self.event_name_lineedit = QLineEdit(SpindleDetectorSumoSettingsView)
        self.event_name_lineedit.setObjectName(u"event_name_lineedit")

        self.event_name_horizontalLayout.addWidget(self.event_name_lineedit)


        self.verticalLayout.addLayout(self.event_name_horizontalLayout)

        self.artifact_events_horizontalLayout = QHBoxLayout()
        self.artifact_events_horizontalLayout.setObjectName(u"artifact_events_horizontalLayout")
        self.artifact_events_label = QLabel(SpindleDetectorSumoSettingsView)
        self.artifact_events_label.setObjectName(u"artifact_events_label")

        self.artifact_events_horizontalLayout.addWidget(self.artifact_events_label)

        self.artifact_events_lineedit = QLineEdit(SpindleDetectorSumoSettingsView)
        self.artifact_events_lineedit.setObjectName(u"artifact_events_lineedit")

        self.artifact_events_horizontalLayout.addWidget(self.artifact_events_lineedit)


        self.verticalLayout.addLayout(self.artifact_events_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SpindleDetectorSumoSettingsView)

        QMetaObject.connectSlotsByName(SpindleDetectorSumoSettingsView)
    # setupUi

    def retranslateUi(self, SpindleDetectorSumoSettingsView):
        SpindleDetectorSumoSettingsView.setWindowTitle(QCoreApplication.translate("SpindleDetectorSumoSettingsView", u"Form", None))
        self.original_signals_label.setText(QCoreApplication.translate("SpindleDetectorSumoSettingsView", u"original_signals", None))
        self.cleaned_signals_label.setText(QCoreApplication.translate("SpindleDetectorSumoSettingsView", u"cleaned_signals", None))
        self.norm_stat_label.setText(QCoreApplication.translate("SpindleDetectorSumoSettingsView", u"norm_stat", None))
        self.event_group_label.setText(QCoreApplication.translate("SpindleDetectorSumoSettingsView", u"event_group", None))
        self.event_name_label.setText(QCoreApplication.translate("SpindleDetectorSumoSettingsView", u"event_name", None))
        self.artifact_events_label.setText(QCoreApplication.translate("SpindleDetectorSumoSettingsView", u"artifact_events", None))
    # retranslateUi

