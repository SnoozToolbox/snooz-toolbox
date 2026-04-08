# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_CreateDictSettingsView.ui'
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

class Ui_CreateDictSettingsView(object):
    def setupUi(self, CreateDictSettingsView):
        if not CreateDictSettingsView.objectName():
            CreateDictSettingsView.setObjectName(u"CreateDictSettingsView")
        CreateDictSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        CreateDictSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(CreateDictSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Key_horizontalLayout = QHBoxLayout()
        self.Key_horizontalLayout.setObjectName(u"Key_horizontalLayout")
        self.Key_label = QLabel(CreateDictSettingsView)
        self.Key_label.setObjectName(u"Key_label")

        self.Key_horizontalLayout.addWidget(self.Key_label)

        self.Key_lineedit = QLineEdit(CreateDictSettingsView)
        self.Key_lineedit.setObjectName(u"Key_lineedit")

        self.Key_horizontalLayout.addWidget(self.Key_lineedit)


        self.verticalLayout.addLayout(self.Key_horizontalLayout)

        self.Value_horizontalLayout = QHBoxLayout()
        self.Value_horizontalLayout.setObjectName(u"Value_horizontalLayout")
        self.Value_label = QLabel(CreateDictSettingsView)
        self.Value_label.setObjectName(u"Value_label")

        self.Value_horizontalLayout.addWidget(self.Value_label)

        self.Value_lineedit = QLineEdit(CreateDictSettingsView)
        self.Value_lineedit.setObjectName(u"Value_lineedit")

        self.Value_horizontalLayout.addWidget(self.Value_lineedit)


        self.verticalLayout.addLayout(self.Value_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(CreateDictSettingsView)

        QMetaObject.connectSlotsByName(CreateDictSettingsView)
    # setupUi

    def retranslateUi(self, CreateDictSettingsView):
        CreateDictSettingsView.setWindowTitle(QCoreApplication.translate("CreateDictSettingsView", u"Form", None))
        self.Key_label.setText(QCoreApplication.translate("CreateDictSettingsView", u"Key", None))
        self.Value_label.setText(QCoreApplication.translate("CreateDictSettingsView", u"Value", None))
    # retranslateUi

