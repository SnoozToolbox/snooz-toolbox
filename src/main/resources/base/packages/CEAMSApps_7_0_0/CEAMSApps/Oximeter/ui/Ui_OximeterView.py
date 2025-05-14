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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from CEAMSApps.Oximeter.OximeterDrawArea import OximeterDrawArea

class Ui_OximeterView(object):
    def setupUi(self, OximeterView):
        if not OximeterView.objectName():
            OximeterView.setObjectName(u"OximeterView")
        OximeterView.resize(815, 496)
        self.verticalLayout = QVBoxLayout(OximeterView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(OximeterView)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.ymin_comboBox = QComboBox(OximeterView)
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.setObjectName(u"ymin_comboBox")

        self.horizontalLayout_2.addWidget(self.ymin_comboBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.oximeter_draw_area = OximeterDrawArea(OximeterView)
        self.oximeter_draw_area.setObjectName(u"oximeter_draw_area")

        self.verticalLayout.addWidget(self.oximeter_draw_area)

        self.label_2 = QLabel(OximeterView)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.line = QFrame(OximeterView)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(OximeterView)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.remove_new_pushButton = QPushButton(OximeterView)
        self.remove_new_pushButton.setObjectName(u"remove_new_pushButton")

        self.horizontalLayout.addWidget(self.remove_new_pushButton)

        self.remove_all_pushButton = QPushButton(OximeterView)
        self.remove_all_pushButton.setObjectName(u"remove_all_pushButton")

        self.horizontalLayout.addWidget(self.remove_all_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(OximeterView)
        self.remove_all_pushButton.clicked.connect(OximeterView.remove_all_clicked)
        self.remove_new_pushButton.clicked.connect(OximeterView.remove_new_clicked)
        self.ymin_comboBox.currentTextChanged.connect(OximeterView.min_saturation_change)

        QMetaObject.connectSlotsByName(OximeterView)
    # setupUi

    def retranslateUi(self, OximeterView):
        OximeterView.setWindowTitle(QCoreApplication.translate("OximeterView", u"Form", None))
        self.label.setText(QCoreApplication.translate("OximeterView", u"Min. Saturation (%)", None))
        self.ymin_comboBox.setItemText(0, QCoreApplication.translate("OximeterView", u"0", None))
        self.ymin_comboBox.setItemText(1, QCoreApplication.translate("OximeterView", u"10", None))
        self.ymin_comboBox.setItemText(2, QCoreApplication.translate("OximeterView", u"20", None))
        self.ymin_comboBox.setItemText(3, QCoreApplication.translate("OximeterView", u"30", None))
        self.ymin_comboBox.setItemText(4, QCoreApplication.translate("OximeterView", u"40", None))
        self.ymin_comboBox.setItemText(5, QCoreApplication.translate("OximeterView", u"50", None))
        self.ymin_comboBox.setItemText(6, QCoreApplication.translate("OximeterView", u"60", None))
        self.ymin_comboBox.setItemText(7, QCoreApplication.translate("OximeterView", u"70", None))
        self.ymin_comboBox.setItemText(8, QCoreApplication.translate("OximeterView", u"80", None))
        self.ymin_comboBox.setItemText(9, QCoreApplication.translate("OximeterView", u"90", None))

        self.label_2.setText(QCoreApplication.translate("OximeterView", u"(Note: Gray sections represent discontinuities in the signal.)", None))
        self.label_3.setText(QCoreApplication.translate("OximeterView", u"Left-click and drag to select invalid sections.", None))
#if QT_CONFIG(tooltip)
        self.remove_new_pushButton.setToolTip(QCoreApplication.translate("OximeterView", u"Remove all new selections, keep the ones that we already saved.", None))
#endif // QT_CONFIG(tooltip)
        self.remove_new_pushButton.setText(QCoreApplication.translate("OximeterView", u"Remove new selections", None))
#if QT_CONFIG(tooltip)
        self.remove_all_pushButton.setToolTip(QCoreApplication.translate("OximeterView", u"Remove all selections, including the ones that we already saved.", None))
#endif // QT_CONFIG(tooltip)
        self.remove_all_pushButton.setText(QCoreApplication.translate("OximeterView", u"Remove all selections", None))
    # retranslateUi

