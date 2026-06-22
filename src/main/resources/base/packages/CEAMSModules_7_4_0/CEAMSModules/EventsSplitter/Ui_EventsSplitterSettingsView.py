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

class Ui_EventsSplitterSettingsView(object):
    def setupUi(self, EventsSplitterSettingsView):
        if not EventsSplitterSettingsView.objectName():
            EventsSplitterSettingsView.setObjectName(u"EventsSplitterSettingsView")
        EventsSplitterSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(EventsSplitterSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.events_horizontalLayout = QHBoxLayout()
        self.events_horizontalLayout.setObjectName(u"events_horizontalLayout")

        self.verticalLayout.addLayout(self.events_horizontalLayout)

        self.max_length_s_horizontalLayout = QHBoxLayout()
        self.max_length_s_horizontalLayout.setObjectName(u"max_length_s_horizontalLayout")
        self.max_length_s_label = QLabel(EventsSplitterSettingsView)
        self.max_length_s_label.setObjectName(u"max_length_s_label")

        self.max_length_s_horizontalLayout.addWidget(self.max_length_s_label)

        self.max_length_s_lineedit = QLineEdit(EventsSplitterSettingsView)
        self.max_length_s_lineedit.setObjectName(u"max_length_s_lineedit")

        self.max_length_s_horizontalLayout.addWidget(self.max_length_s_lineedit)


        self.verticalLayout.addLayout(self.max_length_s_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(EventsSplitterSettingsView)

        QMetaObject.connectSlotsByName(EventsSplitterSettingsView)
    # setupUi

    def retranslateUi(self, EventsSplitterSettingsView):
        EventsSplitterSettingsView.setWindowTitle(QCoreApplication.translate("EventsSplitterSettingsView", u"Form", None))
        self.max_length_s_label.setText(QCoreApplication.translate("EventsSplitterSettingsView", u"max_length_s", None))
    # retranslateUi

