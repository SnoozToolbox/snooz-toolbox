# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SpindleDetectorSelStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_SpindleDetectorSelStep(object):
    def setupUi(self, SpindleDetectorSelStep):
        if not SpindleDetectorSelStep.objectName():
            SpindleDetectorSelStep.setObjectName(u"SpindleDetectorSelStep")
        SpindleDetectorSelStep.resize(816, 632)
        SpindleDetectorSelStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout_5 = QHBoxLayout(SpindleDetectorSelStep)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(SpindleDetectorSelStep)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.label_8 = QLabel(SpindleDetectorSelStep)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(SpindleDetectorSelStep)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(SpindleDetectorSelStep)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.min_length_lineEdit = QLineEdit(SpindleDetectorSelStep)
        self.min_length_lineEdit.setObjectName(u"min_length_lineEdit")

        self.horizontalLayout.addWidget(self.min_length_lineEdit)

        self.label_4 = QLabel(SpindleDetectorSelStep)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.max_length_lineEdit = QLineEdit(SpindleDetectorSelStep)
        self.max_length_lineEdit.setObjectName(u"max_length_lineEdit")

        self.horizontalLayout.addWidget(self.max_length_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_6 = QLabel(SpindleDetectorSelStep)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_2 = QLabel(SpindleDetectorSelStep)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_n1 = QCheckBox(SpindleDetectorSelStep)
        self.checkBox_n1.setObjectName(u"checkBox_n1")

        self.horizontalLayout_2.addWidget(self.checkBox_n1)

        self.checkBox_n2 = QCheckBox(SpindleDetectorSelStep)
        self.checkBox_n2.setObjectName(u"checkBox_n2")
        self.checkBox_n2.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkBox_n2)

        self.checkBox_n3 = QCheckBox(SpindleDetectorSelStep)
        self.checkBox_n3.setObjectName(u"checkBox_n3")
        self.checkBox_n3.setChecked(False)

        self.horizontalLayout_2.addWidget(self.checkBox_n3)

        self.checkBox_r = QCheckBox(SpindleDetectorSelStep)
        self.checkBox_r.setObjectName(u"checkBox_r")

        self.horizontalLayout_2.addWidget(self.checkBox_r)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label_7 = QLabel(SpindleDetectorSelStep)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_3.addWidget(self.label_7)

        self.label_9 = QLabel(SpindleDetectorSelStep)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_excl_nremp = QCheckBox(SpindleDetectorSelStep)
        self.checkBox_excl_nremp.setObjectName(u"checkBox_excl_nremp")
        self.checkBox_excl_nremp.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.checkBox_excl_nremp)

        self.checkBox_excl_remp = QCheckBox(SpindleDetectorSelStep)
        self.checkBox_excl_remp.setObjectName(u"checkBox_excl_remp")
        self.checkBox_excl_remp.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_excl_remp)

        self.checkBox_only_cycles = QCheckBox(SpindleDetectorSelStep)
        self.checkBox_only_cycles.setObjectName(u"checkBox_only_cycles")
        self.checkBox_only_cycles.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_only_cycles)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.label_10 = QLabel(SpindleDetectorSelStep)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout_3.addWidget(self.label_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(SpindleDetectorSelStep)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_4.addWidget(self.label_11)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.radioButton_detect_spindle = QRadioButton(SpindleDetectorSelStep)
        self.radioButton_detect_spindle.setObjectName(u"radioButton_detect_spindle")
        self.radioButton_detect_spindle.setChecked(True)

        self.verticalLayout_3.addWidget(self.radioButton_detect_spindle)

        self.radioButto_analyse_spindle = QRadioButton(SpindleDetectorSelStep)
        self.radioButto_analyse_spindle.setObjectName(u"radioButto_analyse_spindle")

        self.verticalLayout_3.addWidget(self.radioButto_analyse_spindle)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_4 = QSpacerItem(162, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.retranslateUi(SpindleDetectorSelStep)
        self.checkBox_only_cycles.stateChanged.connect(SpindleDetectorSelStep.detect_in_cycle_only_slot)
        self.radioButto_analyse_spindle.clicked.connect(SpindleDetectorSelStep.radio_button_slot)
        self.radioButton_detect_spindle.clicked.connect(SpindleDetectorSelStep.radio_button_slot)

        QMetaObject.connectSlotsByName(SpindleDetectorSelStep)
    # setupUi

    def retranslateUi(self, SpindleDetectorSelStep):
        SpindleDetectorSelStep.setWindowTitle("")
        self.label_5.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Spindle duration filtering</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Define the minimum and maximum duration of a valid spindle (shorter and longer spindle will be discarded)", None))
        self.label.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Length Limit (s)", None))
        self.label_3.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"min", None))
        self.min_length_lineEdit.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"0.3", None))
        self.label_4.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"max", None))
        self.max_length_lineEdit.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"2.5", None))
        self.label_6.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep stage filtering</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Select the stages for which there will be spindle detection", None))
        self.checkBox_n1.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"N1", None))
        self.checkBox_n2.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"N2", None))
        self.checkBox_n3.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"N3", None))
        self.checkBox_r.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"R", None))
        self.label_7.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep cycle filtering</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Define for which sleep cycles (or periods) there will be spindle detection", None))
        self.checkBox_excl_nremp.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Exclude NREM Periods", None))
        self.checkBox_excl_remp.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Exclude REM Periods", None))
        self.checkBox_only_cycles.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Detection in sleep cycles only", None))
        self.label_10.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Detections and/or analyses</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"The event group and name defined in the Martin configuration page (left panel) will be used. ", None))
        self.radioButton_detect_spindle.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Detect spindles", None))
        self.radioButto_analyse_spindle.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Do not detect spindles, just analyze spindles previously detected and saved in the accessory file.", None))
    # retranslateUi

