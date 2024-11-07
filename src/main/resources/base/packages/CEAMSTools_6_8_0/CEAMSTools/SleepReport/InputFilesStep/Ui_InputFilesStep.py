# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_InputFilesStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_InputFilesStep(object):
    def setupUi(self, InputFilesStep):
        if not InputFilesStep.objectName():
            InputFilesStep.setObjectName(u"InputFilesStep")
        InputFilesStep.resize(1173, 598)
        self.verticalLayout_7 = QVBoxLayout(InputFilesStep)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.splitter = QSplitter(InputFilesStep)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_8.addWidget(self.label_12)

        self.file_tableview = QTableView(self.layoutWidget)
        self.file_tableview.setObjectName(u"file_tableview")
        self.file_tableview.setAlternatingRowColors(True)
        self.file_tableview.setSelectionMode(QAbstractItemView.SingleSelection)
        self.file_tableview.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.file_tableview.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_8.addWidget(self.file_tableview)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.remove_pushbutton = QPushButton(self.layoutWidget)
        self.remove_pushbutton.setObjectName(u"remove_pushbutton")

        self.horizontalLayout_2.addWidget(self.remove_pushbutton)

        self.add_from_folder_pushbutton = QPushButton(self.layoutWidget)
        self.add_from_folder_pushbutton.setObjectName(u"add_from_folder_pushbutton")

        self.horizontalLayout_2.addWidget(self.add_from_folder_pushbutton)

        self.add_pushbutton = QPushButton(self.layoutWidget)
        self.add_pushbutton.setObjectName(u"add_pushbutton")

        self.horizontalLayout_2.addWidget(self.add_pushbutton)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 2, 1, 1)

        self.groupBox_5 = QGroupBox(self.layoutWidget1)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sex_combobox = QComboBox(self.groupBox_5)
        self.sex_combobox.addItem("")
        self.sex_combobox.addItem("")
        self.sex_combobox.addItem("")
        self.sex_combobox.setObjectName(u"sex_combobox")

        self.verticalLayout_3.addWidget(self.sex_combobox)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)


        self.gridLayout.addWidget(self.groupBox_5, 0, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 3, 1, 1, 1)

        self.groupBox = QGroupBox(self.layoutWidget1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.groupBox.setFlat(True)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.birthdate_timeedit = QDateTimeEdit(self.groupBox)
        self.birthdate_timeedit.setObjectName(u"birthdate_timeedit")
        self.birthdate_timeedit.setCalendarPopup(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.birthdate_timeedit)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.record_date_timeedit = QDateTimeEdit(self.groupBox)
        self.record_date_timeedit.setObjectName(u"record_date_timeedit")
        self.record_date_timeedit.setCalendarPopup(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.record_date_timeedit)

        self.age_spinbox = QSpinBox(self.groupBox)
        self.age_spinbox.setObjectName(u"age_spinbox")
        self.age_spinbox.setMinimum(0)
        self.age_spinbox.setMaximum(200)
        self.age_spinbox.setValue(0)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.age_spinbox)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_7)


        self.verticalLayout_4.addLayout(self.formLayout_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.layoutWidget1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"")
        self.groupBox_3.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.groupBox_3.setCheckable(False)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.height_doublespinbox = QDoubleSpinBox(self.groupBox_3)
        self.height_doublespinbox.setObjectName(u"height_doublespinbox")
        self.height_doublespinbox.setMaximum(1000.000000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.height_doublespinbox)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.weight_doublespinbox = QDoubleSpinBox(self.groupBox_3)
        self.weight_doublespinbox.setObjectName(u"weight_doublespinbox")
        self.weight_doublespinbox.setMaximum(1000.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.weight_doublespinbox)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.waistline_doublespinbox = QDoubleSpinBox(self.groupBox_3)
        self.waistline_doublespinbox.setObjectName(u"waistline_doublespinbox")
        self.waistline_doublespinbox.setMaximum(1000.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.waistline_doublespinbox)

        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_11)

        self.bmi_doublespinbox = QDoubleSpinBox(self.groupBox_3)
        self.bmi_doublespinbox.setObjectName(u"bmi_doublespinbox")
        self.bmi_doublespinbox.setMaximum(1000.000000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.bmi_doublespinbox)


        self.verticalLayout_5.addLayout(self.formLayout)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)


        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.layoutWidget1)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"")
        self.groupBox_6.setFlat(True)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.height_unit_combobox = QComboBox(self.groupBox_6)
        self.height_unit_combobox.addItem("")
        self.height_unit_combobox.addItem("")
        self.height_unit_combobox.setObjectName(u"height_unit_combobox")

        self.gridLayout_6.addWidget(self.height_unit_combobox, 0, 0, 1, 1)

        self.weight_unit_combobox = QComboBox(self.groupBox_6)
        self.weight_unit_combobox.addItem("")
        self.weight_unit_combobox.addItem("")
        self.weight_unit_combobox.setObjectName(u"weight_unit_combobox")

        self.gridLayout_6.addWidget(self.weight_unit_combobox, 1, 0, 1, 1)

        self.waistline_unit_combobox = QComboBox(self.groupBox_6)
        self.waistline_unit_combobox.addItem("")
        self.waistline_unit_combobox.addItem("")
        self.waistline_unit_combobox.setObjectName(u"waistline_unit_combobox")

        self.gridLayout_6.addWidget(self.waistline_unit_combobox, 2, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_6)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)


        self.gridLayout.addWidget(self.groupBox_6, 1, 2, 1, 1)

        self.deidentify_checkbox = QCheckBox(self.layoutWidget1)
        self.deidentify_checkbox.setObjectName(u"deidentify_checkbox")

        self.gridLayout.addWidget(self.deidentify_checkbox, 2, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.layoutWidget1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font = QFont()
        font.setKerning(True)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"")
        self.groupBox_2.setFlat(True)
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.id2_lineedit = QLineEdit(self.groupBox_2)
        self.id2_lineedit.setObjectName(u"id2_lineedit")

        self.gridLayout_2.addWidget(self.id2_lineedit, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.id1_lineedit = QLineEdit(self.groupBox_2)
        self.id1_lineedit.setObjectName(u"id1_lineedit")

        self.gridLayout_2.addWidget(self.id1_lineedit, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.layoutWidget1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.last_name_lineedit = QLineEdit(self.groupBox_4)
        self.last_name_lineedit.setObjectName(u"last_name_lineedit")

        self.gridLayout_3.addWidget(self.last_name_lineedit, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.first_name_lineedit = QLineEdit(self.groupBox_4)
        self.first_name_lineedit.setObjectName(u"first_name_lineedit")

        self.gridLayout_3.addWidget(self.first_name_lineedit, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)


        self.gridLayout.addWidget(self.groupBox_4, 0, 1, 1, 1)

        self.gridLayout.setRowStretch(3, 1)
        self.splitter.addWidget(self.layoutWidget1)

        self.verticalLayout_7.addWidget(self.splitter)


        self.retranslateUi(InputFilesStep)
        self.remove_pushbutton.clicked.connect(InputFilesStep.on_remove_file)
        self.add_pushbutton.clicked.connect(InputFilesStep.on_add_files)
        self.add_from_folder_pushbutton.clicked.connect(InputFilesStep.on_add_from_folder)
        self.deidentify_checkbox.clicked.connect(InputFilesStep.on_deidentify_change)

        QMetaObject.connectSlotsByName(InputFilesStep)
    # setupUi

    def retranslateUi(self, InputFilesStep):
        InputFilesStep.setWindowTitle("")
        self.label_12.setText(QCoreApplication.translate("InputFilesStep", u"Input files", None))
        self.remove_pushbutton.setText(QCoreApplication.translate("InputFilesStep", u"Remove", None))
        self.add_from_folder_pushbutton.setText(QCoreApplication.translate("InputFilesStep", u"Add from folder", None))
        self.add_pushbutton.setText(QCoreApplication.translate("InputFilesStep", u"Add", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("InputFilesStep", u"Sex", None))
        self.sex_combobox.setItemText(0, QCoreApplication.translate("InputFilesStep", u"Male", None))
        self.sex_combobox.setItemText(1, QCoreApplication.translate("InputFilesStep", u"Female", None))
        self.sex_combobox.setItemText(2, QCoreApplication.translate("InputFilesStep", u"Unknown", None))

        self.groupBox.setTitle(QCoreApplication.translate("InputFilesStep", u"Dates", None))
        self.label_5.setText(QCoreApplication.translate("InputFilesStep", u"Birthdate", None))
        self.birthdate_timeedit.setDisplayFormat(QCoreApplication.translate("InputFilesStep", u"yyyy-MM-dd", None))
        self.label_6.setText(QCoreApplication.translate("InputFilesStep", u"Record date", None))
        self.age_spinbox.setSpecialValueText(QCoreApplication.translate("InputFilesStep", u"Not defined", None))
        self.age_spinbox.setSuffix("")
        self.label_7.setText(QCoreApplication.translate("InputFilesStep", u"Age", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("InputFilesStep", u"Measurements", None))
        self.label_8.setText(QCoreApplication.translate("InputFilesStep", u"Height", None))
        self.height_doublespinbox.setSpecialValueText(QCoreApplication.translate("InputFilesStep", u"Not defined", None))
        self.label_9.setText(QCoreApplication.translate("InputFilesStep", u"Weight", None))
        self.weight_doublespinbox.setSpecialValueText(QCoreApplication.translate("InputFilesStep", u"Not defined", None))
        self.label_10.setText(QCoreApplication.translate("InputFilesStep", u"Waistline", None))
        self.waistline_doublespinbox.setSpecialValueText(QCoreApplication.translate("InputFilesStep", u"Not defined", None))
        self.label_11.setText(QCoreApplication.translate("InputFilesStep", u"BMI", None))
        self.bmi_doublespinbox.setSpecialValueText(QCoreApplication.translate("InputFilesStep", u"Not defined", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("InputFilesStep", u"Units", None))
        self.height_unit_combobox.setItemText(0, QCoreApplication.translate("InputFilesStep", u"meters", None))
        self.height_unit_combobox.setItemText(1, QCoreApplication.translate("InputFilesStep", u"feets", None))

        self.weight_unit_combobox.setItemText(0, QCoreApplication.translate("InputFilesStep", u"kg", None))
        self.weight_unit_combobox.setItemText(1, QCoreApplication.translate("InputFilesStep", u"lbs", None))

        self.waistline_unit_combobox.setItemText(0, QCoreApplication.translate("InputFilesStep", u"cm", None))
        self.waistline_unit_combobox.setItemText(1, QCoreApplication.translate("InputFilesStep", u"inches", None))

        self.deidentify_checkbox.setText(QCoreApplication.translate("InputFilesStep", u"De-identify all files", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("InputFilesStep", u"Identification", None))
        self.label_2.setText(QCoreApplication.translate("InputFilesStep", u"Id 2", None))
        self.label.setText(QCoreApplication.translate("InputFilesStep", u"Id 1", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("InputFilesStep", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("InputFilesStep", u"Last name", None))
        self.label_4.setText(QCoreApplication.translate("InputFilesStep", u"First name", None))
    # retranslateUi

