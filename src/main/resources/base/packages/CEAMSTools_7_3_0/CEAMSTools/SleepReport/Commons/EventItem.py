from CEAMSTools.SleepReport.Commons.GroupItem import GroupItem

class EventItem(GroupItem):
    def __init__(self, group_name, event_name, file_item, original_group_name=None):
        super().__init__(group_name, file_item)
        self._original_group_name = original_group_name
        self._event_name = event_name


    @property
    def original_group_name(self):
        return self._original_group_name

    @property
    def event_name(self):
        return self._event_name
