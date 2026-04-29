"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2025
See the file LICENCE for full license details.

----------------
Compute per-epoch, surrogate-corrected Directed Phase Lag Index (dPLI) matrices
from EEG epochs, with artifact window removal based on NaN/Inf/zero values.
Returns the per-epoch corrected dPLI and the average across epochs.
"""

import numpy as np
from numba import njit, prange
import pandas as pd
from scipy.signal import hilbert
from scipy.stats import wilcoxon
from joblib import Parallel, delayed

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from commons.parallel_utils import normalize_n_jobs, select_joblib_backend

DEBUG = True

# ---------------------------------------------------------------------
# Main DpliConnectivity Node
# ---------------------------------------------------------------------
class DpliConnectivity(SciNode):
    """
    This node computes corrected Directed Phase Lag Index (dPLI) connectivity from EEG epochs.

    Workflow
    --------
    1) Stack input epochs into a 3D array with shape (num_epochs, num_channels, num_samples).
    2) Treat non-finite values (NaN/Inf) as artifacts; convert to NaN so they can be dropped.
    3) Remove artifact windows by dropping any epoch that contains NaN or zeros (across any channel/sample).
    4) For each remaining epoch, compute dPLI between all channel pairs using Hilbert phase.
    5) Build a null distribution via per-channel time-shift surrogates and apply a Wilcoxon test:
    apply the “gap + 0.5” correction logic when p < p_value; otherwise leave at 0.5 baseline.
    6) Return the per-epoch corrected dPLI and the average across epochs, along with channel names.

    Parameters
    ------
    epochs : list[EpochModel]
        Each EpochModel has .samples (2D array W×T: epochs × samples), .sample_rate, .channel.
    events : pandas.DataFrame
        Present for interface consistency; not used by the computation here.
    num_surr : int
        Number of time-shift surrogates for correction (default: 20).
    p_value : float
        Significance threshold for the Wilcoxon signed-rank test (default: 0.05).

    Returns
    -------
    dpli_results : dict
        {
        "final_dpli":   (num_epochs_kept, C, C) array of corrected dPLI per epoch,
        "average_dpli": (C, C) array = mean over kept epochs,
        "channel_names": list[str] of channel labels
        }
    """

    def __init__(self, **kwargs):
        """ Initialize module DpliConnectivity """
        super().__init__(**kwargs)
        if DEBUG: 
            print('DpliConnectivity.__init__')

        # Input plugs
        InputPlug('epochs', self)         # list of SignalModel
        InputPlug('events', self)          # artifact info
        InputPlug('num_surr', self)
        InputPlug('p_value', self)

        # Output plugs
        OutputPlug('dpli_results', self)    # The final DPLI results

        self._is_master = False

    def compute(self, epochs, events, num_surr, p_value):
        """
        Execute dPLI connectivity computation with artifact removal (NaN/Inf/zero).
        """

        # -- Convert input parameters if they're strings --
        # if isinstance(num_surr, str):
        #     num_surr = int(num_surr)
        # if isinstance(p_value, str):
        #     p_value = float(p_value)

        # Normalize possible None/strings from UI before validating
        if num_surr is None: num_surr = 20
        if isinstance(num_surr, str): num_surr = int(num_surr)

        if p_value is None: p_value = 0.05
        if isinstance(p_value, str): p_value = float(p_value)

        # -- Basic checks --
        if not epochs or len(epochs) == 0:
            raise NodeInputException(self.identifier, "epochs", 
                "No epochs provided to DpliConnectivity.")
        if not isinstance(events, pd.DataFrame):
            raise NodeInputException(self.identifier, "events", 
                "Events must be a pandas DataFrame.")
        if not isinstance(num_surr, int) or num_surr < 1:
            raise NodeInputException(self.identifier, "num_surr",
                f"'num_surr' must be a positive integer; got {num_surr}.")
        if not (0 < p_value <= 1.0):
            raise NodeInputException(self.identifier, "p_value",
                f"'p_value' must be in (0, 1]; got {p_value}.")
        if len(epochs) < 2:
            raise NodeInputException(self.identifier, "epochs",
                f"At least two channels are required for connectivity; got {len(epochs)}.")
        
        # if num_surr is None:
        #     num_surr = 20
        # if p_value is None:
        #     p_value = 0.05


        # fs = epochs[0].sample_rate
        # --- Sampling frequency must be identical across channels ---
        fs_list = [float(e.sample_rate) for e in epochs]
        fs0 = fs_list[0]
        same_fs = all(np.isclose(f, fs0, rtol=0.0, atol=1e-9) for f in fs_list)
        if not same_fs:
            uniq = sorted(set(fs_list))
            raise NodeInputException(self.identifier, "epochs",
                f"All channels must share the same sampling frequency. Got: {uniq}")
        fs = fs0  

        # --- All channels must have identical epoch grid & length ---
        shapes = [np.asarray(e.samples).shape for e in epochs]
        if not all(len(s) == 2 for s in shapes):
            raise NodeRuntimeException(self.identifier, "epochs",
                f"Each EpochModel.samples must be 2D (W, T); got shapes: {shapes}")
        W0, T0 = shapes[0]
        if any(s != (W0, T0) for s in shapes):
            raise NodeRuntimeException(self.identifier, "epochs",
                f"All channels must have identical epoch count and epoch length. Got shapes: {shapes}")
        if T0 < 2:
            raise NodeInputException(self.identifier, "epochs",
                f"Epoch length (T) must be >= 2 samples; got {T0}.")
        
        channel_names = [e.channel for e in epochs]
        # Shape: (num_epochs, num_channels, num_samples)

        # Build (num_epochs, num_channels, num_samples) from the EpochModel list.
        windowed_signal = np.stack([e.samples for e in epochs], axis=1)
        # windowed_signal = windowed_signal[:5, :, :]
        if DEBUG:
            print(f"Shape before artifact removal: {windowed_signal.shape}")

        # Treat non-finite values (NaN/Inf) as artifacts: convert to NaN so they get dropped
        if not np.isfinite(windowed_signal).all():
            windowed_signal = windowed_signal.copy()
            windowed_signal[~np.isfinite(windowed_signal)] = np.nan


        # ------------- ARTIFACT REMOVAL (Remove windows with any NaN) -------------
        # valid_windows is a boolean mask: True for windows (epochs) WITHOUT NaNs

        # Find windows with no NaN and no zeros (across all channels and samples)
        valid_windows = (~np.isnan(windowed_signal).any(axis=(1, 2))) & (~(windowed_signal == 0).any(axis=(1, 2)))
        clean_windowed_signal = windowed_signal[valid_windows]

        if clean_windowed_signal.shape[0] == 0:
            raise NodeRuntimeException(self.identifier, "ArtifactRemoval",
                "All epochs were rejected (NaN/Inf/zero). Nothing to compute.")
        if DEBUG:
            print(f"Removed {np.sum(~valid_windows)} epochs due to NaN/Inf/zero.")
            print(f"Shape after artifact removal: {clean_windowed_signal.shape}")


        info = {
            'sample_rate': fs,
            'channel_names': channel_names,
        }


        # Use the cleaned (NaN-free) epochs for dPLI computation.
        try:
            final_dpli, average_dpli = dpli_parallel_numba(
                clean_windowed_signal, info, num_surr, p_value, n_jobs=-1
            )
        except Exception as e:
            raise NodeRuntimeException(self.identifier, "DPLIComputation",
                f"Error in dpli_parallel_numba: {str(e)}")

        # Cache results
        # cache = {
        #     'final_dpli': final_dpli,  # shape (num_windows, C, C)
        #     'average_dpli': average_dpli,  # shape (C, C)
        #     'channel_names': info['channel_names']
        # }
        # self._cache_manager.write_mem_cache(self.identifier, cache)

        # num_windows = final_dpli.shape[0]
        # num_channels = final_dpli.shape[1]
        # self._log_manager.log(self.identifier,
        #     f"DPLI computed over {num_windows} epochs and {num_channels} channels.")

        # return {
        #     'dpli_results': {
        #         'final_dpli': final_dpli,
        #         'average_dpli': average_dpli,
        #         'channel_names': info['channel_names']
        #     }
        # }

        return {
            'dpli_results': {
                'final_dpli': final_dpli,
                'average_dpli': average_dpli,
                'channel_names': info['channel_names']
            }
        }









# ---------------------------------------------------------------------
# Define dPLI methods (Numba-based):
# ---------------------------------------------------------------------

# Parallelization approach for dpli

def get_phase(signal):
    """
    Return per-channel instantaneous phase via the Hilbert transform.

    Parameters
    ----------
    signal : ndarray, shape (C, T)
        Real-valued time series (channels x samples).

    Returns
    -------
    phase : ndarray, shape (C, T)
        Instantaneous phase angles in [-pi, pi].
    """
    # Hilbert transform
    analytic_sig = hilbert(signal)  # shape (C, T)
    phase = np.angle(analytic_sig)  # shape (C, T)
    return phase

@njit(parallel=True)
def compute_dpli_numba(phase1, phase2):
    # Numba-accelerated dPLI between two phase arrays (same shape).
    # dPLI[i,j] = mean(Heaviside(sin(phase1[i]-phase2[j]), 0.5)) over time.

    C, T = phase1.shape
    dpli = np.zeros((C, C), dtype=np.float64)

    for i in prange(C):
        for j in range(C):
            count_pos = 0.0
            for t in range(T):
                diff = phase1[i, t] - phase2[j, t]
                val_sin = np.sin(diff)

                # Heaviside with 0.5 at zero
                if val_sin > 0:
                    count_pos += 1.0
                elif val_sin == 0:
                    count_pos += 0.5

            dpli[i, j] = count_pos / T

    return dpli


# def directed_phase_index_surrogate(signal):
def directed_phase_index_surrogate_from_phase(phase):
    """
    Per-channel circular time-shift surrogate for dPLI.
    1) Compute original phases.---- 1) Input is the original phase matrix.
    2) For each channel, pick a random non-zero splice index in [1, T-1].
    3) Build a phase matrix with independent circular shifts per channel.
    4) Compute dPLI between original phases and randomly shifted phases.
    """

    # num_channels, num_samples = signal.shape
    # phase = get_phase(signal)

    num_channels, num_samples = phase.shape
    # phase = get_phase(phase)

    # Build random_phase with an independent splice per channel
    random_phase = np.zeros_like(phase)
    for ch in range(num_channels):
        splice = np.random.randint(0, num_samples)
        random_phase[ch, :] = np.concatenate((phase[ch, splice:], phase[ch, :splice]), axis=0)

    # Use our Numba-based dPLI
    # surrogate_dpli = compute_dpli_numba(phase, random_phase)
    # return surrogate_dpli
    return compute_dpli_numba(phase, random_phase)


def dpli_corrected_numba(signal, num_surrogates, p_value):
    """
    Compute surrogate-corrected Directed Phase Lag Index (dPLI) for a single epoch.

    Parameters
    ----------
    signal : ndarray, shape (C, T)
        Real-valued time series for one epoch: C channels × T samples.
    num_surrogates : int
        Number of per-channel circular-shift surrogates.
    p_value : float
        Wilcoxon signed-rank significance threshold.

    Returns
    -------
    corrected_dpli : ndarray, shape (C, C)
        Corrected dPLI. Baseline is 0.5 (= no preferred direction). Values are in [0, 1].

    Method
    ------
    1) Hilbert → instantaneous phase for each channel.
    2) Uncorrected dPLI = dPLI(phase, phase) in [0,1]; NaNs (if any) set to 0.5.
    3) Build a null by per-channel circular time-shifts (independent splice per channel),
       compute surrogate dPLI for each surrogate.
    4) For each (i,j), run Wilcoxon on (surrogates - real):
       - If p < p_value, move away from 0.5 by removing the surrogate median's deviation
         (the "gap + 0.5" logic around the 0.5 baseline).
       - Else keep 0.5.
    Notes
    -----
    - Diagonal reflects self-comparison; keep it at 0.5.
    - Optionally clip to [0,1] for numerical safety.
    """
    if len(signal.shape) != 2:
        raise ValueError("Signal must be 2D: (num_channels, num_samples).")

    num_channels, _ = signal.shape

    # 1) Get phases & uncorrected dPLI
    phase = get_phase(signal)
    uncorrected_dpli = compute_dpli_numba(phase, phase)  # shape (C, C)

    # 2) Replace NaN with 0.5
    uncorrected_dpli[np.isnan(uncorrected_dpli)] = 0.5

    # 3) Generate surrogates
    surrogates_dpli = np.zeros((num_surrogates, num_channels, num_channels))
    for i in range(num_surrogates):
        surrogates_dpli[i] = directed_phase_index_surrogate_from_phase(phase)

    # 4) Initialize corrected to 0.5
    corrected_dpli = 0.5 * np.ones_like(uncorrected_dpli)

    # 5) EXACT "gap + 0.5" significance logic
    for i in range(num_channels):
        for j in range(num_channels):
            if i == j:
                corrected_dpli[i, j] = 0.5
                continue
            x = uncorrected_dpli[i, j]
            surrogates_dpli_ij = surrogates_dpli[:, i, j]
            med_s = np.median(surrogates_dpli_ij)

            # _, p = wilcoxon(surrogates_dpli_ij - x)

            diffs = surrogates_dpli_ij - x
            # Guard: if all diffs ~ 0, Wilcoxon is undefined; treat as non-significant.
            if np.allclose(diffs, 0.0):
                p = 1.0
            else:
                try:
                    # Use approximation only when zeros are present in paired differences.
                    # Otherwise keep SciPy's automatic mode to preserve usual behavior.
                    if np.any(np.isclose(diffs, 0.0)):
                        _, p = wilcoxon(diffs, zero_method="zsplit", mode="approx")
                    else:
                        _, p = wilcoxon(diffs, mode="auto")
                except ValueError:
                    p = 1.0

            if p < p_value:
                # Case 1 & 2
                if x >= 0.5 and med_s >= 0.5:
                    gap = x - med_s
                    if gap > 0:
                        corrected_dpli[i, j] = gap + 0.5

                # Case 3 & 4
                elif x <= 0.5 and med_s <= 0.5:
                    gap = x - med_s
                    if gap < 0:
                        corrected_dpli[i, j] = gap + 0.5

                # Case 5 & 6
                elif x >= 0.5 and med_s <= 0.5:
                    extra = 0.5 - med_s
                    corrected_dpli[i, j] = extra + x

                # Case 7 & 8
                elif x <= 0.5 and med_s >= 0.5:
                    extra = med_s - 0.5
                    corrected_dpli[i, j] = x - extra

    return corrected_dpli


def dpli_parallel_numba(windowed_signal, info, num_surrogates, p_value, n_jobs=-1):
    """
    Compute corrected dPLI for each epoch (window) in parallel.

    Parameters
    ----------
    windowed_signal : ndarray, shape (W, C, T)
        W epochs/windows, each C channels × T samples. Should be NaN/Inf/zero-free.
    info : dict
        Metadata such as "sample_rate" and "channel_names" (not used here).
    num_surrogates : int
    p_value : float
    n_jobs : int
        Joblib parallel workers (use -1 for all cores).

    Returns
    -------
    final_dpli : ndarray, shape (W, C, C)
    average_dpli : ndarray, shape (C, C)
    """
    # num_windows = windowed_signal.shape[0]
    # num_channels = info['num_channels']
    # final_dpli = np.zeros((num_windows, num_channels, num_channels))

    num_windows, num_channels, num_samples = windowed_signal.shape
    final_dpli = np.zeros((num_windows, num_channels, num_channels), dtype=np.float64)

    def process_window(w):
        return dpli_corrected_numba(windowed_signal[w, :, :], num_surrogates, p_value)

    effective_n_jobs = normalize_n_jobs(n_jobs, num_windows)

    if effective_n_jobs == 1:
        results = [process_window(w) for w in range(num_windows)]
    else:
        backend = select_joblib_backend()
        parallel_kwargs = {"n_jobs": effective_n_jobs, "backend": backend}
        if backend == "threading":
            parallel_kwargs["prefer"] = "threads"

        # Parallel over windows
        results = Parallel(**parallel_kwargs)(
            delayed(process_window)(w) for w in range(num_windows)
        )

    for w in range(num_windows):
        final_dpli[w] = results[w]

    average_dpli = np.mean(final_dpli, axis=0)
    return final_dpli, average_dpli



