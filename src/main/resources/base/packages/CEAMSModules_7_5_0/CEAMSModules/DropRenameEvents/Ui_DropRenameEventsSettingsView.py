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

class Ui_DropRenameEventsSettingsView(object):
    def setupUi(self, DropRenameEventsSettingsView):
        if not DropRenameEventsSettingsView.objectName():
            DropRenameEventsSettingsView.setObjectName(u"DropRenameEventsSettingsView")
        DropRenameEventsSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(DropRenameEventsSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.events_horizontalLayout = QHBoxLayout()
        self.events_horizontalLayout.setObjectName(u"events_horizontalLayout")
        self.events_label = QLabel(DropRenameEventsSettingsView)
        self.events_label.setObjectName(u"events_label")

        self.events_horizontalLayout.addWidget(self.events_label)

        self.events_lineedit = QLineEdit(DropRenameEventsSettingsView)
        self.events_lineedit.setObjectName(u"events_lineedit")

        self.events_horizontalLayout.addWidget(self.events_lineedit)


        self.verticalLayout.addLayout(self.events_horizontalLayout)

        self.events_to_drop_horizontalLayout = QHBoxLayout()
        self.events_to_drop_horizontalLayout.setObjectName(u"events_to_drop_horizontalLayout")
        self.events_to_drop_label = QLabel(DropRenameEventsSettingsView)
        self.events_to_drop_label.setObjectName(u"events_to_drop_label")

        self.events_to_drop_horizontalLayout.addWidget(self.events_to_drop_label)

        self.events_to_drop_lineedit = QLineEdit(DropRenameEventsSettingsView)
        self.events_to_drop_lineedit.setObjectName(u"events_to_drop_lineedit")

        self.events_to_drop_horizontalLayout.addWidget(self.events_to_drop_lineedit)


        self.verticalLayout.addLayout(self.events_to_drop_horizontalLayout)

        self.event_to_rename_horizontalLayout = QHBoxLayout()
        self.event_to_rename_horizontalLayout.setObjectName(u"event_to_rename_horizontalLayout")
        self.event_to_rename_label = QLabel(DropRenameEventsSettingsView)
        self.event_to_rename_label.setObjectName(u"event_to_rename_label")

        self.event_to_rename_horizontalLayout.addWidget(self.event_to_rename_label)

        self.event_to_rename_lineedit = QLineEdit(DropRenameEventsSettingsView)
        self.event_to_rename_lineedit.setObjectName(u"event_to_rename_lineedit")

        self.event_to_rename_horizontalLayout.addWidget(self.event_to_rename_lineedit)


        self.verticalLayout.addLayout(self.event_to_rename_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(DropRenameEventsSettingsView)

        QMetaObject.connectSlotsByName(DropRenameEventsSettingsView)
    # setupUi

    def retranslateUi(self, DropRenameEventsSettingsView):
        DropRenameEventsSettingsView.setWindowTitle(QCoreApplication.translate("DropRenameEventsSettingsView", u"Form", None))
        self.events_label.setText(QCoreApplication.translate("DropRenameEventsSettingsView", u"events", None))
        self.events_to_drop_label.setText(QCoreApplication.translate("DropRenameEventsSettingsView", u"events_to_drop", None))
        self.event_to_rename_label.setText(QCoreApplication.translate("DropRenameEventsSettingsView", u"event_to_rename", None))
    # retranslateUi

