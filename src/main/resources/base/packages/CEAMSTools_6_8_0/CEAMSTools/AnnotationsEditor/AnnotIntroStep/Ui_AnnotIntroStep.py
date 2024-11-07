# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AnnotIntroStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_AnnotIntroStep(object):
    def setupUi(self, AnnotIntroStep):
        if not AnnotIntroStep.objectName():
            AnnotIntroStep.setObjectName(u"AnnotIntroStep")
        AnnotIntroStep.resize(814, 735)
        AnnotIntroStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout = QHBoxLayout(AnnotIntroStep)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(AnnotIntroStep)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.plainTextEdit = QPlainTextEdit(AnnotIntroStep)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setFrameShape(QFrame.NoFrame)
        self.plainTextEdit.setFrameShadow(QFrame.Plain)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(AnnotIntroStep)

        QMetaObject.connectSlotsByName(AnnotIntroStep)
    # setupUi

    def retranslateUi(self, AnnotIntroStep):
        AnnotIntroStep.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("AnnotIntroStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Annotations Editor</span></p></body></html>", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("AnnotIntroStep", u"This tool allows you to delete or edit annotations in batches. Useful for making annotations across a cohort more concise. \n"
"At runtime the annotations in the original files will be overwritten if you ask any change via this tool.\n"
"Make a copy of your annotations files (.tsv, .STS or .ent).\n"
"\n"
"1 - Input Files : \n"
"   Start by opening your PSG files (.edf, .eeg or .sts). \n"
"    - The .tsv file is also needed for the EDF format. \n"
"    - The .sig file is also needed for Stellate format. \n"
"    - The whole NATUS subject folder is also needed for the .eeg format.\n"
"\n"
"2 - Remove or edit : \n"
"   To remove annotations : uncheck the group/name annotation you want to remove.\n"
"   To rename annotations : directly edit the label in the \"Group-Name\" column.\n"
"\n"
"   To modify annotations for a single recording :\n"
"    - Select the recording in the \"PSG Files\" view you want to modify.\n"
"    - Edit or uncheck the annotation in the \"Events from selection\" view.\n"
"\n"
"   To modify "
                        "annotations for the cohort :\n"
"    - Edit or uncheck the annotation in the \"Events from cohort\" view.\n"
"\n"
"   Press \"Refresh\" to update the \"Events from cohort\" view.\n"
"    - It allows to merge edited groups with the same label.\n"
"    - It allows to sort the annotations based on the new label.\n"
"\n"
"   Press \"Back to original labels\" to undo any annotation changes you've made since opening the files.\n"
"\n"
"   Press \"Export\" to display all the changes that will be applied at the runtime.\n"
"    - The first table shows the annotation to rename.\n"
"    - The second table shows the annotations to remove.\n"
"    - The tables can be downloaded as TSV.", None))
    # retranslateUi

