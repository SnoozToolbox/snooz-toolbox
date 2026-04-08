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
from PySide6.QtWidgets import (QApplication, QLabel, QLayout, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_SlowWaveClassifierResultsView(object):
    def setupUi(self, SlowWaveClassifierResultsView):
        if not SlowWaveClassifierResultsView.objectName():
            SlowWaveClassifierResultsView.setObjectName(u"SlowWaveClassifierResultsView")
        SlowWaveClassifierResultsView.resize(809, 1194)
        self.verticalLayout = QVBoxLayout(SlowWaveClassifierResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(SlowWaveClassifierResultsView)
        self.tabWidget.setObjectName(u"tabWidget")
        self.histo_aic_tab = QWidget()
        self.histo_aic_tab.setObjectName(u"histo_aic_tab")
        self.layoutWidget = QWidget(self.histo_aic_tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 751, 651))
        self.result_layout = QVBoxLayout(self.layoutWidget)
        self.result_layout.setObjectName(u"result_layout")
        self.result_layout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.histo_aic_tab, "")
        self.ssw_categories_tab = QWidget()
        self.ssw_categories_tab.setObjectName(u"ssw_categories_tab")
        self.layoutWidget1 = QWidget(self.ssw_categories_tab)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 751, 561))
        self.tables_layout = QVBoxLayout(self.layoutWidget1)
        self.tables_layout.setObjectName(u"tables_layout")
        self.tables_layout.setSizeConstraint(QLayout.SetMaximumSize)
        self.tables_layout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label.setFont(font)

        self.tables_layout.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.tabWidget.addTab(self.ssw_categories_tab, "")
        self.distribution_tab = QWidget()
        self.distribution_tab.setObjectName(u"distribution_tab")
        self.layoutWidget2 = QWidget(self.distribution_tab)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 791, 1161))
        self.distribution_layout = QVBoxLayout(self.layoutWidget2)
        self.distribution_layout.setObjectName(u"distribution_layout")
        self.distribution_layout.setSizeConstraint(QLayout.SetMaximumSize)
        self.distribution_layout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_2.setFont(font1)

        self.distribution_layout.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.distributions_subclass_tabWidget = QTabWidget(self.layoutWidget2)
        self.distributions_subclass_tabWidget.setObjectName(u"distributions_subclass_tabWidget")
        self.distributions_subclass_tabWidget.setEnabled(True)
        self.distributions_subclass_tabWidget.setUsesScrollButtons(False)
        self.distr_time_tab = QWidget()
        self.distr_time_tab.setObjectName(u"distr_time_tab")
        self.distr_time_tab.setEnabled(True)
        self.verticalLayoutWidget_3 = QWidget(self.distr_time_tab)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 781, 1111))
        self.distr_time_layout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.distr_time_layout.setObjectName(u"distr_time_layout")
        self.distr_time_layout.setContentsMargins(0, 0, 0, 0)
        self.distributions_subclass_tabWidget.addTab(self.distr_time_tab, "")
        self.distr_cycles_tab = QWidget()
        self.distr_cycles_tab.setObjectName(u"distr_cycles_tab")
        self.verticalLayoutWidget_2 = QWidget(self.distr_cycles_tab)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 781, 1111))
        self.distr_cycles_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.distr_cycles_layout.setObjectName(u"distr_cycles_layout")
        self.distr_cycles_layout.setContentsMargins(0, 0, 0, 0)
        self.distributions_subclass_tabWidget.addTab(self.distr_cycles_tab, "")
        self.distr_quarter_tab = QWidget()
        self.distr_quarter_tab.setObjectName(u"distr_quarter_tab")
        self.verticalLayoutWidget = QWidget(self.distr_quarter_tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 781, 1111))
        self.distr_quarter_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.distr_quarter_layout.setObjectName(u"distr_quarter_layout")
        self.distr_quarter_layout.setContentsMargins(0, 0, 0, 0)
        self.distributions_subclass_tabWidget.addTab(self.distr_quarter_tab, "")

        self.distribution_layout.addWidget(self.distributions_subclass_tabWidget)

        self.tabWidget.addTab(self.distribution_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(SlowWaveClassifierResultsView)

        self.tabWidget.setCurrentIndex(0)
        self.distributions_subclass_tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(SlowWaveClassifierResultsView)
    # setupUi

    def retranslateUi(self, SlowWaveClassifierResultsView):
        SlowWaveClassifierResultsView.setWindowTitle(QCoreApplication.translate("SlowWaveClassifierResultsView", u"Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.histo_aic_tab), QCoreApplication.translate("SlowWaveClassifierResultsView", u"Histogram and AIC", None))
        self.label.setText(QCoreApplication.translate("SlowWaveClassifierResultsView", u"Data on each slow wave category", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ssw_categories_tab), QCoreApplication.translate("SlowWaveClassifierResultsView", u"Sleep slow wave categories", None))
        self.label_2.setText(QCoreApplication.translate("SlowWaveClassifierResultsView", u"Distribution of each type of slow wave during the night", None))
        self.distributions_subclass_tabWidget.setTabText(self.distributions_subclass_tabWidget.indexOf(self.distr_time_tab), QCoreApplication.translate("SlowWaveClassifierResultsView", u"Distribution by time", None))
        self.distributions_subclass_tabWidget.setTabText(self.distributions_subclass_tabWidget.indexOf(self.distr_cycles_tab), QCoreApplication.translate("SlowWaveClassifierResultsView", u"Distribution by cycles", None))
        self.distributions_subclass_tabWidget.setTabText(self.distributions_subclass_tabWidget.indexOf(self.distr_quarter_tab), QCoreApplication.translate("SlowWaveClassifierResultsView", u"Distribution by quarter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.distribution_tab), QCoreApplication.translate("SlowWaveClassifierResultsView", u"Sleep slow wave distribution", None))
    # retranslateUi

