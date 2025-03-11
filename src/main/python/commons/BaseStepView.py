"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
class BaseSettingsView
    Defines the minimum interace of a SettingsView class
"""
from commons.BaseSettingsView import BaseSettingsView

class BaseStepView(BaseSettingsView):
    def __init__(self, parent_node, pub_sub_manager, context_manager, process_manager, asset_manager, **kwargs):
        super().__init__(options=None, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._context_manager = context_manager
        self._process_manager = process_manager
        self._asset_manager = asset_manager
        self._pub_sub_manager.subscribe(self, self._context_manager.topic)
    
    @property
    def process_manager(self):
        return self._process_manager

    def on_topic_update(self, topic, message, sender):
        pass
        #if topic == self._context_manager.topic:
        #    print(f"BaseStepView.on_topic_update:{topic}:{message}")