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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)

class Ui_FilterEventsResultsView(object):
    def setupUi(self, FilterEventsResultsView):
        if not FilterEventsResultsView.objectName():
            FilterEventsResultsView.setObjectName(u"FilterEventsResultsView")
        FilterEventsResultsView.resize(927, 262)
        self.verticalLayout = QVBoxLayout(FilterEventsResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signal_layout = QVBoxLayout()
        self.signal_layout.setObjectName(u"signal_layout")

        self.verticalLayout.addLayout(self.signal_layout)


        self.retranslateUi(FilterEventsResultsView)

        QMetaObject.connectSlotsByName(FilterEventsResultsView)
    # setupUi

    def retranslateUi(self, FilterEventsResultsView):
        FilterEventsResultsView.setWindowTitle(QCoreApplication.translate("FilterEventsResultsView", u"Form", None))
    # retranslateUi

