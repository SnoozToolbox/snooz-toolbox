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
    QLineEdit, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_BslVarStep(object):
    def setupUi(self, BslVarStep):
        if not BslVarStep.objectName():
            BslVarStep.setObjectName(u"BslVarStep")
        BslVarStep.resize(1069, 822)
        self.verticalLayout_3 = QVBoxLayout(BslVarStep)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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


        self.verticalLayout_3.addWidget(self.imageWidget)

        self.label_6 = QLabel(BslVarStep)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        self.label_6.setFont(font)

        self.verticalLayout_3.addWidget(self.label_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textEdit_2 = QTextEdit(BslVarStep)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(0, 0))
        self.textEdit_2.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)

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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(110, 0))
        self.label_3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.group_lineEdit = QLineEdit(BslVarStep)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setEnabled(False)
        self.group_lineEdit.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_3.addWidget(self.group_lineEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(BslVarStep)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(110, 0))
        self.label_11.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_4.addWidget(self.label_11)

        self.name_lineEdit = QLineEdit(BslVarStep)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setEnabled(False)
        self.name_lineEdit.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_4.addWidget(self.name_lineEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label = QLabel(BslVarStep)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(BslVarStep)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(200, 16777215))
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
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.textEdit = QTextEdit(BslVarStep)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 250))
        self.textEdit.setFrameShape(QFrame.Shape.StyledPanel)
        self.textEdit.setFrameShadow(QFrame.Shadow.Sunken)
        self.textEdit.setLineWidth(2)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.textEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 405, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.retranslateUi(BslVarStep)

        QMetaObject.connectSlotsByName(BslVarStep)
    # setupUi

    def retranslateUi(self, BslVarStep):
        BslVarStep.setWindowTitle(QCoreApplication.translate("BslVarStep", u"Form", None))
        self.label_7.setText("")
        self.label_6.setText(QCoreApplication.translate("BslVarStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Baseline Variation : Segments with elevated low-frequency power (&lt;0.4 Hz).</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("BslVarStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Identification of baseline variations via spectral power analysis (Welch's method). Low-frequency band power (&lt;0.4 Hz) is computed by integrating the power spectral density estimated using Welch's method, as recommended in [1]. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Power is calculated using 8-s windows with a 4-s step size.</p>\n"
""
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Prior to power estimation, the signal is low-pass filtered at 0.4 Hz using a 10th-order Butterworth IIR filter implemented in second-order sections (SOS) and applied with zero-phase filtering (filtfilt). </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Warning</span>: User-defined filters applied in the &quot;2- Filter EEG Signals&quot; step may affect power estimates in the 0-0.4 Hz frequency band.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; mar"
                        "gin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Reference</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[1] Cox, R. &amp; Fell, J. Analyzing human sleep EEG: A methodological primer with code implementation. Sleep Medicine Reviews, 54, 101353 (2020).       </p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("BslVarStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Event Settings</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("BslVarStep", u"In which \"Event Group\" the detected artifact are added (how they will be written to  the annotation file). Go to the general Detectors Settings to edit the group.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("BslVarStep", u"Event Group", None))
#if QT_CONFIG(tooltip)
        self.group_lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.group_lineEdit.setText(QCoreApplication.translate("BslVarStep", u"art_snooz", None))
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip(QCoreApplication.translate("BslVarStep", u"The event name of the detected artifact (how they will be wrtten to the annotation file).  Go to the general Detectors Settings to edit the name.", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("BslVarStep", u"Event Name", None))
#if QT_CONFIG(tooltip)
        self.name_lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.name_lineEdit.setText(QCoreApplication.translate("BslVarStep", u"art_snooz", None))
        self.label.setText(QCoreApplication.translate("BslVarStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Thresholds</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("BslVarStep", u"The threshold value to identify the artifact. For mean + X SD, the power distribution is estimated from all selected derivations for the recording.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("BslVarStep", u"<html><head/><body><p>Fixed (mean + X SD)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.threshold_lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.threshold_lineEdit.setText(QCoreApplication.translate("BslVarStep", u"4", None))
        self.label_2.setText(QCoreApplication.translate("BslVarStep", u"optimal range: 3.5 - 5;\n"
"computed from all selected derivations", None))
        self.textEdit.setHtml(QCoreApplication.translate("BslVarStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Fixed threshold</span> (mean + X SD)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The power is log10-transformed to reduce skewness and improve normality.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Because the po"
                        "wer distribution is often right-skewed due to artifacts, it is modeled using a three-component Gaussian Mixture Model (GMM). The distribution is estimated from all selected derivations for the recording, so excluding a derivation with poor signal quality can change the threshold applied to the remaining derivations. The threshold is defined as the mean of the main Gaussian component plus a user-defined multiple of its standard deviation (SD).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A segment is flagged when: log10(low-frequency power) &gt; mean + threshold \u00d7 SD</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margi"
                        "n-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To reduce false positives, particularly during large delta waves, increase the threshold value. A value of 5 helps reduce false positives in such recordings.</p></body></html>", None))
    # retranslateUi

