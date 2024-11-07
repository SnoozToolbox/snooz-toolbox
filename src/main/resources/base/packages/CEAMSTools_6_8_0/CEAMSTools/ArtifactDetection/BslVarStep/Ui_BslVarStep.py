# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_BslVarStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from . import BSLVar_res
import themes_rc

class Ui_BslVarStep(object):
    def setupUi(self, BslVarStep):
        if not BslVarStep.objectName():
            BslVarStep.setObjectName(u"BslVarStep")
        BslVarStep.resize(1021, 849)
        BslVarStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_2 = QVBoxLayout(BslVarStep)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(BslVarStep)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1545, 161))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u":/BSLVar/BSLVar.png"))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_7)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(BslVarStep)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)

        self.verticalLayout_4.addWidget(self.label_6)

        self.textEdit = QTextEdit(BslVarStep)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 400))
        self.textEdit.setFrameShape(QFrame.HLine)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.textEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(BslVarStep)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(BslVarStep)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(140, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.group_lineEdit = QLineEdit(BslVarStep)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setEnabled(False)
        self.group_lineEdit.setMaximumSize(QSize(300, 16777215))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.group_lineEdit)

        self.label_11 = QLabel(BslVarStep)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.name_lineEdit = QLineEdit(BslVarStep)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setEnabled(False)
        self.name_lineEdit.setMaximumSize(QSize(300, 16777215))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name_lineEdit)


        self.verticalLayout.addLayout(self.formLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(13, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.label = QLabel(BslVarStep)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(BslVarStep)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(140, 0))
        self.label_5.setMidLineWidth(0)
        self.label_5.setTextFormat(Qt.RichText)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.threshold_lineEdit = QLineEdit(BslVarStep)
        self.threshold_lineEdit.setObjectName(u"threshold_lineEdit")
        self.threshold_lineEdit.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.threshold_lineEdit)

        self.label_2 = QLabel(BslVarStep)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(200, 16777215))
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.plainTextEdit = QPlainTextEdit(BslVarStep)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(500, 0))
        self.plainTextEdit.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit.setFrameShape(QFrame.HLine)
        self.plainTextEdit.setFrameShadow(QFrame.Plain)
        self.plainTextEdit.setLineWidth(0)
        self.plainTextEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.plainTextEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.retranslateUi(BslVarStep)

        QMetaObject.connectSlotsByName(BslVarStep)
    # setupUi

    def retranslateUi(self, BslVarStep):
        BslVarStep.setWindowTitle(QCoreApplication.translate("BslVarStep", u"Form", None))
        self.label_7.setText("")
        self.label_6.setText(QCoreApplication.translate("BslVarStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Baseline Variation : Segments with high power in the low frequency band (&lt;0.4 Hz).</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("BslVarStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Identification of segments with outlier slow power (0-0.4 Hz) via spectral power (STFT : Short Term Fourier Transform).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">* the lowest frequency band is defined by the band-pass filter in step &quot;2- Filter EEG signals&quot;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        "><span style=\" color:#000000;\">Baseline variation can be caused by breathing or sweat corruption.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">EEG signals are low pass filtered 0.4 Hz.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#000000;\">Filter is a 10 th order butterworth IIR filter in Second-Order Sections (SOS) format applied with filtfilt to correct the non-linear phase delay.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">The power is computed on sliding windows through STFT.<br />Window length = 8 s<br />Window step = 4 s</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-bl"
                        "ock-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#000000;\">The STFT is applied to integrate (sum) the signal power within a frequency range of the true spectrum (units\u00b2 ex. \u00b5V\u00b2) as suggested in [1].</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline; color:#000000;\">Fixed threshold</span><span style=\" color:#000000;\"> (mean + x STD)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The power is log10 transformed to make the data more normally distributed, however the distribution of the power of all selected channels is often skewed right du to artifacts.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The distribution is then modeled by a 3-components Gaussian Mixture Model (G"
                        "MM).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The threshold is multiplied by the standard deviation (STD) and added to the mean of the main gaussian (over a mixture of 3).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">An artifact is possibly identified when the log10(power) &gt; (mean + threshold*STD)</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pubmed.ncbi.nlm.nih.gov/12723066/\"><span style=\" text-decoration: underline; color:#000000;\">Reference</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">[1] Cox, R. &amp; Fell, J. Analyzing human sleep EEG: A methodological primer with code implementation. Sleep Medicine Rev"
                        "iews54, 101353 (2020).</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("BslVarStep", u"Event Settings", None))
        self.label_3.setText(QCoreApplication.translate("BslVarStep", u"Event Group", None))
#if QT_CONFIG(tooltip)
        self.group_lineEdit.setToolTip(QCoreApplication.translate("BslVarStep", u"In which \"Event Group\" the detected artifact are added (how they will be written to  the annotation file). Go to the general Detectors Settings to edit the group.", None))
#endif // QT_CONFIG(tooltip)
        self.group_lineEdit.setText(QCoreApplication.translate("BslVarStep", u"art_snooz", None))
        self.label_11.setText(QCoreApplication.translate("BslVarStep", u"Event Name", None))
#if QT_CONFIG(tooltip)
        self.name_lineEdit.setToolTip(QCoreApplication.translate("BslVarStep", u"The event name of the detected artifact (how they will be wrtten to the annotation file).  Go to the general Detectors Settings to edit the name.", None))
#endif // QT_CONFIG(tooltip)
        self.name_lineEdit.setText(QCoreApplication.translate("BslVarStep", u"art_snooz", None))
        self.label.setText(QCoreApplication.translate("BslVarStep", u"<html><head/><body><p>Threshold (mean + x STD)</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("BslVarStep", u"<html><head/><body><p>Threshold value</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.threshold_lineEdit.setToolTip(QCoreApplication.translate("BslVarStep", u"The threshold value to identify the artifact.  Its units is x times the baseline standard deviation.", None))
#endif // QT_CONFIG(tooltip)
        self.threshold_lineEdit.setText(QCoreApplication.translate("BslVarStep", u"4", None))
        self.label_2.setText(QCoreApplication.translate("BslVarStep", u"optimal value from 3.5 to 5", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("BslVarStep", u"The threshold value may depends of the high-pass filter applied on the PSG signals.\n"
"\n"
"When the recording has large low frequency delta waves, please increase the detection threshold to reduce the number of false positives. \n"
"Setting the threshold value to 5 helps reduce false positives.\n"
"It is also possible to deactivate this detector.", None))
    # retranslateUi

