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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QScrollArea,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)
from . import muscular_res
import themes_rc

class Ui_MuscularStep(object):
    def setupUi(self, MuscularStep):
        if not MuscularStep.objectName():
            MuscularStep.setObjectName(u"MuscularStep")
        MuscularStep.resize(1114, 885)
        MuscularStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_4 = QVBoxLayout(MuscularStep)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea = QScrollArea(MuscularStep)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1549, 151))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.picture_label = QLabel(self.scrollAreaWidgetContents)
        self.picture_label.setObjectName(u"picture_label")
        sizePolicy.setHeightForWidth(self.picture_label.sizePolicy().hasHeightForWidth())
        self.picture_label.setSizePolicy(sizePolicy)
        self.picture_label.setPixmap(QPixmap(u":/muscular/muscular.png"))
        self.picture_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.picture_label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_9 = QLabel(MuscularStep)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_9.setFont(font)

        self.verticalLayout_3.addWidget(self.label_9)

        self.line_3 = QFrame(MuscularStep)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.description_textEdit = QTextEdit(MuscularStep)
        self.description_textEdit.setObjectName(u"description_textEdit")
        sizePolicy.setHeightForWidth(self.description_textEdit.sizePolicy().hasHeightForWidth())
        self.description_textEdit.setSizePolicy(sizePolicy)
        self.description_textEdit.setStyleSheet(u"")
        self.description_textEdit.setFrameShape(QFrame.HLine)
        self.description_textEdit.setFrameShadow(QFrame.Plain)
        self.description_textEdit.setLineWidth(0)
        self.description_textEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.description_textEdit)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(MuscularStep)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 20))
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.line = QFrame(MuscularStep)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(MuscularStep)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(140, 0))
        self.label_3.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.group_lineEdit = QLineEdit(MuscularStep)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setEnabled(False)
        self.group_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.group_lineEdit.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.group_lineEdit)

        self.label_11 = QLabel(MuscularStep)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(140, 0))
        self.label_11.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.name_eeg_lineEdit = QLineEdit(MuscularStep)
        self.name_eeg_lineEdit.setObjectName(u"name_eeg_lineEdit")
        self.name_eeg_lineEdit.setEnabled(False)
        self.name_eeg_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.name_eeg_lineEdit.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name_eeg_lineEdit)

        self.name_emg_lineEdit = QLineEdit(MuscularStep)
        self.name_emg_lineEdit.setObjectName(u"name_emg_lineEdit")
        self.name_emg_lineEdit.setEnabled(False)
        self.name_emg_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.name_emg_lineEdit.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.name_emg_lineEdit)

        self.label_7 = QLabel(MuscularStep)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(140, 0))
        self.label_7.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)


        self.verticalLayout.addLayout(self.formLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.label = QLabel(MuscularStep)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.label_8 = QLabel(MuscularStep)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 20))
        self.label_8.setMaximumSize(QSize(16777215, 20))
        self.label_8.setFont(font)

        self.verticalLayout_2.addWidget(self.label_8)

        self.line_2 = QFrame(MuscularStep)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(MuscularStep)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setFont(font)
        self.label_5.setMidLineWidth(0)
        self.label_5.setTextFormat(Qt.RichText)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.EEG_lineEdit = QLineEdit(MuscularStep)
        self.EEG_lineEdit.setObjectName(u"EEG_lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.EEG_lineEdit.sizePolicy().hasHeightForWidth())
        self.EEG_lineEdit.setSizePolicy(sizePolicy1)
        self.EEG_lineEdit.setMaximumSize(QSize(100, 16777215))
        self.EEG_lineEdit.setFont(font)

        self.gridLayout.addWidget(self.EEG_lineEdit, 0, 1, 1, 1)

        self.label_10 = QLabel(MuscularStep)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)

        self.label_2 = QLabel(MuscularStep)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.EMG_lineEdit = QLineEdit(MuscularStep)
        self.EMG_lineEdit.setObjectName(u"EMG_lineEdit")
        sizePolicy1.setHeightForWidth(self.EMG_lineEdit.sizePolicy().hasHeightForWidth())
        self.EMG_lineEdit.setSizePolicy(sizePolicy1)
        self.EMG_lineEdit.setMaximumSize(QSize(100, 16777215))
        self.EMG_lineEdit.setFont(font)

        self.gridLayout.addWidget(self.EMG_lineEdit, 1, 1, 1, 1)

        self.label_12 = QLabel(MuscularStep)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 1, 2, 1, 1)

        self.label_6 = QLabel(MuscularStep)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.both_lineEdit = QLineEdit(MuscularStep)
        self.both_lineEdit.setObjectName(u"both_lineEdit")
        sizePolicy1.setHeightForWidth(self.both_lineEdit.sizePolicy().hasHeightForWidth())
        self.both_lineEdit.setSizePolicy(sizePolicy1)
        self.both_lineEdit.setMaximumSize(QSize(100, 16777215))
        self.both_lineEdit.setFont(font)

        self.gridLayout.addWidget(self.both_lineEdit, 2, 1, 1, 1)

        self.label_13 = QLabel(MuscularStep)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 2, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.label_14 = QLabel(MuscularStep)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_2.addWidget(self.label_14)

        self.label_15 = QLabel(MuscularStep)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_2.addWidget(self.label_15)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.settings_textEdit = QTextEdit(MuscularStep)
        self.settings_textEdit.setObjectName(u"settings_textEdit")
        sizePolicy.setHeightForWidth(self.settings_textEdit.sizePolicy().hasHeightForWidth())
        self.settings_textEdit.setSizePolicy(sizePolicy)
        self.settings_textEdit.setFocusPolicy(Qt.NoFocus)
        self.settings_textEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.settings_textEdit.setAcceptDrops(False)
        self.settings_textEdit.setStyleSheet(u"")
        self.settings_textEdit.setFrameShape(QFrame.HLine)
        self.settings_textEdit.setFrameShadow(QFrame.Plain)
        self.settings_textEdit.setLineWidth(0)
        self.settings_textEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.settings_textEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.retranslateUi(MuscularStep)

        QMetaObject.connectSlotsByName(MuscularStep)
    # setupUi

    def retranslateUi(self, MuscularStep):
        MuscularStep.setWindowTitle(QCoreApplication.translate("MuscularStep", u"Form", None))
        self.picture_label.setText("")
        self.label_9.setText(QCoreApplication.translate("MuscularStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Muscular Artifact : Segments with burst of activity in the frequency band 20.25-32 Hz.</span></p></body></html>", None))
        self.description_textEdit.setHtml(QCoreApplication.translate("MuscularStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Identification of bursts of myogenic activity (26.25\u201332.0 Hz) via spectral power (STFT :  Short Term Fourier Transform).</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">The algorithm compares high frequency activity (26.25\u201332.0 Hz) in each mini 4-s epoch with the activity level in a local 3-min baseline window.\u00a0</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; marg"
                        "in-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">A muscular artifact is identified when the high frequency activity of the 4-s epoch exceeded the local baseline activity by a certain factor (ex. 4 x median value of the baseline).</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">*** To enhance the detection we also use the EMG signal. ***<br />A muscle artifact is identified when an increase in myogenic activity on the EEG signal is greater than a certain high threshold.<br />A slightly lower increase can also be identified as a muscle artifact if it is also measured on the EMG signal. <br />New, not included in [1]</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MuscularStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Event Settings</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MuscularStep", u"Event Group", None))
#if QT_CONFIG(tooltip)
        self.group_lineEdit.setToolTip(QCoreApplication.translate("MuscularStep", u"In which \"Event Group\" the detected artifact are added (label in the annotation file). Go to the general Detectors Settings to edit the group.", None))
#endif // QT_CONFIG(tooltip)
        self.group_lineEdit.setText(QCoreApplication.translate("MuscularStep", u"art_snooz", None))
        self.label_11.setText(QCoreApplication.translate("MuscularStep", u"Event Name - EEG", None))
#if QT_CONFIG(tooltip)
        self.name_eeg_lineEdit.setToolTip(QCoreApplication.translate("MuscularStep", u"The event name of the detected artifact based exclusivement on the EEG signal.  Go to the general Detectors Settings to edit the name.", None))
#endif // QT_CONFIG(tooltip)
        self.name_eeg_lineEdit.setText(QCoreApplication.translate("MuscularStep", u"art_snooz", None))
#if QT_CONFIG(tooltip)
        self.name_emg_lineEdit.setToolTip(QCoreApplication.translate("MuscularStep", u"The event name of the detected artifact using the EMG signal.  Go to the general Detectors Settings to edit the name.", None))
#endif // QT_CONFIG(tooltip)
        self.name_emg_lineEdit.setText(QCoreApplication.translate("MuscularStep", u"art_snooz", None))
        self.label_7.setText(QCoreApplication.translate("MuscularStep", u"Event Name - EMG use", None))
        self.label.setText(QCoreApplication.translate("MuscularStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Threshold (x times the baseline median)</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MuscularStep", u"Artifact when A or (B and C)", None))
        self.label_5.setText(QCoreApplication.translate("MuscularStep", u"<html><head/><body><p>(A) High applied on EEG</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.EEG_lineEdit.setToolTip(QCoreApplication.translate("MuscularStep", u"The threshold value to identify the artifact.  Its units is x times the baseline standard deviation.", None))
#endif // QT_CONFIG(tooltip)
        self.EEG_lineEdit.setText(QCoreApplication.translate("MuscularStep", u"4.5", None))
        self.label_10.setText(QCoreApplication.translate("MuscularStep", u"optimal value from 5 to 9", None))
        self.label_2.setText(QCoreApplication.translate("MuscularStep", u"(B) Applied on EMG", None))
        self.EMG_lineEdit.setText(QCoreApplication.translate("MuscularStep", u"4", None))
        self.label_12.setText(QCoreApplication.translate("MuscularStep", u"optimal value from 4 to 6", None))
        self.label_6.setText(QCoreApplication.translate("MuscularStep", u"(C) Low applied on EEG", None))
        self.both_lineEdit.setText(QCoreApplication.translate("MuscularStep", u"3.5", None))
        self.label_13.setText(QCoreApplication.translate("MuscularStep", u"optimal value from 4 to 6", None))
        self.label_14.setText(QCoreApplication.translate("MuscularStep", u"To reduce the number of false positives, especially during\n"
"spindles, alpha waves, or beta bursts\n"
"please first increase the \"A\" threshold.", None))
        self.label_15.setText(QCoreApplication.translate("MuscularStep", u"The \"B\" and \"C\" thresholds can also be inscreased,\n"
"especially if the EMG channel is unstable or really sensitive.", None))
        self.settings_textEdit.setHtml(QCoreApplication.translate("MuscularStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">EEG signals are filtered from 0.3-30 Hz.<br />EEG signals are downsampled to 64 Hz.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#000000;\">These preprocessing steps are taken from [1]</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#000000;\">Filter is a 6 th order butter"
                        "worth IIR filter in Second-Order Sections (SOS) format applied with filtfilt to correct the non-linear phase delay.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">STFT Settings</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Window length = 4 s<br />Window step = 2 s</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#000000;\">[1] suggested a window step of 4 s, but we wanted a finer time resolution</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#000000;\">The STFT is applied to integrate (sum) the signal power with"
                        "in a frequency range of the true spectrum (units\u00b2 ex. \u00b5V\u00b2) as suggested in [2].</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pubmed.ncbi.nlm.nih.gov/12723066/\"><span style=\" text-decoration: underline; color:#000000;\">Reference</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">[1] D. Brunner, R. Vasko, C. Detka, J. Monahan, C. Reynolds Iii, and D. Kupfer, \u201cMuscle artifacts in the sleep EEG: Automated detection and effect on all-night EEG power spectra,\u201d Journal of Sleep Research, vol. 5, no. 3, pp. 155\u2013164, Sep. 1996, doi: </span><a href=\"https://doi.org/10.1046/j.1365-2869.1996.00009.x\"><span style=\" text-decoration: underline; color:#000000;\">10.1046/j.1365-2869.1996.00009.x</span></a><span style=\" color:#000000;\">.</span></p>\n"
"<p style"
                        "=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">[2]\u00a0Cox, R. &amp; Fell, J. Analyzing human sleep EEG: A methodological primer with code implementation. Sleep Medicine Reviews 54, 101353 (2020).</span></p></body></html>", None))
    # retranslateUi

