# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_TSVValidatorMasterResultsView.ui'
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

class Ui_TSVValidatorMasterResultsView(object):
    def setupUi(self, TSVValidatorMasterResultsView):
        if not TSVValidatorMasterResultsView.objectName():
            TSVValidatorMasterResultsView.setObjectName(u"TSVValidatorMasterResultsView")
        TSVValidatorMasterResultsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        TSVValidatorMasterResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(TSVValidatorMasterResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(TSVValidatorMasterResultsView)

        QMetaObject.connectSlotsByName(TSVValidatorMasterResultsView)
    # setupUi

    def retranslateUi(self, TSVValidatorMasterResultsView):
        TSVValidatorMasterResultsView.setWindowTitle(QCoreApplication.translate("TSVValidatorMasterResultsView", u"Form", None))
    # retranslateUi

