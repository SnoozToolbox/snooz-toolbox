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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_RescaleSignalSettingsView(object):
    def setupUi(self, RescaleSignalSettingsView):
        if not RescaleSignalSettingsView.objectName():
            RescaleSignalSettingsView.setObjectName(u"RescaleSignalSettingsView")
        RescaleSignalSettingsView.resize(519, 517)
        self.verticalLayout_8 = QVBoxLayout(RescaleSignalSettingsView)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(RescaleSignalSettingsView)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_8)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.scaling_approach_comboBox = QComboBox(RescaleSignalSettingsView)
        self.scaling_approach_comboBox.addItem("")
        self.scaling_approach_comboBox.addItem("")
        self.scaling_approach_comboBox.addItem("")
        self.scaling_approach_comboBox.setObjectName(u"scaling_approach_comboBox")

        self.gridLayout_5.addWidget(self.scaling_approach_comboBox, 0, 1, 1, 1)

        self.label = QLabel(RescaleSignalSettingsView)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line = QFrame(RescaleSignalSettingsView)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_2 = QLabel(RescaleSignalSettingsView)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(RescaleSignalSettingsView)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.line_2 = QFrame(RescaleSignalSettingsView)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stackedWidget = QStackedWidget(RescaleSignalSettingsView)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.norm_page = QWidget()
        self.norm_page.setObjectName(u"norm_page")
        self.horizontalLayout_5 = QHBoxLayout(self.norm_page)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.norm_copy_checkBox = QCheckBox(self.norm_page)
        self.norm_copy_checkBox.setObjectName(u"norm_copy_checkBox")
        self.norm_copy_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.norm_copy_checkBox, 2, 1, 1, 1)

        self.norm_max_doubleSpinBox = QDoubleSpinBox(self.norm_page)
        self.norm_max_doubleSpinBox.setObjectName(u"norm_max_doubleSpinBox")
        self.norm_max_doubleSpinBox.setDecimals(5)
        self.norm_max_doubleSpinBox.setMinimum(-100000000.000000000000000)
        self.norm_max_doubleSpinBox.setMaximum(100000000.000000000000000)
        self.norm_max_doubleSpinBox.setSingleStep(0.010000000000000)
        self.norm_max_doubleSpinBox.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.norm_max_doubleSpinBox, 1, 1, 1, 1)

        self.norm_copy = QLabel(self.norm_page)
        self.norm_copy.setObjectName(u"norm_copy")
        self.norm_copy.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.norm_copy, 2, 0, 1, 1)

        self.norm_min = QLabel(self.norm_page)
        self.norm_min.setObjectName(u"norm_min")
        self.norm_min.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.norm_min, 0, 0, 1, 1)

        self.norm_min_doubleSpinBox = QDoubleSpinBox(self.norm_page)
        self.norm_min_doubleSpinBox.setObjectName(u"norm_min_doubleSpinBox")
        self.norm_min_doubleSpinBox.setDecimals(5)
        self.norm_min_doubleSpinBox.setMinimum(-100000000.000000000000000)
        self.norm_min_doubleSpinBox.setMaximum(100000000.000000000000000)
        self.norm_min_doubleSpinBox.setSingleStep(0.010000000000000)
        self.norm_min_doubleSpinBox.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.norm_min_doubleSpinBox, 0, 1, 1, 1)

        self.norm_max = QLabel(self.norm_page)
        self.norm_max.setObjectName(u"norm_max")
        self.norm_max.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.norm_max, 1, 0, 1, 1)

        self.norm_clip = QLabel(self.norm_page)
        self.norm_clip.setObjectName(u"norm_clip")
        self.norm_clip.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.norm_clip, 3, 0, 1, 1)

        self.norm_clip_checkBox = QCheckBox(self.norm_page)
        self.norm_clip_checkBox.setObjectName(u"norm_clip_checkBox")

        self.gridLayout.addWidget(self.norm_clip_checkBox, 3, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.stackedWidget.addWidget(self.norm_page)
        self.stand_page = QWidget()
        self.stand_page.setObjectName(u"stand_page")
        self.horizontalLayout_4 = QHBoxLayout(self.stand_page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stand_copy = QLabel(self.stand_page)
        self.stand_copy.setObjectName(u"stand_copy")

        self.gridLayout_2.addWidget(self.stand_copy, 0, 0, 1, 1)

        self.stand_copy_checkBox = QCheckBox(self.stand_page)
        self.stand_copy_checkBox.setObjectName(u"stand_copy_checkBox")
        self.stand_copy_checkBox.setChecked(True)

        self.gridLayout_2.addWidget(self.stand_copy_checkBox, 0, 1, 1, 1)

        self.stand_with_mean = QLabel(self.stand_page)
        self.stand_with_mean.setObjectName(u"stand_with_mean")

        self.gridLayout_2.addWidget(self.stand_with_mean, 1, 0, 1, 1)

        self.stand_with_mean_checkBox = QCheckBox(self.stand_page)
        self.stand_with_mean_checkBox.setObjectName(u"stand_with_mean_checkBox")
        self.stand_with_mean_checkBox.setChecked(True)

        self.gridLayout_2.addWidget(self.stand_with_mean_checkBox, 1, 1, 1, 1)

        self.stand_with_std = QLabel(self.stand_page)
        self.stand_with_std.setObjectName(u"stand_with_std")

        self.gridLayout_2.addWidget(self.stand_with_std, 2, 0, 1, 1)

        self.stand_with_std_checkBox = QCheckBox(self.stand_page)
        self.stand_with_std_checkBox.setObjectName(u"stand_with_std_checkBox")
        self.stand_with_std_checkBox.setChecked(True)

        self.gridLayout_2.addWidget(self.stand_with_std_checkBox, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.stackedWidget.addWidget(self.stand_page)
        self.discr_page = QWidget()
        self.discr_page.setObjectName(u"discr_page")
        self.horizontalLayout_3 = QHBoxLayout(self.discr_page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.discr_n_bins = QLabel(self.discr_page)
        self.discr_n_bins.setObjectName(u"discr_n_bins")

        self.gridLayout_3.addWidget(self.discr_n_bins, 0, 0, 1, 1)

        self.discr_n_bins_spinBox = QSpinBox(self.discr_page)
        self.discr_n_bins_spinBox.setObjectName(u"discr_n_bins_spinBox")
        self.discr_n_bins_spinBox.setMaximum(10000)
        self.discr_n_bins_spinBox.setValue(5)

        self.gridLayout_3.addWidget(self.discr_n_bins_spinBox, 0, 1, 1, 1)

        self.discr_encode = QLabel(self.discr_page)
        self.discr_encode.setObjectName(u"discr_encode")

        self.gridLayout_3.addWidget(self.discr_encode, 1, 0, 1, 1)

        self.discr_encode_comboBox = QComboBox(self.discr_page)
        self.discr_encode_comboBox.addItem("")
        self.discr_encode_comboBox.addItem("")
        self.discr_encode_comboBox.addItem("")
        self.discr_encode_comboBox.setObjectName(u"discr_encode_comboBox")

        self.gridLayout_3.addWidget(self.discr_encode_comboBox, 1, 1, 1, 1)

        self.discr_strategy = QLabel(self.discr_page)
        self.discr_strategy.setObjectName(u"discr_strategy")

        self.gridLayout_3.addWidget(self.discr_strategy, 2, 0, 1, 1)

        self.discr_strategy_comboBox = QComboBox(self.discr_page)
        self.discr_strategy_comboBox.addItem("")
        self.discr_strategy_comboBox.addItem("")
        self.discr_strategy_comboBox.addItem("")
        self.discr_strategy_comboBox.setObjectName(u"discr_strategy_comboBox")

        self.gridLayout_3.addWidget(self.discr_strategy_comboBox, 2, 1, 1, 1)

        self.discr_dtype = QLabel(self.discr_page)
        self.discr_dtype.setObjectName(u"discr_dtype")

        self.gridLayout_3.addWidget(self.discr_dtype, 3, 0, 1, 1)

        self.discr_dtype_comboBox = QComboBox(self.discr_page)
        self.discr_dtype_comboBox.addItem("")
        self.discr_dtype_comboBox.addItem("")
        self.discr_dtype_comboBox.addItem("")
        self.discr_dtype_comboBox.setObjectName(u"discr_dtype_comboBox")

        self.gridLayout_3.addWidget(self.discr_dtype_comboBox, 3, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.stackedWidget.addWidget(self.discr_page)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 1, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_4)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.retranslateUi(RescaleSignalSettingsView)
        self.scaling_approach_comboBox.currentTextChanged.connect(RescaleSignalSettingsView.on_scaling_approach_choose)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(RescaleSignalSettingsView)
    # setupUi

    def retranslateUi(self, RescaleSignalSettingsView):
        RescaleSignalSettingsView.setWindowTitle(QCoreApplication.translate("RescaleSignalSettingsView", u"Form", None))
#if QT_CONFIG(tooltip)
        RescaleSignalSettingsView.setToolTip(QCoreApplication.translate("RescaleSignalSettingsView", u"Normalization : rescaling values from a specified min and max values.\n"
"Standardization : modifying the distribution of the values to have a mean of zero and/or a standard deviation of one.\n"
"Discretization : convert values into a finite set of intervals to limit the number of possible states", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("RescaleSignalSettingsView", u"RescaleSignal settings", None))
        self.scaling_approach_comboBox.setItemText(0, QCoreApplication.translate("RescaleSignalSettingsView", u"Normalization", None))
        self.scaling_approach_comboBox.setItemText(1, QCoreApplication.translate("RescaleSignalSettingsView", u"Standardization", None))
        self.scaling_approach_comboBox.setItemText(2, QCoreApplication.translate("RescaleSignalSettingsView", u"Discretization", None))

        self.label.setText(QCoreApplication.translate("RescaleSignalSettingsView", u"scaling approach", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("RescaleSignalSettingsView", u"Scaling approach", None))
#if QT_CONFIG(tooltip)
        self.norm_copy_checkBox.setToolTip(QCoreApplication.translate("RescaleSignalSettingsView", u"Uncheck to perform inplace otherwise modified values are copied.", None))
#endif // QT_CONFIG(tooltip)
        self.norm_copy_checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.norm_max_doubleSpinBox.setToolTip(QCoreApplication.translate("RescaleSignalSettingsView", u"Maximum of the desired range of transformed data.", None))
#endif // QT_CONFIG(tooltip)
        self.norm_copy.setText(QCoreApplication.translate("RescaleSignalSettingsView", u"copy", None))
        self.norm_min.setText(QCoreApplication.translate("RescaleSignalSettingsView", u"min", None))
#if QT_CONFIG(tooltip)
        self.norm_min_doubleSpinBox.setToolTip(QCoreApplication.translate("RescaleSignalSettingsView", u"Minimum of the desired range of transformed data.", None))
#endif // QT_CONFIG(tooltip)
        self.norm_max.setText(QCoreApplication.translate("RescaleSignalSettingsView", u"max", None))
        self.norm_clip.setText(QCoreApplication.translate("RescaleSignalSettingsView", u"clip", None))
#if QT_CONFIG(tooltip)
        self.norm_clip_checkBox.setToolTip(QCoreApplication.translate("RescaleSignalSettingsView", u"Check to clip transformed values of held-out data to provided feature range.", None))
#endif // QT_CONFIG(tooltip)
        self.norm_clip_checkBox.setText("")
        self.stand_copy.setText(QCoreApplication.translate("RescaleSignalSettingsView", u"copy", None))
#if QT_CONFIG(tooltip)
        self.stand_copy_checkBox.setToolTip(QCoreApplication.translate("RescaleSignalSettingsView", u"Uncheck to perform inplace otherwise modified values are copied.", None))
#endif // QT_CONFIG(tooltip)
        self.stand_copy_checkBox.setText("")
        self.stand_with_mean.setText(QCoreApplication.translate("RescaleSignalSettingsView", u"with_mean", None))
#if QT_CONFIG(tooltip)
        self.stand_with_mean_checkBox.setToolTip(QCoreApplication.translate("RescaleSignalSettingsView", u"Check to center the data before scaling.", None))
#endif // QT_CONFIG(tooltip)
        self.stand_with_mean_checkBox.setText("")
        self.stand_with_std.setText(QCoreApplication.translate("RescaleSignalSettingsView", u"with_std", None))
#if QT_CONFIG(tooltip)
        self.stand_with_std_checkBox.setToolTip(QCoreApplication.translate("RescaleSignalSettingsView", u"Check to scale the data to unit standard deviation.", None))
#endif // QT_CONFIG(tooltip)
        self.stand_with_std_checkBox.setText("")
        self.discr_n_bins.setText(QCoreApplication.translate("RescaleSignalSettingsView", u"number of bins", None))
#if QT_CONFIG(tooltip)
        self.discr_n_bins_spinBox.setToolTip(QCoreApplication.translate("RescaleSignalSettingsView", u"The number of bins to produce. Raises ValueError if n_bins < 2. ", None))
#endif // QT_CONFIG(tooltip)
        self.discr_encode.setText(QCoreApplication.translate("RescaleSignalSettingsView", u"encode", None))
        self.discr_encode_comboBox.setItemText(0, QCoreApplication.translate("RescaleSignalSettingsView", u"onehot", None))
        self.discr_encode_comboBox.setItemText(1, QCoreApplication.translate("RescaleSignalSettingsView", u"onehot-dense", None))
        self.discr_encode_comboBox.setItemText(2, QCoreApplication.translate("RescaleSignalSettingsView", u"ordinal", None))

#if QT_CONFIG(tooltip)
        self.discr_encode_comboBox.setToolTip(QCoreApplication.translate("RescaleSignalSettingsView", u"Method used to encode the transformed result.\n"
"\n"
"onehot\n"
"Encode the transformed result with one-hot encoding and return a sparse matrix. Ignored features are always stacked to the right.\n"
"\n"
"onehot-dense\n"
"Encode the transformed result with one-hot encoding and return a dense array. Ignored features are always stacked to the right.\n"
"\n"
"ordinal\n"
"Return the bin identifier encoded as an integer value.", None))
#endif // QT_CONFIG(tooltip)
        self.discr_strategy.setText(QCoreApplication.translate("RescaleSignalSettingsView", u"strategy", None))
        self.discr_strategy_comboBox.setItemText(0, QCoreApplication.translate("RescaleSignalSettingsView", u"quantile", None))
        self.discr_strategy_comboBox.setItemText(1, QCoreApplication.translate("RescaleSignalSettingsView", u"uniform", None))
        self.discr_strategy_comboBox.setItemText(2, QCoreApplication.translate("RescaleSignalSettingsView", u"kmeans", None))

#if QT_CONFIG(tooltip)
        self.discr_strategy_comboBox.setToolTip(QCoreApplication.translate("RescaleSignalSettingsView", u"Strategy used to define the widths of the bins.\n"
"\n"
"uniform\n"
"All bins in each feature have identical widths.\n"
"\n"
"quantile\n"
"All bins in each feature have the same number of points.\n"
"\n"
"kmeans\n"
"Values in each bin have the same nearest center of a 1D k-means cluster.", None))
#endif // QT_CONFIG(tooltip)
        self.discr_dtype.setText(QCoreApplication.translate("RescaleSignalSettingsView", u"dtype", None))
        self.discr_dtype_comboBox.setItemText(0, QCoreApplication.translate("RescaleSignalSettingsView", u"None", None))
        self.discr_dtype_comboBox.setItemText(1, QCoreApplication.translate("RescaleSignalSettingsView", u"np.float32", None))
        self.discr_dtype_comboBox.setItemText(2, QCoreApplication.translate("RescaleSignalSettingsView", u"np.float64", None))

#if QT_CONFIG(tooltip)
        self.discr_dtype_comboBox.setToolTip(QCoreApplication.translate("RescaleSignalSettingsView", u"The desired data-type for the output. If None, output dtype is consistent with input dtype. Only np.float32 and np.float64 are supported.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

