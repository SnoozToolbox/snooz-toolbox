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

class Ui_AliasSignalsSettingsView(object):
    def setupUi(self, AliasSignalsSettingsView):
        if not AliasSignalsSettingsView.objectName():
            AliasSignalsSettingsView.setObjectName(u"AliasSignalsSettingsView")
        AliasSignalsSettingsView.resize(415, 224)
        self.layoutWidget = QWidget(AliasSignalsSettingsView)
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

        self.alias_lineedit = QLineEditLive(self.layoutWidget)
        self.alias_lineedit.setObjectName(u"alias_lineedit")

        self.gridLayout_2.addWidget(self.alias_lineedit, 1, 1, 1, 1)


        self.retranslateUi(AliasSignalsSettingsView)

        QMetaObject.connectSlotsByName(AliasSignalsSettingsView)
    # setupUi

    def retranslateUi(self, AliasSignalsSettingsView):
        AliasSignalsSettingsView.setWindowTitle(QCoreApplication.translate("AliasSignalsSettingsView", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("AliasSignalsSettingsView", u"AliasSignals settings", None))
        self.label_9.setText(QCoreApplication.translate("AliasSignalsSettingsView", u"Alias", None))
    # retranslateUi

