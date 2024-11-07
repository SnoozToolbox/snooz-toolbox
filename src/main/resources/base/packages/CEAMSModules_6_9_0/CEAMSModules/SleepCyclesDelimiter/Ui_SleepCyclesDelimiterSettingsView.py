# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SleepCyclesDelimiterSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from . import SleepCycleDelimiter_rs
import themes_rc

class Ui_SleepCyclesDelimiterSettingsView(object):
    def setupUi(self, SleepCyclesDelimiterSettingsView):
        if not SleepCyclesDelimiterSettingsView.objectName():
            SleepCyclesDelimiterSettingsView.setObjectName(u"SleepCyclesDelimiterSettingsView")
        SleepCyclesDelimiterSettingsView.resize(734, 812)
        SleepCyclesDelimiterSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout_2 = QHBoxLayout(SleepCyclesDelimiterSettingsView)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.splitter = QSplitter(SleepCyclesDelimiterSettingsView)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setHandleWidth(15)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetNoConstraint)
        self.textEdit = QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(330, 150))
        self.textEdit.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit.setStyleSheet(u"")
        self.textEdit.setFrameShape(QFrame.HLine)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.textEdit)

        self.textEdit_3 = QTextEdit(self.layoutWidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMinimumSize(QSize(330, 150))
        self.textEdit_3.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit_3.setStyleSheet(u"")
        self.textEdit_3.setFrameShape(QFrame.HLine)
        self.textEdit_3.setFrameShadow(QFrame.Plain)
        self.textEdit_3.setLineWidth(0)

        self.horizontalLayout_3.addWidget(self.textEdit_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(567, 0))
        self.label.setPixmap(QPixmap(u":/sleep_cycle_del/UI_v5_minimal.png"))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox_incl_SOREMP = QCheckBox(self.layoutWidget)
        self.checkBox_incl_SOREMP.setObjectName(u"checkBox_incl_SOREMP")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBox_incl_SOREMP.sizePolicy().hasHeightForWidth())
        self.checkBox_incl_SOREMP.setSizePolicy(sizePolicy1)
        self.checkBox_incl_SOREMP.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_incl_SOREMP.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_incl_SOREMP)

        self.checkBox_incl_last = QCheckBox(self.layoutWidget)
        self.checkBox_incl_last.setObjectName(u"checkBox_incl_last")
        sizePolicy1.setHeightForWidth(self.checkBox_incl_last.sizePolicy().hasHeightForWidth())
        self.checkBox_incl_last.setSizePolicy(sizePolicy1)
        self.checkBox_incl_last.setMinimumSize(QSize(0, 0))
        self.checkBox_incl_last.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.checkBox_incl_last)

        self.checkBox_incl_all = QCheckBox(self.layoutWidget)
        self.checkBox_incl_all.setObjectName(u"checkBox_incl_all")
        sizePolicy1.setHeightForWidth(self.checkBox_incl_all.sizePolicy().hasHeightForWidth())
        self.checkBox_incl_all.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.checkBox_incl_all)


        self.gridLayout.addLayout(self.verticalLayout_2, 3, 0, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.radioButton_Min = QRadioButton(self.layoutWidget)
        self.radioButton_Min.setObjectName(u"radioButton_Min")
        self.radioButton_Min.setMaximumSize(QSize(16777215, 18))
        self.radioButton_Min.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_Min)

        self.radioButton_Floyd = QRadioButton(self.layoutWidget)
        self.radioButton_Floyd.setObjectName(u"radioButton_Floyd")
        self.radioButton_Floyd.setMinimumSize(QSize(160, 0))
        self.radioButton_Floyd.setMaximumSize(QSize(350, 18))

        self.verticalLayout.addWidget(self.radioButton_Floyd)

        self.radioButton_Aesch = QRadioButton(self.layoutWidget)
        self.radioButton_Aesch.setObjectName(u"radioButton_Aesch")
        self.radioButton_Aesch.setMaximumSize(QSize(16777215, 18))

        self.verticalLayout.addWidget(self.radioButton_Aesch)

        self.radioButton_Mice = QRadioButton(self.layoutWidget)
        self.radioButton_Mice.setObjectName(u"radioButton_Mice")
        self.radioButton_Mice.setEnabled(False)
        self.radioButton_Mice.setMaximumSize(QSize(16777215, 18))

        self.verticalLayout.addWidget(self.radioButton_Mice)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.mv_end_checkBox = QCheckBox(self.layoutWidget)
        self.mv_end_checkBox.setObjectName(u"mv_end_checkBox")
        sizePolicy1.setHeightForWidth(self.mv_end_checkBox.sizePolicy().hasHeightForWidth())
        self.mv_end_checkBox.setSizePolicy(sizePolicy1)
        self.mv_end_checkBox.setStyleSheet(u"")
        self.mv_end_checkBox.setCheckable(True)

        self.verticalLayout_5.addWidget(self.mv_end_checkBox)

        self.plainTextEdit = QPlainTextEdit(self.layoutWidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_5.addWidget(self.plainTextEdit)


        self.gridLayout.addLayout(self.verticalLayout_5, 3, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMinimumSize(QSize(0, 0))
        self.label_9.setMaximumSize(QSize(16777215, 18))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.minL_REM_first_lineEdit = QLineEdit(self.layoutWidget)
        self.minL_REM_first_lineEdit.setObjectName(u"minL_REM_first_lineEdit")
        self.minL_REM_first_lineEdit.setEnabled(True)
        self.minL_REM_first_lineEdit.setMaximumSize(QSize(75, 16777215))
        self.minL_REM_first_lineEdit.setStyleSheet(u"")
        self.minL_REM_first_lineEdit.setReadOnly(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.minL_REM_first_lineEdit)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMinimumSize(QSize(0, 0))
        self.label_8.setMaximumSize(QSize(16777215, 18))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.minL_REM_mid_lineEdit = QLineEdit(self.layoutWidget)
        self.minL_REM_mid_lineEdit.setObjectName(u"minL_REM_mid_lineEdit")
        self.minL_REM_mid_lineEdit.setEnabled(True)
        self.minL_REM_mid_lineEdit.setMaximumSize(QSize(75, 16777215))
        self.minL_REM_mid_lineEdit.setStyleSheet(u"")
        self.minL_REM_mid_lineEdit.setReadOnly(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.minL_REM_mid_lineEdit)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setMaximumSize(QSize(16777215, 18))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.minL_REM_last_lineEdit = QLineEdit(self.layoutWidget)
        self.minL_REM_last_lineEdit.setObjectName(u"minL_REM_last_lineEdit")
        self.minL_REM_last_lineEdit.setEnabled(True)
        self.minL_REM_last_lineEdit.setMaximumSize(QSize(75, 16777215))
        self.minL_REM_last_lineEdit.setStyleSheet(u"")
        self.minL_REM_last_lineEdit.setReadOnly(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.minL_REM_last_lineEdit)


        self.horizontalLayout.addLayout(self.formLayout)

        self.textEdit_4 = QTextEdit(self.layoutWidget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMaximumSize(QSize(16777215, 125))
        self.textEdit_4.setStyleSheet(u"")
        self.textEdit_4.setFrameShape(QFrame.HLine)
        self.textEdit_4.setFrameShadow(QFrame.Plain)
        self.textEdit_4.setLineWidth(0)

        self.horizontalLayout.addWidget(self.textEdit_4)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.layoutWidget1)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy1.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy1)
        self.textBrowser.setStyleSheet(u"")
        self.textBrowser.setFrameShape(QFrame.HLine)
        self.textBrowser.setFrameShadow(QFrame.Plain)
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setOpenLinks(True)

        self.verticalLayout_4.addWidget(self.textBrowser)

        self.splitter.addWidget(self.layoutWidget1)

        self.horizontalLayout_2.addWidget(self.splitter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.retranslateUi(SleepCyclesDelimiterSettingsView)
        self.radioButton_Aesch.clicked.connect(SleepCyclesDelimiterSettingsView.on_options_changed)
        self.radioButton_Min.clicked.connect(SleepCyclesDelimiterSettingsView.on_options_changed)
        self.radioButton_Floyd.clicked.connect(SleepCyclesDelimiterSettingsView.on_options_changed)
        self.radioButton_Mice.clicked.connect(SleepCyclesDelimiterSettingsView.on_options_changed)
        self.checkBox_incl_all.clicked.connect(SleepCyclesDelimiterSettingsView.include_incomplete_cycle_slot)
        self.checkBox_incl_SOREMP.clicked.connect(SleepCyclesDelimiterSettingsView.include_SOREMP_slot)
        self.checkBox_incl_last.clicked.connect(SleepCyclesDelimiterSettingsView.include_last_incomplete_slot)

        QMetaObject.connectSlotsByName(SleepCyclesDelimiterSettingsView)
    # setupUi

    def retranslateUi(self, SleepCyclesDelimiterSettingsView):
        SleepCyclesDelimiterSettingsView.setWindowTitle(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep Cycles Definition</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NREM Period (NREMP):</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">First NREMP : begins at the first NREM stage of the recording.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Central NREMPs : begin at the next NREM stage following a REMP end.</li>\n"
"<li style=\" margin-top:0px; margin-bot"
                        "tom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The NREMP ends at the start of a REMP.</li></ul></body></html>", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">REM Period (REMP):</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The REMP ends when there are 15 min without an R stage (except at the last cycle).</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The end is defined as the last R stage of the REMP or the beginning of the next NREMP.</li>\n"
"<l"
                        "i style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The REMP begins at the first stage R.</li></ul></body></html>", None))
        self.label.setText("")
#if QT_CONFIG(tooltip)
        self.checkBox_incl_SOREMP.setToolTip(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Check to include incomplete cycle because of SOREMP (Sleep Onset in REMP).", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_incl_SOREMP.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Include SOREMP", None))
#if QT_CONFIG(tooltip)
        self.checkBox_incl_last.setToolTip(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Check to include the last cycle even if incomplete.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_incl_last.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Include incomplete ending", None))
#if QT_CONFIG(tooltip)
        self.checkBox_incl_all.setToolTip(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Check to include any incomplete cycles even middle sleep cycles.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_incl_all.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Include all", None))
        self.label_6.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">End of the REMP</span></p></body></html>", None))
        self.radioButton_Min.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Minimum Criteria", None))
        self.radioButton_Floyd.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Feinberg et Floyd 1979", None))
        self.radioButton_Aesch.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Aeschbach 1993", None))
        self.radioButton_Mice.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Mice Criteria", None))
        self.label_4.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">Minimum Duration for REM Periods (min)</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">Period Duration Criteria</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">Incomplete cycles</span></p></body></html>", None))
        self.mv_end_checkBox.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Move the end of the REMP to avoid a \"gap\" between cycles", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Check this option to indicate that the end of the REM period must be at the start of the following NREM period, eliminating this temporal \"gap\" between 2 cycles.", None))
        self.label_9.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"First Cycle", None))
        self.minL_REM_first_lineEdit.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"0", None))
        self.label_8.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Middle Cycles", None))
        self.minL_REM_mid_lineEdit.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"0", None))
        self.label_7.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Last Cycle", None))
        self.minL_REM_last_lineEdit.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"0", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A REMP is joined to the preceding one if it does not meet the minimum REMP duration.</p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

