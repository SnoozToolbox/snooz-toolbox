# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SleepStageSelStep.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QButtonGroup, QCheckBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QRadioButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_SleepStageSelStep(object):
    def setupUi(self, SleepStageSelStep):
        if not SleepStageSelStep.objectName():
            SleepStageSelStep.setObjectName(u"SleepStageSelStep")
        SleepStageSelStep.resize(812, 840)
        SleepStageSelStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(SleepStageSelStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(SleepStageSelStep)
        self.label_7.setObjectName(u"label_7")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_7)

        self.textEdit = QTextEdit(SleepStageSelStep)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit.setFrameShape(QFrame.Shape.Panel)
        self.textEdit.setLineWidth(0)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_1 = QCheckBox(SleepStageSelStep)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_1, 0, 0, 1, 1)

        self.checkBox_2 = QCheckBox(SleepStageSelStep)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 2)

        self.checkBox_3 = QCheckBox(SleepStageSelStep)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_3, 0, 3, 1, 1)

        self.checkBox_5 = QCheckBox(SleepStageSelStep)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_5, 0, 4, 1, 1)

        self.checkBox_9 = QCheckBox(SleepStageSelStep)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout.addWidget(self.checkBox_9, 1, 0, 1, 2)

        self.checkBox_0 = QCheckBox(SleepStageSelStep)
        self.checkBox_0.setObjectName(u"checkBox_0")

        self.gridLayout.addWidget(self.checkBox_0, 1, 2, 1, 2)


        self.horizontalLayout_4.addLayout(self.gridLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(SleepStageSelStep)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(SleepStageSelStep)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(SleepStageSelStep)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(SleepStageSelStep)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.radioButton_set1 = QRadioButton(SleepStageSelStep)
        self.Theshold_sets = QButtonGroup(SleepStageSelStep)
        self.Theshold_sets.setObjectName(u"Theshold_sets")
        self.Theshold_sets.addButton(self.radioButton_set1)
        self.radioButton_set1.setObjectName(u"radioButton_set1")
        self.radioButton_set1.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_set1)

        self.textEdit1 = QTextEdit(SleepStageSelStep)
        self.textEdit1.setObjectName(u"textEdit1")
        sizePolicy1.setHeightForWidth(self.textEdit1.sizePolicy().hasHeightForWidth())
        self.textEdit1.setSizePolicy(sizePolicy1)
        self.textEdit1.setMaximumSize(QSize(16777215, 160))
        self.textEdit1.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit1.setLineWidth(0)
        self.textEdit1.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.textEdit1.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit1)

        self.radioButton_set2 = QRadioButton(SleepStageSelStep)
        self.Theshold_sets.addButton(self.radioButton_set2)
        self.radioButton_set2.setObjectName(u"radioButton_set2")

        self.verticalLayout.addWidget(self.radioButton_set2)

        self.textEdit_2 = QTextEdit(SleepStageSelStep)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy1.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy1)
        self.textEdit_2.setMaximumSize(QSize(16777215, 160))
        self.textEdit_2.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit_2)

        self.label_2 = QLabel(SleepStageSelStep)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)


        self.retranslateUi(SleepStageSelStep)
        self.radioButton_set1.clicked.connect(SleepStageSelStep.radio_threshold_slot)
        self.radioButton_set2.clicked.connect(SleepStageSelStep.radio_threshold_slot)
        self.checkBox_0.clicked.connect(SleepStageSelStep.check_stages_slot)
        self.checkBox_1.clicked.connect(SleepStageSelStep.check_stages_slot)
        self.checkBox_2.clicked.connect(SleepStageSelStep.check_stages_slot)
        self.checkBox_3.clicked.connect(SleepStageSelStep.check_stages_slot)
        self.checkBox_5.clicked.connect(SleepStageSelStep.check_stages_slot)
        self.checkBox_9.clicked.connect(SleepStageSelStep.check_stages_slot)

        QMetaObject.connectSlotsByName(SleepStageSelStep)
    # setupUi

    def retranslateUi(self, SleepStageSelStep):
        SleepStageSelStep.setWindowTitle("")
        self.label_7.setText(QCoreApplication.translate("SleepStageSelStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep Stage Selection</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("SleepStageSelStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the sleep stages in which you want to detect artifacts.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Artifact detection performs better when similar slee"
                        "p stages are selected, as the power distribution can be modeled more accurately. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Some detectors use a 3-component Gaussian Mixture Model (GMM) to estimate the standard deviation of non-corrupted data, </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">which is then used to define the threshold value.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* We recommend running artifact detection separately for NREM, REM, and Awake stages.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* Make su"
                        "r to have different annotation group or name to avoid confusion.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please select &quot;Unscored&quot; if your data does not include sleep stages.</p></body></html>", None))
        self.checkBox_1.setText(QCoreApplication.translate("SleepStageSelStep", u"N1", None))
        self.checkBox_2.setText(QCoreApplication.translate("SleepStageSelStep", u"N2", None))
        self.checkBox_3.setText(QCoreApplication.translate("SleepStageSelStep", u"N3", None))
        self.checkBox_5.setText(QCoreApplication.translate("SleepStageSelStep", u"R", None))
        self.checkBox_9.setText(QCoreApplication.translate("SleepStageSelStep", u"Unscored", None))
        self.checkBox_0.setText(QCoreApplication.translate("SleepStageSelStep", u"Awake", None))
        self.label.setText(QCoreApplication.translate("SleepStageSelStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Default threshold values</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("SleepStageSelStep", u"Threshold values for the different algorithms can be edited in \"Step 5 \u2013 Detector Settings\".", None))
        self.label_4.setText(QCoreApplication.translate("SleepStageSelStep", u"However, two sets of default values are also available.", None))
        self.label_5.setText(QCoreApplication.translate("SleepStageSelStep", u"Clicking any of the radio buttons below will automatically apply the corresponding default values to all detectors.", None))
        self.radioButton_set1.setText(QCoreApplication.translate("SleepStageSelStep", u"Set 1 : is intended for NREM sleep stages and can also be used for Awake or Unscored stages.", None))
        self.textEdit1.setHtml(QCoreApplication.translate("SleepStageSelStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Default values for detection in NREM (Set 1)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:700;\">Flatline</span> : 		A=<span style=\" font-weight:700;\">0.25</span> \u00b5V<span style=\" vertical-align:super;\">2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px"
                        "; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:700;\">High Frequency Burst </span>: 	A=<span style=\" font-weight:700;\">4</span> STD; 		B=<span style=\" font-weight:700;\">8</span> BSL MED, 	C=<span style=\" font-weight:700;\">0.1</span> Ratio</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:700;\">Persistent Noise</span> : 		A=<span style=\" font-weight:700;\">4</span> STD; 		B=<span style=\" font-weight:700;\">0.1</span> Ratio</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:700;\">Power Line Contamination</span> : 	A=<span style=\" font-weight:700;\">0</span> STD; 		B=<span style=\" font-weight:700;\">0.1</span> Ratio</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> "
                        "   <span style=\" font-weight:700;\">Baseline Variation</span> : 	A=<span style=\" font-weight:700;\">4</span> STD</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:700;\">Muscular</span> : 		A=<span style=\" font-weight:700;\">8</span> BSL MED, 	B=<span style=\" font-weight:700;\">5 </span>BSL MED, 	C=<span style=\" font-weight:700;\">5</span> BSL MED</p></body></html>", None))
        self.radioButton_set2.setText(QCoreApplication.translate("SleepStageSelStep", u"Set 2 : is more sensitive and intended for REM sleep stages.", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("SleepStageSelStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The default values for detection in REM (Set 2)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:700;\">Flatline</span> : 		A=0.25 \u00b5V<span style=\" vertical-align:super;\">2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0"
                        "; text-indent:0px;\">    <span style=\" font-weight:700;\">High Frequency Burst</span> : 	A=<span style=\" font-weight:700; color:#ff0000;\">3</span> STD; 		B=<span style=\" font-weight:700; color:#ff0000;\">6</span> BSL MED, 	C=0.1 Ratio</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:700;\">Persistent Noise</span> : 		A=<span style=\" font-weight:700; color:#ff0000;\">2</span> STD; 		B=0.1 Ratio</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:700;\">Power Line Contamination</span> : 	A=0 STD; 		B=0.1 Ratio</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:700;\">Baseline Variation</span> : 	A=<span style=\" font-weight:700; color:#ff0000;\">2.5</span> STD</p>\n"
"<p style=\" margi"
                        "n-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:700;\">Muscular</span> : 		A=<span style=\" font-weight:700; color:#ff0000;\">4</span> BSL MED, 	B=<span style=\" font-weight:700; color:#ff0000;\">3</span> BSL MED, 	C=<span style=\" font-weight:700; color:#ff0000;\">3</span> BSL MED</p></body></html>", None))
        self.label_2.setText("")
    # retranslateUi

