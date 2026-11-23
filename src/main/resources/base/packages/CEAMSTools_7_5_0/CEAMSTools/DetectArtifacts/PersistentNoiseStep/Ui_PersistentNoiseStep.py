# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_PersistentNoiseStep.ui'
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
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)
import themes_rc

class Ui_PersistentNoiseStep(object):
    def setupUi(self, PersistentNoiseStep):
        if not PersistentNoiseStep.objectName():
            PersistentNoiseStep.setObjectName(u"PersistentNoiseStep")
        PersistentNoiseStep.resize(1109, 683)
        self.verticalLayout_2 = QVBoxLayout(PersistentNoiseStep)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.imageWidget = QWidget(PersistentNoiseStep)
        self.imageWidget.setObjectName(u"imageWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageWidget.sizePolicy().hasHeightForWidth())
        self.imageWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.imageWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_10 = QLabel(self.imageWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_10)


        self.verticalLayout_2.addWidget(self.imageWidget)

        self.label_9 = QLabel(PersistentNoiseStep)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 20))
        self.label_9.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QFrame.Shape.NoFrame)
        self.label_9.setLineWidth(0)

        self.verticalLayout_2.addWidget(self.label_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.description_textEdit = QTextEdit(PersistentNoiseStep)
        self.description_textEdit.setObjectName(u"description_textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.description_textEdit.sizePolicy().hasHeightForWidth())
        self.description_textEdit.setSizePolicy(sizePolicy1)
        self.description_textEdit.setMinimumSize(QSize(0, 0))
        self.description_textEdit.setMaximumSize(QSize(16777215, 700))
        self.description_textEdit.setStyleSheet(u"")
        self.description_textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.description_textEdit.setFrameShadow(QFrame.Shadow.Plain)
        self.description_textEdit.setLineWidth(0)
        self.description_textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.description_textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.description_textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.description_textEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_4 = QLabel(PersistentNoiseStep)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(PersistentNoiseStep)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setMinimumSize(QSize(110, 0))
        self.label_5.setMaximumSize(QSize(110, 16777215))

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.group_lineEdit = QLineEdit(PersistentNoiseStep)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setEnabled(False)
        self.group_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.group_lineEdit.setFont(font)

        self.gridLayout.addWidget(self.group_lineEdit, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.label_3 = QLabel(PersistentNoiseStep)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(110, 16777215))

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.name_fixe_lineEdit = QLineEdit(PersistentNoiseStep)
        self.name_fixe_lineEdit.setObjectName(u"name_fixe_lineEdit")
        self.name_fixe_lineEdit.setEnabled(False)
        self.name_fixe_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.name_fixe_lineEdit.setFont(font)

        self.gridLayout.addWidget(self.name_fixe_lineEdit, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.label_8 = QLabel(PersistentNoiseStep)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout.addWidget(self.label_8)

        self.label_11 = QLabel(PersistentNoiseStep)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout.addWidget(self.label_11)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(PersistentNoiseStep)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(270, 16777215))

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.tresh_fixe_lineEdit = QLineEdit(PersistentNoiseStep)
        self.tresh_fixe_lineEdit.setObjectName(u"tresh_fixe_lineEdit")
        self.tresh_fixe_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.tresh_fixe_lineEdit.setFont(font)

        self.gridLayout_2.addWidget(self.tresh_fixe_lineEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(PersistentNoiseStep)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)

        self.label = QLabel(PersistentNoiseStep)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(270, 16777215))
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.thres_ratio_lineEdit = QLineEdit(PersistentNoiseStep)
        self.thres_ratio_lineEdit.setObjectName(u"thres_ratio_lineEdit")
        self.thres_ratio_lineEdit.setMinimumSize(QSize(0, 0))
        self.thres_ratio_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.thres_ratio_lineEdit.setFont(font)

        self.gridLayout_2.addWidget(self.thres_ratio_lineEdit, 1, 1, 1, 1)

        self.label_6 = QLabel(PersistentNoiseStep)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.label_6, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.settings_textEdit = QTextEdit(PersistentNoiseStep)
        self.settings_textEdit.setObjectName(u"settings_textEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.settings_textEdit.sizePolicy().hasHeightForWidth())
        self.settings_textEdit.setSizePolicy(sizePolicy4)
        self.settings_textEdit.setMaximumSize(QSize(16777215, 16777215))
        self.settings_textEdit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.settings_textEdit.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.settings_textEdit.setAcceptDrops(False)
        self.settings_textEdit.setStyleSheet(u"")
        self.settings_textEdit.setFrameShape(QFrame.Shape.StyledPanel)
        self.settings_textEdit.setFrameShadow(QFrame.Shadow.Sunken)
        self.settings_textEdit.setLineWidth(0)
        self.settings_textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.settings_textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.settings_textEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.settings_textEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.retranslateUi(PersistentNoiseStep)

        QMetaObject.connectSlotsByName(PersistentNoiseStep)
    # setupUi

    def retranslateUi(self, PersistentNoiseStep):
        PersistentNoiseStep.setWindowTitle(QCoreApplication.translate("PersistentNoiseStep", u"Form", None))
        self.label_10.setText("")
        self.label_9.setText(QCoreApplication.translate("PersistentNoiseStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Persistent Noise : Segments with high frequency noise (&gt;25 Hz).</span></p></body></html>", None))
        self.description_textEdit.setHtml(QCoreApplication.translate("PersistentNoiseStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Identification of segments with outlier high-frequency power via spectral power analysis (Welch's method). </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">High-frequency band power (&gt;25 Hz) is computed by integrating the power spectral density estimated using Welch's method, as recommended in [1].</p>\n"
"<p style=\" margin-top:0px; margin-"
                        "bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Power is calculated using 6-s windows with a 3-s step size.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Reference</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> [1] Cox, R. &amp; Fell, J. Analyzing human sleep EEG: A methodological primer with code implementation. Sleep Medicine Reviews, 54, 101353 (2020).</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("PersistentNoiseStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Event Settings</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("PersistentNoiseStep", u"In which \"Event Group\" the detected artifact are added (label in the annotation file). Go to the general Detectors Settings to edit the group.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("PersistentNoiseStep", u"Event Group", None))
#if QT_CONFIG(tooltip)
        self.group_lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.group_lineEdit.setText(QCoreApplication.translate("PersistentNoiseStep", u"art_snooz", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("PersistentNoiseStep", u"The event name of the detected artifact (label in the annotation file). Go to the general Detectors Settings to edit the name.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("PersistentNoiseStep", u"Event Name", None))
#if QT_CONFIG(tooltip)
        self.name_fixe_lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.name_fixe_lineEdit.setText(QCoreApplication.translate("PersistentNoiseStep", u"art_snooz", None))
        self.label_8.setText(QCoreApplication.translate("PersistentNoiseStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Thresholds</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("PersistentNoiseStep", u"An artifact is identified when the spectral power exceeds two complementary thresholds:", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("PersistentNoiseStep", u"The threshold value to identify the artefact.  Its units is x times the baseline standard deviation.", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("PersistentNoiseStep", u"(A) Fixed threshold (mean + x SD)     ", None))
#if QT_CONFIG(tooltip)
        self.tresh_fixe_lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.tresh_fixe_lineEdit.setText(QCoreApplication.translate("PersistentNoiseStep", u"4", None))
        self.label_2.setText(QCoreApplication.translate("PersistentNoiseStep", u"optimal value from 3 to 5;\n"
"computed from all selected derivations", None))
        self.label.setText(QCoreApplication.translate("PersistentNoiseStep", u"(B) Power ratio (25-64 Hz/1-64 Hz)", None))
        self.thres_ratio_lineEdit.setText(QCoreApplication.translate("PersistentNoiseStep", u"0.25", None))
        self.label_6.setText(QCoreApplication.translate("PersistentNoiseStep", u"optimal value from 0.1 to 0.4", None))
        self.settings_textEdit.setHtml(QCoreApplication.translate("PersistentNoiseStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">A) Fixed threshold</span> (mean + X SD)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The power is log10-transformed to reduce skewness and improve normality. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Because th"
                        "e power distribution is often right-skewed due to artifacts, it is modeled using a three-component Gaussian Mixture Model (GMM). The distribution is estimated from all selected derivations for the recording, so excluding a derivation with poor signal quality can change the threshold applied to the remaining derivations. The threshold is defined as the mean of the main Gaussian component plus a user-defined multiple of its standard deviation (SD).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A segment is flagged when: log10(25-64 Hz power) &gt; mean + threshold x SD</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bott"
                        "om:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">B) Power ratio threshold </span>(relative power)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> High-frequency noise can be masked by strong low-frequency activity and may therefore be non-disturbing. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A segment is flagged when: (25-64 Hz power) / (1-64 Hz power) &gt; threshold</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px;\">A segment is classified as an artifact only when both thresholds are exceeded.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To reduce false positives, particularly during low-amplitude REM sleep, first increase the power ratio threshold. This requires a greater proportion of signal power in the 25-64 Hz frequency band before a segment is classified as an artifact.</p></body></html>", None))
    # retranslateUi

