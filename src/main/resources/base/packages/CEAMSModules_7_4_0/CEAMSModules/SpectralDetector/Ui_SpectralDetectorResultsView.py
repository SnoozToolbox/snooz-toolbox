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

class Ui_SpectralDetectorResultsView(object):
    def setupUi(self, SpectralDetectorResultsView):
        if not SpectralDetectorResultsView.objectName():
            SpectralDetectorResultsView.setObjectName(u"SpectralDetectorResultsView")
        SpectralDetectorResultsView.resize(677, 303)
        self.verticalLayout = QVBoxLayout(SpectralDetectorResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(SpectralDetectorResultsView)

        QMetaObject.connectSlotsByName(SpectralDetectorResultsView)
    # setupUi

    def retranslateUi(self, SpectralDetectorResultsView):
        SpectralDetectorResultsView.setWindowTitle(QCoreApplication.translate("SpectralDetectorResultsView", u"Form", None))
    # retranslateUi

