# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_IntroStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_IntroStep(object):
    def setupUi(self, IntroStep):
        if not IntroStep.objectName():
            IntroStep.setObjectName(u"IntroStep")
        IntroStep.resize(758, 639)
        self.verticalLayout = QVBoxLayout(IntroStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(IntroStep)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.plainTextEdit = QPlainTextEdit(IntroStep)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setFrameShape(QFrame.NoFrame)
        self.plainTextEdit.setFrameShadow(QFrame.Plain)
        self.plainTextEdit.setLineWidth(0)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)


        self.retranslateUi(IntroStep)

        QMetaObject.connectSlotsByName(IntroStep)
    # setupUi

    def retranslateUi(self, IntroStep):
        IntroStep.setWindowTitle("")
        IntroStep.setStyleSheet(QCoreApplication.translate("IntroStep", u"font: 12pt \"Roboto\";", None))
        self.label.setText(QCoreApplication.translate("IntroStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Extract Annotations</span></p></body></html>", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("IntroStep", u"To extract annotations from EDF(.tsv), Natus(.ent) or Stellate(.sts) and write them in a Snooz .tsv file.\n"
"\n"
"1 - Input Files :\n"
"     Add the PSG files to extract annotaions from.\n"
"\n"
"2 - Select Annotations :\n"
"     Select the annotations to save in the ouput .tsv file for each PSG recordings. 	\n"
"\n"
"3- Output Files : \n"
"    Define your output file preferences. \n"
"    The extracted annotations are written in the same directory as the input file.\n"
"    The output file is named as the input file with the suffix defined by the user.\n"
"\n"
"    The columns of the annotations file are as follows:\n"
"    -> 1. group : The group of the event is artifact.\n"
"    -> 2. name : The name of the event. Ex. flatline.\n"
"    -> 3. start_sec : The onset of the event in second. \n"
"    -> 4. duration_sec : The duration of the event in second.\n"
"    -> 5. channels : The list of channels on which the event occurs. \n"
"    ->(optional) 6. time elapsed(HH:MM:SS): The time elapsed since the start o"
                        "f the PSG recording. \n"
"\n"
"    Note that the time elapsed time is only for debug purpose and is not included in the Snooz accessory format.\n"
"    Snooz does not support the time elapsed as part of its accessory file.", None))
    # retranslateUi

