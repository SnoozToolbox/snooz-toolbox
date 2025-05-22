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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ResetSignalArtefactSettingsView(object):
    def setupUi(self, ResetSignalArtefactSettingsView):
        if not ResetSignalArtefactSettingsView.objectName():
            ResetSignalArtefactSettingsView.setObjectName(u"ResetSignalArtefactSettingsView")
        ResetSignalArtefactSettingsView.resize(425, 172)
        self.verticalLayout = QVBoxLayout(ResetSignalArtefactSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.artefact_group_horizontalLayout = QHBoxLayout()
        self.artefact_group_horizontalLayout.setObjectName(u"artefact_group_horizontalLayout")
        self.artefact_group_label = QLabel(ResetSignalArtefactSettingsView)
        self.artefact_group_label.setObjectName(u"artefact_group_label")

        self.artefact_group_horizontalLayout.addWidget(self.artefact_group_label)

        self.artefact_group_lineedit = QLineEdit(ResetSignalArtefactSettingsView)
        self.artefact_group_lineedit.setObjectName(u"artefact_group_lineedit")

        self.artefact_group_horizontalLayout.addWidget(self.artefact_group_lineedit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.artefact_group_horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.artefact_group_horizontalLayout)

        self.artefact_name_horizontalLayout = QHBoxLayout()
        self.artefact_name_horizontalLayout.setObjectName(u"artefact_name_horizontalLayout")
        self.artefact_name_label = QLabel(ResetSignalArtefactSettingsView)
        self.artefact_name_label.setObjectName(u"artefact_name_label")

        self.artefact_name_horizontalLayout.addWidget(self.artefact_name_label)

        self.artefact_name_lineedit = QLineEdit(ResetSignalArtefactSettingsView)
        self.artefact_name_lineedit.setObjectName(u"artefact_name_lineedit")

        self.artefact_name_horizontalLayout.addWidget(self.artefact_name_lineedit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.artefact_name_horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.artefact_name_horizontalLayout)

        self.label = QLabel(ResetSignalArtefactSettingsView)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.signal_value_comboBox = QComboBox(ResetSignalArtefactSettingsView)
        self.signal_value_comboBox.addItem("")
        self.signal_value_comboBox.addItem("")
        self.signal_value_comboBox.setObjectName(u"signal_value_comboBox")

        self.horizontalLayout.addWidget(self.signal_value_comboBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ResetSignalArtefactSettingsView)

        QMetaObject.connectSlotsByName(ResetSignalArtefactSettingsView)
    # setupUi

    def retranslateUi(self, ResetSignalArtefactSettingsView):
        ResetSignalArtefactSettingsView.setWindowTitle(QCoreApplication.translate("ResetSignalArtefactSettingsView", u"Form", None))
        self.artefact_group_label.setText(QCoreApplication.translate("ResetSignalArtefactSettingsView", u"artefact_group", None))
#if QT_CONFIG(tooltip)
        self.artefact_group_lineedit.setToolTip(QCoreApplication.translate("ResetSignalArtefactSettingsView", u"The user can define a single group (and let the name blank) or a single name (and let the group blank). \n"
"If group and name are defined, they must be defined in pairs.\n"
"Each group should be separated by a comma.\n"
"The group works as a pattern matching.  ", None))
#endif // QT_CONFIG(tooltip)
        self.artefact_name_label.setText(QCoreApplication.translate("ResetSignalArtefactSettingsView", u"artefact_name", None))
#if QT_CONFIG(tooltip)
        self.artefact_name_lineedit.setToolTip(QCoreApplication.translate("ResetSignalArtefactSettingsView", u"The user can define a single group (and let the name blank) or a single name (and let the group blank). \n"
"If group and name are defined, they must be defined in pairs.\n"
"Each name should be separated by a comma.\n"
"The name works as a pattern matching.  ", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("ResetSignalArtefactSettingsView", u"Replace artefacted signal values with:", None))
        self.signal_value_comboBox.setItemText(0, QCoreApplication.translate("ResetSignalArtefactSettingsView", u"0 (turkey win)", None))
        self.signal_value_comboBox.setItemText(1, QCoreApplication.translate("ResetSignalArtefactSettingsView", u"NaN", None))

#if QT_CONFIG(tooltip)
        self.signal_value_comboBox.setToolTip(QCoreApplication.translate("ResetSignalArtefactSettingsView", u"Replace the artefacted signal values with zeros, NaNs or\n"
"interpolate between the last valid sample and the next following valid sample.\n"
"        ", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

