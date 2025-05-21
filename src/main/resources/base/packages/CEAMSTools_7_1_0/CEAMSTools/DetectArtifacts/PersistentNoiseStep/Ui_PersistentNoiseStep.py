# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file ''
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QScrollArea, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
from . import high_freq_noise_res_rc
import themes_rc

class Ui_PersistentNoiseStep(object):
    def setupUi(self, PersistentNoiseStep):
        if not PersistentNoiseStep.objectName():
            PersistentNoiseStep.setObjectName(u"PersistentNoiseStep")
        PersistentNoiseStep.resize(905, 781)
        PersistentNoiseStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_2 = QVBoxLayout(PersistentNoiseStep)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(PersistentNoiseStep)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1543, 181))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u":/high_freq_noise/persistent_noise.png"))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_9 = QLabel(PersistentNoiseStep)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 20))
        self.label_9.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QFrame.NoFrame)
        self.label_9.setLineWidth(0)

        self.verticalLayout_3.addWidget(self.label_9)

        self.description_textEdit = QTextEdit(PersistentNoiseStep)
        self.description_textEdit.setObjectName(u"description_textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(5)
        sizePolicy1.setHeightForWidth(self.description_textEdit.sizePolicy().hasHeightForWidth())
        self.description_textEdit.setSizePolicy(sizePolicy1)
        self.description_textEdit.setMinimumSize(QSize(0, 250))
        self.description_textEdit.setStyleSheet(u"")
        self.description_textEdit.setFrameShape(QFrame.NoFrame)
        self.description_textEdit.setFrameShadow(QFrame.Plain)
        self.description_textEdit.setLineWidth(0)
        self.description_textEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.description_textEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(PersistentNoiseStep)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(PersistentNoiseStep)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(140, 0))
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.group_lineEdit = QLineEdit(PersistentNoiseStep)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setEnabled(False)
        self.group_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.group_lineEdit.setFont(font)

        self.gridLayout.addWidget(self.group_lineEdit, 0, 1, 1, 1)

        self.label_11 = QLabel(PersistentNoiseStep)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(140, 0))
        self.label_11.setFont(font)

        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)

        self.name_fixe_lineEdit = QLineEdit(PersistentNoiseStep)
        self.name_fixe_lineEdit.setObjectName(u"name_fixe_lineEdit")
        self.name_fixe_lineEdit.setEnabled(False)
        self.name_fixe_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.name_fixe_lineEdit.setFont(font)

        self.gridLayout.addWidget(self.name_fixe_lineEdit, 1, 1, 1, 1)

        self.label_5 = QLabel(PersistentNoiseStep)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(140, 0))
        self.label_5.setFont(font)
        self.label_5.setMidLineWidth(0)
        self.label_5.setTextFormat(Qt.RichText)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.tresh_fixe_lineEdit = QLineEdit(PersistentNoiseStep)
        self.tresh_fixe_lineEdit.setObjectName(u"tresh_fixe_lineEdit")
        self.tresh_fixe_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.tresh_fixe_lineEdit.setFont(font)

        self.gridLayout.addWidget(self.tresh_fixe_lineEdit, 2, 1, 1, 1)

        self.label_2 = QLabel(PersistentNoiseStep)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)

        self.label = QLabel(PersistentNoiseStep)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.thres_ratio_lineEdit = QLineEdit(PersistentNoiseStep)
        self.thres_ratio_lineEdit.setObjectName(u"thres_ratio_lineEdit")
        self.thres_ratio_lineEdit.setMinimumSize(QSize(0, 0))
        self.thres_ratio_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.thres_ratio_lineEdit.setFont(font)

        self.gridLayout.addWidget(self.thres_ratio_lineEdit, 3, 1, 1, 1)

        self.label_6 = QLabel(PersistentNoiseStep)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.settings_textEdit = QTextEdit(PersistentNoiseStep)
        self.settings_textEdit.setObjectName(u"settings_textEdit")
        self.settings_textEdit.setMaximumSize(QSize(16777215, 16777215))
        self.settings_textEdit.setFocusPolicy(Qt.NoFocus)
        self.settings_textEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.settings_textEdit.setAcceptDrops(False)
        self.settings_textEdit.setStyleSheet(u"")
        self.settings_textEdit.setFrameShape(QFrame.HLine)
        self.settings_textEdit.setFrameShadow(QFrame.Plain)
        self.settings_textEdit.setLineWidth(0)
        self.settings_textEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.settings_textEdit, 0, 1, 2, 1)

        self.textEdit = QTextEdit(PersistentNoiseStep)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit.setFrameShape(QFrame.HLine)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.retranslateUi(PersistentNoiseStep)

        QMetaObject.connectSlotsByName(PersistentNoiseStep)
    # setupUi

    def retranslateUi(self, PersistentNoiseStep):
        PersistentNoiseStep.setWindowTitle(QCoreApplication.translate("PersistentNoiseStep", u"Form", None))
        self.label_10.setText("")
        self.label_9.setText(QCoreApplication.translate("PersistentNoiseStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Persistent Noise : Segments with high frequency noise (&gt;25 Hz).</span></p></body></html>", None))
        self.description_textEdit.setHtml(QCoreApplication.translate("PersistentNoiseStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Identification of segments with outlier power (&gt;25 Hz) via spectral power (STFT : Short Term Fourier Transform).</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">An increase of high frequency power may be caused by a bad connection of the electrode.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decora"
                        "tion: underline;\">Fixed threshold</span><span style=\" color:#000000;\"> (mean + x STD)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The power is log10 transformed to make the data more normally distributed, however the distribution of the power of all selected channels is often skewed right du to artifacts.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The distribution is then modeled by a 3-components Gaussian Mixture Model (GMM).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The threshold is multiplied by the standard deviation (STD) and added to the mean of the main gaussian (over a mixture of 3).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">An artifact is possibly ident"
                        "ified when the log10(power) &gt; (mean + threshold*STD)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Power ratio threshold</span> (relative power)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">High frequency noise can be masked (thus non-disturbing) by a strong low frequency signal. An artifact is possibly identified when the relative power (25-64 Hz)/(1-64 Hz) &gt; threshold.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; t"
                        "ext-indent:0px;\">A segment whose power exceeds the 2 thresholds is considered an artifact.</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("PersistentNoiseStep", u"Event Settings", None))
        self.label_3.setText(QCoreApplication.translate("PersistentNoiseStep", u"Event Group", None))
#if QT_CONFIG(tooltip)
        self.group_lineEdit.setToolTip(QCoreApplication.translate("PersistentNoiseStep", u"In which \"Event Group\" the detected artifact are added (label in the annotation file). Go to the general Detectors Settings to edit the group.", None))
#endif // QT_CONFIG(tooltip)
        self.group_lineEdit.setText(QCoreApplication.translate("PersistentNoiseStep", u"art_snooz", None))
        self.label_11.setText(QCoreApplication.translate("PersistentNoiseStep", u"Event Name", None))
#if QT_CONFIG(tooltip)
        self.name_fixe_lineEdit.setToolTip(QCoreApplication.translate("PersistentNoiseStep", u"The event name of the detected artifact (label in the annotation file). Go to the general Detectors Settings to edit the name.", None))
#endif // QT_CONFIG(tooltip)
        self.name_fixe_lineEdit.setText(QCoreApplication.translate("PersistentNoiseStep", u"art_snooz", None))
        self.label_5.setText(QCoreApplication.translate("PersistentNoiseStep", u"<html><head/><body><p>Fixed threshold (mean + x STD)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.tresh_fixe_lineEdit.setToolTip(QCoreApplication.translate("PersistentNoiseStep", u"The threshold value to identify the artefact.  Its units is x times the baseline standard deviation.", None))
#endif // QT_CONFIG(tooltip)
        self.tresh_fixe_lineEdit.setText(QCoreApplication.translate("PersistentNoiseStep", u"4", None))
        self.label_2.setText(QCoreApplication.translate("PersistentNoiseStep", u"optimal value from 3 to 5", None))
        self.label.setText(QCoreApplication.translate("PersistentNoiseStep", u"Power ratio (25-64 Hz/1-64 Hz)", None))
        self.thres_ratio_lineEdit.setText(QCoreApplication.translate("PersistentNoiseStep", u"0.25", None))
        self.label_6.setText(QCoreApplication.translate("PersistentNoiseStep", u"optimal value from 0.1 to 0.4", None))
        self.settings_textEdit.setHtml(QCoreApplication.translate("PersistentNoiseStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">The power is computed on sliding windows through STFT.<br />Window length = 6 s<br />Window step = 3 s </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#000000;\">The STFT is applied to integrate (sum) the signal power within a frequency range of the true spectrum (units\u00b2 ex. \u00b5V\u00b2) as suggested in [1].</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-"
                        "right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pubmed.ncbi.nlm.nih.gov/12723066/\"><span style=\" text-decoration: underline; color:#000000;\">Reference</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">[1] Cox, R. &amp; Fell, J. Analyzing human sleep EEG: A methodological primer with code implementation. Sleep Medicine Reviews54, 101353 (2020).</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("PersistentNoiseStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To reduce the number of false positives, especially during low amplitude R stage, please first increase the power ratio threshold value.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A greater proportion of the signal in the 25-64 Hz frequency band will be needed to mark the segment as an artifact.</p></body></html>", None))
    # retranslateUi

