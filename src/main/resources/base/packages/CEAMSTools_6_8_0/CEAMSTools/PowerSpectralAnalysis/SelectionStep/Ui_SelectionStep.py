# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SelectionStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_SelectionStep(object):
    def setupUi(self, SelectionStep):
        if not SelectionStep.objectName():
            SelectionStep.setObjectName(u"SelectionStep")
        SelectionStep.resize(707, 753)
        self.verticalLayout_4 = QVBoxLayout(SelectionStep)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(SelectionStep)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)

        self.verticalLayout_4.addWidget(self.label)

        self.radioButton_annotations = QRadioButton(SelectionStep)
        self.radioButton_annotations.setObjectName(u"radioButton_annotations")

        self.verticalLayout_4.addWidget(self.radioButton_annotations)

        self.radioButton_sleep = QRadioButton(SelectionStep)
        self.radioButton_sleep.setObjectName(u"radioButton_sleep")
        self.radioButton_sleep.setChecked(True)

        self.verticalLayout_4.addWidget(self.radioButton_sleep)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(SelectionStep)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.label_3 = QLabel(SelectionStep)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_2 = QLabel(SelectionStep)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.unscored_checkBox = QCheckBox(SelectionStep)
        self.unscored_checkBox.setObjectName(u"unscored_checkBox")
        self.unscored_checkBox.setMinimumSize(QSize(70, 0))

        self.gridLayout.addWidget(self.unscored_checkBox, 0, 0, 1, 1)

        self.n1_checkBox = QCheckBox(SelectionStep)
        self.n1_checkBox.setObjectName(u"n1_checkBox")
        self.n1_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.n1_checkBox, 1, 0, 1, 1)

        self.r_checkBox = QCheckBox(SelectionStep)
        self.r_checkBox.setObjectName(u"r_checkBox")
        self.r_checkBox.setMinimumSize(QSize(70, 0))
        self.r_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.r_checkBox, 2, 1, 1, 1)

        self.w_checkBox = QCheckBox(SelectionStep)
        self.w_checkBox.setObjectName(u"w_checkBox")
        self.w_checkBox.setMinimumSize(QSize(70, 0))
        self.w_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.w_checkBox, 0, 1, 1, 1)

        self.n3_checkBox = QCheckBox(SelectionStep)
        self.n3_checkBox.setObjectName(u"n3_checkBox")
        self.n3_checkBox.setMinimumSize(QSize(70, 0))
        self.n3_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.n3_checkBox, 1, 2, 1, 2)

        self.n2_checkBox = QCheckBox(SelectionStep)
        self.n2_checkBox.setObjectName(u"n2_checkBox")
        self.n2_checkBox.setMinimumSize(QSize(70, 0))
        self.n2_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.n2_checkBox, 1, 1, 1, 1)

        self.s4_checkBox = QCheckBox(SelectionStep)
        self.s4_checkBox.setObjectName(u"s4_checkBox")
        self.s4_checkBox.setEnabled(False)

        self.gridLayout.addWidget(self.s4_checkBox, 2, 0, 1, 1)

        self.nrem_checkBox = QCheckBox(SelectionStep)
        self.nrem_checkBox.setObjectName(u"nrem_checkBox")
        self.nrem_checkBox.setMinimumSize(QSize(70, 0))
        self.nrem_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.nrem_checkBox, 2, 2, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)

        self.label_4 = QLabel(SelectionStep)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_7 = QLabel(SelectionStep)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.in_cycle_checkBox = QCheckBox(SelectionStep)
        self.in_cycle_checkBox.setObjectName(u"in_cycle_checkBox")
        self.in_cycle_checkBox.setEnabled(True)
        self.in_cycle_checkBox.setCheckable(True)
        self.in_cycle_checkBox.setChecked(True)

        self.gridLayout_2.addWidget(self.in_cycle_checkBox, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(SelectionStep)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(0, 50))
        self.plainTextEdit.setMaximumSize(QSize(16777215, 75))
        self.plainTextEdit.setFrameShape(QFrame.HLine)
        self.plainTextEdit.setFrameShadow(QFrame.Plain)
        self.plainTextEdit.setLineWidth(0)
        self.plainTextEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.excl_nremp_checkBox = QCheckBox(SelectionStep)
        self.excl_nremp_checkBox.setObjectName(u"excl_nremp_checkBox")
        self.excl_nremp_checkBox.setMinimumSize(QSize(0, 0))
        self.excl_nremp_checkBox.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_2.addWidget(self.excl_nremp_checkBox)

        self.excl_remp_checkBox = QCheckBox(SelectionStep)
        self.excl_remp_checkBox.setObjectName(u"excl_remp_checkBox")

        self.verticalLayout_2.addWidget(self.excl_remp_checkBox)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.plainTextEdit_2 = QPlainTextEdit(SelectionStep)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setMaximumSize(QSize(16777215, 105))
        self.plainTextEdit_2.setFrameShape(QFrame.HLine)
        self.plainTextEdit_2.setFrameShadow(QFrame.Plain)
        self.plainTextEdit_2.setLineWidth(0)
        self.plainTextEdit_2.setReadOnly(True)

        self.gridLayout_2.addWidget(self.plainTextEdit_2, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.retranslateUi(SelectionStep)
        self.radioButton_annotations.clicked.connect(SelectionStep.update_section_selection_slot)
        self.radioButton_sleep.clicked.connect(SelectionStep.update_section_selection_slot)
        self.nrem_checkBox.clicked.connect(SelectionStep.NREM_checkbox_slot)

        QMetaObject.connectSlotsByName(SelectionStep)
    # setupUi

    def retranslateUi(self, SelectionStep):
        SelectionStep.setWindowTitle("")
#if QT_CONFIG(tooltip)
        SelectionStep.setToolTip("")
#endif // QT_CONFIG(tooltip)
        SelectionStep.setStyleSheet(QCoreApplication.translate("SelectionStep", u"font: 12pt \"Roboto\";", None))
        self.label.setText(QCoreApplication.translate("SelectionStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Section selection to perform the PSA on. </span></p></body></html>", None))
        self.radioButton_annotations.setText(QCoreApplication.translate("SelectionStep", u"Perform PSA on specific annotations (on the next step)", None))
        self.radioButton_sleep.setText(QCoreApplication.translate("SelectionStep", u"Perform PSA on sleep stages and/or cycles (below)", None))
        self.label_5.setText(QCoreApplication.translate("SelectionStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep Stage Selection</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("SelectionStep", u"The PSA is performed per sleep stage.", None))
        self.label_2.setText(QCoreApplication.translate("SelectionStep", u"Select the stages to include in the PSA.", None))
#if QT_CONFIG(tooltip)
        self.unscored_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to perform the PSA on signal unscored.  PSG recording without sleep staging will be marked \"unscored\".", None))
#endif // QT_CONFIG(tooltip)
        self.unscored_checkBox.setText(QCoreApplication.translate("SelectionStep", u"Unscored", None))
#if QT_CONFIG(tooltip)
        self.n1_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to perform the PSA on signal scored N1.", None))
#endif // QT_CONFIG(tooltip)
        self.n1_checkBox.setText(QCoreApplication.translate("SelectionStep", u"N1", None))
#if QT_CONFIG(tooltip)
        self.r_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to perform the PSA on signal scored R (rem).", None))
#endif // QT_CONFIG(tooltip)
        self.r_checkBox.setText(QCoreApplication.translate("SelectionStep", u"R", None))
#if QT_CONFIG(tooltip)
        self.w_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to perform the PSA on signal scored awake.", None))
#endif // QT_CONFIG(tooltip)
        self.w_checkBox.setText(QCoreApplication.translate("SelectionStep", u"Wake", None))
#if QT_CONFIG(tooltip)
        self.n3_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to perform the PSA on signal scored N3.", None))
#endif // QT_CONFIG(tooltip)
        self.n3_checkBox.setText(QCoreApplication.translate("SelectionStep", u"N3", None))
#if QT_CONFIG(tooltip)
        self.n2_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to perform the PSA on signal scored N2.", None))
#endif // QT_CONFIG(tooltip)
        self.n2_checkBox.setText(QCoreApplication.translate("SelectionStep", u"N2", None))
#if QT_CONFIG(tooltip)
        self.s4_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to perform the PSA on signal scored Stage 4.", None))
#endif // QT_CONFIG(tooltip)
        self.s4_checkBox.setText(QCoreApplication.translate("SelectionStep", u"Stage 4", None))
        self.nrem_checkBox.setText(QCoreApplication.translate("SelectionStep", u"NREM", None))
        self.label_4.setText(QCoreApplication.translate("SelectionStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep Period Selection</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("SelectionStep", u"To perform the PSA on specific section of the recording.", None))
#if QT_CONFIG(tooltip)
        self.in_cycle_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to perform the PSA only on the signal included in the sleep cycles i.e. from sleep onset to the last asleep stage.", None))
#endif // QT_CONFIG(tooltip)
        self.in_cycle_checkBox.setText(QCoreApplication.translate("SelectionStep", u"Analyse power in sleep cycle only", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("SelectionStep", u"To perform the PSA only on the signal included in the sleep cycles.\n"
"I.e. from sleep onset to the last asleep stage.\n"
"Useful to run the PSA on complete sleep cycles only (make sure incomplete cycles are not included in the Common Settings for Sleep Cycles in the introduction step of the tool).", None))
#if QT_CONFIG(tooltip)
        self.excl_nremp_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to exclude NREM periods from the Power Spectral Analysis.", None))
#endif // QT_CONFIG(tooltip)
        self.excl_nremp_checkBox.setText(QCoreApplication.translate("SelectionStep", u"Exclude NREM Periods", None))
#if QT_CONFIG(tooltip)
        self.excl_remp_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to exclude REM periods from the Power Spectral Analysis.", None))
#endif // QT_CONFIG(tooltip)
        self.excl_remp_checkBox.setText(QCoreApplication.translate("SelectionStep", u"Exclude REM Periods", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("SelectionStep", u"To exclude sleep periods from the spectral analysis.\n"
"Useful for running PSA on NREM stages included in NREM periods only (not in REM periods). In this case, please check \u201cExclude REM periods\u201d.\n"
"The same idea can be applied for NREM periods.", None))
    # retranslateUi

