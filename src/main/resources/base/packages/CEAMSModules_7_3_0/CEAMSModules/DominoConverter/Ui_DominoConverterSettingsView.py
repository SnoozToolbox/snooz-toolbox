# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DominoConverterSettingsView.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
import themes_rc

class Ui_DominoConverterSettingsView(object):
    def setupUi(self, DominoConverterSettingsView):
        if not DominoConverterSettingsView.objectName():
            DominoConverterSettingsView.setObjectName(u"DominoConverterSettingsView")
        DominoConverterSettingsView.resize(764, 616)
        DominoConverterSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout_4 = QHBoxLayout(DominoConverterSettingsView)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(DominoConverterSettingsView)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(DominoConverterSettingsView)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(DominoConverterSettingsView)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(1000, 16777215))

        self.verticalLayout.addWidget(self.label_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.folders_label = QLabel(DominoConverterSettingsView)
        self.folders_label.setObjectName(u"folders_label")

        self.verticalLayout_3.addWidget(self.folders_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.folders_lineedit = QLineEdit(DominoConverterSettingsView)
        self.folders_lineedit.setObjectName(u"folders_lineedit")
        self.folders_lineedit.setMaximumSize(QSize(1000, 16777215))
        self.folders_lineedit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.folders_lineedit)

        self.pushButton_add_folder = QPushButton(DominoConverterSettingsView)
        self.pushButton_add_folder.setObjectName(u"pushButton_add_folder")
        self.pushButton_add_folder.setMinimumSize(QSize(90, 0))

        self.horizontalLayout.addWidget(self.pushButton_add_folder)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(DominoConverterSettingsView)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_logfilename = QLineEdit(DominoConverterSettingsView)
        self.lineEdit_logfilename.setObjectName(u"lineEdit_logfilename")
        self.lineEdit_logfilename.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_logfilename)

        self.pushButton_browse_log = QPushButton(DominoConverterSettingsView)
        self.pushButton_browse_log.setObjectName(u"pushButton_browse_log")
        self.pushButton_browse_log.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_3.addWidget(self.pushButton_browse_log)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_5 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.label_5 = QLabel(DominoConverterSettingsView)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.textEdit = QTextEdit(DominoConverterSettingsView)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(725, 0))
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.textEdit.setLineWrapColumnOrWidth(0)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textEdit)

        self.verticalSpacer_6 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(32, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.retranslateUi(DominoConverterSettingsView)
        self.pushButton_add_folder.clicked.connect(DominoConverterSettingsView.add_folder_slot)
        self.pushButton_browse_log.clicked.connect(DominoConverterSettingsView.browse_log_slot)

        QMetaObject.connectSlotsByName(DominoConverterSettingsView)
    # setupUi

    def retranslateUi(self, DominoConverterSettingsView):
        DominoConverterSettingsView.setWindowTitle(QCoreApplication.translate("DominoConverterSettingsView", u"Form", None))
        self.label.setText(QCoreApplication.translate("DominoConverterSettingsView", u"Add all the recordng folders, each folder includes :", None))
        self.label_2.setText(QCoreApplication.translate("DominoConverterSettingsView", u" - the edf file of the recording", None))
        self.label_3.setText(QCoreApplication.translate("DominoConverterSettingsView", u" - all the ASCII export annotation files from DOMINO\n"
"   (ANALYSIS DATA- WITHOUT SLEEP PROFILE)", None))
        self.folders_label.setText(QCoreApplication.translate("DominoConverterSettingsView", u"Folder(s)", None))
        self.folders_lineedit.setPlaceholderText(QCoreApplication.translate("DominoConverterSettingsView", u"Select and add folders.", None))
        self.pushButton_add_folder.setText(QCoreApplication.translate("DominoConverterSettingsView", u"Add Folder", None))
        self.label_4.setText(QCoreApplication.translate("DominoConverterSettingsView", u"To save the conversion log warning message.", None))
        self.lineEdit_logfilename.setPlaceholderText(QCoreApplication.translate("DominoConverterSettingsView", u"Define the log file to save.", None))
        self.pushButton_browse_log.setText(QCoreApplication.translate("DominoConverterSettingsView", u"Browse", None))
        self.label_5.setText(QCoreApplication.translate("DominoConverterSettingsView", u"Example of log file", None))
        self.textEdit.setHtml(QCoreApplication.translate("DominoConverterSettingsView", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">recording			filename			warning</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">patient_xxxx		Flow Events		Success</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">patient_xxxx		Sleep profile		Success</p>\n"
"<p style=\" margin-top:0px; margin-b"
                        "ottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">patient_xxxx		Average Frequency Value 	2 columns format but no Rate</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">patient_xxxx		CAP			empty</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">patient_xxxx		Spindle  K			Success</p></body></html>", None))
    # retranslateUi

