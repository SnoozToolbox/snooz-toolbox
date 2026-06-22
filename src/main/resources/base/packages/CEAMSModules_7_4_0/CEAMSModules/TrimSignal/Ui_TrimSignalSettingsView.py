# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_TrimSignalSettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_TrimSignalSettingsView(object):
    def setupUi(self, TrimSignalSettingsView):
        if not TrimSignalSettingsView.objectName():
            TrimSignalSettingsView.setObjectName(u"TrimSignalSettingsView")
        TrimSignalSettingsView.resize(711, 333)
        TrimSignalSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(TrimSignalSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.start_sec_horizontalLayout = QHBoxLayout()
        self.start_sec_horizontalLayout.setObjectName(u"start_sec_horizontalLayout")
        self.start_sec_label = QLabel(TrimSignalSettingsView)
        self.start_sec_label.setObjectName(u"start_sec_label")

        self.start_sec_horizontalLayout.addWidget(self.start_sec_label)

        self.start_sec_lineedit = QLineEdit(TrimSignalSettingsView)
        self.start_sec_lineedit.setObjectName(u"start_sec_lineedit")

        self.start_sec_horizontalLayout.addWidget(self.start_sec_lineedit)


        self.verticalLayout.addLayout(self.start_sec_horizontalLayout)

        self.duration_sec_horizontalLayout = QHBoxLayout()
        self.duration_sec_horizontalLayout.setObjectName(u"duration_sec_horizontalLayout")
        self.duration_sec_label = QLabel(TrimSignalSettingsView)
        self.duration_sec_label.setObjectName(u"duration_sec_label")

        self.duration_sec_horizontalLayout.addWidget(self.duration_sec_label)

        self.duration_sec_lineedit = QLineEdit(TrimSignalSettingsView)
        self.duration_sec_lineedit.setObjectName(u"duration_sec_lineedit")

        self.duration_sec_horizontalLayout.addWidget(self.duration_sec_lineedit)


        self.verticalLayout.addLayout(self.duration_sec_horizontalLayout)

        self.reset_time_horizontalLayout = QHBoxLayout()
        self.reset_time_horizontalLayout.setObjectName(u"reset_time_horizontalLayout")
        self.checkBox = QCheckBox(TrimSignalSettingsView)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.reset_time_horizontalLayout.addWidget(self.checkBox)


        self.verticalLayout.addLayout(self.reset_time_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(TrimSignalSettingsView)

        QMetaObject.connectSlotsByName(TrimSignalSettingsView)
    # setupUi

    def retranslateUi(self, TrimSignalSettingsView):
        TrimSignalSettingsView.setWindowTitle(QCoreApplication.translate("TrimSignalSettingsView", u"Form", None))
        self.start_sec_label.setText(QCoreApplication.translate("TrimSignalSettingsView", u"start_sec", None))
        self.duration_sec_label.setText(QCoreApplication.translate("TrimSignalSettingsView", u"duration_sec", None))
        self.checkBox.setText(QCoreApplication.translate("TrimSignalSettingsView", u"reset_time", None))
    # retranslateUi

