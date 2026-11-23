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

class Ui_WindowsToSamplesSettingsView(object):
    def setupUi(self, WindowsToSamplesSettingsView):
        if not WindowsToSamplesSettingsView.objectName():
            WindowsToSamplesSettingsView.setObjectName(u"WindowsToSamplesSettingsView")
        WindowsToSamplesSettingsView.resize(185, 161)
        self.verticalLayout = QVBoxLayout(WindowsToSamplesSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.windows_values_horizontalLayout = QHBoxLayout()
        self.windows_values_horizontalLayout.setObjectName(u"windows_values_horizontalLayout")

        self.verticalLayout.addLayout(self.windows_values_horizontalLayout)

        self.win_step_sec_horizontalLayout = QHBoxLayout()
        self.win_step_sec_horizontalLayout.setObjectName(u"win_step_sec_horizontalLayout")
        self.win_step_sec_label = QLabel(WindowsToSamplesSettingsView)
        self.win_step_sec_label.setObjectName(u"win_step_sec_label")

        self.win_step_sec_horizontalLayout.addWidget(self.win_step_sec_label)

        self.win_step_sec_lineedit = QLineEdit(WindowsToSamplesSettingsView)
        self.win_step_sec_lineedit.setObjectName(u"win_step_sec_lineedit")

        self.win_step_sec_horizontalLayout.addWidget(self.win_step_sec_lineedit)


        self.verticalLayout.addLayout(self.win_step_sec_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(WindowsToSamplesSettingsView)

        QMetaObject.connectSlotsByName(WindowsToSamplesSettingsView)
    # setupUi

    def retranslateUi(self, WindowsToSamplesSettingsView):
        WindowsToSamplesSettingsView.setWindowTitle(QCoreApplication.translate("WindowsToSamplesSettingsView", u"Form", None))
        self.win_step_sec_label.setText(QCoreApplication.translate("WindowsToSamplesSettingsView", u"win_step_sec", None))
    # retranslateUi

