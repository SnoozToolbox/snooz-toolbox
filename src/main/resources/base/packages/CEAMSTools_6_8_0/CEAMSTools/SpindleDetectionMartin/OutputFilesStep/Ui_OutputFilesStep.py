# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_OutputFilesStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_OutputFilesStep(object):
    def setupUi(self, OutputFilesStep):
        if not OutputFilesStep.objectName():
            OutputFilesStep.setObjectName(u"OutputFilesStep")
        OutputFilesStep.resize(786, 620)
        OutputFilesStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout_3 = QHBoxLayout(OutputFilesStep)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(OutputFilesStep)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(OutputFilesStep)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(OutputFilesStep)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label_4 = QLabel(OutputFilesStep)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(OutputFilesStep)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.textEdit = QTextEdit(OutputFilesStep)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 270))
        self.textEdit.setFrameShape(QFrame.HLine)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit)

        self.checkBox_cohort_file = QCheckBox(OutputFilesStep)
        self.checkBox_cohort_file.setObjectName(u"checkBox_cohort_file")
        self.checkBox_cohort_file.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_cohort_file)

        self.label_8 = QLabel(OutputFilesStep)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cohort_lineedit = QLineEdit(OutputFilesStep)
        self.cohort_lineedit.setObjectName(u"cohort_lineedit")
        self.cohort_lineedit.setMinimumSize(QSize(350, 0))
        self.cohort_lineedit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.cohort_lineedit)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_cohort = QPushButton(OutputFilesStep)
        self.pushButton_cohort.setObjectName(u"pushButton_cohort")

        self.horizontalLayout.addWidget(self.pushButton_cohort)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.checkBox_spindle_file = QCheckBox(OutputFilesStep)
        self.checkBox_spindle_file.setObjectName(u"checkBox_spindle_file")

        self.verticalLayout_2.addWidget(self.checkBox_spindle_file)

        self.label_7 = QLabel(OutputFilesStep)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_6 = QLabel(OutputFilesStep)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(175, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.retranslateUi(OutputFilesStep)
        self.pushButton_cohort.clicked.connect(OutputFilesStep.browse_cohort_slot)
        self.checkBox_cohort_file.clicked.connect(OutputFilesStep.enable_cohort_slot)
        self.checkBox_spindle_file.clicked.connect(OutputFilesStep.enable_spindle_slot)

        QMetaObject.connectSlotsByName(OutputFilesStep)
    # setupUi

    def retranslateUi(self, OutputFilesStep):
        OutputFilesStep.setWindowTitle("")
        self.label_2.setText(QCoreApplication.translate("OutputFilesStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Spindle events</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("OutputFilesStep", u"Spindle events are added in the accessory file (.tsv, .sts or .ent)", None))
        self.label_3.setText(QCoreApplication.translate("OutputFilesStep", u"Spindle events are defined as [group, name, start_sec, duration_sec, channels]", None))
        self.label_4.setText(QCoreApplication.translate("OutputFilesStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Spindle characteristics</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("OutputFilesStep", u"List of characteristics exported", None))
        self.textEdit.setHtml(QCoreApplication.translate("OutputFilesStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; text-decoration: underline;\">For each spindle</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">   - duration (s)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">   - dominent frequency (Hz), </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; col"
                        "or:#000000;\">where spectral energy is maximum</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; color:#000000;\">   - average frequency (Hz) counting peaks</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; color:#000000;\">   - peak-to-peak amplitude (\u00b5V)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; color:#000000;\">   - Root Mean Square (rms) amplitude (\u00b5V)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Droid Sa"
                        "ns Mono','monospace','monospace'; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; text-decoration: underline;\">For the cohort</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">    - spindle count</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">    - spindle density (spinde count per minute)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">    - the average spindle characteristics listed above</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">        - total (all selected stages)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">        - per sleep stage</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">        - per sleep cycle</span></p></body></html>", None))
        self.checkBox_cohort_file.setText(QCoreApplication.translate("OutputFilesStep", u"To save the detailed events report for the cohort (cohort report)", None))
        self.label_8.setText(QCoreApplication.translate("OutputFilesStep", u"* The spindle details are appended at the end of the cohort report if it exists.", None))
        self.cohort_lineedit.setPlaceholderText(QCoreApplication.translate("OutputFilesStep", u"Select the file to save detailed cohort report...", None))
        self.pushButton_cohort.setText(QCoreApplication.translate("OutputFilesStep", u"Browse", None))
        self.checkBox_spindle_file.setText(QCoreApplication.translate("OutputFilesStep", u"To export characteristics of each spindle (one file per recording)", None))
        self.label_7.setText(QCoreApplication.translate("OutputFilesStep", u"    * Files are saved in a new folder named \"spindles_characteristics\" at the cohort report level.", None))
        self.label_6.setText(QCoreApplication.translate("OutputFilesStep", u"    * Without cohort report : the file is saved in the same folder as the PSG file.", None))
    # retranslateUi

