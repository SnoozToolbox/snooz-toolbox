# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Outputfiles.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_Outputfiles(object):
    def setupUi(self, Outputfiles):
        if not Outputfiles.objectName():
            Outputfiles.setObjectName(u"Outputfiles")
        Outputfiles.resize(920, 666)
        self.verticalLayout_4 = QVBoxLayout(Outputfiles)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(Outputfiles)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)

        self.verticalLayout_4.addWidget(self.label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.radioButton_stage = QRadioButton(Outputfiles)
        self.radioButton_stage.setObjectName(u"radioButton_stage")
        self.radioButton_stage.setEnabled(False)
        self.radioButton_stage.setChecked(True)

        self.verticalLayout_3.addWidget(self.radioButton_stage)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.total_checkBox = QCheckBox(Outputfiles)
        self.total_checkBox.setObjectName(u"total_checkBox")
        self.total_checkBox.setMinimumSize(QSize(210, 0))
        self.total_checkBox.setMaximumSize(QSize(210, 16777215))
        self.total_checkBox.setChecked(True)

        self.horizontalLayout.addWidget(self.total_checkBox)

        self.plainTextEdit_tot = QPlainTextEdit(Outputfiles)
        self.plainTextEdit_tot.setObjectName(u"plainTextEdit_tot")
        self.plainTextEdit_tot.setMaximumSize(QSize(16777215, 80))
        self.plainTextEdit_tot.setFrameShape(QFrame.HLine)
        self.plainTextEdit_tot.setFrameShadow(QFrame.Plain)
        self.plainTextEdit_tot.setLineWidth(0)
        self.plainTextEdit_tot.setReadOnly(True)

        self.horizontalLayout.addWidget(self.plainTextEdit_tot)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(30, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.hour_checkBox = QCheckBox(Outputfiles)
        self.hour_checkBox.setObjectName(u"hour_checkBox")
        self.hour_checkBox.setMinimumSize(QSize(210, 0))
        self.hour_checkBox.setMaximumSize(QSize(210, 16777215))
        self.hour_checkBox.setChecked(True)

        self.horizontalLayout_3.addWidget(self.hour_checkBox)

        self.plainTextEdit_hour = QPlainTextEdit(Outputfiles)
        self.plainTextEdit_hour.setObjectName(u"plainTextEdit_hour")
        self.plainTextEdit_hour.setMinimumSize(QSize(0, 80))
        self.plainTextEdit_hour.setMaximumSize(QSize(16777215, 60))
        self.plainTextEdit_hour.setFrameShape(QFrame.HLine)
        self.plainTextEdit_hour.setFrameShadow(QFrame.Plain)
        self.plainTextEdit_hour.setLineWidth(0)
        self.plainTextEdit_hour.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.plainTextEdit_hour)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.cycle_checkBox = QCheckBox(Outputfiles)
        self.cycle_checkBox.setObjectName(u"cycle_checkBox")
        self.cycle_checkBox.setMinimumSize(QSize(210, 0))
        self.cycle_checkBox.setMaximumSize(QSize(210, 16777215))
        self.cycle_checkBox.setChecked(True)

        self.horizontalLayout_4.addWidget(self.cycle_checkBox)

        self.plainTextEdit_cycle = QPlainTextEdit(Outputfiles)
        self.plainTextEdit_cycle.setObjectName(u"plainTextEdit_cycle")
        self.plainTextEdit_cycle.setMinimumSize(QSize(0, 60))
        self.plainTextEdit_cycle.setMaximumSize(QSize(16777215, 45))
        self.plainTextEdit_cycle.setFrameShape(QFrame.HLine)
        self.plainTextEdit_cycle.setFrameShadow(QFrame.Plain)
        self.plainTextEdit_cycle.setLineWidth(0)
        self.plainTextEdit_cycle.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.plainTextEdit_cycle)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.radioButton_annot = QRadioButton(Outputfiles)
        self.radioButton_annot.setObjectName(u"radioButton_annot")
        self.radioButton_annot.setEnabled(False)

        self.verticalLayout_3.addWidget(self.radioButton_annot)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(Outputfiles)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)

        self.verticalLayout_2.addWidget(self.label_4)

        self.plainTextEdit_4 = QPlainTextEdit(Outputfiles)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setMaximumSize(QSize(16777215, 60))
        self.plainTextEdit_4.setFrameShape(QFrame.HLine)
        self.plainTextEdit_4.setFrameShadow(QFrame.Plain)
        self.plainTextEdit_4.setLineWidth(0)
        self.plainTextEdit_4.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.plainTextEdit_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Outputfiles)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.filename_lineEdit = QLineEdit(Outputfiles)
        self.filename_lineEdit.setObjectName(u"filename_lineEdit")
        self.filename_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.filename_lineEdit)

        self.choose_pushButton = QPushButton(Outputfiles)
        self.choose_pushButton.setObjectName(u"choose_pushButton")

        self.horizontalLayout_2.addWidget(self.choose_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 137, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.retranslateUi(Outputfiles)
        self.choose_pushButton.clicked.connect(Outputfiles.choose_button_slot)

        QMetaObject.connectSlotsByName(Outputfiles)
    # setupUi

    def retranslateUi(self, Outputfiles):
        Outputfiles.setWindowTitle("")
        Outputfiles.setStyleSheet(QCoreApplication.translate("Outputfiles", u"font: 12pt \"Roboto\";", None))
        self.label.setText(QCoreApplication.translate("Outputfiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Spectral power distribution to export</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.radioButton_stage.setToolTip(QCoreApplication.translate("Outputfiles", u"To enable the radio button go to the Section Selection Step.", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_stage.setText(QCoreApplication.translate("Outputfiles", u"The spectral power is computed per sleep stage and per hour and/or sleep cycle acording to these selected options:", None))
#if QT_CONFIG(tooltip)
        self.total_checkBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.total_checkBox.setText(QCoreApplication.translate("Outputfiles", u"Total", None))
        self.plainTextEdit_tot.setPlainText(QCoreApplication.translate("Outputfiles", u"To output the spectral power for the whole recording.\n"
"   Warning : If \"Analyse power in sleep cycle only\" in the step \"4-Section Selection\" is checked, \n"
"   the spectral power is computed on epochs included in a sleep cycle, so the gap between cycles are not analysed.\n"
"   Otherwise all the recording is analysed, even before the sleep onset and after the last asleep epoch.", None))
#if QT_CONFIG(tooltip)
        self.hour_checkBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.hour_checkBox.setText(QCoreApplication.translate("Outputfiles", u"Distribution per hour", None))
        self.plainTextEdit_hour.setPlainText(QCoreApplication.translate("Outputfiles", u"To output the spectral power per real clock hour, from hour 1 to 12.  \n"
"The start point is the sleep onset.\n"
"The spectral power value is empty when the hour does not contain any data.", None))
#if QT_CONFIG(tooltip)
        self.cycle_checkBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.cycle_checkBox.setText(QCoreApplication.translate("Outputfiles", u"Distribution per sleep cycle", None))
        self.plainTextEdit_cycle.setPlainText(QCoreApplication.translate("Outputfiles", u"To output the spectral power per sleep cycle, from sleep cycle 1 to 6.\n"
"The spectral power value is empty when the cycle does not exist.", None))
#if QT_CONFIG(tooltip)
        self.radioButton_annot.setToolTip(QCoreApplication.translate("Outputfiles", u"To enable the radio button go to the Section Selection Step.", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_annot.setText(QCoreApplication.translate("Outputfiles", u"The spectral power is computed on selected events.", None))
        self.label_4.setText(QCoreApplication.translate("Outputfiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Output</span></p></body></html>", None))
        self.plainTextEdit_4.setPlainText(QCoreApplication.translate("Outputfiles", u"The output file is a .tsv (tab separated values) file. Each line is specific to a subject, a channel and a frequency band. Warning : the PSA data is added (appended) to the output file, the output file will be modified each time the PSA tool is run.", None))
        self.label_3.setText(QCoreApplication.translate("Outputfiles", u"Filename", None))
        self.filename_lineEdit.setInputMask("")
        self.filename_lineEdit.setText("")
        self.filename_lineEdit.setPlaceholderText(QCoreApplication.translate("Outputfiles", u"Select the file to save the PSA", None))
        self.choose_pushButton.setText(QCoreApplication.translate("Outputfiles", u"Choose", None))
    # retranslateUi

