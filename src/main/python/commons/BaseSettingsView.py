"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
"""
class BaseSettingsView
    Defines the minimum interace of a SettingsView class
"""
class BaseSettingsView:
    def __init__(self, options = None, custom_params = None, **kwargs):
        super().__init__(**kwargs)
        self._options = options
        self._custom_params = custom_params

    @property
    def custom_params(self):
        return self._custom_params
    
    def on_apply_settings(self):
        raise NotImplementedError()
    
    def on_validate_settings(self):
        return True

    def load_settings(self):
        raise NotImplementedError()