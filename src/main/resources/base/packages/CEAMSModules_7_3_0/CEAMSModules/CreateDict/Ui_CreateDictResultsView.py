# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_CreateDictResultsView.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)
import themes_rc

class Ui_CreateDictResultsView(object):
    def setupUi(self, CreateDictResultsView):
        if not CreateDictResultsView.objectName():
            CreateDictResultsView.setObjectName(u"CreateDictResultsView")
        CreateDictResultsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        CreateDictResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(CreateDictResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(CreateDictResultsView)

        QMetaObject.connectSlotsByName(CreateDictResultsView)
    # setupUi

    def retranslateUi(self, CreateDictResultsView):
        CreateDictResultsView.setWindowTitle(QCoreApplication.translate("CreateDictResultsView", u"Form", None))
    # retranslateUi

