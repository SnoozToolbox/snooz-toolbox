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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDialog,
    QGridLayout, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_DialogAddChan(object):
    def setupUi(self, DialogAddChan):
        if not DialogAddChan.objectName():
            DialogAddChan.setObjectName(u"DialogAddChan")
        DialogAddChan.resize(311, 466)
        DialogAddChan.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(DialogAddChan)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(DialogAddChan)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.listView_addChan = QListView(DialogAddChan)
        self.listView_addChan.setObjectName(u"listView_addChan")
        self.listView_addChan.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listView_addChan.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.verticalLayout.addWidget(self.listView_addChan)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(DialogAddChan)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(130, 0))
        self.label.setMaximumSize(QSize(130, 16777215))
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.blank_checkBox = QCheckBox(DialogAddChan)
        self.blank_checkBox.setObjectName(u"blank_checkBox")
        self.blank_checkBox.setFont(font)

        self.gridLayout.addWidget(self.blank_checkBox, 0, 2, 1, 1)

        self.label_3 = QLabel(DialogAddChan)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(130, 0))
        self.label_3.setMaximumSize(QSize(130, 16777215))

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.lineEdit_ROI = QLineEdit(DialogAddChan)
        self.lineEdit_ROI.setObjectName(u"lineEdit_ROI")

        self.gridLayout.addWidget(self.lineEdit_ROI, 1, 2, 1, 1)

        self.cancel = QPushButton(DialogAddChan)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setMinimumSize(QSize(130, 0))
        self.cancel.setMaximumSize(QSize(130, 16777215))
        self.cancel.setFont(font)

        self.gridLayout.addWidget(self.cancel, 2, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 1, 1, 1)

        self.ok = QPushButton(DialogAddChan)
        self.ok.setObjectName(u"ok")
        self.ok.setMinimumSize(QSize(130, 0))
        self.ok.setMaximumSize(QSize(130, 16777215))
        self.ok.setFont(font)

        self.gridLayout.addWidget(self.ok, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(DialogAddChan)
        self.cancel.clicked.connect(DialogAddChan.reject)
        self.ok.clicked.connect(DialogAddChan.accept)

        QMetaObject.connectSlotsByName(DialogAddChan)
    # setupUi

    def retranslateUi(self, DialogAddChan):
        DialogAddChan.setWindowTitle(QCoreApplication.translate("DialogAddChan", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("DialogAddChan", u"Check channels from the list below to create you Region Of Interest (ROI)", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("DialogAddChan", u"Select channels to create your ROI", None))
        self.label.setText(QCoreApplication.translate("DialogAddChan", u"Blank if missing data", None))
#if QT_CONFIG(tooltip)
        self.blank_checkBox.setToolTip(QCoreApplication.translate("DialogAddChan", u"ROI values will be empty if any data is missing for the mean otherwise missing data are ignored.", None))
#endif // QT_CONFIG(tooltip)
        self.blank_checkBox.setText(QCoreApplication.translate("DialogAddChan", u"blank", None))
        self.label_3.setText(QCoreApplication.translate("DialogAddChan", u"ROI label", None))
        self.lineEdit_ROI.setPlaceholderText(QCoreApplication.translate("DialogAddChan", u"name your ROI", None))
        self.cancel.setText(QCoreApplication.translate("DialogAddChan", u"Cancel", None))
        self.ok.setText(QCoreApplication.translate("DialogAddChan", u"OK", None))
    # retranslateUi

