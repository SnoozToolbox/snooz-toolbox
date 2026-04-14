# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_OxygenDesatDetectorResultsView.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from widgets.QLineEditLive import QLineEditLive

class Ui_OxygenDesatDetectorResultsView(object):
    def setupUi(self, OxygenDesatDetectorResultsView):
        if not OxygenDesatDetectorResultsView.objectName():
            OxygenDesatDetectorResultsView.setObjectName(u"OxygenDesatDetectorResultsView")
        OxygenDesatDetectorResultsView.resize(864, 190)
        self.gridLayout = QGridLayout(OxygenDesatDetectorResultsView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(OxygenDesatDetectorResultsView)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.time_label = QLabel(OxygenDesatDetectorResultsView)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.time_label)

        self.time_lineedit = QLineEditLive(OxygenDesatDetectorResultsView)
        self.time_lineedit.setObjectName(u"time_lineedit")
        self.time_lineedit.setEnabled(True)
        self.time_lineedit.setMaximumSize(QSize(100, 16777215))
        self.time_lineedit.setText(u"00:00:00")

        self.horizontalLayout_3.addWidget(self.time_lineedit)

        self.duration_label = QLabel(OxygenDesatDetectorResultsView)
        self.duration_label.setObjectName(u"duration_label")

        self.horizontalLayout_3.addWidget(self.duration_label)

        self.comboBox_duration = QComboBox(OxygenDesatDetectorResultsView)
        self.comboBox_duration.addItem("")
        self.comboBox_duration.addItem("")
        self.comboBox_duration.addItem("")
        self.comboBox_duration.addItem("")
        self.comboBox_duration.addItem("")
        self.comboBox_duration.setObjectName(u"comboBox_duration")

        self.horizontalLayout_3.addWidget(self.comboBox_duration)

        self.checkBox_ylim_norm = QCheckBox(OxygenDesatDetectorResultsView)
        self.checkBox_ylim_norm.setObjectName(u"checkBox_ylim_norm")
        self.checkBox_ylim_norm.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_ylim_norm)

        self.lineEdit_ylim_fixed = QLineEdit(OxygenDesatDetectorResultsView)
        self.lineEdit_ylim_fixed.setObjectName(u"lineEdit_ylim_fixed")
        self.lineEdit_ylim_fixed.setEnabled(False)
        self.lineEdit_ylim_fixed.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_ylim_fixed)

        self.checkBox_display_y = QCheckBox(OxygenDesatDetectorResultsView)
        self.checkBox_display_y.setObjectName(u"checkBox_display_y")

        self.horizontalLayout_3.addWidget(self.checkBox_display_y)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")
        self.result_layout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)

        self.verticalLayout.addLayout(self.result_layout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(OxygenDesatDetectorResultsView)
        self.time_lineedit.editingFinished.connect(OxygenDesatDetectorResultsView.time_elapsed_change_slot)
        self.comboBox_duration.currentIndexChanged.connect(OxygenDesatDetectorResultsView.duration_change_slot)
        self.checkBox_ylim_norm.clicked.connect(OxygenDesatDetectorResultsView.y_limit_enable_slot)
        self.lineEdit_ylim_fixed.editingFinished.connect(OxygenDesatDetectorResultsView.y_limits_change_slot)
        self.checkBox_display_y.clicked.connect(OxygenDesatDetectorResultsView.y_label_slot)

        QMetaObject.connectSlotsByName(OxygenDesatDetectorResultsView)
    # setupUi

    def retranslateUi(self, OxygenDesatDetectorResultsView):
        OxygenDesatDetectorResultsView.setWindowTitle(QCoreApplication.translate("OxygenDesatDetectorResultsView", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("OxygenDesatDetectorResultsView", u"Display signals", None))
        self.time_label.setText(QCoreApplication.translate("OxygenDesatDetectorResultsView", u"Time elapsed (HH:MM:SS)", None))
#if QT_CONFIG(tooltip)
        self.time_lineedit.setToolTip(QCoreApplication.translate("OxygenDesatDetectorResultsView", u"Time elapsed since the beginning of the recording (ex. 01:10:5.5)\n"
"Press enter to display the detection window.", None))
#endif // QT_CONFIG(tooltip)
        self.duration_label.setText(QCoreApplication.translate("OxygenDesatDetectorResultsView", u"Duration (sec)", None))
        self.comboBox_duration.setItemText(0, QCoreApplication.translate("OxygenDesatDetectorResultsView", u"30", None))
        self.comboBox_duration.setItemText(1, QCoreApplication.translate("OxygenDesatDetectorResultsView", u"150", None))
        self.comboBox_duration.setItemText(2, QCoreApplication.translate("OxygenDesatDetectorResultsView", u"300", None))
        self.comboBox_duration.setItemText(3, QCoreApplication.translate("OxygenDesatDetectorResultsView", u"1800", None))
        self.comboBox_duration.setItemText(4, QCoreApplication.translate("OxygenDesatDetectorResultsView", u"3600", None))

        self.checkBox_ylim_norm.setText(QCoreApplication.translate("OxygenDesatDetectorResultsView", u"Normalize y limits", None))
        self.checkBox_display_y.setText(QCoreApplication.translate("OxygenDesatDetectorResultsView", u"Display y axis", None))
    # retranslateUi

