# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SpindleDetectionDoc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from . import spindle_rc
import themes_rc

class Ui_SpindleDetectionDoc(object):
    def setupUi(self, SpindleDetectionDoc):
        if not SpindleDetectionDoc.objectName():
            SpindleDetectionDoc.setObjectName(u"SpindleDetectionDoc")
        SpindleDetectionDoc.resize(1082, 749)
        SpindleDetectionDoc.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_2 = QVBoxLayout(SpindleDetectionDoc)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.spindle_image = QLabel(SpindleDetectionDoc)
        self.spindle_image.setObjectName(u"spindle_image")
        self.spindle_image.setMaximumSize(QSize(16777215, 100))
        self.spindle_image.setPixmap(QPixmap(u":/spindle_moda/e0004-b1-01-05-0001-smp303751_res80.png"))
        self.spindle_image.setScaledContents(False)
        self.spindle_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.spindle_image)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(SpindleDetectionDoc)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.textEdit = QTextEdit(SpindleDetectionDoc)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFrameShape(QFrame.HLine)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(SpindleDetectionDoc)

        QMetaObject.connectSlotsByName(SpindleDetectionDoc)
    # setupUi

    def retranslateUi(self, SpindleDetectionDoc):
        SpindleDetectionDoc.setWindowTitle("")
        self.spindle_image.setText("")
        self.label.setText(QCoreApplication.translate("SpindleDetectionDoc", u"<html><head/><body><p><span style=\" font-weight:600;\">Spindle detection</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("SpindleDetectionDoc", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A spindle is &quot;a train of distinct waves with frequency 11\u201316 Hz (most commonly 12\u201314 Hz) with a duration \u22650.5 s, usually maximal in amplitude using central derivations&quot; [1]</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This tool allows to detect spindles, on specific sleep stages, with the al"
                        "gorithms from (Martin et al. 2013) [2]</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">1 - Input Files : </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	Add your PSG files (.edf, .sts or .eeg). </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	The .tsv file is also needed for the edf format.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	The .sig file is also needed for the Stellate format.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; "
                        "-qt-block-indent:0; text-indent:0px;\">	The whole NATUS subject folder is also needed for the NATUS format. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">2 - Non valid events :</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	Select events to disable the spindle detection (i.e. artefacts previously detected and saved in the accessory file).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\""
                        " text-decoration: underline;\">3 - Spindle Detector : </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	Define the minimum and maximum duration of kept spindles.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	Define in which sleep stage you want to detect spindles.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	You can also choose to detect spindle in the sleep cycles only or to exclude sleep periods from the analysis.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">4 - Output Fi"
                        "les :</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	The spindle events are added into the accessory file (.tsv, .STS or .ent).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	Define your output files for the spindles characteristics (signal characteristics). </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	    - Check &quot;To save the detailed spindles report for the cohort&quot; if wanted and select the filename to save the report.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	    - Check &quot;To export characteristics of each spinlde (one file per recording)&quot; if wanted.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; mar"
                        "gin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">References:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   [1] Iber, C., American Academy of Sleep Medicine, 2007. The AASM Manual for the Scoring of Sleep and Associated Events: Rules, Terminology and Technical Specifications. American Academy of Sleep Medicine. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   [2] N. Martin <span style=\" font-style:italic;\">et al.</span>, \u201cTopography of age-related changes in sleep spindles,\u201d <span style=\" font-style:italic;\">Neurobiol. Aging</span>, vol. 34, no. 2, pp. 468\u2013476, Feb. 2013, doi: <a href=\"https://doi.org/10.1016/j.neurobiolaging.2012.05.020\"><span style=\" text-decoration: underline; colo"
                        "r:#0000ff;\">10.1016/j.neurobiolaging.2012.05.020</span></a>. </p></body></html>", None))
    # retranslateUi

