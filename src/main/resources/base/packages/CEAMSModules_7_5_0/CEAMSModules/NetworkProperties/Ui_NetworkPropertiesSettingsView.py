# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_NetworkPropertiesSettingsView.ui'
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

class Ui_NetworkPropertiesSettingsView(object):
    def setupUi(self, NetworkPropertiesSettingsView):
        if not NetworkPropertiesSettingsView.objectName():
            NetworkPropertiesSettingsView.setObjectName(u"NetworkPropertiesSettingsView")
        NetworkPropertiesSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(NetworkPropertiesSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.recording_path_horizontalLayout = QHBoxLayout()
        self.recording_path_horizontalLayout.setObjectName(u"recording_path_horizontalLayout")
        self.recording_path_label = QLabel(NetworkPropertiesSettingsView)
        self.recording_path_label.setObjectName(u"recording_path_label")

        self.recording_path_horizontalLayout.addWidget(self.recording_path_label)

        self.recording_path_lineedit = QLineEdit(NetworkPropertiesSettingsView)
        self.recording_path_lineedit.setObjectName(u"recording_path_lineedit")

        self.recording_path_horizontalLayout.addWidget(self.recording_path_lineedit)


        self.verticalLayout.addLayout(self.recording_path_horizontalLayout)

        self.subject_info_horizontalLayout = QHBoxLayout()
        self.subject_info_horizontalLayout.setObjectName(u"subject_info_horizontalLayout")
        self.subject_info_label = QLabel(NetworkPropertiesSettingsView)
        self.subject_info_label.setObjectName(u"subject_info_label")

        self.subject_info_horizontalLayout.addWidget(self.subject_info_label)

        self.subject_info_lineedit = QLineEdit(NetworkPropertiesSettingsView)
        self.subject_info_lineedit.setObjectName(u"subject_info_lineedit")

        self.subject_info_horizontalLayout.addWidget(self.subject_info_lineedit)


        self.verticalLayout.addLayout(self.subject_info_horizontalLayout)

        self.con_dict_horizontalLayout = QHBoxLayout()
        self.con_dict_horizontalLayout.setObjectName(u"con_dict_horizontalLayout")
        self.con_dict_label = QLabel(NetworkPropertiesSettingsView)
        self.con_dict_label.setObjectName(u"con_dict_label")

        self.con_dict_horizontalLayout.addWidget(self.con_dict_label)

        self.con_dict_lineedit = QLineEdit(NetworkPropertiesSettingsView)
        self.con_dict_lineedit.setObjectName(u"con_dict_lineedit")

        self.con_dict_horizontalLayout.addWidget(self.con_dict_lineedit)


        self.verticalLayout.addLayout(self.con_dict_horizontalLayout)

        self.threshold_mode_horizontalLayout = QHBoxLayout()
        self.threshold_mode_horizontalLayout.setObjectName(u"threshold_mode_horizontalLayout")
        self.threshold_mode_label = QLabel(NetworkPropertiesSettingsView)
        self.threshold_mode_label.setObjectName(u"threshold_mode_label")

        self.threshold_mode_horizontalLayout.addWidget(self.threshold_mode_label)

        self.threshold_mode_lineedit = QLineEdit(NetworkPropertiesSettingsView)
        self.threshold_mode_lineedit.setObjectName(u"threshold_mode_lineedit")

        self.threshold_mode_horizontalLayout.addWidget(self.threshold_mode_lineedit)


        self.verticalLayout.addLayout(self.threshold_mode_horizontalLayout)

        self.threshold_value_horizontalLayout = QHBoxLayout()
        self.threshold_value_horizontalLayout.setObjectName(u"threshold_value_horizontalLayout")
        self.threshold_value_label = QLabel(NetworkPropertiesSettingsView)
        self.threshold_value_label.setObjectName(u"threshold_value_label")

        self.threshold_value_horizontalLayout.addWidget(self.threshold_value_label)

        self.threshold_value_lineedit = QLineEdit(NetworkPropertiesSettingsView)
        self.threshold_value_lineedit.setObjectName(u"threshold_value_lineedit")

        self.threshold_value_horizontalLayout.addWidget(self.threshold_value_lineedit)


        self.verticalLayout.addLayout(self.threshold_value_horizontalLayout)

        self.output_path_horizontalLayout = QHBoxLayout()
        self.output_path_horizontalLayout.setObjectName(u"output_path_horizontalLayout")
        self.output_path_label = QLabel(NetworkPropertiesSettingsView)
        self.output_path_label.setObjectName(u"output_path_label")

        self.output_path_horizontalLayout.addWidget(self.output_path_label)

        self.output_path_lineedit = QLineEdit(NetworkPropertiesSettingsView)
        self.output_path_lineedit.setObjectName(u"output_path_lineedit")

        self.output_path_horizontalLayout.addWidget(self.output_path_lineedit)


        self.verticalLayout.addLayout(self.output_path_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(NetworkPropertiesSettingsView)

        QMetaObject.connectSlotsByName(NetworkPropertiesSettingsView)
    # setupUi

    def retranslateUi(self, NetworkPropertiesSettingsView):
        NetworkPropertiesSettingsView.setWindowTitle(QCoreApplication.translate("NetworkPropertiesSettingsView", u"Form", None))
        self.recording_path_label.setText(QCoreApplication.translate("NetworkPropertiesSettingsView", u"recording_path", None))
        self.subject_info_label.setText(QCoreApplication.translate("NetworkPropertiesSettingsView", u"subject_info", None))
        self.con_dict_label.setText(QCoreApplication.translate("NetworkPropertiesSettingsView", u"con_dict", None))
        self.threshold_mode_label.setText(QCoreApplication.translate("NetworkPropertiesSettingsView", u"threshold_mode", None))
        self.threshold_value_label.setText(QCoreApplication.translate("NetworkPropertiesSettingsView", u"threshold_value", None))
        self.output_path_label.setText(QCoreApplication.translate("NetworkPropertiesSettingsView", u"output_path", None))
    # retranslateUi

