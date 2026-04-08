# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_PowerLineStep.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_PowerLineStep(object):
    def setupUi(self, PowerLineStep):
        if not PowerLineStep.objectName():
            PowerLineStep.setObjectName(u"PowerLineStep")
        PowerLineStep.resize(1623, 646)
        PowerLineStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_4 = QVBoxLayout(PowerLineStep)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.imageWidget = QWidget(PowerLineStep)
        self.imageWidget.setObjectName(u"imageWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageWidget.sizePolicy().hasHeightForWidth())
        self.imageWidget.setSizePolicy(sizePolicy)
        self.imageWidget.setMinimumSize(QSize(0, 100))
        self.horizontalLayout = QHBoxLayout(self.imageWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_10 = QLabel(self.imageWidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setMinimumSize(QSize(0, 0))
        self.label_10.setMaximumSize(QSize(16777215, 16777215))
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_10)

        self.verticalLayout_4.addWidget(self.imageWidget)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_9 = QLabel(PowerLineStep)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_9.setFont(font)

        self.verticalLayout_3.addWidget(self.label_9)

        self.description_textEdit = QTextEdit(PowerLineStep)
        self.description_textEdit.setObjectName(u"description_textEdit")
        sizePolicy.setHeightForWidth(self.description_textEdit.sizePolicy().hasHeightForWidth())
        self.description_textEdit.setSizePolicy(sizePolicy)
        self.description_textEdit.setMinimumSize(QSize(0, 230))
        self.description_textEdit.setMaximumSize(QSize(16777215, 16777215))
        self.description_textEdit.setAutoFillBackground(True)
        self.description_textEdit.setStyleSheet(u"")
        self.description_textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.description_textEdit.setFrameShadow(QFrame.Shadow.Sunken)
        self.description_textEdit.setLineWidth(1)
        self.description_textEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.description_textEdit)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_4 = QLabel(PowerLineStep)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMinimumSize(QSize(0, 20))
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_3 = QLabel(PowerLineStep)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMinimumSize(QSize(120, 0))
        self.label_3.setMaximumSize(QSize(120, 16777215))
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.group_lineEdit = QLineEdit(PowerLineStep)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.group_lineEdit.sizePolicy().hasHeightForWidth())
        self.group_lineEdit.setSizePolicy(sizePolicy3)
        self.group_lineEdit.setMinimumSize(QSize(300, 0))
        self.group_lineEdit.setMaximumSize(QSize(300, 16777215))
        self.group_lineEdit.setFont(font)

        self.horizontalLayout_2.addWidget(self.group_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_11 = QLabel(PowerLineStep)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setMinimumSize(QSize(120, 0))
        self.label_11.setMaximumSize(QSize(120, 16777215))
        self.label_11.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.name_rel_lineEdit = QLineEdit(PowerLineStep)
        self.name_rel_lineEdit.setObjectName(u"name_rel_lineEdit")
        self.name_rel_lineEdit.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.name_rel_lineEdit.sizePolicy().hasHeightForWidth())
        self.name_rel_lineEdit.setSizePolicy(sizePolicy3)
        self.name_rel_lineEdit.setMinimumSize(QSize(300, 0))
        self.name_rel_lineEdit.setMaximumSize(QSize(300, 16777215))
        self.name_rel_lineEdit.setFont(font)

        self.horizontalLayout_3.addWidget(self.name_rel_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.settings_textEdit = QTextEdit(PowerLineStep)
        self.settings_textEdit.setObjectName(u"settings_textEdit")
        self.settings_textEdit.setMinimumSize(QSize(0, 0))
        self.settings_textEdit.setMaximumSize(QSize(16777215, 200))
        self.settings_textEdit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.settings_textEdit.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.settings_textEdit.setAcceptDrops(False)
        self.settings_textEdit.setAutoFillBackground(True)
        self.settings_textEdit.setStyleSheet(u"")
        self.settings_textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.settings_textEdit.setFrameShadow(QFrame.Shadow.Sunken)
        self.settings_textEdit.setLineWidth(1)
        self.settings_textEdit.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.settings_textEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label = QLabel(PowerLineStep)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.label_8 = QLabel(PowerLineStep)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_2.addWidget(self.label_8)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.thresh_rel_lineEdit = QLineEdit(PowerLineStep)
        self.thresh_rel_lineEdit.setObjectName(u"thresh_rel_lineEdit")
        self.thresh_rel_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.thresh_rel_lineEdit.setFont(font)

        self.gridLayout.addWidget(self.thresh_rel_lineEdit, 1, 1, 1, 1)

        self.label_7 = QLabel(PowerLineStep)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)

        self.tresh_abs_lineEdit = QLineEdit(PowerLineStep)
        self.tresh_abs_lineEdit.setObjectName(u"tresh_abs_lineEdit")
        self.tresh_abs_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.tresh_abs_lineEdit.setFont(font)

        self.gridLayout.addWidget(self.tresh_abs_lineEdit, 0, 1, 1, 1)

        self.label_6 = QLabel(PowerLineStep)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setTextFormat(Qt.TextFormat.RichText)

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_2 = QLabel(PowerLineStep)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.TextFormat.RichText)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_12 = QLabel(PowerLineStep)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.label_5 = QLabel(PowerLineStep)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_2.addWidget(self.label_5)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.retranslateUi(PowerLineStep)

        QMetaObject.connectSlotsByName(PowerLineStep)
    # setupUi

    def retranslateUi(self, PowerLineStep):
        PowerLineStep.setWindowTitle(QCoreApplication.translate("PowerLineStep", u"Form", None))
        self.label_10.setText("")
        self.label_9.setText(QCoreApplication.translate("PowerLineStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Power Line Contamination : Segments corrupted by 50 or 60 Hz power.</span></p></body></html>", None))
        self.description_textEdit.setHtml(QCoreApplication.translate("PowerLineStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Identification of segments with power line contamination (50 or 60 Hz) via spectral power (STFT : Short Term Fourier Transform). The absolute and the relative power are computed. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-le"
                        "ft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Fixed threshold</span><span style=\" color:#000000;\"> (mean + x STD)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The power is log10 transformed to make the data more normally distributed, however the distribution of the power of all selected channels is often skewed right du to artifacts.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The distribution is then modeled by a 3-components Gaussian Mixture Model (GMM).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The threshold is multiplied by the standard deviation (STD) and added to the mean of the main gaussian (over a mixture of 3).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:"
                        "0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">An artifact is possibly identified when the log10(power) &gt; (mean + threshold*STD)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Power ratio threshold</span> (relative power)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Power line contamination can be masked (thus non-disturbing) by a strong low frequency signal. An artifact is possibly identified when the relative power (60 Hz)/(1-61 Hz) &gt; threshold.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\""
                        " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A segment whose power exceeds the 2 thresholds is considered an artifact.</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("PowerLineStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Event Settings</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("PowerLineStep", u"Event Group", None))
#if QT_CONFIG(tooltip)
        self.group_lineEdit.setToolTip(QCoreApplication.translate("PowerLineStep", u"In which \"Event Group\" the detected artifact are added (label in the annotation file). Go to the general Detectors Settings to edit the group.", None))
#endif // QT_CONFIG(tooltip)
        self.group_lineEdit.setText(QCoreApplication.translate("PowerLineStep", u"art_snooz", None))
        self.label_11.setText(QCoreApplication.translate("PowerLineStep", u"Event Name", None))
#if QT_CONFIG(tooltip)
        self.name_rel_lineEdit.setToolTip(QCoreApplication.translate("PowerLineStep", u"The event name of the detected artifact based on the absolute power. Go to the general Detectors Settings to edit the name.", None))
#endif // QT_CONFIG(tooltip)
        self.name_rel_lineEdit.setText(QCoreApplication.translate("PowerLineStep", u"art_snooz", None))
        self.settings_textEdit.setHtml(QCoreApplication.translate("PowerLineStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">The power is computed on sliding windows through STFT.<br />Window length = 6 s<br />Window step = 3 s </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#000000;\">The STFT is applied to integrate (sum) the signal power within a frequency ran"
                        "ge of the true spectrum (units\u00b2 ex. \u00b5V\u00b2) as suggested in [1].</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pubmed.ncbi.nlm.nih.gov/12723066/\"><span style=\" text-decoration: underline; color:#000000;\">Reference</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">[1] Cox, R. &amp; Fell, J. Analyzing human sleep EEG: A methodological primer with code implementation. Sleep Medicine Reviews54, 101353 (2020).</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("PowerLineStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Thresholds </span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("PowerLineStep", u"Artifact when (A and B)", None))
        self.thresh_rel_lineEdit.setText(QCoreApplication.translate("PowerLineStep", u"0.1", None))
        self.label_7.setText(QCoreApplication.translate("PowerLineStep", u"optimal value from 0 to 2, where 0 is the mean", None))
        self.tresh_abs_lineEdit.setText(QCoreApplication.translate("PowerLineStep", u"0", None))
        self.label_6.setText(QCoreApplication.translate("PowerLineStep", u"<html><head/><body><p>(B) Power ratio (60Hz/1-61Hz)</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("PowerLineStep", u"(A) Fixed (mean + X STD)", None))
        self.label_12.setText(QCoreApplication.translate("PowerLineStep", u"optimal value from 0.05 to 0.2", None))
        self.label_5.setText(QCoreApplication.translate("PowerLineStep", u"* or 50 Hz when selected in Detectors Settings Step", None))
    # retranslateUi

