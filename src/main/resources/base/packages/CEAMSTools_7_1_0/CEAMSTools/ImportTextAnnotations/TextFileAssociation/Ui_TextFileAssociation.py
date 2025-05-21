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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
import themes_rc

class Ui_TextFileAssociation(object):
    def setupUi(self, TextFileAssociation):
        if not TextFileAssociation.objectName():
            TextFileAssociation.setObjectName(u"TextFileAssociation")
        TextFileAssociation.resize(730, 590)
        TextFileAssociation.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout = QHBoxLayout(TextFileAssociation)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_16 = QLabel(TextFileAssociation)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout.addWidget(self.label_16)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_17 = QLabel(TextFileAssociation)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout.addWidget(self.label_17)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_18 = QLabel(TextFileAssociation)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(50, 0))

        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_19 = QLabel(TextFileAssociation)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 1, 0, 1, 1)

        self.lineEdit_prefix = QLineEdit(TextFileAssociation)
        self.lineEdit_prefix.setObjectName(u"lineEdit_prefix")

        self.gridLayout_3.addWidget(self.lineEdit_prefix, 0, 1, 1, 1)

        self.lineEdit_suffix = QLineEdit(TextFileAssociation)
        self.lineEdit_suffix.setObjectName(u"lineEdit_suffix")

        self.gridLayout_3.addWidget(self.lineEdit_suffix, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.label = QLabel(TextFileAssociation)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 0))

        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)

        self.lineEdit_ext = QLineEdit(TextFileAssociation)
        self.lineEdit_ext.setObjectName(u"lineEdit_ext")

        self.gridLayout_3.addWidget(self.lineEdit_ext, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.checkBox_case_sensitive = QCheckBox(TextFileAssociation)
        self.checkBox_case_sensitive.setObjectName(u"checkBox_case_sensitive")
        self.checkBox_case_sensitive.setEnabled(False)
        self.checkBox_case_sensitive.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox_case_sensitive)

        self.textEdit = QTextEdit(TextFileAssociation)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(222, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(TextFileAssociation)

        QMetaObject.connectSlotsByName(TextFileAssociation)
    # setupUi

    def retranslateUi(self, TextFileAssociation):
        TextFileAssociation.setWindowTitle("")
        self.label_16.setText(QCoreApplication.translate("TextFileAssociation", u"<html><head/><body><p><span style=\" font-weight:600;\">Annotations Text File Name</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("TextFileAssociation", u"Define the filename to read annotations based on the PSG filename.", None))
        self.label_18.setText(QCoreApplication.translate("TextFileAssociation", u"prefix", None))
        self.label_19.setText(QCoreApplication.translate("TextFileAssociation", u"suffix", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_prefix.setToolTip(QCoreApplication.translate("TextFileAssociation", u"Optionally, define the prefix to insert before the PSG filename to identify the stages filename.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEdit_suffix.setToolTip(QCoreApplication.translate("TextFileAssociation", u"Optionally, define the suffix to append to the PSG filename to identify the stages filename.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("TextFileAssociation", u"extension", None))
        self.lineEdit_ext.setText(QCoreApplication.translate("TextFileAssociation", u"tsv", None))
#if QT_CONFIG(tooltip)
        self.checkBox_case_sensitive.setToolTip(QCoreApplication.translate("TextFileAssociation", u"Uncheck if the sleep stage filename has a different case than the EDF filename.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_case_sensitive.setText(QCoreApplication.translate("TextFileAssociation", u"Filenames are case sensitive", None))
        self.textEdit.setHtml(QCoreApplication.translate("TextFileAssociation", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Example )</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:600;\">prefix		</span>annot_</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:600;\">PSG filename	</span>subject1.edf</p>\n"
"<p"
                        " style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:600;\">suffix		</span> _expert1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:600;\">extension</span> 	tsv</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:600;\">text filename	</span>annot_subject1_expert1.tsv</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

