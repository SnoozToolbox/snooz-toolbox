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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MutualInfoSettingsView(object):
    def setupUi(self, MutualInfoSettingsView):
        if not MutualInfoSettingsView.objectName():
            MutualInfoSettingsView.setObjectName(u"MutualInfoSettingsView")
        MutualInfoSettingsView.resize(448, 241)
        self.gridLayout = QGridLayout(MutualInfoSettingsView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Title = QLabel(MutualInfoSettingsView)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setBold(True)
        self.Title.setFont(font)
        self.Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(MutualInfoSettingsView)

        QMetaObject.connectSlotsByName(MutualInfoSettingsView)
    # setupUi

    def retranslateUi(self, MutualInfoSettingsView):
        MutualInfoSettingsView.setWindowTitle(QCoreApplication.translate("MutualInfoSettingsView", u"Form", None))
        self.Title.setText(QCoreApplication.translate("MutualInfoSettingsView", u"MutualInfo settings", None))
    # retranslateUi

