# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ROIStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_ROIStep(object):
    def setupUi(self, ROIStep):
        if not ROIStep.objectName():
            ROIStep.setObjectName(u"ROIStep")
        ROIStep.resize(500, 528)
        ROIStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout_2 = QHBoxLayout(ROIStep)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(ROIStep)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.chan_cohort_listWidget = QListWidget(ROIStep)
        self.chan_cohort_listWidget.setObjectName(u"chan_cohort_listWidget")

        self.verticalLayout.addWidget(self.chan_cohort_listWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_rem_ROI = QPushButton(ROIStep)
        self.pushButton_rem_ROI.setObjectName(u"pushButton_rem_ROI")

        self.horizontalLayout.addWidget(self.pushButton_rem_ROI)

        self.add_ROI_pushButton = QPushButton(ROIStep)
        self.add_ROI_pushButton.setObjectName(u"add_ROI_pushButton")

        self.horizontalLayout.addWidget(self.add_ROI_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(215, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.retranslateUi(ROIStep)
        self.add_ROI_pushButton.clicked.connect(ROIStep.add_ROI_slot)
        self.pushButton_rem_ROI.clicked.connect(ROIStep.rem_ROI_slot)

        QMetaObject.connectSlotsByName(ROIStep)
    # setupUi

    def retranslateUi(self, ROIStep):
        ROIStep.setWindowTitle("")
        self.label_3.setText(QCoreApplication.translate("ROIStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Cohort Channel List</span></p></body></html>", None))
        self.pushButton_rem_ROI.setText(QCoreApplication.translate("ROIStep", u"Remove ROI", None))
        self.add_ROI_pushButton.setText(QCoreApplication.translate("ROIStep", u"Add ROI", None))
    # retranslateUi

