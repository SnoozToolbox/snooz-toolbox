"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the SleepCyclesDelimiter plugin
"""

from qtpy import QtWidgets
from qtpy.QtGui import QPixmap, QImage
from qtpy.QtCore import QFile, QTimer, Slot
import base64

#from . import SleepCycleDelimiter_rs

from CEAMSModules.SleepCyclesDelimiter.Ui_SleepCyclesDelimiterSettingsView import Ui_SleepCyclesDelimiterSettingsView
from commons.BaseSettingsView import BaseSettingsView
import config


class SleepCyclesDelimiterSettingsView( BaseSettingsView,  Ui_SleepCyclesDelimiterSettingsView, QtWidgets.QWidget):
    """
        SleepCyclesDelimiterView display the settings for the SleepCyclesDelimiter plugin.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        # keep the qrc module alive
        #self._SleepCycleDelimiter_ref = SleepCycleDelimiter_rs  # prevent it from being garbage collected
        
        # Remove the old image paths - we'll use base64 now
        # self.image_min = "./UI_v5_minimal.png"
        # self.image_aesch = "./UI_v5_Aeschbach.png"
        # self.image_floyd = "./UI_v5_Feinberg_floyd.png"

        # flag to make sure we only load once
        self._image_loaded = False

        # Dictionary to convert into string
        self.parameters = {}

        # Hard coded parameters
        #   not from the UI anymore (not chosen by the user)
        self.dur_ends_REMP = 15
        self.minL_NREM_first = 0.5
        self.minL_NREM_mid = 0.5
        self.minL_NREM_val_last = 0
        self.sleep_stages = "N1,N2,N3,N4,R"
        
        # Subscribe to the proper topics to send/get data from the node
        self._parameters_topic = f'{self._parent_node.identifier}.parameters'
        self._pub_sub_manager.subscribe(self, self._parameters_topic)
        

    def showEvent(self, event):
        """
        Called automatically by Qt when the widget becomes visible.
        → We load the image here (once) so that it is done *after* the
          widget has been inserted in the UI and actually displayed.
        """
        super().showEvent(event)
        if not self._image_loaded:
            self._load_embedded_pixmap('aeschbach')  # Default image
            self._image_loaded = True

    def _load_embedded_pixmap(self, image_type):
        """Load the embedded base64 image data into the QLabel."""
        try:
            # Import the base64 data from the separate file
            from .sleep_cycle_image_data import MINIMAL_IMAGE_BASE64, AESCHBACH_IMAGE_BASE64, FEINBERG_FLOYD_IMAGE_BASE64
            
            # Select the appropriate image based on type
            if image_type == 'minimal':
                image_data = MINIMAL_IMAGE_BASE64
            elif image_type == 'aeschbach':
                image_data = AESCHBACH_IMAGE_BASE64
            elif image_type == 'feinberg_floyd':
                image_data = FEINBERG_FLOYD_IMAGE_BASE64
            else:
                print(f"Unknown image type: {image_type}")
                return
            
            # Decode base64 data to bytes
            image_bytes = base64.b64decode(image_data)
            
            # Create QPixmap from bytes
            pixmap = QPixmap()
            if pixmap.loadFromData(image_bytes):
                self.image.setPixmap(pixmap)
            else:
                print(f"Failed to load {image_type} image from base64 data")
        except ImportError:
            print("Could not import sleep cycle image data - make sure sleep_cycle_image_data.py exists")
        except Exception as e:
            print(f"Error loading embedded image: {e}")

    # Replace the old _load_pixmap method
    def _load_pixmap(self, image_path: str):
        """Legacy method - now routes to embedded images."""
        if "minimal" in image_path:
            self._load_embedded_pixmap('minimal')
        elif "Aeschbach" in image_path:
            self._load_embedded_pixmap('aeschbach')
        elif "floyd" in image_path or "Feinberg" in image_path:
            self._load_embedded_pixmap('feinberg_floyd')
        else:
            print(f"Unknown image path: {image_path}")

    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._parameters_topic, 'ping')
        

    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        # Update the parameters dictionary to send it to the publisher
        if self.radioButton_Min.isChecked():
            # Store the radio button checked
            self.parameters['defined_option'] = "Minimum Criteria"
        elif self.radioButton_Aesch.isChecked():
            # Store the radio button checked
            self.parameters['defined_option'] = "Aeschbach 1993"
        elif self.radioButton_Floyd.isChecked():
            # Store the radio button checked
            self.parameters['defined_option'] = "Feinberg 1979"
        elif self.radioButton_Mice.isChecked():
            # Store the radio button checked
            self.parameters['defined_option'] = "Mice"
        
        self.parameters['Include_SOREMP'] = str(int(self.checkBox_incl_SOREMP.isChecked()))
        self.parameters['Include_last_incompl'] = str(int(self.checkBox_incl_last.isChecked()))
        self.parameters['Include_all_incompl'] = str(int(self.checkBox_incl_all.isChecked()))
        # NREM Periods Init
        self.parameters['NREM_min_len_first'] = str(self.minL_NREM_first)
        self.parameters['NREM_min_len_mid_last'] = str(self.minL_NREM_mid)
        self.parameters['NREM_min_len_val_last'] = str(self.minL_NREM_val_last)
        self.parameters['dur_ends_REMP'] = str(self.dur_ends_REMP)
        # REM Periods Init
        self.parameters['REM_min_len_first'] = str(self.minL_REM_first_lineEdit.text())
        self.parameters['REM_min_len_mid'] = str(self.minL_REM_mid_lineEdit.text())
        self.parameters['REM_min_len_last'] = str(self.minL_REM_last_lineEdit.text())
        self.parameters['mv_end_REMP'] = str(int(self.mv_end_checkBox.isChecked()))
        # Sleep Onset
        self.parameters['sleep_stages'] = self.sleep_stages
        # Details
        self.parameters['details'] = self.textBrowser.toHtml()
        # Send the string of the parameter dict
        self._pub_sub_manager.publish(self, self._parameters_topic, \
            str(self.parameters))


    def on_topic_update(self, topic, message, sender):
        pass


    # Called by the publisher to display settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._parameters_topic:
            self.parameters = eval(message)
            # Fill all the lineEdit, checkbox and text linked
            # based on the dictionary
            if self.parameters['defined_option'] == "Minimum Criteria":
                self.radioButton_Min.setChecked(True)
                self._load_embedded_pixmap('minimal')
                
            elif self.parameters['defined_option'] == "Aeschbach 1993":
                self.radioButton_Aesch.setChecked(True)
                self._load_embedded_pixmap('aeschbach')              

            elif self.parameters['defined_option'] == "Feinberg 1979":
                self.radioButton_Floyd.setChecked(True)
                self._load_embedded_pixmap('feinberg_floyd')
            
            # NREM Periods Init
            self.minL_NREM_first = float(self.parameters['NREM_min_len_first'])
            self.minL_NREM_mid = float(self.parameters['NREM_min_len_mid_last'])
            self.minL_NREM_val_last = float(self.parameters['NREM_min_len_val_last'])

            # REM Periods Init
            self.minL_REM_first_lineEdit.setText(self.parameters['REM_min_len_first'])
            self.minL_REM_mid_lineEdit.setText(self.parameters['REM_min_len_mid'])
            self.minL_REM_last_lineEdit.setText(self.parameters['REM_min_len_last'])

            # Sleep Onset
            self.sleep_stages = self.parameters['sleep_stages']

            # Details
            self.textBrowser.setReadOnly(False)
            self.textBrowser.setHtml(self.parameters['details'])
            self.textBrowser.setReadOnly(True)

            # Set if the incomplete cycles should be kept
            self.checkBox_incl_SOREMP.setChecked(int(self.parameters['Include_SOREMP']))
            self.checkBox_incl_last.setChecked(int(self.parameters['Include_last_incompl']))
            self.checkBox_incl_all.setChecked(int(self.parameters['Include_all_incompl']))
            # Set if the user wants to extend the REM period
            self.mv_end_checkBox.setChecked(int(self.parameters['mv_end_REMP']))


    # Changes are made visible right away on the SettingsView but are updated into the dict
    # only when the user apply settings.
    def on_options_changed(self):
        if self.radioButton_Min.isChecked():
            self._load_embedded_pixmap('minimal')
            #QTimer.singleShot(300, lambda: self._load_pixmap(self.image_min))
            # Include incomplete cycle
            self.checkBox_incl_SOREMP.setChecked(1)
            self.checkBox_incl_last.setChecked(1)
            self.checkBox_incl_all.setChecked(1)
            # NREM Periods Init
            self.minL_NREM_first = 0.5
            self.minL_NREM_mid = 0.5
            self.minL_NREM_val_last = 0
            # REM Periods Not read only anymore
            self.minL_REM_first_lineEdit.setReadOnly(False)
            self.minL_REM_mid_lineEdit.setReadOnly(False)
            self.minL_REM_last_lineEdit.setReadOnly(False)
            # REM Periods Init
            self.minL_REM_first_lineEdit.setText('0.5')     
            self.minL_REM_mid_lineEdit.setText('0.5')
            self.minL_REM_last_lineEdit.setText('0.5')
            self.mv_end_checkBox.setChecked(False)
            # Sleep Stages
            self.sleep_stages = "N1, N2, N3, N4, R"
            # Details
            self.textBrowser.setReadOnly(False)
            self.textBrowser.setHtml("<p>Adjust options based on minimum criteria.<br />These criteria are generally used in the clinic.</p>")
            self.textBrowser.setReadOnly(True)

        elif self.radioButton_Aesch.isChecked():
            self._load_embedded_pixmap('aeschbach')
            # Include incomplete cycle
            self.checkBox_incl_SOREMP.setChecked(1)
            self.checkBox_incl_last.setChecked(1)
            self.checkBox_incl_all.setChecked(1)
            # NREM Periods Init
            self.minL_NREM_first = 15
            self.minL_NREM_mid = 15
            self.minL_NREM_val_last = 5
            # REM Periods Not read only anymore
            self.minL_REM_first_lineEdit.setReadOnly(False)
            self.minL_REM_mid_lineEdit.setReadOnly(False)
            self.minL_REM_last_lineEdit.setReadOnly(False)
            # REM Periods Init
            self.minL_REM_first_lineEdit.setText('0.5')     
            self.minL_REM_mid_lineEdit.setText('5')
            self.minL_REM_last_lineEdit.setText('0.5')
            self.mv_end_checkBox.setChecked(True)
            # Sleep Stages
            self.sleep_stages = "N2, N3, N4, R"
            # Details
            self.textBrowser.setReadOnly(False)
            self.textBrowser.setHtml('<div>Adjust options based on [1].</div><div>&nbsp;</div><div>NREM-REMS cycles were defined [...] by the succession of a NREMS episode of at least 15 min duration and a REMS episode of at least 5 min duration. No minimal duration of the REMS episode was required for the completion of the first and last cycle. NREMS episodes were defined as the time interval between the first occurrence of stage 2 and the first occurrence of REMS within a cycle. Consequently REMS episodes were defined as the time intervals between two consecutive NREMS episodes or the time interval between the last NREMS episode and the final awakening. Thus occasional stage 1 epochs between REMS and stage 2 were included in the REMS episode. The reasons for selecting this criterion were the similarity of the EEG in REMS and stage 1, the better delimitation of cycle onset by using stage 2 instead of stage 1, and the fact that the initiation of cycle 1 with stage 2 corresponds to a frequently used criterion of sleep onset.</div><div>&nbsp;</div>'\
                + '<div>[1] Aeschbach D, Borbely AA. All-night dynamics of the human sleep EEG. J Sleep Res. 1993 Jun; 2(2):70-81.<span style="color: #00ccff; "> <a style="color: #00ccff; " href="https://doi.org/10.1111/j.1365-2869.1993.tb00065.x" aria-label="Digital Object Identifier">https://doi.org/10.1111/j.1365-2869.1993.tb00065.x</a></div>')
            self.textBrowser.setReadOnly(True)

        elif self.radioButton_Floyd.isChecked():
            self._load_embedded_pixmap('feinberg_floyd')
            # Include incomplete cycle
            self.checkBox_incl_SOREMP.setChecked(1)
            self.checkBox_incl_last.setChecked(1)
            self.checkBox_incl_all.setChecked(1)
            # NREM Periods Init
            self.minL_NREM_first = 15
            self.minL_NREM_mid = 15
            self.minL_NREM_val_last = 5
            # REM Periods Not read only anymore
            self.minL_REM_first_lineEdit.setReadOnly(False)
            self.minL_REM_mid_lineEdit.setReadOnly(False)
            self.minL_REM_last_lineEdit.setReadOnly(False)
            # REM Periods Init
            self.minL_REM_first_lineEdit.setText('0.5')     
            self.minL_REM_mid_lineEdit.setText('5')
            self.minL_REM_last_lineEdit.setText('5')
            self.mv_end_checkBox.setChecked(True)
            # Sleep Stages
            self.sleep_stages = "N2, N3, N4, R"
            # Details
            self.textBrowser.setReadOnly(False)
            self.textBrowser.setHtml('<div>Adjust options based on [1].</div><div>&nbsp;</div><div>[] 15-min minimum for NREMPs in order to avoid considering brief stage 2 epochs in REM as separate NREMPs. Since we controlled time in bed, i.e., awoke subjects in the moming, additional criteria were needed. We defined as complete the last NREMP of the night if it was followed by 5 min or more of REM sleep before awakening, which sometimes was experimenter-induced rather than spontaneous. Similarly, the last REMP was considered complete if it was followed by 5 min or longer of NREM sleep. Thus, no sleep period was considered complete if it was interrupted by the final awakening of the night.</div>'\
                + '<div>&nbsp;</div><div>[1] Feinberg I, Floyd TC. Systematic trends across the night in human sleep cycles. Psychophysiology. 1979 May; 16(3):283-91.<span style="color: #00ccff; "> <a style="color: #00ccff; " href="https://doi.org/10.1111/j.1469-8986.1979.tb02991.x" aria-label="Digital Object Identifier">https://doi.org/10.1111/j.1469-8986.1979.tb02991.x</a></div><div>&nbsp;</div><div>&nbsp;</div>')
            self.textBrowser.setReadOnly(True)
     


    # Called when the user check/uncheck the checkbox to include all incomplete cycles.
    def include_incomplete_cycle_slot(self):
        if self.checkBox_incl_all.isChecked():
            self.checkBox_incl_last.setChecked(True)
            self.checkBox_incl_SOREMP.setChecked(True)
        

    # Called when user check/uncheck the include incomplete ending
    def include_last_incomplete_slot(self):
        # The user unchecked it
        if not self.checkBox_incl_last.isChecked():
            # Unchecked the include all (no more true)
            self.checkBox_incl_all.setChecked(False)


    # Called when user check/uncheck the include incomplete ending
    def include_SOREMP_slot(self):
        # The user unchecked it
        if not self.checkBox_incl_SOREMP.isChecked():
            # Unchecked the include all (no more true)
            self.checkBox_incl_all.setChecked(False)


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._parameters_topic)
        self.image_min = None
        self.image_aesch = None
        self.image_floyd = None