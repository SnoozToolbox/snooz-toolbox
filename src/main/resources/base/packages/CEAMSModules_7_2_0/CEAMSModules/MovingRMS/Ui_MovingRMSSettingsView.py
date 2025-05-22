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

class Ui_MovingRMSSettingsView(object):
    def setupUi(self, MovingRMSSettingsView):
        if not MovingRMSSettingsView.objectName():
            MovingRMSSettingsView.setObjectName(u"MovingRMSSettingsView")
        MovingRMSSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(MovingRMSSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signals_horizontalLayout = QHBoxLayout()
        self.signals_horizontalLayout.setObjectName(u"signals_horizontalLayout")

        self.verticalLayout.addLayout(self.signals_horizontalLayout)

        self.win_len_sec_horizontalLayout = QHBoxLayout()
        self.win_len_sec_horizontalLayout.setObjectName(u"win_len_sec_horizontalLayout")
        self.win_len_sec_label = QLabel(MovingRMSSettingsView)
        self.win_len_sec_label.setObjectName(u"win_len_sec_label")
        self.win_len_sec_label.setMinimumSize(QSize(105, 0))

        self.win_len_sec_horizontalLayout.addWidget(self.win_len_sec_label)

        self.win_len_sec_lineedit = QLineEdit(MovingRMSSettingsView)
        self.win_len_sec_lineedit.setObjectName(u"win_len_sec_lineedit")

        self.win_len_sec_horizontalLayout.addWidget(self.win_len_sec_lineedit)


        self.verticalLayout.addLayout(self.win_len_sec_horizontalLayout)

        self.win_step_sec_horizontalLayout = QHBoxLayout()
        self.win_step_sec_horizontalLayout.setObjectName(u"win_step_sec_horizontalLayout")
        self.win_step_sec_label = QLabel(MovingRMSSettingsView)
        self.win_step_sec_label.setObjectName(u"win_step_sec_label")
        self.win_step_sec_label.setMinimumSize(QSize(105, 0))

        self.win_step_sec_horizontalLayout.addWidget(self.win_step_sec_label)

        self.win_step_sec_lineedit = QLineEdit(MovingRMSSettingsView)
        self.win_step_sec_lineedit.setObjectName(u"win_step_sec_lineedit")

        self.win_step_sec_horizontalLayout.addWidget(self.win_step_sec_lineedit)


        self.verticalLayout.addLayout(self.win_step_sec_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(MovingRMSSettingsView)

        QMetaObject.connectSlotsByName(MovingRMSSettingsView)
    # setupUi

    def retranslateUi(self, MovingRMSSettingsView):
        MovingRMSSettingsView.setWindowTitle(QCoreApplication.translate("MovingRMSSettingsView", u"Form", None))
        self.win_len_sec_label.setText(QCoreApplication.translate("MovingRMSSettingsView", u"Window length (sec)", None))
        self.win_step_sec_label.setText(QCoreApplication.translate("MovingRMSSettingsView", u"Window step (sec)", None))
    # retranslateUi

