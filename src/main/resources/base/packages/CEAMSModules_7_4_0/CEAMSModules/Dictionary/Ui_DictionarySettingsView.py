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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_DictionarySettingsView(object):
    def setupUi(self, DictionarySettingsView):
        if not DictionarySettingsView.objectName():
            DictionarySettingsView.setObjectName(u"DictionarySettingsView")
        DictionarySettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(DictionarySettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.key_horizontalLayout = QHBoxLayout()
        self.key_horizontalLayout.setObjectName(u"key_horizontalLayout")
        self.key_label = QLabel(DictionarySettingsView)
        self.key_label.setObjectName(u"key_label")

        self.key_horizontalLayout.addWidget(self.key_label)

        self.key_lineedit = QLineEdit(DictionarySettingsView)
        self.key_lineedit.setObjectName(u"key_lineedit")

        self.key_horizontalLayout.addWidget(self.key_lineedit)


        self.verticalLayout.addLayout(self.key_horizontalLayout)

        self.dictionary_horizontalLayout = QHBoxLayout()
        self.dictionary_horizontalLayout.setObjectName(u"dictionary_horizontalLayout")
        self.dictionary_label = QLabel(DictionarySettingsView)
        self.dictionary_label.setObjectName(u"dictionary_label")

        self.dictionary_horizontalLayout.addWidget(self.dictionary_label)

        self.dictionary_lineedit = QLineEdit(DictionarySettingsView)
        self.dictionary_lineedit.setObjectName(u"dictionary_lineedit")

        self.dictionary_horizontalLayout.addWidget(self.dictionary_lineedit)


        self.verticalLayout.addLayout(self.dictionary_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(DictionarySettingsView)

        QMetaObject.connectSlotsByName(DictionarySettingsView)
    # setupUi

    def retranslateUi(self, DictionarySettingsView):
        DictionarySettingsView.setWindowTitle(QCoreApplication.translate("DictionarySettingsView", u"Form", None))
        self.key_label.setText(QCoreApplication.translate("DictionarySettingsView", u"key", None))
        self.dictionary_label.setText(QCoreApplication.translate("DictionarySettingsView", u"dictionary", None))
    # retranslateUi

