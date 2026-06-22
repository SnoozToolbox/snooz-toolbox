# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_PSACompilationFOOOFSettingsView.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_PSACompilationFOOOFSettingsView(object):
    def setupUi(self, PSACompilationFOOOFSettingsView):
        if not PSACompilationFOOOFSettingsView.objectName():
            PSACompilationFOOOFSettingsView.setObjectName(u"PSACompilationFOOOFSettingsView")
        PSACompilationFOOOFSettingsView.resize(711, 530)
        PSACompilationFOOOFSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(PSACompilationFOOOFSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.subject_info_horizontalLayout = QHBoxLayout()
        self.subject_info_horizontalLayout.setObjectName(u"subject_info_horizontalLayout")
        self.subject_info_label = QLabel(PSACompilationFOOOFSettingsView)
        self.subject_info_label.setObjectName(u"subject_info_label")

        self.subject_info_horizontalLayout.addWidget(self.subject_info_label)

        self.subject_info_lineedit = QLineEdit(PSACompilationFOOOFSettingsView)
        self.subject_info_lineedit.setObjectName(u"subject_info_lineedit")

        self.subject_info_horizontalLayout.addWidget(self.subject_info_lineedit)


        self.verticalLayout.addLayout(self.subject_info_horizontalLayout)

        self.PSD_horizontalLayout = QHBoxLayout()
        self.PSD_horizontalLayout.setObjectName(u"PSD_horizontalLayout")
        self.PSD_label = QLabel(PSACompilationFOOOFSettingsView)
        self.PSD_label.setObjectName(u"PSD_label")

        self.PSD_horizontalLayout.addWidget(self.PSD_label)

        self.PSD_lineedit = QLineEdit(PSACompilationFOOOFSettingsView)
        self.PSD_lineedit.setObjectName(u"PSD_lineedit")

        self.PSD_horizontalLayout.addWidget(self.PSD_lineedit)


        self.verticalLayout.addLayout(self.PSD_horizontalLayout)

        self.events_horizontalLayout = QHBoxLayout()
        self.events_horizontalLayout.setObjectName(u"events_horizontalLayout")
        self.events_label = QLabel(PSACompilationFOOOFSettingsView)
        self.events_label.setObjectName(u"events_label")

        self.events_horizontalLayout.addWidget(self.events_label)

        self.events_lineedit = QLineEdit(PSACompilationFOOOFSettingsView)
        self.events_lineedit.setObjectName(u"events_lineedit")

        self.events_horizontalLayout.addWidget(self.events_lineedit)


        self.verticalLayout.addLayout(self.events_horizontalLayout)

        self.sleep_stages_horizontalLayout = QHBoxLayout()
        self.sleep_stages_horizontalLayout.setObjectName(u"sleep_stages_horizontalLayout")
        self.sleep_stages_label = QLabel(PSACompilationFOOOFSettingsView)
        self.sleep_stages_label.setObjectName(u"sleep_stages_label")

        self.sleep_stages_horizontalLayout.addWidget(self.sleep_stages_label)

        self.sleep_stages_lineedit = QLineEdit(PSACompilationFOOOFSettingsView)
        self.sleep_stages_lineedit.setObjectName(u"sleep_stages_lineedit")

        self.sleep_stages_horizontalLayout.addWidget(self.sleep_stages_lineedit)


        self.verticalLayout.addLayout(self.sleep_stages_horizontalLayout)

        self.mini_bandwidth_horizontalLayout = QHBoxLayout()
        self.mini_bandwidth_horizontalLayout.setObjectName(u"mini_bandwidth_horizontalLayout")
        self.mini_bandwidth_label = QLabel(PSACompilationFOOOFSettingsView)
        self.mini_bandwidth_label.setObjectName(u"mini_bandwidth_label")

        self.mini_bandwidth_horizontalLayout.addWidget(self.mini_bandwidth_label)

        self.mini_bandwidth_lineedit = QLineEdit(PSACompilationFOOOFSettingsView)
        self.mini_bandwidth_lineedit.setObjectName(u"mini_bandwidth_lineedit")

        self.mini_bandwidth_horizontalLayout.addWidget(self.mini_bandwidth_lineedit)


        self.verticalLayout.addLayout(self.mini_bandwidth_horizontalLayout)

        self.first_freq_horizontalLayout = QHBoxLayout()
        self.first_freq_horizontalLayout.setObjectName(u"first_freq_horizontalLayout")
        self.first_freq_label = QLabel(PSACompilationFOOOFSettingsView)
        self.first_freq_label.setObjectName(u"first_freq_label")

        self.first_freq_horizontalLayout.addWidget(self.first_freq_label)

        self.first_freq_lineedit = QLineEdit(PSACompilationFOOOFSettingsView)
        self.first_freq_lineedit.setObjectName(u"first_freq_lineedit")

        self.first_freq_horizontalLayout.addWidget(self.first_freq_lineedit)


        self.verticalLayout.addLayout(self.first_freq_horizontalLayout)

        self.last_freq_horizontalLayout = QHBoxLayout()
        self.last_freq_horizontalLayout.setObjectName(u"last_freq_horizontalLayout")
        self.last_freq_label = QLabel(PSACompilationFOOOFSettingsView)
        self.last_freq_label.setObjectName(u"last_freq_label")

        self.last_freq_horizontalLayout.addWidget(self.last_freq_label)

        self.last_freq_lineedit = QLineEdit(PSACompilationFOOOFSettingsView)
        self.last_freq_lineedit.setObjectName(u"last_freq_lineedit")

        self.last_freq_horizontalLayout.addWidget(self.last_freq_lineedit)


        self.verticalLayout.addLayout(self.last_freq_horizontalLayout)

        self.dist_total_horizontalLayout = QHBoxLayout()
        self.dist_total_horizontalLayout.setObjectName(u"dist_total_horizontalLayout")
        self.dist_total_label = QLabel(PSACompilationFOOOFSettingsView)
        self.dist_total_label.setObjectName(u"dist_total_label")

        self.dist_total_horizontalLayout.addWidget(self.dist_total_label)

        self.dist_total_lineedit = QLineEdit(PSACompilationFOOOFSettingsView)
        self.dist_total_lineedit.setObjectName(u"dist_total_lineedit")

        self.dist_total_horizontalLayout.addWidget(self.dist_total_lineedit)


        self.verticalLayout.addLayout(self.dist_total_horizontalLayout)

        self.dist_hour_horizontalLayout = QHBoxLayout()
        self.dist_hour_horizontalLayout.setObjectName(u"dist_hour_horizontalLayout")
        self.dist_hour_label = QLabel(PSACompilationFOOOFSettingsView)
        self.dist_hour_label.setObjectName(u"dist_hour_label")

        self.dist_hour_horizontalLayout.addWidget(self.dist_hour_label)

        self.dist_hour_lineedit = QLineEdit(PSACompilationFOOOFSettingsView)
        self.dist_hour_lineedit.setObjectName(u"dist_hour_lineedit")

        self.dist_hour_horizontalLayout.addWidget(self.dist_hour_lineedit)


        self.verticalLayout.addLayout(self.dist_hour_horizontalLayout)

        self.dist_cycle_horizontalLayout = QHBoxLayout()
        self.dist_cycle_horizontalLayout.setObjectName(u"dist_cycle_horizontalLayout")
        self.dist_cycle_label = QLabel(PSACompilationFOOOFSettingsView)
        self.dist_cycle_label.setObjectName(u"dist_cycle_label")

        self.dist_cycle_horizontalLayout.addWidget(self.dist_cycle_label)

        self.dist_cycle_lineedit = QLineEdit(PSACompilationFOOOFSettingsView)
        self.dist_cycle_lineedit.setObjectName(u"dist_cycle_lineedit")

        self.dist_cycle_horizontalLayout.addWidget(self.dist_cycle_lineedit)


        self.verticalLayout.addLayout(self.dist_cycle_horizontalLayout)

        self.parameters_cycle_horizontalLayout = QHBoxLayout()
        self.parameters_cycle_horizontalLayout.setObjectName(u"parameters_cycle_horizontalLayout")
        self.parameters_cycle_label = QLabel(PSACompilationFOOOFSettingsView)
        self.parameters_cycle_label.setObjectName(u"parameters_cycle_label")

        self.parameters_cycle_horizontalLayout.addWidget(self.parameters_cycle_label)

        self.parameters_cycle_lineedit = QLineEdit(PSACompilationFOOOFSettingsView)
        self.parameters_cycle_lineedit.setObjectName(u"parameters_cycle_lineedit")

        self.parameters_cycle_horizontalLayout.addWidget(self.parameters_cycle_lineedit)


        self.verticalLayout.addLayout(self.parameters_cycle_horizontalLayout)

        self.artefact_group_horizontalLayout = QHBoxLayout()
        self.artefact_group_horizontalLayout.setObjectName(u"artefact_group_horizontalLayout")
        self.artefact_group_label = QLabel(PSACompilationFOOOFSettingsView)
        self.artefact_group_label.setObjectName(u"artefact_group_label")

        self.artefact_group_horizontalLayout.addWidget(self.artefact_group_label)

        self.artefact_group_lineedit = QLineEdit(PSACompilationFOOOFSettingsView)
        self.artefact_group_lineedit.setObjectName(u"artefact_group_lineedit")

        self.artefact_group_horizontalLayout.addWidget(self.artefact_group_lineedit)


        self.verticalLayout.addLayout(self.artefact_group_horizontalLayout)

        self.artefact_name_horizontalLayout = QHBoxLayout()
        self.artefact_name_horizontalLayout.setObjectName(u"artefact_name_horizontalLayout")
        self.artefact_name_label = QLabel(PSACompilationFOOOFSettingsView)
        self.artefact_name_label.setObjectName(u"artefact_name_label")

        self.artefact_name_horizontalLayout.addWidget(self.artefact_name_label)

        self.artefact_name_lineedit = QLineEdit(PSACompilationFOOOFSettingsView)
        self.artefact_name_lineedit.setObjectName(u"artefact_name_lineedit")

        self.artefact_name_horizontalLayout.addWidget(self.artefact_name_lineedit)


        self.verticalLayout.addLayout(self.artefact_name_horizontalLayout)

        self.cycle_labelled_horizontalLayout = QHBoxLayout()
        self.cycle_labelled_horizontalLayout.setObjectName(u"cycle_labelled_horizontalLayout")
        self.cycle_labelled_label = QLabel(PSACompilationFOOOFSettingsView)
        self.cycle_labelled_label.setObjectName(u"cycle_labelled_label")

        self.cycle_labelled_horizontalLayout.addWidget(self.cycle_labelled_label)

        self.cycle_labelled_lineedit = QLineEdit(PSACompilationFOOOFSettingsView)
        self.cycle_labelled_lineedit.setObjectName(u"cycle_labelled_lineedit")

        self.cycle_labelled_horizontalLayout.addWidget(self.cycle_labelled_lineedit)


        self.verticalLayout.addLayout(self.cycle_labelled_horizontalLayout)

        self.report_constants_horizontalLayout = QHBoxLayout()
        self.report_constants_horizontalLayout.setObjectName(u"report_constants_horizontalLayout")
        self.report_constants_label = QLabel(PSACompilationFOOOFSettingsView)
        self.report_constants_label.setObjectName(u"report_constants_label")

        self.report_constants_horizontalLayout.addWidget(self.report_constants_label)

        self.report_constants_lineedit = QLineEdit(PSACompilationFOOOFSettingsView)
        self.report_constants_lineedit.setObjectName(u"report_constants_lineedit")

        self.report_constants_horizontalLayout.addWidget(self.report_constants_lineedit)


        self.verticalLayout.addLayout(self.report_constants_horizontalLayout)

        self.filename_horizontalLayout = QHBoxLayout()
        self.filename_horizontalLayout.setObjectName(u"filename_horizontalLayout")
        self.filename_label = QLabel(PSACompilationFOOOFSettingsView)
        self.filename_label.setObjectName(u"filename_label")

        self.filename_horizontalLayout.addWidget(self.filename_label)

        self.filename_lineedit = QLineEdit(PSACompilationFOOOFSettingsView)
        self.filename_lineedit.setObjectName(u"filename_lineedit")

        self.filename_horizontalLayout.addWidget(self.filename_lineedit)


        self.verticalLayout.addLayout(self.filename_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(PSACompilationFOOOFSettingsView)

        QMetaObject.connectSlotsByName(PSACompilationFOOOFSettingsView)
    # setupUi

    def retranslateUi(self, PSACompilationFOOOFSettingsView):
        PSACompilationFOOOFSettingsView.setWindowTitle(QCoreApplication.translate("PSACompilationFOOOFSettingsView", u"Form", None))
        self.subject_info_label.setText(QCoreApplication.translate("PSACompilationFOOOFSettingsView", u"subject_info", None))
        self.PSD_label.setText(QCoreApplication.translate("PSACompilationFOOOFSettingsView", u"PSD", None))
        self.events_label.setText(QCoreApplication.translate("PSACompilationFOOOFSettingsView", u"events", None))
        self.sleep_stages_label.setText(QCoreApplication.translate("PSACompilationFOOOFSettingsView", u"sleep_stages", None))
        self.mini_bandwidth_label.setText(QCoreApplication.translate("PSACompilationFOOOFSettingsView", u"mini_bandwidth", None))
        self.first_freq_label.setText(QCoreApplication.translate("PSACompilationFOOOFSettingsView", u"first_freq", None))
        self.last_freq_label.setText(QCoreApplication.translate("PSACompilationFOOOFSettingsView", u"last_freq", None))
        self.dist_total_label.setText(QCoreApplication.translate("PSACompilationFOOOFSettingsView", u"dist_total", None))
        self.dist_hour_label.setText(QCoreApplication.translate("PSACompilationFOOOFSettingsView", u"dist_hour", None))
        self.dist_cycle_label.setText(QCoreApplication.translate("PSACompilationFOOOFSettingsView", u"dist_cycle", None))
        self.parameters_cycle_label.setText(QCoreApplication.translate("PSACompilationFOOOFSettingsView", u"parameters_cycle", None))
        self.artefact_group_label.setText(QCoreApplication.translate("PSACompilationFOOOFSettingsView", u"artefact_group", None))
        self.artefact_name_label.setText(QCoreApplication.translate("PSACompilationFOOOFSettingsView", u"artefact_name", None))
        self.cycle_labelled_label.setText(QCoreApplication.translate("PSACompilationFOOOFSettingsView", u"cycle_labelled", None))
        self.report_constants_label.setText(QCoreApplication.translate("PSACompilationFOOOFSettingsView", u"report_constants", None))
        self.filename_label.setText(QCoreApplication.translate("PSACompilationFOOOFSettingsView", u"filename", None))
    # retranslateUi

