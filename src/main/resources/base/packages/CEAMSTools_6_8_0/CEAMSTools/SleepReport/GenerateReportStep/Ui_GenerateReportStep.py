# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_GenerateReportStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_GenerateReportStep(object):
    def setupUi(self, GenerateReportStep):
        if not GenerateReportStep.objectName():
            GenerateReportStep.setObjectName(u"GenerateReportStep")
        GenerateReportStep.resize(730, 590)
        self.verticalLayout = QVBoxLayout(GenerateReportStep)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(GenerateReportStep)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.csv_report_checkbox = QCheckBox(self.groupBox)
        self.csv_report_checkbox.setObjectName(u"csv_report_checkbox")

        self.verticalLayout_2.addWidget(self.csv_report_checkbox)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(GenerateReportStep)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.output_lineedit = QLineEdit(GenerateReportStep)
        self.output_lineedit.setObjectName(u"output_lineedit")

        self.horizontalLayout.addWidget(self.output_lineedit)

        self.choose_pushbutton = QPushButton(GenerateReportStep)
        self.choose_pushbutton.setObjectName(u"choose_pushbutton")

        self.horizontalLayout.addWidget(self.choose_pushbutton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(GenerateReportStep)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.prefix_lineedit = QLineEdit(GenerateReportStep)
        self.prefix_lineedit.setObjectName(u"prefix_lineedit")

        self.horizontalLayout_2.addWidget(self.prefix_lineedit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_2 = QLabel(GenerateReportStep)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.event_report_listwidget = QListWidget(GenerateReportStep)
        self.event_report_listwidget.setObjectName(u"event_report_listwidget")
        self.event_report_listwidget.setEditTriggers(QAbstractItemView.CurrentChanged|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.event_report_listwidget.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.event_report_listwidget)

        self.label_4 = QLabel(GenerateReportStep)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.temporallinks_listwidget = QListWidget(GenerateReportStep)
        self.temporallinks_listwidget.setObjectName(u"temporallinks_listwidget")
        self.temporallinks_listwidget.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.temporallinks_listwidget)


        self.retranslateUi(GenerateReportStep)
        self.choose_pushbutton.clicked.connect(GenerateReportStep.on_choose)

        QMetaObject.connectSlotsByName(GenerateReportStep)
    # setupUi

    def retranslateUi(self, GenerateReportStep):
        GenerateReportStep.setWindowTitle("")
        GenerateReportStep.setStyleSheet(QCoreApplication.translate("GenerateReportStep", u"font: 12pt \"Roboto\";", None))
        self.groupBox.setTitle(QCoreApplication.translate("GenerateReportStep", u"Detailed report", None))
        self.csv_report_checkbox.setText(QCoreApplication.translate("GenerateReportStep", u"CSV report", None))
        self.label.setText(QCoreApplication.translate("GenerateReportStep", u"Output directory", None))
        self.choose_pushbutton.setText(QCoreApplication.translate("GenerateReportStep", u"Choose", None))
        self.label_3.setText(QCoreApplication.translate("GenerateReportStep", u"Report prefix", None))
        self.label_2.setText(QCoreApplication.translate("GenerateReportStep", u"List of event reports to generate", None))
        self.label_4.setText(QCoreApplication.translate("GenerateReportStep", u"List of temporal links report to generate", None))
    # retranslateUi

