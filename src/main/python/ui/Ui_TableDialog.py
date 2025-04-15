# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_TableDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_TableDialog(object):
    def setupUi(self, TableDialog):
        if not TableDialog.objectName():
            TableDialog.setObjectName(u"TableDialog")
        TableDialog.resize(442, 406)
        self.verticalLayout = QVBoxLayout(TableDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title_label = QLabel(TableDialog)
        self.title_label.setObjectName(u"title_label")

        self.verticalLayout_2.addWidget(self.title_label)

        self.message_label = QLabel(TableDialog)
        self.message_label.setObjectName(u"message_label")
        self.message_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.message_label)

        self.tablewidget = QTableWidget(TableDialog)
        self.tablewidget.setObjectName(u"tablewidget")
        self.tablewidget.setColumnCount(0)
        self.tablewidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tablewidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ok_pushbutton = QPushButton(TableDialog)
        self.ok_pushbutton.setObjectName(u"ok_pushbutton")

        self.horizontalLayout.addWidget(self.ok_pushbutton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(TableDialog)
        self.ok_pushbutton.clicked.connect(TableDialog.close)

        QMetaObject.connectSlotsByName(TableDialog)
    # setupUi

    def retranslateUi(self, TableDialog):
        TableDialog.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("TableDialog", u"<html><head/><body><p>Title</p></body></html>", None))
        self.message_label.setText(QCoreApplication.translate("TableDialog", u"message", None))
        self.ok_pushbutton.setText(QCoreApplication.translate("TableDialog", u"Ok", None))
    # retranslateUi

