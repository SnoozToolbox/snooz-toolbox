# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DpliConnectivityResultsView.ui'
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
class Ui_DpliConnectivityResultsView(object):
    def setupUi(self, DpliConnectivityResultsView):
        if not DpliConnectivityResultsView.objectName():
            DpliConnectivityResultsView.setObjectName(u"DpliConnectivityResultsView")
        DpliConnectivityResultsView.setStyleSheet(u"font: 10pt \"Roboto-Regular\";")
        DpliConnectivityResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(DpliConnectivityResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(DpliConnectivityResultsView)

        QMetaObject.connectSlotsByName(DpliConnectivityResultsView)
    # setupUi

    def retranslateUi(self, DpliConnectivityResultsView):
        DpliConnectivityResultsView.setWindowTitle(QCoreApplication.translate("DpliConnectivityResultsView", u"Form", None))
    # retranslateUi

