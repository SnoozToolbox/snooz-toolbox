"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    RemoveChannelArtefact
    TODO CLASS DESCRIPTION
"""
import pandas as pd

from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from flowpipe import SciNode, InputPlug, OutputPlug
from widgets.WarningDialog import WarningDialog

from CEAMSModules.PSGReader.SignalModel import SignalModel

DEBUG = False

class RemoveChannelArtefact(SciNode):
    """
        Remove full-channel artefacts from signals and events.

        This module accepts one or multiple artefact group/name pairs to identify
        channel-level artefacts. It removes any SignalModel whose channel matches
        these artefacts (after warning if the artefact does not span the full signal)
        and drops the corresponding events from the DataFrame.

        Inputs:
        -------
        signals : list of SignalModel
            List of SignalModel objects, each with attributes:
                .samples (numpy array),
                .sample_rate (Hz),
                .channel (str),
                .start_time (s),
                .end_time (s) and .duration (s).
        events : pandas.DataFrame
            DataFrame of events with columns ['group','name','start_sec','duration_sec','channels'].
        artefact_group : str
            Comma-separated artefact event groups (e.g. 'art_inspector').
        artefact_name : str
            Comma-separated artefact event names (e.g. 'non_brain,art_channel').
            If only one group is given but multiple names, that group is applied to all names.

        Outputs:
        -------
        clean_signals : list of SignalModel
            Signals with any full-channel artefacts removed.
        clean_events : pandas.DataFrame
            Events DataFrame with specified artefact rows removed.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('RemoveChannelArtefact.__init__')

        # Input plugs
        InputPlug('signals', self)
        InputPlug('events', self)
        InputPlug('artefact_group', self)
        InputPlug('artefact_name', self)

        # Output plugs
        OutputPlug('clean_signals', self)
        OutputPlug('clean_events', self)

        self._is_master = False

    def compute(self, signals, events, artefact_group, artefact_name):
        """
        RemoveChannelArtefact.compute:

        Parameters
        ----------
        signals : list of SignalModel
            The original list of signals.
        events : pandas.DataFrame
            The events DataFrame, possibly containing artefact rows.
        artefact_group : str
            Comma-separated list of groups to remove.
        artefact_name : str
            Comma-separated list of names to remove.
            If one group and multiple names are given, that single group applies to all names.

        Returns
        -------
        clean_signals : list of SignalModel
            Signals list with specified artefact channels removed.
        clean_events : pandas.DataFrame
            Events DataFrame with artefact rows removed.

        Raises
        ------
        NodeInputException
            For invalid input types or mismatched lists.
        NodeRuntimeException
            For runtime errors.
        """
        # Validate inputs
        if not isinstance(signals, list):
            raise NodeInputException(self.identifier, 'signals',
                f'Expected signals to be list, got {type(signals)}')
        if not isinstance(events, pd.DataFrame):
            raise NodeInputException(self.identifier, 'events',
                f'Expected events to be pandas.DataFrame, got {type(events)}')
        if not isinstance(artefact_group, str) or not isinstance(artefact_name, str):
            raise NodeInputException(self.identifier, 'artefact_group/name',
                'artefact_group and artefact_name must be strings')

        # Parse lists of groups and names
        groups = [g.strip() for g in artefact_group.split(',') if g.strip()]
        names  = [n.strip() for n in artefact_name.split(',') if n.strip()]

        if DEBUG:
            print(events['group'].unique())
            print(events['name'].unique())

        # Support single group with multiple names
        if len(groups) == 1 and len(names) > 1:
            groups = groups * len(names)
        # Support single name with multiple groups
        if len(names) == 1 and len(groups) > 1:
            names = names * len(groups)
        if len(groups) != len(names):
            raise NodeInputException(self.identifier, 'artefact_name',
                'artefact_group and artefact_name must have the same number of items')

        # make sure both DataFrame columns and our lists are trimmed
        grp_series = events['group'].astype(str).str.strip()
        nam_series = events['name'].astype(str).str.strip()

        # pick *all* rows whose (stripped) group is in our groups *and* whose (stripped) name is in our names
        mask = grp_series.isin(groups) & nam_series.isin(names)
        artefact_rows = events.loc[mask].copy()

        # now the unique channels that had those artefacts
        channels_to_remove = artefact_rows['channels'].astype(str).str.strip().unique().tolist()

        self._log_manager.log(self.identifier,
        f"→ Found {len(artefact_rows)} artefact rows on channels: {channels_to_remove}")


        # Warn if artefact does not cover full signal
        for ch in channels_to_remove:
            sig = next((s for s in signals if s.channel == ch), None)
            if sig is None:
                continue
            subset = artefact_rows[artefact_rows['channels'] == ch]
            start_min = subset['start_sec'].min()
            end_max = (subset['start_sec'] + subset['duration_sec']).max()
            full_start = sig.start_time
            full_end   = sig.start_time + sig.duration
            if not (start_min <= full_start and end_max >= full_end):
                WarningDialog(
                    f"Artefact ({','.join(groups)},{','.join(names)}) on channel {ch} does not span full signal."
                )

        # Filter out signals and events
        clean_signals = [s for s in signals if s.channel not in channels_to_remove]
        clean_events = events[~(
            events['group'].isin(groups) &
            events['name'].isin(names) &
            events['channels'].isin(channels_to_remove)
        )].reset_index(drop=True)

        # Cache removed info
        cache = {
            'removed_channels': channels_to_remove,
            'removed_events': artefact_rows
        }
        self._cache_manager.write_mem_cache(self.identifier, cache)

        self._log_manager.log(self.identifier, f"RemoveChannelArtefact cache: {cache}")

        return {
            'clean_signals': clean_signals,
            'clean_events': clean_events
        }

# from flowpipe import SciNode, InputPlug, OutputPlug
# from commons.NodeInputException import NodeInputException
# from commons.NodeRuntimeException import NodeRuntimeException

# DEBUG = False

# class RemoveChannelArtefact(SciNode):
#     """
#     TODO CLASS DESCRIPTION

#     Parameters
#     ----------
#         signals: TODO TYPE
#             TODO DESCRIPTION
#         events: TODO TYPE
#             TODO DESCRIPTION
#         artefact_group: TODO TYPE
#             TODO DESCRIPTION
#         artefact_name: TODO TYPE
#             TODO DESCRIPTION
        

#     Returns
#     -------
#         clean_signals: TODO TYPE
#             TODO DESCRIPTION
#         clean_events: TODO TYPE
#             TODO DESCRIPTION
        
#     """
#     def __init__(self, **kwargs):
#         """ Initialize module RemoveChannelArtefact """
#         super().__init__(**kwargs)
#         if DEBUG: print('RemoveChannelArtefact.__init__')

#         # Input plugs
#         InputPlug('signals',self)
#         InputPlug('events',self)
#         InputPlug('artefact_group',self)
#         InputPlug('artefact_name',self)
        

#         # Output plugs
#         OutputPlug('clean_signals',self)
#         OutputPlug('clean_events',self)
        

#         # Init module variables
#         self.this_is_an_example_you_can_delete_it = 0

#         # A master module allows the process to be reexcuted multiple time.
#         # For exemple, this is useful when the process must be repeated over multiple
#         # files. When the master module is done, ie when all the files were process, 
#         # The compute function must set self.is_done = True
#         # There can only be 1 master module per process.
#         self._is_master = False 
    
#     def compute(self, signals,events,artefact_group,artefact_name):
#         """
#         TODO DESCRIPTION

#         Parameters
#         ----------
#             signals: TODO TYPE
#                 TODO DESCRIPTION
#             events: TODO TYPE
#                 TODO DESCRIPTION
#             artefact_group: TODO TYPE
#                 TODO DESCRIPTION
#             artefact_name: TODO TYPE
#                 TODO DESCRIPTION
            

#         Returns
#         -------
#             clean_signals: TODO TYPE
#                 TODO DESCRIPTION
#             clean_events: TODO TYPE
#                 TODO DESCRIPTION
            

#         Raises
#         ------
#             NodeInputException
#                 If any of the input parameters have invalid types or missing keys.
#             NodeRuntimeException
#                 If an error occurs during the execution of the function.
#         """

#         # Code examples

#         # Raise NodeInputException if the an input is wrong. This type of
#         # exception will stop the process with the error message given in parameter.
#         # raise NodeInputException(self.identifier, "my_input", \
#         #        f"RemoveChannelArtefact this input is wrong.")

#         # Raise NodeRuntimeException if there is a critical error during runtime. 
#         # This will usually be a user error, a file that can't be read due to security reason,
#         # a parameter that is out of bound, etc. This exception will stop and skip the current
#         # process but will not stop the followin iterations if a master node is not done.
#         # Once the master node is completed, a dialog will appear to show all NodeRuntimeException
#         # to the user.
#         #
#         # Set the iteration_identifier if this module is a master node.
#         # This will be used to identify the problematic iteration if a runtime exception occurs
#         # in any module during this process. For example, a master node that reads one file at a 
#         # could set the identifier to the name of the file.
#         # self.iteration_identifier = current_filename
#         #
#         # Iteration count and counter are used to show a progress bar in percent.
#         # Update these when creating a master node to properly show the progress 
#         # for each iteration. This is optional and can be ignored but it's a good practice
#         # to do for your users.
#         #self.iteration_count = the total amout of iteration to make
#         #self.iteration_counter = the current iteration number

#         #
#         # Raise the runtime exception
#         # raise NodeRuntimeException(self.identifier, "files", \
#         #        f"Some file could not be open.")

#         #
#         #

#         # Write to the cache to use the data in the resultTab
#         # cache = {}
#         # cache['this_is_a_key'] = 42
#         # self._cache_manager.write_mem_cache(self.identifier, cache)

#         # Log message for the Logs tab
#         self._log_manager.log(self.identifier, "This module does nothing.")

#         return {
#             'clean_signals': None,
#             'clean_events': None
#         }