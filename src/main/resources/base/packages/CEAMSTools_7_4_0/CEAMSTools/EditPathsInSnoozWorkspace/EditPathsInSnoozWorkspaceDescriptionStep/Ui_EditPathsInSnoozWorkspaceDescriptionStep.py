# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EditPathsInSnoozWorkspaceDescriptionStep.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_EditPathsInSnoozWorkspaceDescriptionStep(object):
    def setupUi(self, EditPathsInSnoozWorkspaceDescriptionStep):
        if not EditPathsInSnoozWorkspaceDescriptionStep.objectName():
            EditPathsInSnoozWorkspaceDescriptionStep.setObjectName(u"EditPathsInSnoozWorkspaceDescriptionStep")
        EditPathsInSnoozWorkspaceDescriptionStep.resize(1032, 815)
        EditPathsInSnoozWorkspaceDescriptionStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(EditPathsInSnoozWorkspaceDescriptionStep)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.textEdit = QTextEdit(EditPathsInSnoozWorkspaceDescriptionStep)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Shadow.Raised)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.textEdit)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.retranslateUi(EditPathsInSnoozWorkspaceDescriptionStep)

        QMetaObject.connectSlotsByName(EditPathsInSnoozWorkspaceDescriptionStep)
    # setupUi

    def retranslateUi(self, EditPathsInSnoozWorkspaceDescriptionStep):
        EditPathsInSnoozWorkspaceDescriptionStep.setWindowTitle("")
        self.textEdit.setHtml(QCoreApplication.translate("EditPathsInSnoozWorkspaceDescriptionStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Snooz Workspace Path Editor</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This tool helps you update th"
                        "e internal paths in your Snooz workspaces (JSON files) to ensure compatibility across different systems.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Key Features:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Path Adaptation</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	- Automatically updates paths stored in Snooz workspace files when transferring them to a different machine or environment</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	- Supports both absolute and relative paths</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. System Compatibilit"
                        "y</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	- Converts between Windows (\\) and Unix (/) path formats</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	- Adjusts for changes in directory depth or structure</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">How to use:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Select one or more Snooz workspaces (with .json extension), or choose an entire folder</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-rig"
                        "ht:0px; -qt-block-indent:0; text-indent:0px;\">- Snooz can batch-process multiple workspaces at once</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- A warning is shown if an edited path does not exist</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Preview all path changes before running the tool or saving the modified files in the <span style=\" font-weight:700;\">select all mode</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- <span style=\" font-weight:700;\">A warning</span> is displayed if the exact same path appears in more than one selected workspace. To avoid confusion during path replacement, users must load only workspaces with unique paths.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\">- <span style=\" font-weight:700;\">IMPORTANT NOTE:</span> Please ensure that all intended workspaces <span style=\" font-weight:700;\">are selected</span> before running the tool. If no workspaces are selected, the path modifications will <span style=\" font-weight:700;\">not</span> be applied, <span style=\" font-weight:700;\">even</span> if the workspaces are loaded.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Input:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	- Snooz workspace files (.json)<br />	- Paths as plain strings inside the workspace<br />	- Output folder and suffix for saving modified files</p>\n"
"<p"
                        " style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Output:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	- Updated Snooz workspace files with updated paths</p></body></html>", None))
    # retranslateUi

