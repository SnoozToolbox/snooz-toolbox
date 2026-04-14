# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_OutputFiles.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QDoubleSpinBox,
    QFontComboBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)
import themes_rc

class Ui_OutputFiles(object):
    def setupUi(self, OutputFiles):
        if not OutputFiles.objectName():
            OutputFiles.setObjectName(u"OutputFiles")
        OutputFiles.resize(895, 1161)
        OutputFiles.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_5 = QVBoxLayout(OutputFiles)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.radioButton_report_level = QRadioButton(OutputFiles)
        self.buttonGroup_level = QButtonGroup(OutputFiles)
        self.buttonGroup_level.setObjectName(u"buttonGroup_level")
        self.buttonGroup_level.addButton(self.radioButton_report_level)
        self.radioButton_report_level.setObjectName(u"radioButton_report_level")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.radioButton_report_level.setFont(font)

        self.verticalLayout_10.addWidget(self.radioButton_report_level)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_subject_avg = QCheckBox(OutputFiles)
        self.checkBox_subject_avg.setObjectName(u"checkBox_subject_avg")
        self.checkBox_subject_avg.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_subject_avg)

        self.label_9 = QLabel(OutputFiles)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.label_2 = QLabel(OutputFiles)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.checkBox_subject_sel = QCheckBox(OutputFiles)
        self.checkBox_subject_sel.setObjectName(u"checkBox_subject_sel")
        self.checkBox_subject_sel.setEnabled(True)
        self.checkBox_subject_sel.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_subject_sel)

        self.label_3 = QLabel(OutputFiles)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_10 = QLabel(OutputFiles)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_10.addLayout(self.horizontalLayout)


        self.verticalLayout_8.addLayout(self.verticalLayout_10)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.radioButton_cohort_level = QRadioButton(OutputFiles)
        self.buttonGroup_level.addButton(self.radioButton_cohort_level)
        self.radioButton_cohort_level.setObjectName(u"radioButton_cohort_level")
        self.radioButton_cohort_level.setFont(font)

        self.verticalLayout_11.addWidget(self.radioButton_cohort_level)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox_cohort_avg = QCheckBox(OutputFiles)
        self.checkBox_cohort_avg.setObjectName(u"checkBox_cohort_avg")
        self.checkBox_cohort_avg.setChecked(False)

        self.verticalLayout_2.addWidget(self.checkBox_cohort_avg)

        self.label_11 = QLabel(OutputFiles)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.label_11)

        self.label_19 = QLabel(OutputFiles)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.label_19)

        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.checkBox_cohort_sel = QCheckBox(OutputFiles)
        self.checkBox_cohort_sel.setObjectName(u"checkBox_cohort_sel")
        self.checkBox_cohort_sel.setEnabled(True)

        self.verticalLayout_2.addWidget(self.checkBox_cohort_sel)

        self.label_12 = QLabel(OutputFiles)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.label_12)

        self.label_20 = QLabel(OutputFiles)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.label_20)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_11)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(OutputFiles)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.textEdit = QTextEdit(OutputFiles)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setMaximumSize(QSize(16777215, 100))
        self.textEdit.setTabletTracking(False)
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setLineWidth(0)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_Wake = QCheckBox(OutputFiles)
        self.checkBox_Wake.setObjectName(u"checkBox_Wake")

        self.horizontalLayout_4.addWidget(self.checkBox_Wake)

        self.checkBox_N1 = QCheckBox(OutputFiles)
        self.checkBox_N1.setObjectName(u"checkBox_N1")

        self.horizontalLayout_4.addWidget(self.checkBox_N1)

        self.checkBox_N2 = QCheckBox(OutputFiles)
        self.checkBox_N2.setObjectName(u"checkBox_N2")

        self.horizontalLayout_4.addWidget(self.checkBox_N2)

        self.checkBox_N3 = QCheckBox(OutputFiles)
        self.checkBox_N3.setObjectName(u"checkBox_N3")

        self.horizontalLayout_4.addWidget(self.checkBox_N3)

        self.checkBox_REM = QCheckBox(OutputFiles)
        self.checkBox_REM.setObjectName(u"checkBox_REM")

        self.horizontalLayout_4.addWidget(self.checkBox_REM)

        self.checkBox_Unscored = QCheckBox(OutputFiles)
        self.checkBox_Unscored.setObjectName(u"checkBox_Unscored")

        self.horizontalLayout_4.addWidget(self.checkBox_Unscored)

        self.checkBox_All = QCheckBox(OutputFiles)
        self.checkBox_All.setObjectName(u"checkBox_All")

        self.horizontalLayout_4.addWidget(self.checkBox_All)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(OutputFiles)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_7 = QLabel(OutputFiles)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_17 = QLabel(OutputFiles)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 1, 1, 1, 1)

        self.radioButton_sleep_cycle = QRadioButton(OutputFiles)
        self.buttonGroup_section = QButtonGroup(OutputFiles)
        self.buttonGroup_section.setObjectName(u"buttonGroup_section")
        self.buttonGroup_section.addButton(self.radioButton_sleep_cycle)
        self.radioButton_sleep_cycle.setObjectName(u"radioButton_sleep_cycle")

        self.gridLayout_4.addWidget(self.radioButton_sleep_cycle, 1, 0, 1, 1)

        self.spinBox_sleep_cycle = QSpinBox(OutputFiles)
        self.spinBox_sleep_cycle.setObjectName(u"spinBox_sleep_cycle")

        self.gridLayout_4.addWidget(self.spinBox_sleep_cycle, 1, 2, 1, 1)

        self.spinBox_clock_hour = QSpinBox(OutputFiles)
        self.spinBox_clock_hour.setObjectName(u"spinBox_clock_hour")

        self.gridLayout_4.addWidget(self.spinBox_clock_hour, 2, 2, 1, 1)

        self.spinBox_stage_hour = QSpinBox(OutputFiles)
        self.spinBox_stage_hour.setObjectName(u"spinBox_stage_hour")

        self.gridLayout_4.addWidget(self.spinBox_stage_hour, 3, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.radioButton_stage_hour = QRadioButton(OutputFiles)
        self.buttonGroup_section.addButton(self.radioButton_stage_hour)
        self.radioButton_stage_hour.setObjectName(u"radioButton_stage_hour")

        self.gridLayout_4.addWidget(self.radioButton_stage_hour, 3, 0, 1, 1)

        self.radioButton_total = QRadioButton(OutputFiles)
        self.buttonGroup_section.addButton(self.radioButton_total)
        self.radioButton_total.setObjectName(u"radioButton_total")
        self.radioButton_total.setChecked(True)

        self.gridLayout_4.addWidget(self.radioButton_total, 0, 0, 1, 1)

        self.label_18 = QLabel(OutputFiles)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 3, 1, 1, 1)

        self.radioButton_clock_hour = QRadioButton(OutputFiles)
        self.buttonGroup_section.addButton(self.radioButton_clock_hour)
        self.radioButton_clock_hour.setObjectName(u"radioButton_clock_hour")

        self.gridLayout_4.addWidget(self.radioButton_clock_hour, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 4, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_4)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_9 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_9)

        self.label = QLabel(OutputFiles)
        self.label.setObjectName(u"label")

        self.verticalLayout_8.addWidget(self.label)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.checkBox_force_axis = QCheckBox(OutputFiles)
        self.checkBox_force_axis.setObjectName(u"checkBox_force_axis")

        self.horizontalLayout_14.addWidget(self.checkBox_force_axis)

        self.label_25 = QLabel(OutputFiles)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_25)

        self.doubleSpinBox_xmin = QDoubleSpinBox(OutputFiles)
        self.doubleSpinBox_xmin.setObjectName(u"doubleSpinBox_xmin")
        self.doubleSpinBox_xmin.setEnabled(False)
        self.doubleSpinBox_xmin.setMinimum(-5.000000000000000)
        self.doubleSpinBox_xmin.setMaximum(5.000000000000000)
        self.doubleSpinBox_xmin.setSingleStep(0.500000000000000)

        self.horizontalLayout_14.addWidget(self.doubleSpinBox_xmin)

        self.label_26 = QLabel(OutputFiles)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_26)

        self.doubleSpinBox_xmax = QDoubleSpinBox(OutputFiles)
        self.doubleSpinBox_xmax.setObjectName(u"doubleSpinBox_xmax")
        self.doubleSpinBox_xmax.setEnabled(False)
        self.doubleSpinBox_xmax.setMinimum(-5.000000000000000)
        self.doubleSpinBox_xmax.setMaximum(5.000000000000000)
        self.doubleSpinBox_xmax.setSingleStep(0.500000000000000)

        self.horizontalLayout_14.addWidget(self.doubleSpinBox_xmax)

        self.label_27 = QLabel(OutputFiles)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_27)

        self.doubleSpinBox_ymin = QDoubleSpinBox(OutputFiles)
        self.doubleSpinBox_ymin.setObjectName(u"doubleSpinBox_ymin")
        self.doubleSpinBox_ymin.setEnabled(False)
        self.doubleSpinBox_ymin.setMinimum(-500.000000000000000)
        self.doubleSpinBox_ymin.setMaximum(500.000000000000000)
        self.doubleSpinBox_ymin.setSingleStep(50.000000000000000)

        self.horizontalLayout_14.addWidget(self.doubleSpinBox_ymin)

        self.label_28 = QLabel(OutputFiles)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_28)

        self.doubleSpinBox_ymax = QDoubleSpinBox(OutputFiles)
        self.doubleSpinBox_ymax.setObjectName(u"doubleSpinBox_ymax")
        self.doubleSpinBox_ymax.setEnabled(False)
        self.doubleSpinBox_ymax.setMinimum(-500.000000000000000)
        self.doubleSpinBox_ymax.setMaximum(500.000000000000000)
        self.doubleSpinBox_ymax.setSingleStep(50.000000000000000)

        self.horizontalLayout_14.addWidget(self.doubleSpinBox_ymax)


        self.gridLayout_6.addLayout(self.horizontalLayout_14, 3, 0, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.radioButton_all = QRadioButton(OutputFiles)
        self.buttonGroup_display = QButtonGroup(OutputFiles)
        self.buttonGroup_display.setObjectName(u"buttonGroup_display")
        self.buttonGroup_display.addButton(self.radioButton_all)
        self.radioButton_all.setObjectName(u"radioButton_all")

        self.verticalLayout_13.addWidget(self.radioButton_all)

        self.radioButton_mean = QRadioButton(OutputFiles)
        self.buttonGroup_display.addButton(self.radioButton_mean)
        self.radioButton_mean.setObjectName(u"radioButton_mean")

        self.verticalLayout_13.addWidget(self.radioButton_mean)

        self.radioButton_meanstd = QRadioButton(OutputFiles)
        self.buttonGroup_display.addButton(self.radioButton_meanstd)
        self.radioButton_meanstd.setObjectName(u"radioButton_meanstd")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_meanstd.sizePolicy().hasHeightForWidth())
        self.radioButton_meanstd.setSizePolicy(sizePolicy)
        self.radioButton_meanstd.setMinimumSize(QSize(0, 0))
        self.radioButton_meanstd.setChecked(True)

        self.verticalLayout_13.addWidget(self.radioButton_meanstd)


        self.gridLayout_6.addLayout(self.verticalLayout_13, 1, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.checkBox_log = QCheckBox(OutputFiles)
        self.checkBox_log.setObjectName(u"checkBox_log")

        self.horizontalLayout_13.addWidget(self.checkBox_log)

        self.checkBox_legend = QCheckBox(OutputFiles)
        self.checkBox_legend.setObjectName(u"checkBox_legend")
        self.checkBox_legend.setChecked(False)

        self.horizontalLayout_13.addWidget(self.checkBox_legend)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)


        self.gridLayout_6.addLayout(self.horizontalLayout_13, 2, 0, 1, 1)

        self.horizontalLayout_disp = QHBoxLayout()
        self.horizontalLayout_disp.setObjectName(u"horizontalLayout_disp")
        self.label_13 = QLabel(OutputFiles)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_disp.addWidget(self.label_13)

        self.fontComboBox = QFontComboBox(OutputFiles)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.horizontalLayout_disp.addWidget(self.fontComboBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_disp.addItem(self.horizontalSpacer_5)

        self.label_FontSize = QLabel(OutputFiles)
        self.label_FontSize.setObjectName(u"label_FontSize")

        self.horizontalLayout_disp.addWidget(self.label_FontSize)

        self.spinBox_fontsize = QSpinBox(OutputFiles)
        self.spinBox_fontsize.setObjectName(u"spinBox_fontsize")
        self.spinBox_fontsize.setValue(12)

        self.horizontalLayout_disp.addWidget(self.spinBox_fontsize)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_disp.addItem(self.horizontalSpacer_6)

        self.label_14 = QLabel(OutputFiles)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_disp.addWidget(self.label_14)

        self.label_16 = QLabel(OutputFiles)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_disp.addWidget(self.label_16)

        self.spinBox_figwidth = QSpinBox(OutputFiles)
        self.spinBox_figwidth.setObjectName(u"spinBox_figwidth")
        self.spinBox_figwidth.setValue(8)

        self.horizontalLayout_disp.addWidget(self.spinBox_figwidth)

        self.label_15 = QLabel(OutputFiles)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_disp.addWidget(self.label_15)

        self.spinBox_figheight = QSpinBox(OutputFiles)
        self.spinBox_figheight.setObjectName(u"spinBox_figheight")
        self.spinBox_figheight.setValue(6)

        self.horizontalLayout_disp.addWidget(self.spinBox_figheight)


        self.gridLayout_6.addLayout(self.horizontalLayout_disp, 4, 0, 1, 1)


        self.horizontalLayout_12.addLayout(self.gridLayout_6)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(OutputFiles)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_9.addWidget(self.label_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_output = QLineEdit(OutputFiles)
        self.lineEdit_output.setObjectName(u"lineEdit_output")
        self.lineEdit_output.setMinimumSize(QSize(0, 0))
        self.lineEdit_output.setMaximumSize(QSize(900, 16777215))
        self.lineEdit_output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_output)

        self.pushButton_choose = QPushButton(OutputFiles)
        self.pushButton_choose.setObjectName(u"pushButton_choose")
        self.pushButton_choose.setMinimumSize(QSize(80, 0))
        self.pushButton_choose.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_choose)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.label_5 = QLabel(OutputFiles)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5)


        self.verticalLayout_8.addLayout(self.verticalLayout_9)


        self.verticalLayout_5.addLayout(self.verticalLayout_8)


        self.retranslateUi(OutputFiles)
        self.pushButton_choose.clicked.connect(OutputFiles.choose_slot)
        self.checkBox_cohort_avg.clicked.connect(OutputFiles.out_options_slot)
        self.checkBox_cohort_sel.clicked.connect(OutputFiles.out_options_slot)
        self.checkBox_subject_avg.clicked.connect(OutputFiles.out_options_slot)
        self.checkBox_subject_sel.clicked.connect(OutputFiles.out_options_slot)

        QMetaObject.connectSlotsByName(OutputFiles)
    # setupUi

    def retranslateUi(self, OutputFiles):
        OutputFiles.setWindowTitle("")
        self.radioButton_report_level.setText(QCoreApplication.translate("OutputFiles", u"Group level : to generate pictures for each individual group.", None))
#if QT_CONFIG(tooltip)
        self.checkBox_subject_avg.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.checkBox_subject_avg.setText(QCoreApplication.translate("OutputFiles", u"One picture per group", None))
        self.label_9.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p>All the selected channels or ROIs are illustrated on the same picture.</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p>*The MEAN display option shows the average of all subjects in the group.</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.checkBox_subject_sel.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.checkBox_subject_sel.setText(QCoreApplication.translate("OutputFiles", u"One picture per channel or ROI per group", None))
        self.label_3.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p>All the subjects in a group are illustrated on the same picture.</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p>*The MEAN display option shows the average of all subjects per group For each selected channel.</p></body></html>", None))
        self.radioButton_cohort_level.setText(QCoreApplication.translate("OutputFiles", u"Cohort level : to generate pictures for the cohort.", None))
        self.checkBox_cohort_avg.setText(QCoreApplication.translate("OutputFiles", u"One picture per cohort", None))
        self.label_11.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p>EEG spectral power averaged across channels per group of subjects.</p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p>Each spectral power curve represents the signal averaged across the selected channels or ROIs for a group of subjects.</p></body></html>", None))
        self.checkBox_cohort_sel.setText(QCoreApplication.translate("OutputFiles", u"One picture per channel or ROI", None))
        self.label_12.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p>EEG spectral power per channel per group of subjects.</p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p>Each EEG spectral power curve represents the signal for a selected channel or ROI for a group of subjects.</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:700;\">Sleep Stage Selection</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("OutputFiles", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Note: When N2 and N3 stages are selected together, the generated figure displays only the EEG spectral power data corresponding to the &quot;N2N3&quot; column of the report. Similarly, when N1, N2, and N3 stages are all selected, the figure presents only the data from the &quot;NREM&quot; column.</p></body></html>", None))
        self.checkBox_Wake.setText(QCoreApplication.translate("OutputFiles", u"Wake", None))
        self.checkBox_N1.setText(QCoreApplication.translate("OutputFiles", u"N1", None))
        self.checkBox_N2.setText(QCoreApplication.translate("OutputFiles", u"N2", None))
        self.checkBox_N3.setText(QCoreApplication.translate("OutputFiles", u"N3", None))
        self.checkBox_REM.setText(QCoreApplication.translate("OutputFiles", u"REM", None))
        self.checkBox_Unscored.setText(QCoreApplication.translate("OutputFiles", u"Unscored", None))
        self.checkBox_All.setText(QCoreApplication.translate("OutputFiles", u"All", None))
        self.label_6.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Section to Display</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("OutputFiles", u"Desired Hour", None))
        self.label_17.setText(QCoreApplication.translate("OutputFiles", u"Desired Cycle", None))
        self.radioButton_sleep_cycle.setText(QCoreApplication.translate("OutputFiles", u"Sleep Cycle", None))
        self.radioButton_stage_hour.setText(QCoreApplication.translate("OutputFiles", u"Stage Hour", None))
        self.radioButton_total.setText(QCoreApplication.translate("OutputFiles", u"Total", None))
        self.label_18.setText(QCoreApplication.translate("OutputFiles", u"Desired Hour", None))
        self.radioButton_clock_hour.setText(QCoreApplication.translate("OutputFiles", u"Clock Hour", None))
        self.label.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Display Options</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.checkBox_force_axis.setToolTip(QCoreApplication.translate("OutputFiles", u"Enable this option for consistent axes across all pictures and define the axes limits. Otherwise, the axes are automatically determined based on the data.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_force_axis.setText(QCoreApplication.translate("OutputFiles", u"Force axis limits", None))
        self.label_25.setText(QCoreApplication.translate("OutputFiles", u"x-min:", None))
        self.label_26.setText(QCoreApplication.translate("OutputFiles", u"x-max:", None))
        self.label_27.setText(QCoreApplication.translate("OutputFiles", u"y-min:", None))
        self.label_28.setText(QCoreApplication.translate("OutputFiles", u"y-max:", None))
        self.radioButton_all.setText(QCoreApplication.translate("OutputFiles", u"Display all the EEG spectral power curves on the picture.", None))
        self.radioButton_mean.setText(QCoreApplication.translate("OutputFiles", u"MEAN : Display only the mean of EEG spectral power curve", None))
        self.radioButton_meanstd.setText(QCoreApplication.translate("OutputFiles", u"MEAN + STD : Display the mean of EEG spectral power curve in bold line\n"
"and its standard deviation in a shaded area.", None))
        self.checkBox_log.setText(QCoreApplication.translate("OutputFiles", u"Logarithmic Scale", None))
        self.checkBox_legend.setText(QCoreApplication.translate("OutputFiles", u"Show Legend", None))
        self.label_13.setText(QCoreApplication.translate("OutputFiles", u"Font", None))
        self.label_FontSize.setText(QCoreApplication.translate("OutputFiles", u"Font Size", None))
        self.label_14.setText(QCoreApplication.translate("OutputFiles", u"Figure Size (inch):", None))
        self.label_16.setText(QCoreApplication.translate("OutputFiles", u"Width", None))
        self.label_15.setText(QCoreApplication.translate("OutputFiles", u"Height", None))
        self.label_4.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Ouput folder to save pictures</span></p></body></html>", None))
        self.lineEdit_output.setPlaceholderText(QCoreApplication.translate("OutputFiles", u"Select the folder where the pictures will be saved.", None))
        self.pushButton_choose.setText(QCoreApplication.translate("OutputFiles", u"Choose", None))
        self.label_5.setText(QCoreApplication.translate("OutputFiles", u"Pictures are identified with the basename of the PSG recording and\\or channel label.", None))
    # retranslateUi

