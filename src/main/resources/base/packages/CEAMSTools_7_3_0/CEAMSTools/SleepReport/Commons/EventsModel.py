from qtpy.QtCore import QObject, Qt

from CEAMSTools.SleepReport.Commons.EventItem import EventItem
from CEAMSTools.SleepReport.Commons.GroupItem import GroupItem

class EventsModel(QObject):
    def __init__(self, file_item, events_data=None):
        super().__init__()
        self._items = []
        self._file_item = file_item
        if events_data is not None:
            self._init_items(events_data)

    @property
    def items(self):
        return self._items

    def clear(self):
        for group_item in self._items:
            group_item.reports_model.clear()
            for i in range( group_item.childCount()):
                event_item = group_item.child(i)
                event_item.reports_model.clear()
            

    def reports_count(self):
        count = 0
        for event_item in self._items:
            count = count + event_item.reports_count()
        return count

    def _init_items(self, events_data):
        for raw_event in events_data.itertuples():
            if raw_event.name == '':
                continue
        
            group_item = self.find_group_by_name(raw_event.group)
            if group_item is None:
                group_item = GroupItem(raw_event.group, self._file_item)
                group_item.setData(0, Qt.DisplayRole, raw_event.group)
                group_item.setData(1, Qt.DisplayRole, 0)
                group_item.setData(2, Qt.DisplayRole, 0)
                self._items.append(group_item)

            event_item = self.find_event_by_name(group_item, raw_event.name)
            if event_item is None:
                event_item = EventItem(raw_event.group, raw_event.name, self._file_item)
                event_item.setData(0, Qt.DisplayRole, raw_event.name)
                event_item.setData(1, Qt.DisplayRole, 0)
                event_item.setData(2, Qt.DisplayRole, 0)
                group_item.addChild(event_item)

            group_event_count = group_item.data(1, Qt.DisplayRole) + 1
            group_item.setData(1, Qt.DisplayRole, group_event_count)
            event_count = event_item.data(1, Qt.DisplayRole) + 1
            event_item.setData(1, Qt.DisplayRole, event_count)
            
    def find_group_by_name(self, name):
        for item in self._items:
            if item.data(0, Qt.DisplayRole) == name:
                return item
        return None

    def find_event_by_name(self, group_item, event_name):
        for i in range(group_item.childCount()):
            event_item = group_item.child(i)
            if event_item.data(0, Qt.DisplayRole) == event_name:
                return event_item
        return None

    def add_group(self, group_data, events):
        group_item = GroupItem(group_data['name'], self._file_item)
        group_item.setData(0, Qt.DisplayRole, group_data['name'])
        group_item.setData(1, Qt.DisplayRole, group_data['count'])
        group_item.setData(2, Qt.DisplayRole, 0)

        for event_data in events:
            event_item = EventItem(group_data['name'], event_data['name'], self._file_item, event_data['original_group_name'])
            event_item.setData(0, Qt.DisplayRole, event_data['name'])
            event_item.setData(1, Qt.DisplayRole, event_data['count'])
            event_item.setData(2, Qt.DisplayRole, 0)
            group_item.addChild(event_item)

        self._items.append(group_item)
