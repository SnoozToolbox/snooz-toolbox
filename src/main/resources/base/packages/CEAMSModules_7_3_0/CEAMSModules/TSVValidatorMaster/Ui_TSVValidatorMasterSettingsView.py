# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_TSVValidatorMasterSettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_TSVValidatorMasterSettingsView(object):
    def setupUi(self, TSVValidatorMasterSettingsView):
        if not TSVValidatorMasterSettingsView.objectName():
            TSVValidatorMasterSettingsView.setObjectName(u"TSVValidatorMasterSettingsView")
        TSVValidatorMasterSettingsView.resize(711, 333)
        TSVValidatorMasterSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(TSVValidatorMasterSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(TSVValidatorMasterSettingsView)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.frame = QFrame(TSVValidatorMasterSettingsView)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(TSVValidatorMasterSettingsView)

        QMetaObject.connectSlotsByName(TSVValidatorMasterSettingsView)
    # setupUi

    def retranslateUi(self, TSVValidatorMasterSettingsView):
        TSVValidatorMasterSettingsView.setWindowTitle(QCoreApplication.translate("TSVValidatorMasterSettingsView", u"Form", None))
        self.pushButton_2.setText(QCoreApplication.translate("TSVValidatorMasterSettingsView", u"Clear", None))
        self.pushButton.setText(QCoreApplication.translate("TSVValidatorMasterSettingsView", u"Choose", None))
    # retranslateUi

