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
import themes_rc

class Ui_RenameFileListResultsView(object):
    def setupUi(self, RenameFileListResultsView):
        if not RenameFileListResultsView.objectName():
            RenameFileListResultsView.setObjectName(u"RenameFileListResultsView")
        RenameFileListResultsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        RenameFileListResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(RenameFileListResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(RenameFileListResultsView)

        QMetaObject.connectSlotsByName(RenameFileListResultsView)
    # setupUi

    def retranslateUi(self, RenameFileListResultsView):
        RenameFileListResultsView.setWindowTitle(QCoreApplication.translate("RenameFileListResultsView", u"Form", None))
    # retranslateUi

