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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGroupBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ChannelSelection(object):
    def setupUi(self, ChannelSelection):
        if not ChannelSelection.objectName():
            ChannelSelection.setObjectName(u"ChannelSelection")
        ChannelSelection.resize(340, 233)
        self.verticalLayout = QVBoxLayout(ChannelSelection)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(ChannelSelection)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.groupBox_3 = QGroupBox(ChannelSelection)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.montages_comboBox = QComboBox(self.groupBox_3)
        self.montages_comboBox.setObjectName(u"montages_comboBox")

        self.horizontalLayout.addWidget(self.montages_comboBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(ChannelSelection)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.oxy_channel_comboBox = QComboBox(self.groupBox_4)
        self.oxy_channel_comboBox.setObjectName(u"oxy_channel_comboBox")

        self.horizontalLayout_2.addWidget(self.oxy_channel_comboBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(ChannelSelection)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ChannelSelection)
        self.buttonBox.accepted.connect(ChannelSelection.accept)
        self.buttonBox.rejected.connect(ChannelSelection.reject)

        QMetaObject.connectSlotsByName(ChannelSelection)
    # setupUi

    def retranslateUi(self, ChannelSelection):
        ChannelSelection.setWindowTitle(QCoreApplication.translate("ChannelSelection", u"Channels selection", None))
        self.label.setText(QCoreApplication.translate("ChannelSelection", u"Please select the oximeter channel", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ChannelSelection", u"Montage", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("ChannelSelection", u"Oximeter channel", None))
    # retranslateUi

