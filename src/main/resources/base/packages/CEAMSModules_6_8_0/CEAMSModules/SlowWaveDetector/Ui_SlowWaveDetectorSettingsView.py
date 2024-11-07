# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SlowWaveDetectorSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_SlowWaveDetectorSettingsView(object):
    def setupUi(self, SlowWaveDetectorSettingsView):
        if not SlowWaveDetectorSettingsView.objectName():
            SlowWaveDetectorSettingsView.setObjectName(u"SlowWaveDetectorSettingsView")
        SlowWaveDetectorSettingsView.resize(574, 390)
        SlowWaveDetectorSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.gridLayout_2 = QGridLayout(SlowWaveDetectorSettingsView)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(SlowWaveDetectorSettingsView)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_14 = QLabel(SlowWaveDetectorSettingsView)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 8, 2, 1, 1)

        self.label_10 = QLabel(SlowWaveDetectorSettingsView)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 7, 2, 1, 1)

        self.label_4 = QLabel(SlowWaveDetectorSettingsView)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 6, 1, 1, 1)

        self.spinBox_min_pos = QSpinBox(SlowWaveDetectorSettingsView)
        self.spinBox_min_pos.setObjectName(u"spinBox_min_pos")
        self.spinBox_min_pos.setMaximum(3000)

        self.gridLayout.addWidget(self.spinBox_min_pos, 8, 3, 1, 1)

        self.label = QLabel(SlowWaveDetectorSettingsView)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)

        self.spinBox_max_pos = QSpinBox(SlowWaveDetectorSettingsView)
        self.spinBox_max_pos.setObjectName(u"spinBox_max_pos")
        self.spinBox_max_pos.setMaximum(3000)

        self.gridLayout.addWidget(self.spinBox_max_pos, 8, 5, 1, 1)

        self.label_3 = QLabel(SlowWaveDetectorSettingsView)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.label_2 = QLabel(SlowWaveDetectorSettingsView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1)

        self.doubleSpinBox_neg_amp = QDoubleSpinBox(SlowWaveDetectorSettingsView)
        self.doubleSpinBox_neg_amp.setObjectName(u"doubleSpinBox_neg_amp")
        self.doubleSpinBox_neg_amp.setMaximum(200.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_neg_amp, 6, 2, 1, 4)

        self.comboBox_sex = QComboBox(SlowWaveDetectorSettingsView)
        self.comboBox_sex.addItem("")
        self.comboBox_sex.addItem("")
        self.comboBox_sex.setObjectName(u"comboBox_sex")
        self.comboBox_sex.setEnabled(False)

        self.gridLayout.addWidget(self.comboBox_sex, 11, 2, 1, 4)

        self.label_6 = QLabel(SlowWaveDetectorSettingsView)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(130, 0))
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 7, 1, 1, 1)

        self.label_11 = QLabel(SlowWaveDetectorSettingsView)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(50, 0))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 7, 4, 1, 1)

        self.label_15 = QLabel(SlowWaveDetectorSettingsView)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_15, 8, 4, 1, 1)

        self.spinBox_years = QSpinBox(SlowWaveDetectorSettingsView)
        self.spinBox_years.setObjectName(u"spinBox_years")
        self.spinBox_years.setEnabled(False)
        self.spinBox_years.setMinimumSize(QSize(50, 0))
        self.spinBox_years.setMaximum(122)

        self.gridLayout.addWidget(self.spinBox_years, 10, 2, 1, 1)

        self.event_name_lineedit = QLineEdit(SlowWaveDetectorSettingsView)
        self.event_name_lineedit.setObjectName(u"event_name_lineedit")

        self.gridLayout.addWidget(self.event_name_lineedit, 3, 2, 1, 4)

        self.label_months = QLabel(SlowWaveDetectorSettingsView)
        self.label_months.setObjectName(u"label_months")
        self.label_months.setEnabled(False)

        self.gridLayout.addWidget(self.label_months, 10, 5, 1, 1)

        self.group_lineedit = QLineEdit(SlowWaveDetectorSettingsView)
        self.group_lineedit.setObjectName(u"group_lineedit")

        self.gridLayout.addWidget(self.group_lineedit, 2, 2, 1, 4)

        self.label_years = QLabel(SlowWaveDetectorSettingsView)
        self.label_years.setObjectName(u"label_years")
        self.label_years.setEnabled(False)

        self.gridLayout.addWidget(self.label_years, 10, 3, 1, 1)

        self.spinBox_min_neg = QSpinBox(SlowWaveDetectorSettingsView)
        self.spinBox_min_neg.setObjectName(u"spinBox_min_neg")
        self.spinBox_min_neg.setMinimumSize(QSize(70, 0))
        self.spinBox_min_neg.setMaximum(3000)

        self.gridLayout.addWidget(self.spinBox_min_neg, 7, 3, 1, 1)

        self.label_8 = QLabel(SlowWaveDetectorSettingsView)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)

        self.doubleSpinBox_PaP_amp = QDoubleSpinBox(SlowWaveDetectorSettingsView)
        self.doubleSpinBox_PaP_amp.setObjectName(u"doubleSpinBox_PaP_amp")
        self.doubleSpinBox_PaP_amp.setMaximum(200.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_PaP_amp, 5, 2, 1, 4)

        self.personalized_radioButton = QRadioButton(SlowWaveDetectorSettingsView)
        self.personalized_radioButton.setObjectName(u"personalized_radioButton")

        self.gridLayout.addWidget(self.personalized_radioButton, 0, 5, 1, 1)

        self.spinBox_months = QSpinBox(SlowWaveDetectorSettingsView)
        self.spinBox_months.setObjectName(u"spinBox_months")
        self.spinBox_months.setEnabled(False)
        self.spinBox_months.setMaximum(11)

        self.gridLayout.addWidget(self.spinBox_months, 10, 4, 1, 1)

        self.spinBox_max_neg = QSpinBox(SlowWaveDetectorSettingsView)
        self.spinBox_max_neg.setObjectName(u"spinBox_max_neg")
        self.spinBox_max_neg.setMinimumSize(QSize(70, 0))
        self.spinBox_max_neg.setMaximum(3000)

        self.gridLayout.addWidget(self.spinBox_max_neg, 7, 5, 1, 1)

        self.label_7 = QLabel(SlowWaveDetectorSettingsView)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 8, 1, 1, 1)

        self.carrier_radioButton = QRadioButton(SlowWaveDetectorSettingsView)
        self.carrier_radioButton.setObjectName(u"carrier_radioButton")
        self.carrier_radioButton.setChecked(True)

        self.gridLayout.addWidget(self.carrier_radioButton, 0, 2, 1, 1)

        self.label_9 = QLabel(SlowWaveDetectorSettingsView)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 4, 1, 1, 1, Qt.AlignRight|Qt.AlignVCenter)

        self.label_12 = QLabel(SlowWaveDetectorSettingsView)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 4, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_13 = QLabel(SlowWaveDetectorSettingsView)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 4, 4, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.doubleSpinBox_f_min = QDoubleSpinBox(SlowWaveDetectorSettingsView)
        self.doubleSpinBox_f_min.setObjectName(u"doubleSpinBox_f_min")

        self.gridLayout.addWidget(self.doubleSpinBox_f_min, 4, 3, 1, 1)

        self.doubleSpinBox_f_max = QDoubleSpinBox(SlowWaveDetectorSettingsView)
        self.doubleSpinBox_f_max.setObjectName(u"doubleSpinBox_f_max")

        self.gridLayout.addWidget(self.doubleSpinBox_f_max, 4, 5, 1, 1)

        self.line = QFrame(SlowWaveDetectorSettingsView)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 1, 1, 5)

        self.checkBox_age = QCheckBox(SlowWaveDetectorSettingsView)
        self.checkBox_age.setObjectName(u"checkBox_age")
        self.checkBox_age.setEnabled(False)
        self.checkBox_age.setFont(font)
        self.checkBox_age.setLayoutDirection(Qt.RightToLeft)
        self.checkBox_age.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_age, 10, 1, 1, 1)

        self.checkBox_sex = QCheckBox(SlowWaveDetectorSettingsView)
        self.checkBox_sex.setObjectName(u"checkBox_sex")
        self.checkBox_sex.setEnabled(False)
        self.checkBox_sex.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.checkBox_sex, 11, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.retranslateUi(SlowWaveDetectorSettingsView)

        QMetaObject.connectSlotsByName(SlowWaveDetectorSettingsView)
    # setupUi

    def retranslateUi(self, SlowWaveDetectorSettingsView):
        SlowWaveDetectorSettingsView.setWindowTitle(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"Form", None))
#if QT_CONFIG(tooltip)
        SlowWaveDetectorSettingsView.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"Slow Wave Detector settings", None))
        self.label_14.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"between", None))
        self.label_10.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"between", None))
#if QT_CONFIG(whatsthis)
        self.label_4.setWhatsThis(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"uV", None))
#endif // QT_CONFIG(whatsthis)
        self.label_4.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"Negative amplitude", None))
        self.label.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"Event name", None))
        self.label_3.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"Event group", None))
#if QT_CONFIG(whatsthis)
        self.label_2.setWhatsThis(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"uV", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"Peak-to-peak amplitude", None))
        self.comboBox_sex.setItemText(0, QCoreApplication.translate("SlowWaveDetectorSettingsView", u"Female", None))
        self.comboBox_sex.setItemText(1, QCoreApplication.translate("SlowWaveDetectorSettingsView", u"Male", None))

#if QT_CONFIG(whatsthis)
        self.label_6.setWhatsThis(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"msec", None))
#endif // QT_CONFIG(whatsthis)
        self.label_6.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"Duration of negative part", None))
        self.label_11.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"and", None))
        self.label_15.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"and", None))
        self.label_months.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"months", None))
        self.label_years.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"years", None))
        self.label_8.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"Criterias", None))
        self.personalized_radioButton.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"Personalized settings", None))
#if QT_CONFIG(whatsthis)
        self.label_7.setWhatsThis(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"msec", None))
#endif // QT_CONFIG(whatsthis)
        self.label_7.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"Duration of positive part", None))
        self.carrier_radioButton.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"Carrier", None))
        self.label_9.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"Wave frequency", None))
        self.label_12.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"between", None))
        self.label_13.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"and", None))
#if QT_CONFIG(whatsthis)
        self.checkBox_age.setWhatsThis(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"Modify parameters automatically according to patients age", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBox_age.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"Age", None))
#if QT_CONFIG(whatsthis)
        self.checkBox_sex.setWhatsThis(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"<html><head/><body><p>Modify parameters according to patients sex</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBox_sex.setText(QCoreApplication.translate("SlowWaveDetectorSettingsView", u"Sex", None))
    # retranslateUi

