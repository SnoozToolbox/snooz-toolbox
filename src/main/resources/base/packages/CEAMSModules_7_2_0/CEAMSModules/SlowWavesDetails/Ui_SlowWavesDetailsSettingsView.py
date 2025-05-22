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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_SlowWavesDetailsSettingsView(object):
    def setupUi(self, SlowWavesDetailsSettingsView):
        if not SlowWavesDetailsSettingsView.objectName():
            SlowWavesDetailsSettingsView.setObjectName(u"SlowWavesDetailsSettingsView")
        SlowWavesDetailsSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(SlowWavesDetailsSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.recording_path_horizontalLayout = QHBoxLayout()
        self.recording_path_horizontalLayout.setObjectName(u"recording_path_horizontalLayout")
        self.recording_path_label = QLabel(SlowWavesDetailsSettingsView)
        self.recording_path_label.setObjectName(u"recording_path_label")

        self.recording_path_horizontalLayout.addWidget(self.recording_path_label)

        self.recording_path_lineedit = QLineEdit(SlowWavesDetailsSettingsView)
        self.recording_path_lineedit.setObjectName(u"recording_path_lineedit")

        self.recording_path_horizontalLayout.addWidget(self.recording_path_lineedit)


        self.verticalLayout.addLayout(self.recording_path_horizontalLayout)

        self.subject_info_horizontalLayout = QHBoxLayout()
        self.subject_info_horizontalLayout.setObjectName(u"subject_info_horizontalLayout")
        self.subject_info_label = QLabel(SlowWavesDetailsSettingsView)
        self.subject_info_label.setObjectName(u"subject_info_label")

        self.subject_info_horizontalLayout.addWidget(self.subject_info_label)

        self.subject_info_lineedit = QLineEdit(SlowWavesDetailsSettingsView)
        self.subject_info_lineedit.setObjectName(u"subject_info_lineedit")

        self.subject_info_horizontalLayout.addWidget(self.subject_info_lineedit)


        self.verticalLayout.addLayout(self.subject_info_horizontalLayout)

        self.signals_horizontalLayout = QHBoxLayout()
        self.signals_horizontalLayout.setObjectName(u"signals_horizontalLayout")
        self.signals_label = QLabel(SlowWavesDetailsSettingsView)
        self.signals_label.setObjectName(u"signals_label")

        self.signals_horizontalLayout.addWidget(self.signals_label)

        self.signals_lineedit = QLineEdit(SlowWavesDetailsSettingsView)
        self.signals_lineedit.setObjectName(u"signals_lineedit")

        self.signals_horizontalLayout.addWidget(self.signals_lineedit)


        self.verticalLayout.addLayout(self.signals_horizontalLayout)

        self.sw_events_details_horizontalLayout = QHBoxLayout()
        self.sw_events_details_horizontalLayout.setObjectName(u"sw_events_details_horizontalLayout")
        self.sw_events_details_label = QLabel(SlowWavesDetailsSettingsView)
        self.sw_events_details_label.setObjectName(u"sw_events_details_label")

        self.sw_events_details_horizontalLayout.addWidget(self.sw_events_details_label)

        self.sw_events_details_lineedit = QLineEdit(SlowWavesDetailsSettingsView)
        self.sw_events_details_lineedit.setObjectName(u"sw_events_details_lineedit")

        self.sw_events_details_horizontalLayout.addWidget(self.sw_events_details_lineedit)


        self.verticalLayout.addLayout(self.sw_events_details_horizontalLayout)

        self.artifact_events_horizontalLayout = QHBoxLayout()
        self.artifact_events_horizontalLayout.setObjectName(u"artifact_events_horizontalLayout")
        self.artifact_events_label = QLabel(SlowWavesDetailsSettingsView)
        self.artifact_events_label.setObjectName(u"artifact_events_label")

        self.artifact_events_horizontalLayout.addWidget(self.artifact_events_label)

        self.artifact_events_lineedit = QLineEdit(SlowWavesDetailsSettingsView)
        self.artifact_events_lineedit.setObjectName(u"artifact_events_lineedit")

        self.artifact_events_horizontalLayout.addWidget(self.artifact_events_lineedit)


        self.verticalLayout.addLayout(self.artifact_events_horizontalLayout)

        self.sleep_cycle_param_horizontalLayout = QHBoxLayout()
        self.sleep_cycle_param_horizontalLayout.setObjectName(u"sleep_cycle_param_horizontalLayout")
        self.sleep_cycle_param_label = QLabel(SlowWavesDetailsSettingsView)
        self.sleep_cycle_param_label.setObjectName(u"sleep_cycle_param_label")

        self.sleep_cycle_param_horizontalLayout.addWidget(self.sleep_cycle_param_label)

        self.sleep_cycle_param_lineedit = QLineEdit(SlowWavesDetailsSettingsView)
        self.sleep_cycle_param_lineedit.setObjectName(u"sleep_cycle_param_lineedit")

        self.sleep_cycle_param_horizontalLayout.addWidget(self.sleep_cycle_param_lineedit)


        self.verticalLayout.addLayout(self.sleep_cycle_param_horizontalLayout)

        self.slow_wave_det_param_horizontalLayout = QHBoxLayout()
        self.slow_wave_det_param_horizontalLayout.setObjectName(u"slow_wave_det_param_horizontalLayout")
        self.slow_wave_det_param_label = QLabel(SlowWavesDetailsSettingsView)
        self.slow_wave_det_param_label.setObjectName(u"slow_wave_det_param_label")

        self.slow_wave_det_param_horizontalLayout.addWidget(self.slow_wave_det_param_label)

        self.slow_wave_det_param_lineedit = QLineEdit(SlowWavesDetailsSettingsView)
        self.slow_wave_det_param_lineedit.setObjectName(u"slow_wave_det_param_lineedit")

        self.slow_wave_det_param_horizontalLayout.addWidget(self.slow_wave_det_param_lineedit)


        self.verticalLayout.addLayout(self.slow_wave_det_param_horizontalLayout)

        self.cohort_filename_horizontalLayout = QHBoxLayout()
        self.cohort_filename_horizontalLayout.setObjectName(u"cohort_filename_horizontalLayout")
        self.cohort_filename_label = QLabel(SlowWavesDetailsSettingsView)
        self.cohort_filename_label.setObjectName(u"cohort_filename_label")

        self.cohort_filename_horizontalLayout.addWidget(self.cohort_filename_label)

        self.cohort_filename_lineedit = QLineEdit(SlowWavesDetailsSettingsView)
        self.cohort_filename_lineedit.setObjectName(u"cohort_filename_lineedit")

        self.cohort_filename_horizontalLayout.addWidget(self.cohort_filename_lineedit)


        self.verticalLayout.addLayout(self.cohort_filename_horizontalLayout)

        self.export_slow_wave_horizontalLayout = QHBoxLayout()
        self.export_slow_wave_horizontalLayout.setObjectName(u"export_slow_wave_horizontalLayout")
        self.export_slow_wave_label = QLabel(SlowWavesDetailsSettingsView)
        self.export_slow_wave_label.setObjectName(u"export_slow_wave_label")

        self.export_slow_wave_horizontalLayout.addWidget(self.export_slow_wave_label)

        self.export_slow_wave_lineedit = QLineEdit(SlowWavesDetailsSettingsView)
        self.export_slow_wave_lineedit.setObjectName(u"export_slow_wave_lineedit")

        self.export_slow_wave_horizontalLayout.addWidget(self.export_slow_wave_lineedit)


        self.verticalLayout.addLayout(self.export_slow_wave_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SlowWavesDetailsSettingsView)

        QMetaObject.connectSlotsByName(SlowWavesDetailsSettingsView)
    # setupUi

    def retranslateUi(self, SlowWavesDetailsSettingsView):
        SlowWavesDetailsSettingsView.setWindowTitle(QCoreApplication.translate("SlowWavesDetailsSettingsView", u"Form", None))
        self.recording_path_label.setText(QCoreApplication.translate("SlowWavesDetailsSettingsView", u"recording_path", None))
        self.subject_info_label.setText(QCoreApplication.translate("SlowWavesDetailsSettingsView", u"subject_info", None))
        self.signals_label.setText(QCoreApplication.translate("SlowWavesDetailsSettingsView", u"signals", None))
        self.sw_events_details_label.setText(QCoreApplication.translate("SlowWavesDetailsSettingsView", u"sw_events_details", None))
        self.artifact_events_label.setText(QCoreApplication.translate("SlowWavesDetailsSettingsView", u"artifact_events", None))
        self.sleep_cycle_param_label.setText(QCoreApplication.translate("SlowWavesDetailsSettingsView", u"sleep_cycle_param", None))
        self.slow_wave_det_param_label.setText(QCoreApplication.translate("SlowWavesDetailsSettingsView", u"slow_wave_det_param", None))
        self.cohort_filename_label.setText(QCoreApplication.translate("SlowWavesDetailsSettingsView", u"cohort_filename", None))
        self.export_slow_wave_label.setText(QCoreApplication.translate("SlowWavesDetailsSettingsView", u"export_slow_wave", None))
    # retranslateUi

