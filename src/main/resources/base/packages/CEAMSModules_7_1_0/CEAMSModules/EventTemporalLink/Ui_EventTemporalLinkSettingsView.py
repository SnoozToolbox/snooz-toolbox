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

class Ui_EventTemporalLinkSettingsView(object):
    def setupUi(self, EventTemporalLinkSettingsView):
        if not EventTemporalLinkSettingsView.objectName():
            EventTemporalLinkSettingsView.setObjectName(u"EventTemporalLinkSettingsView")
        EventTemporalLinkSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(EventTemporalLinkSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.event_reports_horizontalLayout = QHBoxLayout()
        self.event_reports_horizontalLayout.setObjectName(u"event_reports_horizontalLayout")
        self.event_reports_label = QLabel(EventTemporalLinkSettingsView)
        self.event_reports_label.setObjectName(u"event_reports_label")

        self.event_reports_horizontalLayout.addWidget(self.event_reports_label)

        self.event_reports_lineedit = QLineEdit(EventTemporalLinkSettingsView)
        self.event_reports_lineedit.setObjectName(u"event_reports_lineedit")

        self.event_reports_horizontalLayout.addWidget(self.event_reports_lineedit)


        self.verticalLayout.addLayout(self.event_reports_horizontalLayout)

        self.record_info_horizontalLayout = QHBoxLayout()
        self.record_info_horizontalLayout.setObjectName(u"record_info_horizontalLayout")
        self.record_info_label = QLabel(EventTemporalLinkSettingsView)
        self.record_info_label.setObjectName(u"record_info_label")

        self.record_info_horizontalLayout.addWidget(self.record_info_label)

        self.record_info_lineedit = QLineEdit(EventTemporalLinkSettingsView)
        self.record_info_lineedit.setObjectName(u"record_info_lineedit")

        self.record_info_horizontalLayout.addWidget(self.record_info_lineedit)


        self.verticalLayout.addLayout(self.record_info_horizontalLayout)

        self.window_size_horizontalLayout = QHBoxLayout()
        self.window_size_horizontalLayout.setObjectName(u"window_size_horizontalLayout")
        self.window_size_label = QLabel(EventTemporalLinkSettingsView)
        self.window_size_label.setObjectName(u"window_size_label")

        self.window_size_horizontalLayout.addWidget(self.window_size_label)

        self.window_size_lineedit = QLineEdit(EventTemporalLinkSettingsView)
        self.window_size_lineedit.setObjectName(u"window_size_lineedit")

        self.window_size_horizontalLayout.addWidget(self.window_size_lineedit)


        self.verticalLayout.addLayout(self.window_size_horizontalLayout)

        self.temporal_links_horizontalLayout = QHBoxLayout()
        self.temporal_links_horizontalLayout.setObjectName(u"temporal_links_horizontalLayout")
        self.temporal_links_label = QLabel(EventTemporalLinkSettingsView)
        self.temporal_links_label.setObjectName(u"temporal_links_label")

        self.temporal_links_horizontalLayout.addWidget(self.temporal_links_label)

        self.temporal_links_lineedit = QLineEdit(EventTemporalLinkSettingsView)
        self.temporal_links_lineedit.setObjectName(u"temporal_links_lineedit")

        self.temporal_links_horizontalLayout.addWidget(self.temporal_links_lineedit)


        self.verticalLayout.addLayout(self.temporal_links_horizontalLayout)

        self.html_report_horizontalLayout = QHBoxLayout()
        self.html_report_horizontalLayout.setObjectName(u"html_report_horizontalLayout")
        self.html_report_label = QLabel(EventTemporalLinkSettingsView)
        self.html_report_label.setObjectName(u"html_report_label")

        self.html_report_horizontalLayout.addWidget(self.html_report_label)

        self.html_report_lineedit = QLineEdit(EventTemporalLinkSettingsView)
        self.html_report_lineedit.setObjectName(u"html_report_lineedit")

        self.html_report_horizontalLayout.addWidget(self.html_report_lineedit)


        self.verticalLayout.addLayout(self.html_report_horizontalLayout)

        self.html_report_config_horizontalLayout = QHBoxLayout()
        self.html_report_config_horizontalLayout.setObjectName(u"html_report_config_horizontalLayout")
        self.html_report_config_label = QLabel(EventTemporalLinkSettingsView)
        self.html_report_config_label.setObjectName(u"html_report_config_label")

        self.html_report_config_horizontalLayout.addWidget(self.html_report_config_label)

        self.html_report_config_lineedit = QLineEdit(EventTemporalLinkSettingsView)
        self.html_report_config_lineedit.setObjectName(u"html_report_config_lineedit")

        self.html_report_config_horizontalLayout.addWidget(self.html_report_config_lineedit)


        self.verticalLayout.addLayout(self.html_report_config_horizontalLayout)

        self.csv_report_horizontalLayout = QHBoxLayout()
        self.csv_report_horizontalLayout.setObjectName(u"csv_report_horizontalLayout")
        self.csv_report_label = QLabel(EventTemporalLinkSettingsView)
        self.csv_report_label.setObjectName(u"csv_report_label")

        self.csv_report_horizontalLayout.addWidget(self.csv_report_label)

        self.csv_report_lineedit = QLineEdit(EventTemporalLinkSettingsView)
        self.csv_report_lineedit.setObjectName(u"csv_report_lineedit")

        self.csv_report_horizontalLayout.addWidget(self.csv_report_lineedit)


        self.verticalLayout.addLayout(self.csv_report_horizontalLayout)

        self.base_output_fullpath_horizontalLayout = QHBoxLayout()
        self.base_output_fullpath_horizontalLayout.setObjectName(u"base_output_fullpath_horizontalLayout")
        self.base_output_fullpath_label = QLabel(EventTemporalLinkSettingsView)
        self.base_output_fullpath_label.setObjectName(u"base_output_fullpath_label")

        self.base_output_fullpath_horizontalLayout.addWidget(self.base_output_fullpath_label)

        self.base_output_fullpath_lineedit = QLineEdit(EventTemporalLinkSettingsView)
        self.base_output_fullpath_lineedit.setObjectName(u"base_output_fullpath_lineedit")

        self.base_output_fullpath_horizontalLayout.addWidget(self.base_output_fullpath_lineedit)


        self.verticalLayout.addLayout(self.base_output_fullpath_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(EventTemporalLinkSettingsView)

        QMetaObject.connectSlotsByName(EventTemporalLinkSettingsView)
    # setupUi

    def retranslateUi(self, EventTemporalLinkSettingsView):
        EventTemporalLinkSettingsView.setWindowTitle(QCoreApplication.translate("EventTemporalLinkSettingsView", u"Form", None))
        self.event_reports_label.setText(QCoreApplication.translate("EventTemporalLinkSettingsView", u"event_reports", None))
        self.record_info_label.setText(QCoreApplication.translate("EventTemporalLinkSettingsView", u"record_info", None))
        self.window_size_label.setText(QCoreApplication.translate("EventTemporalLinkSettingsView", u"window_size", None))
        self.temporal_links_label.setText(QCoreApplication.translate("EventTemporalLinkSettingsView", u"temporal_links", None))
        self.html_report_label.setText(QCoreApplication.translate("EventTemporalLinkSettingsView", u"html_report", None))
        self.html_report_config_label.setText(QCoreApplication.translate("EventTemporalLinkSettingsView", u"html_report_config", None))
        self.csv_report_label.setText(QCoreApplication.translate("EventTemporalLinkSettingsView", u"csv_report", None))
        self.base_output_fullpath_label.setText(QCoreApplication.translate("EventTemporalLinkSettingsView", u"base_output_fullpath", None))
    # retranslateUi

