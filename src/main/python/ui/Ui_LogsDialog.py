# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_LogsDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_LogsDialog(object):
    def setupUi(self, LogsDialog):
        if not LogsDialog.objectName():
            LogsDialog.setObjectName(u"LogsDialog")
        LogsDialog.resize(673, 436)
        self.verticalLayout = QVBoxLayout(LogsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(LogsDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.logs_textedit = QPlainTextEdit(LogsDialog)
        self.logs_textedit.setObjectName(u"logs_textedit")
        self.logs_textedit.setReadOnly(True)

        self.verticalLayout.addWidget(self.logs_textedit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.clear_pushbutton = QPushButton(LogsDialog)
        self.clear_pushbutton.setObjectName(u"clear_pushbutton")

        self.horizontalLayout.addWidget(self.clear_pushbutton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.close_pushbutton = QPushButton(LogsDialog)
        self.close_pushbutton.setObjectName(u"close_pushbutton")

        self.horizontalLayout.addWidget(self.close_pushbutton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(LogsDialog)
        self.close_pushbutton.clicked.connect(LogsDialog.close)
        self.clear_pushbutton.clicked.connect(LogsDialog.on_clear)

        QMetaObject.connectSlotsByName(LogsDialog)
    # setupUi

    def retranslateUi(self, LogsDialog):
        LogsDialog.setWindowTitle(QCoreApplication.translate("LogsDialog", u"Logs", None))
        self.label.setText(QCoreApplication.translate("LogsDialog", u"Logs generated while running a process.", None))
        self.logs_textedit.setPlainText("")
        self.clear_pushbutton.setText(QCoreApplication.translate("LogsDialog", u"Clear", None))
        self.close_pushbutton.setText(QCoreApplication.translate("LogsDialog", u"Close", None))
    # retranslateUi

