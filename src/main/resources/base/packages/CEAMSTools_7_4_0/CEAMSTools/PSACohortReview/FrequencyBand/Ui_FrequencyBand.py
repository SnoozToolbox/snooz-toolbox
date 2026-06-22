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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_FrequencyBand(object):
    def setupUi(self, FrequencyBand):
        if not FrequencyBand.objectName():
            FrequencyBand.setObjectName(u"FrequencyBand")
        FrequencyBand.resize(799, 590)
        self.horizontalLayout_3 = QHBoxLayout(FrequencyBand)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(FrequencyBand)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)

        self.verticalLayout_2.addWidget(self.label_5)

        self.tiny_band_tableView = QTableView(FrequencyBand)
        self.tiny_band_tableView.setObjectName(u"tiny_band_tableView")
        self.tiny_band_tableView.setMaximumSize(QSize(350, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        self.tiny_band_tableView.setFont(font1)
        self.tiny_band_tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_2.addWidget(self.tiny_band_tableView)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(FrequencyBand)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout.addWidget(self.label_6)

        self.new_band_tableView = QTableView(FrequencyBand)
        self.new_band_tableView.setObjectName(u"new_band_tableView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_band_tableView.sizePolicy().hasHeightForWidth())
        self.new_band_tableView.setSizePolicy(sizePolicy)
        self.new_band_tableView.setMinimumSize(QSize(0, 0))
        self.new_band_tableView.setMaximumSize(QSize(16777215, 16777215))
        self.new_band_tableView.setFont(font1)
        self.new_band_tableView.setFocusPolicy(Qt.ClickFocus)
        self.new_band_tableView.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.new_band_tableView.setAlternatingRowColors(False)
        self.new_band_tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.new_band_tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.new_band_tableView.setTextElideMode(Qt.ElideLeft)

        self.verticalLayout.addWidget(self.new_band_tableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_pushButton = QPushButton(FrequencyBand)
        self.add_pushButton.setObjectName(u"add_pushButton")
        self.add_pushButton.setFont(font)

        self.horizontalLayout.addWidget(self.add_pushButton)

        self.rem_pushButton = QPushButton(FrequencyBand)
        self.rem_pushButton.setObjectName(u"rem_pushButton")
        self.rem_pushButton.setFont(font)

        self.horizontalLayout.addWidget(self.rem_pushButton)

        self.load_pushButton = QPushButton(FrequencyBand)
        self.load_pushButton.setObjectName(u"load_pushButton")
        self.load_pushButton.setFont(font)

        self.horizontalLayout.addWidget(self.load_pushButton)

        self.save_pushButton = QPushButton(FrequencyBand)
        self.save_pushButton.setObjectName(u"save_pushButton")
        self.save_pushButton.setFont(font)

        self.horizontalLayout.addWidget(self.save_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(FrequencyBand)
        self.add_pushButton.clicked.connect(FrequencyBand.add_row_freq_band_slot)
        self.rem_pushButton.clicked.connect(FrequencyBand.rem_row_freq_band_slot)
        self.load_pushButton.clicked.connect(FrequencyBand.load_freq_band_slot)
        self.save_pushButton.clicked.connect(FrequencyBand.save_freq_band_slot)

        QMetaObject.connectSlotsByName(FrequencyBand)
    # setupUi

    def retranslateUi(self, FrequencyBand):
        FrequencyBand.setWindowTitle("")
        FrequencyBand.setStyleSheet(QCoreApplication.translate("FrequencyBand", u"font: 12pt \"Roboto\";", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("FrequencyBand", u"The frequency band is defined as the low bin is included and the high bin is excluded in order to avoid twice averaging the energy from the same frequency bin. ", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("FrequencyBand", u"Frequency Bins Available [low, high[ ", None))
        self.label_6.setText(QCoreApplication.translate("FrequencyBand", u"Frequency Bands to Compute", None))
        self.add_pushButton.setText(QCoreApplication.translate("FrequencyBand", u"Add", None))
        self.rem_pushButton.setText(QCoreApplication.translate("FrequencyBand", u"Remove", None))
        self.load_pushButton.setText(QCoreApplication.translate("FrequencyBand", u"&Load", None))
        self.save_pushButton.setText(QCoreApplication.translate("FrequencyBand", u"&Save", None))
    # retranslateUi

