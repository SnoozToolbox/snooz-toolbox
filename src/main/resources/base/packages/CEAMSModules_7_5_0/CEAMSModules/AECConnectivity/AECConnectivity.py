"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

AECConnectivity
----------------
Compute per-epoch Amplitude Envelope Correlation (AEC) matrices from EEG epochs,
with artifact window removal based on NaN/Inf/zero values.
Returns the per-epoch AEC and the average across epochs.
"""

import numpy as np
import pandas as pd
from scipy.signal import hilbert
from scipy.stats import pearsonr
from joblib import Parallel, delayed


from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from commons.parallel_utils import normalize_n_jobs, select_joblib_backend

DEBUG = True

class AECConnectivity(SciNode):
    """
    This node computes Amplitude Envelope Correlation (AEC) connectivity from EEG epochs.

    Workflow
    --------
    1) Stack input epochs into a 3D array with shape (num_epochs, num_channels, num_samples).
    2) Treat non-finite values (NaN/Inf) as artifacts; convert to NaN so they can be dropped.
    3) Remove artifact windows by dropping any epoch that contains NaN or zeros (across any channel/sample).
    4) For each remaining epoch, compute AEC between all channel pairs using:
       - Hilbert transform to extract amplitude envelopes
       - Leakage correction via linear regression to reduce volume conduction
       - Pearson correlation between corrected envelopes
    5) Return the per-epoch AEC and the average across epochs, along with channel names.

    Parameters
    ----------
    epochs : list[EpochModel]
        Each EpochModel has .samples (2D array W×T: epochs × samples), .sample_rate, .channel.
    events : pandas.DataFrame
        Present for interface consistency; not used by the computation here.

    Returns
    -------
    aec_results : dict
        {
        "final_aec":   (num_epochs_kept, C, C) array of AEC per epoch,
        "average_aec": (C, C) array = mean over kept epochs,
        "channel_names": list[str] of channel labels
        }
    
    Notes
    -----
    Unlike dPLI and wPLI, AEC does not include surrogate-based statistical correction,
    as the leakage correction step already addresses spurious connectivity from volume conduction.
    """
    def __init__(self, **kwargs):
        """ Initialize module AECConnectivity """
        super().__init__(**kwargs)
        if DEBUG: print('AECConnectivity.__init__')

        # Input plugs
        InputPlug('epochs',self)
        InputPlug('events',self)
        

        # Output plugs
        OutputPlug('aec_results',self)
        

        self._is_master = False 
    
    def compute(self, epochs, events):
        """
        Execute AEC connectivity computation with artifact removal (NaN/Inf/zero).

        Parameters
        ----------
        epochs : list[EpochModel]
            Each element has .samples (2D: W epochs × T samples), .sample_rate, .channel.
        events : pandas.DataFrame
            Artifact information (not actively used in computation, kept for interface consistency).

        Returns
        -------
        dict
            Contains 'aec_results' with keys:
            - 'final_aec': ndarray (num_epochs_kept, C, C)
            - 'average_aec': ndarray (C, C)
            - 'channel_names': list[str]

        Raises
        ------
        NodeInputException
            If epochs are missing, events is not a DataFrame, fewer than 2 channels,
            or sampling frequencies/epoch shapes don't match across channels.
        NodeRuntimeException
            If all epochs are rejected due to artifacts, or if AEC computation fails.
        """

        # -- Basic checks --
        if not epochs or len(epochs) == 0:
            raise NodeInputException(self.identifier, "signals", 
                "No epochs provided to AECConnectivity.")
        if not isinstance(events, pd.DataFrame):
            raise NodeInputException(self.identifier, "events", 
                "Events must be a pandas DataFrame.")
        if len(epochs) < 2:
            raise NodeInputException(self.identifier, "epochs",
                f"At least two channels are required for connectivity; got {len(epochs)}.")
        
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

        # Build (num_epochs, num_channels, num_samples) from the EpochModel list.
        windowed_signal = np.stack([e.samples for e in epochs], axis=1)
        if DEBUG:
            print(f"Shape before artifact removal: {windowed_signal.shape}")

        # Treat non-finite values (NaN/Inf) as artifacts: convert to NaN so they get dropped
        if not np.isfinite(windowed_signal).all():
            windowed_signal = windowed_signal.copy()
            windowed_signal[~np.isfinite(windowed_signal)] = np.nan
        
        # ------------- ARTIFACT REMOVAL -------------
        # Reject an epoch if any sample is NaN/Inf (real artefacts from
        # ResetSignalArtefact) or if the entire epoch is exactly zero
        # (all channels, all samples — a completely flat/dead segment).
        nan_epoch_mask = np.isnan(windowed_signal).any(axis=(1, 2))
        zero_epoch_mask = (windowed_signal == 0).all(axis=(1, 2))
        valid_windows = (~nan_epoch_mask) & (~zero_epoch_mask)
        clean_windowed_signal = windowed_signal[valid_windows]

        if DEBUG:
            n_nan = int(np.sum(nan_epoch_mask))
            n_zero_only = int(np.sum(zero_epoch_mask & ~nan_epoch_mask))
            print(f"[AECConnectivity] Epochs: {windowed_signal.shape[0]} | "
                  f"dropped NaN/Inf: {n_nan} | dropped all-zero: {n_zero_only} | "
                  f"kept: {int(np.sum(valid_windows))}")
            if n_nan > 0:
                nan_epochs_per_channel = np.isnan(windowed_signal).any(axis=2).sum(axis=0)
                nan_offenders = [(channel_names[c], int(nan_epochs_per_channel[c]))
                                 for c in np.argsort(nan_epochs_per_channel)[::-1]
                                 if nan_epochs_per_channel[c] > 0]
                print(f"[AECConnectivity] Channels with NaN/Inf samples "
                      f"(channel: #epochs affected): {nan_offenders}")
            if n_zero_only > 0:
                print(f"[AECConnectivity] Rejected {n_zero_only} epoch(s) "
                      f"where all channels and samples were exactly zero.")
            print(f"Shape after artifact removal: {clean_windowed_signal.shape}")

        if clean_windowed_signal.shape[0] == 0:
            raise NodeRuntimeException(self.identifier, "ArtifactRemoval",
                "All epochs were rejected (NaN/Inf/zero). Nothing to compute.")


        info = {
            'sample_rate': fs,
            'channel_names': channel_names,
        }


        # Use the cleaned (NaN-free) epochs for AEC computation.
        try:
            final_aec, average_aec = aec_parallel(
                clean_windowed_signal, info, n_jobs=-1
            )
        except Exception as e:
            raise NodeRuntimeException(self.identifier, "AECComputation",
                f"Error in aec_parallel: {str(e)}")

        return {
            'aec_results': {
                'final_aec': final_aec,
                'average_aec': average_aec,
                'channel_names': info['channel_names']
            }
        }
    




# ---------------------------------------------------------------------
# Define AEC method (Numba-based):
# ---------------------------------------------------------------------


def get_envelope(signal):
    """
    Apply Hilbert transform and extract the amplitude envelope.
    
    The Hilbert transform converts a real signal into an analytic signal,
    whose magnitude represents the instantaneous amplitude envelope.

    Parameters
    ----------
    signal : ndarray, shape (num_channels, num_samples)
        Real-valued time series data.

    Returns
    -------
    envelope : ndarray, shape (num_channels, num_samples)
        Amplitude envelope for each channel.
    """
    analytic = hilbert(signal, axis=1)
    envelope = np.abs(analytic)
    return envelope


def leakage_correct(x, y):
    """
    Reduce signal leakage (volume conduction) between two signals using linear regression.
    
    This method orthogonalizes signal x with respect to signal y by removing the linear
    component of y from x. This helps mitigate spurious connectivity caused by volume
    conduction in EEG.

    Parameters
    ----------
    x : ndarray, shape (num_samples, 1)
        Target signal to be corrected (transposed).
    y : ndarray, shape (num_samples, 1)
        Reference signal (transposed).

    Returns
    -------
    x_corrected : ndarray, shape (num_samples, 1)
        Signal x with the linear influence of y removed.
    """
    beta_leak = np.linalg.pinv(y) @ x
    x_corrected = x - y @ beta_leak
    return x_corrected


def compute_aec(signal):
    """
    Compute Amplitude Envelope Correlation (AEC) between all pairs of channels.
    
    AEC measures connectivity by computing the correlation between amplitude envelopes
    of band-pass filtered signals. This implementation includes leakage correction to
    reduce spurious connectivity from volume conduction.

    Algorithm
    ---------
    1) For each channel pair (i, j):
       a) Apply leakage correction: remove linear influence of channel i from channel j
       b) Compute Hilbert envelopes for both corrected and reference signals
       c) Mean-center the envelopes
       d) Compute Pearson correlation between envelopes
    2) Symmetrize the matrix and set diagonal to 0

    Parameters
    ----------
    signal : ndarray, shape (num_channels, num_samples)
        Real-valued time series for one epoch.

    Returns
    -------
    aec : ndarray, shape (num_channels, num_channels)
        AEC connectivity matrix. Values range approximately [0, 1], where higher values
        indicate stronger amplitude envelope coupling between channel pairs.
    
    Notes
    -----
    - Diagonal elements are set to 0 (no self-connectivity).
    - The matrix is symmetrized: AEC[i,j] = AEC[j,i].
    """
    C, T = signal.shape
    aec = np.zeros((C, C), dtype=np.float64)

    for i in range(C):
        y = signal[i].reshape(1, T)
        for j in range(C):
            if i == j:
                continue

            x = signal[j].reshape(1, T)
            # Apply leakage correction: remove linear influence of y from x
            x_corr = leakage_correct(x.T, y.T).T

            # Compute envelopes for corrected and reference signals
            combined = np.vstack((x_corr, y))
            env = get_envelope(combined)
            # Mean-center envelopes before correlation
            env -= np.mean(env, axis=1, keepdims=True)

            # Compute absolute value of Pearson correlation
            corr = pearsonr(env[0], env[1])[0]
            aec[i, j] = abs(corr)

    # Symmetrize the matrix
    aec = (aec + aec.T) / 2
    np.fill_diagonal(aec, 0.0)

    return aec


def aec_parallel(windowed_signal, info=None, n_jobs=-1):
    """
    Compute AEC for each epoch (window) in parallel using optimized job distribution.

    This function processes multiple epochs in parallel to compute AEC connectivity matrices.
    It uses intelligent parallelization that:
    - Normalizes n_jobs to avoid over-subscription
    - Selects appropriate backend (threading/loky) based on environment
    - Falls back to serial execution when appropriate (single worker or few windows)

    Parameters
    ----------
    windowed_signal : ndarray, shape (num_windows, num_channels, num_samples)
        3D array of windowed EEG data. Should be NaN/Inf/zero-free after artifact removal.
    info : dict, optional
        Metadata such as 'sample_rate' and 'channel_names'. Not actively used in computation,
        kept for consistency with other connectivity modules.
    n_jobs : int, default=-1
        Number of parallel workers. Use -1 for all available cores.

    Returns
    -------
    final_aec : ndarray, shape (num_windows, num_channels, num_channels)
        AEC connectivity matrices for each epoch.
    average_aec : ndarray, shape (num_channels, num_channels)
        Mean AEC matrix averaged across all epochs.
    
    Notes
    -----
    The parallelization strategy matches that of DpliConnectivity and WpliConnectivity
    for consistent performance and stability across connectivity measures.
    """
    num_windows, num_channels, num_samples = windowed_signal.shape

    def process_window(w):
        data_2d = windowed_signal[w]  # shape (channels, time)
        return compute_aec(data_2d)

    # Normalize n_jobs to avoid requesting more workers than windows/CPUs
    effective_n_jobs = normalize_n_jobs(n_jobs, num_windows)

    if effective_n_jobs == 1:
        # Serial execution for single worker
        results = [process_window(w) for w in range(num_windows)]
    else:
        # Parallel execution with intelligent backend selection
        backend = select_joblib_backend()
        parallel_kwargs = {"n_jobs": effective_n_jobs, "backend": backend}
        if backend == "threading":
            parallel_kwargs["prefer"] = "threads"
        
        results = Parallel(**parallel_kwargs)(
            delayed(process_window)(w) for w in range(num_windows)
        )

    final_aec = np.stack(results, axis=0)
    average_aec = np.mean(final_aec, axis=0)

    return final_aec, average_aec