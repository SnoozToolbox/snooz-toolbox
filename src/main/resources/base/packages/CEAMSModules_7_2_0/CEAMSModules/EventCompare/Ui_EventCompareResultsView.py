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

class Ui_EventCompareResultsView(object):
    def setupUi(self, EventCompareResultsView):
        if not EventCompareResultsView.objectName():
            EventCompareResultsView.setObjectName(u"EventCompareResultsView")
        EventCompareResultsView.resize(660, 550)
        self.verticalLayout = QVBoxLayout(EventCompareResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.result_tablewidget = QTableWidget(EventCompareResultsView)
        self.result_tablewidget.setObjectName(u"result_tablewidget")

        self.verticalLayout_2.addWidget(self.result_tablewidget)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(EventCompareResultsView)

        QMetaObject.connectSlotsByName(EventCompareResultsView)
    # setupUi

    def retranslateUi(self, EventCompareResultsView):
        EventCompareResultsView.setWindowTitle(QCoreApplication.translate("EventCompareResultsView", u"Form", None))
    # retranslateUi

