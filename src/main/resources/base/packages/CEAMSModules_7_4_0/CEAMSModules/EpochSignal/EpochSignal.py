"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

EpochSignal
-----------
This module segments EEG signals into overlapping or non-overlapping epochs
of fixed duration, optionally discarding or padding the last segment.
It takes the (potentially discontinuous) SignalModels from the
SignalsFromEvents node, slices them into epochs, and then
groups all epochs for each channel into one EpochModel.

Inputs:
    signals : list of SignalModel
    events   : pandas.DataFrame
    epoch_length_sec : float or str
    overlap_sec      : float or str
    droplast         : bool or str

Outputs:
    epochs : list of EpochModel  (one per channel)
    events : pandas.DataFrame    (one row per epoch)
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import numpy as np
import pandas as pd

from CEAMSModules.EpochSignal.EpochModel import EpochModel

DEBUG = False

class EpochSignal(SciNode):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        InputPlug('signals',       self)
        InputPlug('events',        self)
        InputPlug('epoch_length_sec', self)
        InputPlug('overlap_sec',      self)
        InputPlug('droplast',        self)

        OutputPlug('epochs', self)
        OutputPlug('events', self)

    def compute(self, signals, events, epoch_length_sec, overlap_sec, droplast):

        # --- 1) INPUT CHECKS ---
        if not isinstance(signals, list):
            raise NodeInputException(self.identifier, "signals",
                f"Expected list of SignalModel, got {type(signals)}")
        if not signals:
            raise NodeInputException(self.identifier, "signals",
                "Input signal list is empty.")
        if not isinstance(events, pd.DataFrame):
            raise NodeInputException(self.identifier, "events",
                f"Expected pandas.DataFrame, got {type(events)}")
        try:
            epoch_length_sec = float(epoch_length_sec)
            overlap_sec = float(overlap_sec)
        except Exception as e:
            raise NodeInputException(self.identifier, "epoch_length_sec/overlap_sec",
                f"Could not convert epoch_length_sec or overlap_sec to float: {e}")

        if epoch_length_sec <= 0:
            raise NodeInputException(self.identifier, "epoch_length_sec",
                "Epoch length must be positive.")
        if overlap_sec < 0:
            raise NodeInputException(self.identifier, "overlap_sec",
                "Overlap must be non-negative.")
        if overlap_sec >= epoch_length_sec:
            raise NodeInputException(self.identifier, "overlap_sec",
                "Overlap must be less than epoch length.")
        
        # # --- 2) PARAM COERCION ---
        # epoch_length_sec = float(epoch_length_sec)
        # overlap_sec      = float(overlap_sec)

        # Always drop the last partial epoch:
        if DEBUG:
            print("################################################################################################")
            for sigg in signals:
                print(f"for channel:{sigg.channel} sample_rate is :{sigg.sample_rate} and shape is:{sigg.samples.shape}")
            print("################################################################################################")

        droplast = True
        if DEBUG:
            print("--------------------------------------------------------------------------------------------------------------")
            channels = []
            for signal in signals:
                channels.append(signal.channel)
            print(f"length signal model in the input of EpochSignal is {len(channels)}")
            print("--------------------------------------------------------------------------------------------------------------")

        # >>>>>>>>>>>> <<<<<<<<<<<<<<
        total_points = {}
        total_epochs = {}
        for sig in signals:
            ch = sig.channel
            if ch not in total_points.keys():
                total_points[ch] = 0
            if ch not in total_epochs.keys():
                total_epochs[ch] = 0
            total_points[ch] += len(sig.samples)
            total_epochs[ch] += 1
        if DEBUG:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            for ch, total in total_points.items():
                print(f"Channel '{ch}' TOTAL: {total} points in {total_epochs[ch]} different segments")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            # >>>>>>>>>>>> <<<<<<<<<<<<<<

        channel_segments = {}
        for sig in signals:
            ch_name = sig.channel
            if ch_name not in channel_segments.keys():
                channel_segments[ch_name] = []
            channel_segments[ch_name].append(sig)


        for ch_name in channel_segments.keys():
            channel_segments[ch_name] = self.merge_back_to_back_segments(channel_segments[ch_name])


        epochs = []
        for ch_name, segments in channel_segments.items():
            if not segments:
                raise NodeRuntimeException(
                    self.identifier, "EpochSignal",
                    f"No segments found for channel '{ch_name}'. This usually means your input signals list was missing data for this channel.")
            em = EpochModel()
            em.sample_rate = segments[0].sample_rate
            em.channel = segments[0].channel
            epoch_samples = []
            start_times = []
            end_times = []
            for segment in segments:
                segmented_samples = self.segment_epochs(segment.samples, segment.sample_rate, epoch_length_sec, overlap_sec, droplast)
                epoch_samples.append(segmented_samples)
                start_times += list(np.arange(segmented_samples.shape[0])*epoch_length_sec + segment.start_time)
                end_times += list(np.arange(1, segmented_samples.shape[0]+1)*epoch_length_sec + segment.start_time)

            em.start_time = start_times
            em.end_time = end_times
            em.samples = np.concatenate(epoch_samples)
            em.num_epochs = em.samples.shape[0]
            em.duration = epoch_length_sec
            em.alias          = getattr(segments[0], 'alias', '')
            em.meta           = getattr(segments[0], 'meta', {}).copy()
            em.is_modified    = getattr(segments[0], 'is_modified', False)
            em.montage_index  = getattr(segments[0], 'montage_index', 0)
            epochs.append(em)
            
        if DEBUG:
            for em in epochs:
                print(f'epoch for channel {em.channel} shape:{em.samples.shape} sample rate:{em.sample_rate} start_time:{em.start_time[:10]} end_time:{em.end_time[:10]} duration:{em.duration}')

        self._log_manager.log(
            self.identifier,
            f"[EpochSignal] processed {len(epochs)} channels, {em.num_epochs} for each channel"
        )

        cache = {
            'n_channels'        : len(epochs),
            'epochs_per_channel': {em.channel: em.num_epochs for em in epochs},
            # 'events_df'         : events_df
        }
        self._cache_manager.write_mem_cache(self.identifier, cache)

        # --- 6) RETURN ---
        return {
            'epochs': epochs,
            'events': events
        }





    def merge_back_to_back_segments(self, segments, *, tol=1e-3):
        """Merge only segments that touch exactly (no gap, no overlap)."""
        if not segments:
            return []

        # segs = sorted(segments, key=lambda s: s.start_time)
        # merged = [segs[0]]

        try:
            segs = sorted(segments, key=lambda s: s.start_time)
        except Exception as e:
            raise NodeRuntimeException(self.identifier, "merge_back_to_back_segments",
                f"Error sorting segments by start_time: {e}")
        merged = [segs[0]]

        for seg in segs[1:]:
            prev = merged[-1]
            prev_end = prev.start_time + prev.duration

            # REQUIRE: new segment starts *right after* previous ends (±tol)
            delta = seg.start_time - prev_end
            if -tol <= delta <= tol:                      # strictly consecutive
                prev.samples   = np.concatenate([prev.samples, seg.samples])
                prev.duration = prev.duration + seg.duration
            else:                                       # gap or overlap → keep separate
                merged.append(seg)

        return merged





    def segment_epochs(self, sig, sf, window_sec, overlap_sec, droplast):

        # This function is to get overlapping windowed data in points
        # we assume data is a c*p matrix where c are number of channels and p is the number of points
        step_sec = window_sec - overlap_sec
        window_size = int(window_sec * sf)     #in points

        if len(sig) < window_size:
            raise NodeRuntimeException(self.identifier, "segment_epochs",
                f"Signal length {len(sig)} is shorter than window size {window_size}")
        
        step = np.floor(step_sec * sf)

        if droplast:
            iterator = np.arange(0, len(sig)-window_size + 1, step).astype(int)  if (len(sig)-window_size) >= 0 else []
        else:
            iterator = np.arange(0, len(sig), step).astype(int)

        segmented_sig = np.zeros((len(iterator), window_size))
        for index, it in enumerate(iterator):
            segmented_sig[index, :] = sig[it:it+window_size]
        return segmented_sig


    # Code examples

    # Raise NodeInputException if the an input is wrong. This type of
    # exception will stop the process with the error message given in parameter.
    # raise NodeInputException(self.identifier, "my_input", \
    #        f"EpochSignal this input is wrong.")

    # Raise NodeRuntimeException if there is a critical error during runtime. 
    # This will usually be a user error, a file that can't be read due to security reason,
    # a parameter that is out of bound, etc. This exception will stop and skip the current
    # process but will not stop the followin iterations if a master node is not done.
    # Once the master node is completed, a dialog will appear to show all NodeRuntimeException
    # to the user.
    #
    # Set the iteration_identifier if this module is a master node.
    # This will be used to identify the problematic iteration if a runtime exception occurs
    # in any module during this process. For example, a master node that reads one file at a 
    # could set the identifier to the name of the file.
    # self.iteration_identifier = current_filename
    #
    # Iteration count and counter are used to show a progress bar in percent.
    # Update these when creating a master node to properly show the progress 
    # for each iteration. This is optional and can be ignored but it's a good practice
    # to do for your users.
    #self.iteration_count = the total amout of iteration to make
    #self.iteration_counter = the current iteration number

    #
    # Raise the runtime exception
    # raise NodeRuntimeException(self.identifier, "files", \
    #        f"Some file could not be open.")

    #
    #

    # Write to the cache to use the data in the resultTab
    # cache = {}
    # cache['this_is_a_key'] = 42
    # self._cache_manager.write_mem_cache(self.identifier, cache)

    # Log message for the Logs tab
    # self._log_manager.log(self.identifier, "This module does nothing.")

    # return {
    #     'epochs': None,
    #     'events': None
    # }