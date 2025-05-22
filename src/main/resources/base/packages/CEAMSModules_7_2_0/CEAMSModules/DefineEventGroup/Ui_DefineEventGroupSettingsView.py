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

class Ui_DefineEventGroupSettingsView(object):
    def setupUi(self, DefineEventGroupSettingsView):
        if not DefineEventGroupSettingsView.objectName():
            DefineEventGroupSettingsView.setObjectName(u"DefineEventGroupSettingsView")
        DefineEventGroupSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(DefineEventGroupSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.events_horizontalLayout = QHBoxLayout()
        self.events_horizontalLayout.setObjectName(u"events_horizontalLayout")
        self.events_label = QLabel(DefineEventGroupSettingsView)
        self.events_label.setObjectName(u"events_label")

        self.events_horizontalLayout.addWidget(self.events_label)

        self.events_lineedit = QLineEdit(DefineEventGroupSettingsView)
        self.events_lineedit.setObjectName(u"events_lineedit")

        self.events_horizontalLayout.addWidget(self.events_lineedit)


        self.verticalLayout.addLayout(self.events_horizontalLayout)

        self.groups_horizontalLayout = QHBoxLayout()
        self.groups_horizontalLayout.setObjectName(u"groups_horizontalLayout")
        self.groups_label = QLabel(DefineEventGroupSettingsView)
        self.groups_label.setObjectName(u"groups_label")

        self.groups_horizontalLayout.addWidget(self.groups_label)

        self.groups_lineedit = QLineEdit(DefineEventGroupSettingsView)
        self.groups_lineedit.setObjectName(u"groups_lineedit")

        self.groups_horizontalLayout.addWidget(self.groups_lineedit)


        self.verticalLayout.addLayout(self.groups_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(DefineEventGroupSettingsView)

        QMetaObject.connectSlotsByName(DefineEventGroupSettingsView)
    # setupUi

    def retranslateUi(self, DefineEventGroupSettingsView):
        DefineEventGroupSettingsView.setWindowTitle(QCoreApplication.translate("DefineEventGroupSettingsView", u"Form", None))
        self.events_label.setText(QCoreApplication.translate("DefineEventGroupSettingsView", u"events", None))
        self.groups_label.setText(QCoreApplication.translate("DefineEventGroupSettingsView", u"groups", None))
    # retranslateUi

