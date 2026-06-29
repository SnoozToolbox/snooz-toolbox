# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_RemoveChannelArtefactSettingsView.ui'
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

class Ui_RemoveChannelArtefactSettingsView(object):
    def setupUi(self, RemoveChannelArtefactSettingsView):
        if not RemoveChannelArtefactSettingsView.objectName():
            RemoveChannelArtefactSettingsView.setObjectName(u"RemoveChannelArtefactSettingsView")
        RemoveChannelArtefactSettingsView.resize(711, 333)
        RemoveChannelArtefactSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(RemoveChannelArtefactSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.artefact_group_horizontalLayout = QHBoxLayout()
        self.artefact_group_horizontalLayout.setObjectName(u"artefact_group_horizontalLayout")
        self.artefact_group_label = QLabel(RemoveChannelArtefactSettingsView)
        self.artefact_group_label.setObjectName(u"artefact_group_label")

        self.artefact_group_horizontalLayout.addWidget(self.artefact_group_label)

        self.artefact_group_lineedit = QLineEdit(RemoveChannelArtefactSettingsView)
        self.artefact_group_lineedit.setObjectName(u"artefact_group_lineedit")

        self.artefact_group_horizontalLayout.addWidget(self.artefact_group_lineedit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.artefact_group_horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.artefact_group_horizontalLayout)

        self.artefact_name_horizontalLayout = QHBoxLayout()
        self.artefact_name_horizontalLayout.setObjectName(u"artefact_name_horizontalLayout")
        self.artefact_name_label = QLabel(RemoveChannelArtefactSettingsView)
        self.artefact_name_label.setObjectName(u"artefact_name_label")

        self.artefact_name_horizontalLayout.addWidget(self.artefact_name_label)

        self.artefact_name_lineedit = QLineEdit(RemoveChannelArtefactSettingsView)
        self.artefact_name_lineedit.setObjectName(u"artefact_name_lineedit")

        self.artefact_name_horizontalLayout.addWidget(self.artefact_name_lineedit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.artefact_name_horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.artefact_name_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(RemoveChannelArtefactSettingsView)

        QMetaObject.connectSlotsByName(RemoveChannelArtefactSettingsView)
    # setupUi

    def retranslateUi(self, RemoveChannelArtefactSettingsView):
        RemoveChannelArtefactSettingsView.setWindowTitle(QCoreApplication.translate("RemoveChannelArtefactSettingsView", u"Form", None))
        self.artefact_group_label.setText(QCoreApplication.translate("RemoveChannelArtefactSettingsView", u"artefact_group", None))
        self.artefact_name_label.setText(QCoreApplication.translate("RemoveChannelArtefactSettingsView", u"artefact_name", None))
    # retranslateUi

