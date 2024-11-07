# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_OutputFiles.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_OutputFiles(object):
    def setupUi(self, OutputFiles):
        if not OutputFiles.objectName():
            OutputFiles.setObjectName(u"OutputFiles")
        OutputFiles.resize(715, 641)
        OutputFiles.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout = QHBoxLayout(OutputFiles)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(OutputFiles)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_5 = QLabel(OutputFiles)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(OutputFiles)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_7 = QLabel(OutputFiles)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout.addWidget(self.label_7)

        self.plainTextEdit = QPlainTextEdit(OutputFiles)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(0, 0))
        self.plainTextEdit.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit.setFrameShape(QFrame.NoFrame)
        self.plainTextEdit.setFrameShadow(QFrame.Plain)
        self.plainTextEdit.setLineWidth(0)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.checkBox_time = QCheckBox(OutputFiles)
        self.checkBox_time.setObjectName(u"checkBox_time")

        self.verticalLayout.addWidget(self.checkBox_time)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_2 = QLabel(OutputFiles)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(OutputFiles)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_8 = QLabel(OutputFiles)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.lineEdit_suffix = QLineEdit(OutputFiles)
        self.lineEdit_suffix.setObjectName(u"lineEdit_suffix")
        self.lineEdit_suffix.setMaximumSize(QSize(350, 16777215))

        self.verticalLayout.addWidget(self.lineEdit_suffix)

        self.label_4 = QLabel(OutputFiles)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(OutputFiles)

        QMetaObject.connectSlotsByName(OutputFiles)
    # setupUi

    def retranslateUi(self, OutputFiles):
        OutputFiles.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Output .TSV file</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("OutputFiles", u"File Location", None))
        self.label_6.setText(QCoreApplication.translate("OutputFiles", u"The extracted annotations are written in the same directory as the input file.", None))
        self.label_7.setText(QCoreApplication.translate("OutputFiles", u"Content", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("OutputFiles", u"The columns of the annotations file are as follows:\n"
"-> 1. group : The group of the event is artifact.\n"
"-> 2. name : The name of the event. Ex. flatline.\n"
"-> 3. start_sec : The onset of the event in second. \n"
"-> 4. duration_sec : The duration of the event in second.\n"
"-> 5. channels : The list of channels on which the event occurs. \n"
"->(optional) 6. time elapsed(HH:MM:SS): The time elapsed since the start of the PSG recording. \n"
"\n"
"Note that the time elapsed is only for debugging purposes and is not included in the Snooz accessory format. Snooz does not support the time elapsed as part of its accessory file.", None))
        self.checkBox_time.setText(QCoreApplication.translate("OutputFiles", u"Add Time Elapsed (HH:MM:SS) since the start of the recording.", None))
        self.label_2.setText(QCoreApplication.translate("OutputFiles", u"Suffix ", None))
        self.label_3.setText(QCoreApplication.translate("OutputFiles", u"The file is named as the PSG recording with the suffix defined below.", None))
        self.label_8.setText(QCoreApplication.translate("OutputFiles", u"The original .tsv file will be overwritten if the suffix is left blank.", None))
        self.lineEdit_suffix.setPlaceholderText(QCoreApplication.translate("OutputFiles", u"_annot", None))
        self.label_4.setText(QCoreApplication.translate("OutputFiles", u"The extension of the file is .tsv (tab separated values).", None))
    # retranslateUi

