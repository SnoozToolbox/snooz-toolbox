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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QLabel, QLayout, QLineEdit,
    QRadioButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_FilterSignalSettingsView(object):
    def setupUi(self, FilterSignalSettingsView):
        if not FilterSignalSettingsView.objectName():
            FilterSignalSettingsView.setObjectName(u"FilterSignalSettingsView")
        FilterSignalSettingsView.resize(1065, 440)
        self.formLayout = QFormLayout(FilterSignalSettingsView)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(FilterSignalSettingsView)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.line_4 = QFrame(FilterSignalSettingsView)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.IR_comboBox = QComboBox(FilterSignalSettingsView)
        self.IR_comboBox.addItem("")
        self.IR_comboBox.addItem("")
        self.IR_comboBox.setObjectName(u"IR_comboBox")

        self.gridLayout.addWidget(self.IR_comboBox, 0, 1, 1, 1)

        self.type_combobox = QComboBox(FilterSignalSettingsView)
        self.type_combobox.addItem("")
        self.type_combobox.addItem("")
        self.type_combobox.addItem("")
        self.type_combobox.addItem("")
        self.type_combobox.setObjectName(u"type_combobox")

        self.gridLayout.addWidget(self.type_combobox, 0, 2, 1, 1)

        self.label_2 = QLabel(FilterSignalSettingsView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setMaximumSize(QSize(100, 16777215))
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_11 = QLabel(FilterSignalSettingsView)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)

        self.cutoff_lineedit = QLineEdit(FilterSignalSettingsView)
        self.cutoff_lineedit.setObjectName(u"cutoff_lineedit")

        self.gridLayout.addWidget(self.cutoff_lineedit, 1, 1, 1, 2)

        self.label_4 = QLabel(FilterSignalSettingsView)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setMaximumSize(QSize(100, 16777215))
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setInputMethodHints(Qt.ImhNoEditMenu|Qt.ImhNoTextHandles)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.freq_resp_unit_comboBox = QComboBox(FilterSignalSettingsView)
        self.freq_resp_unit_comboBox.addItem("")
        self.freq_resp_unit_comboBox.addItem("")
        self.freq_resp_unit_comboBox.setObjectName(u"freq_resp_unit_comboBox")

        self.gridLayout.addWidget(self.freq_resp_unit_comboBox, 3, 1, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        self.label_9 = QLabel(FilterSignalSettingsView)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout.addWidget(self.label_9)

        self.line_3 = QFrame(FilterSignalSettingsView)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_10 = QLabel(FilterSignalSettingsView)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(100, 0))
        self.label_10.setMaximumSize(QSize(100, 16777215))
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)

        self.iir_order_lineEdit = QLineEdit(FilterSignalSettingsView)
        self.iir_order_lineEdit.setObjectName(u"iir_order_lineEdit")

        self.gridLayout_4.addWidget(self.iir_order_lineEdit, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.textEdit = QTextEdit(FilterSignalSettingsView)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(380, 70))
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.label_8 = QLabel(FilterSignalSettingsView)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout.addWidget(self.label_8)

        self.line_2 = QFrame(FilterSignalSettingsView)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label = QLabel(FilterSignalSettingsView)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.window_combobox = QComboBox(FilterSignalSettingsView)
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.setObjectName(u"window_combobox")
        self.window_combobox.setEnabled(False)

        self.gridLayout_2.addWidget(self.window_combobox, 3, 1, 1, 1)

        self.sleep_std_radiobutton = QRadioButton(FilterSignalSettingsView)
        self.sleep_std_radiobutton.setObjectName(u"sleep_std_radiobutton")
        self.sleep_std_radiobutton.setEnabled(False)
        self.sleep_std_radiobutton.setMinimumSize(QSize(100, 0))
        self.sleep_std_radiobutton.setMaximumSize(QSize(100, 16777215))
        self.sleep_std_radiobutton.setChecked(False)

        self.gridLayout_2.addWidget(self.sleep_std_radiobutton, 0, 0, 1, 1)

        self.std_order_lineedit = QLineEdit(FilterSignalSettingsView)
        self.std_order_lineedit.setObjectName(u"std_order_lineedit")
        self.std_order_lineedit.setEnabled(False)
        self.std_order_lineedit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.std_order_lineedit, 0, 1, 1, 1)

        self.custom_radiobutton = QRadioButton(FilterSignalSettingsView)
        self.custom_radiobutton.setObjectName(u"custom_radiobutton")
        self.custom_radiobutton.setEnabled(False)
        self.custom_radiobutton.setMinimumSize(QSize(100, 0))
        self.custom_radiobutton.setMaximumSize(QSize(100, 16777215))
        self.custom_radiobutton.setChecked(True)

        self.gridLayout_2.addWidget(self.custom_radiobutton, 2, 0, 1, 1)

        self.custom_order_lineedit = QLineEdit(FilterSignalSettingsView)
        self.custom_order_lineedit.setObjectName(u"custom_order_lineedit")
        self.custom_order_lineedit.setEnabled(False)

        self.gridLayout_2.addWidget(self.custom_order_lineedit, 2, 1, 1, 1)

        self.label_3 = QLabel(FilterSignalSettingsView)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setMaximumSize(QSize(100, 16777215))
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.line = QFrame(FilterSignalSettingsView)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_7 = QLabel(FilterSignalSettingsView)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_6 = QLabel(FilterSignalSettingsView)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 0))
        self.label_6.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.sample_rate_lineedit = QLineEdit(FilterSignalSettingsView)
        self.sample_rate_lineedit.setObjectName(u"sample_rate_lineedit")

        self.gridLayout_3.addWidget(self.sample_rate_lineedit, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.verticalSpacer = QSpacerItem(17, 17, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout)

        self.freq_resp_layout = QVBoxLayout()
        self.freq_resp_layout.setObjectName(u"freq_resp_layout")
        self.freq_resp_layout.setSizeConstraint(QLayout.SetMinimumSize)

        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.freq_resp_layout)


        self.retranslateUi(FilterSignalSettingsView)
        self.type_combobox.currentTextChanged.connect(FilterSignalSettingsView.on_settings_changed)
        self.sleep_std_radiobutton.clicked.connect(FilterSignalSettingsView.on_order_type_changed)
        self.custom_radiobutton.clicked.connect(FilterSignalSettingsView.on_order_type_changed)
        self.cutoff_lineedit.returnPressed.connect(FilterSignalSettingsView.on_settings_changed)
        self.window_combobox.currentTextChanged.connect(FilterSignalSettingsView.on_settings_changed)
        self.sample_rate_lineedit.returnPressed.connect(FilterSignalSettingsView.on_settings_changed)
        self.custom_order_lineedit.textChanged.connect(FilterSignalSettingsView.on_settings_changed)
        self.IR_comboBox.currentTextChanged.connect(FilterSignalSettingsView.on_settings_changed)
        self.iir_order_lineEdit.returnPressed.connect(FilterSignalSettingsView.on_settings_changed)
        self.freq_resp_unit_comboBox.currentTextChanged.connect(FilterSignalSettingsView.on_settings_changed)

        self.window_combobox.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(FilterSignalSettingsView)
    # setupUi

    def retranslateUi(self, FilterSignalSettingsView):
        FilterSignalSettingsView.setWindowTitle(QCoreApplication.translate("FilterSignalSettingsView", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("FilterSignalSettingsView", u"Filter settings", None))
        self.IR_comboBox.setItemText(0, QCoreApplication.translate("FilterSignalSettingsView", u"IIR", None))
        self.IR_comboBox.setItemText(1, QCoreApplication.translate("FilterSignalSettingsView", u"FIR", None))

#if QT_CONFIG(tooltip)
        self.IR_comboBox.setToolTip(QCoreApplication.translate("FilterSignalSettingsView", u"Select the Infinite Impulse Response Filter (IIR) or the Finite Impulse Filter (FIR).", None))
#endif // QT_CONFIG(tooltip)
        self.type_combobox.setItemText(0, QCoreApplication.translate("FilterSignalSettingsView", u"bandpass", None))
        self.type_combobox.setItemText(1, QCoreApplication.translate("FilterSignalSettingsView", u"lowpass", None))
        self.type_combobox.setItemText(2, QCoreApplication.translate("FilterSignalSettingsView", u"highpass", None))
        self.type_combobox.setItemText(3, QCoreApplication.translate("FilterSignalSettingsView", u"bandstop", None))

        self.label_2.setText(QCoreApplication.translate("FilterSignalSettingsView", u"Cutoff", None))
        self.label_11.setText(QCoreApplication.translate("FilterSignalSettingsView", u"Frequency response units", None))
#if QT_CONFIG(tooltip)
        self.cutoff_lineedit.setToolTip(QCoreApplication.translate("FilterSignalSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">bandpass</span> : edit low and high frequency cutoff in Hz separated by a space. ex)0.3 100</p><p><span style=\" font-weight:600;\">lowpass</span> : edit high frequency cutoff in Hz.</p><p><span style=\" font-weight:600;\">highpass</span> : edit low frequency cutoff in Hz.</p><p><span style=\" font-weight:600;\">stopband</span> : edit the low and high frequency cutoff in Hz separated by a space. ex)59 61</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cutoff_lineedit.setText(QCoreApplication.translate("FilterSignalSettingsView", u"0.3 100", None))
        self.label_4.setText(QCoreApplication.translate("FilterSignalSettingsView", u"Type", None))
        self.freq_resp_unit_comboBox.setItemText(0, QCoreApplication.translate("FilterSignalSettingsView", u"Attenuation (dB)", None))
        self.freq_resp_unit_comboBox.setItemText(1, QCoreApplication.translate("FilterSignalSettingsView", u"Amplitude (%)", None))

        self.label_9.setText(QCoreApplication.translate("FilterSignalSettingsView", u"IIR Filter Settings", None))
        self.label_10.setText(QCoreApplication.translate("FilterSignalSettingsView", u"Order", None))
        self.iir_order_lineEdit.setText(QCoreApplication.translate("FilterSignalSettingsView", u"6", None))
        self.textEdit.setHtml(QCoreApplication.translate("FilterSignalSettingsView", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The IIR filter is applied forward and backward to cancel the phase delay.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The order is divided by 2 when applied since is it applied twice.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ex) An ordre of 6 is sufficient for a bandpass filter </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-in"
                        "dent:0px;\">      0.3-100 Hz with a sample rate=256 Hz</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("FilterSignalSettingsView", u"FIR Filter Settings", None))
        self.label.setText(QCoreApplication.translate("FilterSignalSettingsView", u"Order", None))
        self.window_combobox.setItemText(0, QCoreApplication.translate("FilterSignalSettingsView", u"boxcar", None))
        self.window_combobox.setItemText(1, QCoreApplication.translate("FilterSignalSettingsView", u"trlang", None))
        self.window_combobox.setItemText(2, QCoreApplication.translate("FilterSignalSettingsView", u"blackman", None))
        self.window_combobox.setItemText(3, QCoreApplication.translate("FilterSignalSettingsView", u"hamming", None))
        self.window_combobox.setItemText(4, QCoreApplication.translate("FilterSignalSettingsView", u"hann", None))
        self.window_combobox.setItemText(5, QCoreApplication.translate("FilterSignalSettingsView", u"bartlett", None))
        self.window_combobox.setItemText(6, QCoreApplication.translate("FilterSignalSettingsView", u"flattop", None))
        self.window_combobox.setItemText(7, QCoreApplication.translate("FilterSignalSettingsView", u"parzen", None))
        self.window_combobox.setItemText(8, QCoreApplication.translate("FilterSignalSettingsView", u"bohman", None))
        self.window_combobox.setItemText(9, QCoreApplication.translate("FilterSignalSettingsView", u"blackmanharris", None))
        self.window_combobox.setItemText(10, QCoreApplication.translate("FilterSignalSettingsView", u"nuttall", None))
        self.window_combobox.setItemText(11, QCoreApplication.translate("FilterSignalSettingsView", u"barthann", None))
        self.window_combobox.setItemText(12, QCoreApplication.translate("FilterSignalSettingsView", u"kaiser", None))
        self.window_combobox.setItemText(13, QCoreApplication.translate("FilterSignalSettingsView", u"gaussian", None))
        self.window_combobox.setItemText(14, QCoreApplication.translate("FilterSignalSettingsView", u"general_gaussian", None))
        self.window_combobox.setItemText(15, QCoreApplication.translate("FilterSignalSettingsView", u"dpss", None))
        self.window_combobox.setItemText(16, QCoreApplication.translate("FilterSignalSettingsView", u"chebwin", None))
        self.window_combobox.setItemText(17, QCoreApplication.translate("FilterSignalSettingsView", u"exponential", None))
        self.window_combobox.setItemText(18, QCoreApplication.translate("FilterSignalSettingsView", u"tukey", None))
        self.window_combobox.setItemText(19, QCoreApplication.translate("FilterSignalSettingsView", u"taylor", None))

        self.window_combobox.setCurrentText(QCoreApplication.translate("FilterSignalSettingsView", u"hamming", None))
#if QT_CONFIG(tooltip)
        self.sleep_std_radiobutton.setToolTip(QCoreApplication.translate("FilterSignalSettingsView", u"The standard in sleep medicine is to use an order equals to: 5*sample_rate/lower_frequency", None))
#endif // QT_CONFIG(tooltip)
        self.sleep_std_radiobutton.setText(QCoreApplication.translate("FilterSignalSettingsView", u"Sleep standard", None))
        self.custom_radiobutton.setText(QCoreApplication.translate("FilterSignalSettingsView", u"Custom", None))
        self.custom_order_lineedit.setText(QCoreApplication.translate("FilterSignalSettingsView", u"101", None))
        self.label_3.setText(QCoreApplication.translate("FilterSignalSettingsView", u"Window", None))
        self.label_7.setText(QCoreApplication.translate("FilterSignalSettingsView", u"(Only used for the visualisation)", None))
        self.label_6.setText(QCoreApplication.translate("FilterSignalSettingsView", u"Sample Rate", None))
        self.sample_rate_lineedit.setText(QCoreApplication.translate("FilterSignalSettingsView", u"256", None))
    # retranslateUi

