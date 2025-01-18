# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SSWDCriterias.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc
from . import sw_pic_rc

class Ui_SSWDCriterias(object):
    def setupUi(self, SSWDCriterias):
        if not SSWDCriterias.objectName():
            SSWDCriterias.setObjectName(u"SSWDCriterias")
        SSWDCriterias.resize(887, 806)
        SSWDCriterias.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_9 = QVBoxLayout(SSWDCriterias)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_16 = QLabel(SSWDCriterias)
        self.label_16.setObjectName(u"label_16")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setLayoutDirection(Qt.LeftToRight)
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.label_16)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_18 = QLabel(SSWDCriterias)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_3.addWidget(self.label_18)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.group_lineedit = QLineEdit(SSWDCriterias)
        self.group_lineedit.setObjectName(u"group_lineedit")

        self.gridLayout_2.addWidget(self.group_lineedit, 0, 1, 1, 1)

        self.label = QLabel(SSWDCriterias)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_3 = QLabel(SSWDCriterias)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.event_name_lineedit = QLineEdit(SSWDCriterias)
        self.event_name_lineedit.setObjectName(u"event_name_lineedit")
        self.event_name_lineedit.setEnabled(True)

        self.gridLayout_2.addWidget(self.event_name_lineedit, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_17 = QLabel(SSWDCriterias)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.verticalLayout_6.addWidget(self.label_17)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton_det = QRadioButton(SSWDCriterias)
        self.buttonGroup = QButtonGroup(SSWDCriterias)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_det)
        self.radioButton_det.setObjectName(u"radioButton_det")
        self.radioButton_det.setEnabled(True)
        self.radioButton_det.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_det)

        self.radioButton_anal = QRadioButton(SSWDCriterias)
        self.buttonGroup.addButton(self.radioButton_anal)
        self.radioButton_anal.setObjectName(u"radioButton_anal")
        self.radioButton_anal.setEnabled(False)

        self.verticalLayout.addWidget(self.radioButton_anal)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_19 = QLabel(SSWDCriterias)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.verticalLayout_4.addWidget(self.label_19)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.checkBox_n1 = QCheckBox(SSWDCriterias)
        self.checkBox_n1.setObjectName(u"checkBox_n1")

        self.horizontalLayout_2.addWidget(self.checkBox_n1)

        self.checkBox_n2 = QCheckBox(SSWDCriterias)
        self.checkBox_n2.setObjectName(u"checkBox_n2")
        self.checkBox_n2.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkBox_n2)

        self.checkBox_n3 = QCheckBox(SSWDCriterias)
        self.checkBox_n3.setObjectName(u"checkBox_n3")
        self.checkBox_n3.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkBox_n3)

        self.checkBox_r = QCheckBox(SSWDCriterias)
        self.checkBox_r.setObjectName(u"checkBox_r")

        self.horizontalLayout_2.addWidget(self.checkBox_r)

        self.checkBox_excl_remp = QCheckBox(SSWDCriterias)
        self.checkBox_excl_remp.setObjectName(u"checkBox_excl_remp")

        self.horizontalLayout_2.addWidget(self.checkBox_excl_remp)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(SSWDCriterias)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_8 = QLabel(SSWDCriterias)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.carrier_radioButton = QRadioButton(SSWDCriterias)
        self.buttonGroup_2 = QButtonGroup(SSWDCriterias)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.carrier_radioButton)
        self.carrier_radioButton.setObjectName(u"carrier_radioButton")
        self.carrier_radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.carrier_radioButton)

        self.personalized_radioButton = QRadioButton(SSWDCriterias)
        self.buttonGroup_2.addButton(self.personalized_radioButton)
        self.personalized_radioButton.setObjectName(u"personalized_radioButton")

        self.horizontalLayout.addWidget(self.personalized_radioButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.line = QFrame(SSWDCriterias)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_sex = QComboBox(SSWDCriterias)
        self.comboBox_sex.addItem("")
        self.comboBox_sex.addItem("")
        self.comboBox_sex.setObjectName(u"comboBox_sex")
        self.comboBox_sex.setEnabled(False)

        self.gridLayout.addWidget(self.comboBox_sex, 6, 1, 1, 2)

        self.spinBox_max_pos = QSpinBox(SSWDCriterias)
        self.spinBox_max_pos.setObjectName(u"spinBox_max_pos")
        self.spinBox_max_pos.setEnabled(False)
        self.spinBox_max_pos.setMaximum(3000)

        self.gridLayout.addWidget(self.spinBox_max_pos, 4, 4, 1, 1)

        self.label_14 = QLabel(SSWDCriterias)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 4, 1, 1, 1)

        self.label_months = QLabel(SSWDCriterias)
        self.label_months.setObjectName(u"label_months")
        self.label_months.setEnabled(False)

        self.gridLayout.addWidget(self.label_months, 5, 4, 1, 1)

        self.label_years = QLabel(SSWDCriterias)
        self.label_years.setObjectName(u"label_years")
        self.label_years.setEnabled(False)

        self.gridLayout.addWidget(self.label_years, 5, 2, 1, 1)

        self.label_12 = QLabel(SSWDCriterias)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 1)

        self.label_6 = QLabel(SSWDCriterias)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.checkBox_age = QCheckBox(SSWDCriterias)
        self.checkBox_age.setObjectName(u"checkBox_age")
        self.checkBox_age.setEnabled(False)
        self.checkBox_age.setFont(font)
        self.checkBox_age.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_age, 5, 0, 1, 1)

        self.doubleSpinBox_f_min = QDoubleSpinBox(SSWDCriterias)
        self.doubleSpinBox_f_min.setObjectName(u"doubleSpinBox_f_min")
        self.doubleSpinBox_f_min.setEnabled(False)

        self.gridLayout.addWidget(self.doubleSpinBox_f_min, 0, 2, 1, 1)

        self.doubleSpinBox_neg_amp = QDoubleSpinBox(SSWDCriterias)
        self.doubleSpinBox_neg_amp.setObjectName(u"doubleSpinBox_neg_amp")
        self.doubleSpinBox_neg_amp.setEnabled(False)
        self.doubleSpinBox_neg_amp.setMaximum(200.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_neg_amp, 2, 1, 1, 1)

        self.label_11 = QLabel(SSWDCriterias)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(50, 0))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 3, 3, 1, 1)

        self.spinBox_min_pos = QSpinBox(SSWDCriterias)
        self.spinBox_min_pos.setObjectName(u"spinBox_min_pos")
        self.spinBox_min_pos.setEnabled(False)
        self.spinBox_min_pos.setMaximum(3000)

        self.gridLayout.addWidget(self.spinBox_min_pos, 4, 2, 1, 1)

        self.label_7 = QLabel(SSWDCriterias)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_13 = QLabel(SSWDCriterias)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 0, 3, 1, 1)

        self.label_2 = QLabel(SSWDCriterias)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.doubleSpinBox_PaP_amp = QDoubleSpinBox(SSWDCriterias)
        self.doubleSpinBox_PaP_amp.setObjectName(u"doubleSpinBox_PaP_amp")
        self.doubleSpinBox_PaP_amp.setEnabled(False)
        self.doubleSpinBox_PaP_amp.setMaximum(200.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_PaP_amp, 1, 1, 1, 1)

        self.label_4 = QLabel(SSWDCriterias)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.checkBox_sex = QCheckBox(SSWDCriterias)
        self.checkBox_sex.setObjectName(u"checkBox_sex")
        self.checkBox_sex.setEnabled(False)

        self.gridLayout.addWidget(self.checkBox_sex, 6, 0, 1, 1)

        self.label_10 = QLabel(SSWDCriterias)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 3, 1, 1, 1)

        self.spinBox_max_neg = QSpinBox(SSWDCriterias)
        self.spinBox_max_neg.setObjectName(u"spinBox_max_neg")
        self.spinBox_max_neg.setEnabled(False)
        self.spinBox_max_neg.setMinimumSize(QSize(70, 0))
        self.spinBox_max_neg.setMaximum(3000)

        self.gridLayout.addWidget(self.spinBox_max_neg, 3, 4, 1, 1)

        self.spinBox_min_neg = QSpinBox(SSWDCriterias)
        self.spinBox_min_neg.setObjectName(u"spinBox_min_neg")
        self.spinBox_min_neg.setEnabled(False)
        self.spinBox_min_neg.setMinimumSize(QSize(70, 0))
        self.spinBox_min_neg.setMaximum(3000)

        self.gridLayout.addWidget(self.spinBox_min_neg, 3, 2, 1, 1)

        self.label_15 = QLabel(SSWDCriterias)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_15, 4, 3, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 7, 1, 1, 1)

        self.spinBox_years = QSpinBox(SSWDCriterias)
        self.spinBox_years.setObjectName(u"spinBox_years")
        self.spinBox_years.setEnabled(False)
        self.spinBox_years.setMinimumSize(QSize(50, 0))
        self.spinBox_years.setMaximum(122)

        self.gridLayout.addWidget(self.spinBox_years, 5, 1, 1, 1)

        self.doubleSpinBox_f_max = QDoubleSpinBox(SSWDCriterias)
        self.doubleSpinBox_f_max.setObjectName(u"doubleSpinBox_f_max")
        self.doubleSpinBox_f_max.setEnabled(False)

        self.gridLayout.addWidget(self.doubleSpinBox_f_max, 0, 4, 1, 1)

        self.label_9 = QLabel(SSWDCriterias)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)

        self.spinBox_months = QSpinBox(SSWDCriterias)
        self.spinBox_months.setObjectName(u"spinBox_months")
        self.spinBox_months.setEnabled(False)
        self.spinBox_months.setMaximum(11)

        self.gridLayout.addWidget(self.spinBox_months, 5, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.SW_picture = QLabel(SSWDCriterias)
        self.SW_picture.setObjectName(u"SW_picture")
        self.SW_picture.setPixmap(QPixmap(u":/sw_pic/phase_slow_wave_small.jpg"))

        self.horizontalLayout_3.addWidget(self.SW_picture)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_8.addLayout(self.verticalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)


        self.retranslateUi(SSWDCriterias)
        self.buttonGroup_2.buttonClicked.connect(SSWDCriterias.on_input_format_changed)
        self.checkBox_age.clicked.connect(SSWDCriterias.on_input_format_changed)
        self.checkBox_sex.clicked.connect(SSWDCriterias.on_input_format_changed)

        QMetaObject.connectSlotsByName(SSWDCriterias)
    # setupUi

    def retranslateUi(self, SSWDCriterias):
        SSWDCriterias.setWindowTitle(QCoreApplication.translate("SSWDCriterias", u"Form", None))
#if QT_CONFIG(tooltip)
        SSWDCriterias.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("SSWDCriterias", u"<html><head/><body><p><span style=\" font-weight:600;\">Slow Wave Event Definition</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("SSWDCriterias", u"Event group and name to label the new detection or to select the annotations to analyze.", None))
        self.label.setText(QCoreApplication.translate("SSWDCriterias", u"Event name", None))
        self.label_3.setText(QCoreApplication.translate("SSWDCriterias", u"Event group", None))
        self.label_17.setText(QCoreApplication.translate("SSWDCriterias", u"<html><head/><body><p><span style=\" font-weight:600;\">Detections and/or analyses</span></p></body></html>", None))
        self.radioButton_det.setText(QCoreApplication.translate("SSWDCriterias", u"Detect slow waves.", None))
        self.radioButton_anal.setText(QCoreApplication.translate("SSWDCriterias", u"Do not detect slow waves, just analyze slow waves previously detected and saved in the accessory file.", None))
        self.label_19.setText(QCoreApplication.translate("SSWDCriterias", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep stages and periods selection</span></p></body></html>", None))
        self.checkBox_n1.setText(QCoreApplication.translate("SSWDCriterias", u"N1", None))
        self.checkBox_n2.setText(QCoreApplication.translate("SSWDCriterias", u"N2", None))
        self.checkBox_n3.setText(QCoreApplication.translate("SSWDCriterias", u"N3", None))
        self.checkBox_r.setText(QCoreApplication.translate("SSWDCriterias", u"R", None))
#if QT_CONFIG(tooltip)
        self.checkBox_excl_remp.setToolTip(QCoreApplication.translate("SSWDCriterias", u"Useful to detect on NREM stages included in NREM periods only (not in REM periods).", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_excl_remp.setText(QCoreApplication.translate("SSWDCriterias", u"Exclude REM Periods", None))
        self.label_5.setText(QCoreApplication.translate("SSWDCriterias", u"<html><head/><body><p><span style=\" font-weight:600;\">Slow Wave Detector Criteria</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("SSWDCriterias", u"Criterias", None))
        self.carrier_radioButton.setText(QCoreApplication.translate("SSWDCriterias", u"Carrier", None))
        self.personalized_radioButton.setText(QCoreApplication.translate("SSWDCriterias", u"Personalized settings", None))
        self.comboBox_sex.setItemText(0, QCoreApplication.translate("SSWDCriterias", u"Female", None))
        self.comboBox_sex.setItemText(1, QCoreApplication.translate("SSWDCriterias", u"Male", None))

        self.label_14.setText(QCoreApplication.translate("SSWDCriterias", u"between", None))
        self.label_months.setText(QCoreApplication.translate("SSWDCriterias", u"months", None))
        self.label_years.setText(QCoreApplication.translate("SSWDCriterias", u"years", None))
        self.label_12.setText(QCoreApplication.translate("SSWDCriterias", u"between", None))
#if QT_CONFIG(whatsthis)
        self.label_6.setWhatsThis(QCoreApplication.translate("SSWDCriterias", u"msec", None))
#endif // QT_CONFIG(whatsthis)
        self.label_6.setText(QCoreApplication.translate("SSWDCriterias", u"Duration (ms) of negative part", None))
#if QT_CONFIG(whatsthis)
        self.checkBox_age.setWhatsThis(QCoreApplication.translate("SSWDCriterias", u"Modify parameters automatically according to patients age", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBox_age.setText(QCoreApplication.translate("SSWDCriterias", u"Age", None))
        self.label_11.setText(QCoreApplication.translate("SSWDCriterias", u"and", None))
#if QT_CONFIG(whatsthis)
        self.label_7.setWhatsThis(QCoreApplication.translate("SSWDCriterias", u"msec", None))
#endif // QT_CONFIG(whatsthis)
        self.label_7.setText(QCoreApplication.translate("SSWDCriterias", u"Duration (ms) of positive part", None))
        self.label_13.setText(QCoreApplication.translate("SSWDCriterias", u"and", None))
#if QT_CONFIG(whatsthis)
        self.label_2.setWhatsThis(QCoreApplication.translate("SSWDCriterias", u"uV", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("SSWDCriterias", u"Peak-to-peak amplitude \u00b5V (H to D)", None))
#if QT_CONFIG(whatsthis)
        self.label_4.setWhatsThis(QCoreApplication.translate("SSWDCriterias", u"uV", None))
#endif // QT_CONFIG(whatsthis)
        self.label_4.setText(QCoreApplication.translate("SSWDCriterias", u"Negative amplitude \u00b5V (H)", None))
#if QT_CONFIG(whatsthis)
        self.checkBox_sex.setWhatsThis(QCoreApplication.translate("SSWDCriterias", u"<html><head/><body><p>Modify parameters according to patients sex</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBox_sex.setText(QCoreApplication.translate("SSWDCriterias", u"Sex", None))
        self.label_10.setText(QCoreApplication.translate("SSWDCriterias", u"between", None))
        self.label_15.setText(QCoreApplication.translate("SSWDCriterias", u"and", None))
        self.label_9.setText(QCoreApplication.translate("SSWDCriterias", u"Wave frequency Hz (1/T)", None))
        self.SW_picture.setText("")
    # retranslateUi

