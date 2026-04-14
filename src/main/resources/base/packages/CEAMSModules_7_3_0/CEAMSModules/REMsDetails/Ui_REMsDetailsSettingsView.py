# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_REMsDetailsSettingsView.ui'
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

class Ui_REMsDetailsSettingsView(object):
    def setupUi(self, REMsDetailsSettingsView):
        if not REMsDetailsSettingsView.objectName():
            REMsDetailsSettingsView.setObjectName(u"REMsDetailsSettingsView")
        REMsDetailsSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        REMsDetailsSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(REMsDetailsSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.recording_path_horizontalLayout = QHBoxLayout()
        self.recording_path_horizontalLayout.setObjectName(u"recording_path_horizontalLayout")
        self.recording_path_label = QLabel(REMsDetailsSettingsView)
        self.recording_path_label.setObjectName(u"recording_path_label")

        self.recording_path_horizontalLayout.addWidget(self.recording_path_label)

        self.recording_path_lineedit = QLineEdit(REMsDetailsSettingsView)
        self.recording_path_lineedit.setObjectName(u"recording_path_lineedit")

        self.recording_path_horizontalLayout.addWidget(self.recording_path_lineedit)


        self.verticalLayout.addLayout(self.recording_path_horizontalLayout)

        self.subject_info_horizontalLayout = QHBoxLayout()
        self.subject_info_horizontalLayout.setObjectName(u"subject_info_horizontalLayout")
        self.subject_info_label = QLabel(REMsDetailsSettingsView)
        self.subject_info_label.setObjectName(u"subject_info_label")

        self.subject_info_horizontalLayout.addWidget(self.subject_info_label)

        self.subject_info_lineedit = QLineEdit(REMsDetailsSettingsView)
        self.subject_info_lineedit.setObjectName(u"subject_info_lineedit")

        self.subject_info_horizontalLayout.addWidget(self.subject_info_lineedit)


        self.verticalLayout.addLayout(self.subject_info_horizontalLayout)

        self.signals_horizontalLayout = QHBoxLayout()
        self.signals_horizontalLayout.setObjectName(u"signals_horizontalLayout")
        self.signals_label = QLabel(REMsDetailsSettingsView)
        self.signals_label.setObjectName(u"signals_label")

        self.signals_horizontalLayout.addWidget(self.signals_label)

        self.signals_lineedit = QLineEdit(REMsDetailsSettingsView)
        self.signals_lineedit.setObjectName(u"signals_lineedit")

        self.signals_horizontalLayout.addWidget(self.signals_lineedit)


        self.verticalLayout.addLayout(self.signals_horizontalLayout)

        self.rems_events_details_horizontalLayout = QHBoxLayout()
        self.rems_events_details_horizontalLayout.setObjectName(u"rems_events_details_horizontalLayout")
        self.rems_events_details_label = QLabel(REMsDetailsSettingsView)
        self.rems_events_details_label.setObjectName(u"rems_events_details_label")

        self.rems_events_details_horizontalLayout.addWidget(self.rems_events_details_label)

        self.rems_events_details_lineedit = QLineEdit(REMsDetailsSettingsView)
        self.rems_events_details_lineedit.setObjectName(u"rems_events_details_lineedit")

        self.rems_events_details_horizontalLayout.addWidget(self.rems_events_details_lineedit)


        self.verticalLayout.addLayout(self.rems_events_details_horizontalLayout)

        self.artifact_events_horizontalLayout = QHBoxLayout()
        self.artifact_events_horizontalLayout.setObjectName(u"artifact_events_horizontalLayout")
        self.artifact_events_label = QLabel(REMsDetailsSettingsView)
        self.artifact_events_label.setObjectName(u"artifact_events_label")

        self.artifact_events_horizontalLayout.addWidget(self.artifact_events_label)

        self.artifact_events_lineedit = QLineEdit(REMsDetailsSettingsView)
        self.artifact_events_lineedit.setObjectName(u"artifact_events_lineedit")

        self.artifact_events_horizontalLayout.addWidget(self.artifact_events_lineedit)


        self.verticalLayout.addLayout(self.artifact_events_horizontalLayout)

        self.sleep_cycle_param_horizontalLayout = QHBoxLayout()
        self.sleep_cycle_param_horizontalLayout.setObjectName(u"sleep_cycle_param_horizontalLayout")
        self.sleep_cycle_param_label = QLabel(REMsDetailsSettingsView)
        self.sleep_cycle_param_label.setObjectName(u"sleep_cycle_param_label")

        self.sleep_cycle_param_horizontalLayout.addWidget(self.sleep_cycle_param_label)

        self.sleep_cycle_param_lineedit = QLineEdit(REMsDetailsSettingsView)
        self.sleep_cycle_param_lineedit.setObjectName(u"sleep_cycle_param_lineedit")

        self.sleep_cycle_param_horizontalLayout.addWidget(self.sleep_cycle_param_lineedit)


        self.verticalLayout.addLayout(self.sleep_cycle_param_horizontalLayout)

        self.stages_cycles_horizontalLayout = QHBoxLayout()
        self.stages_cycles_horizontalLayout.setObjectName(u"stages_cycles_horizontalLayout")
        self.stages_cycles_label = QLabel(REMsDetailsSettingsView)
        self.stages_cycles_label.setObjectName(u"stages_cycles_label")

        self.stages_cycles_horizontalLayout.addWidget(self.stages_cycles_label)

        self.stages_cycles_lineedit = QLineEdit(REMsDetailsSettingsView)
        self.stages_cycles_lineedit.setObjectName(u"stages_cycles_lineedit")

        self.stages_cycles_horizontalLayout.addWidget(self.stages_cycles_lineedit)


        self.verticalLayout.addLayout(self.stages_cycles_horizontalLayout)

        self.rems_det_param_horizontalLayout = QHBoxLayout()
        self.rems_det_param_horizontalLayout.setObjectName(u"rems_det_param_horizontalLayout")
        self.rems_det_param_label = QLabel(REMsDetailsSettingsView)
        self.rems_det_param_label.setObjectName(u"rems_det_param_label")

        self.rems_det_param_horizontalLayout.addWidget(self.rems_det_param_label)

        self.rems_det_param_lineedit = QLineEdit(REMsDetailsSettingsView)
        self.rems_det_param_lineedit.setObjectName(u"rems_det_param_lineedit")

        self.rems_det_param_horizontalLayout.addWidget(self.rems_det_param_lineedit)


        self.verticalLayout.addLayout(self.rems_det_param_horizontalLayout)

        self.report_constants_horizontalLayout = QHBoxLayout()
        self.report_constants_horizontalLayout.setObjectName(u"report_constants_horizontalLayout")
        self.report_constants_label = QLabel(REMsDetailsSettingsView)
        self.report_constants_label.setObjectName(u"report_constants_label")

        self.report_constants_horizontalLayout.addWidget(self.report_constants_label)

        self.report_constants_lineedit = QLineEdit(REMsDetailsSettingsView)
        self.report_constants_lineedit.setObjectName(u"report_constants_lineedit")

        self.report_constants_horizontalLayout.addWidget(self.report_constants_lineedit)


        self.verticalLayout.addLayout(self.report_constants_horizontalLayout)

        self.cohort_filename_horizontalLayout = QHBoxLayout()
        self.cohort_filename_horizontalLayout.setObjectName(u"cohort_filename_horizontalLayout")
        self.cohort_filename_label = QLabel(REMsDetailsSettingsView)
        self.cohort_filename_label.setObjectName(u"cohort_filename_label")

        self.cohort_filename_horizontalLayout.addWidget(self.cohort_filename_label)

        self.cohort_filename_lineedit = QLineEdit(REMsDetailsSettingsView)
        self.cohort_filename_lineedit.setObjectName(u"cohort_filename_lineedit")

        self.cohort_filename_horizontalLayout.addWidget(self.cohort_filename_lineedit)


        self.verticalLayout.addLayout(self.cohort_filename_horizontalLayout)

        self.export_rems_horizontalLayout = QHBoxLayout()
        self.export_rems_horizontalLayout.setObjectName(u"export_rems_horizontalLayout")
        self.export_rems_label = QLabel(REMsDetailsSettingsView)
        self.export_rems_label.setObjectName(u"export_rems_label")

        self.export_rems_horizontalLayout.addWidget(self.export_rems_label)

        self.export_rems_lineedit = QLineEdit(REMsDetailsSettingsView)
        self.export_rems_lineedit.setObjectName(u"export_rems_lineedit")

        self.export_rems_horizontalLayout.addWidget(self.export_rems_lineedit)


        self.verticalLayout.addLayout(self.export_rems_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(REMsDetailsSettingsView)

        QMetaObject.connectSlotsByName(REMsDetailsSettingsView)
    # setupUi

    def retranslateUi(self, REMsDetailsSettingsView):
        REMsDetailsSettingsView.setWindowTitle(QCoreApplication.translate("REMsDetailsSettingsView", u"Form", None))
        self.recording_path_label.setText(QCoreApplication.translate("REMsDetailsSettingsView", u"recording_path", None))
        self.subject_info_label.setText(QCoreApplication.translate("REMsDetailsSettingsView", u"subject_info", None))
        self.signals_label.setText(QCoreApplication.translate("REMsDetailsSettingsView", u"signals", None))
        self.rems_events_details_label.setText(QCoreApplication.translate("REMsDetailsSettingsView", u"rems_events_details", None))
        self.artifact_events_label.setText(QCoreApplication.translate("REMsDetailsSettingsView", u"artifact_events", None))
        self.sleep_cycle_param_label.setText(QCoreApplication.translate("REMsDetailsSettingsView", u"sleep_cycle_param", None))
        self.stages_cycles_label.setText(QCoreApplication.translate("REMsDetailsSettingsView", u"stages_cycles", None))
        self.rems_det_param_label.setText(QCoreApplication.translate("REMsDetailsSettingsView", u"rems_det_param", None))
        self.report_constants_label.setText(QCoreApplication.translate("REMsDetailsSettingsView", u"report_constants", None))
        self.cohort_filename_label.setText(QCoreApplication.translate("REMsDetailsSettingsView", u"cohort_filename", None))
        self.export_rems_label.setText(QCoreApplication.translate("REMsDetailsSettingsView", u"export_rems", None))
    # retranslateUi

