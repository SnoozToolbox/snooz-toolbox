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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from widgets.QLineEditLive import QLineEditLive

class Ui_EdfXmlReaderSettingsView(object):
    def setupUi(self, EdfXmlReaderSettingsView):
        if not EdfXmlReaderSettingsView.objectName():
            EdfXmlReaderSettingsView.setObjectName(u"EdfXmlReaderSettingsView")
        EdfXmlReaderSettingsView.resize(415, 224)
        self.verticalLayout = QVBoxLayout(EdfXmlReaderSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.filename_lineedit = QLineEditLive(EdfXmlReaderSettingsView)
        self.filename_lineedit.setObjectName(u"filename_lineedit")
        self.filename_lineedit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.filename_lineedit, 0, 1, 1, 1)

        self.filename_label = QLabel(EdfXmlReaderSettingsView)
        self.filename_label.setObjectName(u"filename_label")
        self.filename_label.setLayoutDirection(Qt.LeftToRight)
        self.filename_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.filename_label, 0, 0, 1, 1)

        self.choose_pushbutton = QPushButton(EdfXmlReaderSettingsView)
        self.choose_pushbutton.setObjectName(u"choose_pushbutton")

        self.gridLayout.addWidget(self.choose_pushbutton, 0, 2, 1, 1)

        self.event_label = QLabel(EdfXmlReaderSettingsView)
        self.event_label.setObjectName(u"event_label")

        self.gridLayout.addWidget(self.event_label, 1, 0, 1, 1)

        self.event_name_lineEdit = QLineEditLive(EdfXmlReaderSettingsView)
        self.event_name_lineEdit.setObjectName(u"event_name_lineEdit")

        self.gridLayout.addWidget(self.event_name_lineEdit, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(EdfXmlReaderSettingsView)
        self.choose_pushbutton.clicked.connect(EdfXmlReaderSettingsView.on_choose)

        QMetaObject.connectSlotsByName(EdfXmlReaderSettingsView)
    # setupUi

    def retranslateUi(self, EdfXmlReaderSettingsView):
        EdfXmlReaderSettingsView.setWindowTitle(QCoreApplication.translate("EdfXmlReaderSettingsView", u"Form", None))
        self.filename_lineedit.setText("")
        self.filename_lineedit.setPlaceholderText(QCoreApplication.translate("EdfXmlReaderSettingsView", u"Choose a EDF.XML file to read", None))
        self.filename_label.setText(QCoreApplication.translate("EdfXmlReaderSettingsView", u"Filename", None))
        self.choose_pushbutton.setText(QCoreApplication.translate("EdfXmlReaderSettingsView", u"Choose", None))
        self.event_label.setText(QCoreApplication.translate("EdfXmlReaderSettingsView", u"Event name", None))
#if QT_CONFIG(tooltip)
        self.event_name_lineEdit.setToolTip(QCoreApplication.translate("EdfXmlReaderSettingsView", u"Event name is optional. Event name can be a list of labels.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

