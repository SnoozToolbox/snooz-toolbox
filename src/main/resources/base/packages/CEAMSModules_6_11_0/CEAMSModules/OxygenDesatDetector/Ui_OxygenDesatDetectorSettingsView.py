# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_OxygenDesatDetectorSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_OxygenDesatDetectorSettingsView(object):
    def setupUi(self, OxygenDesatDetectorSettingsView):
        if not OxygenDesatDetectorSettingsView.objectName():
            OxygenDesatDetectorSettingsView.setObjectName(u"OxygenDesatDetectorSettingsView")
        OxygenDesatDetectorSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(OxygenDesatDetectorSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.artifact_group_horizontalLayout = QHBoxLayout()
        self.artifact_group_horizontalLayout.setObjectName(u"artifact_group_horizontalLayout")
        self.artifact_group_label = QLabel(OxygenDesatDetectorSettingsView)
        self.artifact_group_label.setObjectName(u"artifact_group_label")

        self.artifact_group_horizontalLayout.addWidget(self.artifact_group_label)

        self.artifact_group_lineedit = QLineEdit(OxygenDesatDetectorSettingsView)
        self.artifact_group_lineedit.setObjectName(u"artifact_group_lineedit")

        self.artifact_group_horizontalLayout.addWidget(self.artifact_group_lineedit)


        self.verticalLayout.addLayout(self.artifact_group_horizontalLayout)

        self.artifact_name_horizontalLayout = QHBoxLayout()
        self.artifact_name_horizontalLayout.setObjectName(u"artifact_name_horizontalLayout")
        self.artifact_name_label = QLabel(OxygenDesatDetectorSettingsView)
        self.artifact_name_label.setObjectName(u"artifact_name_label")

        self.artifact_name_horizontalLayout.addWidget(self.artifact_name_label)

        self.artifact_name_lineedit = QLineEdit(OxygenDesatDetectorSettingsView)
        self.artifact_name_lineedit.setObjectName(u"artifact_name_lineedit")

        self.artifact_name_horizontalLayout.addWidget(self.artifact_name_lineedit)


        self.verticalLayout.addLayout(self.artifact_name_horizontalLayout)

        self.arousal_group_horizontalLayout = QHBoxLayout()
        self.arousal_group_horizontalLayout.setObjectName(u"arousal_group_horizontalLayout")
        self.arousal_group_label = QLabel(OxygenDesatDetectorSettingsView)
        self.arousal_group_label.setObjectName(u"arousal_group_label")

        self.arousal_group_horizontalLayout.addWidget(self.arousal_group_label)

        self.arousal_group_lineedit = QLineEdit(OxygenDesatDetectorSettingsView)
        self.arousal_group_lineedit.setObjectName(u"arousal_group_lineedit")

        self.arousal_group_horizontalLayout.addWidget(self.arousal_group_lineedit)


        self.verticalLayout.addLayout(self.arousal_group_horizontalLayout)

        self.arousal_name_horizontalLayout = QHBoxLayout()
        self.arousal_name_horizontalLayout.setObjectName(u"arousal_name_horizontalLayout")
        self.arousal_name_label = QLabel(OxygenDesatDetectorSettingsView)
        self.arousal_name_label.setObjectName(u"arousal_name_label")

        self.arousal_name_horizontalLayout.addWidget(self.arousal_name_label)

        self.arousal_name_lineedit = QLineEdit(OxygenDesatDetectorSettingsView)
        self.arousal_name_lineedit.setObjectName(u"arousal_name_lineedit")

        self.arousal_name_horizontalLayout.addWidget(self.arousal_name_lineedit)


        self.verticalLayout.addLayout(self.arousal_name_horizontalLayout)

        self.parameters_oxy_horizontalLayout = QHBoxLayout()
        self.parameters_oxy_horizontalLayout.setObjectName(u"parameters_oxy_horizontalLayout")
        self.parameters_oxy_label = QLabel(OxygenDesatDetectorSettingsView)
        self.parameters_oxy_label.setObjectName(u"parameters_oxy_label")

        self.parameters_oxy_horizontalLayout.addWidget(self.parameters_oxy_label)

        self.parameters_oxy_lineedit = QLineEdit(OxygenDesatDetectorSettingsView)
        self.parameters_oxy_lineedit.setObjectName(u"parameters_oxy_lineedit")

        self.parameters_oxy_horizontalLayout.addWidget(self.parameters_oxy_lineedit)


        self.verticalLayout.addLayout(self.parameters_oxy_horizontalLayout)

        self.parameters_cycle_horizontalLayout = QHBoxLayout()
        self.parameters_cycle_horizontalLayout.setObjectName(u"parameters_cycle_horizontalLayout")
        self.parameters_cycle_label = QLabel(OxygenDesatDetectorSettingsView)
        self.parameters_cycle_label.setObjectName(u"parameters_cycle_label")

        self.parameters_cycle_horizontalLayout.addWidget(self.parameters_cycle_label)

        self.parameters_cycle_lineedit = QLineEdit(OxygenDesatDetectorSettingsView)
        self.parameters_cycle_lineedit.setObjectName(u"parameters_cycle_lineedit")

        self.parameters_cycle_horizontalLayout.addWidget(self.parameters_cycle_lineedit)


        self.verticalLayout.addLayout(self.parameters_cycle_horizontalLayout)

        self.cohort_filename_horizontalLayout = QHBoxLayout()
        self.cohort_filename_horizontalLayout.setObjectName(u"cohort_filename_horizontalLayout")
        self.cohort_filename_label = QLabel(OxygenDesatDetectorSettingsView)
        self.cohort_filename_label.setObjectName(u"cohort_filename_label")

        self.cohort_filename_horizontalLayout.addWidget(self.cohort_filename_label)

        self.cohort_filename_lineedit = QLineEdit(OxygenDesatDetectorSettingsView)
        self.cohort_filename_lineedit.setObjectName(u"cohort_filename_lineedit")

        self.cohort_filename_horizontalLayout.addWidget(self.cohort_filename_lineedit)


        self.verticalLayout.addLayout(self.cohort_filename_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(OxygenDesatDetectorSettingsView)

        QMetaObject.connectSlotsByName(OxygenDesatDetectorSettingsView)
    # setupUi

    def retranslateUi(self, OxygenDesatDetectorSettingsView):
        OxygenDesatDetectorSettingsView.setWindowTitle(QCoreApplication.translate("OxygenDesatDetectorSettingsView", u"Form", None))
        self.artifact_group_label.setText(QCoreApplication.translate("OxygenDesatDetectorSettingsView", u"artifact_group", None))
        self.artifact_name_label.setText(QCoreApplication.translate("OxygenDesatDetectorSettingsView", u"artifact_name", None))
        self.arousal_group_label.setText(QCoreApplication.translate("OxygenDesatDetectorSettingsView", u"arousal_group", None))
        self.arousal_name_label.setText(QCoreApplication.translate("OxygenDesatDetectorSettingsView", u"arousal_name", None))
        self.parameters_oxy_label.setText(QCoreApplication.translate("OxygenDesatDetectorSettingsView", u"parameters_oxy", None))
        self.parameters_cycle_label.setText(QCoreApplication.translate("OxygenDesatDetectorSettingsView", u"parameters_cycle", None))
        self.cohort_filename_label.setText(QCoreApplication.translate("OxygenDesatDetectorSettingsView", u"cohort_filename", None))
    # retranslateUi

