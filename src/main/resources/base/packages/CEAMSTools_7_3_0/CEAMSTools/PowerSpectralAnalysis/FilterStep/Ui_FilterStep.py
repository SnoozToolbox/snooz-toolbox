# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_FilterStep.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QRadioButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
import themes_rc

class Ui_FilterStep(object):
    def setupUi(self, FilterStep):
        if not FilterStep.objectName():
            FilterStep.setObjectName(u"FilterStep")
        FilterStep.resize(813, 565)
        self.verticalLayout = QVBoxLayout(FilterStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(FilterStep)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 22))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.textBrowser = QTextEdit(FilterStep)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(0, 380))
        self.textBrowser.setMaximumSize(QSize(16777215, 500))
        self.textBrowser.setFrameShape(QFrame.Shape.NoFrame)
        self.textBrowser.setFrameShadow(QFrame.Shadow.Plain)
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.textBrowser)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.bp_checkBox = QCheckBox(FilterStep)
        self.bp_checkBox.setObjectName(u"bp_checkBox")
        self.bp_checkBox.setFont(font)
        self.bp_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.bp_checkBox, 0, 0, 1, 2)

        self.notch_checkBox = QCheckBox(FilterStep)
        self.notch_checkBox.setObjectName(u"notch_checkBox")
        self.notch_checkBox.setFont(font)

        self.gridLayout.addWidget(self.notch_checkBox, 0, 3, 1, 1)

        self.label = QLabel(FilterStep)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 0))
        self.label.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.low_cutoff_lineEdit = QLineEdit(FilterStep)
        self.low_cutoff_lineEdit.setObjectName(u"low_cutoff_lineEdit")
        self.low_cutoff_lineEdit.setMaximumSize(QSize(110, 16777215))

        self.gridLayout.addWidget(self.low_cutoff_lineEdit, 1, 1, 1, 1)

        self.radioButton_60Hz = QRadioButton(FilterStep)
        self.radioButton_60Hz.setObjectName(u"radioButton_60Hz")
        self.radioButton_60Hz.setEnabled(False)

        self.gridLayout.addWidget(self.radioButton_60Hz, 1, 3, 1, 1)

        self.label_6 = QLabel(FilterStep)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(80, 0))
        self.label_6.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.high_cutoff_lineEdit = QLineEdit(FilterStep)
        self.high_cutoff_lineEdit.setObjectName(u"high_cutoff_lineEdit")
        self.high_cutoff_lineEdit.setMaximumSize(QSize(110, 16777215))

        self.gridLayout.addWidget(self.high_cutoff_lineEdit, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.radioButton_50Hz = QRadioButton(FilterStep)
        self.radioButton_50Hz.setObjectName(u"radioButton_50Hz")
        self.radioButton_50Hz.setEnabled(False)

        self.gridLayout.addWidget(self.radioButton_50Hz, 2, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(FilterStep)
        self.bp_checkBox.clicked.connect(FilterStep.update_filter_settings_slot)
        self.notch_checkBox.clicked.connect(FilterStep.update_filter_settings_slot)
        self.radioButton_50Hz.clicked.connect(FilterStep.update_filter_settings_slot)
        self.radioButton_60Hz.clicked.connect(FilterStep.update_filter_settings_slot)

        QMetaObject.connectSlotsByName(FilterStep)
    # setupUi

    def retranslateUi(self, FilterStep):
        FilterStep.setWindowTitle("")
        FilterStep.setStyleSheet(QCoreApplication.translate("FilterStep", u"font: 12pt \"Roboto\";", None))
        self.label_2.setText(QCoreApplication.translate("FilterStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Filtering</span></p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("FilterStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The user may optionally add a bandpass filter and a power-line notch filter, depending on signal quality and the research question.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">We recommend applying the same filters used during visual review.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px"
                        "; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Warning</span>: The highest cutoff frequency must be lower than <span style=\" font-weight:700;\">sample rate / 2</span>.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">PSG file not modified</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Filtering is applied only for detection; the original PSG signals remain unchanged.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left"
                        ":0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Filter Design</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The filter is a Butterworth design implemented in second-order-section (SOS) form and applied using bidirectional zero-phase filtering. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This approach preserves the requested magnitude response while eliminating phase distortion.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:"
                        "0px;\">   Bandpass filter parameters:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      - Type : IIR bandpass</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      - Order : 6 (internally halved before the forward/backward pass)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   Notch filter parameters:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      - Type : IIR stopband</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      - Order : 20 (intern"
                        "ally halved before the forward/backward pass)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.bp_checkBox.setText(QCoreApplication.translate("FilterStep", u"Bandpass filter", None))
        self.notch_checkBox.setText(QCoreApplication.translate("FilterStep", u"Power line notch filter", None))
        self.label.setText(QCoreApplication.translate("FilterStep", u"Low cutoff", None))
#if QT_CONFIG(tooltip)
        self.low_cutoff_lineEdit.setToolTip(QCoreApplication.translate("FilterStep", u"Edit the low cutoff frequency in Hz (i.e. 0.3).", None))
#endif // QT_CONFIG(tooltip)
        self.low_cutoff_lineEdit.setText(QCoreApplication.translate("FilterStep", u"0.3", None))
        self.radioButton_60Hz.setText(QCoreApplication.translate("FilterStep", u"60 Hz", None))
        self.label_6.setText(QCoreApplication.translate("FilterStep", u"High cutoff", None))
#if QT_CONFIG(tooltip)
        self.high_cutoff_lineEdit.setToolTip(QCoreApplication.translate("FilterStep", u"Edit the high cutoff frequency in Hz (i.e. 100).", None))
#endif // QT_CONFIG(tooltip)
        self.high_cutoff_lineEdit.setText(QCoreApplication.translate("FilterStep", u"100", None))
        self.radioButton_50Hz.setText(QCoreApplication.translate("FilterStep", u"50 Hz", None))
    # retranslateUi

