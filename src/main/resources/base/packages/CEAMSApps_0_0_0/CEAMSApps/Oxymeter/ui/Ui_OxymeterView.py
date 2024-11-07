# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_OxymeterView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from CEAMSApps.Oxymeter.OxymeterDrawArea import OxymeterDrawArea


class Ui_OxymeterView(object):
    def setupUi(self, OxymeterView):
        if not OxymeterView.objectName():
            OxymeterView.setObjectName(u"OxymeterView")
        OxymeterView.resize(815, 496)
        self.verticalLayout = QVBoxLayout(OxymeterView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(OxymeterView)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.ymin_comboBox = QComboBox(OxymeterView)
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

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.oxymeter_draw_area = OxymeterDrawArea(OxymeterView)
        self.oxymeter_draw_area.setObjectName(u"oxymeter_draw_area")

        self.verticalLayout.addWidget(self.oxymeter_draw_area)

        self.label_2 = QLabel(OxymeterView)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.line = QFrame(OxymeterView)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(OxymeterView)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.remove_new_pushButton = QPushButton(OxymeterView)
        self.remove_new_pushButton.setObjectName(u"remove_new_pushButton")

        self.horizontalLayout.addWidget(self.remove_new_pushButton)

        self.remove_all_pushButton = QPushButton(OxymeterView)
        self.remove_all_pushButton.setObjectName(u"remove_all_pushButton")

        self.horizontalLayout.addWidget(self.remove_all_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(OxymeterView)
        self.remove_all_pushButton.clicked.connect(OxymeterView.remove_all_clicked)
        self.remove_new_pushButton.clicked.connect(OxymeterView.remove_new_clicked)
        self.ymin_comboBox.currentTextChanged.connect(OxymeterView.min_saturation_change)

        QMetaObject.connectSlotsByName(OxymeterView)
    # setupUi

    def retranslateUi(self, OxymeterView):
        OxymeterView.setWindowTitle(QCoreApplication.translate("OxymeterView", u"Form", None))
        self.label.setText(QCoreApplication.translate("OxymeterView", u"Min. Saturation (%)", None))
        self.ymin_comboBox.setItemText(0, QCoreApplication.translate("OxymeterView", u"0", None))
        self.ymin_comboBox.setItemText(1, QCoreApplication.translate("OxymeterView", u"10", None))
        self.ymin_comboBox.setItemText(2, QCoreApplication.translate("OxymeterView", u"20", None))
        self.ymin_comboBox.setItemText(3, QCoreApplication.translate("OxymeterView", u"30", None))
        self.ymin_comboBox.setItemText(4, QCoreApplication.translate("OxymeterView", u"40", None))
        self.ymin_comboBox.setItemText(5, QCoreApplication.translate("OxymeterView", u"50", None))
        self.ymin_comboBox.setItemText(6, QCoreApplication.translate("OxymeterView", u"60", None))
        self.ymin_comboBox.setItemText(7, QCoreApplication.translate("OxymeterView", u"70", None))
        self.ymin_comboBox.setItemText(8, QCoreApplication.translate("OxymeterView", u"80", None))
        self.ymin_comboBox.setItemText(9, QCoreApplication.translate("OxymeterView", u"90", None))

        self.label_2.setText(QCoreApplication.translate("OxymeterView", u"(Note: Gray sections represent discontinuities in the signal.)", None))
        self.label_3.setText(QCoreApplication.translate("OxymeterView", u"Left-click and drag to select invalid sections.", None))
#if QT_CONFIG(tooltip)
        self.remove_new_pushButton.setToolTip(QCoreApplication.translate("OxymeterView", u"Remove all new selections, keep the ones that we already saved.", None))
#endif // QT_CONFIG(tooltip)
        self.remove_new_pushButton.setText(QCoreApplication.translate("OxymeterView", u"Remove new selections", None))
#if QT_CONFIG(tooltip)
        self.remove_all_pushButton.setToolTip(QCoreApplication.translate("OxymeterView", u"Remove all selections, including the ones that we already saved.", None))
#endif // QT_CONFIG(tooltip)
        self.remove_all_pushButton.setText(QCoreApplication.translate("OxymeterView", u"Remove all selections", None))
    # retranslateUi

