"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2025
See the file LICENCE for full license details.

WpliConnectivity
----------------
Compute per-epoch, surrogate-corrected Weighted Phase Lag Index (wPLI) matrices
from EEG epochs, with removal of artifact windows (NaN/Inf/zero).
Returns the per-epoch corrected wPLI and the average across epochs.
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


DEBUG = False

# ---------------------------------------------------------------------
# Main WpliConnectivity Node
# ---------------------------------------------------------------------
class WpliConnectivity(SciNode):
    """
    This node computes corrected Weighted Phase Lag Index (wPLI) connectivity from EEG epochs.

    Workflow
    --------
    1) Stack input epochs into a 3D array with shape (num_epochs, num_channels, num_samples).
    2) Remove artifact windows by dropping any epoch that contains NaNs (across all channels/samples).
    3) For each remaining epoch, compute wPLI between all channel pairs using the analytic (Hilbert) signal.
    4) Build a null distribution via time-shift (lag) surrogates and apply a Wilcoxon test:
    keep (real wPLI − median(surrogates)) if p < p_value and real > median; otherwise set 0.
    5) Return the per-epoch corrected wPLI and the average across epochs, along with channel names.

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
    wpli_results : dict
        {
        "final_wpli":   (num_epochs_kept, C, C) array of corrected wPLI per epoch,
        "average_wpli": (C, C) array = mean over kept epochs,
        "channel_names": list[str] of channel labels
        }
    """

    def __init__(self, **kwargs):
        """ Initialize module WpliConnectivity """
        super().__init__(**kwargs)
        if DEBUG: 
            print('WpliConnectivity.__init__')

        # Input plugs
        InputPlug('epochs', self)         # list of EpochModel
        InputPlug('events', self)          # info
        InputPlug('num_surr', self)
        InputPlug('p_value', self)

        # Output plugs
        OutputPlug('wpli_results', self)    # The final WPLI results

        self._is_master = False

    def compute(self, epochs, events, num_surr, p_value):
        """
        Run corrected wPLI on the provided epochs:
        - normalize parameters,
        - stack epochs to (W, C, T),
        - drop any epoch containing NaNs,
        - compute corrected wPLI per epoch (with time-shift surrogates),
        - average across epochs,
        - return results + channel names.
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
            raise NodeInputException(self.identifier, "signals", 
                "No epochs provided to WpliConnectivity.")
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
        # windowed_signal = windowed_signal[:50, :, :]
        if DEBUG:
            print(f"Shape before removing NaN windows: {windowed_signal.shape}")

        # Treat non-finite values as artifacts (convert to NaN so they get dropped)
        if not np.isfinite(windowed_signal).all():
            windowed_signal = windowed_signal.copy()
            windowed_signal[~np.isfinite(windowed_signal)] = np.nan


        
        # ------------- ARTIFACT REMOVAL (Remove windows with any NaN) -------------
        # valid_windows is a boolean mask: True for windows (epochs) WITHOUT NaNs
        
        # Find epochs (windows) that do NOT have any NaN (across all channels and samples)
        # valid_windows = ~np.isnan(windowed_signal).any(axis=(1, 2))
        valid_windows = (~np.isnan(windowed_signal).any(axis=(1, 2))) & (~(windowed_signal == 0).any(axis=(1, 2)))
        clean_windowed_signal = windowed_signal[valid_windows]

        if clean_windowed_signal.shape[0] == 0:
            raise NodeRuntimeException(self.identifier, "ArtifactRemoval",
                "All epochs were rejected (NaN/Inf/zero). Nothing to compute.")
        
        if DEBUG:
            print(f"Removed {np.sum(~valid_windows)} windowed signals with artifacts (NaNs).")
            print(f"Shape after removing NaN windows: {clean_windowed_signal.shape}")


        info = {
            'sample_rate': fs,
            'channel_names': channel_names,
        }

        # Use the cleaned (NaN-free) epochs for wPLI computation.
        try:
            final_wpli, average_wpli = wpli_parallel_numba(
                clean_windowed_signal, info, num_surr, p_value, n_jobs=-1
            )
            
        except Exception as e:
            raise NodeRuntimeException(self.identifier, "WPLIComputation",
                f"Error in wpli_parallel_numba: {str(e)}")

        # Cache results
        # cache = {
        #     'final_wpli': final_wpli,  # shape (num_windows, C, C)
        #     'average_wpli': average_wpli,  # shape (C, C)
        #     'channel_names': info['channel_names']
        # }
        # self._cache_manager.write_mem_cache(self.identifier, cache)

        # num_windows = final_wpli.shape[0]
        # num_channels = final_wpli.shape[1]
        # self._log_manager.log(self.identifier,
        #     f"WPLI computed over {num_windows} epochs and {num_channels} channels.")

        return {
            'wpli_results': {
                'final_wpli': final_wpli,
                'average_wpli': average_wpli,
                'channel_names': info['channel_names']
            }
        }

# ---------------------------------------------------------------------
# Define wPLI methods (Numba-based):
# ---------------------------------------------------------------------

def get_phase(signal):
    """Compute the Hilbert transform for each channel -> analytic signal."""
    return hilbert(signal)


@njit(parallel=True)
def compute_wpli_numba(analytic_signal1, analytic_signal2):
    # Numba-accelerated wPLI between two analytic signals (same shape).
    # For each pair (i, j), wPLI = |mean(Im(x_i * conj(y_j)))| / mean(|Im(x_i * conj(y_j))|).

    C, T = analytic_signal1.shape
    wpli = np.zeros((C, C), dtype=np.float64)
    
    for i in prange(C):
        for j in range(i + 1, C):
            sum_imag = 0.0
            sum_abs_imag = 0.0
            
            for t in range(T):
                phase_diff = analytic_signal1[i, t] * np.conj(analytic_signal2[j, t])
                imag_val = phase_diff.imag
                sum_imag += imag_val
                sum_abs_imag += abs(imag_val)
            
            numerator = abs(sum_imag / T)
            denominator = sum_abs_imag / T
            
            if denominator < 1e-15:
                wpli_val = 0.0
            else:
                wpli_val = numerator / denominator
            
            wpli[i, j] = wpli_val
            wpli[j, i] = wpli_val
        
        wpli[i, i] = 0.0
    
    return wpli



def compute_surrogate_wpli_numba(analytic_signal, splice):
    """
    Compute a surrogate wPLI by circularly time-shifting all channels by `splice` samples
    and comparing the original analytic signal vs. its shifted version. This lag surrogate
    breaks zero-lag phase-locking by relating channel i at time t to channel j at time t+splice.
    """
    C, T = analytic_signal.shape
    shifted = np.concatenate((analytic_signal[:, splice:], analytic_signal[:, :splice]), axis=1)
    return compute_wpli_numba(analytic_signal, shifted)


def wpli_corrected_numba(signal, num_surrogates, p_value):
    """
    Compute surrogate-corrected wPLI for a single epoch.

    Steps
    -----
    1) Compute uncorrected wPLI on the epoch.
    2) Build `num_surrogates` lag-surrogate wPLI matrices by circularly shifting in time.
    3) For each (i, j), run a Wilcoxon signed-rank test on (surrogates − real):
    if p < p_value and real > median(surrogates), keep (real − median); else 0.

    Parameters
    ----------
    signal : ndarray, shape (C, T)
    num_surrogates : int
    p_value : float

    Returns
    -------
    corrected_wpli : ndarray, shape (C, C)
    """

    if len(signal.shape) != 2:
        raise ValueError("Signal must be 2D: (num_channels, num_samples).")
    
    analytic_sig = get_phase(signal)
    uncorrected_wpli = compute_wpli_numba(analytic_sig, analytic_sig)
    
    num_channels = uncorrected_wpli.shape[0]
    surrogates_wpli = np.zeros((num_surrogates, num_channels, num_channels), dtype=np.float64)
    
    for s in range(num_surrogates):
        splice_idx = np.random.randint(analytic_sig.shape[1])
        surrogates_wpli[s] = compute_surrogate_wpli_numba(analytic_sig, splice_idx)
    
    corrected_wpli = np.zeros_like(uncorrected_wpli)
    for i in range(num_channels):
        for j in range(num_channels):
            if i == j:
                continue
            real_val = uncorrected_wpli[i, j]
            surrogate_vals = surrogates_wpli[:, i, j]
            median_sur = np.median(surrogate_vals)
            
            # _, p = wilcoxon(surrogate_vals - real_val, mode='approx')
            # if p < p_value and (real_val > median_sur):
            #     corrected_wpli[i, j] = real_val - median_sur
            diffs = surrogate_vals - real_val
            # Guard: if all diffs are ~0, Wilcoxon can error; treat as non-significant
            if np.allclose(diffs, 0):
                p = 1.0
            else:
                try:
                    _, p = wilcoxon(diffs, mode='auto')
                except ValueError:
                    p = 1.0
            if p < p_value and (real_val > median_sur):
                corrected_wpli[i, j] = real_val - median_sur

    return corrected_wpli

def wpli_parallel_numba(windowed_signal, info, num_surrogates, p_value, n_jobs=-1):
    """
    windowed_signal: shape (num_windows, num_channels, num_samples)
    info: dictionary with sample_rate, channel_names, etc. (unused in example)
    num_surrogates, p_value: user parameters
    """
    num_windows, num_channels, num_samples = windowed_signal.shape
    final_wpli = np.zeros((num_windows, num_channels, num_channels), dtype=np.float64)
    
    def process_window(w):
        data_2d = windowed_signal[w]  # shape (num_channels, num_samples)
        return wpli_corrected_numba(data_2d, num_surrogates, p_value)

    effective_n_jobs = normalize_n_jobs(n_jobs, num_windows)

    if effective_n_jobs == 1:
        results = [process_window(w) for w in range(num_windows)]
    else:
        backend = select_joblib_backend()
        parallel_kwargs = {"n_jobs": effective_n_jobs, "backend": backend}
        if backend == "threading":
            parallel_kwargs["prefer"] = "threads"
        results = Parallel(**parallel_kwargs)(
            delayed(process_window)(w) for w in range(num_windows)
        )
    
    for w in range(num_windows):
        final_wpli[w] = results[w]
    
    average_wpli = np.mean(final_wpli, axis=0)
    return final_wpli, average_wpli









