# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MontageSelection.ui'
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

class Ui_MontageSelection(object):
    def setupUi(self, MontageSelection):
        if not MontageSelection.objectName():
            MontageSelection.setObjectName(u"MontageSelection")
        MontageSelection.resize(340, 152)
        self.verticalLayout = QVBoxLayout(MontageSelection)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(MontageSelection)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.groupBox_3 = QGroupBox(MontageSelection)
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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(MontageSelection)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(MontageSelection)
        self.buttonBox.accepted.connect(MontageSelection.accept)
        self.buttonBox.rejected.connect(MontageSelection.reject)

        QMetaObject.connectSlotsByName(MontageSelection)
    # setupUi

    def retranslateUi(self, MontageSelection):
        MontageSelection.setWindowTitle(QCoreApplication.translate("MontageSelection", u"Montage selection", None))
        self.label.setText(QCoreApplication.translate("MontageSelection", u"Please select the desired montage", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MontageSelection", u"Montage", None))
    # retranslateUi

