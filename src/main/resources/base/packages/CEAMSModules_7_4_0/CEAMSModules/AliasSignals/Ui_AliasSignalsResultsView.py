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

class Ui_AliasSignalsResultsView(object):
    def setupUi(self, AliasSignalsResultsView):
        if not AliasSignalsResultsView.objectName():
            AliasSignalsResultsView.setObjectName(u"AliasSignalsResultsView")
        AliasSignalsResultsView.resize(927, 262)
        self.verticalLayout = QVBoxLayout(AliasSignalsResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signal_layout = QVBoxLayout()
        self.signal_layout.setObjectName(u"signal_layout")

        self.verticalLayout.addLayout(self.signal_layout)


        self.retranslateUi(AliasSignalsResultsView)

        QMetaObject.connectSlotsByName(AliasSignalsResultsView)
    # setupUi

    def retranslateUi(self, AliasSignalsResultsView):
        AliasSignalsResultsView.setWindowTitle(QCoreApplication.translate("AliasSignalsResultsView", u"Form", None))
    # retranslateUi

