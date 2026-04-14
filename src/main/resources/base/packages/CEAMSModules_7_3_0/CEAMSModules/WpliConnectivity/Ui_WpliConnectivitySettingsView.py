# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_WpliConnectivitySettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_WpliConnectivitySettingsView(object):
    def setupUi(self, WpliConnectivitySettingsView):
        if not WpliConnectivitySettingsView.objectName():
            WpliConnectivitySettingsView.setObjectName(u"WpliConnectivitySettingsView")
        WpliConnectivitySettingsView.resize(650, 333)
        WpliConnectivitySettingsView.setStyleSheet(u"font: 10pt \"Roboto-Regular\";")
        self.verticalLayout_3 = QVBoxLayout(WpliConnectivitySettingsView)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(WpliConnectivitySettingsView)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.num_surr_label = QLabel(self.frame)
        self.num_surr_label.setObjectName(u"num_surr_label")

        self.horizontalLayout_5.addWidget(self.num_surr_label)

        self.num_surr_lineedit = QLineEdit(self.frame)
        self.num_surr_lineedit.setObjectName(u"num_surr_lineedit")
        self.num_surr_lineedit.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.num_surr_lineedit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.epoch_length_label = QLabel(self.frame)
        self.epoch_length_label.setObjectName(u"epoch_length_label")

        self.horizontalLayout_4.addWidget(self.epoch_length_label)

        self.epoch_length_lineEdit = QLineEdit(self.frame)
        self.epoch_length_lineEdit.setObjectName(u"epoch_length_lineEdit")
        self.epoch_length_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_4.addWidget(self.epoch_length_lineEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_7.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.p_value_label = QLabel(self.frame)
        self.p_value_label.setObjectName(u"p_value_label")

        self.horizontalLayout.addWidget(self.p_value_label)

        self.p_value_lineedit = QLineEdit(self.frame)
        self.p_value_lineedit.setObjectName(u"p_value_lineedit")
        self.p_value_lineedit.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.p_value_lineedit)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.epoch_overlap_label = QLabel(self.frame)
        self.epoch_overlap_label.setObjectName(u"epoch_overlap_label")

        self.horizontalLayout_3.addWidget(self.epoch_overlap_label)

        self.epoch_overlap_lineEdit = QLineEdit(self.frame)
        self.epoch_overlap_lineEdit.setObjectName(u"epoch_overlap_lineEdit")
        self.epoch_overlap_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.epoch_overlap_lineEdit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.verticalLayout_3.addWidget(self.frame)

        self.label_2 = QLabel(WpliConnectivitySettingsView)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(WpliConnectivitySettingsView)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.Output_pat_pushButton = QPushButton(WpliConnectivitySettingsView)
        self.Output_pat_pushButton.setObjectName(u"Output_pat_pushButton")

        self.horizontalLayout_2.addWidget(self.Output_pat_pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.retranslateUi(WpliConnectivitySettingsView)

        QMetaObject.connectSlotsByName(WpliConnectivitySettingsView)
    # setupUi

    def retranslateUi(self, WpliConnectivitySettingsView):
        WpliConnectivitySettingsView.setWindowTitle(QCoreApplication.translate("WpliConnectivitySettingsView", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("WpliConnectivitySettingsView", u"<html><head/><body><p><span style=\" font-weight:700;\">Connectivity Settings:</span><br/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("WpliConnectivitySettingsView", u"Specify the number of surrogates and the p-value to use for the connectivity analysis:\n"
"Surrogates and p-value help remove connections that could appear by chance, keeping only the statistically\n"
"significant brain connections.", None))
        self.num_surr_label.setText(QCoreApplication.translate("WpliConnectivitySettingsView", u"number of surrogrations", None))
        self.num_surr_lineedit.setText(QCoreApplication.translate("WpliConnectivitySettingsView", u"20", None))
        self.epoch_length_label.setText(QCoreApplication.translate("WpliConnectivitySettingsView", u"epoch length (s)", None))
        self.epoch_length_lineEdit.setText(QCoreApplication.translate("WpliConnectivitySettingsView", u"10", None))
        self.p_value_label.setText(QCoreApplication.translate("WpliConnectivitySettingsView", u"p_value", None))
        self.p_value_lineedit.setText(QCoreApplication.translate("WpliConnectivitySettingsView", u"0.05", None))
        self.epoch_overlap_label.setText(QCoreApplication.translate("WpliConnectivitySettingsView", u"epoch overlap (s)", None))
        self.epoch_overlap_lineEdit.setText(QCoreApplication.translate("WpliConnectivitySettingsView", u"0", None))
        self.label_2.setText(QCoreApplication.translate("WpliConnectivitySettingsView", u"Choose the directory where you\u2019d like to save the output.\n"
"The output is a .tsv (tab-separated values) file that contains the connectivity data between channels.", None))
        self.Output_pat_pushButton.setText(QCoreApplication.translate("WpliConnectivitySettingsView", u"Choose", None))
    # retranslateUi

