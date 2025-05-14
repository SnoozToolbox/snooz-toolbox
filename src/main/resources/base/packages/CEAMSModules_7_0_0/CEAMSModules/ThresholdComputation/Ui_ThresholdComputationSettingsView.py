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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ThresholdComputationSettingsView(object):
    def setupUi(self, ThresholdComputationSettingsView):
        if not ThresholdComputationSettingsView.objectName():
            ThresholdComputationSettingsView.setObjectName(u"ThresholdComputationSettingsView")
        ThresholdComputationSettingsView.resize(369, 261)
        self.verticalLayout_2 = QVBoxLayout(ThresholdComputationSettingsView)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.threshold_definition_label = QLabel(ThresholdComputationSettingsView)
        self.threshold_definition_label.setObjectName(u"threshold_definition_label")
        self.threshold_definition_label.setMinimumSize(QSize(150, 0))
        self.threshold_definition_label.setMaximumSize(QSize(150, 16777215))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.threshold_definition_label)

        self.threshold_definition_lineedit = QLineEdit(ThresholdComputationSettingsView)
        self.threshold_definition_lineedit.setObjectName(u"threshold_definition_lineedit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.threshold_definition_lineedit)

        self.threshold_metric_label = QLabel(ThresholdComputationSettingsView)
        self.threshold_metric_label.setObjectName(u"threshold_metric_label")
        self.threshold_metric_label.setMinimumSize(QSize(150, 0))
        self.threshold_metric_label.setMaximumSize(QSize(150, 16777215))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.threshold_metric_label)

        self.unit_comboBox = QComboBox(ThresholdComputationSettingsView)
        self.unit_comboBox.addItem("")
        self.unit_comboBox.addItem("")
        self.unit_comboBox.addItem("")
        self.unit_comboBox.addItem("")
        self.unit_comboBox.setObjectName(u"unit_comboBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.unit_comboBox)

        self.label_2 = QLabel(ThresholdComputationSettingsView)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_2)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(ThresholdComputationSettingsView)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.thresh_signal_radioButton = QRadioButton(ThresholdComputationSettingsView)
        self.thresh_signal_radioButton.setObjectName(u"thresh_signal_radioButton")

        self.verticalLayout.addWidget(self.thresh_signal_radioButton)

        self.thresh_cycle_radioButton = QRadioButton(ThresholdComputationSettingsView)
        self.thresh_cycle_radioButton.setObjectName(u"thresh_cycle_radioButton")

        self.verticalLayout.addWidget(self.thresh_cycle_radioButton)

        self.thresh_channel_radioButton = QRadioButton(ThresholdComputationSettingsView)
        self.thresh_channel_radioButton.setObjectName(u"thresh_channel_radioButton")

        self.verticalLayout.addWidget(self.thresh_channel_radioButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(ThresholdComputationSettingsView)
        self.thresh_signal_radioButton.clicked.connect(ThresholdComputationSettingsView.on_settings_changed)
        self.thresh_cycle_radioButton.clicked.connect(ThresholdComputationSettingsView.on_settings_changed)
        self.thresh_channel_radioButton.clicked.connect(ThresholdComputationSettingsView.on_settings_changed)

        QMetaObject.connectSlotsByName(ThresholdComputationSettingsView)
    # setupUi

    def retranslateUi(self, ThresholdComputationSettingsView):
        ThresholdComputationSettingsView.setWindowTitle(QCoreApplication.translate("ThresholdComputationSettingsView", u"Form", None))
        self.threshold_definition_label.setText(QCoreApplication.translate("ThresholdComputationSettingsView", u"threshold value (definition)", None))
#if QT_CONFIG(tooltip)
        self.threshold_definition_lineedit.setToolTip(QCoreApplication.translate("ThresholdComputationSettingsView", u"Enter the threshold value to compute i.e. 95 for 95 percentile or 4 for 4 x standard deviation.", None))
#endif // QT_CONFIG(tooltip)
        self.threshold_metric_label.setText(QCoreApplication.translate("ThresholdComputationSettingsView", u"threshold metric (unit)", None))
        self.unit_comboBox.setItemText(0, QCoreApplication.translate("ThresholdComputationSettingsView", u"percentile", None))
        self.unit_comboBox.setItemText(1, QCoreApplication.translate("ThresholdComputationSettingsView", u"standard deviation", None))
        self.unit_comboBox.setItemText(2, QCoreApplication.translate("ThresholdComputationSettingsView", u"median", None))
        self.unit_comboBox.setItemText(3, QCoreApplication.translate("ThresholdComputationSettingsView", u"variance", None))

        self.label_2.setText(QCoreApplication.translate("ThresholdComputationSettingsView", u"Threshold Computation Settings", None))
        self.label.setText(QCoreApplication.translate("ThresholdComputationSettingsView", u"Compute a theshold per ...", None))
#if QT_CONFIG(tooltip)
        self.thresh_signal_radioButton.setToolTip(QCoreApplication.translate("ThresholdComputationSettingsView", u"Select to compute a threshold per item of signals (each channel and bout of signals will be linked to its own threshold)", None))
#endif // QT_CONFIG(tooltip)
        self.thresh_signal_radioButton.setText(QCoreApplication.translate("ThresholdComputationSettingsView", u"item of signals", None))
#if QT_CONFIG(tooltip)
        self.thresh_cycle_radioButton.setToolTip(QCoreApplication.translate("ThresholdComputationSettingsView", u"Select to compute a threshold per sleep cycle and channel(the threshold will be duplicated for all signals included in the same sleep cycle).", None))
#endif // QT_CONFIG(tooltip)
        self.thresh_cycle_radioButton.setText(QCoreApplication.translate("ThresholdComputationSettingsView", u"sleep cycle and channel", None))
#if QT_CONFIG(tooltip)
        self.thresh_channel_radioButton.setToolTip(QCoreApplication.translate("ThresholdComputationSettingsView", u"Select to compute a single threshold per channel (through all signals and/or sleep cycles).", None))
#endif // QT_CONFIG(tooltip)
        self.thresh_channel_radioButton.setText(QCoreApplication.translate("ThresholdComputationSettingsView", u"channel (through all signals)", None))
    # retranslateUi

