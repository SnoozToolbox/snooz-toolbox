import sys

from qtpy.QtCore import Property, QRectF, Qt
from qtpy.QtGui import QColor, QPainter, QPalette
from qtpy.QtWidgets import QMenuBar, QMenu, QAction

from commons.theme_helpers import round_menu_corners
from Endpoints.EndpointHandler import EndpointHandler
from Managers.PackageManager import PackageManager

# Right padding of the menu items (QMenu::item rule of the style sheet): the style
# draws the version of an item just before it.
_ITEM_RIGHT_PADDING = 30

class OrderedMenu(QMenu):
    def __init__(self, title, parent=None):
        super(OrderedMenu, self).__init__(title, parent)
        self.setObjectName(title)
        round_menu_corners(self)
        self._version_background = QColor("#e9edf3")
        self._version_color = QColor("#1b2a41")

        self._full_title = title
        # Remove ordered prefix
        title = self._remove_ordered_prefix(title)
        self.menuAction().setText(title)

    @property
    def full_title(self):
        return self._full_title

    def _get_version_background(self):
        return self._version_background

    def _set_version_background(self, color):
        self._version_background = QColor(color)

    def _get_version_color(self):
        return self._version_color

    def _set_version_color(self, color):
        self._version_color = QColor(color)

    # Colors of the version boxes, set by the style sheet (qproperty-versionBackground...)
    versionBackground = Property(QColor, _get_version_background, _set_version_background)
    versionColor = Property(QColor, _get_version_color, _set_version_color)

    def paintEvent(self, event):
        super(OrderedMenu, self).paintEvent(event)
        self._paint_versions(event)

    def _paint_versions(self, event):
        """ Draw the version of each item (its text after the tab) in a box.

        The boxes have the same width and cover the versions drawn by the style. The
        box of the highlighted item is white, to stand out from the highlight.
        """
        versions = {action: action.text().split("\t", 1)[1]
                    for action in self.actions() if "\t" in action.text()}
        if not versions:
            return
        metrics = self.fontMetrics()
        column_width = max(metrics.horizontalAdvance(version) for version in versions.values())
        highlighted_background = self.palette().color(QPalette.Base)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setFont(self.font())
        for action, version in versions.items():
            item = self.actionGeometry(action)
            if not item.intersects(event.rect()):
                continue
            # The version is drawn by the style at the left of a column ending at "right":
            # the box starts just before it and goes into the right padding of the item.
            right = item.right() - _ITEM_RIGHT_PADDING
            box = QRectF(right - column_width - 4, item.center().y() - metrics.height() / 2 - 2,
                         column_width + 24, metrics.height() + 4)
            painter.setPen(Qt.NoPen)
            painter.setBrush(highlighted_background if action == self.activeAction()
                             else self._version_background)
            painter.drawRoundedRect(box, box.height() / 2, box.height() / 2)
            painter.setPen(self._version_color)
            painter.drawText(box, Qt.AlignCenter, version)
        painter.end()

    # Modify title function inherited from QMenu
    def _remove_ordered_prefix(self, title):
        # Find if there's a dash in the name
        if '-' in title:
            # get the string that comes before the dash
            start_text = title.split('-')[0]

            # check if the string is a number by using isdigit
            if start_text.isdigit():
                # substring based on the position of the dash cahracter
                start_text = title[title.index('-')+1:]
                return start_text
               
        return title

    

class MenuEndpointHandler(EndpointHandler):
    # DO NOT CHANGE THIS.
    # The name of the endpoint is used in every modules, tools and apps description file.
    # When you change the name, it breaks all backward compatibility with those.
    ENDPOINT_NAME = "menu_endpoint"

    def __init__(self, managers):
        super(MenuEndpointHandler, self).__init__()
        self._managers = managers
        self._package_manager = managers.package_manager
        self._menu_bar = None
        self._before_menu = None
        self._actions = {}
        # Hook of each action, by label: the item it opens (see menu_items)
        self._hooks = {}
        self._categories = {}
        self._ordered_categories_menu = []

    def set_menu_bar(self, menu_bar):
        self._menu_bar = menu_bar

    def set_before_menu(self, before_menu):
        self._before_menu = before_menu

    def register_hook(self, hook):
        assert "parameters" in hook

        hook_parameters = hook["parameters"]
        label = hook_parameters["menu_label"]
        full_label = self._action_text(label, hook["item_version"])
        category = hook_parameters["menu_category"]

        if category not in self._categories:
            menu_category = OrderedMenu(category, self._menu_bar)
            self._categories[category] = menu_category
            # insert the category into _ordered_categories_menu so it appears 
            # before other categories alphabetically based on the title.
            insertion_index = 0
            for menu in self._ordered_categories_menu:
                if menu.full_title > category:
                    break
                insertion_index += 1
            
            self._ordered_categories_menu.insert(insertion_index, menu_category)
            
            # Remove all first level menu from menu_bar
            for menu in self._menu_bar.children():
                if isinstance(menu, OrderedMenu):
                    self._menu_bar.removeAction(menu.menuAction())

            # Add them back in order
            for menu in self._ordered_categories_menu:
                self._menu_bar.insertMenu(self._before_menu.menuAction(), menu)
        else:
            menu_category = self._categories[category]

        action = QAction(full_label, self, triggered=(lambda checked, hook=hook: self.on_action(hook)))
        menu_category.addAction(action)
        self._actions[label] = action 
        self._hooks[label] = hook
        self._managers.pub_sub_manager.publish(self, "menus_changed", None)

    def unregister_hook(self, hook):
        assert "parameters" in hook
        hook_parameters = hook["parameters"]
        label = hook_parameters["menu_label"]
        full_label = self._action_text(label, hook["item_version"])
        
        if hook_parameters["menu_category"] not in self._categories:
            return
        menu_category = self._categories[hook_parameters["menu_category"]]

        if label not in self._actions:
            return
        action = self._actions[label]

        if action.text() == full_label:
            menu_category.removeAction(action)
            del self._actions[label]
            self._hooks.pop(label, None)

            if len(menu_category.actions()) == 0:
                self._menu_bar.removeAction(menu_category.menuAction())
                del self._categories[hook_parameters["menu_category"]]
            self._managers.pub_sub_manager.publish(self, "menus_changed", None)
    
    
    def clear(self):
        # Remove all first level menu from menu_bar
        for menu in self._menu_bar.children():
            if isinstance(menu, OrderedMenu):
                self._menu_bar.removeAction(menu.menuAction())

        self._actions = {}
        self._hooks = {}
        self._categories = {}
        self._ordered_categories_menu = []
        self._managers.pub_sub_manager.publish(self, "menus_changed", None)

    def menu_items(self):
        """ The items of the menus (tools, apps), in the order of the menus.

        Returns
        -------
        list of dict
            label, category (title of its menu), version, description (the
            item_description of the item, "" if it has none) and action (the QAction
            that opens the item).
        """
        labels = {action: label for label, action in self._actions.items()}
        items = []
        for menu in self._ordered_categories_menu:
            for action in menu.actions():
                label = labels.get(action)
                hook = self._hooks.get(label)
                if hook is None:
                    continue
                description = ""
                try:
                    package_item = self._package_manager.get_package_item(
                        hook["package_name"], hook["package_version"], hook["item_name"])
                    if package_item is not None:
                        description = package_item.description.get("item_description", "") or ""
                except Exception:
                    # An item without a readable description is still listed
                    description = ""
                items.append({"label": label, "category": menu.menuAction().text(),
                              "version": hook["item_version"],
                              # Some descriptions are saved with their quotation marks
                              "description": str(description).strip().strip('"').strip(),
                              "action": action})
        return items

    @staticmethod
    def _action_text(label, version):
        # The version is right-aligned in the menu (text after a tab), except on
        # macOS where the native menu would read it as a keyboard shortcut.
        separator = " " if sys.platform == "darwin" else "\t"
        return f"{label}{separator}v{version}"

    def on_action(self, hook):
        package_name = hook["package_name"]
        package_version = hook["package_version"]
        item_name = hook["item_name"]
        package_item = self._package_manager.get_package_item(package_name, package_version, item_name)
        package_item.activate()