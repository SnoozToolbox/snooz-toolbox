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

class Ui_SignalsFromEventsSettingsView(object):
    def setupUi(self, SignalsFromEventsSettingsView):
        if not SignalsFromEventsSettingsView.objectName():
            SignalsFromEventsSettingsView.setObjectName(u"SignalsFromEventsSettingsView")
        SignalsFromEventsSettingsView.resize(272, 137)
        self.horizontalLayout_2 = QHBoxLayout(SignalsFromEventsSettingsView)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(SignalsFromEventsSettingsView)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(SignalsFromEventsSettingsView)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.events_names_lineEdit = QLineEdit(SignalsFromEventsSettingsView)
        self.events_names_lineEdit.setObjectName(u"events_names_lineEdit")

        self.horizontalLayout.addWidget(self.events_names_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(45, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.retranslateUi(SignalsFromEventsSettingsView)

        QMetaObject.connectSlotsByName(SignalsFromEventsSettingsView)
    # setupUi

    def retranslateUi(self, SignalsFromEventsSettingsView):
        SignalsFromEventsSettingsView.setWindowTitle(QCoreApplication.translate("SignalsFromEventsSettingsView", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("SignalsFromEventsSettingsView", u"SignalsFromEvents settings", None))
        self.label.setText(QCoreApplication.translate("SignalsFromEventsSettingsView", u"Event name", None))
#if QT_CONFIG(tooltip)
        self.events_names_lineEdit.setToolTip(QCoreApplication.translate("SignalsFromEventsSettingsView", u"String of the desired events to take in account. Separated by a comma without spaces. An empty string will take every events in the dataframe.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

