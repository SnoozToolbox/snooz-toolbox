from qtpy.QtWidgets import QMenuBar, QMenu, QAction

from Endpoints.EndpointHandler import EndpointHandler
from Managers.PackageManager import PackageManager

class OrderedMenu(QMenu):
    def __init__(self, title, parent=None):
        super(OrderedMenu, self).__init__(title, parent)
        self.setObjectName(title)

        self._full_title = title
        # Remove ordered prefix
        title = self._remove_ordered_prefix(title)
        self.menuAction().setText(title)

    @property
    def full_title(self):
        return self._full_title

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
        full_label = label + " v" + hook["item_version"]
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

    def unregister_hook(self, hook):
        assert "parameters" in hook
        hook_parameters = hook["parameters"]
        label = hook_parameters["menu_label"]
        full_label = label + " v" + hook["item_version"]
        
        if hook_parameters["menu_category"] not in self._categories:
            return
        menu_category = self._categories[hook_parameters["menu_category"]]

        if label not in self._actions:
            return
        action = self._actions[label]

        if action.text() == full_label:
            menu_category.removeAction(action)
            del self._actions[label]

            if len(menu_category.actions()) == 0:
                self._menu_bar.removeAction(menu_category.menuAction())
                del self._categories[hook_parameters["menu_category"]]
    
    
    def clear(self):
        # Remove all first level menu from menu_bar
        for menu in self._menu_bar.children():
            if isinstance(menu, OrderedMenu):
                self._menu_bar.removeAction(menu.menuAction())

        self._actions = {}
        self._categories = {}
        self._ordered_categories_menu = []

    def on_action(self, hook):
        package_name = hook["package_name"]
        package_version = hook["package_version"]
        item_name = hook["item_name"]
        package_item = self._package_manager.get_package_item(package_name, package_version, item_name)
        package_item.activate()