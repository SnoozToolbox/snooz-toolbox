# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EventSleepReportSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_EventSleepReportSettingsView(object):
    def setupUi(self, EventSleepReportSettingsView):
        if not EventSleepReportSettingsView.objectName():
            EventSleepReportSettingsView.setObjectName(u"EventSleepReportSettingsView")
        EventSleepReportSettingsView.resize(711, 333)
        self.gridLayout = QGridLayout(EventSleepReportSettingsView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.html_checkBox = QCheckBox(EventSleepReportSettingsView)
        self.html_checkBox.setObjectName(u"html_checkBox")

        self.verticalLayout.addWidget(self.html_checkBox)

        self.csv_report_checkBox = QCheckBox(EventSleepReportSettingsView)
        self.csv_report_checkBox.setObjectName(u"csv_report_checkBox")
        self.csv_report_checkBox.setChecked(True)

        self.verticalLayout.addWidget(self.csv_report_checkBox)

        self.save_events_report_checkBox = QCheckBox(EventSleepReportSettingsView)
        self.save_events_report_checkBox.setObjectName(u"save_events_report_checkBox")

        self.verticalLayout.addWidget(self.save_events_report_checkBox)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.output_prefix_label = QLabel(EventSleepReportSettingsView)
        self.output_prefix_label.setObjectName(u"output_prefix_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.output_prefix_label)

        self.output_prefix_lineedit = QLineEdit(EventSleepReportSettingsView)
        self.output_prefix_lineedit.setObjectName(u"output_prefix_lineedit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.output_prefix_lineedit)

        self.output_directory_label = QLabel(EventSleepReportSettingsView)
        self.output_directory_label.setObjectName(u"output_directory_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.output_directory_label)

        self.output_directory_lineEdit = QLineEdit(EventSleepReportSettingsView)
        self.output_directory_lineEdit.setObjectName(u"output_directory_lineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.output_directory_lineEdit)


        self.verticalLayout.addLayout(self.formLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(340, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.retranslateUi(EventSleepReportSettingsView)

        QMetaObject.connectSlotsByName(EventSleepReportSettingsView)
    # setupUi

    def retranslateUi(self, EventSleepReportSettingsView):
        EventSleepReportSettingsView.setWindowTitle(QCoreApplication.translate("EventSleepReportSettingsView", u"Form", None))
        self.html_checkBox.setText(QCoreApplication.translate("EventSleepReportSettingsView", u"html report", None))
        self.csv_report_checkBox.setText(QCoreApplication.translate("EventSleepReportSettingsView", u"csv report", None))
        self.save_events_report_checkBox.setText(QCoreApplication.translate("EventSleepReportSettingsView", u"save events report", None))
        self.output_prefix_label.setText(QCoreApplication.translate("EventSleepReportSettingsView", u"output prefix", None))
        self.output_directory_label.setText(QCoreApplication.translate("EventSleepReportSettingsView", u"output directory", None))
    # retranslateUi

