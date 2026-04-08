# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_BslVarStep.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QSplitter,
    QTextEdit, QVBoxLayout, QWidget)
import themes_rc

class Ui_BslVarStep(object):
    def setupUi(self, BslVarStep):
        if not BslVarStep.objectName():
            BslVarStep.setObjectName(u"BslVarStep")
        BslVarStep.resize(704, 776)
        BslVarStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_2 = QVBoxLayout(BslVarStep)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.imageWidget = QWidget(BslVarStep)
        self.imageWidget.setObjectName(u"imageWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageWidget.sizePolicy().hasHeightForWidth())
        self.imageWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.imageWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.imageWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_7)


        self.verticalLayout_2.addWidget(self.imageWidget)

        self.label_6 = QLabel(BslVarStep)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_6.setFont(font)

        self.verticalLayout_2.addWidget(self.label_6)

        self.splitter = QSplitter(BslVarStep)
        self.splitter.setObjectName(u"splitter")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy2)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.textEdit_2 = QTextEdit(self.splitter)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(0, 250))
        self.textEdit_2.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_2.setReadOnly(True)
        self.splitter.addWidget(self.textEdit_2)
        self.textEdit = QTextEdit(self.splitter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 250))
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Shadow.Sunken)
        self.textEdit.setLineWidth(1)
        self.textEdit.setReadOnly(True)
        self.splitter.addWidget(self.textEdit)

        self.verticalLayout_2.addWidget(self.splitter)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(BslVarStep)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(BslVarStep)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.group_lineEdit = QLineEdit(BslVarStep)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setEnabled(False)
        self.group_lineEdit.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_3.addWidget(self.group_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(BslVarStep)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_4.addWidget(self.label_11)

        self.name_lineEdit = QLineEdit(BslVarStep)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setEnabled(False)
        self.name_lineEdit.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_4.addWidget(self.name_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(13, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.label = QLabel(BslVarStep)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(BslVarStep)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(140, 0))
        self.label_5.setMidLineWidth(0)
        self.label_5.setTextFormat(Qt.TextFormat.RichText)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.threshold_lineEdit = QLineEdit(BslVarStep)
        self.threshold_lineEdit.setObjectName(u"threshold_lineEdit")
        self.threshold_lineEdit.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.threshold_lineEdit)

        self.label_2 = QLabel(BslVarStep)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMaximumSize(QSize(200, 16777215))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.textEdit1 = QTextEdit(BslVarStep)
        self.textEdit1.setObjectName(u"textEdit1")
        sizePolicy2.setHeightForWidth(self.textEdit1.sizePolicy().hasHeightForWidth())
        self.textEdit1.setSizePolicy(sizePolicy2)
        self.textEdit1.setMinimumSize(QSize(0, 0))
        self.textEdit1.setMaximumSize(QSize(16777215, 130))
        self.textEdit1.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit1.setFrameShadow(QFrame.Shadow.Sunken)
        self.textEdit1.setLineWidth(1)
        self.textEdit1.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit1.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit1.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(BslVarStep)

        QMetaObject.connectSlotsByName(BslVarStep)
    # setupUi

    def retranslateUi(self, BslVarStep):
        BslVarStep.setWindowTitle(QCoreApplication.translate("BslVarStep", u"Form", None))
        self.label_7.setText("")
        self.label_6.setText(QCoreApplication.translate("BslVarStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Baseline Variation : Segments with high power in the low frequency band (&lt;0.4 Hz).</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("BslVarStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Identification of segments with outlier slow power (0-0.4 Hz) via spectral power (STFT : Short Term Fourier Transform).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">* the lowest frequency band is defined by the band-pass filter in step &quot;2- Filte"
                        "r EEG signals&quot;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Baseline variation can be caused by breathing or sweat corruption.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">EEG signals are low pass filtered 0.4 Hz.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#000000;\">Filter is a 10 th order butterworth IIR filter in Second-Order Sections (SOS) format <br />applied with filtfilt to correct the non-linear phase delay.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">The power is computed on sliding windows thro"
                        "ugh STFT.<br />Window length = 8 s<br />Window step = 4 s</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#000000;\">The STFT is applied to integrate (sum) the signal power within a frequency range<br /> of the true spectrum (units\u00b2 ex. \u00b5V\u00b2) as suggested in [1].</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("BslVarStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline; color:#000000;\">Fixed threshold</span><span style=\" color:#000000;\"> (mean + x STD)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The power is log10 transformed to make the data more normally distributed, <br />however the distribution of the power of all selected ch"
                        "annels is often skewed right du to artifacts.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The distribution is then modeled by a 3-components Gaussian Mixture Model (GMM).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The threshold is multiplied by the standard deviation (STD) and <br />added to the mean of the main gaussian (over a mixture of 3).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">An artifact is possibly identified when the log10(power) &gt; (mean + threshold*STD)</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pubmed.ncbi.nlm.nih.gov/12723066/\"><span style=\" text-decoration: underline; color:#000000;\">Reference</span></a></p>\n"
"<p style=\" margin-t"
                        "op:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">[1] Cox, R. &amp; Fell, J. Analyzing human sleep EEG: A methodological primer with code implementation. <br />Sleep Medicine Reviews54, 101353 (2020).</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("BslVarStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Event Settings</span></p></body></html>", None))
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
        self.label.setText(QCoreApplication.translate("BslVarStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Threshold (mean + x STD)</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("BslVarStep", u"<html><head/><body><p>(A) Threshold value</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.threshold_lineEdit.setToolTip(QCoreApplication.translate("BslVarStep", u"The threshold value to identify the artifact.  Its units is x times the baseline standard deviation.", None))
#endif // QT_CONFIG(tooltip)
        self.threshold_lineEdit.setText(QCoreApplication.translate("BslVarStep", u"4", None))
        self.label_2.setText(QCoreApplication.translate("BslVarStep", u"optimal value from 3.5 to 5", None))
        self.textEdit1.setHtml(QCoreApplication.translate("BslVarStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The threshold value may depends of the high-pass filter applied on the PSG signals.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When the recording has large lo"
                        "w frequency delta waves, please increase the detection threshold to reduce the number of false positives. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Setting the threshold value to 5 helps reduce false positives.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It is also possible to deactivate this detector.</p></body></html>", None))
    # retranslateUi

