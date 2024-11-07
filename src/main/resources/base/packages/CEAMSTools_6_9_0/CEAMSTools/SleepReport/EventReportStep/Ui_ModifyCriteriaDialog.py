# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ModifyCriteriaDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_ModifyCriteriaDialog(object):
    def setupUi(self, ModifyCriteriaDialog):
        if not ModifyCriteriaDialog.objectName():
            ModifyCriteriaDialog.setObjectName(u"ModifyCriteriaDialog")
        ModifyCriteriaDialog.resize(400, 388)
        self.verticalLayout = QVBoxLayout(ModifyCriteriaDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(ModifyCriteriaDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(ModifyCriteriaDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_3 = QLabel(ModifyCriteriaDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_4 = QLabel(ModifyCriteriaDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_5 = QLabel(ModifyCriteriaDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_6 = QLabel(ModifyCriteriaDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)

        self.label_7 = QLabel(ModifyCriteriaDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)

        self.label_8 = QLabel(ModifyCriteriaDialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)

        self.label_9 = QLabel(ModifyCriteriaDialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 10, 0, 1, 1)

        self.events_in_combobox = QComboBox(ModifyCriteriaDialog)
        self.events_in_combobox.addItem("")
        self.events_in_combobox.addItem("")
        self.events_in_combobox.addItem("")
        self.events_in_combobox.addItem("")
        self.events_in_combobox.setObjectName(u"events_in_combobox")

        self.gridLayout.addWidget(self.events_in_combobox, 10, 1, 1, 1)

        self.label_10 = QLabel(ModifyCriteriaDialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_10, 11, 0, 1, 1)

        self.graphic_combobox = QComboBox(ModifyCriteriaDialog)
        self.graphic_combobox.setObjectName(u"graphic_combobox")
        self.graphic_combobox.setEnabled(False)

        self.gridLayout.addWidget(self.graphic_combobox, 11, 1, 1, 1)

        self.minimum_count_spinbox = QSpinBox(ModifyCriteriaDialog)
        self.minimum_count_spinbox.setObjectName(u"minimum_count_spinbox")

        self.gridLayout.addWidget(self.minimum_count_spinbox, 5, 1, 1, 1)

        self.end_period_after_doublespinbox = QDoubleSpinBox(ModifyCriteriaDialog)
        self.end_period_after_doublespinbox.setObjectName(u"end_period_after_doublespinbox")

        self.gridLayout.addWidget(self.end_period_after_doublespinbox, 7, 1, 1, 1)

        self.se_from_doublespinbox = QDoubleSpinBox(ModifyCriteriaDialog)
        self.se_from_doublespinbox.setObjectName(u"se_from_doublespinbox")
        self.se_from_doublespinbox.setMinimum(-99.000000000000000)

        self.gridLayout.addWidget(self.se_from_doublespinbox, 8, 1, 1, 1)

        self.se_to_doublespinbox = QDoubleSpinBox(ModifyCriteriaDialog)
        self.se_to_doublespinbox.setObjectName(u"se_to_doublespinbox")
        self.se_to_doublespinbox.setMinimum(-99.000000000000000)

        self.gridLayout.addWidget(self.se_to_doublespinbox, 9, 1, 1, 1)

        self.interval_to_doublespinbox = QDoubleSpinBox(ModifyCriteriaDialog)
        self.interval_to_doublespinbox.setObjectName(u"interval_to_doublespinbox")

        self.gridLayout.addWidget(self.interval_to_doublespinbox, 4, 1, 1, 1)

        self.interval_from_doublespinbox = QDoubleSpinBox(ModifyCriteriaDialog)
        self.interval_from_doublespinbox.setObjectName(u"interval_from_doublespinbox")

        self.gridLayout.addWidget(self.interval_from_doublespinbox, 3, 1, 1, 1)

        self.duration_to_doublespinbox = QDoubleSpinBox(ModifyCriteriaDialog)
        self.duration_to_doublespinbox.setObjectName(u"duration_to_doublespinbox")

        self.gridLayout.addWidget(self.duration_to_doublespinbox, 2, 1, 1, 1)

        self.duration_from_doublespinbox = QDoubleSpinBox(ModifyCriteriaDialog)
        self.duration_from_doublespinbox.setObjectName(u"duration_from_doublespinbox")

        self.gridLayout.addWidget(self.duration_from_doublespinbox, 1, 1, 1, 1)

        self.label_11 = QLabel(ModifyCriteriaDialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.report_name_lineedit = QLineEdit(ModifyCriteriaDialog)
        self.report_name_lineedit.setObjectName(u"report_name_lineedit")

        self.gridLayout.addWidget(self.report_name_lineedit, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancel_pushbutton = QPushButton(ModifyCriteriaDialog)
        self.cancel_pushbutton.setObjectName(u"cancel_pushbutton")

        self.horizontalLayout.addWidget(self.cancel_pushbutton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ok_to_all_pushbutton = QPushButton(ModifyCriteriaDialog)
        self.ok_to_all_pushbutton.setObjectName(u"ok_to_all_pushbutton")

        self.horizontalLayout.addWidget(self.ok_to_all_pushbutton)

        self.ok_pushbutton = QPushButton(ModifyCriteriaDialog)
        self.ok_pushbutton.setObjectName(u"ok_pushbutton")

        self.horizontalLayout.addWidget(self.ok_pushbutton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ModifyCriteriaDialog)
        self.ok_pushbutton.clicked.connect(ModifyCriteriaDialog.on_ok)
        self.cancel_pushbutton.clicked.connect(ModifyCriteriaDialog.on_cancel)
        self.ok_to_all_pushbutton.clicked.connect(ModifyCriteriaDialog.on_ok_to_all)

        QMetaObject.connectSlotsByName(ModifyCriteriaDialog)
    # setupUi

    def retranslateUi(self, ModifyCriteriaDialog):
        ModifyCriteriaDialog.setWindowTitle(QCoreApplication.translate("ModifyCriteriaDialog", u"Dialog", None))
        ModifyCriteriaDialog.setStyleSheet(QCoreApplication.translate("ModifyCriteriaDialog", u"font: 12pt \"Roboto\";", None))
        self.label.setText(QCoreApplication.translate("ModifyCriteriaDialog", u"Duration from:", None))
        self.label_2.setText(QCoreApplication.translate("ModifyCriteriaDialog", u"Duration to:", None))
        self.label_3.setText(QCoreApplication.translate("ModifyCriteriaDialog", u"Interval from:", None))
        self.label_4.setText(QCoreApplication.translate("ModifyCriteriaDialog", u"Interval to:", None))
        self.label_5.setText(QCoreApplication.translate("ModifyCriteriaDialog", u"Minimum count:", None))
        self.label_6.setText(QCoreApplication.translate("ModifyCriteriaDialog", u"End period after:", None))
        self.label_7.setText(QCoreApplication.translate("ModifyCriteriaDialog", u"Sleep event association from:", None))
        self.label_8.setText(QCoreApplication.translate("ModifyCriteriaDialog", u"Sleep event association to:", None))
        self.label_9.setText(QCoreApplication.translate("ModifyCriteriaDialog", u"Events in:", None))
        self.events_in_combobox.setItemText(0, QCoreApplication.translate("ModifyCriteriaDialog", u"Sleep only", None))
        self.events_in_combobox.setItemText(1, QCoreApplication.translate("ModifyCriteriaDialog", u"Recording time", None))
        self.events_in_combobox.setItemText(2, QCoreApplication.translate("ModifyCriteriaDialog", u"Awake in sleep period", None))
        self.events_in_combobox.setItemText(3, QCoreApplication.translate("ModifyCriteriaDialog", u"Before sleep onset", None))

        self.label_10.setText(QCoreApplication.translate("ModifyCriteriaDialog", u"Graphic:", None))
        self.se_to_doublespinbox.setSpecialValueText("")
        self.interval_to_doublespinbox.setSpecialValueText("")
        self.duration_to_doublespinbox.setSpecialValueText("")
        self.label_11.setText(QCoreApplication.translate("ModifyCriteriaDialog", u"Report name:", None))
        self.cancel_pushbutton.setText(QCoreApplication.translate("ModifyCriteriaDialog", u"Cancel", None))
        self.ok_to_all_pushbutton.setText(QCoreApplication.translate("ModifyCriteriaDialog", u"Add to all files", None))
        self.ok_pushbutton.setText(QCoreApplication.translate("ModifyCriteriaDialog", u"Add", None))
    # retranslateUi

