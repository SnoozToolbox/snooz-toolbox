# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SleepStageRenameSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SleepStageRenameSettingsView(object):
    def setupUi(self, SleepStageRenameSettingsView):
        if not SleepStageRenameSettingsView.objectName():
            SleepStageRenameSettingsView.setObjectName(u"SleepStageRenameSettingsView")
        SleepStageRenameSettingsView.resize(550, 710)
        self.verticalLayout_2 = QVBoxLayout(SleepStageRenameSettingsView)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_8 = QLabel(SleepStageRenameSettingsView)
        self.label_8.setObjectName(u"label_8")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textEdit = QTextEdit(SleepStageRenameSettingsView)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.textEdit)

        self.frame = QFrame(SleepStageRenameSettingsView)
        self.frame.setObjectName(u"frame")
        font1 = QFont()
        font1.setKerning(False)
        self.frame.setFont(font1)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_32 = QLabel(self.frame)
        self.label_32.setObjectName(u"label_32")
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(False)
        self.label_32.setFont(font2)
        self.label_32.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_32)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 7, 1, 1, 1)

        self.label_26 = QLabel(self.frame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_26, 9, 2, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_13, 4, 0, 1, 1)

        self.label_22 = QLabel(self.frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_22, 4, 2, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 9, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 8, 1, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)

        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_20, 3, 0, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 1)

        self.label_30 = QLabel(self.frame)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_30, 3, 2, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 6, 1, 1, 1)

        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_17, 9, 0, 1, 1)

        self.label_33 = QLabel(self.frame)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font2)

        self.gridLayout.addWidget(self.label_33, 0, 0, 1, 1)

        self.label_27 = QLabel(self.frame)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_27, 5, 2, 1, 1)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_14, 8, 0, 1, 1)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 5, 1, 1, 1)

        self.label_25 = QLabel(self.frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_25, 6, 2, 1, 1)

        self.label_24 = QLabel(self.frame)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_24, 2, 2, 1, 1)

        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_23, 8, 2, 1, 1)

        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_18, 5, 0, 1, 1)

        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_21, 7, 0, 1, 1)

        self.label_29 = QLabel(self.frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_29, 0, 2, 1, 1)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_16, 6, 0, 1, 1)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)

        self.label_31 = QLabel(self.frame)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_31, 7, 2, 1, 1)

        self.label_28 = QLabel(self.frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_28, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.horizontalLayout.addWidget(self.frame)

        self.horizontalSpacer = QSpacerItem(13, 222, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_new_7 = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_new_7.setObjectName(u"lineEdit_new_7")

        self.gridLayout_2.addWidget(self.lineEdit_new_7, 9, 3, 1, 1)

        self.lineEdit_new_5 = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_new_5.setObjectName(u"lineEdit_new_5")

        self.gridLayout_2.addWidget(self.lineEdit_new_5, 7, 3, 1, 1)

        self.lineEdit_new_6 = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_new_6.setObjectName(u"lineEdit_new_6")

        self.gridLayout_2.addWidget(self.lineEdit_new_6, 8, 3, 1, 1)

        self.lineEdit_new_3 = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_new_3.setObjectName(u"lineEdit_new_3")

        self.gridLayout_2.addWidget(self.lineEdit_new_3, 5, 3, 1, 1)

        self.label_40 = QLabel(SleepStageRenameSettingsView)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_2.addWidget(self.label_40, 8, 0, 1, 1)

        self.lineEdit_ori_2 = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_ori_2.setObjectName(u"lineEdit_ori_2")

        self.gridLayout_2.addWidget(self.lineEdit_ori_2, 4, 1, 1, 1)

        self.lineEdit_new_0 = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_new_0.setObjectName(u"lineEdit_new_0")

        self.gridLayout_2.addWidget(self.lineEdit_new_0, 2, 3, 1, 1)

        self.label_46 = QLabel(SleepStageRenameSettingsView)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font)

        self.gridLayout_2.addWidget(self.label_46, 1, 3, 1, 1)

        self.label_34 = QLabel(SleepStageRenameSettingsView)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_2.addWidget(self.label_34, 2, 0, 1, 1)

        self.label_36 = QLabel(SleepStageRenameSettingsView)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_2.addWidget(self.label_36, 4, 0, 1, 1)

        self.lineEdit_ori_0 = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_ori_0.setObjectName(u"lineEdit_ori_0")

        self.gridLayout_2.addWidget(self.lineEdit_ori_0, 2, 1, 1, 1)

        self.lineEdit_group_ori = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_group_ori.setObjectName(u"lineEdit_group_ori")

        self.gridLayout_2.addWidget(self.lineEdit_group_ori, 0, 1, 1, 1)

        self.lineEdit_ori_5 = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_ori_5.setObjectName(u"lineEdit_ori_5")

        self.gridLayout_2.addWidget(self.lineEdit_ori_5, 7, 1, 1, 1)

        self.lineEdit_ori_6 = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_ori_6.setObjectName(u"lineEdit_ori_6")

        self.gridLayout_2.addWidget(self.lineEdit_ori_6, 8, 1, 1, 1)

        self.lineEdit_new_1 = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_new_1.setObjectName(u"lineEdit_new_1")

        self.gridLayout_2.addWidget(self.lineEdit_new_1, 3, 3, 1, 1)

        self.lineEdit_ori_1 = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_ori_1.setObjectName(u"lineEdit_ori_1")

        self.gridLayout_2.addWidget(self.lineEdit_ori_1, 3, 1, 1, 1)

        self.lineEdit_new_9 = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_new_9.setObjectName(u"lineEdit_new_9")

        self.gridLayout_2.addWidget(self.lineEdit_new_9, 10, 3, 1, 1)

        self.label_43 = QLabel(SleepStageRenameSettingsView)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font)

        self.gridLayout_2.addWidget(self.label_43, 1, 1, 1, 2)

        self.lineEdit_ori_7 = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_ori_7.setObjectName(u"lineEdit_ori_7")

        self.gridLayout_2.addWidget(self.lineEdit_ori_7, 9, 1, 1, 1)

        self.label_9 = QLabel(SleepStageRenameSettingsView)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_35 = QLabel(SleepStageRenameSettingsView)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_2.addWidget(self.label_35, 3, 0, 1, 1)

        self.lineEdit_ori_3 = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_ori_3.setObjectName(u"lineEdit_ori_3")

        self.gridLayout_2.addWidget(self.lineEdit_ori_3, 5, 1, 1, 1)

        self.lineEdit_new_2 = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_new_2.setObjectName(u"lineEdit_new_2")

        self.gridLayout_2.addWidget(self.lineEdit_new_2, 4, 3, 1, 1)

        self.lineEdit_new_4 = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_new_4.setObjectName(u"lineEdit_new_4")

        self.gridLayout_2.addWidget(self.lineEdit_new_4, 6, 3, 1, 1)

        self.label_39 = QLabel(SleepStageRenameSettingsView)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_2.addWidget(self.label_39, 7, 0, 1, 1)

        self.lineEdit_ori_9 = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_ori_9.setObjectName(u"lineEdit_ori_9")

        self.gridLayout_2.addWidget(self.lineEdit_ori_9, 10, 1, 1, 1)

        self.label_38 = QLabel(SleepStageRenameSettingsView)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_2.addWidget(self.label_38, 6, 0, 1, 1)

        self.label_41 = QLabel(SleepStageRenameSettingsView)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(90, 0))

        self.gridLayout_2.addWidget(self.label_41, 9, 0, 1, 1)

        self.label_42 = QLabel(SleepStageRenameSettingsView)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_2.addWidget(self.label_42, 10, 0, 1, 1)

        self.lineEdit_group_new = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_group_new.setObjectName(u"lineEdit_group_new")

        self.gridLayout_2.addWidget(self.lineEdit_group_new, 0, 2, 1, 2)

        self.label_37 = QLabel(SleepStageRenameSettingsView)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_2.addWidget(self.label_37, 5, 0, 1, 1)

        self.label_47 = QLabel(SleepStageRenameSettingsView)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(90, 0))
        self.label_47.setFont(font)

        self.gridLayout_2.addWidget(self.label_47, 0, 0, 1, 1)

        self.lineEdit_ori_4 = QLineEdit(SleepStageRenameSettingsView)
        self.lineEdit_ori_4.setObjectName(u"lineEdit_ori_4")

        self.gridLayout_2.addWidget(self.lineEdit_ori_4, 6, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 11, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)

        self.line_2 = QFrame(SleepStageRenameSettingsView)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(SleepStageRenameSettingsView)

        QMetaObject.connectSlotsByName(SleepStageRenameSettingsView)
    # setupUi

    def retranslateUi(self, SleepStageRenameSettingsView):
        SleepStageRenameSettingsView.setWindowTitle(QCoreApplication.translate("SleepStageRenameSettingsView", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Sleep Stage Conversion settings", None))
        self.textEdit.setHtml(QCoreApplication.translate("SleepStageRenameSettingsView", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Each original annotation is renamed with the new annotation name.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Enter the annotation name or number that define each sleep stage in your study.</span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Reference table", None))
        self.label_3.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"3", None))
        self.label_11.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"6", None))
        self.label_26.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"-", None))
        self.label_13.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Stage 3", None))
        self.label_22.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"N3", None))
        self.label_5.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"9", None))
        self.label.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"1", None))
        self.label_7.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"7", None))
        self.label_6.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"0", None))
        self.label_20.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Stage 2", None))
        self.label_12.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"R&K", None))
        self.label_30.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"N2", None))
        self.label_4.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"5", None))
        self.label_17.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Unscored", None))
        self.label_33.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Stage", None))
        self.label_27.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"-", None))
        self.label_14.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Tech Intervention", None))
        self.label_10.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"4", None))
        self.label_25.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"R", None))
        self.label_24.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"N1", None))
        self.label_23.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"-", None))
        self.label_19.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Wake", None))
        self.label_18.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Stage 4", None))
        self.label_21.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Movement", None))
        self.label_29.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"AASM", None))
        self.label_16.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"REM", None))
        self.label_15.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Stage 1", None))
        self.label_2.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"2", None))
        self.label_31.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"6", None))
        self.label_28.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"W", None))
        self.lineEdit_new_7.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"7", None))
        self.lineEdit_new_5.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"5", None))
        self.lineEdit_new_6.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"6", None))
        self.lineEdit_new_3.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"3", None))
        self.label_40.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Movement", None))
        self.lineEdit_ori_2.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"NREM2", None))
        self.lineEdit_new_0.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"0", None))
        self.label_46.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"New Annotation Name", None))
        self.label_34.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Wake", None))
        self.label_36.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Stage 2", None))
        self.lineEdit_ori_0.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"wake", None))
        self.lineEdit_group_ori.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"stage", None))
        self.lineEdit_ori_5.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"REM", None))
        self.lineEdit_ori_6.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"movement", None))
        self.lineEdit_new_1.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"1", None))
        self.lineEdit_ori_1.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"NREM1", None))
        self.lineEdit_new_9.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"9", None))
        self.label_43.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Original Annotation Name", None))
        self.lineEdit_ori_7.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"tech", None))
        self.label_9.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Name Event", None))
        self.label_35.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Stage 1", None))
        self.lineEdit_ori_3.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"NREM3", None))
        self.lineEdit_new_2.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"2", None))
        self.lineEdit_new_4.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"4", None))
        self.label_39.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"REM", None))
        self.lineEdit_ori_9.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"undefined", None))
        self.label_38.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Stage 4", None))
        self.label_41.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Tech Intervention", None))
        self.label_42.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Unscored", None))
        self.lineEdit_group_new.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"stage", None))
        self.label_37.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Stage 3", None))
        self.label_47.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"Group Event", None))
        self.lineEdit_ori_4.setText(QCoreApplication.translate("SleepStageRenameSettingsView", u"NREM4", None))
    # retranslateUi

