# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DisplaySettings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_DisplaySettings(object):
    def setupUi(self, DisplaySettings):
        if not DisplaySettings.objectName():
            DisplaySettings.setObjectName(u"DisplaySettings")
        DisplaySettings.resize(1326, 580)
        DisplaySettings.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_7 = QVBoxLayout(DisplaySettings)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_16 = QLabel(DisplaySettings)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_7.addWidget(self.label_16)

        self.label_23 = QLabel(DisplaySettings)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_7.addWidget(self.label_23)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)

        self.label = QLabel(DisplaySettings)
        self.label.setObjectName(u"label")

        self.verticalLayout_7.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.checkBox_subject_avg_auto = QCheckBox(DisplaySettings)
        self.checkBox_subject_avg_auto.setObjectName(u"checkBox_subject_avg_auto")
        self.checkBox_subject_avg_auto.setMaximumSize(QSize(200, 16777215))
        self.checkBox_subject_avg_auto.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkBox_subject_avg_auto)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(DisplaySettings)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)

        self.label_9 = QLabel(DisplaySettings)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_4.addWidget(self.label_9)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_10 = QLabel(DisplaySettings)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.comboBox_subject_avg_chan1 = QComboBox(DisplaySettings)
        self.comboBox_subject_avg_chan1.addItem("")
        self.comboBox_subject_avg_chan1.addItem("")
        self.comboBox_subject_avg_chan1.addItem("")
        self.comboBox_subject_avg_chan1.addItem("")
        self.comboBox_subject_avg_chan1.addItem("")
        self.comboBox_subject_avg_chan1.addItem("")
        self.comboBox_subject_avg_chan1.addItem("")
        self.comboBox_subject_avg_chan1.addItem("")
        self.comboBox_subject_avg_chan1.addItem("")
        self.comboBox_subject_avg_chan1.addItem("")
        self.comboBox_subject_avg_chan1.setObjectName(u"comboBox_subject_avg_chan1")
        self.comboBox_subject_avg_chan1.setEnabled(False)

        self.gridLayout_2.addWidget(self.comboBox_subject_avg_chan1, 1, 0, 1, 1)

        self.comboBox_subject_avg_chan4 = QComboBox(DisplaySettings)
        self.comboBox_subject_avg_chan4.addItem("")
        self.comboBox_subject_avg_chan4.addItem("")
        self.comboBox_subject_avg_chan4.addItem("")
        self.comboBox_subject_avg_chan4.addItem("")
        self.comboBox_subject_avg_chan4.addItem("")
        self.comboBox_subject_avg_chan4.addItem("")
        self.comboBox_subject_avg_chan4.addItem("")
        self.comboBox_subject_avg_chan4.addItem("")
        self.comboBox_subject_avg_chan4.addItem("")
        self.comboBox_subject_avg_chan4.addItem("")
        self.comboBox_subject_avg_chan4.setObjectName(u"comboBox_subject_avg_chan4")
        self.comboBox_subject_avg_chan4.setEnabled(False)

        self.gridLayout_2.addWidget(self.comboBox_subject_avg_chan4, 1, 3, 1, 1)

        self.label_12 = QLabel(DisplaySettings)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 0, 2, 1, 1)

        self.label_13 = QLabel(DisplaySettings)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 0, 3, 1, 1)

        self.label_11 = QLabel(DisplaySettings)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1)

        self.comboBox_subject_avg_chan2 = QComboBox(DisplaySettings)
        self.comboBox_subject_avg_chan2.addItem("")
        self.comboBox_subject_avg_chan2.addItem("")
        self.comboBox_subject_avg_chan2.addItem("")
        self.comboBox_subject_avg_chan2.addItem("")
        self.comboBox_subject_avg_chan2.addItem("")
        self.comboBox_subject_avg_chan2.addItem("")
        self.comboBox_subject_avg_chan2.addItem("")
        self.comboBox_subject_avg_chan2.addItem("")
        self.comboBox_subject_avg_chan2.addItem("")
        self.comboBox_subject_avg_chan2.addItem("")
        self.comboBox_subject_avg_chan2.setObjectName(u"comboBox_subject_avg_chan2")
        self.comboBox_subject_avg_chan2.setEnabled(False)

        self.gridLayout_2.addWidget(self.comboBox_subject_avg_chan2, 1, 1, 1, 1)

        self.comboBox_subject_avg_chan3 = QComboBox(DisplaySettings)
        self.comboBox_subject_avg_chan3.addItem("")
        self.comboBox_subject_avg_chan3.addItem("")
        self.comboBox_subject_avg_chan3.addItem("")
        self.comboBox_subject_avg_chan3.addItem("")
        self.comboBox_subject_avg_chan3.addItem("")
        self.comboBox_subject_avg_chan3.addItem("")
        self.comboBox_subject_avg_chan3.addItem("")
        self.comboBox_subject_avg_chan3.addItem("")
        self.comboBox_subject_avg_chan3.addItem("")
        self.comboBox_subject_avg_chan3.addItem("")
        self.comboBox_subject_avg_chan3.setObjectName(u"comboBox_subject_avg_chan3")
        self.comboBox_subject_avg_chan3.setEnabled(False)

        self.gridLayout_2.addWidget(self.comboBox_subject_avg_chan3, 1, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.label_15 = QLabel(DisplaySettings)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_3.addWidget(self.label_15)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.checkBox_subject_sel_auto = QCheckBox(DisplaySettings)
        self.checkBox_subject_sel_auto.setObjectName(u"checkBox_subject_sel_auto")
        self.checkBox_subject_sel_auto.setMaximumSize(QSize(200, 16777215))
        self.checkBox_subject_sel_auto.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBox_subject_sel_auto)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(DisplaySettings)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(DisplaySettings)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(DisplaySettings)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(DisplaySettings)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_6 = QLabel(DisplaySettings)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.label_7 = QLabel(DisplaySettings)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)

        self.comboBox_subject_sel_cat1 = QComboBox(DisplaySettings)
        self.comboBox_subject_sel_cat1.addItem("")
        self.comboBox_subject_sel_cat1.addItem("")
        self.comboBox_subject_sel_cat1.addItem("")
        self.comboBox_subject_sel_cat1.addItem("")
        self.comboBox_subject_sel_cat1.addItem("")
        self.comboBox_subject_sel_cat1.addItem("")
        self.comboBox_subject_sel_cat1.addItem("")
        self.comboBox_subject_sel_cat1.addItem("")
        self.comboBox_subject_sel_cat1.addItem("")
        self.comboBox_subject_sel_cat1.addItem("")
        self.comboBox_subject_sel_cat1.setObjectName(u"comboBox_subject_sel_cat1")
        self.comboBox_subject_sel_cat1.setEnabled(False)

        self.gridLayout.addWidget(self.comboBox_subject_sel_cat1, 1, 0, 1, 1)

        self.comboBox_subject_sel_cat2 = QComboBox(DisplaySettings)
        self.comboBox_subject_sel_cat2.addItem("")
        self.comboBox_subject_sel_cat2.addItem("")
        self.comboBox_subject_sel_cat2.addItem("")
        self.comboBox_subject_sel_cat2.addItem("")
        self.comboBox_subject_sel_cat2.addItem("")
        self.comboBox_subject_sel_cat2.addItem("")
        self.comboBox_subject_sel_cat2.addItem("")
        self.comboBox_subject_sel_cat2.addItem("")
        self.comboBox_subject_sel_cat2.addItem("")
        self.comboBox_subject_sel_cat2.addItem("")
        self.comboBox_subject_sel_cat2.setObjectName(u"comboBox_subject_sel_cat2")
        self.comboBox_subject_sel_cat2.setEnabled(False)

        self.gridLayout.addWidget(self.comboBox_subject_sel_cat2, 1, 1, 1, 1)

        self.comboBox_subject_sel_cat3 = QComboBox(DisplaySettings)
        self.comboBox_subject_sel_cat3.addItem("")
        self.comboBox_subject_sel_cat3.addItem("")
        self.comboBox_subject_sel_cat3.addItem("")
        self.comboBox_subject_sel_cat3.addItem("")
        self.comboBox_subject_sel_cat3.addItem("")
        self.comboBox_subject_sel_cat3.addItem("")
        self.comboBox_subject_sel_cat3.addItem("")
        self.comboBox_subject_sel_cat3.addItem("")
        self.comboBox_subject_sel_cat3.addItem("")
        self.comboBox_subject_sel_cat3.addItem("")
        self.comboBox_subject_sel_cat3.setObjectName(u"comboBox_subject_sel_cat3")
        self.comboBox_subject_sel_cat3.setEnabled(False)

        self.gridLayout.addWidget(self.comboBox_subject_sel_cat3, 1, 2, 1, 1)

        self.comboBox_subject_sel_cat4 = QComboBox(DisplaySettings)
        self.comboBox_subject_sel_cat4.addItem("")
        self.comboBox_subject_sel_cat4.addItem("")
        self.comboBox_subject_sel_cat4.addItem("")
        self.comboBox_subject_sel_cat4.addItem("")
        self.comboBox_subject_sel_cat4.addItem("")
        self.comboBox_subject_sel_cat4.addItem("")
        self.comboBox_subject_sel_cat4.addItem("")
        self.comboBox_subject_sel_cat4.addItem("")
        self.comboBox_subject_sel_cat4.addItem("")
        self.comboBox_subject_sel_cat4.addItem("")
        self.comboBox_subject_sel_cat4.setObjectName(u"comboBox_subject_sel_cat4")
        self.comboBox_subject_sel_cat4.setEnabled(False)

        self.gridLayout.addWidget(self.comboBox_subject_sel_cat4, 1, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.label_14 = QLabel(DisplaySettings)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_7.addWidget(self.label_14)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.checkBox_cohort_auto = QCheckBox(DisplaySettings)
        self.checkBox_cohort_auto.setObjectName(u"checkBox_cohort_auto")
        self.checkBox_cohort_auto.setMaximumSize(QSize(200, 16777215))
        self.checkBox_cohort_auto.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_cohort_auto)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_17 = QLabel(DisplaySettings)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_6.addWidget(self.label_17)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_18 = QLabel(DisplaySettings)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)

        self.comboBox_cohort_group1 = QComboBox(DisplaySettings)
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.setObjectName(u"comboBox_cohort_group1")
        self.comboBox_cohort_group1.setEnabled(False)

        self.gridLayout_3.addWidget(self.comboBox_cohort_group1, 1, 0, 1, 1)

        self.comboBox_cohort_group4 = QComboBox(DisplaySettings)
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.setObjectName(u"comboBox_cohort_group4")
        self.comboBox_cohort_group4.setEnabled(False)

        self.gridLayout_3.addWidget(self.comboBox_cohort_group4, 1, 3, 1, 1)

        self.label_19 = QLabel(DisplaySettings)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 0, 2, 1, 1)

        self.label_20 = QLabel(DisplaySettings)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 0, 3, 1, 1)

        self.label_21 = QLabel(DisplaySettings)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_3.addWidget(self.label_21, 0, 1, 1, 1)

        self.comboBox_cohort_group2 = QComboBox(DisplaySettings)
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.setObjectName(u"comboBox_cohort_group2")
        self.comboBox_cohort_group2.setEnabled(False)

        self.gridLayout_3.addWidget(self.comboBox_cohort_group2, 1, 1, 1, 1)

        self.comboBox_cohort_group3 = QComboBox(DisplaySettings)
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.setObjectName(u"comboBox_cohort_group3")
        self.comboBox_cohort_group3.setEnabled(False)

        self.gridLayout_3.addWidget(self.comboBox_cohort_group3, 1, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_3)

        self.label_22 = QLabel(DisplaySettings)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_5.addWidget(self.label_22)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 116, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)


        self.retranslateUi(DisplaySettings)
        self.checkBox_cohort_auto.clicked.connect(DisplaySettings.update_colors_slot)
        self.checkBox_subject_avg_auto.clicked.connect(DisplaySettings.update_colors_slot)
        self.checkBox_subject_sel_auto.clicked.connect(DisplaySettings.update_colors_slot)
        self.comboBox_cohort_group1.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_cohort_group2.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_cohort_group3.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_cohort_group4.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_subject_avg_chan1.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_subject_avg_chan2.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_subject_avg_chan3.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_subject_avg_chan4.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_subject_sel_cat1.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_subject_sel_cat2.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_subject_sel_cat3.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_subject_sel_cat4.currentIndexChanged.connect(DisplaySettings.update_colors_slot)

        QMetaObject.connectSlotsByName(DisplaySettings)
    # setupUi

    def retranslateUi(self, DisplaySettings):
        DisplaySettings.setWindowTitle("")
        self.label_16.setText(QCoreApplication.translate("DisplaySettings", u"<html><head/><body><p><span style=\" font-weight:600;\">Colors settings</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("DisplaySettings", u"This page allows you to define the first four colors out of a possibility of ten used in the pictures. Note that the condition groups and channels are not limited to four; ten colors are available.", None))
        self.label.setText(QCoreApplication.translate("DisplaySettings", u"<html><head/><body><p><span style=\" font-weight:600;\">Pictures at the subject level.</span></p></body></html>", None))
        self.checkBox_subject_avg_auto.setText(QCoreApplication.translate("DisplaySettings", u"Auto", None))
        self.label_8.setText(QCoreApplication.translate("DisplaySettings", u"<html><head/><body><p><span style=\" font-weight:600;\">One picture per subject</span> (available when displaying the mean signal curve).</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("DisplaySettings", u"Colors are used to differentiate channels.", None))
        self.label_10.setText(QCoreApplication.translate("DisplaySettings", u"Channel #1", None))
        self.comboBox_subject_avg_chan1.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_subject_avg_chan1.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_subject_avg_chan1.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_subject_avg_chan1.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_subject_avg_chan1.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_subject_avg_chan1.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_subject_avg_chan1.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_subject_avg_chan1.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_subject_avg_chan1.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_subject_avg_chan1.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_subject_avg_chan4.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_subject_avg_chan4.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_subject_avg_chan4.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_subject_avg_chan4.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_subject_avg_chan4.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_subject_avg_chan4.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_subject_avg_chan4.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_subject_avg_chan4.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_subject_avg_chan4.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_subject_avg_chan4.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_subject_avg_chan4.setCurrentText(QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.label_12.setText(QCoreApplication.translate("DisplaySettings", u"Channel #3", None))
        self.label_13.setText(QCoreApplication.translate("DisplaySettings", u"Channel #4", None))
        self.label_11.setText(QCoreApplication.translate("DisplaySettings", u"Channel #2", None))
        self.comboBox_subject_avg_chan2.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_subject_avg_chan2.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_subject_avg_chan2.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_subject_avg_chan2.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_subject_avg_chan2.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_subject_avg_chan2.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_subject_avg_chan2.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_subject_avg_chan2.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_subject_avg_chan2.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_subject_avg_chan2.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_subject_avg_chan2.setCurrentText(QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_subject_avg_chan3.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_subject_avg_chan3.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_subject_avg_chan3.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_subject_avg_chan3.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_subject_avg_chan3.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_subject_avg_chan3.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_subject_avg_chan3.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_subject_avg_chan3.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_subject_avg_chan3.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_subject_avg_chan3.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_subject_avg_chan3.setCurrentText(QCoreApplication.translate("DisplaySettings", u"green", None))
        self.label_15.setText(QCoreApplication.translate("DisplaySettings", u"SW categories are distinguished by the line style when multiple channels are displayed.  The lower colors (for SW categories) are used when there is only a single channel to display.", None))
        self.checkBox_subject_sel_auto.setText(QCoreApplication.translate("DisplaySettings", u"Auto", None))
        self.label_2.setText(QCoreApplication.translate("DisplaySettings", u"<html><head/><body><p><span style=\" font-weight:600;\">One picture per channel</span> (available when displaying all sw signal curves).</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("DisplaySettings", u"Colors are used to differentiate SW categories.", None))
        self.label_4.setText(QCoreApplication.translate("DisplaySettings", u"SW category #1", None))
        self.label_5.setText(QCoreApplication.translate("DisplaySettings", u"SW category #2", None))
        self.label_6.setText(QCoreApplication.translate("DisplaySettings", u"SW category #3", None))
        self.label_7.setText(QCoreApplication.translate("DisplaySettings", u"SW category #4", None))
        self.comboBox_subject_sel_cat1.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_subject_sel_cat1.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_subject_sel_cat1.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_subject_sel_cat1.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_subject_sel_cat1.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_subject_sel_cat1.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_subject_sel_cat1.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_subject_sel_cat1.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_subject_sel_cat1.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_subject_sel_cat1.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_subject_sel_cat2.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_subject_sel_cat2.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_subject_sel_cat2.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_subject_sel_cat2.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_subject_sel_cat2.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_subject_sel_cat2.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_subject_sel_cat2.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_subject_sel_cat2.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_subject_sel_cat2.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_subject_sel_cat2.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_subject_sel_cat2.setCurrentText(QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_subject_sel_cat3.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_subject_sel_cat3.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_subject_sel_cat3.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_subject_sel_cat3.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_subject_sel_cat3.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_subject_sel_cat3.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_subject_sel_cat3.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_subject_sel_cat3.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_subject_sel_cat3.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_subject_sel_cat3.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_subject_sel_cat3.setCurrentText(QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_subject_sel_cat4.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_subject_sel_cat4.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_subject_sel_cat4.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_subject_sel_cat4.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_subject_sel_cat4.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_subject_sel_cat4.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_subject_sel_cat4.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_subject_sel_cat4.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_subject_sel_cat4.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_subject_sel_cat4.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_subject_sel_cat4.setCurrentText(QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.label_14.setText(QCoreApplication.translate("DisplaySettings", u"<html><head/><body><p><span style=\" font-weight:600;\">Pictures at the cohort level.</span></p></body></html>", None))
        self.checkBox_cohort_auto.setText(QCoreApplication.translate("DisplaySettings", u"Auto", None))
        self.label_17.setText(QCoreApplication.translate("DisplaySettings", u"Colors are used to differentiate condition group.", None))
        self.label_18.setText(QCoreApplication.translate("DisplaySettings", u"Group #1", None))
        self.comboBox_cohort_group1.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_cohort_group1.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_cohort_group1.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_cohort_group1.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_cohort_group1.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_cohort_group1.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_cohort_group1.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_cohort_group1.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_cohort_group1.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_cohort_group1.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_cohort_group4.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_cohort_group4.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_cohort_group4.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_cohort_group4.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_cohort_group4.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_cohort_group4.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_cohort_group4.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_cohort_group4.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_cohort_group4.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_cohort_group4.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_cohort_group4.setCurrentText(QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.label_19.setText(QCoreApplication.translate("DisplaySettings", u"Group #3", None))
        self.label_20.setText(QCoreApplication.translate("DisplaySettings", u"Group #4", None))
        self.label_21.setText(QCoreApplication.translate("DisplaySettings", u"Group #2", None))
        self.comboBox_cohort_group2.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_cohort_group2.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_cohort_group2.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_cohort_group2.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_cohort_group2.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_cohort_group2.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_cohort_group2.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_cohort_group2.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_cohort_group2.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_cohort_group2.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_cohort_group2.setCurrentText(QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_cohort_group3.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_cohort_group3.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_cohort_group3.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_cohort_group3.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_cohort_group3.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_cohort_group3.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_cohort_group3.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_cohort_group3.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_cohort_group3.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_cohort_group3.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_cohort_group3.setCurrentText(QCoreApplication.translate("DisplaySettings", u"green", None))
        self.label_22.setText(QCoreApplication.translate("DisplaySettings", u"SW categories are differentiated with the line style.", None))
    # retranslateUi

