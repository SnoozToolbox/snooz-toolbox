# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AboutDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import Snooz_logo_rc
import themes_rc

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(879, 516)
        AboutDialog.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.snooz_label = QLabel(AboutDialog)
        self.snooz_label.setObjectName(u"snooz_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.snooz_label.sizePolicy().hasHeightForWidth())
        self.snooz_label.setSizePolicy(sizePolicy)
        self.snooz_label.setMinimumSize(QSize(0, 0))
        self.snooz_label.setMaximumSize(QSize(200, 100))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.snooz_label.setFont(font)
        self.snooz_label.setFrameShape(QFrame.NoFrame)
        self.snooz_label.setPixmap(QPixmap(u":/Snooz_logo/Snooz_logo.png"))
        self.snooz_label.setScaledContents(True)
        self.snooz_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.snooz_label)

        self.label = QLabel(AboutDialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(AboutDialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.snooz_version_label = QLabel(AboutDialog)
        self.snooz_version_label.setObjectName(u"snooz_version_label")
        self.snooz_version_label.setFont(font)

        self.verticalLayout.addWidget(self.snooz_version_label)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_released_version = QLabel(AboutDialog)
        self.label_released_version.setObjectName(u"label_released_version")

        self.verticalLayout.addWidget(self.label_released_version)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_4 = QLabel(AboutDialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_windows = QPushButton(AboutDialog)
        self.pushButton_windows.setObjectName(u"pushButton_windows")
        self.pushButton_windows.setStyleSheet(u"background-color: rgb(78, 134, 255);")

        self.horizontalLayout.addWidget(self.pushButton_windows)

        self.pushButton_mac = QPushButton(AboutDialog)
        self.pushButton_mac.setObjectName(u"pushButton_mac")
        self.pushButton_mac.setEnabled(False)
        self.pushButton_mac.setStyleSheet(u"background-color: rgb(78, 134, 255);")

        self.horizontalLayout.addWidget(self.pushButton_mac)

        self.pushButton_linux = QPushButton(AboutDialog)
        self.pushButton_linux.setObjectName(u"pushButton_linux")
        self.pushButton_linux.setStyleSheet(u"background-color: rgb(78, 134, 255);")

        self.horizontalLayout.addWidget(self.pushButton_linux)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(AboutDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_5 = QLabel(AboutDialog)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.verticalSpacer_2 = QSpacerItem(20, 119, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(AboutDialog)
        self.pushButton_windows.clicked.connect(AboutDialog.download_windows_slot)
        self.pushButton_mac.clicked.connect(AboutDialog.download_MAC_slot)
        self.pushButton_linux.clicked.connect(AboutDialog.download_Linux_slot)

        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About Snooz", None))
        self.snooz_label.setText("")
        self.label.setText(QCoreApplication.translate("AboutDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Snooz Toolbox</span> is a Python 3.10 software for analyzing sleep recordings (Polysomnography).<br/>It is developed by the team at the CARSM (Center for Advanced Research in Sleep Medicine) in Montreal.</p><p>Snooz is built using a cross-platform graphical interface framework called PyQt, <br/>making it compatible with Windows, Linux, and Mac computers.<br/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("AboutDialog", u"@ Valorisation Recherche HSCM, Societe en Commandite - 2024", None))
        self.snooz_version_label.setText(QCoreApplication.translate("AboutDialog", u"<html><head/><body><p>The current version installed :<span style=\" font-weight:600;\"> beta-0.3.0</span></p></body></html>", None))
        self.label_released_version.setText(QCoreApplication.translate("AboutDialog", u"<html><head/><body><p>The latest version released :<span style=\" font-weight:600;\"> beta-0.3.0 </span><span style=\" font-family:'Roboto'; font-size:medium; color:#95a5a6;\">\u00a0(June 21, 2024)</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("AboutDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Click here to download the latest installer </span></p></body></html>", None))
        self.pushButton_windows.setText(QCoreApplication.translate("AboutDialog", u"Download for Windows", None))
        self.pushButton_mac.setText(QCoreApplication.translate("AboutDialog", u"Download for MAC", None))
        self.pushButton_linux.setText(QCoreApplication.translate("AboutDialog", u"Download for Linux", None))
        self.label_2.setText(QCoreApplication.translate("AboutDialog", u"Close the current version before installing the new one to avoid errors.", None))
        self.label_5.setText(QCoreApplication.translate("AboutDialog", u"Once Snooz is installed, make sure to activate the latest version\n"
"of the CEAMS package in the settings by navigating to File > Settings > Packages. ", None))
    # retranslateUi

