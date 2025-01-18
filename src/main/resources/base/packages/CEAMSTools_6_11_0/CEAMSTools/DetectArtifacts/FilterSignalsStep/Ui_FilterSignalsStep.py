# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_FilterSignalsStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_FilterSignalsStep(object):
    def setupUi(self, FilterSignalsStep):
        if not FilterSignalsStep.objectName():
            FilterSignalsStep.setObjectName(u"FilterSignalsStep")
        FilterSignalsStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        FilterSignalsStep.resize(680, 343)
        self.horizontalLayout = QHBoxLayout(FilterSignalsStep)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(FilterSignalsStep)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setFrameShape(QFrame.HLine)
        self.textBrowser.setFrameShadow(QFrame.Plain)
        self.textBrowser.setLineWidth(0)

        self.verticalLayout.addWidget(self.textBrowser)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.notch_checkBox = QCheckBox(FilterSignalsStep)
        self.notch_checkBox.setObjectName(u"notch_checkBox")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.notch_checkBox.setFont(font)

        self.gridLayout.addWidget(self.notch_checkBox, 0, 3, 1, 1)

        self.radioButton_50Hz = QRadioButton(FilterSignalsStep)
        self.radioButton_50Hz.setObjectName(u"radioButton_50Hz")
        self.radioButton_50Hz.setEnabled(False)

        self.gridLayout.addWidget(self.radioButton_50Hz, 2, 3, 1, 1)

        self.label = QLabel(FilterSignalsStep)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 0))

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.low_cutoff_lineEdit = QLineEdit(FilterSignalsStep)
        self.low_cutoff_lineEdit.setObjectName(u"low_cutoff_lineEdit")
        self.low_cutoff_lineEdit.setMaximumSize(QSize(110, 16777215))

        self.gridLayout.addWidget(self.low_cutoff_lineEdit, 1, 1, 1, 1)

        self.label_6 = QLabel(FilterSignalsStep)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(80, 0))

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.bp_checkBox = QCheckBox(FilterSignalsStep)
        self.bp_checkBox.setObjectName(u"bp_checkBox")
        self.bp_checkBox.setEnabled(False)
        self.bp_checkBox.setFont(font)
        self.bp_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.bp_checkBox, 0, 0, 1, 2)

        self.high_cutoff_lineEdit = QLineEdit(FilterSignalsStep)
        self.high_cutoff_lineEdit.setObjectName(u"high_cutoff_lineEdit")
        self.high_cutoff_lineEdit.setMaximumSize(QSize(110, 16777215))

        self.gridLayout.addWidget(self.high_cutoff_lineEdit, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.radioButton_60Hz = QRadioButton(FilterSignalsStep)
        self.radioButton_60Hz.setObjectName(u"radioButton_60Hz")
        self.radioButton_60Hz.setEnabled(False)

        self.gridLayout.addWidget(self.radioButton_60Hz, 1, 3, 1, 1)

        self.label_2 = QLabel(FilterSignalsStep)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 52, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(FilterSignalsStep)
        self.bp_checkBox.clicked.connect(FilterSignalsStep.update_filter_settings)
        self.notch_checkBox.clicked.connect(FilterSignalsStep.update_filter_settings)
        self.radioButton_50Hz.clicked.connect(FilterSignalsStep.update_filter_settings)
        self.radioButton_60Hz.clicked.connect(FilterSignalsStep.update_filter_settings)
        self.high_cutoff_lineEdit.editingFinished.connect(FilterSignalsStep.update_high_cutoff_slot)
        self.low_cutoff_lineEdit.editingFinished.connect(FilterSignalsStep.update_low_cutoff_slot)

        QMetaObject.connectSlotsByName(FilterSignalsStep)
    # setupUi

    def retranslateUi(self, FilterSignalsStep):
        FilterSignalsStep.setWindowTitle("")
#if QT_CONFIG(tooltip)
        FilterSignalsStep.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.textBrowser.setHtml(QCoreApplication.translate("FilterSignalsStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt\">The EEG signals are downsampled to 256 Hz (if the sampling rate is above 256 Hz) to reduce the processing time.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt\">Note that very high frequency noise &gt; 128 Hz will not be detected as"
                        " artifact since a 128 Hz low pass filter is applied before downsampling.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt text-decoration: underline;\">Warning</span><span style=\" font-size:12pt\"> : The high cutoff of the bandpass filter can not be higher than the signal sampling rate / 2.  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt\">               I.e. 128 Hz for a sampling rate of 256 Hz.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt\"><br /></p></body></html>", None))
        self.notch_checkBox.setText(QCoreApplication.translate("FilterSignalsStep", u"Power line notch filter", None))
        self.radioButton_50Hz.setText(QCoreApplication.translate("FilterSignalsStep", u"50 Hz", None))
        self.label.setText(QCoreApplication.translate("FilterSignalsStep", u"Low cutoff", None))
#if QT_CONFIG(tooltip)
        self.low_cutoff_lineEdit.setToolTip(QCoreApplication.translate("FilterSignalsStep", u"Edit the low cutoff frequency in Hz (i.e. 0.3).", None))
#endif // QT_CONFIG(tooltip)
        self.low_cutoff_lineEdit.setText(QCoreApplication.translate("FilterSignalsStep", u"0", None))
        self.label_6.setText(QCoreApplication.translate("FilterSignalsStep", u"High cutoff", None))
        self.bp_checkBox.setText(QCoreApplication.translate("FilterSignalsStep", u"Bandpass filter", None))
#if QT_CONFIG(tooltip)
        self.high_cutoff_lineEdit.setToolTip(QCoreApplication.translate("FilterSignalsStep", u"Edit the high cutoff frequency in Hz (i.e. 100).", None))
#endif // QT_CONFIG(tooltip)
        self.high_cutoff_lineEdit.setText(QCoreApplication.translate("FilterSignalsStep", u"100", None))
        self.radioButton_60Hz.setText(QCoreApplication.translate("FilterSignalsStep", u"60 Hz", None))
        self.label_2.setText(QCoreApplication.translate("FilterSignalsStep", u"* if activated, the power line contamination will be desactivated", None))
    # retranslateUi

