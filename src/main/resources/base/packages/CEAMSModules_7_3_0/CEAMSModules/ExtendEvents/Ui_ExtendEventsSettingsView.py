# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ExtendEventsSettingsView.ui'
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

class Ui_ExtendEventsSettingsView(object):
    def setupUi(self, ExtendEventsSettingsView):
        if not ExtendEventsSettingsView.objectName():
            ExtendEventsSettingsView.setObjectName(u"ExtendEventsSettingsView")
        ExtendEventsSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        ExtendEventsSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(ExtendEventsSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.events_horizontalLayout = QHBoxLayout()
        self.events_horizontalLayout.setObjectName(u"events_horizontalLayout")
        self.events_label = QLabel(ExtendEventsSettingsView)
        self.events_label.setObjectName(u"events_label")

        self.events_horizontalLayout.addWidget(self.events_label)

        self.events_lineedit = QLineEdit(ExtendEventsSettingsView)
        self.events_lineedit.setObjectName(u"events_lineedit")

        self.events_horizontalLayout.addWidget(self.events_lineedit)


        self.verticalLayout.addLayout(self.events_horizontalLayout)

        self.per_side_exten_percent_horizontalLayout = QHBoxLayout()
        self.per_side_exten_percent_horizontalLayout.setObjectName(u"per_side_exten_percent_horizontalLayout")
        self.per_side_exten_percent_label = QLabel(ExtendEventsSettingsView)
        self.per_side_exten_percent_label.setObjectName(u"per_side_exten_percent_label")

        self.per_side_exten_percent_horizontalLayout.addWidget(self.per_side_exten_percent_label)

        self.per_side_exten_percent_lineedit = QLineEdit(ExtendEventsSettingsView)
        self.per_side_exten_percent_lineedit.setObjectName(u"per_side_exten_percent_lineedit")

        self.per_side_exten_percent_horizontalLayout.addWidget(self.per_side_exten_percent_lineedit)


        self.verticalLayout.addLayout(self.per_side_exten_percent_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ExtendEventsSettingsView)

        QMetaObject.connectSlotsByName(ExtendEventsSettingsView)
    # setupUi

    def retranslateUi(self, ExtendEventsSettingsView):
        ExtendEventsSettingsView.setWindowTitle(QCoreApplication.translate("ExtendEventsSettingsView", u"Form", None))
        self.events_label.setText(QCoreApplication.translate("ExtendEventsSettingsView", u"events", None))
        self.per_side_exten_percent_label.setText(QCoreApplication.translate("ExtendEventsSettingsView", u"per_side_exten_percent", None))
    # retranslateUi

