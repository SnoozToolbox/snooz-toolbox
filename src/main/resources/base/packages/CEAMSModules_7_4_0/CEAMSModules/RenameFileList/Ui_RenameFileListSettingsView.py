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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_RenameFileListSettingsView(object):
    def setupUi(self, RenameFileListSettingsView):
        if not RenameFileListSettingsView.objectName():
            RenameFileListSettingsView.setObjectName(u"RenameFileListSettingsView")
        RenameFileListSettingsView.resize(943, 741)
        RenameFileListSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout_2 = QHBoxLayout(RenameFileListSettingsView)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableWidget_files = QTableWidget(RenameFileListSettingsView)
        self.tableWidget_files.setObjectName(u"tableWidget_files")

        self.verticalLayout_4.addWidget(self.tableWidget_files)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_choose = QPushButton(RenameFileListSettingsView)
        self.pushButton_choose.setObjectName(u"pushButton_choose")
        self.pushButton_choose.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.pushButton_choose)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.pushButton_clear = QPushButton(RenameFileListSettingsView)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.pushButton_clear)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ext_selection_horizontalLayout = QHBoxLayout()
        self.ext_selection_horizontalLayout.setObjectName(u"ext_selection_horizontalLayout")
        self.ext_selection_label = QLabel(RenameFileListSettingsView)
        self.ext_selection_label.setObjectName(u"ext_selection_label")
        self.ext_selection_label.setMinimumSize(QSize(450, 0))

        self.ext_selection_horizontalLayout.addWidget(self.ext_selection_label)

        self.ext_selection_lineedit = QLineEdit(RenameFileListSettingsView)
        self.ext_selection_lineedit.setObjectName(u"ext_selection_lineedit")
        self.ext_selection_lineedit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.ext_selection_horizontalLayout.addWidget(self.ext_selection_lineedit)


        self.verticalLayout.addLayout(self.ext_selection_horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.n_char_to_keep_horizontalLayout = QHBoxLayout()
        self.n_char_to_keep_horizontalLayout.setObjectName(u"n_char_to_keep_horizontalLayout")
        self.n_char_to_keep_label = QLabel(RenameFileListSettingsView)
        self.n_char_to_keep_label.setObjectName(u"n_char_to_keep_label")
        self.n_char_to_keep_label.setMinimumSize(QSize(450, 0))

        self.n_char_to_keep_horizontalLayout.addWidget(self.n_char_to_keep_label)

        self.checkBox_keep_all_char = QCheckBox(RenameFileListSettingsView)
        self.checkBox_keep_all_char.setObjectName(u"checkBox_keep_all_char")
        self.checkBox_keep_all_char.setChecked(True)

        self.n_char_to_keep_horizontalLayout.addWidget(self.checkBox_keep_all_char)

        self.spinBox_n_char_to_keep = QSpinBox(RenameFileListSettingsView)
        self.spinBox_n_char_to_keep.setObjectName(u"spinBox_n_char_to_keep")
        self.spinBox_n_char_to_keep.setEnabled(False)
        self.spinBox_n_char_to_keep.setMinimum(-1)
        self.spinBox_n_char_to_keep.setValue(-1)

        self.n_char_to_keep_horizontalLayout.addWidget(self.spinBox_n_char_to_keep)


        self.verticalLayout_2.addLayout(self.n_char_to_keep_horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pattern_to_rem_horizontalLayout = QHBoxLayout()
        self.pattern_to_rem_horizontalLayout.setObjectName(u"pattern_to_rem_horizontalLayout")
        self.pattern_to_rem_label = QLabel(RenameFileListSettingsView)
        self.pattern_to_rem_label.setObjectName(u"pattern_to_rem_label")
        self.pattern_to_rem_label.setMinimumSize(QSize(450, 0))

        self.pattern_to_rem_horizontalLayout.addWidget(self.pattern_to_rem_label)

        self.pattern_to_rem_lineedit = QLineEdit(RenameFileListSettingsView)
        self.pattern_to_rem_lineedit.setObjectName(u"pattern_to_rem_lineedit")

        self.pattern_to_rem_horizontalLayout.addWidget(self.pattern_to_rem_lineedit)


        self.verticalLayout_3.addLayout(self.pattern_to_rem_horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.prefix_horizontalLayout = QHBoxLayout()
        self.prefix_horizontalLayout.setObjectName(u"prefix_horizontalLayout")
        self.prefix_label = QLabel(RenameFileListSettingsView)
        self.prefix_label.setObjectName(u"prefix_label")
        self.prefix_label.setMinimumSize(QSize(450, 0))

        self.prefix_horizontalLayout.addWidget(self.prefix_label)

        self.prefix_lineedit = QLineEdit(RenameFileListSettingsView)
        self.prefix_lineedit.setObjectName(u"prefix_lineedit")

        self.prefix_horizontalLayout.addWidget(self.prefix_lineedit)


        self.verticalLayout_4.addLayout(self.prefix_horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.suffix_horizontalLayout = QHBoxLayout()
        self.suffix_horizontalLayout.setObjectName(u"suffix_horizontalLayout")
        self.suffix_label = QLabel(RenameFileListSettingsView)
        self.suffix_label.setObjectName(u"suffix_label")
        self.suffix_label.setMinimumSize(QSize(450, 0))

        self.suffix_horizontalLayout.addWidget(self.suffix_label)

        self.suffix_lineedit = QLineEdit(RenameFileListSettingsView)
        self.suffix_lineedit.setObjectName(u"suffix_lineedit")

        self.suffix_horizontalLayout.addWidget(self.suffix_lineedit)


        self.verticalLayout_4.addLayout(self.suffix_horizontalLayout)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_7)

        self.checkBox_keep_original = QCheckBox(RenameFileListSettingsView)
        self.checkBox_keep_original.setObjectName(u"checkBox_keep_original")
        self.checkBox_keep_original.setChecked(True)

        self.verticalLayout_4.addWidget(self.checkBox_keep_original)

        self.label = QLabel(RenameFileListSettingsView)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.retranslateUi(RenameFileListSettingsView)
        self.checkBox_keep_all_char.clicked.connect(RenameFileListSettingsView.keep_all_char_slot)
        self.pushButton_choose.clicked.connect(RenameFileListSettingsView.choose_slot)
        self.pushButton_clear.clicked.connect(RenameFileListSettingsView.clear_slot)

        QMetaObject.connectSlotsByName(RenameFileListSettingsView)
    # setupUi

    def retranslateUi(self, RenameFileListSettingsView):
        RenameFileListSettingsView.setWindowTitle(QCoreApplication.translate("RenameFileListSettingsView", u"Form", None))
        self.pushButton_choose.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Choose", None))
        self.pushButton_clear.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Clear", None))
        self.ext_selection_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"File extension of the file to rename (to filter the file list)", None))
#if QT_CONFIG(tooltip)
        self.ext_selection_lineedit.setToolTip(QCoreApplication.translate("RenameFileListSettingsView", u"e.g. tsv, txt, csv, xml, edf", None))
#endif // QT_CONFIG(tooltip)
        self.ext_selection_lineedit.setPlaceholderText(QCoreApplication.translate("RenameFileListSettingsView", u"tsv", None))
        self.n_char_to_keep_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Number of characters to keep from the original name", None))
#if QT_CONFIG(tooltip)
        self.checkBox_keep_all_char.setToolTip(QCoreApplication.translate("RenameFileListSettingsView", u"Check to keep all the characters.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_keep_all_char.setText(QCoreApplication.translate("RenameFileListSettingsView", u"all", None))
#if QT_CONFIG(tooltip)
        self.spinBox_n_char_to_keep.setToolTip(QCoreApplication.translate("RenameFileListSettingsView", u"e.g. keeping 9 characters renames \"subject01 filtered.tsv\" to \"subject01.tsv\". Use -1 to keep all characters.", None))
#endif // QT_CONFIG(tooltip)
        self.pattern_to_rem_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Pattern to remove from the original name", None))
#if QT_CONFIG(tooltip)
        self.pattern_to_rem_lineedit.setToolTip(QCoreApplication.translate("RenameFileListSettingsView", u"e.g. remove \"_annotations\" to rename \"subject01_annotations.txt\" as \"subject01.txt\"", None))
#endif // QT_CONFIG(tooltip)
        self.prefix_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Prefix to add to the original filename", None))
#if QT_CONFIG(tooltip)
        self.prefix_lineedit.setToolTip(QCoreApplication.translate("RenameFileListSettingsView", u"e.g. \"visit1_\" to rename \"subject01.tsv\" to \"visit1_subject01.tsv\"", None))
#endif // QT_CONFIG(tooltip)
        self.suffix_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Suffix to add to the original filename", None))
#if QT_CONFIG(tooltip)
        self.suffix_lineedit.setToolTip(QCoreApplication.translate("RenameFileListSettingsView", u"e.g. \"_visit1\" to rename \"subject01.tsv\" to \"subject01_visit1.tsv\"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox_keep_original.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.checkBox_keep_original.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Keep the original file.\n"
"Check to save a copy of the file before renaming it.", None))
        self.label.setText("")
    # retranslateUi

