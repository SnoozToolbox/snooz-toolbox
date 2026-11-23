# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ConnectivitySettings.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QRadioButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_ConnectivitySettings(object):
    def setupUi(self, ConnectivitySettings):
        if not ConnectivitySettings.objectName():
            ConnectivitySettings.setObjectName(u"ConnectivitySettings")
        ConnectivitySettings.resize(877, 850)
        self.verticalLayout = QVBoxLayout(ConnectivitySettings)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(ConnectivitySettings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.connectivity_type_label = QLabel(self.frame_2)
        self.connectivity_type_label.setObjectName(u"connectivity_type_label")

        self.verticalLayout_4.addWidget(self.connectivity_type_label)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.wpli_radioButton = QRadioButton(self.frame_2)
        self.connectivity_buttonGroup = QButtonGroup(ConnectivitySettings)
        self.connectivity_buttonGroup.setObjectName(u"connectivity_buttonGroup")
        self.connectivity_buttonGroup.addButton(self.wpli_radioButton)
        self.wpli_radioButton.setObjectName(u"wpli_radioButton")
        self.wpli_radioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.wpli_radioButton)

        self.dpli_radioButton = QRadioButton(self.frame_2)
        self.connectivity_buttonGroup.addButton(self.dpli_radioButton)
        self.dpli_radioButton.setObjectName(u"dpli_radioButton")

        self.horizontalLayout_2.addWidget(self.dpli_radioButton)

        self.aec_radioButton = QRadioButton(self.frame_2)
        self.connectivity_buttonGroup.addButton(self.aec_radioButton)
        self.aec_radioButton.setObjectName(u"aec_radioButton")

        self.horizontalLayout_2.addWidget(self.aec_radioButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(ConnectivitySettings)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.connectivity_settings_header_label = QLabel(self.frame)
        self.connectivity_settings_header_label.setObjectName(u"connectivity_settings_header_label")

        self.verticalLayout_2.addWidget(self.connectivity_settings_header_label)

        self.connectivity_settings_label = QLabel(self.frame)
        self.connectivity_settings_label.setObjectName(u"connectivity_settings_label")
        self.connectivity_settings_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.connectivity_settings_label)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.num_surr_label = QLabel(self.frame)
        self.num_surr_label.setObjectName(u"num_surr_label")
        self.num_surr_label.setMinimumSize(QSize(175, 0))

        self.horizontalLayout_5.addWidget(self.num_surr_label)

        self.num_surr_lineedit = QLineEdit(self.frame)
        self.num_surr_lineedit.setObjectName(u"num_surr_lineedit")
        self.num_surr_lineedit.setMaximumSize(QSize(100, 16777215))
        self.num_surr_lineedit.setMaxLength(3)

        self.horizontalLayout_5.addWidget(self.num_surr_lineedit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.p_value_label = QLabel(self.frame)
        self.p_value_label.setObjectName(u"p_value_label")
        self.p_value_label.setMinimumSize(QSize(125, 0))

        self.horizontalLayout.addWidget(self.p_value_label)

        self.p_value_lineedit = QLineEdit(self.frame)
        self.p_value_lineedit.setObjectName(u"p_value_lineedit")
        self.p_value_lineedit.setMaximumSize(QSize(100, 16777215))
        self.p_value_lineedit.setMaxLength(4)

        self.horizontalLayout.addWidget(self.p_value_lineedit)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.horizontalLayout_10.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.select_epoch_label = QLabel(self.frame)
        self.select_epoch_label.setObjectName(u"select_epoch_label")

        self.verticalLayout_2.addWidget(self.select_epoch_label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.epoch_length_label = QLabel(self.frame)
        self.epoch_length_label.setObjectName(u"epoch_length_label")
        self.epoch_length_label.setMinimumSize(QSize(175, 0))

        self.horizontalLayout_4.addWidget(self.epoch_length_label)

        self.epoch_length_lineEdit = QLineEdit(self.frame)
        self.epoch_length_lineEdit.setObjectName(u"epoch_length_lineEdit")
        self.epoch_length_lineEdit.setMaximumSize(QSize(100, 16777215))
        self.epoch_length_lineEdit.setMaxLength(3)

        self.horizontalLayout_4.addWidget(self.epoch_length_lineEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.epoch_overlap_label = QLabel(self.frame)
        self.epoch_overlap_label.setObjectName(u"epoch_overlap_label")
        self.epoch_overlap_label.setMinimumSize(QSize(125, 0))

        self.horizontalLayout_3.addWidget(self.epoch_overlap_label)

        self.epoch_overlap_lineEdit = QLineEdit(self.frame)
        self.epoch_overlap_lineEdit.setObjectName(u"epoch_overlap_lineEdit")
        self.epoch_overlap_lineEdit.setMaximumSize(QSize(100, 16777215))
        self.epoch_overlap_lineEdit.setMaxLength(3)

        self.horizontalLayout_3.addWidget(self.epoch_overlap_lineEdit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(ConnectivitySettings)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.network_properties_header_label = QLabel(self.frame_3)
        self.network_properties_header_label.setObjectName(u"network_properties_header_label")

        self.verticalLayout_7.addWidget(self.network_properties_header_label)

        self.network_properties_textEdit = QTextEdit(self.frame_3)
        self.network_properties_textEdit.setObjectName(u"network_properties_textEdit")
        self.network_properties_textEdit.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_7.addWidget(self.network_properties_textEdit)

        self.select_mode_label = QLabel(self.frame_3)
        self.select_mode_label.setObjectName(u"select_mode_label")

        self.verticalLayout_7.addWidget(self.select_mode_label)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.mst_radioButton = QRadioButton(self.frame_3)
        self.threshold_buttonGroup = QButtonGroup(ConnectivitySettings)
        self.threshold_buttonGroup.setObjectName(u"threshold_buttonGroup")
        self.threshold_buttonGroup.addButton(self.mst_radioButton)
        self.mst_radioButton.setObjectName(u"mst_radioButton")
        self.mst_radioButton.setChecked(True)

        self.horizontalLayout_6.addWidget(self.mst_radioButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.custom_threshold_radioButton = QRadioButton(self.frame_3)
        self.threshold_buttonGroup.addButton(self.custom_threshold_radioButton)
        self.custom_threshold_radioButton.setObjectName(u"custom_threshold_radioButton")

        self.horizontalLayout_6.addWidget(self.custom_threshold_radioButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.threshold_val_label = QLabel(self.frame_3)
        self.threshold_val_label.setObjectName(u"threshold_val_label")

        self.horizontalLayout_8.addWidget(self.threshold_val_label)

        self.threshold_val_doubleSpinBox = QDoubleSpinBox(self.frame_3)
        self.threshold_val_doubleSpinBox.setObjectName(u"threshold_val_doubleSpinBox")
        self.threshold_val_doubleSpinBox.setMinimum(0.010000000000000)
        self.threshold_val_doubleSpinBox.setMaximum(0.990000000000000)
        self.threshold_val_doubleSpinBox.setSingleStep(0.010000000000000)
        self.threshold_val_doubleSpinBox.setValue(0.050000000000000)

        self.horizontalLayout_8.addWidget(self.threshold_val_doubleSpinBox)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)


        self.verticalLayout.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ConnectivitySettings)

        QMetaObject.connectSlotsByName(ConnectivitySettings)
    # setupUi

    def retranslateUi(self, ConnectivitySettings):
        ConnectivitySettings.setWindowTitle("")
        self.connectivity_type_label.setText(QCoreApplication.translate("ConnectivitySettings", u"<html><head/><body><p><span style=\" font-weight:700;\">Connectivity Type:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("ConnectivitySettings", u"Choose the connectivity analysis you want to run. You may run the tool twice if you wish to use both metrics.", None))
        self.wpli_radioButton.setText(QCoreApplication.translate("ConnectivitySettings", u"Weighted Phase Lag Index (WPLI)", None))
        self.dpli_radioButton.setText(QCoreApplication.translate("ConnectivitySettings", u"Directed Phase Lag Index (DPLI)", None))
        self.aec_radioButton.setText(QCoreApplication.translate("ConnectivitySettings", u"Amplitude Envelope Correlation (AEC)", None))
        self.connectivity_settings_header_label.setText(QCoreApplication.translate("ConnectivitySettings", u"<html><head/><body><p><span style=\" font-weight:700;\">Connectivity Settings:</span></p></body></html>", None))
        self.connectivity_settings_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Specify the number of surrogates and the p-value to use for the connectivity analysis:\n"
"\n"
"Surrogates and p-value help remove connections that could appear by chance, keeping only the statistically significant brain connections.\n"
"", None))
        self.num_surr_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Number of surrogrations", None))
        self.num_surr_lineedit.setText(QCoreApplication.translate("ConnectivitySettings", u"20", None))
        self.p_value_label.setText(QCoreApplication.translate("ConnectivitySettings", u"P_value", None))
        self.p_value_lineedit.setText(QCoreApplication.translate("ConnectivitySettings", u"0.05", None))
        self.select_epoch_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Set window length and overlap for epoching the data:", None))
        self.epoch_length_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Epoch length (s)", None))
        self.epoch_length_lineEdit.setText(QCoreApplication.translate("ConnectivitySettings", u"10", None))
        self.epoch_overlap_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Epoch overlap (s)", None))
        self.epoch_overlap_lineEdit.setText(QCoreApplication.translate("ConnectivitySettings", u"0", None))
        self.network_properties_header_label.setText(QCoreApplication.translate("ConnectivitySettings", u"<html><head/><body><p><span style=\" font-weight:700;\">Network Properties Settings:</span></p></body></html>", None))
        self.network_properties_textEdit.setHtml(QCoreApplication.translate("ConnectivitySettings", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Network Properties computes key graph metrics to characterize the network\u2019s efficiency, integration, segregation, and small-world organization.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The output includes five global measures: average shortest path length, clustering coefficient, global efficiency, small-worldness (clustering/pa"
                        "th ratio), and modularity.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This analysis runs only when the number of channels is greater than 32. Connectivity can be thresholded using either a minimum spanning tree or a custom threshold.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">minimally_spanning_tree</span>: finds the smallest threshold that keeps the network fully connected (recommended).<br /><span style=\" font-weight:700;\">custom_threshold</span> : retains the top X % of strongest edges (value between 0 and 1).</p></body></html>", None))
        self.select_mode_label.setText(QCoreApplication.translate("ConnectivitySettings", u"<html><head/><body><p>Select threshold mode, and threshold value if threshold mode is set to custom threshold.</p></body></html>", None))
        self.mst_radioButton.setText(QCoreApplication.translate("ConnectivitySettings", u"Minimally spanning tree", None))
        self.custom_threshold_radioButton.setText(QCoreApplication.translate("ConnectivitySettings", u"Custom threshold", None))
        self.threshold_val_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Threshold value", None))
    # retranslateUi

