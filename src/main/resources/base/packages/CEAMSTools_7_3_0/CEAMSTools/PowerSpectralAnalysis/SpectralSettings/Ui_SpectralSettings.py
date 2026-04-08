# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SpectralSettings.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QRadioButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_SpectralSettings(object):
    def setupUi(self, SpectralSettings):
        if not SpectralSettings.objectName():
            SpectralSettings.setObjectName(u"SpectralSettings")
        SpectralSettings.resize(739, 546)
        SpectralSettings.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(SpectralSettings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.label_3 = QLabel(SpectralSettings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.textEdit_2 = QTextEdit(SpectralSettings)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(0, 0))
        self.textEdit_2.setMaximumSize(QSize(16777215, 110))
        self.textEdit_2.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_2.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_2.setLineWidth(0)
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.textEdit_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.label_2 = QLabel(SpectralSettings)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(200, 0))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.win_step_lineEdit = QLineEdit(SpectralSettings)
        self.win_step_lineEdit.setObjectName(u"win_step_lineEdit")
        self.win_step_lineEdit.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.win_step_lineEdit, 1, 1, 1, 1)

        self.win_len_lineEdit = QLineEdit(SpectralSettings)
        self.win_len_lineEdit.setObjectName(u"win_len_lineEdit")
        self.win_len_lineEdit.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.win_len_lineEdit, 0, 1, 1, 1)

        self.label = QLabel(SpectralSettings)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(450, 0))
        self.label.setMaximumSize(QSize(500, 500))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_7 = QLabel(SpectralSettings)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setFont(font)

        self.verticalLayout_5.addWidget(self.label_7)

        self.textEdit = QTextEdit(SpectralSettings)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit.setSizeIncrement(QSize(0, 0))
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.textEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout_5)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_8 = QLabel(SpectralSettings)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(450, 0))
        self.label_8.setMaximumSize(QSize(450, 16777215))

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.miniband_lineEdit = QLineEdit(SpectralSettings)
        self.miniband_lineEdit.setObjectName(u"miniband_lineEdit")
        self.miniband_lineEdit.setMinimumSize(QSize(0, 0))
        self.miniband_lineEdit.setMaximumSize(QSize(80, 16777215))
        self.miniband_lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.miniband_lineEdit, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(58, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.label_4 = QLabel(SpectralSettings)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.first_freq_lineEdit = QLineEdit(SpectralSettings)
        self.first_freq_lineEdit.setObjectName(u"first_freq_lineEdit")
        self.first_freq_lineEdit.setMaximumSize(QSize(80, 16777215))
        self.first_freq_lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.first_freq_lineEdit, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.label_9 = QLabel(SpectralSettings)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QSize(300, 0))
        self.label_9.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)

        self.last_freq_lineEdit = QLineEdit(SpectralSettings)
        self.last_freq_lineEdit.setObjectName(u"last_freq_lineEdit")
        self.last_freq_lineEdit.setMaximumSize(QSize(80, 16777215))
        self.last_freq_lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.last_freq_lineEdit, 2, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 2, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.label_10 = QLabel(SpectralSettings)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_10)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(SpectralSettings)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_4.addWidget(self.label_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.std_radioButton = QRadioButton(SpectralSettings)
        self.std_radioButton.setObjectName(u"std_radioButton")
        self.std_radioButton.setEnabled(True)
        self.std_radioButton.setMinimumSize(QSize(225, 0))
        self.std_radioButton.setMaximumSize(QSize(500, 16777215))
        self.std_radioButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.std_radioButton)

        self.RA_radioButton = QRadioButton(SpectralSettings)
        self.RA_radioButton.setObjectName(u"RA_radioButton")
        self.RA_radioButton.setEnabled(False)
        self.RA_radioButton.setMinimumSize(QSize(225, 0))

        self.horizontalLayout_3.addWidget(self.RA_radioButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalSpacer = QSpacerItem(709, 19, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(SpectralSettings)
        self.win_len_lineEdit.editingFinished.connect(SpectralSettings.miniband_edit_slot)
        self.last_freq_lineEdit.editingFinished.connect(SpectralSettings.lastfreq_edit_slot)
        self.miniband_lineEdit.editingFinished.connect(SpectralSettings.miniband_edit_slot)

        QMetaObject.connectSlotsByName(SpectralSettings)
    # setupUi

    def retranslateUi(self, SpectralSettings):
        SpectralSettings.setWindowTitle("")
        SpectralSettings.setStyleSheet(QCoreApplication.translate("SpectralSettings", u"font: 12pt \"Roboto\";", None))
        self.label_3.setText(QCoreApplication.translate("SpectralSettings", u"<html><head/><body><p><span style=\" font-weight:700;\">Windowed FFT Settings</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("SpectralSettings", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The analysis is performed by dividing the signal into multiple short windows to estimate spectral power. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This procedure is based on Welch\u2019s method, which applies a Fast Fourier Transform (FFT) to each window and averages the resulting periodograms.</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("SpectralSettings", u"Window step (s)", None))
#if QT_CONFIG(tooltip)
        self.win_step_lineEdit.setToolTip(QCoreApplication.translate("SpectralSettings", u"At which window steps (s) the FFT (Fast Fourier Transform) is performed.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.win_len_lineEdit.setToolTip(QCoreApplication.translate("SpectralSettings", u"Window length (s) used to perform the FFT (Fast Fourier Transform).", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("SpectralSettings", u"Window length (s)", None))
        self.label_7.setText(QCoreApplication.translate("SpectralSettings", u"<html><head/><body><p><span style=\" font-weight:600;\">Frequency bands</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("SpectralSettings", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It is common to average the power from a few frequency bins in order to estimate the spectral power in a frequency band.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0"
                        "px;\">The width of the mini bands has to be equal or larger than the FFT frequency bin resolution (Hz) which is :</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   1 / [fft windows length (s)]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   i.e. 1 / 5 s = 0.2 Hz or 1 / 4 s = 0.25 Hz</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The mini bandwidth must be a multiple of the frequency bin resolution.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-&gt; bandwidth of 0.2 Hz or 1 Hz with a fft windows length of 5 s.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-&gt; bandwidth of 0.25 Hz, 0.5 Hz or 1 Hz with a"
                        " fft windows length of 4 s. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The last frequency analyzed is limited to FS/2.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   FS : Sampling rate of the channel (Hz)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   i.e. 256 Hz / 2 = 128 Hz</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("SpectralSettings", u"Width of each mini band (Hz) (the first band can be smaller)", None))
        self.miniband_lineEdit.setText(QCoreApplication.translate("SpectralSettings", u"0.5", None))
        self.label_4.setText(QCoreApplication.translate("SpectralSettings", u"First frequency analyzed (Hz)", None))
        self.first_freq_lineEdit.setText(QCoreApplication.translate("SpectralSettings", u"0.0", None))
        self.label_9.setText(QCoreApplication.translate("SpectralSettings", u"Last frequency analyzed (Hz)", None))
        self.last_freq_lineEdit.setText(QCoreApplication.translate("SpectralSettings", u"64", None))
        self.label_10.setText(QCoreApplication.translate("SpectralSettings", u"<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">* Warning : The last frequency is limited to FS/2 </span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("SpectralSettings", u"<html><head/><body><p><span style=\" font-weight:600;\">Power Spectral Analysis</span></p></body></html>", None))
        self.std_radioButton.setText(QCoreApplication.translate("SpectralSettings", u"Standard ", None))
        self.RA_radioButton.setText(QCoreApplication.translate("SpectralSettings", u"Rythmic/arythmic", None))
    # retranslateUi

