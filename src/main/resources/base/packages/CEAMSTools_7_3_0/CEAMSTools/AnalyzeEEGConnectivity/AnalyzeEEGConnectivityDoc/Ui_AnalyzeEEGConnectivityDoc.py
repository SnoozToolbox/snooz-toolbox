# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AnalyzeEEGConnectivityDoc.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_AnalyzeEEGConnectivityDoc(object):
    def setupUi(self, AnalyzeEEGConnectivityDoc):
        if not AnalyzeEEGConnectivityDoc.objectName():
            AnalyzeEEGConnectivityDoc.setObjectName(u"AnalyzeEEGConnectivityDoc")
        AnalyzeEEGConnectivityDoc.resize(858, 644)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AnalyzeEEGConnectivityDoc.sizePolicy().hasHeightForWidth())
        AnalyzeEEGConnectivityDoc.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(AnalyzeEEGConnectivityDoc)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(AnalyzeEEGConnectivityDoc)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setMouseTracking(True)

        self.verticalLayout.addWidget(self.label)

        self.textEdit = QTextEdit(AnalyzeEEGConnectivityDoc)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setItalic(True)
        self.textEdit.setFont(font1)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)


        self.retranslateUi(AnalyzeEEGConnectivityDoc)

        QMetaObject.connectSlotsByName(AnalyzeEEGConnectivityDoc)
    # setupUi

    def retranslateUi(self, AnalyzeEEGConnectivityDoc):
        AnalyzeEEGConnectivityDoc.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"<html><head/><body><p><span style=\" font-weight:700;\">Analyze EEG Connectivity</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; font-style:normal;\">Weighted phase lag index (wPLI)</span><span style=\" font-style:normal;\"> quantifies the strength of non-zero phase-lagged connectivity of EEG channels, emphasizing stronger, more consistent interactions while minimizing the influence of noise and common sources [1]. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px;"
                        " margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; font-style:normal;\">Directed phase lag index (dPLI)</span><span style=\" font-style:normal;\"> is a measure of directional functional connectivity based on the consistency of phase lead-lag relationship between EEG channels, insensitive to volume conduction [2].</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:normal;\">This tool computes wPLI and dPLI connectivity, using the algorithms described by Vinck et al. (2011) [1] for wPLI and Stam et al. (2012) [2] for dPLI. The statistical testing procedure to remove chance-related artifacts is based on Duclos et al. (2023) [3].</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:normal;\">Connectivity analysis cannot be performed with fewer than 2 brain"
                        " EEG channels.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:normal; text-decoration: underline;\">1 - Input Files:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:normal;\">Add your PSG files (.edf, .sts or .eeg). <br />The .tsv file is also needed for the edf format.<br />The .sig file is also needed for the Stellate format.<br />The whole NATUS subject folder is also needed for the NATUS format. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:normal;\"><br /></span><span style=\" font-style:normal; text-decoration: underline;\">2 - Events Exclusion:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent"
                        ":0; text-indent:0px;\"><span style=\" font-style:normal;\">Select events to discard from the analysis (i.e. artefacts previously detected and saved in the accessory file).<br /></span><span style=\" font-weight:700; font-style:normal;\">Important note:<br /></span><span style=\" font-style:normal;\">Connectivity analysis can only be performed on brain EEG channels. Any channels marked with the annotation group &quot;art_inspector&quot; and the name &quot;art_channel&quot; or &quot;non_brain&quot; will now be automatically excluded from the analysis.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:normal;\"><br /></span><span style=\" font-style:normal; text-decoration: underline;\">3 - Filter Settings:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:normal; text-decoration: underlin"
                        "e;\">Frequency Band Selection:<br /></span><span style=\" font-style:normal;\">Define the appropriate frequency band to align with your research objectives (e.g., Full frequency band, Delta,  Theta, Alpha, Beta)</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:normal; text-decoration: underline;\">Recording Scope Selection:<br /></span><span style=\" font-style:normal;\">Select Sleep Stages to analyze specific stages, Unscored to analyze the full recording or a chosen time segment, or Specific Annotations to base the analysis on event markers.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:normal;\"><br /></span><span style=\" font-style:normal; text-decoration: underline;\">4 - Annotation Selection:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; ma"
                        "rgin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:normal;\">If the Analyse EEG Connectivity is performed on specific annotations, select them.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:normal; text-decoration: underline;\"><br />5 - Connectivity Settings:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:normal;\">Define the connectivity type (dPLI or wPLI)<br />Specify the Epoch length and Epoch overlap (in seconds) and number of surrogates and p-value threshold for statistical testing.<br /></span><span style=\" font-weight:700; font-style:normal;\">note:</span><span style=\" font-style:normal;\"><br />Statistical testing ensures connections are not due to chance and provides more reliable connectivity estimates.</span></p>\n"
"<p style=\" margin"
                        "-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:normal; text-decoration: underline;\"><br />6 - Output Files :</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:normal;\">All files are saved in the selected Output folder (or next to the input recording if the &quot; save in the same folder is checked). Filenames use the subject name and metric (wPLI or dPLI).</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:normal;\">- Connectivity matrix (TSV) --- &lt;Filename&gt;_{wpli|dpli}_convalue.tsv<br />- Connectivity heatmap (PNG) --- &lt;Filename&gt;_{wpli|dpli}_conheatmap.png<br />- Head connectivity plot (PNG) \u2014 &lt;Filename&gt;_{wpli|dpli}_contopomap.png (saved only if a best montage with \u2265 4 EEG c"
                        "hannels is found)<br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:normal;\">References:</span><span style=\" font-family:'Segoe UI'; font-style:normal;\"><br />[1] Stam, C. J., &amp; van Straaten, E. C. W. (2012). </span><span style=\" font-family:'Segoe UI';\">Go with the flow: Use of a directed phase lag index (dPLI) to characterize patterns of phase relations in a large-scale model of brain dynamics</span><span style=\" font-family:'Segoe UI'; font-style:normal;\">. NeuroImage, 62(3), 1415\u20131428. https://doi.org/10.1016/j.neuroimage.2012.05.050<br />[2] Vinck, M., Oostenveld, R., van Wingerden, M., Battaglia, F., &amp; Pennartz, C. M. (2011). </span><span style=\" font-family:'Segoe UI';\">An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias</span><span style=\" font-family:'Segoe UI'; font-style:nor"
                        "mal;\">. NeuroImage, 55(4), 1548\u20131565. https://doi.org/10.1016/j.neuroimage.2011.01.055<br />[3] Duclos, C., Maschke, C., Mahdid, Y., Nadin, D., Rokos, A., Arbour, C., Badawy, M., L\u00e9tourneau, J., Owen, A. M., Plourde, G., &amp; Blain-Moraes, S. (2023). Brain responses to propofol in advance of recovery from coma and disorders of consciousness: A preliminary study. *American Journal of Respiratory and Critical Care Medicine, 207*(5), 602\u2013613. https://doi.org/10.1164/rccm.202105-1223OC</span></p></body></html>", None))
    # retranslateUi

