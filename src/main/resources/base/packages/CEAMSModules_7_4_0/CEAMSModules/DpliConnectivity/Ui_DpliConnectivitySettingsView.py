# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DpliConnectivitySettingsView.ui'
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

class Ui_DpliConnectivitySettingsView(object):
    def setupUi(self, DpliConnectivitySettingsView):
        if not DpliConnectivitySettingsView.objectName():
            DpliConnectivitySettingsView.setObjectName(u"DpliConnectivitySettingsView")
        DpliConnectivitySettingsView.resize(711, 333)
        DpliConnectivitySettingsView.setStyleSheet(u"font: 10pt \"Roboto-Regular\";")
        self.verticalLayout = QVBoxLayout(DpliConnectivitySettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signals_horizontalLayout = QHBoxLayout()
        self.signals_horizontalLayout.setObjectName(u"signals_horizontalLayout")
        self.epochs_label = QLabel(DpliConnectivitySettingsView)
        self.epochs_label.setObjectName(u"epochs_label")

        self.signals_horizontalLayout.addWidget(self.epochs_label)

        self.epochs_lineedit = QLineEdit(DpliConnectivitySettingsView)
        self.epochs_lineedit.setObjectName(u"epochs_lineedit")

        self.signals_horizontalLayout.addWidget(self.epochs_lineedit)


        self.verticalLayout.addLayout(self.signals_horizontalLayout)

        self.events_horizontalLayout = QHBoxLayout()
        self.events_horizontalLayout.setObjectName(u"events_horizontalLayout")
        self.events_label = QLabel(DpliConnectivitySettingsView)
        self.events_label.setObjectName(u"events_label")

        self.events_horizontalLayout.addWidget(self.events_label)

        self.events_lineedit = QLineEdit(DpliConnectivitySettingsView)
        self.events_lineedit.setObjectName(u"events_lineedit")

        self.events_horizontalLayout.addWidget(self.events_lineedit)


        self.verticalLayout.addLayout(self.events_horizontalLayout)

        self.num_surr_horizontalLayout = QHBoxLayout()
        self.num_surr_horizontalLayout.setObjectName(u"num_surr_horizontalLayout")
        self.num_surr_label = QLabel(DpliConnectivitySettingsView)
        self.num_surr_label.setObjectName(u"num_surr_label")

        self.num_surr_horizontalLayout.addWidget(self.num_surr_label)

        self.num_surr_lineedit = QLineEdit(DpliConnectivitySettingsView)
        self.num_surr_lineedit.setObjectName(u"num_surr_lineedit")

        self.num_surr_horizontalLayout.addWidget(self.num_surr_lineedit)


        self.verticalLayout.addLayout(self.num_surr_horizontalLayout)

        self.p_value_horizontalLayout = QHBoxLayout()
        self.p_value_horizontalLayout.setObjectName(u"p_value_horizontalLayout")
        self.p_value_label = QLabel(DpliConnectivitySettingsView)
        self.p_value_label.setObjectName(u"p_value_label")

        self.p_value_horizontalLayout.addWidget(self.p_value_label)

        self.p_value_lineedit = QLineEdit(DpliConnectivitySettingsView)
        self.p_value_lineedit.setObjectName(u"p_value_lineedit")

        self.p_value_horizontalLayout.addWidget(self.p_value_lineedit)


        self.verticalLayout.addLayout(self.p_value_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(DpliConnectivitySettingsView)

        QMetaObject.connectSlotsByName(DpliConnectivitySettingsView)
    # setupUi

    def retranslateUi(self, DpliConnectivitySettingsView):
        DpliConnectivitySettingsView.setWindowTitle(QCoreApplication.translate("DpliConnectivitySettingsView", u"Form", None))
        self.epochs_label.setText(QCoreApplication.translate("DpliConnectivitySettingsView", u"epochs", None))
        self.events_label.setText(QCoreApplication.translate("DpliConnectivitySettingsView", u"events", None))
        self.num_surr_label.setText(QCoreApplication.translate("DpliConnectivitySettingsView", u"num_surr", None))
        self.p_value_label.setText(QCoreApplication.translate("DpliConnectivitySettingsView", u"p_value", None))
    # retranslateUi

