# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EDFAnnotationsReaderResultsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_EDFAnnotationsReaderResultsView(object):
    def setupUi(self, EDFAnnotationsReaderResultsView):
        if not EDFAnnotationsReaderResultsView.objectName():
            EDFAnnotationsReaderResultsView.setObjectName(u"EDFAnnotationsReaderResultsView")
        EDFAnnotationsReaderResultsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        EDFAnnotationsReaderResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(EDFAnnotationsReaderResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(EDFAnnotationsReaderResultsView)

        QMetaObject.connectSlotsByName(EDFAnnotationsReaderResultsView)
    # setupUi

    def retranslateUi(self, EDFAnnotationsReaderResultsView):
        EDFAnnotationsReaderResultsView.setWindowTitle(QCoreApplication.translate("EDFAnnotationsReaderResultsView", u"Form", None))
    # retranslateUi

