# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EEGInspectorView.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)
import themes_rc

class Ui_EEGInspectorView(object):
    def setupUi(self, EEGInspectorView):
        if not EEGInspectorView.objectName():
            EEGInspectorView.setObjectName(u"EEGInspectorView")
        EEGInspectorView.resize(999, 726)
        EEGInspectorView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_3 = QVBoxLayout(EEGInspectorView)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.file_name_label1 = QLabel(EEGInspectorView)
        self.file_name_label1.setObjectName(u"file_name_label1")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.file_name_label1.setFont(font)

        self.verticalLayout_3.addWidget(self.file_name_label1)

        self.StackedWidget = QStackedWidget(EEGInspectorView)
        self.StackedWidget.setObjectName(u"StackedWidget")
        self.Page1 = QWidget()
        self.Page1.setObjectName(u"Page1")
        self.verticalLayout = QVBoxLayout(self.Page1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.Page1)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.desc_label11 = QLabel(self.Page1)
        self.desc_label11.setObjectName(u"desc_label11")
        self.desc_label11.setFont(font)

        self.verticalLayout.addWidget(self.desc_label11)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.edf_lineEdit = QLineEdit(self.Page1)
        self.edf_lineEdit.setObjectName(u"edf_lineEdit")
        self.edf_lineEdit.setFont(font)

        self.horizontalLayout_11.addWidget(self.edf_lineEdit)

        self.edf_pushButton = QPushButton(self.Page1)
        self.edf_pushButton.setObjectName(u"edf_pushButton")
        self.edf_pushButton.setFont(font)

        self.horizontalLayout_11.addWidget(self.edf_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.line_1 = QFrame(self.Page1)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setFrameShape(QFrame.Shape.HLine)
        self.line_1.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_1)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.figure_placeholder1 = QWidget(self.Page1)
        self.figure_placeholder1.setObjectName(u"figure_placeholder1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.figure_placeholder1.sizePolicy().hasHeightForWidth())
        self.figure_placeholder1.setSizePolicy(sizePolicy)
        self.figure_placeholder1.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.figure_placeholder1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.desc_label13 = QLabel(self.Page1)
        self.desc_label13.setObjectName(u"desc_label13")
        self.desc_label13.setFont(font)

        self.horizontalLayout_13.addWidget(self.desc_label13)

        self.NextButton1 = QPushButton(self.Page1)
        self.NextButton1.setObjectName(u"NextButton1")
        self.NextButton1.setEnabled(False)
        self.NextButton1.setFont(font)

        self.horizontalLayout_13.addWidget(self.NextButton1)

        self.SkipButton1 = QPushButton(self.Page1)
        self.SkipButton1.setObjectName(u"SkipButton1")
        self.SkipButton1.setEnabled(False)
        self.SkipButton1.setFont(font)

        self.horizontalLayout_13.addWidget(self.SkipButton1)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.StackedWidget.addWidget(self.Page1)
        self.Page2 = QWidget()
        self.Page2.setObjectName(u"Page2")
        self.verticalLayout_5 = QVBoxLayout(self.Page2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textEdit = QTextEdit(self.Page2)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setMaximumSize(QSize(16777215, 80))
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.textEdit)

        self.textEdit_3 = QTextEdit(self.Page2)
        self.textEdit_3.setObjectName(u"textEdit_3")
        sizePolicy1.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy1)
        self.textEdit_3.setMaximumSize(QSize(350, 80))
        self.textEdit_3.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_3.setReadOnly(True)

        self.horizontalLayout.addWidget(self.textEdit_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(self.Page2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)

        self.verticalSpacer_2 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.figure_placeholder2 = QWidget(self.Page2)
        self.figure_placeholder2.setObjectName(u"figure_placeholder2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.figure_placeholder2.sizePolicy().hasHeightForWidth())
        self.figure_placeholder2.setSizePolicy(sizePolicy2)
        self.figure_placeholder2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_5.addWidget(self.figure_placeholder2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.BackButton2 = QPushButton(self.Page2)
        self.BackButton2.setObjectName(u"BackButton2")
        self.BackButton2.setFont(font)

        self.horizontalLayout_2.addWidget(self.BackButton2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.desc_label22 = QLabel(self.Page2)
        self.desc_label22.setObjectName(u"desc_label22")
        self.desc_label22.setFont(font)

        self.horizontalLayout_2.addWidget(self.desc_label22)

        self.NextButton2 = QPushButton(self.Page2)
        self.NextButton2.setObjectName(u"NextButton2")
        self.NextButton2.setEnabled(True)
        self.NextButton2.setFont(font)

        self.horizontalLayout_2.addWidget(self.NextButton2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.StackedWidget.addWidget(self.Page2)
        self.Page3 = QWidget()
        self.Page3.setObjectName(u"Page3")
        self.verticalLayout_2 = QVBoxLayout(self.Page3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.textEdit_2 = QTextEdit(self.Page3)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy1.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy1)
        self.textEdit_2.setMaximumSize(QSize(16777215, 90))
        self.textEdit_2.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_2.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.textEdit_2)

        self.textEdit_4 = QTextEdit(self.Page3)
        self.textEdit_4.setObjectName(u"textEdit_4")
        sizePolicy1.setHeightForWidth(self.textEdit_4.sizePolicy().hasHeightForWidth())
        self.textEdit_4.setSizePolicy(sizePolicy1)
        self.textEdit_4.setMaximumSize(QSize(350, 90))
        self.textEdit_4.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_4.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.textEdit_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.line_3 = QFrame(self.Page3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.desc_label32 = QLabel(self.Page3)
        self.desc_label32.setObjectName(u"desc_label32")
        self.desc_label32.setFont(font)

        self.horizontalLayout_31.addWidget(self.desc_label32)

        self.Epoch_len_comboBox = QComboBox(self.Page3)
        self.Epoch_len_comboBox.addItem("")
        self.Epoch_len_comboBox.addItem("")
        self.Epoch_len_comboBox.setObjectName(u"Epoch_len_comboBox")
        self.Epoch_len_comboBox.setFont(font)

        self.horizontalLayout_31.addWidget(self.Epoch_len_comboBox)

        self.ApplyButton = QPushButton(self.Page3)
        self.ApplyButton.setObjectName(u"ApplyButton")
        self.ApplyButton.setFont(font)

        self.horizontalLayout_31.addWidget(self.ApplyButton)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_31)


        self.verticalLayout_2.addLayout(self.horizontalLayout_31)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.figure_placeholder3 = QWidget(self.Page3)
        self.figure_placeholder3.setObjectName(u"figure_placeholder3")
        sizePolicy.setHeightForWidth(self.figure_placeholder3.sizePolicy().hasHeightForWidth())
        self.figure_placeholder3.setSizePolicy(sizePolicy)
        self.figure_placeholder3.setMinimumSize(QSize(0, 0))

        self.verticalLayout_2.addWidget(self.figure_placeholder3)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.BackButton3 = QPushButton(self.Page3)
        self.BackButton3.setObjectName(u"BackButton3")
        self.BackButton3.setFont(font)

        self.horizontalLayout_32.addWidget(self.BackButton3)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_32)

        self.desc_label_33 = QLabel(self.Page3)
        self.desc_label_33.setObjectName(u"desc_label_33")
        self.desc_label_33.setFont(font)

        self.horizontalLayout_32.addWidget(self.desc_label_33)

        self.NextButton3 = QPushButton(self.Page3)
        self.NextButton3.setObjectName(u"NextButton3")
        self.NextButton3.setEnabled(False)
        self.NextButton3.setFont(font)

        self.horizontalLayout_32.addWidget(self.NextButton3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_32)

        self.StackedWidget.addWidget(self.Page3)
        self.Page4 = QWidget()
        self.Page4.setObjectName(u"Page4")
        self.verticalLayout_4 = QVBoxLayout(self.Page4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.desc_label41 = QLabel(self.Page4)
        self.desc_label41.setObjectName(u"desc_label41")
        self.desc_label41.setFont(font)

        self.verticalLayout_4.addWidget(self.desc_label41)

        self.line_4 = QFrame(self.Page4)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_4)

        self.figure_placeholder4 = QWidget(self.Page4)
        self.figure_placeholder4.setObjectName(u"figure_placeholder4")
        self.figure_placeholder4.setMinimumSize(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.figure_placeholder4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.checkBox_same_file = QCheckBox(self.Page4)
        self.checkBox_same_file.setObjectName(u"checkBox_same_file")
        self.checkBox_same_file.setFont(font)
        self.checkBox_same_file.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.checkBox_same_file.setChecked(True)

        self.horizontalLayout_4.addWidget(self.checkBox_same_file)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.checkBox_overwrite = QCheckBox(self.Page4)
        self.checkBox_overwrite.setObjectName(u"checkBox_overwrite")
        self.checkBox_overwrite.setFont(font)
        self.checkBox_overwrite.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.checkBox_overwrite.setChecked(True)

        self.horizontalLayout_5.addWidget(self.checkBox_overwrite)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.desc_label42 = QLabel(self.Page4)
        self.desc_label42.setObjectName(u"desc_label42")
        self.desc_label42.setFont(font)

        self.horizontalLayout_41.addWidget(self.desc_label42)

        self.save_lineedit = QLineEdit(self.Page4)
        self.save_lineedit.setObjectName(u"save_lineedit")

        self.horizontalLayout_41.addWidget(self.save_lineedit)

        self.BrowseButton = QPushButton(self.Page4)
        self.BrowseButton.setObjectName(u"BrowseButton")
        self.BrowseButton.setEnabled(False)
        self.BrowseButton.setFont(font)

        self.horizontalLayout_41.addWidget(self.BrowseButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.BackButton4 = QPushButton(self.Page4)
        self.BackButton4.setObjectName(u"BackButton4")
        self.BackButton4.setFont(font)

        self.horizontalLayout_42.addWidget(self.BackButton4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_4)

        self.SaveButton = QPushButton(self.Page4)
        self.SaveButton.setObjectName(u"SaveButton")
        self.SaveButton.setEnabled(True)
        self.SaveButton.setFont(font)

        self.horizontalLayout_42.addWidget(self.SaveButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_42)

        self.StackedWidget.addWidget(self.Page4)

        self.verticalLayout_3.addWidget(self.StackedWidget)


        self.retranslateUi(EEGInspectorView)

        self.StackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(EEGInspectorView)
    # setupUi

    def retranslateUi(self, EEGInspectorView):
        EEGInspectorView.setWindowTitle(QCoreApplication.translate("EEGInspectorView", u"Form", None))
        self.file_name_label1.setText("")
        self.label.setText(QCoreApplication.translate("EEGInspectorView", u"<html><head/><body><p><span style=\" font-weight:700;\">EEGInspector App</span></p><p>Easily review and clean EEG data with EEGInspector. </p><p>This tool allows you to quickly identify and select bad channels and epochs based on visual inspection of EEG signals, <br/>making preprocessing faster and more reliable.</p><p><span style=\" font-style:italic;\">Note: EEGInspector is not optimized for long recordings with many channels. performance may be slower, so please be patient!</span></p></body></html>", None))
        self.desc_label11.setText(QCoreApplication.translate("EEGInspectorView", u"Browse to your EEG file, select the montage, and wait for the data to load.\n"
"Then, mark the non-brain channels for exclusion, confirm your selection, and click Next to proceed with further analysis.", None))
        self.edf_pushButton.setText(QCoreApplication.translate("EEGInspectorView", u"Choose", None))
        self.desc_label13.setText(QCoreApplication.translate("EEGInspectorView", u"Click on \"Next\" once your selection is finished or click on \"skip\" if you want to skip this step.", None))
        self.NextButton1.setText(QCoreApplication.translate("EEGInspectorView", u"Next", None))
        self.SkipButton1.setText(QCoreApplication.translate("EEGInspectorView", u"Skip", None))
        self.textEdit.setHtml(QCoreApplication.translate("EEGInspectorView", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select noisy channels to exclude them from further analysis.<br />Select channels that appear different from the others.<br />Click on the signal view, then use <span style=\" font-weight:700;\">+</span> / <span style=\" font-weight:700;\">\u2013</span> to adjust display sensitivity.</p></body></html>", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("EEGInspectorView", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Warning:</span> EEG inspector events previously saved in the PSG file are not displayed.</p></body></html>", None))
        self.BackButton2.setText(QCoreApplication.translate("EEGInspectorView", u"Back", None))
        self.desc_label22.setText(QCoreApplication.translate("EEGInspectorView", u"Click on \"Next\" once your selection is finished.", None))
        self.NextButton2.setText(QCoreApplication.translate("EEGInspectorView", u"Next", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("EEGInspectorView", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select bad epochs to exclude them from further analysis.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click on the signal view, then use <span style=\" font-weight:700;\">+ / \u2013</span> to adjust display sensitivity.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px;\">When viewing the entire recording (long recordings only), right-click on the signal view to display 30-second windows.</p></body></html>", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("EEGInspectorView", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Warning:</span> EEG inspector events previously saved in the PSG file are not displayed.</p></body></html>", None))
        self.desc_label32.setText(QCoreApplication.translate("EEGInspectorView", u"Size of sliding windows:", None))
        self.Epoch_len_comboBox.setItemText(0, QCoreApplication.translate("EEGInspectorView", u"10 seconds", None))
        self.Epoch_len_comboBox.setItemText(1, QCoreApplication.translate("EEGInspectorView", u"30 seconds", None))

        self.ApplyButton.setText(QCoreApplication.translate("EEGInspectorView", u"Apply", None))
        self.BackButton3.setText(QCoreApplication.translate("EEGInspectorView", u"Back", None))
        self.desc_label_33.setText(QCoreApplication.translate("EEGInspectorView", u"Click on \"Next\" once your selection is finished.", None))
        self.NextButton3.setText(QCoreApplication.translate("EEGInspectorView", u"Next", None))
        self.desc_label41.setText(QCoreApplication.translate("EEGInspectorView", u"EEG visual inspection is complete. The Power Spectral Density (PSD) is displayed without bad channels or epochs.\n"
"If you are satisfied with the results, save the artifact inspector events to exclude them from future analyses.", None))
        self.checkBox_same_file.setText(QCoreApplication.translate("EEGInspectorView", u"Check here if you want to write the event on your original input file. Otherwise, browse a directory to save a new file.", None))
        self.checkBox_overwrite.setText(QCoreApplication.translate("EEGInspectorView", u"Check here if you want to delete old events with the same group and name and replace the new ones", None))
        self.desc_label42.setText(QCoreApplication.translate("EEGInspectorView", u"Please select your destination to save the artifacts event file:", None))
        self.BrowseButton.setText(QCoreApplication.translate("EEGInspectorView", u"Browse", None))
        self.BackButton4.setText(QCoreApplication.translate("EEGInspectorView", u"Back", None))
        self.SaveButton.setText(QCoreApplication.translate("EEGInspectorView", u"save", None))
    # retranslateUi

