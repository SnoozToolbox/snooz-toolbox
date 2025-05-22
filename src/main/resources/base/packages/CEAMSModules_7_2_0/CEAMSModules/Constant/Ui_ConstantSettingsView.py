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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

from widgets.QLineEditLive import QLineEditLive

class Ui_ConstantSettingsView(object):
    def setupUi(self, ConstantSettingsView):
        if not ConstantSettingsView.objectName():
            ConstantSettingsView.setObjectName(u"ConstantSettingsView")
        ConstantSettingsView.resize(415, 224)
        self.layoutWidget = QWidget(ConstantSettingsView)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 248, 46))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setBold(True)
        self.label_8.setFont(font)

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 2)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.constant_lineedit = QLineEditLive(self.layoutWidget)
        self.constant_lineedit.setObjectName(u"constant_lineedit")

        self.gridLayout_2.addWidget(self.constant_lineedit, 1, 1, 1, 1)


        self.retranslateUi(ConstantSettingsView)

        QMetaObject.connectSlotsByName(ConstantSettingsView)
    # setupUi

    def retranslateUi(self, ConstantSettingsView):
        ConstantSettingsView.setWindowTitle(QCoreApplication.translate("ConstantSettingsView", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("ConstantSettingsView", u"Constant settings", None))
        self.label_9.setText(QCoreApplication.translate("ConstantSettingsView", u"Constant value", None))
    # retranslateUi

