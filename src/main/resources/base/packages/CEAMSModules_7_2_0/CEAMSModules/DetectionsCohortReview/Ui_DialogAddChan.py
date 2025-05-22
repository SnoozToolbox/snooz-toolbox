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
    QHBoxLayout, QLabel, QListView, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_DialogAddChan(object):
    def setupUi(self, DialogAddChan):
        if not DialogAddChan.objectName():
            DialogAddChan.setObjectName(u"DialogAddChan")
        DialogAddChan.resize(230, 345)
        self.verticalLayout_2 = QVBoxLayout(DialogAddChan)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(DialogAddChan)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.listView_addChan = QListView(DialogAddChan)
        self.listView_addChan.setObjectName(u"listView_addChan")
        self.listView_addChan.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listView_addChan.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.verticalLayout.addWidget(self.listView_addChan)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(DialogAddChan)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(58, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.blank_checkBox = QCheckBox(DialogAddChan)
        self.blank_checkBox.setObjectName(u"blank_checkBox")
        self.blank_checkBox.setFont(font)

        self.horizontalLayout.addWidget(self.blank_checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cancel = QPushButton(DialogAddChan)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setFont(font)

        self.horizontalLayout_2.addWidget(self.cancel)

        self.ok = QPushButton(DialogAddChan)
        self.ok.setObjectName(u"ok")
        self.ok.setFont(font)

        self.horizontalLayout_2.addWidget(self.ok)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


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
        self.cancel.setText(QCoreApplication.translate("DialogAddChan", u"Cancel", None))
        self.ok.setText(QCoreApplication.translate("DialogAddChan", u"OK", None))
    # retranslateUi

