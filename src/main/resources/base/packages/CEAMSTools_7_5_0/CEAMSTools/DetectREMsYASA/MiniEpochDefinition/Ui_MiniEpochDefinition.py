# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MiniEpochDefinition.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_MiniEpochDefinition(object):
    def setupUi(self, MiniEpochDefinition):
        if not MiniEpochDefinition.objectName():
            MiniEpochDefinition.setObjectName(u"MiniEpochDefinition")
        MiniEpochDefinition.resize(954, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MiniEpochDefinition.sizePolicy().hasHeightForWidth())
        MiniEpochDefinition.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(MiniEpochDefinition)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(MiniEpochDefinition)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.verticalSpacer_2 = QSpacerItem(20, 29, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_9 = QLabel(MiniEpochDefinition)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.label_5 = QLabel(MiniEpochDefinition)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(MiniEpochDefinition)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(MiniEpochDefinition)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_group = QLineEdit(MiniEpochDefinition)
        self.lineEdit_group.setObjectName(u"lineEdit_group")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_group)

        self.label_2 = QLabel(MiniEpochDefinition)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_name_Phasic = QLineEdit(MiniEpochDefinition)
        self.lineEdit_name_Phasic.setObjectName(u"lineEdit_name_Phasic")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_name_Phasic)

        self.label_3 = QLabel(MiniEpochDefinition)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_name_Tonic = QLineEdit(MiniEpochDefinition)
        self.lineEdit_name_Tonic.setObjectName(u"lineEdit_name_Tonic")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_name_Tonic)


        self.horizontalLayout.addLayout(self.formLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_8 = QLabel(MiniEpochDefinition)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.comboBox_length = QComboBox(MiniEpochDefinition)
        self.comboBox_length.addItem("")
        self.comboBox_length.addItem("")
        self.comboBox_length.addItem("")
        self.comboBox_length.addItem("")
        self.comboBox_length.setObjectName(u"comboBox_length")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox_length)


        self.horizontalLayout_2.addLayout(self.formLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.label_7 = QLabel(MiniEpochDefinition)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(MiniEpochDefinition)

        QMetaObject.connectSlotsByName(MiniEpochDefinition)
    # setupUi

    def retranslateUi(self, MiniEpochDefinition):
        MiniEpochDefinition.setWindowTitle("")
        self.label_4.setText(QCoreApplication.translate("MiniEpochDefinition", u"<html><head/><body><p><span style=\" font-weight:700;\">Define the labels and length of the mini-epochs for phasic and tonic REMs.</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MiniEpochDefinition", u"<html><head/><body><p><span style=\" font-weight:700;\">General definition</span></p><p><span style=\" text-decoration: underline;\">Tonic REM</span><span style=\"\"> corresponds to more stable REM activity with minimal eye movements and lower physiological variability.</span></p><p><span style=\" text-decoration: underline;\">Phasic REM</span><span style=\"\"> is characterized by bursts of rapid eye movements, transient muscle activity, and increased neural and autonomic<br/>activation. This separation enables more detailed investigation of REM sleep dynamics and related biomarkers.</span></p><p><br/></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MiniEpochDefinition", u"<html><head/><body><p><span style=\" font-weight:700;\">Mini-epochs group and name definition</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MiniEpochDefinition", u"<html><head/><body><p>Each event belongs to a group and is labeled by a name.</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MiniEpochDefinition", u"Group for the mini-epoch", None))
        self.label_2.setText(QCoreApplication.translate("MiniEpochDefinition", u"Name for the Phasic mini-epoch", None))
        self.label_3.setText(QCoreApplication.translate("MiniEpochDefinition", u"Name for the Tonic mini-epoch", None))
        self.label_8.setText(QCoreApplication.translate("MiniEpochDefinition", u"Window length (sec)                ", None))
        self.comboBox_length.setItemText(0, QCoreApplication.translate("MiniEpochDefinition", u"3", None))
        self.comboBox_length.setItemText(1, QCoreApplication.translate("MiniEpochDefinition", u"5", None))
        self.comboBox_length.setItemText(2, QCoreApplication.translate("MiniEpochDefinition", u"10", None))
        self.comboBox_length.setItemText(3, QCoreApplication.translate("MiniEpochDefinition", u"30", None))

        self.label_7.setText(QCoreApplication.translate("MiniEpochDefinition", u"<html><head/><body><p><span style=\" font-weight:700;\">Mini-epochs length value configuration</span></p><p>Configurable mini-epoch lengths (e.g., 3, 5, 10 or 30s) enable finer characterization of REM microstructure by capturing brief<br/>phasic bursts and separating tonic and phasic activity within standard 30-s REM epochs.</p></body></html>", None))
    # retranslateUi

