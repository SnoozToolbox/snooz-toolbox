# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_A7Settings.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox, QApplication, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_A7Settings(object):
    def setupUi(self, A7Settings):
        if not A7Settings.objectName():
            A7Settings.setObjectName(u"A7Settings")
        A7Settings.resize(1125, 880)
        self.verticalLayout = QVBoxLayout(A7Settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(A7Settings)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_6.setFont(font)

        self.verticalLayout.addWidget(self.label_6)

        self.textEdit = QTextEdit(A7Settings)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 100))
        self.textEdit.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.label_15 = QLabel(A7Settings)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_4.addWidget(self.label_15, 0, 2, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(A7Settings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(275, 0))
        self.label_3.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.name_lineEdit = QLineEdit(A7Settings)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(120, 0))
        self.name_lineEdit.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_3.addWidget(self.name_lineEdit)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 1, 4, 1, 1)

        self.label = QLabel(A7Settings)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(A7Settings)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(275, 0))
        self.label_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.label_2)

        self.group_lineEdit = QLineEdit(A7Settings)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setMinimumSize(QSize(120, 0))
        self.group_lineEdit.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.group_lineEdit)


        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_14 = QLabel(A7Settings)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_4.addWidget(self.label_14)

        self.doubleSpinBox_Lower_Bound = QDoubleSpinBox(A7Settings)
        self.doubleSpinBox_Lower_Bound.setObjectName(u"doubleSpinBox_Lower_Bound")
        self.doubleSpinBox_Lower_Bound.setSingleStep(0.100000000000000)
        self.doubleSpinBox_Lower_Bound.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.doubleSpinBox_Lower_Bound.setValue(11.000000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_Lower_Bound)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 1, 2, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_16 = QLabel(A7Settings)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_5.addWidget(self.label_16)

        self.doubleSpinBox_Upper_Bound = QDoubleSpinBox(A7Settings)
        self.doubleSpinBox_Upper_Bound.setObjectName(u"doubleSpinBox_Upper_Bound")
        self.doubleSpinBox_Upper_Bound.setSingleStep(0.100000000000000)
        self.doubleSpinBox_Upper_Bound.setValue(16.000000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_Upper_Bound)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 34, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.textEdit_6 = QTextEdit(A7Settings)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setMaximumSize(QSize(16777215, 65))
        self.textEdit_6.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_6.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_6.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit_6)

        self.label_5 = QLabel(A7Settings)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.doubleSpinBox_relSigma = QDoubleSpinBox(A7Settings)
        self.doubleSpinBox_relSigma.setObjectName(u"doubleSpinBox_relSigma")
        self.doubleSpinBox_relSigma.setMaximum(30.000000000000000)
        self.doubleSpinBox_relSigma.setSingleStep(0.100000000000000)
        self.doubleSpinBox_relSigma.setValue(1.600000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_relSigma, 1, 1, 1, 1)

        self.label_8 = QLabel(A7Settings)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_11 = QLabel(A7Settings)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 1, 2, 1, 1)

        self.label_7 = QLabel(A7Settings)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(230, 0))
        self.label_7.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_9 = QLabel(A7Settings)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)

        self.doubleSpinBox_sigmaCov = QDoubleSpinBox(A7Settings)
        self.doubleSpinBox_sigmaCov.setObjectName(u"doubleSpinBox_sigmaCov")
        self.doubleSpinBox_sigmaCov.setMaximum(30.000000000000000)
        self.doubleSpinBox_sigmaCov.setSingleStep(0.100000000000000)
        self.doubleSpinBox_sigmaCov.setValue(1.300000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_sigmaCov, 2, 1, 1, 1)

        self.label_13 = QLabel(A7Settings)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 3, 2, 1, 1)

        self.label_10 = QLabel(A7Settings)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)

        self.doubleSpinBox_absSigma = QDoubleSpinBox(A7Settings)
        self.doubleSpinBox_absSigma.setObjectName(u"doubleSpinBox_absSigma")
        self.doubleSpinBox_absSigma.setSingleStep(0.250000000000000)
        self.doubleSpinBox_absSigma.setValue(1.250000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_absSigma, 0, 1, 1, 1)

        self.label_4 = QLabel(A7Settings)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(275, 0))

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_12 = QLabel(A7Settings)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 2, 2, 1, 1)

        self.doubleSpinBox_sigmaCor = QDoubleSpinBox(A7Settings)
        self.doubleSpinBox_sigmaCor.setObjectName(u"doubleSpinBox_sigmaCor")
        self.doubleSpinBox_sigmaCor.setDecimals(0)
        self.doubleSpinBox_sigmaCor.setValue(69.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_sigmaCor, 3, 1, 1, 1)

        self.textEdit_2 = QTextEdit(A7Settings)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(400, 0))
        self.textEdit_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.textEdit_2.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit_2, 0, 3, 1, 1)

        self.textEdit_5 = QTextEdit(A7Settings)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setMinimumSize(QSize(400, 0))
        self.textEdit_5.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.textEdit_5.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit_5, 1, 3, 1, 1)

        self.textEdit_3 = QTextEdit(A7Settings)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMinimumSize(QSize(400, 0))
        self.textEdit_3.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.textEdit_3.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit_3, 2, 3, 1, 1)

        self.textEdit_4 = QTextEdit(A7Settings)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMinimumSize(QSize(400, 0))
        self.textEdit_4.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.textEdit_4.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit_4, 3, 3, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 34, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(A7Settings)

        QMetaObject.connectSlotsByName(A7Settings)
    # setupUi

    def retranslateUi(self, A7Settings):
        A7Settings.setWindowTitle("")
        A7Settings.setStyleSheet(QCoreApplication.translate("A7Settings", u"font: 12pt \"Roboto\";", None))
        self.label_6.setText(QCoreApplication.translate("A7Settings", u"<html><head/><body><p><span style=\" font-weight:600;\">Spindle detector that emulates human scoring.</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("A7Settings", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Computes the absolute power (mean square) in the sigma band, the relative sigma power based on the power spectral density (PSD), and the covariance and correlation between the sigma-filtered and unfiltered EEG signals over sliding windows (0.3 s length with a 0.1 s step). It then detects a spindle if the 4 features extracted from EEG exceed their respective threshold (1.25 \u03bcV2, 1.6 \u00d7 STD, 1.3"
                        " \u00d7 STD and 69%).<br /><span style=\" font-weight:700;\">Note:</span> These thresholds are set for the default sigma band (11-16 Hz)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:135%;\"><span style=\" text-decoration: underline;\">Reference</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:135%;\">[1] Lacourse, K., Delfrate, J., Beaudry, J., Peppard, P., Warby, S.C., 2019. A sleep spindle detection algorithm that emulates human expert spindle scoring. Journal of Neuroscience Methods 316, 3\u201311. <a href=\"https://doi.org/10.1016/j.jneumeth.2018.08.014\"><span style=\" text-decoration: underline; color:#0000ff;\">https://doi.org/10.1016/j.jneumeth.2018.08.014<"
                        "/span></a> </p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("A7Settings", u"<html><head/><body><p><span style=\" font-weight:700;\">Sigma Band Settings</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("A7Settings", u"Name", None))
#if QT_CONFIG(tooltip)
        self.name_lineEdit.setToolTip(QCoreApplication.translate("A7Settings", u"Define the name of the spindle events.", None))
#endif // QT_CONFIG(tooltip)
        self.name_lineEdit.setText(QCoreApplication.translate("A7Settings", u"a7", None))
        self.label.setText(QCoreApplication.translate("A7Settings", u"<html><head/><body><p><span style=\" font-weight:600;\">Events Settings</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("A7Settings", u"Group", None))
#if QT_CONFIG(tooltip)
        self.group_lineEdit.setToolTip(QCoreApplication.translate("A7Settings", u"Define in which group the spindles will be added.", None))
#endif // QT_CONFIG(tooltip)
        self.group_lineEdit.setText(QCoreApplication.translate("A7Settings", u"spindle", None))
        self.label_14.setText(QCoreApplication.translate("A7Settings", u"Lower bound", None))
        self.label_16.setText(QCoreApplication.translate("A7Settings", u"Upper bound", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("A7Settings", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Warning:</span> The spindle detection thresholds are pre-set and validated specifically for the sigma frequency band (11-16 Hz). If you change the frequency band from the default values, you may need to adjust the threshold values to ensure accurate spindle detection.</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("A7Settings", u"<html><head/><body><p><span style=\" font-weight:600;\">Thresholds</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("A7Settings", u"Sigma Covariance", None))
        self.label_11.setText(QCoreApplication.translate("A7Settings", u"x STD", None))
        self.label_7.setText(QCoreApplication.translate("A7Settings", u"Relative Sigma Power (PSD)", None))
        self.label_9.setText(QCoreApplication.translate("A7Settings", u"Sigma Correlation", None))
        self.label_13.setText(QCoreApplication.translate("A7Settings", u"%", None))
        self.label_10.setText(QCoreApplication.translate("A7Settings", u"\u00b5V2", None))
        self.label_4.setText(QCoreApplication.translate("A7Settings", u"Absolute Sigma Power (Mean Square)", None))
        self.label_12.setText(QCoreApplication.translate("A7Settings", u"x STD", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("A7Settings", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">log10( mean squared sigma power )</p></body></html>", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("A7Settings", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">z-score( log10( PSD:sigma band Hz/PSD:4.5-30Hz ) )</p></body></html>", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("A7Settings", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">z-score( log10( cov( EEG:0.3-30Hz, EEG:sigma band Hz ) ) )</p></body></html>", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("A7Settings", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">cov ( EEG:0.3-30Hz, EEG:sigma band Hz )  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">std(EEG:0.3-30Hz) * std(EEG:sigma band Hz)</p></body></html>", None))
    # retranslateUi

