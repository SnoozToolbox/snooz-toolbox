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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

from widgets.QLineEditLive import QLineEditLive

class Ui_EventCreatorSettingsView(object):
    def setupUi(self, EventCreatorSettingsView):
        if not EventCreatorSettingsView.objectName():
            EventCreatorSettingsView.setObjectName(u"EventCreatorSettingsView")
        EventCreatorSettingsView.resize(415, 224)
        self.widget = QWidget(EventCreatorSettingsView)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 12, 208, 162))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setBold(True)
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 2)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.event_name_lineedit = QLineEditLive(self.widget)
        self.event_name_lineedit.setObjectName(u"event_name_lineedit")

        self.gridLayout.addWidget(self.event_name_lineedit, 1, 1, 1, 1)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.start_time_lineedit = QLineEditLive(self.widget)
        self.start_time_lineedit.setObjectName(u"start_time_lineedit")

        self.gridLayout.addWidget(self.start_time_lineedit, 2, 1, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)

        self.duration_lineedit = QLineEditLive(self.widget)
        self.duration_lineedit.setObjectName(u"duration_lineedit")

        self.gridLayout.addWidget(self.duration_lineedit, 3, 1, 1, 1)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)

        self.group_name_lineedit = QLineEditLive(self.widget)
        self.group_name_lineedit.setObjectName(u"group_name_lineedit")

        self.gridLayout.addWidget(self.group_name_lineedit, 4, 1, 1, 1)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)

        self.channels_lineedit = QLineEditLive(self.widget)
        self.channels_lineedit.setObjectName(u"channels_lineedit")

        self.gridLayout.addWidget(self.channels_lineedit, 5, 1, 1, 1)


        self.retranslateUi(EventCreatorSettingsView)

        QMetaObject.connectSlotsByName(EventCreatorSettingsView)
    # setupUi

    def retranslateUi(self, EventCreatorSettingsView):
        EventCreatorSettingsView.setWindowTitle(QCoreApplication.translate("EventCreatorSettingsView", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("EventCreatorSettingsView", u"EventCreator settings", None))
        self.label_9.setText(QCoreApplication.translate("EventCreatorSettingsView", u"Event name", None))
        self.label_10.setText(QCoreApplication.translate("EventCreatorSettingsView", u"Start time", None))
        self.label_11.setText(QCoreApplication.translate("EventCreatorSettingsView", u"Duration", None))
        self.label_12.setText(QCoreApplication.translate("EventCreatorSettingsView", u"Group name", None))
        self.label_13.setText(QCoreApplication.translate("EventCreatorSettingsView", u"Channels", None))
#if QT_CONFIG(tooltip)
        self.channels_lineedit.setToolTip(QCoreApplication.translate("EventCreatorSettingsView", u"Space separated list of channels", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

