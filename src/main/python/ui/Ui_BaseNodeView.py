# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_BaseNodeView.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_BaseNodeView(object):
    def setupUi(self, BaseNodeView):
        if not BaseNodeView.objectName():
            BaseNodeView.setObjectName(u"BaseNodeView")
        BaseNodeView.setWindowModality(Qt.NonModal)
        BaseNodeView.resize(677, 379)
        self.horizontalLayout = QHBoxLayout(BaseNodeView)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(BaseNodeView)
        self.tabWidget.setObjectName(u"tabWidget")
        self.settings_tab = QWidget()
        self.settings_tab.setObjectName(u"settings_tab")
        self.verticalLayout_2 = QVBoxLayout(self.settings_tab)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settings_main_layout = QVBoxLayout()
        self.settings_main_layout.setSpacing(0)
        self.settings_main_layout.setObjectName(u"settings_main_layout")
        self.settings_layout = QVBoxLayout()
        self.settings_layout.setObjectName(u"settings_layout")

        self.settings_main_layout.addLayout(self.settings_layout)

        self.line = QFrame(self.settings_tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.settings_main_layout.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.cancel_settings_pushbutton = QPushButton(self.settings_tab)
        self.cancel_settings_pushbutton.setObjectName(u"cancel_settings_pushbutton")

        self.horizontalLayout_3.addWidget(self.cancel_settings_pushbutton)

        self.apply_settings_pushbutton = QPushButton(self.settings_tab)
        self.apply_settings_pushbutton.setObjectName(u"apply_settings_pushbutton")

        self.horizontalLayout_3.addWidget(self.apply_settings_pushbutton)


        self.settings_main_layout.addLayout(self.horizontalLayout_3)

        self.settings_main_layout.setStretch(0, 1)

        self.verticalLayout_2.addLayout(self.settings_main_layout)

        self.tabWidget.addTab(self.settings_tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_6 = QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.results_layout = QVBoxLayout()
        self.results_layout.setSpacing(0)
        self.results_layout.setObjectName(u"results_layout")

        self.verticalLayout_6.addLayout(self.results_layout)

        self.tabWidget.addTab(self.tab_2, "")
        self.logs_tab = QWidget()
        self.logs_tab.setObjectName(u"logs_tab")
        self.verticalLayout_5 = QVBoxLayout(self.logs_tab)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.logs_textedit = QTextEdit(self.logs_tab)
        self.logs_textedit.setObjectName(u"logs_textedit")
        font = QFont()
        font.setFamilies([u"Courier 10 Pitch"])
        self.logs_textedit.setFont(font)
        self.logs_textedit.setReadOnly(True)
        self.logs_textedit.setAcceptRichText(False)

        self.verticalLayout_4.addWidget(self.logs_textedit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.clear_pushbutton = QPushButton(self.logs_tab)
        self.clear_pushbutton.setObjectName(u"clear_pushbutton")

        self.horizontalLayout_2.addWidget(self.clear_pushbutton)

        self.save_pushbutton = QPushButton(self.logs_tab)
        self.save_pushbutton.setObjectName(u"save_pushbutton")

        self.horizontalLayout_2.addWidget(self.save_pushbutton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.logs_tab, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(BaseNodeView)
        self.clear_pushbutton.clicked.connect(BaseNodeView.on_clear_logs)
        self.save_pushbutton.clicked.connect(BaseNodeView.on_save_logs)
        self.apply_settings_pushbutton.clicked.connect(BaseNodeView.on_apply_settings)
        self.cancel_settings_pushbutton.clicked.connect(BaseNodeView.on_cancel_settings)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(BaseNodeView)
    # setupUi

    def retranslateUi(self, BaseNodeView):
        BaseNodeView.setWindowTitle(QCoreApplication.translate("BaseNodeView", u"BaseNodeView", None))
        self.cancel_settings_pushbutton.setText(QCoreApplication.translate("BaseNodeView", u"Cancel", None))
        self.apply_settings_pushbutton.setText(QCoreApplication.translate("BaseNodeView", u"Apply", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), QCoreApplication.translate("BaseNodeView", u"Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("BaseNodeView", u"Results", None))
        self.clear_pushbutton.setText(QCoreApplication.translate("BaseNodeView", u"Clear", None))
        self.save_pushbutton.setText(QCoreApplication.translate("BaseNodeView", u"Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.logs_tab), QCoreApplication.translate("BaseNodeView", u"Logs", None))
    # retranslateUi

