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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_StftResultsView(object):
    def setupUi(self, StftResultsView):
        if not StftResultsView.objectName():
            StftResultsView.setObjectName(u"StftResultsView")
        StftResultsView.resize(668, 105)
        self.gridLayout = QGridLayout(StftResultsView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.time_label = QLabel(StftResultsView)
        self.time_label.setObjectName(u"time_label")

        self.horizontalLayout.addWidget(self.time_label)

        self.time_lineEdit = QLineEdit(StftResultsView)
        self.time_lineEdit.setObjectName(u"time_lineEdit")

        self.horizontalLayout.addWidget(self.time_lineEdit)

        self.previous_pb = QPushButton(StftResultsView)
        self.previous_pb.setObjectName(u"previous_pb")

        self.horizontalLayout.addWidget(self.previous_pb)

        self.next_pb = QPushButton(StftResultsView)
        self.next_pb.setObjectName(u"next_pb")

        self.horizontalLayout.addWidget(self.next_pb)

        self.length_label = QLabel(StftResultsView)
        self.length_label.setObjectName(u"length_label")

        self.horizontalLayout.addWidget(self.length_label)

        self.length_lineEdit = QLineEdit(StftResultsView)
        self.length_lineEdit.setObjectName(u"length_lineEdit")

        self.horizontalLayout.addWidget(self.length_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.log_cb = QCheckBox(StftResultsView)
        self.log_cb.setObjectName(u"log_cb")
        self.log_cb.setCheckable(True)
        self.log_cb.setChecked(True)
        self.log_cb.setTristate(False)

        self.horizontalLayout_2.addWidget(self.log_cb)

        self.zoom_cb = QCheckBox(StftResultsView)
        self.zoom_cb.setObjectName(u"zoom_cb")
        self.zoom_cb.setChecked(True)

        self.horizontalLayout_2.addWidget(self.zoom_cb)

        self.horizontalSpacer_2 = QSpacerItem(98, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.file_label = QLabel(StftResultsView)
        self.file_label.setObjectName(u"file_label")

        self.horizontalLayout_2.addWidget(self.file_label)

        self.filename_lineEdit = QLineEdit(StftResultsView)
        self.filename_lineEdit.setObjectName(u"filename_lineEdit")

        self.horizontalLayout_2.addWidget(self.filename_lineEdit)

        self.choose_pb = QPushButton(StftResultsView)
        self.choose_pb.setObjectName(u"choose_pb")

        self.horizontalLayout_2.addWidget(self.choose_pb)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(StftResultsView)
        self.choose_pb.clicked.connect(StftResultsView.on_choose)
        self.next_pb.clicked.connect(StftResultsView.on_next)
        self.previous_pb.clicked.connect(StftResultsView.on_previous)
        self.time_lineEdit.returnPressed.connect(StftResultsView.on_time_changed)
        self.length_lineEdit.returnPressed.connect(StftResultsView.on_time_changed)
        self.zoom_cb.stateChanged.connect(StftResultsView.on_plot_cb)
        self.log_cb.stateChanged.connect(StftResultsView.on_plot_cb)

        QMetaObject.connectSlotsByName(StftResultsView)
    # setupUi

    def retranslateUi(self, StftResultsView):
        StftResultsView.setWindowTitle(QCoreApplication.translate("StftResultsView", u"Form", None))
        self.time_label.setText(QCoreApplication.translate("StftResultsView", u"Time elapsed (HH:MM:SS)", None))
        self.time_lineEdit.setText(QCoreApplication.translate("StftResultsView", u"00:00:00", None))
        self.previous_pb.setText(QCoreApplication.translate("StftResultsView", u"<<", None))
        self.next_pb.setText(QCoreApplication.translate("StftResultsView", u">>", None))
        self.length_label.setText(QCoreApplication.translate("StftResultsView", u"Window length", None))
        self.length_lineEdit.setText(QCoreApplication.translate("StftResultsView", u"30", None))
        self.log_cb.setText(QCoreApplication.translate("StftResultsView", u"Show log scale", None))
        self.zoom_cb.setText(QCoreApplication.translate("StftResultsView", u"Show <30 Hz", None))
        self.file_label.setText(QCoreApplication.translate("StftResultsView", u"To load another STFT file", None))
        self.filename_lineEdit.setText(QCoreApplication.translate("StftResultsView", u"filename", None))
        self.choose_pb.setText(QCoreApplication.translate("StftResultsView", u"Choose", None))
    # retranslateUi

