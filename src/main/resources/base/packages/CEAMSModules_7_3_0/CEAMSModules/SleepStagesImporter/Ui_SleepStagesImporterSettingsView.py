# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SleepStagesImporterSettingsView.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QSplitter, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
import themes_rc

class Ui_SleepStagesImporterSettingsView(object):
    def setupUi(self, SleepStagesImporterSettingsView):
        if not SleepStagesImporterSettingsView.objectName():
            SleepStagesImporterSettingsView.setObjectName(u"SleepStagesImporterSettingsView")
        SleepStagesImporterSettingsView.resize(871, 664)
        SleepStagesImporterSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout_2 = QHBoxLayout(SleepStagesImporterSettingsView)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.splitter = QSplitter(SleepStagesImporterSettingsView)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(30)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.tableWidget_files = QTableWidget(self.layoutWidget)
        self.tableWidget_files.setObjectName(u"tableWidget_files")
        self.tableWidget_files.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget_files.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout_3.addWidget(self.tableWidget_files)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_choose = QPushButton(self.layoutWidget)
        self.pushButton_choose.setObjectName(u"pushButton_choose")
        self.pushButton_choose.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_choose)

        self.pushButton_clear = QPushButton(self.layoutWidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_clear)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(250, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout.addWidget(self.label_16)

        self.label_17 = QLabel(self.layoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout.addWidget(self.label_17)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_prefix = QLineEdit(self.layoutWidget)
        self.lineEdit_prefix.setObjectName(u"lineEdit_prefix")

        self.gridLayout_3.addWidget(self.lineEdit_prefix, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.label_18 = QLabel(self.layoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(50, 0))

        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_19 = QLabel(self.layoutWidget)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 1, 0, 1, 1)

        self.lineEdit_suffix = QLineEdit(self.layoutWidget)
        self.lineEdit_suffix.setObjectName(u"lineEdit_suffix")

        self.gridLayout_3.addWidget(self.lineEdit_suffix, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.checkBox_case_sensitive = QCheckBox(self.layoutWidget)
        self.checkBox_case_sensitive.setObjectName(u"checkBox_case_sensitive")
        self.checkBox_case_sensitive.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox_case_sensitive)

        self.textEdit = QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_ori_3 = QLineEdit(self.layoutWidget1)
        self.lineEdit_ori_3.setObjectName(u"lineEdit_ori_3")
        self.lineEdit_ori_3.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_ori_3, 5, 1, 1, 1)

        self.label_10 = QLabel(self.layoutWidget1)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 7, 3, 1, 1)

        self.label_37 = QLabel(self.layoutWidget1)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_2.addWidget(self.label_37, 5, 0, 1, 1)

        self.lineEdit_ori_5 = QLineEdit(self.layoutWidget1)
        self.lineEdit_ori_5.setObjectName(u"lineEdit_ori_5")
        self.lineEdit_ori_5.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_ori_5, 6, 1, 1, 1)

        self.label_0 = QLabel(self.layoutWidget1)
        self.label_0.setObjectName(u"label_0")
        self.label_0.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_2.addWidget(self.label_0, 2, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 3, 4, 1, 1)

        self.label_42 = QLabel(self.layoutWidget1)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_2.addWidget(self.label_42, 9, 0, 1, 1)

        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 8, 3, 1, 1)

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 4, 3, 1, 1)

        self.label_34 = QLabel(self.layoutWidget1)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_2.addWidget(self.label_34, 2, 0, 1, 1)

        self.lineEdit_ori_9 = QLineEdit(self.layoutWidget1)
        self.lineEdit_ori_9.setObjectName(u"lineEdit_ori_9")
        self.lineEdit_ori_9.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_ori_9, 9, 1, 1, 1)

        self.line_2 = QFrame(self.layoutWidget1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 1, 0, 1, 1)

        self.label_35 = QLabel(self.layoutWidget1)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_2.addWidget(self.label_35, 3, 0, 1, 1)

        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_43 = QLabel(self.layoutWidget1)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(100, 16777215))
        self.label_43.setFont(font)

        self.gridLayout_2.addWidget(self.label_43, 0, 1, 1, 1)

        self.lineEdit_ori_7 = QLineEdit(self.layoutWidget1)
        self.lineEdit_ori_7.setObjectName(u"lineEdit_ori_7")
        self.lineEdit_ori_7.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_ori_7, 8, 1, 1, 1)

        self.lineEdit_ori_6 = QLineEdit(self.layoutWidget1)
        self.lineEdit_ori_6.setObjectName(u"lineEdit_ori_6")
        self.lineEdit_ori_6.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_ori_6, 7, 1, 1, 1)

        self.label_40 = QLabel(self.layoutWidget1)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_2.addWidget(self.label_40, 7, 0, 1, 1)

        self.lineEdit_ori_1 = QLineEdit(self.layoutWidget1)
        self.lineEdit_ori_1.setObjectName(u"lineEdit_ori_1")
        self.lineEdit_ori_1.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_ori_1, 3, 1, 1, 1)

        self.label_1 = QLabel(self.layoutWidget1)
        self.label_1.setObjectName(u"label_1")

        self.gridLayout_2.addWidget(self.label_1, 3, 3, 1, 1)

        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 5, 3, 1, 1)

        self.lineEdit_ori_0 = QLineEdit(self.layoutWidget1)
        self.lineEdit_ori_0.setObjectName(u"lineEdit_ori_0")
        self.lineEdit_ori_0.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_ori_0, 2, 1, 1, 1)

        self.lineEdit_ori_2 = QLineEdit(self.layoutWidget1)
        self.lineEdit_ori_2.setObjectName(u"lineEdit_ori_2")
        self.lineEdit_ori_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_ori_2, 4, 1, 1, 1)

        self.label_46 = QLabel(self.layoutWidget1)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font)

        self.gridLayout_2.addWidget(self.label_46, 0, 3, 1, 1)

        self.line_3 = QFrame(self.layoutWidget1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 1, 3, 1, 1)

        self.label_12 = QLabel(self.layoutWidget1)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 9, 3, 1, 1)

        self.label_36 = QLabel(self.layoutWidget1)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_2.addWidget(self.label_36, 4, 0, 1, 1)

        self.label_41 = QLabel(self.layoutWidget1)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(90, 0))

        self.gridLayout_2.addWidget(self.label_41, 8, 0, 1, 1)

        self.line = QFrame(self.layoutWidget1)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 1, 1, 1)

        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 6, 3, 1, 1)

        self.label_39 = QLabel(self.layoutWidget1)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_2.addWidget(self.label_39, 6, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(250, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.spinBox_colstage = QSpinBox(self.layoutWidget1)
        self.spinBox_colstage.setObjectName(u"spinBox_colstage")
        self.spinBox_colstage.setMinimum(1)

        self.gridLayout.addWidget(self.spinBox_colstage, 4, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(220, 0))

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.comboBox_sep = QComboBox(self.layoutWidget1)
        self.comboBox_sep.addItem("")
        self.comboBox_sep.addItem("")
        self.comboBox_sep.addItem("")
        self.comboBox_sep.addItem("")
        self.comboBox_sep.addItem("")
        self.comboBox_sep.setObjectName(u"comboBox_sep")

        self.gridLayout.addWidget(self.comboBox_sep, 2, 1, 1, 1)

        self.label_14 = QLabel(self.layoutWidget1)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 4, 0, 1, 1)

        self.comboBox_stage_s = QComboBox(self.layoutWidget1)
        self.comboBox_stage_s.addItem("")
        self.comboBox_stage_s.addItem("")
        self.comboBox_stage_s.addItem("")
        self.comboBox_stage_s.addItem("")
        self.comboBox_stage_s.addItem("")
        self.comboBox_stage_s.addItem("")
        self.comboBox_stage_s.addItem("")
        self.comboBox_stage_s.addItem("")
        self.comboBox_stage_s.setObjectName(u"comboBox_stage_s")

        self.gridLayout.addWidget(self.comboBox_stage_s, 5, 1, 1, 1)

        self.spinBox_n_rows = QSpinBox(self.layoutWidget1)
        self.spinBox_n_rows.setObjectName(u"spinBox_n_rows")

        self.gridLayout.addWidget(self.spinBox_n_rows, 0, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.comboBox_encoding = QComboBox(self.layoutWidget1)
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.setObjectName(u"comboBox_encoding")

        self.gridLayout.addWidget(self.comboBox_encoding, 3, 1, 1, 1)

        self.label_13 = QLabel(self.layoutWidget1)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 3, 0, 1, 1)

        self.label_15 = QLabel(self.layoutWidget1)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 5, 0, 1, 1)

        self.label_20 = QLabel(self.layoutWidget1)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.gridLayout.addWidget(self.label_20, 1, 0, 1, 2)


        self.verticalLayout_6.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.splitter.addWidget(self.layoutWidget1)

        self.horizontalLayout_2.addWidget(self.splitter)


        self.retranslateUi(SleepStagesImporterSettingsView)
        self.pushButton_choose.clicked.connect(SleepStagesImporterSettingsView.choose_slot)
        self.pushButton_clear.clicked.connect(SleepStagesImporterSettingsView.clear_slot)

        QMetaObject.connectSlotsByName(SleepStagesImporterSettingsView)
    # setupUi

    def retranslateUi(self, SleepStagesImporterSettingsView):
        SleepStagesImporterSettingsView.setWindowTitle(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep Stages Files List</span></p></body></html>", None))
        self.pushButton_choose.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Add Files", None))
        self.pushButton_clear.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Clear", None))
        self.label_16.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep Stages File Name</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Define the filename to read stages based on the PSG filename.", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_prefix.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Optionally, define the prefix to insert before the PSG filename to identify the stages filename.", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"prefix", None))
        self.label_19.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"suffix", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_suffix.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Optionally, define the suffix to append to the PSG filename to identify the stages filename.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox_case_sensitive.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Uncheck if the sleep stage filename has a different case than the EDF filename.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_case_sensitive.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Filenames are case sensitive", None))
        self.textEdit.setHtml(QCoreApplication.translate("SleepStagesImporterSettingsView", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Example )</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:600;\">prefix		</span>hyp_</p>\n"
"<p style=\" margin-top:0px; margin-bott"
                        "om:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:600;\">PSG filename	</span>subject1.edf</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:600;\">suffix		</span> _annotation</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:600;\">stages filename	</span>hyp_subject1_annotation</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">Stage renaming</span></p></body></html>", None))
        self.lineEdit_ori_3.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"N3", None))
        self.label_10.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"6", None))
        self.label_37.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"NREM 3", None))
        self.lineEdit_ori_5.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"R", None))
        self.label_0.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"0", None))
        self.label_42.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Unscored", None))
        self.label_11.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"7", None))
        self.label_6.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"2", None))
        self.label_34.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Wake", None))
        self.lineEdit_ori_9.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Unscored", None))
        self.label_35.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"NREM 1", None))
        self.label_9.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Description", None))
        self.label_43.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Original Label\n"
"in file to read", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_ori_7.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Let the default label when not applicable.", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_ori_7.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Tech", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_ori_6.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Let the default label when not applicable.", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_ori_6.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Mov", None))
        self.label_40.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Movement", None))
        self.lineEdit_ori_1.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"N1", None))
        self.label_1.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"1", None))
        self.label_7.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"3", None))
        self.lineEdit_ori_0.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"W", None))
        self.lineEdit_ori_2.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"N2", None))
        self.label_46.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Snooz label", None))
        self.label_12.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"9", None))
        self.label_36.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"NREM 2", None))
        self.label_41.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Tech\n"
"Intervention", None))
        self.label_8.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"5", None))
        self.label_39.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"REM", None))
        self.label.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep Stages File Format</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.spinBox_colstage.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Define the column index to extract the stage labels. 1 means the first column.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Number of rows to skip.", None))
        self.comboBox_sep.setItemText(0, QCoreApplication.translate("SleepStagesImporterSettingsView", u"None", None))
        self.comboBox_sep.setItemText(1, QCoreApplication.translate("SleepStagesImporterSettingsView", u"\\t", None))
        self.comboBox_sep.setItemText(2, QCoreApplication.translate("SleepStagesImporterSettingsView", u";", None))
        self.comboBox_sep.setItemText(3, QCoreApplication.translate("SleepStagesImporterSettingsView", u",", None))
        self.comboBox_sep.setItemText(4, QCoreApplication.translate("SleepStagesImporterSettingsView", u"\\r", None))

#if QT_CONFIG(tooltip)
        self.comboBox_sep.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Delimiter character or pattern for the sleep stages file.\n"
"Set to None if unknown, and the engine will detect it.\n"
"Open the file in a text editor to see the separator.", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Column Index for stage", None))
        self.comboBox_stage_s.setItemText(0, QCoreApplication.translate("SleepStagesImporterSettingsView", u"1", None))
        self.comboBox_stage_s.setItemText(1, QCoreApplication.translate("SleepStagesImporterSettingsView", u"2", None))
        self.comboBox_stage_s.setItemText(2, QCoreApplication.translate("SleepStagesImporterSettingsView", u"3", None))
        self.comboBox_stage_s.setItemText(3, QCoreApplication.translate("SleepStagesImporterSettingsView", u"5", None))
        self.comboBox_stage_s.setItemText(4, QCoreApplication.translate("SleepStagesImporterSettingsView", u"6", None))
        self.comboBox_stage_s.setItemText(5, QCoreApplication.translate("SleepStagesImporterSettingsView", u"10", None))
        self.comboBox_stage_s.setItemText(6, QCoreApplication.translate("SleepStagesImporterSettingsView", u"15", None))
        self.comboBox_stage_s.setItemText(7, QCoreApplication.translate("SleepStagesImporterSettingsView", u"30", None))

#if QT_CONFIG(tooltip)
        self.comboBox_stage_s.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Define the duration (s) of the stage corresponding to one row in the sleep stages text file.", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_stage_s.setCurrentText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"1", None))
#if QT_CONFIG(tooltip)
        self.spinBox_n_rows.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Number of rows to skip before reading the sleep stages.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Item separator", None))
        self.comboBox_encoding.setItemText(0, QCoreApplication.translate("SleepStagesImporterSettingsView", u"utf-8", None))
        self.comboBox_encoding.setItemText(1, QCoreApplication.translate("SleepStagesImporterSettingsView", u"latin-1", None))
        self.comboBox_encoding.setItemText(2, QCoreApplication.translate("SleepStagesImporterSettingsView", u"utf-16", None))
        self.comboBox_encoding.setItemText(3, QCoreApplication.translate("SleepStagesImporterSettingsView", u"utf-32", None))
        self.comboBox_encoding.setItemText(4, QCoreApplication.translate("SleepStagesImporterSettingsView", u"iso-8859", None))
        self.comboBox_encoding.setItemText(5, QCoreApplication.translate("SleepStagesImporterSettingsView", u"ascii", None))

#if QT_CONFIG(tooltip)
        self.comboBox_encoding.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Define the sleep stage file encoding. You can open in Notepad++ to find out.", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Encoding", None))
        self.label_15.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Stage duration (s)", None))
        self.label_20.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"<html><head/><body><p>*Do not skip the row with column titles, if any.</p></body></html>", None))
    # retranslateUi

