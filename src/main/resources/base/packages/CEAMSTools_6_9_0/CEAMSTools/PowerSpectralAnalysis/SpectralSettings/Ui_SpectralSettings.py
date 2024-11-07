# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SpectralSettings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_SpectralSettings(object):
    def setupUi(self, SpectralSettings):
        if not SpectralSettings.objectName():
            SpectralSettings.setObjectName(u"SpectralSettings")
        SpectralSettings.resize(730, 738)
        SpectralSettings.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(SpectralSettings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(SpectralSettings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.plainTextEdit_2 = QPlainTextEdit(SpectralSettings)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setMinimumSize(QSize(0, 45))
        self.plainTextEdit_2.setMaximumSize(QSize(16777215, 80))
        self.plainTextEdit_2.setFrameShape(QFrame.HLine)
        self.plainTextEdit_2.setFrameShadow(QFrame.Plain)
        self.plainTextEdit_2.setLineWidth(0)
        self.plainTextEdit_2.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.label_2 = QLabel(SpectralSettings)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
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
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(350, 0))
        self.label.setMaximumSize(QSize(500, 500))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(SpectralSettings)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setFont(font)

        self.verticalLayout_5.addWidget(self.label_7)

        self.plainTextEdit = QPlainTextEdit(SpectralSettings)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy1)
        self.plainTextEdit.setMinimumSize(QSize(0, 300))
        self.plainTextEdit.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit.setFrameShape(QFrame.HLine)
        self.plainTextEdit.setFrameShadow(QFrame.Plain)
        self.plainTextEdit.setLineWidth(0)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.plainTextEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout_5)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_8 = QLabel(SpectralSettings)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(350, 0))
        self.label_8.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.miniband_lineEdit = QLineEdit(SpectralSettings)
        self.miniband_lineEdit.setObjectName(u"miniband_lineEdit")
        self.miniband_lineEdit.setMinimumSize(QSize(0, 0))
        self.miniband_lineEdit.setMaximumSize(QSize(80, 16777215))
        self.miniband_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.miniband_lineEdit, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(58, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.label_4 = QLabel(SpectralSettings)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.first_freq_lineEdit = QLineEdit(SpectralSettings)
        self.first_freq_lineEdit.setObjectName(u"first_freq_lineEdit")
        self.first_freq_lineEdit.setMaximumSize(QSize(80, 16777215))
        self.first_freq_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.first_freq_lineEdit, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.last_freq_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.last_freq_lineEdit, 2, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 2, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.label_10 = QLabel(SpectralSettings)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_10)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

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
        self.std_radioButton.setMinimumSize(QSize(175, 0))
        self.std_radioButton.setMaximumSize(QSize(500, 16777215))
        self.std_radioButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.std_radioButton)

        self.RA_radioButton = QRadioButton(SpectralSettings)
        self.RA_radioButton.setObjectName(u"RA_radioButton")
        self.RA_radioButton.setEnabled(False)
        self.RA_radioButton.setMinimumSize(QSize(175, 0))

        self.horizontalLayout_3.addWidget(self.RA_radioButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalSpacer = QSpacerItem(709, 19, QSizePolicy.Minimum, QSizePolicy.Expanding)

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
        self.label_3.setText(QCoreApplication.translate("SpectralSettings", u"<html><head/><body><p><span style=\" font-weight:600;\">Short Time Fourier Transform Settings</span></p></body></html>", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("SpectralSettings", u"The PSA is performed through many short windows in order to estimate the spectral power.  The procedure is called Short Time Fourier Transform (STFT).\n"
"Define the window length (s) used to perform each FFT (Fast Fourier Transform) and at which window steps (s) each FFT is performed.", None))
        self.label_2.setText(QCoreApplication.translate("SpectralSettings", u"Window step (s)", None))
#if QT_CONFIG(tooltip)
        self.win_step_lineEdit.setToolTip(QCoreApplication.translate("SpectralSettings", u"At which window steps (s) the FFT (Fast Fourier Transform) is performed.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.win_len_lineEdit.setToolTip(QCoreApplication.translate("SpectralSettings", u"Window length (s) used to perform the FFT (Fast Fourier Transform).", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("SpectralSettings", u"Window length (s)", None))
        self.label_7.setText(QCoreApplication.translate("SpectralSettings", u"<html><head/><body><p><span style=\" font-weight:600;\">Frequency bands</span></p></body></html>", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("SpectralSettings", u"It is common to average the power from a few frequency bins in order to estimate the spectral power in a frequency band.\n"
"\n"
"The width of the mini bands has to be equal or larger than the FFT frequency bin resolution (Hz) which is :\n"
"   1 / [fft windows length (s)]\n"
"   i.e. 1 / 5 s = 0.2 Hz or 1 / 4 s = 0.25 Hz\n"
"The mini bandwidth must be a multiple of the frequency bin resolution.\n"
"-> bandwidth of 0.2 Hz or 1 Hz with a fft windows length of 5 s.\n"
"-> bandwidth of 0.25 Hz, 0.5 Hz or 1 Hz with a fft windows length of 4 s. \n"
"\n"
"The last frequency analyzed is limited to FS/2.\n"
"   FS : Sampling rate of the channel (Hz)\n"
"   i.e. 256 Hz / 2 = 128 Hz", None))
        self.label_8.setText(QCoreApplication.translate("SpectralSettings", u"Width of each mini band (Hz) (the first band can be smaller)", None))
        self.miniband_lineEdit.setText(QCoreApplication.translate("SpectralSettings", u"0.5", None))
        self.label_4.setText(QCoreApplication.translate("SpectralSettings", u"First frequency analyzed (Hz)", None))
        self.first_freq_lineEdit.setText(QCoreApplication.translate("SpectralSettings", u"0.0", None))
        self.label_9.setText(QCoreApplication.translate("SpectralSettings", u"Last frequency analyzed (Hz)", None))
        self.last_freq_lineEdit.setText(QCoreApplication.translate("SpectralSettings", u"64", None))
        self.label_10.setText(QCoreApplication.translate("SpectralSettings", u"<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">* Warning : The last frequency is limited to FS/2 </span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("SpectralSettings", u"<html><head/><body><p><span style=\" font-weight:600;\">PSA technique</span></p></body></html>", None))
        self.std_radioButton.setText(QCoreApplication.translate("SpectralSettings", u"Standard ", None))
        self.RA_radioButton.setText(QCoreApplication.translate("SpectralSettings", u"Rythmic/arythmic", None))
    # retranslateUi

