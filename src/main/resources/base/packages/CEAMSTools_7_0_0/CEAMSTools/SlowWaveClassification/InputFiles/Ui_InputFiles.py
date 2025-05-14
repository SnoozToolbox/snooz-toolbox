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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_InputFiles(object):
    def setupUi(self, InputFiles):
        if not InputFiles.objectName():
            InputFiles.setObjectName(u"InputFiles")
        InputFiles.resize(882, 666)
        self.verticalLayout_4 = QVBoxLayout(InputFiles)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_9 = QLabel(InputFiles)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_4.addWidget(self.label_9)

        self.label_10 = QLabel(InputFiles)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(InputFiles)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(InputFiles)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.tableWidget_char_files = QTableWidget(InputFiles)
        self.tableWidget_char_files.setObjectName(u"tableWidget_char_files")
        self.tableWidget_char_files.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_char_files.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout.addWidget(self.tableWidget_char_files)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_choose = QPushButton(InputFiles)
        self.pushButton_choose.setObjectName(u"pushButton_choose")
        self.pushButton_choose.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_choose)

        self.pushButton_clear = QPushButton(InputFiles)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_clear)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(InputFiles)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_4 = QLabel(InputFiles)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(InputFiles)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_choose_cohort = QPushButton(InputFiles)
        self.pushButton_choose_cohort.setObjectName(u"pushButton_choose_cohort")

        self.horizontalLayout_2.addWidget(self.pushButton_choose_cohort)

        self.lineEdit_cohort_file = QLineEdit(InputFiles)
        self.lineEdit_cohort_file.setObjectName(u"lineEdit_cohort_file")
        self.lineEdit_cohort_file.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_cohort_file)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(InputFiles)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.label_6 = QLabel(InputFiles)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_8 = QLabel(InputFiles)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.tableWidget_stage_files = QTableWidget(InputFiles)
        self.tableWidget_stage_files.setObjectName(u"tableWidget_stage_files")
        self.tableWidget_stage_files.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_stage_files.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_3.addWidget(self.tableWidget_stage_files)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_choose_stage = QPushButton(InputFiles)
        self.pushButton_choose_stage.setObjectName(u"pushButton_choose_stage")
        self.pushButton_choose_stage.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_choose_stage)

        self.pushButton_clear_stage = QPushButton(InputFiles)
        self.pushButton_clear_stage.setObjectName(u"pushButton_clear_stage")
        self.pushButton_clear_stage.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_clear_stage)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 65, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.retranslateUi(InputFiles)
        self.pushButton_clear.clicked.connect(InputFiles.clear_slot)
        self.pushButton_choose.clicked.connect(InputFiles.choose_slot)
        self.pushButton_choose_cohort.clicked.connect(InputFiles.choose_cohort_slot)
        self.pushButton_choose_stage.clicked.connect(InputFiles.choose_stage_slot)
        self.pushButton_clear_stage.clicked.connect(InputFiles.clear_stage_slot)

        QMetaObject.connectSlotsByName(InputFiles)
    # setupUi

    def retranslateUi(self, InputFiles):
        InputFiles.setWindowTitle("")
        InputFiles.setStyleSheet(QCoreApplication.translate("InputFiles", u"font: 12pt \"Roboto\";", None))
        self.label_9.setText(QCoreApplication.translate("InputFiles", u"The classifier uses the files generated by the tool \"Slow Wave Detector\".", None))
        self.label_10.setText(QCoreApplication.translate("InputFiles", u"The slow wave characteristics files, the cohort report and the sleep stages files must have been generated.", None))
        self.label.setText(QCoreApplication.translate("InputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Slow wave characteristics file</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("InputFiles", u"The distribution of transition frequency values is used to classify slow wave events.", None))
        self.pushButton_choose.setText(QCoreApplication.translate("InputFiles", u"Choose", None))
        self.pushButton_clear.setText(QCoreApplication.translate("InputFiles", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("InputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Slow wave cohort report</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("InputFiles", u"The valid duration of each recording, along with the valid duration of each sleep cycle, ", None))
        self.label_5.setText(QCoreApplication.translate("InputFiles", u"are used to compute the slow wave density for each slow wave category.", None))
        self.pushButton_choose_cohort.setText(QCoreApplication.translate("InputFiles", u"Choose", None))
        self.lineEdit_cohort_file.setPlaceholderText(QCoreApplication.translate("InputFiles", u"Choose the cohort report for the slow wave characteristics files loaded above...", None))
        self.label_7.setText(QCoreApplication.translate("InputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep stages file</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("InputFiles", u"The sleep stages file is used to determine the epochs on which the slow wave detector has been run. ", None))
        self.label_8.setText(QCoreApplication.translate("InputFiles", u"The start time and duration of these epochs are necessary for computing the slow wave density per division of the night.", None))
        self.pushButton_choose_stage.setText(QCoreApplication.translate("InputFiles", u"Choose", None))
        self.pushButton_clear_stage.setText(QCoreApplication.translate("InputFiles", u"Clear", None))
    # retranslateUi

