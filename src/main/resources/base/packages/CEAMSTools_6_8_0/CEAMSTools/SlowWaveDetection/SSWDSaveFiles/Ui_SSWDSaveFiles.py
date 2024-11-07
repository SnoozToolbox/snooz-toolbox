# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SSWDSaveFiles.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc
from . import criteria_rc

class Ui_SSWDSaveFiles(object):
    def setupUi(self, SSWDSaveFiles):
        if not SSWDSaveFiles.objectName():
            SSWDSaveFiles.setObjectName(u"SSWDSaveFiles")
        SSWDSaveFiles.resize(995, 748)
        SSWDSaveFiles.setMinimumSize(QSize(0, 0))
        SSWDSaveFiles.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_4 = QVBoxLayout(SSWDSaveFiles)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_title = QLabel(SSWDSaveFiles)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_title.setFont(font)

        self.verticalLayout_4.addWidget(self.label_title)

        self.label_3 = QLabel(SSWDSaveFiles)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.label_title_2 = QLabel(SSWDSaveFiles)
        self.label_title_2.setObjectName(u"label_title_2")
        self.label_title_2.setFont(font)

        self.verticalLayout_4.addWidget(self.label_title_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(SSWDSaveFiles)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(700, 16777215))
        self.textEdit.setFrameShape(QFrame.HLine)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.checkBox_export_sw = QCheckBox(SSWDSaveFiles)
        self.checkBox_export_sw.setObjectName(u"checkBox_export_sw")

        self.verticalLayout.addWidget(self.checkBox_export_sw)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.image = QLabel(SSWDSaveFiles)
        self.image.setObjectName(u"image")
        self.image.setLineWidth(0)
        self.image.setPixmap(QPixmap(u":/criteria/phase_slow_wave_small.jpg"))
        self.image.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.image)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(SSWDSaveFiles)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.textEdit_2 = QTextEdit(SSWDSaveFiles)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 130))
        self.textEdit_2.setFrameShape(QFrame.HLine)
        self.textEdit_2.setFrameShadow(QFrame.Plain)
        self.textEdit_2.setLineWidth(0)
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_save_cohort = QCheckBox(SSWDSaveFiles)
        self.checkBox_save_cohort.setObjectName(u"checkBox_save_cohort")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_save_cohort.sizePolicy().hasHeightForWidth())
        self.checkBox_save_cohort.setSizePolicy(sizePolicy)
        self.checkBox_save_cohort.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.checkBox_save_cohort)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_cohort_report = QLineEdit(SSWDSaveFiles)
        self.lineEdit_cohort_report.setObjectName(u"lineEdit_cohort_report")
        self.lineEdit_cohort_report.setEnabled(False)
        self.lineEdit_cohort_report.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_cohort_report.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.lineEdit_cohort_report)

        self.pushButto_browse = QPushButton(SSWDSaveFiles)
        self.pushButto_browse.setObjectName(u"pushButto_browse")
        self.pushButto_browse.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButto_browse.sizePolicy().hasHeightForWidth())
        self.pushButto_browse.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.pushButto_browse)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(SSWDSaveFiles)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(SSWDSaveFiles)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.textEdit_3 = QTextEdit(SSWDSaveFiles)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setFrameShape(QFrame.HLine)
        self.textEdit_3.setFrameShadow(QFrame.Plain)
        self.textEdit_3.setLineWidth(0)
        self.textEdit_3.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textEdit_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.retranslateUi(SSWDSaveFiles)
        self.checkBox_export_sw.clicked.connect(SSWDSaveFiles.check_export_sw_file_slot)
        self.pushButto_browse.clicked.connect(SSWDSaveFiles.browse_cohort_slot)
        self.checkBox_save_cohort.clicked.connect(SSWDSaveFiles.check_save_cohort_slot)

        QMetaObject.connectSlotsByName(SSWDSaveFiles)
    # setupUi

    def retranslateUi(self, SSWDSaveFiles):
        SSWDSaveFiles.setWindowTitle("")
        self.label_title.setText(QCoreApplication.translate("SSWDSaveFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Slow wave events</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("SSWDSaveFiles", u"Slow wave events are added in the accessory file (.tsv, .sts or .ent) of each PSG recording.", None))
        self.label_title_2.setText(QCoreApplication.translate("SSWDSaveFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Slow wave characteristics</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("SSWDSaveFiles", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; text-decoration: underline;\">Slow wave details by event level </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">   - </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; color:#000000;\">peak-to-peak amplitude (\u00b5V) corresponds to H to D on the image (A)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0"
                        "; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">   - duration (s) corresponds to T </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; color:#000000;\">on the image (A)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">   - frequency (Hz) corresponds to 1/T </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; color:#000000;\">on the image (A)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">   - </span><span style=\" font-family:'Arial','sans-serif'; color:#000000; background-color:transparent;\">negative peak amplitude </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; color:#000000;\">(\u00b5V) correspond to H on the image (A)</span></p>\n"
"<p style=\" margin-top:0px; margin-"
                        "bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; color:#000000;\">   - </span><a name=\"docs-internal-guid-7597fb9e-7fff-dd5c-4478-b33f09691339\"></a><span style=\" font-family:'Arial','sans-serif'; color:#000000; background-color:transparent;\">n</span><span style=\" font-family:'Arial','sans-serif'; color:#000000; background-color:transparent;\">egative duration (s) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial','sans-serif'; color:#000000; background-color:transparent;\">   - </span><a name=\"docs-internal-guid-f6ea236d-7fff-1fb4-6202-3e00854b0b90\"></a><span style=\" font-family:'Arial','sans-serif'; color:#000000; background-color:transparent;\">p</span><span style=\" font-family:'Arial','sans-serif'; color:#000000; background-color:transparent;\">ositive duration (s)</span></p"
                        ">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; color:#000000;\">   - transition frequency (Hz) corresponds to 1/(2 tau) on the image (A)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; color:#000000;\">   - slope (\u00b5V/s)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; color:#000000;\">        - from the 0 crossing to the min of the negative component</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospac"
                        "e'; color:#000000;\">        - from the min of the negative component to the max of the positive component</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; color:#000000;\">        - from the max of the positive to the 0 crossing</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Droid Sans Mono','monospace','monospace'; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; color:#000000;\">*Files are saved in a new folder named &quot;slow_waves_characteristics&quot; at the cohort report level.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"
                        " margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; color:#000000;\">*Without the cohort report : each file is saved in the same folder as the PSG file.</span></p></body></html>", None))
        self.checkBox_export_sw.setText(QCoreApplication.translate("SSWDSaveFiles", u"To export characteristics of each slow wave (one file per recording)", None))
        self.image.setText("")
        self.label.setText(QCoreApplication.translate("SSWDSaveFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Slow wave cohort report</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("SSWDSaveFiles", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; text-decoration: underline;\">Slow wave details by subject level</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">    - slow wave count</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">    - the average slow wave characteristics listed above</span></p>\n"
"<p style=\" marg"
                        "in-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">        - total (all selected stages)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">        - per sleep stage</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">        - per sleep cycle</span></p></body></html>", None))
        self.checkBox_save_cohort.setText(QCoreApplication.translate("SSWDSaveFiles", u"To save the detailed events report for the cohort (cohort report)", None))
        self.lineEdit_cohort_report.setPlaceholderText(QCoreApplication.translate("SSWDSaveFiles", u"Select the file to save the detailed cohort report...", None))
        self.pushButto_browse.setText(QCoreApplication.translate("SSWDSaveFiles", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("SSWDSaveFiles", u"* The slow wave details are appended at the end of the cohort report if it exists.", None))
        self.label_6.setText(QCoreApplication.translate("SSWDSaveFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep stages</span></p></body></html>", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("SSWDSaveFiles", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sleep stages seen by the slow wave detector are saved in a new folder named &quot;slow_wave_sleep_stages&quot; at the cohort report level.  </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sleep stages selected for detection are useful to compute the slow wave density per division of the night.</p>\n"
"<p style=\"-qt-p"
                        "aragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* Sleep stages files are generated only when the slow wave characteristics files and the slow wave cohort report are generated.</p></body></html>", None))
    # retranslateUi

