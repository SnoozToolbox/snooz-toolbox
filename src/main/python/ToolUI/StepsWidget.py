"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
import importlib
import os

from qtpy import QtCore, QtWidgets
from qtpy import QtGui
from qtpy.QtGui import QDesktopServices
from qtpy.QtCore import QUrl

from config import C
from commons.BaseSettingsView import BaseSettingsView
from ui.Ui_StepsWidget import Ui_StepsWidget
from ToolUI.ContextManager import ContextManager

class SidebarStep(QtWidgets.QWidget):

    def __init__(self, step_widget, step, process_description):
        super().__init__(None)
        self.setObjectName("SidebarStep")
        self.setAccessibleName("SidebarStep")
        layout = QtWidgets.QVBoxLayout()
        self._step_content_index = step_widget._add_step_content(step, process_description)
        # Add configs if any
        if 'configs' in step:
            
            # Add the configs label
            settings_label = QtWidgets.QLabel(f"{step['configs']['label']}")
            layout.addWidget(settings_label)

            # Add a line
            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.HLine)
            line.setObjectName("line")
            layout.addWidget(line)

            # Add all config links
            for idx, config in enumerate(step['configs']['list']):
                label = QtWidgets.QLabel(f"   {config['name']}")
                label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                label.setStyleSheet(f"color: {C.clickable_link_color};")

                step_content_index = step_widget._add_step_content(config, process_description, self._step_content_index, step["name"])
                label.mousePressEvent = lambda e, step_content_index=step_content_index: step_widget._on_open_config(step_content_index)
                layout.addWidget(label)

            # Add a line
            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.HLine)
            line.setObjectName("line")
            layout.addWidget(line)

        # Add a description
        label = QtWidgets.QLabel(f"{step['description']}")
        label.setWordWrap(True)
        label.setAlignment(QtCore.Qt.AlignTop)
        layout.addWidget(label)
        layout.addStretch()

        self.setLayout(layout)

    @property
    def step_content_index(self):
        return self._step_content_index

class StepsWidget(QtWidgets.QWidget, Ui_StepsWidget):
    def __init__(self, managers, description, activation_params, tool_filepath, *args, **kwargs):
        super(StepsWidget, self).__init__(*args, **kwargs)
        self._managers = managers
        self._activation_params = activation_params
        self.setObjectName("StepsWidget")
        self.setAccessibleName("StepsWidget")
        self._pub_sub_manager = self._managers.pub_sub_manager
        self._package_manager = self._managers.package_manager
        self._process_description = description

        self._context_manager = ContextManager(self._pub_sub_manager)
        self._tool_filepath = tool_filepath

        self.setupUi(self)
        self.splitter.setStretchFactor(0, 0)
        self.splitter.setStretchFactor(1, 1)
       
        # Load steps
        self.steps_toolbox.removeItem(0)
        self.steps_tabwidget.removeTab(0)

        next_label_index = 1
        
        # Verofy if there is 'tool_params' as a key in the description file
        if "tool_params" in self._process_description:
            for idx, step in enumerate(self._process_description['tool_params']['steps']):
                sidebar_step = SidebarStep(self, step, self._process_description)
                
                if 'show_index' not in step or \
                    'show_index' in step and step['show_index']:
                    step_name = f"{next_label_index} - {step['name']}"
                    next_label_index = next_label_index + 1
                else:
                    step_name = f"{step['name']}"

                self.steps_toolbox.addItem(sidebar_step, step_name)

            # Hide all tab's tab
            for i in range(self.steps_tabwidget.count()):
                self.steps_tabwidget.setTabVisible(i, False)

            # Show the feedback button if necessary
            if "feedback" in self._process_description or True:
                self.feedback_pushButton.setVisible(True)
            else:
                self.feedback_pushButton.setVisible(False)

            # Once everything is in place, load_settings for all pages
            self._load_all_settings()
            self.steps_tabwidget.setCurrentIndex(0)

            # important to do it after everything to avoid triggering it when
            # things are being setup.
            self.steps_toolbox.currentChanged.connect(self.on_step_changed) 

    # Slots
    @QtCore.Slot()
    def change_step(self, step_index:int):
        self.steps_tabwidget.setCurrentIndex(step_index)

    # Public methods
    def unsubscribe_all_topics(self):
        self._context_manager.unsubscribe_all_topics()

    def on_save_logs(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Log File')
        if filename == '':
            return
        
        with open(filename,'w') as log_file:
            log_file.close()

    def save_clicked(self):
        #success = self._validate_all_settings()
        #if not success:
        #    return
        self._apply_all_settings()
        filepath, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Save workspace', filter='*.json')
        if filepath == '':
            return
        if not filepath.endswith(".json"):
            filepath = filepath + ".json"
            
        self._managers.process_manager.save_scene_to_file(filepath)
        message = f"Workspace saved"
        self._managers.pub_sub_manager.publish(self, "show_info_message", message)

    def feedback_pressed(self,event):
        toolname = self._process_description['item_name']
        url_text = f"https://form.jotform.com/240234589570258?toolname={toolname}"
        
        url = QUrl(url_text, QUrl.TolerantMode)
        QDesktopServices.openUrl(url)

    def _add_step_content(self, step_content, process_description, back_step_index=None, back_step_name=None):
        top_widget = QtWidgets.QWidget()
        top_layout = QtWidgets.QVBoxLayout()
        top_widget.setLayout(top_layout)

        if back_step_index is not None:
            h_layout = QtWidgets.QHBoxLayout()
            back_button = QtWidgets.QPushButton("< " + back_step_name)
            back_button.clicked.connect(lambda checked=None,index=back_step_index:self.change_step(index))
            h_layout.addWidget(back_button)
            h_layout.addStretch(1)
            top_layout.addLayout(h_layout)

        if 'module_id' in step_content:
            module_id = step_content['module_id']
            module = self._managers.process_manager.get_node_by_id(module_id)
            if module is None:
                print(f'ERROR module_id isn\'t found in the process:{module_id}')
                return None
            else:
                page = module.create_settings_view(self._activation_params)
                top_layout.addWidget(page)

        elif 'custom_step_name' in step_content:
            custom_step_name = step_content['custom_step_name']

            package_name = process_description["tool_params"]["package_name"]
            tool_name = process_description["item_name"]

            asset_directory = None
            if "asset_directory" in process_description["tool_params"] and \
                self._tool_filepath is not None:
                asset_directory = os.path.join(self._tool_filepath, process_description["tool_params"]["asset_directory"])

            module_name = f'{package_name}.{tool_name}.{custom_step_name}.{custom_step_name}'
            module = importlib.import_module(module_name)
            Page = getattr(module, f'{custom_step_name}')
            page = Page(parent_node=None, pub_sub_manager=self._pub_sub_manager,
                context_manager=self._context_manager,
                process_manager=self._managers.process_manager, asset_manager=asset_directory, custom_params=self._activation_params)
                #node_manager = self._node_manager, asset_manager=self._asset_manager)
            top_layout.addWidget(page)

        return self.steps_tabwidget.addTab(top_widget, QtGui.QIcon(),"")

    def run_clicked(self):
        success = self._validate_all_settings()
        if success:
            self._apply_all_settings()
            self._managers.process_manager.run_current_process()
        else:
            self._managers.pub_sub_manager.publish(self, "show_error_message", "Please fix all errors before running")  
    
    def on_next(self):
        self.steps_toolbox.setCurrentIndex(
            min(self.steps_toolbox.currentIndex() + 1, 
                self.steps_toolbox.count() - 1))
    
    def on_previous(self):
        self.steps_toolbox.setCurrentIndex(
            max(0, self.steps_toolbox.currentIndex() - 1))
        
    def _load_all_settings(self):
        for i in range(self.steps_tabwidget.count()):
            page = self.steps_tabwidget.widget(i)
            base_settings_views = page.findChildren(BaseSettingsView)
            for base_setting_view in base_settings_views:
                base_setting_view.load_settings()

    def _apply_all_settings(self):
        for i in range(self.steps_tabwidget.count()):
            page = self.steps_tabwidget.widget(i)
            base_settings_views = page.findChildren(BaseSettingsView)
            for base_setting_view in base_settings_views:
                base_setting_view.on_apply_settings()

    def _validate_all_settings(self):
        for i in range(self.steps_tabwidget.count()):
            page = self.steps_tabwidget.widget(i)
            base_settings_views = page.findChildren(BaseSettingsView)
            for base_setting_view in base_settings_views:
                success = base_setting_view.on_validate_settings()
                if not success:
                    return False
        return True

    def on_step_changed(self):
        current_widget = self.steps_toolbox.currentWidget()
        if current_widget is not None:
            step_content_index = self.steps_toolbox.currentWidget().step_content_index
            if step_content_index is not None:
                self.steps_tabwidget.setCurrentIndex(step_content_index)
                self.next_pushbutton.setVisible(not self._is_last_step())
            else:
                print("ERROR: step_content_index is None. Usually this means the module_id was not found in the step definition")
            
    def _is_last_step(self):
        """
        Return if the current step is the last step.
        """
        return self.steps_toolbox.currentIndex() == self.steps_toolbox.count() - 1
    
    def _on_open_config(self, step_content_index):
        self.steps_tabwidget.setCurrentIndex(step_content_index)
