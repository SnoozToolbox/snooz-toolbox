"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    ExtendEvents
    Extends or shrinks event windows by a given percentage of their duration.
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import pandas as pd

DEBUG = False

class ExtendEvents(SciNode):
    """
    Extend or shrink events by a percentage of their duration, applied to **each side**.

    Parameters
    ----------
    events : pandas.DataFrame
        A dataframe with required columns:
        ['group', 'name', 'start_sec', 'duration_sec', 'channels']
    per_side_exten_percent : float
        Percentage to extend (+) or shrink (−) **on each side**.
        For example:
            50.0 → start moves 50% earlier, end moves 50% later
           -20.0 → start moves 20% later, end moves 20% earlier

    Returns
    -------
    extended_events : pandas.DataFrame
        Copy of `events` with updated 'start_sec' and 'duration_sec'.
    """

    def __init__(self, **kwargs):
        """Initialize module ExtendEvents"""
        super().__init__(**kwargs)
        if DEBUG: print('ExtendEvents.__init__')

        # Input plugs
        InputPlug('events', self)
        InputPlug('per_side_exten_percent', self)

        # Output plugs
        OutputPlug('extended_events', self)

        self._is_master = False 
    
    def compute(self, events, per_side_exten_percent):
        """
        Extend or shrink events based on percentage per side.
        """
        # ---- Validate inputs ----
        if not isinstance(per_side_exten_percent, (int, float)):
            raise NodeInputException(self.identifier, "percent", "per_side_exten_percent must be int or float.")

        if not isinstance(events, pd.DataFrame):
            raise NodeInputException(self.identifier, "events", "`events` must be a pandas DataFrame")

        try:
            extended = events.copy()

            # Amount to extend/shrink each side
            delta_side = extended["duration_sec"] * (per_side_exten_percent / 100.0)

            # Adjust start and duration
            extended["start_sec"] = extended["start_sec"] - delta_side
            extended["duration_sec"] = extended["duration_sec"] + 2 * delta_side

            # Prevent negative durations
            extended["duration_sec"] = extended["duration_sec"].clip(lower=0)

        except Exception as e:
            raise NodeRuntimeException(f"ExtendEvents failed: {e}")

        return {
            "extended_events": extended
        }