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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_IcaRestoreSettingsView(object):
    def setupUi(self, IcaRestoreSettingsView):
        if not IcaRestoreSettingsView.objectName():
            IcaRestoreSettingsView.setObjectName(u"IcaRestoreSettingsView")
        IcaRestoreSettingsView.resize(448, 241)
        self.gridLayout = QGridLayout(IcaRestoreSettingsView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Title = QLabel(IcaRestoreSettingsView)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setBold(True)
        self.Title.setFont(font)
        self.Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(230, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(IcaRestoreSettingsView)

        QMetaObject.connectSlotsByName(IcaRestoreSettingsView)
    # setupUi

    def retranslateUi(self, IcaRestoreSettingsView):
        IcaRestoreSettingsView.setWindowTitle(QCoreApplication.translate("IcaRestoreSettingsView", u"Form", None))
        self.Title.setText(QCoreApplication.translate("IcaRestoreSettingsView", u"IcaRestore settings", None))
    # retranslateUi

