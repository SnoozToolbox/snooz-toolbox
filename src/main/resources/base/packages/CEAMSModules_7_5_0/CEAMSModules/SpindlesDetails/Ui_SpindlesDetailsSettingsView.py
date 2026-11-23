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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_SpindlesDetailsSettingsView(object):
    def setupUi(self, SpindlesDetailsSettingsView):
        if not SpindlesDetailsSettingsView.objectName():
            SpindlesDetailsSettingsView.setObjectName(u"SpindlesDetailsSettingsView")
        SpindlesDetailsSettingsView.resize(794, 272)
        self.verticalLayout = QVBoxLayout(SpindlesDetailsSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(SpindlesDetailsSettingsView)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.details_filename_label = QLabel(SpindlesDetailsSettingsView)
        self.details_filename_label.setObjectName(u"details_filename_label")

        self.horizontalLayout.addWidget(self.details_filename_label)

        self.details_filename_lineedit = QLineEdit(SpindlesDetailsSettingsView)
        self.details_filename_lineedit.setObjectName(u"details_filename_lineedit")
        self.details_filename_lineedit.setMinimumSize(QSize(340, 0))
        self.details_filename_lineedit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.details_filename_lineedit)

        self.pushButton_browse = QPushButton(SpindlesDetailsSettingsView)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.horizontalLayout.addWidget(self.pushButton_browse)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SpindlesDetailsSettingsView)
        self.pushButton_browse.clicked.connect(SpindlesDetailsSettingsView.browse_slot)

        QMetaObject.connectSlotsByName(SpindlesDetailsSettingsView)
    # setupUi

    def retranslateUi(self, SpindlesDetailsSettingsView):
        SpindlesDetailsSettingsView.setWindowTitle(QCoreApplication.translate("SpindlesDetailsSettingsView", u"Form", None))
        self.label.setText(QCoreApplication.translate("SpindlesDetailsSettingsView", u"Spindle event details Settings View", None))
        self.details_filename_label.setText(QCoreApplication.translate("SpindlesDetailsSettingsView", u"Spindle events details filename", None))
        self.details_filename_lineedit.setPlaceholderText(QCoreApplication.translate("SpindlesDetailsSettingsView", u"Choose the filename to save the spindle events details...", None))
        self.pushButton_browse.setText(QCoreApplication.translate("SpindlesDetailsSettingsView", u"Browse", None))
    # retranslateUi

