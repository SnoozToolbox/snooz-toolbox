from qtpy import QtCore

from CEAMSTools.SleepReport.Commons.EventsModel import EventsModel
from CEAMSTools.SleepReport.Commons.IdentificationModel import IdentificationModel
from CEAMSTools.SleepReport.Commons.TemporalLinksModel import TemporalLinksModel


class FileItem():
    def __init__(self, data, id_data, events_data, pub_sub_manager):
        self._data = data
        self._pub_sub_manager = pub_sub_manager
        self._id_model = IdentificationModel(id_data)
        self._events_model = EventsModel(self, events_data)
        self._temporal_links_model = TemporalLinksModel(self)
        
    @property
    def full_filename(self):
        return self._data[1]

    @property
    def data(self):
        return self._data

    @property
    def id_model(self):
        return self._id_model

    @property
    def events_model(self):
        return self._events_model

    @property
    def temporal_links_model(self):
        return self._temporal_links_model

    def update_reports_count(self):
        event_reports_count = self._events_model.reports_count()
        self._data[2] = event_reports_count
        tl_count = self._temporal_links_model.reports_count()
        self._data[3] = tl_count

    def on_add_report(self, report):
        self.temporal_links_model.on_add_report(report)
        self.update_reports_count()

    def on_remove_report(self, report):
        self.temporal_links_model.on_remove_report(report)
        self.update_reports_count()

    def on_modify_report(self, report, previous_name):
        self.temporal_links_model.on_modify_report(report, previous_name)
