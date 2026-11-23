# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AECConnectivitySettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_AECConnectivitySettingsView(object):
    def setupUi(self, AECConnectivitySettingsView):
        if not AECConnectivitySettingsView.objectName():
            AECConnectivitySettingsView.setObjectName(u"AECConnectivitySettingsView")
        AECConnectivitySettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(AECConnectivitySettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.epochs_horizontalLayout = QHBoxLayout()
        self.epochs_horizontalLayout.setObjectName(u"epochs_horizontalLayout")
        self.epochs_label = QLabel(AECConnectivitySettingsView)
        self.epochs_label.setObjectName(u"epochs_label")

        self.epochs_horizontalLayout.addWidget(self.epochs_label)

        self.epochs_lineedit = QLineEdit(AECConnectivitySettingsView)
        self.epochs_lineedit.setObjectName(u"epochs_lineedit")

        self.epochs_horizontalLayout.addWidget(self.epochs_lineedit)


        self.verticalLayout.addLayout(self.epochs_horizontalLayout)

        self.events_horizontalLayout = QHBoxLayout()
        self.events_horizontalLayout.setObjectName(u"events_horizontalLayout")
        self.events_label = QLabel(AECConnectivitySettingsView)
        self.events_label.setObjectName(u"events_label")

        self.events_horizontalLayout.addWidget(self.events_label)

        self.events_lineedit = QLineEdit(AECConnectivitySettingsView)
        self.events_lineedit.setObjectName(u"events_lineedit")

        self.events_horizontalLayout.addWidget(self.events_lineedit)


        self.verticalLayout.addLayout(self.events_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(AECConnectivitySettingsView)

        QMetaObject.connectSlotsByName(AECConnectivitySettingsView)
    # setupUi

    def retranslateUi(self, AECConnectivitySettingsView):
        AECConnectivitySettingsView.setWindowTitle(QCoreApplication.translate("AECConnectivitySettingsView", u"Form", None))
        self.epochs_label.setText(QCoreApplication.translate("AECConnectivitySettingsView", u"epochs", None))
        self.events_label.setText(QCoreApplication.translate("AECConnectivitySettingsView", u"events", None))
    # retranslateUi

