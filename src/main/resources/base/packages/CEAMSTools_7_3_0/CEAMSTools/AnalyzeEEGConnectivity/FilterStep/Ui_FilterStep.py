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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QLabel, QRadioButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_FilterStep(object):
    def setupUi(self, FilterStep):
        if not FilterStep.objectName():
            FilterStep.setObjectName(u"FilterStep")
        FilterStep.resize(904, 728)
        FilterStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_5 = QVBoxLayout(FilterStep)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(FilterStep)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_4.setFont(font)

        self.verticalLayout_2.addWidget(self.label_4)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.fullband_radioButton = QRadioButton(self.frame)
        self.buttonGroup_freq = QButtonGroup(FilterStep)
        self.buttonGroup_freq.setObjectName(u"buttonGroup_freq")
        self.buttonGroup_freq.addButton(self.fullband_radioButton)
        self.fullband_radioButton.setObjectName(u"fullband_radioButton")
        self.fullband_radioButton.setChecked(True)

        self.verticalLayout_2.addWidget(self.fullband_radioButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.delta_radioButton = QRadioButton(self.frame)
        self.buttonGroup_freq.addButton(self.delta_radioButton)
        self.delta_radioButton.setObjectName(u"delta_radioButton")

        self.horizontalLayout.addWidget(self.delta_radioButton)

        self.theta_radioButton = QRadioButton(self.frame)
        self.buttonGroup_freq.addButton(self.theta_radioButton)
        self.theta_radioButton.setObjectName(u"theta_radioButton")

        self.horizontalLayout.addWidget(self.theta_radioButton)

        self.alpha_radioButton = QRadioButton(self.frame)
        self.buttonGroup_freq.addButton(self.alpha_radioButton)
        self.alpha_radioButton.setObjectName(u"alpha_radioButton")

        self.horizontalLayout.addWidget(self.alpha_radioButton)

        self.beta_radioButton = QRadioButton(self.frame)
        self.buttonGroup_freq.addButton(self.beta_radioButton)
        self.beta_radioButton.setObjectName(u"beta_radioButton")

        self.horizontalLayout.addWidget(self.beta_radioButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.custom_radioButton = QRadioButton(self.frame)
        self.buttonGroup_freq.addButton(self.custom_radioButton)
        self.custom_radioButton.setObjectName(u"custom_radioButton")

        self.horizontalLayout_5.addWidget(self.custom_radioButton)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.low_cutoff_label = QLabel(self.frame)
        self.low_cutoff_label.setObjectName(u"low_cutoff_label")
        self.low_cutoff_label.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.low_cutoff_label)

        self.lowcutoff_doubleSpinBox = QDoubleSpinBox(self.frame)
        self.lowcutoff_doubleSpinBox.setObjectName(u"lowcutoff_doubleSpinBox")
        self.lowcutoff_doubleSpinBox.setEnabled(False)
        self.lowcutoff_doubleSpinBox.setMinimum(0.100000000000000)
        self.lowcutoff_doubleSpinBox.setMaximum(40.000000000000000)

        self.horizontalLayout_3.addWidget(self.lowcutoff_doubleSpinBox)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.high_cutoff_label = QLabel(self.frame)
        self.high_cutoff_label.setObjectName(u"high_cutoff_label")
        self.high_cutoff_label.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.high_cutoff_label)

        self.highcutoff_doubleSpinBox = QDoubleSpinBox(self.frame)
        self.highcutoff_doubleSpinBox.setObjectName(u"highcutoff_doubleSpinBox")
        self.highcutoff_doubleSpinBox.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.highcutoff_doubleSpinBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(FilterStep)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.scopes_label = QLabel(self.frame_2)
        self.scopes_label.setObjectName(u"scopes_label")

        self.verticalLayout.addWidget(self.scopes_label)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.sleep_stages_radioButton = QRadioButton(self.frame_2)
        self.buttonGroup_scope = QButtonGroup(FilterStep)
        self.buttonGroup_scope.setObjectName(u"buttonGroup_scope")
        self.buttonGroup_scope.addButton(self.sleep_stages_radioButton)
        self.sleep_stages_radioButton.setObjectName(u"sleep_stages_radioButton")
        self.sleep_stages_radioButton.setChecked(True)

        self.horizontalLayout_10.addWidget(self.sleep_stages_radioButton)

        self.unscored_radioButton = QRadioButton(self.frame_2)
        self.buttonGroup_scope.addButton(self.unscored_radioButton)
        self.unscored_radioButton.setObjectName(u"unscored_radioButton")
        self.unscored_radioButton.setChecked(False)

        self.horizontalLayout_10.addWidget(self.unscored_radioButton)

        self.specific_annotations_radioButton = QRadioButton(self.frame_2)
        self.buttonGroup_scope.addButton(self.specific_annotations_radioButton)
        self.specific_annotations_radioButton.setObjectName(u"specific_annotations_radioButton")

        self.horizontalLayout_10.addWidget(self.specific_annotations_radioButton)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rem_checkBox = QCheckBox(self.frame_2)
        self.rem_checkBox.setObjectName(u"rem_checkBox")

        self.horizontalLayout_2.addWidget(self.rem_checkBox)

        self.n1_checkBox = QCheckBox(self.frame_2)
        self.n1_checkBox.setObjectName(u"n1_checkBox")

        self.horizontalLayout_2.addWidget(self.n1_checkBox)

        self.n2_checkBox = QCheckBox(self.frame_2)
        self.n2_checkBox.setObjectName(u"n2_checkBox")

        self.horizontalLayout_2.addWidget(self.n2_checkBox)

        self.n3_checkBox = QCheckBox(self.frame_2)
        self.n3_checkBox.setObjectName(u"n3_checkBox")
        self.n3_checkBox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.n3_checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.trim_checkBox = QCheckBox(self.frame_2)
        self.trim_checkBox.setObjectName(u"trim_checkBox")
        self.trim_checkBox.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.trim_checkBox)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.start_time_label = QLabel(self.frame_2)
        self.start_time_label.setObjectName(u"start_time_label")
        self.start_time_label.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.start_time_label)

        self.start_time_doubleSpinBox = QDoubleSpinBox(self.frame_2)
        self.start_time_doubleSpinBox.setObjectName(u"start_time_doubleSpinBox")
        self.start_time_doubleSpinBox.setEnabled(False)
        self.start_time_doubleSpinBox.setMaximum(1000000.000000000000000)
        self.start_time_doubleSpinBox.setSingleStep(10.000000000000000)

        self.horizontalLayout_8.addWidget(self.start_time_doubleSpinBox)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)

        self.duration_time_label = QLabel(self.frame_2)
        self.duration_time_label.setObjectName(u"duration_time_label")
        self.duration_time_label.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.duration_time_label)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.duration_time_doubleSpinBox = QDoubleSpinBox(self.frame_2)
        self.duration_time_doubleSpinBox.setObjectName(u"duration_time_doubleSpinBox")
        self.duration_time_doubleSpinBox.setEnabled(False)
        self.duration_time_doubleSpinBox.setMaximum(1000000.000000000000000)
        self.duration_time_doubleSpinBox.setSingleStep(10.000000000000000)
        self.duration_time_doubleSpinBox.setValue(300.000000000000000)

        self.horizontalLayout_9.addWidget(self.duration_time_doubleSpinBox)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_9)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.retranslateUi(FilterStep)

        QMetaObject.connectSlotsByName(FilterStep)
    # setupUi

    def retranslateUi(self, FilterStep):
        FilterStep.setWindowTitle("")
        self.label_4.setText(QCoreApplication.translate("FilterStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Frequency Band Selection</span><br/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("FilterStep", u"Select the frequency band that best matches your research objectives. \n"
"This step filters the EEG signal into one of the standard bands, allowing you to focus your analysis on specific brain oscillations:\n"
"", None))
        self.fullband_radioButton.setText(QCoreApplication.translate("FilterStep", u"Full Frequency Band (0.16\u201330 Hz)", None))
        self.delta_radioButton.setText(QCoreApplication.translate("FilterStep", u"Delta (0.16\u20134 Hz)", None))
        self.theta_radioButton.setText(QCoreApplication.translate("FilterStep", u"Theta (4\u20138 Hz)", None))
        self.alpha_radioButton.setText(QCoreApplication.translate("FilterStep", u"Alpha (8\u201313 Hz)", None))
        self.beta_radioButton.setText(QCoreApplication.translate("FilterStep", u"Beta (13\u201330 Hz)", None))
        self.custom_radioButton.setText(QCoreApplication.translate("FilterStep", u"Custom Frequency Band", None))
        self.low_cutoff_label.setText(QCoreApplication.translate("FilterStep", u"Low cutoff", None))
        self.high_cutoff_label.setText(QCoreApplication.translate("FilterStep", u"High cutoff", None))
        self.textEdit.setHtml(QCoreApplication.translate("FilterStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Filter Design</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The filter is a Butterworth design implemen"
                        "ted in second-order-section (SOS) form and applied using bidirectional zero-phase filtering. This approach preserves the requested magnitude response while eliminating phase distortion.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   Bandpass filter parameters:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      - Type : IIR bandpass</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      - Order : 6 (internally halved before the forward/backward pass)</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("FilterStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Recording Scope Selection</span><br/></p></body></html>", None))
        self.scopes_label.setText(QCoreApplication.translate("FilterStep", u"<html><head/><body><p>Select <span style=\" font-weight:700;\">Sleep Stages</span> to choose specific sleep stages for connectivity analysis.<br/>Select <span style=\" font-weight:700;\">Unscored</span> to analyze the entire recording or a selected time segment.<br/>Select <span style=\" font-weight:700;\">Specific Annotations</span> to perform the analysis based on event annotations.</p></body></html>", None))
        self.sleep_stages_radioButton.setText(QCoreApplication.translate("FilterStep", u"Sleep Stages", None))
        self.unscored_radioButton.setText(QCoreApplication.translate("FilterStep", u"Unscored", None))
        self.specific_annotations_radioButton.setText(QCoreApplication.translate("FilterStep", u"Specific Annotations (select on next step)", None))
        self.rem_checkBox.setText(QCoreApplication.translate("FilterStep", u"REM", None))
        self.n1_checkBox.setText(QCoreApplication.translate("FilterStep", u"N1", None))
        self.n2_checkBox.setText(QCoreApplication.translate("FilterStep", u"N2", None))
        self.n3_checkBox.setText(QCoreApplication.translate("FilterStep", u"N3", None))
        self.trim_checkBox.setText(QCoreApplication.translate("FilterStep", u"Trim Signal", None))
        self.start_time_label.setText(QCoreApplication.translate("FilterStep", u"Start time (s):", None))
        self.duration_time_label.setText(QCoreApplication.translate("FilterStep", u"Duration (s):", None))
    # retranslateUi

