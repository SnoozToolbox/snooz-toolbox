# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EventReportStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_EventReportStep(object):
    def setupUi(self, EventReportStep):
        if not EventReportStep.objectName():
            EventReportStep.setObjectName(u"EventReportStep")
        EventReportStep.resize(828, 640)
        self.verticalLayout_14 = QVBoxLayout(EventReportStep)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.splitter = QSplitter(EventReportStep)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.file_tableview = QTableView(self.verticalLayoutWidget)
        self.file_tableview.setObjectName(u"file_tableview")
        self.file_tableview.setAlternatingRowColors(True)
        self.file_tableview.setSelectionMode(QAbstractItemView.SingleSelection)
        self.file_tableview.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.file_tableview.setSortingEnabled(False)
        self.file_tableview.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_5.addWidget(self.file_tableview)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer)

        self.clear_all_reports_pushbutton = QPushButton(self.verticalLayoutWidget)
        self.clear_all_reports_pushbutton.setObjectName(u"clear_all_reports_pushbutton")

        self.horizontalLayout_25.addWidget(self.clear_all_reports_pushbutton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_25)

        self.splitter.addWidget(self.verticalLayoutWidget)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.event_treewidget = QTreeWidget(self.layoutWidget)
        self.event_treewidget.setObjectName(u"event_treewidget")
        self.event_treewidget.setAlternatingRowColors(True)
        self.event_treewidget.setColumnCount(3)

        self.verticalLayout_2.addWidget(self.event_treewidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.combine_pushbutton = QPushButton(self.layoutWidget)
        self.combine_pushbutton.setObjectName(u"combine_pushbutton")

        self.horizontalLayout.addWidget(self.combine_pushbutton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.horizontalLayout_13.addWidget(self.label)

        self.report_combobox = QComboBox(self.layoutWidget1)
        self.report_combobox.setObjectName(u"report_combobox")

        self.horizontalLayout_13.addWidget(self.report_combobox)

        self.horizontalLayout_13.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.add_pushbutton = QPushButton(self.layoutWidget1)
        self.add_pushbutton.setObjectName(u"add_pushbutton")

        self.horizontalLayout_3.addWidget(self.add_pushbutton)

        self.add_to_all_pushbutton = QPushButton(self.layoutWidget1)
        self.add_to_all_pushbutton.setObjectName(u"add_to_all_pushbutton")

        self.horizontalLayout_3.addWidget(self.add_to_all_pushbutton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.report_listview = QListView(self.layoutWidget1)
        self.report_listview.setObjectName(u"report_listview")
        self.report_listview.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.report_listview)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.modify_pushbutton = QPushButton(self.layoutWidget1)
        self.modify_pushbutton.setObjectName(u"modify_pushbutton")

        self.horizontalLayout_26.addWidget(self.modify_pushbutton)


        self.verticalLayout.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.remove_pushbutton = QPushButton(self.layoutWidget1)
        self.remove_pushbutton.setObjectName(u"remove_pushbutton")

        self.horizontalLayout_4.addWidget(self.remove_pushbutton)

        self.remove_to_all_pushbutton = QPushButton(self.layoutWidget1)
        self.remove_to_all_pushbutton.setObjectName(u"remove_to_all_pushbutton")

        self.horizontalLayout_4.addWidget(self.remove_to_all_pushbutton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")

        self.verticalLayout.addLayout(self.horizontalLayout_27)

        self.create_pushbutton = QPushButton(self.layoutWidget1)
        self.create_pushbutton.setObjectName(u"create_pushbutton")

        self.verticalLayout.addWidget(self.create_pushbutton)

        self.groupBox = QGroupBox(self.layoutWidget1)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.duration_min_label = QLabel(self.groupBox)
        self.duration_min_label.setObjectName(u"duration_min_label")

        self.horizontalLayout_12.addWidget(self.duration_min_label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_12.addWidget(self.label_2)

        self.duration_max_label = QLabel(self.groupBox)
        self.duration_max_label.setObjectName(u"duration_max_label")

        self.horizontalLayout_12.addWidget(self.duration_max_label)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_12.addWidget(self.label_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_12)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_15)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.interval_min_label = QLabel(self.groupBox)
        self.interval_min_label.setObjectName(u"interval_min_label")

        self.horizontalLayout_10.addWidget(self.interval_min_label)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_10.addWidget(self.label_4)

        self.interval_max_label = QLabel(self.groupBox)
        self.interval_max_label.setObjectName(u"interval_max_label")

        self.horizontalLayout_10.addWidget(self.interval_max_label)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_10)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_13)

        self.min_count_label = QLabel(self.groupBox)
        self.min_count_label.setObjectName(u"min_count_label")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.min_count_label)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_11)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.resp_event_asso_min_label = QLabel(self.groupBox)
        self.resp_event_asso_min_label.setObjectName(u"resp_event_asso_min_label")

        self.horizontalLayout_7.addWidget(self.resp_event_asso_min_label)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.resp_event_asso_max_label = QLabel(self.groupBox)
        self.resp_event_asso_max_label.setObjectName(u"resp_event_asso_max_label")

        self.horizontalLayout_7.addWidget(self.resp_event_asso_max_label)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)


        self.formLayout.setLayout(8, QFormLayout.FieldRole, self.horizontalLayout_7)

        self.label_28 = QLabel(self.groupBox)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_28)

        self.analysis_period_label = QLabel(self.groupBox)
        self.analysis_period_label.setObjectName(u"analysis_period_label")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.analysis_period_label)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_3)

        self.graphic_label = QLabel(self.groupBox)
        self.graphic_label.setObjectName(u"graphic_label")
        self.graphic_label.setEnabled(False)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.graphic_label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.end_period_label = QLabel(self.groupBox)
        self.end_period_label.setObjectName(u"end_period_label")

        self.horizontalLayout_5.addWidget(self.end_period_label)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_5.addWidget(self.label_12)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.formLayout.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.report_name_label = QLabel(self.groupBox)
        self.report_name_label.setObjectName(u"report_name_label")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.report_name_label)


        self.verticalLayout_3.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.layoutWidget1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.csv_report_checkbox = QCheckBox(self.groupBox_2)
        self.csv_report_checkbox.setObjectName(u"csv_report_checkbox")
        self.csv_report_checkbox.setChecked(True)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.csv_report_checkbox)

        self.events_list_checkBox = QCheckBox(self.groupBox_2)
        self.events_list_checkBox.setObjectName(u"events_list_checkBox")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.events_list_checkBox)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.splitter.addWidget(self.layoutWidget1)

        self.verticalLayout_14.addWidget(self.splitter)


        self.retranslateUi(EventReportStep)
        self.event_treewidget.clicked.connect(EventReportStep.on_event_selected)
        self.combine_pushbutton.clicked.connect(EventReportStep.on_combine_events)
        self.add_to_all_pushbutton.clicked.connect(EventReportStep.on_add_to_all)
        self.add_pushbutton.clicked.connect(EventReportStep.on_add)
        self.remove_pushbutton.clicked.connect(EventReportStep.on_remove)
        self.modify_pushbutton.clicked.connect(EventReportStep.on_modify)
        self.create_pushbutton.clicked.connect(EventReportStep.on_create)
        self.report_listview.clicked.connect(EventReportStep.on_report_selected)
        self.remove_to_all_pushbutton.clicked.connect(EventReportStep.on_remove_to_all)
        self.clear_all_reports_pushbutton.clicked.connect(EventReportStep.on_clear_all)
        self.file_tableview.clicked.connect(EventReportStep.on_file_selected)

        QMetaObject.connectSlotsByName(EventReportStep)
    # setupUi

    def retranslateUi(self, EventReportStep):
        EventReportStep.setWindowTitle("")
        EventReportStep.setStyleSheet(QCoreApplication.translate("EventReportStep", u"font: 12pt \"Roboto\";", None))
        self.clear_all_reports_pushbutton.setText(QCoreApplication.translate("EventReportStep", u"Clear all reports", None))
        ___qtreewidgetitem = self.event_treewidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("EventReportStep", u"Report count", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("EventReportStep", u"Event count", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("EventReportStep", u"Name", None));
        self.combine_pushbutton.setText(QCoreApplication.translate("EventReportStep", u"Combine events", None))
        self.label.setText(QCoreApplication.translate("EventReportStep", u"Reports", None))
        self.add_pushbutton.setText(QCoreApplication.translate("EventReportStep", u"Add", None))
        self.add_to_all_pushbutton.setText(QCoreApplication.translate("EventReportStep", u"Add to all files", None))
        self.modify_pushbutton.setText(QCoreApplication.translate("EventReportStep", u"Modify", None))
        self.remove_pushbutton.setText(QCoreApplication.translate("EventReportStep", u"Remove", None))
        self.remove_to_all_pushbutton.setText(QCoreApplication.translate("EventReportStep", u"Remove from all files", None))
        self.create_pushbutton.setText(QCoreApplication.translate("EventReportStep", u"Create new report", None))
        self.groupBox.setTitle(QCoreApplication.translate("EventReportStep", u"Selection criteria", None))
        self.label_5.setText(QCoreApplication.translate("EventReportStep", u"Duration:", None))
        self.duration_min_label.setText("")
        self.label_2.setText(QCoreApplication.translate("EventReportStep", u"to", None))
        self.duration_max_label.setText("")
        self.label_7.setText(QCoreApplication.translate("EventReportStep", u"seconds", None))
        self.label_15.setText(QCoreApplication.translate("EventReportStep", u"Interval:", None))
        self.interval_min_label.setText("")
        self.label_4.setText(QCoreApplication.translate("EventReportStep", u"to", None))
        self.interval_max_label.setText("")
        self.label_8.setText(QCoreApplication.translate("EventReportStep", u"seconds", None))
        self.label_13.setText(QCoreApplication.translate("EventReportStep", u"Min. count:", None))
        self.min_count_label.setText("")
        self.label_11.setText(QCoreApplication.translate("EventReportStep", u"End period after:", None))
        self.label_9.setText(QCoreApplication.translate("EventReportStep", u"Resp. event:", None))
        self.resp_event_asso_min_label.setText("")
        self.label_6.setText(QCoreApplication.translate("EventReportStep", u"to", None))
        self.resp_event_asso_max_label.setText("")
        self.label_10.setText(QCoreApplication.translate("EventReportStep", u"seconds", None))
        self.label_28.setText(QCoreApplication.translate("EventReportStep", u"Events in:", None))
        self.analysis_period_label.setText("")
        self.label_3.setText(QCoreApplication.translate("EventReportStep", u"Graphic:", None))
        self.graphic_label.setText("")
        self.end_period_label.setText("")
        self.label_12.setText(QCoreApplication.translate("EventReportStep", u"minutes", None))
        self.label_14.setText(QCoreApplication.translate("EventReportStep", u"Name:", None))
        self.report_name_label.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("EventReportStep", u"Output format", None))
#if QT_CONFIG(tooltip)
        self.csv_report_checkbox.setToolTip(QCoreApplication.translate("EventReportStep", u"CSV reports are generated by default (values are easily exportable).", None))
#endif // QT_CONFIG(tooltip)
        self.csv_report_checkbox.setText(QCoreApplication.translate("EventReportStep", u"CSV report", None))
#if QT_CONFIG(tooltip)
        self.events_list_checkBox.setToolTip(QCoreApplication.translate("EventReportStep", u"Check to generate the events list for each report and recording.", None))
#endif // QT_CONFIG(tooltip)
        self.events_list_checkBox.setText(QCoreApplication.translate("EventReportStep", u"CSV events list", None))
    # retranslateUi

