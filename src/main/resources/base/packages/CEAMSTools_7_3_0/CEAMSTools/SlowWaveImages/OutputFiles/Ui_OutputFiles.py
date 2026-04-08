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
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_OutputFiles(object):
    def setupUi(self, OutputFiles):
        if not OutputFiles.objectName():
            OutputFiles.setObjectName(u"OutputFiles")
        OutputFiles.resize(1045, 923)
        OutputFiles.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_6 = QVBoxLayout(OutputFiles)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkBox_enable_subject = QCheckBox(OutputFiles)
        self.checkBox_enable_subject.setObjectName(u"checkBox_enable_subject")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_enable_subject.sizePolicy().hasHeightForWidth())
        self.checkBox_enable_subject.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.checkBox_enable_subject.setFont(font)

        self.verticalLayout_5.addWidget(self.checkBox_enable_subject)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(OutputFiles)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.radioButton_subject_avg = QRadioButton(OutputFiles)
        self.buttonGroup_subject_pics = QButtonGroup(OutputFiles)
        self.buttonGroup_subject_pics.setObjectName(u"buttonGroup_subject_pics")
        self.buttonGroup_subject_pics.addButton(self.radioButton_subject_avg)
        self.radioButton_subject_avg.setObjectName(u"radioButton_subject_avg")
        self.radioButton_subject_avg.setEnabled(False)
        sizePolicy.setHeightForWidth(self.radioButton_subject_avg.sizePolicy().hasHeightForWidth())
        self.radioButton_subject_avg.setSizePolicy(sizePolicy)
        self.radioButton_subject_avg.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_subject_avg)

        self.label_17 = QLabel(OutputFiles)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout.addWidget(self.label_17)

        self.label_subject_pic_mean = QLabel(OutputFiles)
        self.label_subject_pic_mean.setObjectName(u"label_subject_pic_mean")
        self.label_subject_pic_mean.setFrameShape(QFrame.Shape.NoFrame)
        self.label_subject_pic_mean.setScaledContents(False)

        self.verticalLayout.addWidget(self.label_subject_pic_mean)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_10 = QLabel(OutputFiles)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)

        self.radioButton_subject_sel = QRadioButton(OutputFiles)
        self.buttonGroup_subject_pics.addButton(self.radioButton_subject_sel)
        self.radioButton_subject_sel.setObjectName(u"radioButton_subject_sel")
        self.radioButton_subject_sel.setEnabled(False)
        sizePolicy.setHeightForWidth(self.radioButton_subject_sel.sizePolicy().hasHeightForWidth())
        self.radioButton_subject_sel.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.radioButton_subject_sel)

        self.label_18 = QLabel(OutputFiles)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_4.addWidget(self.label_18)

        self.label_subject_pic_all = QLabel(OutputFiles)
        self.label_subject_pic_all.setObjectName(u"label_subject_pic_all")
        self.label_subject_pic_all.setFrameShape(QFrame.Shape.NoFrame)
        self.label_subject_pic_all.setScaledContents(False)

        self.verticalLayout_4.addWidget(self.label_subject_pic_all)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.line = QFrame(OutputFiles)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.label_2 = QLabel(OutputFiles)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(OutputFiles)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_cohort_pic_all = QLabel(OutputFiles)
        self.label_cohort_pic_all.setObjectName(u"label_cohort_pic_all")
        self.label_cohort_pic_all.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_cohort_pic_all.sizePolicy().hasHeightForWidth())
        self.label_cohort_pic_all.setSizePolicy(sizePolicy1)
        self.label_cohort_pic_all.setMinimumSize(QSize(0, 0))
        self.label_cohort_pic_all.setMaximumSize(QSize(16777215, 16777215))
        self.label_cohort_pic_all.setFrameShape(QFrame.Shape.NoFrame)
        self.label_cohort_pic_all.setScaledContents(False)
        self.label_cohort_pic_all.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_cohort_pic_all, 3, 1, 1, 1)

        self.radioButton_all = QRadioButton(OutputFiles)
        self.buttonGroup_mean = QButtonGroup(OutputFiles)
        self.buttonGroup_mean.setObjectName(u"buttonGroup_mean")
        self.buttonGroup_mean.addButton(self.radioButton_all)
        self.radioButton_all.setObjectName(u"radioButton_all")

        self.gridLayout.addWidget(self.radioButton_all, 0, 1, 1, 1)

        self.radioButton_mean = QRadioButton(OutputFiles)
        self.buttonGroup_mean.addButton(self.radioButton_mean)
        self.radioButton_mean.setObjectName(u"radioButton_mean")

        self.gridLayout.addWidget(self.radioButton_mean, 1, 0, 1, 1)

        self.radioButton_meanstd = QRadioButton(OutputFiles)
        self.buttonGroup_mean.addButton(self.radioButton_meanstd)
        self.radioButton_meanstd.setObjectName(u"radioButton_meanstd")
        sizePolicy.setHeightForWidth(self.radioButton_meanstd.sizePolicy().hasHeightForWidth())
        self.radioButton_meanstd.setSizePolicy(sizePolicy)
        self.radioButton_meanstd.setMinimumSize(QSize(0, 0))
        self.radioButton_meanstd.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_meanstd, 0, 0, 1, 1)

        self.label_cohort_pic_shade = QLabel(OutputFiles)
        self.label_cohort_pic_shade.setObjectName(u"label_cohort_pic_shade")
        sizePolicy1.setHeightForWidth(self.label_cohort_pic_shade.sizePolicy().hasHeightForWidth())
        self.label_cohort_pic_shade.setSizePolicy(sizePolicy1)
        self.label_cohort_pic_shade.setMinimumSize(QSize(0, 0))
        self.label_cohort_pic_shade.setMaximumSize(QSize(16777215, 16777215))
        self.label_cohort_pic_shade.setFrameShape(QFrame.Shape.NoFrame)
        self.label_cohort_pic_shade.setScaledContents(False)

        self.gridLayout.addWidget(self.label_cohort_pic_shade, 3, 0, 1, 1)

        self.label_6 = QLabel(OutputFiles)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_7 = QLabel(OutputFiles)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.label_11 = QLabel(OutputFiles)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_2.addWidget(self.label_11)

        self.checkBox_cohort_avg = QCheckBox(OutputFiles)
        self.checkBox_cohort_avg.setObjectName(u"checkBox_cohort_avg")
        sizePolicy.setHeightForWidth(self.checkBox_cohort_avg.sizePolicy().hasHeightForWidth())
        self.checkBox_cohort_avg.setSizePolicy(sizePolicy)
        self.checkBox_cohort_avg.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_cohort_avg)

        self.label_12 = QLabel(OutputFiles)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_2.addWidget(self.label_12)

        self.checkBox_cohort_sel = QCheckBox(OutputFiles)
        self.checkBox_cohort_sel.setObjectName(u"checkBox_cohort_sel")
        sizePolicy.setHeightForWidth(self.checkBox_cohort_sel.sizePolicy().hasHeightForWidth())
        self.checkBox_cohort_sel.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.checkBox_cohort_sel)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.line_2 = QFrame(OutputFiles)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(OutputFiles)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)

        self.verticalLayout_7.addWidget(self.label_8)

        self.checkBox_category = QCheckBox(OutputFiles)
        self.checkBox_category.setObjectName(u"checkBox_category")
        sizePolicy.setHeightForWidth(self.checkBox_category.sizePolicy().hasHeightForWidth())
        self.checkBox_category.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.checkBox_category)


        self.verticalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_9)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(OutputFiles)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.checkBox_inverse = QCheckBox(OutputFiles)
        self.checkBox_inverse.setObjectName(u"checkBox_inverse")
        sizePolicy.setHeightForWidth(self.checkBox_inverse.sizePolicy().hasHeightForWidth())
        self.checkBox_inverse.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.checkBox_inverse)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_force_axis = QCheckBox(OutputFiles)
        self.checkBox_force_axis.setObjectName(u"checkBox_force_axis")
        sizePolicy.setHeightForWidth(self.checkBox_force_axis.sizePolicy().hasHeightForWidth())
        self.checkBox_force_axis.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.checkBox_force_axis)

        self.label_13 = QLabel(OutputFiles)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_13)

        self.doubleSpinBox_xmin = QDoubleSpinBox(OutputFiles)
        self.doubleSpinBox_xmin.setObjectName(u"doubleSpinBox_xmin")
        self.doubleSpinBox_xmin.setEnabled(False)
        self.doubleSpinBox_xmin.setMinimum(-5.000000000000000)
        self.doubleSpinBox_xmin.setMaximum(5.000000000000000)
        self.doubleSpinBox_xmin.setSingleStep(0.500000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_xmin)

        self.label_14 = QLabel(OutputFiles)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_14)

        self.doubleSpinBox_xmax = QDoubleSpinBox(OutputFiles)
        self.doubleSpinBox_xmax.setObjectName(u"doubleSpinBox_xmax")
        self.doubleSpinBox_xmax.setEnabled(False)
        self.doubleSpinBox_xmax.setMinimum(-5.000000000000000)
        self.doubleSpinBox_xmax.setMaximum(5.000000000000000)
        self.doubleSpinBox_xmax.setSingleStep(0.500000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_xmax)

        self.label_15 = QLabel(OutputFiles)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_15)

        self.doubleSpinBox_ymin = QDoubleSpinBox(OutputFiles)
        self.doubleSpinBox_ymin.setObjectName(u"doubleSpinBox_ymin")
        self.doubleSpinBox_ymin.setEnabled(False)
        self.doubleSpinBox_ymin.setMinimum(-500.000000000000000)
        self.doubleSpinBox_ymin.setMaximum(500.000000000000000)
        self.doubleSpinBox_ymin.setSingleStep(50.000000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_ymin)

        self.label_16 = QLabel(OutputFiles)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_16)

        self.doubleSpinBox_ymax = QDoubleSpinBox(OutputFiles)
        self.doubleSpinBox_ymax.setObjectName(u"doubleSpinBox_ymax")
        self.doubleSpinBox_ymax.setEnabled(False)
        self.doubleSpinBox_ymax.setMinimum(-500.000000000000000)
        self.doubleSpinBox_ymax.setMaximum(500.000000000000000)
        self.doubleSpinBox_ymax.setSingleStep(50.000000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_ymax)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

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


        self.verticalLayout_5.addLayout(self.verticalLayout_9)

        self.verticalSpacer_2 = QSpacerItem(20, 126, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.retranslateUi(OutputFiles)
        self.pushButton_choose.clicked.connect(OutputFiles.choose_slot)
        self.checkBox_cohort_avg.clicked.connect(OutputFiles.out_options_slot)
        self.checkBox_cohort_sel.clicked.connect(OutputFiles.out_options_slot)
        self.buttonGroup_mean.buttonClicked.connect(OutputFiles.out_options_slot)
        self.checkBox_force_axis.clicked.connect(OutputFiles.out_options_slot)
        self.checkBox_enable_subject.clicked.connect(OutputFiles.out_options_slot)

        QMetaObject.connectSlotsByName(OutputFiles)
    # setupUi

    def retranslateUi(self, OutputFiles):
        OutputFiles.setWindowTitle("")
        self.checkBox_enable_subject.setText(QCoreApplication.translate("OutputFiles", u"Subject Level : to generate pictures for each individual subject.", None))
        self.label_9.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">One picture per subject</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.radioButton_subject_avg.setToolTip(QCoreApplication.translate("OutputFiles", u"Check the display option 'MEAN' in order to check this option.", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_subject_avg.setText(QCoreApplication.translate("OutputFiles", u"All channels or ROIs are shown on the same figure.\n"
"Useful for exploring topographic differences.\n"
"The mean and standard deviation (STD) across SW\n"
"for each channel or ROI are displayed.", None))
        self.label_17.setText(QCoreApplication.translate("OutputFiles", u"Example of a figure showing the averaged SW for two channels.", None))
        self.label_subject_pic_mean.setText("")
        self.label_10.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">One picture per channel or ROI</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.radioButton_subject_sel.setToolTip(QCoreApplication.translate("OutputFiles", u"Check the display option 'Display all the SW' in order to check this option.", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_subject_sel.setText(QCoreApplication.translate("OutputFiles", u"Useful for exploring the set of SW events to identify outliers or artifacts.\n"
"All SW curves are displayed.", None))
        self.label_18.setText(QCoreApplication.translate("OutputFiles", u"Example of a figure showing all SW detected for one channel.", None))
        self.label_subject_pic_all.setText("")
        self.label_2.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p>Cohort level : to generate pictures for the cohort, groups are all displayed on the same picture.</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:700;\">Display Options</span></p></body></html>", None))
        self.label_cohort_pic_all.setText("")
        self.radioButton_all.setText(QCoreApplication.translate("OutputFiles", u"Display all the SW signal curves on the picture.", None))
        self.radioButton_mean.setText(QCoreApplication.translate("OutputFiles", u"MEAN : Display only the mean SW curve", None))
        self.radioButton_meanstd.setText(QCoreApplication.translate("OutputFiles", u"MEAN + STD : Display the mean SW curve in bold line\n"
"and the SW curve standard deviation in gray shaded area.", None))
        self.label_cohort_pic_shade.setText("")
        self.label_6.setText(QCoreApplication.translate("OutputFiles", u"Example of a figure showing the averaged SW for each group.\n"
"Average and STD displayed are across the subjects of each group.", None))
        self.label_7.setText(QCoreApplication.translate("OutputFiles", u"Example of a figure showing the averaged SW of each recording.\n"
"The averaged curve is computed across all channels.", None))
        self.label_11.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">One picture per cohort</span></p></body></html>", None))
        self.checkBox_cohort_avg.setText(QCoreApplication.translate("OutputFiles", u"SW averaged across channels per group of subjects. Each curve represents the signal averaged accross all the channels or ROIs.", None))
        self.label_12.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">One picture per channel or ROI</span></p></body></html>", None))
        self.checkBox_cohort_sel.setText(QCoreApplication.translate("OutputFiles", u"SW per channel per group of subjects. Each curve represents the signal for a selected channel or ROI.", None))
        self.label_8.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Slow wave category</span></p></body></html>", None))
        self.checkBox_category.setText(QCoreApplication.translate("OutputFiles", u"Differentiate SW categories: use patterned colors to distinguish SW with different transition frequencies (when this information is available).", None))
        self.label.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Axes Options</span></p></body></html>", None))
        self.checkBox_inverse.setText(QCoreApplication.translate("OutputFiles", u"Inverse the SW signal curves to display negative up.", None))
#if QT_CONFIG(tooltip)
        self.checkBox_force_axis.setToolTip(QCoreApplication.translate("OutputFiles", u"Enable this option for consistent axes across all pictures and define the axes limits. Otherwise, the axes are automatically determined based on the data.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_force_axis.setText(QCoreApplication.translate("OutputFiles", u"Force axis limits", None))
        self.label_13.setText(QCoreApplication.translate("OutputFiles", u"x-min:", None))
        self.label_14.setText(QCoreApplication.translate("OutputFiles", u"x-max:", None))
        self.label_15.setText(QCoreApplication.translate("OutputFiles", u"y-min:", None))
        self.label_16.setText(QCoreApplication.translate("OutputFiles", u"y-max:", None))
        self.label_4.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Ouput folder to save pictures</span></p></body></html>", None))
        self.lineEdit_output.setPlaceholderText(QCoreApplication.translate("OutputFiles", u"Select the folder where the pictures will be saved.", None))
        self.pushButton_choose.setText(QCoreApplication.translate("OutputFiles", u"Choose", None))
        self.label_5.setText(QCoreApplication.translate("OutputFiles", u"Pictures are identified with the basename of the PSG recording and\\or channel label.", None))
    # retranslateUi

