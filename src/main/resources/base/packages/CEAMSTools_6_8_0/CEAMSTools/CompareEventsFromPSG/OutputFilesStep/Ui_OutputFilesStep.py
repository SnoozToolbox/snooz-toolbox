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
        OutputFilesStep.resize(701, 757)
        self.verticalLayout_3 = QVBoxLayout(OutputFilesStep)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(OutputFilesStep)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_W = QCheckBox(OutputFilesStep)
        self.checkBox_W.setObjectName(u"checkBox_W")

        self.gridLayout.addWidget(self.checkBox_W, 0, 0, 1, 1)

        self.checkBox_1 = QCheckBox(OutputFilesStep)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_1, 0, 1, 1, 1)

        self.checkBox_R = QCheckBox(OutputFilesStep)
        self.checkBox_R.setObjectName(u"checkBox_R")

        self.gridLayout.addWidget(self.checkBox_R, 1, 0, 1, 1)

        self.checkBox_2 = QCheckBox(OutputFilesStep)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_2, 1, 1, 1, 1)

        self.checkBox_4 = QCheckBox(OutputFilesStep)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(False)

        self.gridLayout.addWidget(self.checkBox_4, 2, 0, 1, 1)

        self.checkBox_3 = QCheckBox(OutputFilesStep)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_3, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label = QLabel(OutputFilesStep)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 15))
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(OutputFilesStep)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 0))
        self.label_2.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_jaccord = QLineEdit(OutputFilesStep)
        self.lineEdit_jaccord.setObjectName(u"lineEdit_jaccord")

        self.horizontalLayout.addWidget(self.lineEdit_jaccord)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textEdit = QTextEdit(OutputFilesStep)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(500, 0))
        self.textEdit.setMaximumSize(QSize(16777215, 125))
        self.textEdit.setFrameShape(QFrame.HLine)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(OutputFilesStep)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 15))
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3)

        self.textEdit_2 = QTextEdit(OutputFilesStep)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 85))
        self.textEdit_2.setFrameShape(QFrame.HLine)
        self.textEdit_2.setLineWidth(0)
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(OutputFilesStep)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(200, 0))
        self.label_4.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_suffix = QLineEdit(OutputFilesStep)
        self.lineEdit_suffix.setObjectName(u"lineEdit_suffix")

        self.horizontalLayout_2.addWidget(self.lineEdit_suffix)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_title = QLabel(OutputFilesStep)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setFont(font)

        self.verticalLayout.addWidget(self.label_title)

        self.checkBox_TP_exp = QCheckBox(OutputFilesStep)
        self.checkBox_TP_exp.setObjectName(u"checkBox_TP_exp")

        self.verticalLayout.addWidget(self.checkBox_TP_exp)

        self.label_6 = QLabel(OutputFilesStep)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.checkBox_FPFN_exp = QCheckBox(OutputFilesStep)
        self.checkBox_FPFN_exp.setObjectName(u"checkBox_FPFN_exp")

        self.verticalLayout.addWidget(self.checkBox_FPFN_exp)

        self.label_7 = QLabel(OutputFilesStep)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(OutputFilesStep)

        QMetaObject.connectSlotsByName(OutputFilesStep)
    # setupUi

    def retranslateUi(self, OutputFilesStep):
        OutputFilesStep.setWindowTitle("")
        OutputFilesStep.setStyleSheet(QCoreApplication.translate("OutputFilesStep", u"font: 12pt \"Roboto\";", None))
        self.label_5.setText(QCoreApplication.translate("OutputFilesStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep stage selection</span></p></body></html>", None))
        self.checkBox_W.setText(QCoreApplication.translate("OutputFilesStep", u"Wake", None))
        self.checkBox_1.setText(QCoreApplication.translate("OutputFilesStep", u"N1", None))
        self.checkBox_R.setText(QCoreApplication.translate("OutputFilesStep", u"R", None))
        self.checkBox_2.setText(QCoreApplication.translate("OutputFilesStep", u"N2", None))
        self.checkBox_4.setText(QCoreApplication.translate("OutputFilesStep", u"Stage 4", None))
        self.checkBox_3.setText(QCoreApplication.translate("OutputFilesStep", u"N3", None))
        self.label.setText(QCoreApplication.translate("OutputFilesStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Performance evaluation</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("OutputFilesStep", u"Jaccord index threshold", None))
        self.textEdit.setHtml(QCoreApplication.translate("OutputFilesStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Note:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    e represents the event from the expert</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    d represents the detection</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Jaccord index : (intersection between e and d) / (union of e and d)</p>\n"
"<p style=\" mar"
                        "gin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    To considere a &quot;d&quot; as a True Positive, the jaccord index must exceed a certain threshold.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Only one &quot;d&quot; can match a &quot;e&quot;, the one with the highest Jaccord index.</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("OutputFilesStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Output file</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("OutputFilesStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The output performance file is written in the same directory as the PSG file.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The performance at by-sample and by-event level are included.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The output file is named as the PSG file with an additional suffix and the extension .tsv.</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("OutputFilesStep", u"Suffix for the performance file", None))
        self.lineEdit_suffix.setPlaceholderText(QCoreApplication.translate("OutputFilesStep", u"_perf", None))
        self.label_title.setText(QCoreApplication.translate("OutputFilesStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Additional output file</span></p></body></html>", None))
        self.checkBox_TP_exp.setText(QCoreApplication.translate("OutputFilesStep", u"Check to export the True Positive (TP) events (detected events that match the expert scoring).", None))
        self.label_6.setText(QCoreApplication.translate("OutputFilesStep", u"    The output file of the TP events is named with the suffix TP.", None))
        self.checkBox_FPFN_exp.setText(QCoreApplication.translate("OutputFilesStep", u"Check to export the False Negative (FN) and False Positive (FP) events (false detections and expert events missed).", None))
        self.label_7.setText(QCoreApplication.translate("OutputFilesStep", u"    The output file of the FN and FP events is named with the suffix FNFP.", None))
    # retranslateUi

