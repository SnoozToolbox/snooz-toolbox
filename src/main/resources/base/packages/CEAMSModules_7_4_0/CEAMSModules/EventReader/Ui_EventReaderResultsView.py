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

class Ui_EventReaderResultsView(object):
    def setupUi(self, EventReaderResultsView):
        if not EventReaderResultsView.objectName():
            EventReaderResultsView.setObjectName(u"EventReaderResultsView")
        EventReaderResultsView.resize(483, 218)
        self.verticalLayout_2 = QVBoxLayout(EventReaderResultsView)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_tablewidget = QTableWidget(EventReaderResultsView)
        self.result_tablewidget.setObjectName(u"result_tablewidget")

        self.verticalLayout.addWidget(self.result_tablewidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(EventReaderResultsView)

        QMetaObject.connectSlotsByName(EventReaderResultsView)
    # setupUi

    def retranslateUi(self, EventReaderResultsView):
        EventReaderResultsView.setWindowTitle(QCoreApplication.translate("EventReaderResultsView", u"Form", None))
    # retranslateUi

