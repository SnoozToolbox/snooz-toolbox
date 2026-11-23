# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_FlatlineStep.ui'
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

class Ui_FlatlineStep(object):
    def setupUi(self, FlatlineStep):
        if not FlatlineStep.objectName():
            FlatlineStep.setObjectName(u"FlatlineStep")
        FlatlineStep.resize(996, 620)
        self.verticalLayout_5 = QVBoxLayout(FlatlineStep)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(FlatlineStep)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.widget)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(FlatlineStep)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        self.label_6.setFont(font)

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(FlatlineStep)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_3.addWidget(self.label_7)

        self.textEdit_2 = QTextEdit(FlatlineStep)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_2.setLineWidth(0)
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textEdit_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(FlatlineStep)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.group_lineEdit = QLineEdit(FlatlineStep)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setEnabled(False)
        self.group_lineEdit.setMaximumSize(QSize(500, 16777215))
        self.group_lineEdit.setFont(font)

        self.gridLayout_5.addWidget(self.group_lineEdit, 0, 1, 1, 1)

        self.name_lineEdit = QLineEdit(FlatlineStep)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setEnabled(False)
        self.name_lineEdit.setMaximumSize(QSize(500, 16777215))
        self.name_lineEdit.setFont(font)

        self.gridLayout_5.addWidget(self.name_lineEdit, 1, 1, 1, 1)

        self.label_11 = QLabel(FlatlineStep)
        self.label_11.setObjectName(u"label_11")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(110, 0))

        self.gridLayout_5.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_3 = QLabel(FlatlineStep)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(110, 0))

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_5)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(FlatlineStep)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_5 = QLabel(FlatlineStep)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(140, 0))
        self.label_5.setMidLineWidth(0)
        self.label_5.setTextFormat(Qt.TextFormat.RichText)

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.threshold_lineEdit = QLineEdit(FlatlineStep)
        self.threshold_lineEdit.setObjectName(u"threshold_lineEdit")
        self.threshold_lineEdit.setMaximumSize(QSize(500, 16777215))

        self.gridLayout_4.addWidget(self.threshold_lineEdit, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.textEdit = QTextEdit(FlatlineStep)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 100))
        self.textEdit.setFrameShape(QFrame.Shape.HLine)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)

        self.gridLayout_4.addWidget(self.textEdit, 1, 0, 1, 3)


        self.verticalLayout_2.addLayout(self.gridLayout_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.retranslateUi(FlatlineStep)

        QMetaObject.connectSlotsByName(FlatlineStep)
    # setupUi

    def retranslateUi(self, FlatlineStep):
        FlatlineStep.setWindowTitle(QCoreApplication.translate("FlatlineStep", u"Form", None))
        self.label_2.setText("")
        self.label_6.setText(QCoreApplication.translate("FlatlineStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Flatline : Segments of low power, flatlined signal.</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("FlatlineStep", u"Identification of low power via spectral power analysis (Welch's method).", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("FlatlineStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Band power in the 1-64 Hz range is computed by integrating the power spectral density estimated using Welch's method, as recommended in [1]. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Power is calculated using 6-s windows with a 3-s step size. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-b"
                        "lock-indent:0; text-indent:0px;\">Segments where the broadband power falls below a user-defined threshold are flagged as flatlines.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Reference</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[1] Cox, R. &amp; Fell, J. Analyzing human sleep EEG: A methodological primer with code implementation. Sleep Medicine Reviews54, 101353 (2020).</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("FlatlineStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Event Settings</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.group_lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.group_lineEdit.setText(QCoreApplication.translate("FlatlineStep", u"art_snooz", None))
#if QT_CONFIG(tooltip)
        self.name_lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.name_lineEdit.setText(QCoreApplication.translate("FlatlineStep", u"art_snooz", None))
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip(QCoreApplication.translate("FlatlineStep", u"The event name of the detected artifact (how they will be wrtten to the annotation file).  Go to the general Detectors Settings to edit the name.", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("FlatlineStep", u"Event Name", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("FlatlineStep", u"In which \"Event Group\" the detected artifact are added (how they will be written to  the annotation file).  Go to the general Detectors Settings to edit the group.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("FlatlineStep", u"Event Group", None))
        self.label.setText(QCoreApplication.translate("FlatlineStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Threshold (\u00b5V</span><span style=\" font-weight:600; vertical-align:super;\">2</span><span style=\" font-weight:600;\">)</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("FlatlineStep", u"The threshold value to identify the artifact.  Its units is x times the baseline standard deviation.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("FlatlineStep", u"<html><head/><body><p><span style=\" font-size:12pt\">Threshold value</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.threshold_lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.threshold_lineEdit.setText(QCoreApplication.translate("FlatlineStep", u"0.25", None))
        self.textEdit.setHtml(QCoreApplication.translate("FlatlineStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To reduce the number of false positives, especially for low amplitude signals in the R stage, lower the threshold as low as you want.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Setting the value to 0.01 reduces the number of false positives.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px;\">It is also possible to deactivate the detector.</p></body></html>", None))
    # retranslateUi

