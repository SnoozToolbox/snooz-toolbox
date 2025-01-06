# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_HighFreqBurstStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from . import high_freq_noise_res
import themes_rc

class Ui_HighFreqBurstStep(object):
    def setupUi(self, HighFreqBurstStep):
        if not HighFreqBurstStep.objectName():
            HighFreqBurstStep.setObjectName(u"HighFreqBurstStep")
        HighFreqBurstStep.resize(1002, 658)
        HighFreqBurstStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_2 = QVBoxLayout(HighFreqBurstStep)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(HighFreqBurstStep)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1543, 182))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u":/high_freq_noise/burst_noise.png"))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.label_9 = QLabel(HighFreqBurstStep)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)

        self.verticalLayout_2.addWidget(self.label_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(HighFreqBurstStep)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout.addWidget(self.label_6)

        self.verticalSpacer_2 = QSpacerItem(508, 18, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_4 = QLabel(HighFreqBurstStep)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(HighFreqBurstStep)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(140, 0))
        self.label_3.setMaximumSize(QSize(210, 16777215))
        self.label_3.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.group_lineEdit = QLineEdit(HighFreqBurstStep)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setEnabled(False)
        self.group_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.group_lineEdit)

        self.label_7 = QLabel(HighFreqBurstStep)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(140, 0))
        self.label_7.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.name_burst_lineEdit = QLineEdit(HighFreqBurstStep)
        self.name_burst_lineEdit.setObjectName(u"name_burst_lineEdit")
        self.name_burst_lineEdit.setEnabled(False)
        self.name_burst_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name_burst_lineEdit)


        self.horizontalLayout_3.addLayout(self.formLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(380, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(HighFreqBurstStep)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_8 = QLabel(HighFreqBurstStep)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout.addWidget(self.label_8)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(HighFreqBurstStep)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(140, 0))
        self.label_5.setFont(font)
        self.label_5.setMidLineWidth(0)
        self.label_5.setTextFormat(Qt.RichText)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.tresh_fixe_lineEdit = QLineEdit(HighFreqBurstStep)
        self.tresh_fixe_lineEdit.setObjectName(u"tresh_fixe_lineEdit")
        self.tresh_fixe_lineEdit.setMinimumSize(QSize(0, 0))
        self.tresh_fixe_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.tresh_fixe_lineEdit, 0, 1, 1, 1)

        self.label_12 = QLabel(HighFreqBurstStep)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 0, 2, 1, 1)

        self.label_2 = QLabel(HighFreqBurstStep)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(210, 0))
        self.label_2.setMaximumSize(QSize(210, 16777215))
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.RichText)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.thresh_adp_lineEdit = QLineEdit(HighFreqBurstStep)
        self.thresh_adp_lineEdit.setObjectName(u"thresh_adp_lineEdit")
        self.thresh_adp_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.thresh_adp_lineEdit, 1, 1, 1, 1)

        self.label_13 = QLabel(HighFreqBurstStep)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 1, 2, 1, 1)

        self.label_11 = QLabel(HighFreqBurstStep)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)

        self.thresh_ratio_lineEdit = QLineEdit(HighFreqBurstStep)
        self.thresh_ratio_lineEdit.setObjectName(u"thresh_ratio_lineEdit")
        self.thresh_ratio_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.thresh_ratio_lineEdit, 2, 1, 1, 1)

        self.label_14 = QLabel(HighFreqBurstStep)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_3 = QSpacerItem(548, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.textEdit = QTextEdit(HighFreqBurstStep)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFont(font)
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setFrameShape(QFrame.HLine)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.textEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.textEdit_2 = QTextEdit(HighFreqBurstStep)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit_2.setFont(font)
        self.textEdit_2.setAutoFillBackground(True)
        self.textEdit_2.setFrameShape(QFrame.HLine)
        self.textEdit_2.setFrameShadow(QFrame.Plain)
        self.textEdit_2.setLineWidth(0)
        self.textEdit_2.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.textEdit_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.retranslateUi(HighFreqBurstStep)

        QMetaObject.connectSlotsByName(HighFreqBurstStep)
    # setupUi

    def retranslateUi(self, HighFreqBurstStep):
        HighFreqBurstStep.setWindowTitle(QCoreApplication.translate("HighFreqBurstStep", u"Form", None))
        self.label_10.setText("")
        self.label_9.setText(QCoreApplication.translate("HighFreqBurstStep", u"<html><head/><body><p><span style=\" font-weight:600;\">High Frequency burst : Segments with a burst of high frequency power (&gt;25 Hz).</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("HighFreqBurstStep", u"Identification of bursts of high frequency (>25 Hz) noise\n"
"via spectral power (STFT :  Short Term Fourier Transform).\n"
"A glitch or a noise burst may be caused by a bad connection of the electrode.", None))
        self.label_4.setText(QCoreApplication.translate("HighFreqBurstStep", u"Event Settings", None))
        self.label_3.setText(QCoreApplication.translate("HighFreqBurstStep", u"Event Group", None))
#if QT_CONFIG(tooltip)
        self.group_lineEdit.setToolTip(QCoreApplication.translate("HighFreqBurstStep", u"In which \"Event Group\" the detected artifact are added (how they will be written to  the annotation file). Go to the general Detectors Settings to edit the group.", None))
#endif // QT_CONFIG(tooltip)
        self.group_lineEdit.setText(QCoreApplication.translate("HighFreqBurstStep", u"art_snooz", None))
        self.label_7.setText(QCoreApplication.translate("HighFreqBurstStep", u"Event Name", None))
#if QT_CONFIG(tooltip)
        self.name_burst_lineEdit.setToolTip(QCoreApplication.translate("HighFreqBurstStep", u"The event name of the detected artifact (how they will be wrtten to the annotation file).  Go to the general Detectors Settings to edit the name.", None))
#endif // QT_CONFIG(tooltip)
        self.name_burst_lineEdit.setText(QCoreApplication.translate("HighFreqBurstStep", u"art_snooz", None))
        self.label.setText(QCoreApplication.translate("HighFreqBurstStep", u"Thresholds", None))
        self.label_8.setText(QCoreApplication.translate("HighFreqBurstStep", u"Artifact when A and B and C", None))
        self.label_5.setText(QCoreApplication.translate("HighFreqBurstStep", u"<html><head/><body><p>(A) Fixed (mean + x STD) of main gaussian</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.tresh_fixe_lineEdit.setToolTip(QCoreApplication.translate("HighFreqBurstStep", u"The threshold value to identify the artifact.  Its units is x times the baseline standard deviation.", None))
#endif // QT_CONFIG(tooltip)
        self.tresh_fixe_lineEdit.setText(QCoreApplication.translate("HighFreqBurstStep", u"4", None))
        self.label_12.setText(QCoreApplication.translate("HighFreqBurstStep", u"optimal value from 3 to 5", None))
        self.label_2.setText(QCoreApplication.translate("HighFreqBurstStep", u"<html><head/><body><p>(B) Adaptive (x BSL MEDIAN)</p></body></html>", None))
        self.thresh_adp_lineEdit.setText(QCoreApplication.translate("HighFreqBurstStep", u"8", None))
        self.label_13.setText(QCoreApplication.translate("HighFreqBurstStep", u"optimal value from 6 to 10", None))
        self.label_11.setText(QCoreApplication.translate("HighFreqBurstStep", u"(C) Power ratio (25-64 Hz/8-64Hz)", None))
        self.thresh_ratio_lineEdit.setText(QCoreApplication.translate("HighFreqBurstStep", u"0.1", None))
        self.label_14.setText(QCoreApplication.translate("HighFreqBurstStep", u"optimal value from 0.05 to 0.4", None))
        self.textEdit.setHtml(QCoreApplication.translate("HighFreqBurstStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Fixed threshold</span><span style=\" color:#000000;\"> (mean + x STD)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The power is log10 transformed to make the data more normally distributed, however the distribution of the power of all selected channels is often skewed right du to artifacts.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The distribut"
                        "ion is then modeled by a 3-components Gaussian Mixture Model (GMM).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The threshold is multiplied by the standard deviation (STD) and added to the mean of the main gaussian (over a mixture of 3).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">An artifact is possibly identified when the log10(power) &gt; (mean + threshold*STD)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Adaptive threshold</span> (baseline)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-i"
                        "ndent:0px;\">An adaptive threshold is computed from a baseline window (BSL) of 30 s around the segment to evaluate.  A segment with a power x times the median power of the baseline is possibly an artifact. The adaptive threshold may be too sensitive when the EEG recording does not include much high frequency noise. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Power ratio threshold</span> (relative power)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">High frequency bursts can be masked (thus non-disturbing) by a strong low frequency signal. An artifact is possibly identified when the relative power (25-64 Hz)/(8-64 Hz) &gt; threshold.</p>\n"
"<"
                        "p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A segment whose power exceeds the 3 thresholds is considered an artifact.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To reduce the number of false positives, especially during spindles, alpha waves, or beta bursts, please first increase the power ratio threshold value.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A greater proportion of the signal in the 25-64 Hz frequency band will be needed to mark the segme"
                        "nt as an artifact.</p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("HighFreqBurstStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The power is computed on sliding windows through STFT.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Window length = 0.5 s</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Window step = 0.25 s </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The STFT is applied to integrate (sum) the signal power within a frequency range of "
                        "the true spectrum (units\u00b2 ex. \u00b5V\u00b2) as suggested in [1].</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The adaptive treshold is computed from a baseline window (BSL).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Window length around the segment = 30 s</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Reference</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[1] Cox, R. &amp; Fell, J. Analyzing human sleep EEG: A methodological primer with code implementation. Sleep M"
                        "edicine Reviews54, 101353 (2020).</p></body></html>", None))
    # retranslateUi

