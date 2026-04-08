# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SlowWaveAlignment.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_SlowWaveAlignment(object):
    def setupUi(self, SlowWaveAlignment):
        if not SlowWaveAlignment.objectName():
            SlowWaveAlignment.setObjectName(u"SlowWaveAlignment")
        SlowWaveAlignment.resize(699, 617)
        self.verticalLayout_2 = QVBoxLayout(SlowWaveAlignment)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(SlowWaveAlignment)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label = QLabel(SlowWaveAlignment)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.radioButton_zc = QRadioButton(SlowWaveAlignment)
        self.radioButton_zc.setObjectName(u"radioButton_zc")
        self.radioButton_zc.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_zc)

        self.radioButton_np = QRadioButton(SlowWaveAlignment)
        self.radioButton_np.setObjectName(u"radioButton_np")

        self.verticalLayout.addWidget(self.radioButton_np)

        self.radioButton_pp = QRadioButton(SlowWaveAlignment)
        self.radioButton_pp.setObjectName(u"radioButton_pp")

        self.verticalLayout.addWidget(self.radioButton_pp)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(SlowWaveAlignment)
        self.label_7.setObjectName(u"label_7")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.label_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setLineWidth(0)
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setMargin(0)
        self.label_7.setIndent(0)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.horizontalSpacer_5 = QSpacerItem(144, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 166, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(SlowWaveAlignment)

        QMetaObject.connectSlotsByName(SlowWaveAlignment)
    # setupUi

    def retranslateUi(self, SlowWaveAlignment):
        SlowWaveAlignment.setWindowTitle(QCoreApplication.translate("SlowWaveAlignment", u"SlowWaveAlignment", None))
        self.label_6.setText(QCoreApplication.translate("SlowWaveAlignment", u"<html><head/><body><p><span style=\" font-weight:600;\">Slow wave alignment reference</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("SlowWaveAlignment", u"This page allows you to define how the slow-wave curves are aligned with each other for display.", None))
        self.radioButton_zc.setText(QCoreApplication.translate("SlowWaveAlignment", u"Zero-crossing point (ZC)", None))
        self.radioButton_np.setText(QCoreApplication.translate("SlowWaveAlignment", u"Negative peak (NP)", None))
        self.radioButton_pp.setText(QCoreApplication.translate("SlowWaveAlignment", u"Positive peak (PP)", None))
        self.label_7.setText("")
    # retranslateUi

