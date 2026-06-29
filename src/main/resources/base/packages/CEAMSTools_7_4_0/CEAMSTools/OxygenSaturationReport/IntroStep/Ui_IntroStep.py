# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_IntroStep.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QSizePolicy, QTextEdit, QWidget)
import themes_rc

class Ui_IntroStep(object):
    def setupUi(self, IntroStep):
        if not IntroStep.objectName():
            IntroStep.setObjectName(u"IntroStep")
        IntroStep.resize(1008, 773)
        self.horizontalLayout = QHBoxLayout(IntroStep)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textEdit = QTextEdit(IntroStep)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.textEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.textEdit)


        self.retranslateUi(IntroStep)

        QMetaObject.connectSlotsByName(IntroStep)
    # setupUi

    def retranslateUi(self, IntroStep):
        IntroStep.setWindowTitle("")
        IntroStep.setStyleSheet(QCoreApplication.translate("IntroStep", u"font: 12pt \"Roboto\";", None))
        self.textEdit.setHtml(QCoreApplication.translate("IntroStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Oxygen Saturation Report</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A tool to analyze oxygen saturation, detect oxygen desaturations, and export an Oxygen Saturation Report.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-bloc"
                        "k-indent:0; text-indent:0px;\">Sleep staging is essential because oxygen saturation is particularly relevant during the sleep period (SP).<br />The SP is defined as the duration (in minutes) from the first epoch scored as sleep (N1, N2, N3, R) to the final awakening, including the last epoch scored as sleep.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The desaturation detector is inspired by ABOSA v1.2.2 [1], a freely available automatic oxygen saturation analysis software.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Common settings : <br /><span style=\" font-weight:700; color:#ff0000;\">NOTE:</span><span style=\" color:#ff0000;\"> Please define the sleep cycle configuration to use for the analysis using the blue panel on the left.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">1 - Input Files :</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Add the PSG files to analyze.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto-Regular';\">- European Data Format (EDF) : The .edf and .tsv files must have the exact same filename and be stored in the same directory.<br />- Stellate : The .sig and .sts files must have the exact same filename and be stored in the same directory.<br />- NATUS (</span><span style=\" font-family:'Roboto-Regular'; font-style:italic;\">for CEAMS users</span><span style=\" font-family:'Roboto-Regular';\">) : </span><span style=\" font-family:'MS Shell Dlg 2';\">The entire NATUS subject folder is required.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-"
                        "right:0px; -qt-block-indent:0; text-indent:0px;\">Define the montage and channels for each open file you want to run the tool on.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">2 - Invalid sections :</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The detector includes basic automatic artifact detection (limited to obvious artifacts). <br />Manual annotation of subtle artifacts is recommended prior to analysis.<br />The user must select any annotations to be excluded from the oxygen saturation analysis.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">3 - Detection Settings : </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0"
                        "px; -qt-block-indent:0; text-indent:0px;\">The user must define the oxygen desaturation criteria, including:</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- the oxygen drop threshold (%)<br />- the minimum desaturation duration (s)<br />- the maximum desaturation duration (s)</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">4 - Output Files :</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Cohort Saturation Report</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Cohort Oxygen Saturation Report includes three categories of metrics:</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; ma"
                        "rgin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">1. Oxygen saturation variables</span> <br />Minimum, maximum, and average oxygen saturation per recording, computed for:</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- the full sleep period<br />- sleep halves and thirds<br />- individual sleep cycles<br />- sleep stages</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">2. Oxygen desaturation variables </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- oxygen desaturation index (ODI, events per sleep hour)<br />- desaturation severity (sum of areas under desaturation events, in percent\u00b7sec, over the sleep period)<br />- percentage of sleep time spent in desaturation"
                        "<br />- average and median desaturation characteristics (duration, area, slope, drop)</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">3. Oxygen recovery variables </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Index, severity, percentage of sleep time spent in recovery and the average and median recovery characteristics.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The <span style=\" font-weight:700;\">Total Severity </span>corresponds to the sum of the individual desaturation and recovery areas in percent*sec over the valid sleep period (sec).</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">All variables are computed for the total sleep p"
                        "eriod. <br />Each recording is saved as a single row in the cohort report. New recordings are appended to the existing file.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The user specifies the file location to save the Cohort Oxygen Saturation Report.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Optional outputs</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The detected desaturation and recovery events can be saved in the accessory file associated with the recording, for review.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Annotation for desaturation events : group = SpO2; name = desat_SpO2; <br />Annotation for recovery events : gro"
                        "up = SpO2; name = recovery_SpO2; </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Lato','proxima-nova','Helvetica Neue','Arial','sans-serif'; font-size:16px; color:#404040; background-color:#fcfcfc;\">The user can select an output directory to save the following outputs for each recording :</span><br />- A desaturation characteristics report, including:<br />   - start time (s)<br />   - duration (s)<br />   - slope (%/s)<br />   - depth (%)<br />   - area (%*s)<br />- The oxygen saturation graph, including saturation signal for the entire recording and invalid sections highlighted.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

