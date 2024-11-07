"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
        EventCreator creates a pandas Dataframe of events.

        Inputs:
            event_name(str):    The name of the event.
            group_name(str):    The group of the event.
            start_time(double): The start time of the event from the beginning of the recording.
            duration(double):   The duration of the event.
            channels(str):      A space separated list of channels

        Ouputs:
            pandas.Dataframe: A list of created events.

"""
from flowpipe import SciNode, InputPlug, OutputPlug

import pandas as pd

DEBUG = False

class EventCreator(SciNode):
    """
        EventCreator creates a pandas Dataframe of events.

        Inputs:
            event_name(str):    The name of the event.
            group_name(str):    The group of the event.
            start_time(double): The start time of the event from the beginning of the recording.
            duration(double):   The duration of the event.
            channels(str):      A space separated list of channels
            interval(double):   Interval in seconds between the start of two event
            count(int):         How many events to generate

        Ouputs:
            pandas.Dataframe: A list of created events.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('EventCreator.__init__')
        InputPlug('event_name', self)
        InputPlug('group_name', self)
        InputPlug('start_time', self)
        InputPlug('duration', self)
        InputPlug('channels', self)
        InputPlug('interval', self)
        InputPlug('count', self)
        OutputPlug('events', self)


    def __del__(self):
        if DEBUG: print('EventCreator.__del__')


    def subscribe_topics(self):
        pass


    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'EventCreator.on_topic_update {topic}:{message}')


    def compute(self, event_name, group_name, start_time, duration, channels, interval, count):
        """
        EventCreator creates a pandas Dataframe of events.

        Inputs:
            event_name(str):    The name of the event.
            group_name(str):    The group of the event.
            start_time(double): The start time of the event from the beginning of the recording.
            duration(double):   The duration of the event.
            channels(str):      A space separated list of channels
            interval(double):   Interval in seconds between the start of two event
            count(int):         How many events to generate

        Ouputs:
            pandas.Dataframe: A list of created events.
        """
        if DEBUG: print('EventCreator.compute')
        
        self.clear_cache()
        
        events = []

        for i in range(int(count)):
            events.append({
                'group':        group_name,
                'name':         event_name,
                'start_sec':    float(start_time) + i * float(interval),
                'duration_sec': float(duration),
                'channels':     channels})

        return {"events":pd.DataFrame(events)}
        