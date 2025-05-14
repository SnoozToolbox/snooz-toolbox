# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_CreateListofGroupNameSettingsView.ui'
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

class Ui_CreateListofGroupNameSettingsView(object):
    def setupUi(self, CreateListofGroupNameSettingsView):
        if not CreateListofGroupNameSettingsView.objectName():
            CreateListofGroupNameSettingsView.setObjectName(u"CreateListofGroupNameSettingsView")
        CreateListofGroupNameSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        CreateListofGroupNameSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(CreateListofGroupNameSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.events_horizontalLayout = QHBoxLayout()
        self.events_horizontalLayout.setObjectName(u"events_horizontalLayout")
        self.events_label = QLabel(CreateListofGroupNameSettingsView)
        self.events_label.setObjectName(u"events_label")

        self.events_horizontalLayout.addWidget(self.events_label)

        self.events_lineedit = QLineEdit(CreateListofGroupNameSettingsView)
        self.events_lineedit.setObjectName(u"events_lineedit")

        self.events_horizontalLayout.addWidget(self.events_lineedit)


        self.verticalLayout.addLayout(self.events_horizontalLayout)

        self.group_horizontalLayout = QHBoxLayout()
        self.group_horizontalLayout.setObjectName(u"group_horizontalLayout")
        self.group_label = QLabel(CreateListofGroupNameSettingsView)
        self.group_label.setObjectName(u"group_label")

        self.group_horizontalLayout.addWidget(self.group_label)

        self.group_lineedit = QLineEdit(CreateListofGroupNameSettingsView)
        self.group_lineedit.setObjectName(u"group_lineedit")

        self.group_horizontalLayout.addWidget(self.group_lineedit)


        self.verticalLayout.addLayout(self.group_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(CreateListofGroupNameSettingsView)

        QMetaObject.connectSlotsByName(CreateListofGroupNameSettingsView)
    # setupUi

    def retranslateUi(self, CreateListofGroupNameSettingsView):
        CreateListofGroupNameSettingsView.setWindowTitle(QCoreApplication.translate("CreateListofGroupNameSettingsView", u"Form", None))
        self.events_label.setText(QCoreApplication.translate("CreateListofGroupNameSettingsView", u"events", None))
        self.group_label.setText(QCoreApplication.translate("CreateListofGroupNameSettingsView", u"group", None))
    # retranslateUi

