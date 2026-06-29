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

class Ui_EdfXmlWriterSettingsView(object):
    def setupUi(self, EdfXmlWriterSettingsView):
        if not EdfXmlWriterSettingsView.objectName():
            EdfXmlWriterSettingsView.setObjectName(u"EdfXmlWriterSettingsView")
        EdfXmlWriterSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(EdfXmlWriterSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.filename_horizontalLayout = QHBoxLayout()
        self.filename_horizontalLayout.setObjectName(u"filename_horizontalLayout")
        self.filename_label = QLabel(EdfXmlWriterSettingsView)
        self.filename_label.setObjectName(u"filename_label")

        self.filename_horizontalLayout.addWidget(self.filename_label)

        self.filename_lineedit = QLineEdit(EdfXmlWriterSettingsView)
        self.filename_lineedit.setObjectName(u"filename_lineedit")

        self.filename_horizontalLayout.addWidget(self.filename_lineedit)


        self.verticalLayout.addLayout(self.filename_horizontalLayout)

        self.events_horizontalLayout = QHBoxLayout()
        self.events_horizontalLayout.setObjectName(u"events_horizontalLayout")
        self.events_label = QLabel(EdfXmlWriterSettingsView)
        self.events_label.setObjectName(u"events_label")

        self.events_horizontalLayout.addWidget(self.events_label)

        self.events_lineedit = QLineEdit(EdfXmlWriterSettingsView)
        self.events_lineedit.setObjectName(u"events_lineedit")

        self.events_horizontalLayout.addWidget(self.events_lineedit)


        self.verticalLayout.addLayout(self.events_horizontalLayout)

        self.epoch_len_horizontalLayout = QHBoxLayout()
        self.epoch_len_horizontalLayout.setObjectName(u"epoch_len_horizontalLayout")
        self.epoch_len_label = QLabel(EdfXmlWriterSettingsView)
        self.epoch_len_label.setObjectName(u"epoch_len_label")

        self.epoch_len_horizontalLayout.addWidget(self.epoch_len_label)

        self.epoch_len_lineedit = QLineEdit(EdfXmlWriterSettingsView)
        self.epoch_len_lineedit.setObjectName(u"epoch_len_lineedit")

        self.epoch_len_horizontalLayout.addWidget(self.epoch_len_lineedit)


        self.verticalLayout.addLayout(self.epoch_len_horizontalLayout)

        self.stages_df_horizontalLayout = QHBoxLayout()
        self.stages_df_horizontalLayout.setObjectName(u"stages_df_horizontalLayout")
        self.stages_df_label = QLabel(EdfXmlWriterSettingsView)
        self.stages_df_label.setObjectName(u"stages_df_label")

        self.stages_df_horizontalLayout.addWidget(self.stages_df_label)

        self.stages_df_lineedit = QLineEdit(EdfXmlWriterSettingsView)
        self.stages_df_lineedit.setObjectName(u"stages_df_lineedit")

        self.stages_df_horizontalLayout.addWidget(self.stages_df_lineedit)


        self.verticalLayout.addLayout(self.stages_df_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(EdfXmlWriterSettingsView)

        QMetaObject.connectSlotsByName(EdfXmlWriterSettingsView)
    # setupUi

    def retranslateUi(self, EdfXmlWriterSettingsView):
        EdfXmlWriterSettingsView.setWindowTitle(QCoreApplication.translate("EdfXmlWriterSettingsView", u"Form", None))
        self.filename_label.setText(QCoreApplication.translate("EdfXmlWriterSettingsView", u"filename", None))
        self.events_label.setText(QCoreApplication.translate("EdfXmlWriterSettingsView", u"events", None))
        self.epoch_len_label.setText(QCoreApplication.translate("EdfXmlWriterSettingsView", u"epoch_len", None))
        self.stages_df_label.setText(QCoreApplication.translate("EdfXmlWriterSettingsView", u"stages_df", None))
    # retranslateUi

