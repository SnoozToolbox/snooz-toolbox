# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_HighFreqBurstStep.ui'
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
    QLabel, QLayout, QLineEdit, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
import themes_rc

class Ui_HighFreqBurstStep(object):
    def setupUi(self, HighFreqBurstStep):
        if not HighFreqBurstStep.objectName():
            HighFreqBurstStep.setObjectName(u"HighFreqBurstStep")
        HighFreqBurstStep.resize(1479, 646)
        self.verticalLayout_2 = QVBoxLayout(HighFreqBurstStep)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(HighFreqBurstStep)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_10)


        self.verticalLayout_2.addWidget(self.widget)

        self.label_9 = QLabel(HighFreqBurstStep)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        self.label_9.setFont(font)

        self.verticalLayout_2.addWidget(self.label_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit_2 = QTextEdit(HighFreqBurstStep)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_2.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_2.setLineWidth(0)
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit_2)

        self.verticalSpacer_2 = QSpacerItem(508, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_4 = QLabel(HighFreqBurstStep)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.label_3 = QLabel(HighFreqBurstStep)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(110, 0))
        self.label_3.setMaximumSize(QSize(80, 16777215))
        self.label_3.setFont(font)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_7 = QLabel(HighFreqBurstStep)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMinimumSize(QSize(110, 0))
        self.label_7.setMaximumSize(QSize(80, 16777215))
        self.label_7.setFont(font)

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.name_burst_lineEdit = QLineEdit(HighFreqBurstStep)
        self.name_burst_lineEdit.setObjectName(u"name_burst_lineEdit")
        self.name_burst_lineEdit.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.name_burst_lineEdit.sizePolicy().hasHeightForWidth())
        self.name_burst_lineEdit.setSizePolicy(sizePolicy3)
        self.name_burst_lineEdit.setMinimumSize(QSize(500, 0))
        self.name_burst_lineEdit.setMaximumSize(QSize(500, 16777215))

        self.gridLayout_3.addWidget(self.name_burst_lineEdit, 1, 1, 1, 1)

        self.group_lineEdit = QLineEdit(HighFreqBurstStep)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.group_lineEdit.sizePolicy().hasHeightForWidth())
        self.group_lineEdit.setSizePolicy(sizePolicy3)
        self.group_lineEdit.setMinimumSize(QSize(500, 0))
        self.group_lineEdit.setMaximumSize(QSize(500, 16777215))

        self.gridLayout_3.addWidget(self.group_lineEdit, 0, 1, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(380, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(HighFreqBurstStep)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_8 = QLabel(HighFreqBurstStep)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setFont(font)

        self.verticalLayout.addWidget(self.label_8)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.tresh_fixe_lineEdit = QLineEdit(HighFreqBurstStep)
        self.tresh_fixe_lineEdit.setObjectName(u"tresh_fixe_lineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tresh_fixe_lineEdit.sizePolicy().hasHeightForWidth())
        self.tresh_fixe_lineEdit.setSizePolicy(sizePolicy4)
        self.tresh_fixe_lineEdit.setMinimumSize(QSize(0, 0))
        self.tresh_fixe_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.tresh_fixe_lineEdit, 0, 1, 1, 1)

        self.label_13 = QLabel(HighFreqBurstStep)
        self.label_13.setObjectName(u"label_13")
        sizePolicy4.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy4)
        self.label_13.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_13, 1, 2, 1, 1)

        self.label_15 = QLabel(HighFreqBurstStep)
        self.label_15.setObjectName(u"label_15")
        sizePolicy4.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy4)
        self.label_15.setMaximumSize(QSize(315, 16777215))
        self.label_15.setMouseTracking(True)

        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_11 = QLabel(HighFreqBurstStep)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)
        self.label_11.setMaximumSize(QSize(315, 16777215))
        self.label_11.setFont(font)

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)

        self.label_12 = QLabel(HighFreqBurstStep)
        self.label_12.setObjectName(u"label_12")
        sizePolicy4.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy4)
        self.label_12.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_12, 0, 2, 1, 1)

        self.thresh_adp_lineEdit = QLineEdit(HighFreqBurstStep)
        self.thresh_adp_lineEdit.setObjectName(u"thresh_adp_lineEdit")
        sizePolicy4.setHeightForWidth(self.thresh_adp_lineEdit.sizePolicy().hasHeightForWidth())
        self.thresh_adp_lineEdit.setSizePolicy(sizePolicy4)
        self.thresh_adp_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.thresh_adp_lineEdit, 1, 1, 1, 1)

        self.thresh_ratio_lineEdit = QLineEdit(HighFreqBurstStep)
        self.thresh_ratio_lineEdit.setObjectName(u"thresh_ratio_lineEdit")
        sizePolicy4.setHeightForWidth(self.thresh_ratio_lineEdit.sizePolicy().hasHeightForWidth())
        self.thresh_ratio_lineEdit.setSizePolicy(sizePolicy4)
        self.thresh_ratio_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.thresh_ratio_lineEdit, 2, 1, 1, 1)

        self.label_2 = QLabel(HighFreqBurstStep)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setMinimumSize(QSize(210, 0))
        self.label_2.setMaximumSize(QSize(315, 16777215))
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.TextFormat.RichText)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_14 = QLabel(HighFreqBurstStep)
        self.label_14.setObjectName(u"label_14")
        sizePolicy4.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy4)
        self.label_14.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_14, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.textEdit = QTextEdit(HighFreqBurstStep)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFont(font)
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setFrameShape(QFrame.Shape.StyledPanel)
        self.textEdit.setFrameShadow(QFrame.Shadow.Sunken)
        self.textEdit.setLineWidth(2)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.textEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.retranslateUi(HighFreqBurstStep)

        QMetaObject.connectSlotsByName(HighFreqBurstStep)
    # setupUi

    def retranslateUi(self, HighFreqBurstStep):
        HighFreqBurstStep.setWindowTitle(QCoreApplication.translate("HighFreqBurstStep", u"Form", None))
        self.label_10.setText("")
        self.label_9.setText(QCoreApplication.translate("HighFreqBurstStep", u"<html><head/><body><p><span style=\" font-weight:600;\">High Frequency burst : Segments with a burst of high frequency power (&gt;25 Hz).</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("HighFreqBurstStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Identification of high-frequency bursts via spectral power analysis (Welch\u2019s method).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">High-frequency band power (&gt;25 Hz) is computed by integrating the power spectral density</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-"
                        "indent:0px;\">estimated using Welch\u2019s method, as recommended in [1].</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Power is calculated using 0.5-s windows with a 0.25-s step size.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Reference:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[1] Cox, R. &amp; Fell, J. Analyzing human sleep EEG: A methodological primer with code implementation.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sleep Medicine Reviews54, 101353 (2020).</"
                        "p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("HighFreqBurstStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Event Settings</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("HighFreqBurstStep", u"In which \"Event Group\" the detected artifact are added (how they will be written to  the annotation file). Go to the general Detectors Settings to edit the group.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("HighFreqBurstStep", u"<html><head/><body><p>Event Group</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("HighFreqBurstStep", u"The event name of the detected artifact (how they will be wrtten to the annotation file).  Go to the general Detectors Settings to edit the name.", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("HighFreqBurstStep", u"Event Name", None))
#if QT_CONFIG(tooltip)
        self.name_burst_lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.name_burst_lineEdit.setText(QCoreApplication.translate("HighFreqBurstStep", u"art_snooz", None))
#if QT_CONFIG(tooltip)
        self.group_lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.group_lineEdit.setText(QCoreApplication.translate("HighFreqBurstStep", u"art_snooz", None))
        self.label.setText(QCoreApplication.translate("HighFreqBurstStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Thresholds</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("HighFreqBurstStep", u"An artifact is identified when the spectral power exceeds three complementary thresholds:", None))
#if QT_CONFIG(tooltip)
        self.tresh_fixe_lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.tresh_fixe_lineEdit.setText(QCoreApplication.translate("HighFreqBurstStep", u"4", None))
        self.label_13.setText(QCoreApplication.translate("HighFreqBurstStep", u"optimal value from 6 to 10", None))
#if QT_CONFIG(tooltip)
        self.label_15.setToolTip(QCoreApplication.translate("HighFreqBurstStep", u"The threshold value to identify the artifact.  Its units is x times the baseline standard deviation.", None))
#endif // QT_CONFIG(tooltip)
        self.label_15.setText(QCoreApplication.translate("HighFreqBurstStep", u"(A) Fixed (mean + x SD) of main gaussian     ", None))
        self.label_11.setText(QCoreApplication.translate("HighFreqBurstStep", u"(C) Power ratio (25-64 Hz/8-64Hz)", None))
        self.label_12.setText(QCoreApplication.translate("HighFreqBurstStep", u"optimal value from 3 to 5; \n"
"computed from all selected derivations", None))
        self.thresh_adp_lineEdit.setText(QCoreApplication.translate("HighFreqBurstStep", u"8", None))
        self.thresh_ratio_lineEdit.setText(QCoreApplication.translate("HighFreqBurstStep", u"0.1", None))
        self.label_2.setText(QCoreApplication.translate("HighFreqBurstStep", u"<html><head/><body><p>(B) Adaptive (x BSL MEDIAN) </p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("HighFreqBurstStep", u"optimal value from 0.05 to 0.4", None))
        self.textEdit.setHtml(QCoreApplication.translate("HighFreqBurstStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">A) Fixed threshold</span><span style=\" color:#000000;\"> (mean + x SD)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The power is log10-transformed to reduce skewness and improve normality. Because the power distribution is often right-skewed due to artifacts, it is modeled using a three-co"
                        "mponent Gaussian Mixture Model (GMM). The distribution is estimated from all selected derivations for the recording, so excluding a derivation with poor signal quality can change the threshold applied to the remaining derivations. The threshold is defined as the mean of the main Gaussian component plus a user-defined multiple of its standard deviation (SD).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A segment is flagged when: log10(25-64 Hz power) &gt; mean + threshold \u00d7 SD</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">B) Adaptive threshold</span> (baseline)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\">An adaptive threshold is computed from a 30-s baseline window surrounding the segment under evaluation. A segment is flagged when its power exceeds a user-defined multiple of the baseline median power. This threshold may be overly sensitive when the EEG recording is relatively free of high-frequency noise.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A segment is flagged when: 25-64 Hz power &gt; threshold x BSL MEDIAN</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">C) Power ratio threshold</span> (relative power)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px;\">High-frequency bursts can be masked by strong low-frequency activity and may therefore be non-disturbing. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A segment is flagged when: (25-64 Hz power) / (8-64 Hz power) &gt; threshold</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A segment is classified as an artifact only when all three thresholds are exceeded.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To r"
                        "educe false positives, particularly during spindles, alpha activity, or beta bursts, first increase the power ratio threshold. This requires a greater proportion of signal power in the 25-64 Hz frequency band before a segment is classified as an artifact.</p></body></html>", None))
    # retranslateUi

