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
from PySide6.QtWidgets import (QApplication, QHeaderView, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_EdfXmlReaderResultsView(object):
    def setupUi(self, EdfXmlReaderResultsView):
        if not EdfXmlReaderResultsView.objectName():
            EdfXmlReaderResultsView.setObjectName(u"EdfXmlReaderResultsView")
        EdfXmlReaderResultsView.resize(483, 218)
        self.verticalLayout_2 = QVBoxLayout(EdfXmlReaderResultsView)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_tablewidget = QTableWidget(EdfXmlReaderResultsView)
        self.result_tablewidget.setObjectName(u"result_tablewidget")

        self.verticalLayout.addWidget(self.result_tablewidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(EdfXmlReaderResultsView)

        QMetaObject.connectSlotsByName(EdfXmlReaderResultsView)
    # setupUi

    def retranslateUi(self, EdfXmlReaderResultsView):
        EdfXmlReaderResultsView.setWindowTitle(QCoreApplication.translate("EdfXmlReaderResultsView", u"Form", None))
    # retranslateUi

