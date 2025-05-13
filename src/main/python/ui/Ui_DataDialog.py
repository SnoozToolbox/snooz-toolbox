# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DataDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLayout,
    QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_DataDialog(object):
    def setupUi(self, DataDialog):
        if not DataDialog.objectName():
            DataDialog.setObjectName(u"DataDialog")
        DataDialog.resize(668, 272)
        DataDialog.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.vboxLayout = QVBoxLayout(DataDialog)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.textBrowser = QTextBrowser(DataDialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"QTextBrowser {\n"
"    background-color: #f5faff;  /* light blue */\n"
"    color: #2c3e50;             /* dark text */\n"
"    border: 1px solid #ccc;\n"
"    padding: 5px;\n"
"}\n"
"font: 12pt \"Roboto\";")
        self.textBrowser.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.textBrowser)


        self.vboxLayout.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(250, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.data_dialog_close_button = QPushButton(DataDialog)
        self.data_dialog_close_button.setObjectName(u"data_dialog_close_button")
        self.data_dialog_close_button.setStyleSheet(u"QPushButton#data_dialog_close_button {\n"
"    background-color: rgba(0, 182, 121, 255);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton#data_dialog_close_button:hover {\n"
"    background-color: rgba(0, 224, 121, 255);\n"
"}\n"
"\n"
"QPushButton#data_dialog_close_button:pressed {\n"
"    background-color: rgba(0, 160, 121, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.data_dialog_close_button)

        self.horizontalSpacer_2 = QSpacerItem(250, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.vboxLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DataDialog)
        self.data_dialog_close_button.clicked.connect(DataDialog.close)

        QMetaObject.connectSlotsByName(DataDialog)
    # setupUi

    def retranslateUi(self, DataDialog):
        DataDialog.setWindowTitle(QCoreApplication.translate("DataDialog", u"Data Files", None))
        self.textBrowser.setHtml(QCoreApplication.translate("DataDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">The following link leads to a GitHub repository hosted by the Snooz ToolBox Team. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">It contains two </span><span style=\" font-family:'Courier New';\">.edf</span><span style=\" font-fa"
                        "mily:'Segoe UI';\"> files and their corresponding </span><span style=\" font-family:'Courier New';\">.tsv</span><span style=\" font-family:'Segoe UI';\"> files, which are compatible with most tools that Snooz offers. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/SnoozToolbox/snooz-datasets/releases/tag/latest\"><span style=\" font-family:'Segoe UI'; font-weight:700; text-decoration: underline; color:#0000ff;\">Download NSRR Example Files</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-weight:700; text-decoration: underline; color:#99ebff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">After arriving on the download page, "
                        "simply click on the filenames that you which to download in the </span><span style=\" font-family:'Segoe UI'; font-weight:700;\">Assets</span><span style=\" font-family:'Segoe UI';\"> section.</span></p></body></html>", None))
#if QT_CONFIG(accessibility)
        self.data_dialog_close_button.setAccessibleName(QCoreApplication.translate("DataDialog", u"data_dialog_close_button", None))
#endif // QT_CONFIG(accessibility)
        self.data_dialog_close_button.setText(QCoreApplication.translate("DataDialog", u"Close", None))
    # retranslateUi

