from qtpy.QtWidgets import QDialog, QComboBox, QVBoxLayout, QLabel, QDialogButtonBox
from qtpy.QtCore import Qt

from Endpoints.EndpointHandler import EndpointHandler

class FileMenuEndpointHandler(EndpointHandler):
    # DO NOT CHANGE THIS.
    # The name of the endpoint is used in every modules, tools and apps description file.
    # When you change the name, it breaks all backward compatibility with those.
    ENDPOINT_NAME = "file_menu_endpoint"

    def __init__(self, managers):
        super(FileMenuEndpointHandler, self).__init__()
        self._managers = managers
        self._hooks = {}

    def register_hook(self, hook):
        assert "parameters" in hook
        hook_parameters = hook["parameters"]
        label = hook_parameters["app_label"]

        if label not in self._hooks:
            self._hooks[label] = hook

    def unregister_hook(self, hook):
        assert "parameters" in hook
        hook_parameters = hook["parameters"]
        label = hook_parameters["app_label"]

        if label in self._hooks:
            del self._hooks[label]

    def open_file(self):
        if len(self._hooks) == 0:
            message = "No app registered to open a file"
            self._managers.pub_sub_manager.publish(self, "show_info_message", message)
            return
        
        # Let's create a dialog that contains a combo box with the app list
        dialog = QDialog()
        dialog.setWindowTitle("Select an app")
        dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        combo_box = QComboBox()
        for label in self._hooks:
            combo_box.addItem(label)
        
        dialog.layout = QVBoxLayout()
        # Add a label to ask the user which app to use
        label = QLabel("Select the app you want to open the file with:")
        dialog.layout.addWidget(label)
        dialog.layout.addWidget(combo_box)
        # Add a ok and a cancel button
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, dialog)
        dialog.layout.addWidget(button_box)
        # Handle buttonbox events
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)

        dialog.setLayout(dialog.layout)
        
        if dialog.exec_() == QDialog.Accepted:
            selected_app = combo_box.currentText()
            hook = self._hooks[selected_app]
        else:
            return
        
        package_name = hook["package_name"]
        package_version = hook["package_version"]
        item_name = hook["item_name"]
        package_item = self._managers.package_manager.get_package_item(package_name, package_version, item_name)
        params = {"startup_action": "open_file"}
        package_item.activate(params)
