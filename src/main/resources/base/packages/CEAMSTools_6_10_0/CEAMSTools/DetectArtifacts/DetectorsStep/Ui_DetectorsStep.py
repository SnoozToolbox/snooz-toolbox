# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DetectorsStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_DetectorsStep(object):
    def setupUi(self, DetectorsStep):
        if not DetectorsStep.objectName():
            DetectorsStep.setObjectName(u"DetectorsStep")
        DetectorsStep.resize(722, 663)
        DetectorsStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_5 = QVBoxLayout(DetectorsStep)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(DetectorsStep)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)

        self.verticalLayout_5.addWidget(self.label_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.common_radioButton = QRadioButton(DetectorsStep)
        self.buttonGroup = QButtonGroup(DetectorsStep)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.common_radioButton)
        self.common_radioButton.setObjectName(u"common_radioButton")
        self.common_radioButton.setMinimumSize(QSize(230, 0))
        self.common_radioButton.setMaximumSize(QSize(230, 16777215))
        self.common_radioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.common_radioButton)

        self.label_4 = QLabel(DetectorsStep)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.unique_group_lineEdit = QLineEdit(DetectorsStep)
        self.unique_group_lineEdit.setObjectName(u"unique_group_lineEdit")
        self.unique_group_lineEdit.setMinimumSize(QSize(150, 0))
        self.unique_group_lineEdit.setMaximumSize(QSize(150, 16777215))
        self.unique_group_lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.unique_group_lineEdit)

        self.label_5 = QLabel(DetectorsStep)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.unique_name_lineEdit = QLineEdit(DetectorsStep)
        self.unique_name_lineEdit.setObjectName(u"unique_name_lineEdit")
        self.unique_name_lineEdit.setMinimumSize(QSize(150, 0))
        self.unique_name_lineEdit.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.unique_name_lineEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.specific_radioButton = QRadioButton(DetectorsStep)
        self.buttonGroup.addButton(self.specific_radioButton)
        self.specific_radioButton.setObjectName(u"specific_radioButton")
        self.specific_radioButton.setMinimumSize(QSize(230, 0))
        self.specific_radioButton.setMaximumSize(QSize(230, 16777215))

        self.horizontalLayout_3.addWidget(self.specific_radioButton)

        self.specific_name_label = QLabel(DetectorsStep)
        self.specific_name_label.setObjectName(u"specific_name_label")
        self.specific_name_label.setEnabled(False)
        self.specific_name_label.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.specific_name_label)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_6 = QLabel(DetectorsStep)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_2 = QLabel(DetectorsStep)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.flatline_checkBox = QCheckBox(DetectorsStep)
        self.flatline_checkBox.setObjectName(u"flatline_checkBox")
        self.flatline_checkBox.setChecked(False)

        self.verticalLayout_2.addWidget(self.flatline_checkBox)

        self.highfreq_checkBox = QCheckBox(DetectorsStep)
        self.highfreq_checkBox.setObjectName(u"highfreq_checkBox")
        self.highfreq_checkBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.highfreq_checkBox)

        self.persistent_checkBox = QCheckBox(DetectorsStep)
        self.persistent_checkBox.setObjectName(u"persistent_checkBox")
        self.persistent_checkBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.persistent_checkBox)

        self.powerline_checkBox = QCheckBox(DetectorsStep)
        self.powerline_checkBox.setObjectName(u"powerline_checkBox")
        self.powerline_checkBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.powerline_checkBox)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.label = QLabel(DetectorsStep)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_5.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.radioButton_60Hz = QRadioButton(DetectorsStep)
        self.buttonGroup_2 = QButtonGroup(DetectorsStep)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_60Hz)
        self.radioButton_60Hz.setObjectName(u"radioButton_60Hz")
        self.radioButton_60Hz.setMaximumSize(QSize(150, 16777215))
        self.radioButton_60Hz.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_60Hz)

        self.radioButton_50Hz = QRadioButton(DetectorsStep)
        self.buttonGroup_2.addButton(self.radioButton_50Hz)
        self.radioButton_50Hz.setObjectName(u"radioButton_50Hz")
        self.radioButton_50Hz.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout.addWidget(self.radioButton_50Hz)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.bslvar_checkBox = QCheckBox(DetectorsStep)
        self.bslvar_checkBox.setObjectName(u"bslvar_checkBox")
        self.bslvar_checkBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.bslvar_checkBox)

        self.muscle_checkBox = QCheckBox(DetectorsStep)
        self.muscle_checkBox.setObjectName(u"muscle_checkBox")
        self.muscle_checkBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.muscle_checkBox)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.textEdit = QTextEdit(DetectorsStep)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setMaximumSize(QSize(16777215, 268))
        self.textEdit.setFrameShape(QFrame.VLine)
        self.textEdit.setLineWidth(0)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.textEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(DetectorsStep)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(DetectorsStep)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_1 = QCheckBox(DetectorsStep)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_1, 0, 0, 1, 1)

        self.checkBox_2 = QCheckBox(DetectorsStep)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 2)

        self.checkBox_3 = QCheckBox(DetectorsStep)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_3, 0, 3, 1, 1)

        self.checkBox_5 = QCheckBox(DetectorsStep)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_5, 0, 4, 1, 1)

        self.checkBox_9 = QCheckBox(DetectorsStep)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout.addWidget(self.checkBox_9, 1, 0, 1, 2)

        self.checkBox_0 = QCheckBox(DetectorsStep)
        self.checkBox_0.setObjectName(u"checkBox_0")

        self.gridLayout.addWidget(self.checkBox_0, 1, 2, 1, 2)


        self.horizontalLayout_4.addLayout(self.gridLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)


        self.retranslateUi(DetectorsStep)
        self.radioButton_50Hz.clicked.connect(DetectorsStep.update_settings_slot)
        self.radioButton_60Hz.clicked.connect(DetectorsStep.update_settings_slot)
        self.powerline_checkBox.clicked.connect(DetectorsStep.update_settings_slot)
        self.common_radioButton.clicked.connect(DetectorsStep.update_event_label_slot)
        self.specific_radioButton.clicked.connect(DetectorsStep.update_event_label_slot)
        self.unique_group_lineEdit.editingFinished.connect(DetectorsStep.update_event_label_slot)
        self.unique_name_lineEdit.editingFinished.connect(DetectorsStep.update_event_label_slot)
        self.checkBox_0.clicked.connect(DetectorsStep.update_stages_slot)
        self.checkBox_1.clicked.connect(DetectorsStep.update_stages_slot)
        self.checkBox_2.clicked.connect(DetectorsStep.update_stages_slot)
        self.checkBox_3.clicked.connect(DetectorsStep.update_stages_slot)
        self.checkBox_5.clicked.connect(DetectorsStep.update_stages_slot)

        QMetaObject.connectSlotsByName(DetectorsStep)
    # setupUi

    def retranslateUi(self, DetectorsStep):
        DetectorsStep.setWindowTitle("")
        self.label_3.setText(QCoreApplication.translate("DetectorsStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Artifact Event Labels</span></p></body></html>", None))
        self.common_radioButton.setText(QCoreApplication.translate("DetectorsStep", u"Common to all the detectors", None))
        self.label_4.setText(QCoreApplication.translate("DetectorsStep", u"Group", None))
#if QT_CONFIG(tooltip)
        self.unique_group_lineEdit.setToolTip(QCoreApplication.translate("DetectorsStep", u"Write the common artifact event name to use for all the detectors.", None))
#endif // QT_CONFIG(tooltip)
        self.unique_group_lineEdit.setText(QCoreApplication.translate("DetectorsStep", u"art_snooz", None))
        self.label_5.setText(QCoreApplication.translate("DetectorsStep", u"Name", None))
        self.unique_name_lineEdit.setText(QCoreApplication.translate("DetectorsStep", u"art_snooz", None))
        self.specific_radioButton.setText(QCoreApplication.translate("DetectorsStep", u"Specific to each detector", None))
        self.specific_name_label.setText(QCoreApplication.translate("DetectorsStep", u"Group and name are defined in the settings page of each detector.", None))
        self.label_6.setText(QCoreApplication.translate("DetectorsStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Artifact Detectors</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("DetectorsStep", u"Check the artifact detectors to run:", None))
        self.flatline_checkBox.setText(QCoreApplication.translate("DetectorsStep", u"Flatline : Segments of low power, flatlined signal.", None))
        self.highfreq_checkBox.setText(QCoreApplication.translate("DetectorsStep", u"High Frequency burst : Segments with a burst of high frequency power (>25 Hz).", None))
        self.persistent_checkBox.setText(QCoreApplication.translate("DetectorsStep", u"Persistent Noise : Segments with high frequency noise (>25 Hz).", None))
        self.powerline_checkBox.setText(QCoreApplication.translate("DetectorsStep", u"Power Line Contamination : Segments corrupted by 50 or 60 Hz power.", None))
        self.label.setText(QCoreApplication.translate("DetectorsStep", u"Power line contamination is turned off when a notch filter is applied", None))
        self.radioButton_60Hz.setText(QCoreApplication.translate("DetectorsStep", u"60 Hz", None))
        self.radioButton_50Hz.setText(QCoreApplication.translate("DetectorsStep", u"50 Hz", None))
        self.bslvar_checkBox.setText(QCoreApplication.translate("DetectorsStep", u"Baseline Variation (Breathing, Sweat) : Segments with high power in the low frequency band (<0.4 Hz).", None))
        self.muscle_checkBox.setText(QCoreApplication.translate("DetectorsStep", u"Muscle Artifact : Segments with burst of activity in the frequency band 20.25-32 Hz.", None))
        self.textEdit.setHtml(QCoreApplication.translate("DetectorsStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The thresholds of each detector can be modified in the &quot;Detectors Settings&quot; configuration pages.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    To make a detector more precise : </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
                        "\">        - Flatline detector : decrease the threshold</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        - All other detectors : increase the thresholds</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        - You could start by increasing the fixed thresholds based on the main gaussian distrbution.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">          I.e. increase the thresholds from 4 X STD to 5 X STD.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    To make a detector more sensitive : </p>\n"
"<p style=\" margin-top"
                        ":0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        - Flatline detector : increase the threshold</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        - All other detectors : decrease the thresholds</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        - You could start by decreasing the fixed thresholds based on the main gaussian distrbution.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">          I.e. decrease the thresholds from 4 X STD to 3 X STD, except for the baseline variation which the minimum value should be 3.5.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:"
                        "0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For more information see the  &quot;Detectors Settings&quot; configuration page for each specific detector. </p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("DetectorsStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep Stage Selection</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("DetectorsStep", u"Artifact detection is performed on the entire recording.\n"
"However, you can select specific sleep stages to potentially establish a cleaner baseline\n"
"for the set of algorithms that use a 3-component Gaussian Mixture Model (GMM).", None))
        self.checkBox_1.setText(QCoreApplication.translate("DetectorsStep", u"N1", None))
        self.checkBox_2.setText(QCoreApplication.translate("DetectorsStep", u"N2", None))
        self.checkBox_3.setText(QCoreApplication.translate("DetectorsStep", u"N3", None))
        self.checkBox_5.setText(QCoreApplication.translate("DetectorsStep", u"R", None))
        self.checkBox_9.setText(QCoreApplication.translate("DetectorsStep", u"Unscored", None))
        self.checkBox_0.setText(QCoreApplication.translate("DetectorsStep", u"Awake", None))
    # retranslateUi

