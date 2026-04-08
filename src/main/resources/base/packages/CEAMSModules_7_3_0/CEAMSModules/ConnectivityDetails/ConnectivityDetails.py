# @ Valorisation Recherche HSCM, Societe en Commandite – 2025
# See the file LICENCE for full license details.

"""
ConnectivityDetails
----------------------------------------------------------
- outputs (matrix TSV + heatmap PNG + head-shaped connectivity plot (if montage ≥4 matched channels)
- For now uses MANUAL thresholds by default (standard values below)
- Auto mode is implemented but disabled by default (ready for a future 'mode' input)

Expected con_dict formats:
- New nested:
    {'wpli_results': {'final_wpli', 'average_wpli', 'channel_names'}}
    {'dpli_results': {'final_dpli', 'average_dpli', 'channel_names'}}
- Backward-compatible:
    {'average_wpli', 'channel_names'}  or  {'average_dpli', 'channel_names'}

Optional (future) plot_options (NOT required for now):
    {
      'mode': 'manual' | 'auto',   # default 'manual'
      # dPLI manual:
      'neutral_abs': 0.01, 'moderate_abs': 0.02, 'strong_abs': 0.08, 'max_abs': 0.25,
      # dPLI auto:
      'auto_density': 0.15, 'strong_top_frac': 0.5, 'max_abs': 'auto',
      # wPLI manual:
      'neutral_min': 0.05, 'moderate_min': 0.10, 'strong_min': 0.20, 'max_val': 0.40,
      # wPLI auto:
      'auto_density': 0.15, 'strong_top_frac': 0.5, 'max_val': 'auto',
      # layout:
      'target_radius': 0.49, 'rotate_deg': 0.0, 'shift_x': 0.0, 'shift_y': 0.0,
      # dPLI direction visualization:
      'direction_mode': 'gradient' | 'order'   # default 'gradient'
    }
"""

import os
import re
from matplotlib import ticker
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.cm as cm

import mne
from mne.channels import make_standard_montage, get_builtin_montages
from mne.channels.layout import _find_topomap_coords

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = False

# -------------------------------
# ConnectivityDetails node
# -------------------------------
class ConnectivityDetails(SciNode):
    """
    Node for saving connectivity results (matrix, heatmap, and head plot) to disk.
    Works for wPLI and dPLI results. Head plot is created only if ≥4 channels match a montage.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('ConnectivityDetails.__init__')
        InputPlug('recording_path', self)
        InputPlug('subject_info', self)
        InputPlug('con_dict', self)
        InputPlug('output_path', self)
        self._is_master = False

    def _extract_results(self, con_dict):
        """Return metric ('wpli'|'dpli'), matrix (average), channel_names (list)."""
        if isinstance(con_dict, dict):
            if 'wpli_results' in con_dict:
                r = con_dict['wpli_results']
                return 'wpli', r['average_wpli'], r['channel_names']
            if 'dpli_results' in con_dict:
                r = con_dict['dpli_results']
                return 'dpli', r['average_dpli'], r['channel_names']
        if 'average_wpli' in con_dict:
            return 'wpli', con_dict['average_wpli'], con_dict['channel_names']
        if 'average_dpli' in con_dict:
            return 'dpli', con_dict['average_dpli'], con_dict['channel_names']
        raise NodeInputException(self.identifier, "con_dict",
                                 "No wPLI/dPLI results found (expected 'wpli_results' or 'dpli_results').")

    def compute(self, recording_path, subject_info, con_dict, output_path):
        # --- Basic checks ---
        if not recording_path:
            raise NodeInputException(self.identifier, "recording_path", "Missing recording path.")
        if not subject_info or "filename" not in subject_info:
            raise NodeInputException(self.identifier, "subject_info", "Missing subject_info['filename'].")

        subject_name = subject_info["filename"]
        if output_path:
            out_dir = output_path
        elif os.path.isdir(recording_path):
            out_dir = recording_path
        else:
            out_dir = os.path.dirname(recording_path)

        if DEBUG:
            print("************************************")
            print(f"ConnectivityDetails called for subject: {subject_name}")
            print(f"recording_path: {recording_path}")
            print(f"output_path: {output_path!r}")
            print(f"Saving outputs in: {out_dir}")
            print("************************************")

        # --- Extract connectivity ---
        metric, matrix, channel_names = self._extract_results(con_dict)
        base = f"{subject_name}_{metric}"
        title = f"{metric.upper()} Connectivity"

        tsv_path = os.path.join(out_dir, f"{base}_convalue.tsv")
        img_path = os.path.join(out_dir, f"{base}_conheatmap.png")
        head_path = os.path.join(out_dir, f"{base}_contopomap.png")

        # --- Save matrix as TSV ---
        try:
            df = pd.DataFrame(matrix, index=channel_names, columns=channel_names)
            df.to_csv(tsv_path, sep="\t")
            self._log_manager.log(self.identifier, f"Saved connectivity TSV: {tsv_path}")
        except Exception as e:
            raise NodeRuntimeException(self.identifier, "TSV", f"Failed to save TSV: {str(e)}")

        # --- Save matrix heatmap as PNG ---
        try:
            N = len(channel_names)
            base_w, base_h = 8.0, 6.0
            scale = 1.0 + 0.01 * max(0, N - 64)
            fig_w = min(18.0, base_w * scale)
            fig_h = min(14.0, base_h * scale)

            plt.figure(figsize=(fig_w, fig_h), dpi=200)
            if metric == 'wpli':
                im = plt.imshow(matrix, cmap="jet", aspect="auto", vmin=0.0, vmax=0.3)  # <-- set limits
            elif metric == 'dpli':
                im = plt.imshow(matrix, cmap="jet", aspect="auto", vmin=0.3, vmax=0.7)  # <-- set limits
            cbar = plt.colorbar(im)

            # --- force formatting with 2 decimal places ---
            cbar.ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
            cbar.set_label(title)
            cbar.ax.tick_params(labelsize=6)
            plt.xticks(ticks=np.arange(N), labels=channel_names, rotation=90, fontsize=6)
            plt.yticks(ticks=np.arange(N), labels=channel_names, fontsize=6)
            plt.tick_params(length=0)
            plt.tight_layout()
            plt.savefig(img_path, dpi=200)
            plt.close()
            self._log_manager.log(self.identifier, f"Saved connectivity image: {img_path}")
        except Exception as e:
            raise NodeRuntimeException(self.identifier, "Image", f"Failed to save PNG: {str(e)}")

        # --- NEW: Try to save head plot (manual thresholds by default) ---
        try:
            # 1) Best montage from names (dummy zeros; very fast)
            final_raw, best_montage, matched = find_best_montage_from_names(channel_names, sfreq=1.0)
            if len(matched) < 4:
                if DEBUG:
                    print("[INFO] <4 matched EEG channels -> skipping head plot.")
                return {}

            # 2) Manual standard parameters (current default). Auto code is present but off.
            if metric == 'dpli':
                fig = plot_best_dpli(
                    M=matrix,
                    raw=final_raw,
                    channel_names=channel_names,
                    montage_name=best_montage,
                    # info_channel_names=channel_names,
                    # final_raw=final_raw,
                    # best_montage_name=best_montage,
                    mode='manual',
                    neutral_abs=0.01,
                    moderate_abs=0.02,
                    strong_abs=0.08,
                    max_abs=0.25,
                    target_radius=0.49, rotate_deg=0.0, shift_x=0.0, shift_y=0.0,
                    direction_mode='gradient'  # default behavior
                )
            else:  # 'wpli'
                fig = plot_best_wpli(
                    W=matrix,
                    raw=final_raw,
                    channel_names=channel_names,
                    montage_name=best_montage,
                    # info_channel_names=channel_names,
                    # final_raw=final_raw,
                    # best_montage_name=best_montage,
                    mode='manual',
                    neutral_min=0.05,
                    moderate_min=0.10,
                    strong_min=0.20,
                    max_val=0.40,
                    target_radius=0.49, rotate_deg=0.0, shift_x=0.0, shift_y=0.0,
                )

            fig.savefig(head_path, dpi=300, bbox_inches='tight')
            plt.close(fig)
            self._log_manager.log(self.identifier, f"Saved connectivity head plot: {head_path}")

        except Exception as e:
            # Soft-fail: TSV/heatmap were already saved
            if DEBUG:
                print(f"[WARN] Skipped head plot due to: {e}")

        return {}

# -------------------------------
# Geometry / montage helpers
# -------------------------------
NON_BRAIN_HC_128_129 = [
    'E127', 'E126', 'E17', 'E21', 'E14', 'E25', 'E8', 'E128', 'E125', 'E43',
    'E120', 'E48', 'E119', 'E49', 'E113', 'E81', 'E73', 'E88', 'E68', 'E94',
    'E63', 'E99', 'E56', 'E107'
]

def _kasa_circle(xy: np.ndarray):
    x, y = xy[:, 0], xy[:, 1]
    A = np.c_[2 * x, 2 * y, np.ones_like(x)]
    b = x ** 2 + y ** 2
    xc, yc, c3 = np.linalg.lstsq(A, b, rcond=None)[0]
    R = np.sqrt(max(c3 + xc ** 2 + yc ** 2, 0.0))
    return float(xc), float(yc), float(R)

# def _coords_for_montage(montage_name: str):
#     montage = make_standard_montage(montage_name)
#     names = montage.ch_names
#     info = mne.create_info(names, sfreq=250.0, ch_types="eeg")
#     info.set_montage(montage)
#     picks = np.arange(len(names))
#     xy = _find_topomap_coords(info, picks=picks)
#     return names, xy

def _normalize_xy(xy: np.ndarray, target_radius=0.49, rotate_deg=0.0, shift_x=0.0, shift_y=0.0):
    xc, yc, _ = _kasa_circle(xy)
    xy0 = xy - np.array([xc, yc])
    Rref = float(np.max(np.linalg.norm(xy0, axis=1)))
    scale = target_radius / Rref if Rref > 0 else 1.0
    XY = xy0 * scale
    if rotate_deg:
        th = np.deg2rad(rotate_deg)
        Rm = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
        XY = XY @ Rm.T
    XY = XY + np.array([0.5 + shift_x, 0.5 + shift_y])
    return XY

def _is_hc_128_129(name: str) -> bool:
    m = name.lower().replace('_', '-').replace(' ', '-')
    return ('gsn-hydrocel-128' in m) or ('gsn-hydrocel-129' in m)

# -------------------------------
# Channel renaming (Try1 / Try2) + label mapping
# -------------------------------
def make_ch_map_try1(ch_names):
    ch_map = {}
    for ch in ch_names:
        if "vref" in ch.lower():
            ch_map[ch] = "Cz"
        else:
            ch_map[ch] = re.sub(r"[^0-9a-zA-Z]+", "", ch).replace("EEG", "E")
    return ch_map

def make_ch_map_try2(ch_names):
    ch_map = {
        ch: re.sub(r"[^0-9a-z]+", "",
                   ch.lower().replace("eeg", "").replace("olr", "").replace("cle", ""))
        for ch in ch_names
    }
    for ch in ch_names:
        if "vref" in ch.lower():
            ch_map[ch] = "Cz"
    return ch_map

# def _norm_simple(s: str) -> str:
#     return re.sub(r"[^0-9a-z]+", "", s.lower())

# def _choose_best_label_mapping(info_channel_names, final_raw):
#     """Pick A/B/C mapping that best matches final_raw.ch_names (case/sep-insensitive)."""
#     A = list(info_channel_names)
#     map1 = make_ch_map_try1(info_channel_names); B = [map1.get(ch, ch) for ch in info_channel_names]
#     map2 = make_ch_map_try2(info_channel_names); C = [map2.get(ch, ch) for ch in info_channel_names]
#     final_norm = {_norm_simple(n) for n in final_raw.ch_names}
#     best = ("A", A, -1)
#     for tag, lab in [("A", A), ("B", B), ("C", C)]:
#         overlap = sum(1 for n in lab if _norm_simple(n) in final_norm)
#         if overlap > best[2]:
#             best = (tag, lab, overlap)
#     if DEBUG:
#         print(f"[INFO] label mapping guessed as pass {best[0]} (overlap={best[2]})")
#     return best[1]

# -------------------------------
# Montage scoring & search (from names only; dummy Raw)
# -------------------------------
# def _score_for_montage(raw, montage_name: str) -> float:
#     tmp = raw.copy()
#     montage = make_standard_montage(montage_name)
#     tmp.set_montage(montage, match_alias=True, match_case=False, on_missing='ignore')
#     return 1.1 * len(tmp.info.get('dig') or []) - 0.1 * len(montage.ch_names)





# def find_best_montage_from_names(channel_names, sfreq=1.0):
#     """
#     Build a tiny RawArray with zeros, test passes A/B/C across built-in montages.
#     Return final_raw (winning montage & names), best_montage_name, matched_names.
#     """
#     n_ch = len(channel_names)
#     data = np.zeros((n_ch, 10), dtype=float)  # 10 samples is enough
#     raw_info = mne.create_info(ch_names=list(channel_names), sfreq=float(sfreq), ch_types='eeg')
#     raw_orig = mne.io.RawArray(data, raw_info)

#     ch_map_try1 = make_ch_map_try1(raw_orig.ch_names)
#     ch_map_try2 = make_ch_map_try2(raw_orig.ch_names)

#     best_name, best_score, best_pass = "", -np.inf, "A"
#     # Pass A
#     for item in get_builtin_montages():
#         s = _score_for_montage(raw_orig, item)
#         if s > best_score: best_name, best_score, best_pass = item, s, "A"
#     # Pass B
#     raw_try1 = raw_orig.copy().rename_channels(ch_map_try1)
#     for item in get_builtin_montages():
#         s = _score_for_montage(raw_try1, item)
#         if s > best_score: best_name, best_score, best_pass = item, s, "B"
#     # Pass C
#     raw_try2 = raw_orig.copy().rename_channels(ch_map_try2)
#     for item in get_builtin_montages():
#         s = _score_for_montage(raw_try2, item)
#         if s > best_score: best_name, best_score, best_pass = item, s, "C"

#     # Build final_raw per winning pass
#     if best_pass == "A":
#         final_raw = raw_orig.copy()
#     elif best_pass == "B":
#         final_raw = raw_orig.copy().rename_channels(ch_map_try1)
#     else:
#         final_raw = raw_orig.copy().rename_channels(ch_map_try2)

#     final_montage = make_standard_montage(best_name)
#     final_raw.set_montage(montage=final_montage, match_alias=True, match_case=False, on_missing='ignore')

#     # Matched channels (with non-zero positions)
#     matched = []
#     for idx, ch in enumerate(final_raw.info['chs']):
#         if ch['kind'] == mne.io.constants.FIFF.FIFFV_EEG_CH and not np.allclose(ch['loc'][:3], 0):
#             matched.append(final_raw.info['ch_names'][idx])

#     if DEBUG:
#         print(f"[INFO] Best montage: {best_name} (pass {best_pass}) score={best_score:.2f}")
#         print(f"[INFO] Matched: {len(matched)}")
#     return final_raw, best_name, matched


def find_best_montage_from_names(channel_names, sfreq=1.0):
    """
    1. Finds the best montage/renaming strategy.
    2. Applies the montage.
    3. Renames channels BACK to original names.
    
    Returns:
        final_raw: Raw object with ORIGINAL names but with montage positions loaded.
        best_montage_name: The name of the montage used.
        matched_channels: List of ORIGINAL channel names that have coordinates.
    """
    
    # --- 1. Define Scenarios (Same as before) ---
    map_A = {ch: ch for ch in channel_names}
    map_B = make_ch_map_try1(channel_names)
    map_C = make_ch_map_try2(channel_names)
    variants = [('A', map_A), ('B', map_B), ('C', map_C)]

    best_score = (1, float('inf')) 
    best_montage_name = None
    best_variant_map = None 

    base_info = mne.create_info(channel_names, sfreq, ch_types='eeg')

    for _, current_map in variants:

        info = base_info.copy()
        info.rename_channels(current_map)

        for m_name in get_builtin_montages():

            montage = make_standard_montage(m_name)
            m_size = len(montage.ch_names)
            
            tmp_info = info.copy()
            tmp_info.set_montage(montage, match_alias=True, match_case=False, on_missing='ignore')
            matches = 0

            for ch in tmp_info['chs']:
                if not np.isnan(ch['loc'][:3]).any():
                        matches += 1

            if matches > best_score[0]:
                best_score = (matches, m_size)
                best_montage_name = m_name
                best_variant_map = current_map
            elif matches == best_score[0]:
                if m_size < best_score[1]:
                    best_score = (matches, m_size)
                    best_montage_name = m_name
                    best_variant_map = current_map

    if best_montage_name is None:
        if DEBUG:
            print("[WARN] No matching montage found.")
        return None, None, []

    # --- 3. Apply Logic (The "Sandwich") ---
    
    # A. Create Raw with ORIGINAL names
    info = mne.create_info(channel_names, sfreq, ch_types='eeg')
    data = np.zeros((len(channel_names), 10))
    raw = mne.io.RawArray(data, info)
    
    # B. Rename to Standard (Forward Map)
    #    e.g. { "EEG 001": "E1" }
    raw.rename_channels(best_variant_map)
    
    # C. Apply Montage
    #    Now "E1" gets coordinates.
    montage = make_standard_montage(best_montage_name)
    raw.set_montage(montage, match_alias=True, match_case=False, on_missing='ignore')
    
    # D. Rename BACK to Original (Inverse Map)
    #    Create inverse: { "E1": "EEG 001" }
    #    Note: We only invert keys that were actually used in the map.
    inv_map = {v: k for k, v in best_variant_map.items()}
    
    try:
        raw.rename_channels(inv_map)
    except ValueError as e:
        # This happens if two original channels mapped to the same new name (rare collision)
        if DEBUG:
            print(f"[WARN] Could not rename back fully due to collision: {e}")

    # E. Verify matches using ORIGINAL names
    #    We check which channels have non-zero locations in the 'chs' list
    matched = []
    for ch in raw.info['chs']:
        # If the first 3 values of 'loc' are not all zero, it has a position
        if not np.allclose(ch['loc'][:3], 0):
            matched.append(ch['ch_name'])
    if DEBUG:        
        print(f"Montage '{best_montage_name}' applied. {len(matched)} channels matched.")
    return raw, best_montage_name, matched



# def _get_coords_from_raw(raw):
#     """
#     Extracts 2D (x,y) plotting coordinates from a Raw object 
#     that already has a montage applied.
#     Returns: dictionary {channel_name: [x, y]}
#     """
#     # This public function projects 3D 'loc' to 2D
#     layout = mne.channels.find_layout(raw.info)
    
#     # Create a lookup dict for easy access
#     # layout.names contains the channel names
#     # layout.pos contains [x, y, width, height] -> we want x,y
#     coords_map = {}
#     for name, pos in zip(layout.names, layout.pos):
#         coords_map[name] = pos[:2]
        
#     return coords_map



# -------------------------------
# dPLI plotting (manual + auto ready; NO title)
# -------------------------------
def plot_dpli_generic(
    M, raw, channel_names, montage_name,
    mode: str = 'manual',
    # Manual-threshold defaults:
    neutral_abs: float = 0.01,
    moderate_abs: float = 0.02,
    strong_abs: float = 0.08,
    max_abs=0.25,
    # Auto mode knobs (not used unless mode='auto'):
    auto_density: float = 0.15,
    strong_top_frac: float = 0.5,
    # Layout:
    target_radius: float = 0.49, rotate_deg: float = 0.0, shift_x: float = 0.0, shift_y: float = 0.0,
    figsize=(8,8), dpi=300,
    # Direction visualization:
    direction_mode: str = 'gradient'   # 'gradient' (default) or 'order'
):
    # montage coords (exclude HydroCel non-brain)
    # m_names, m_xy = _coords_for_montage(montage_name)

    # 1. Get valid coordinates from the Raw object
    # coords_map = _get_coords_from_raw(raw)
    m_xy = _find_topomap_coords(raw.info, picks=raw.ch_names)
    m_names = channel_names

    keep_idx = list(range(len(m_names)))
    if _is_hc_128_129(montage_name):
        exclude = set(NON_BRAIN_HC_128_129)
        keep_idx = [i for i, n in enumerate(m_names) if n not in exclude]
    m_names = [m_names[i] for i in keep_idx]; m_xy = m_xy[keep_idx]

    def _norm(s): return re.sub(r"[^0-9a-z]+", "", s.lower())
    label_norm_to_idx = {_norm(n): i for i, n in enumerate(channel_names)}

    pairs = []
    for i_m, nm in enumerate(m_names):
        k = _norm(nm)
        if k in label_norm_to_idx:
            pairs.append((i_m, label_norm_to_idx[k]))
    if len(pairs) < 2:
        raise RuntimeError("Not enough overlapping channels to plot dPLI.")

    idx_m, idx_l = zip(*pairs); idx_m, idx_l = list(idx_m), list(idx_l)
    D = np.asarray(M, float)[np.ix_(idx_l, idx_l)]
    np.fill_diagonal(D, 0.5)

    XY_all = _normalize_xy(m_xy, target_radius, rotate_deg, shift_x, shift_y)
    XYp = np.stack([XY_all[i_m] for i_m in idx_m], axis=0)
    present_names = [m_names[i] for i in idx_m]

    # candidate edges (use upper triangle only)
    cand = []
    for a in range(len(idx_l)):
        for b in range(a + 1, len(idx_l)):
            bias = float(D[a, b]) - 0.5
            cand.append((a, b, bias, abs(bias)))

    edges_strong, edges_mod = [], []
    if mode == 'auto':
        n_pairs = len(cand)
        if n_pairs == 0: raise RuntimeError("No pairs for auto-density.")
        keep_n = max(1, int(round(float(auto_density) * n_pairs)))
        kept = sorted(cand, key=lambda x: x[3], reverse=True)[:keep_n]
        cut = max(1, int(round((1.0 - float(strong_top_frac)) * len(kept))))
        thin, thick = kept[:cut], kept[cut:]
        if isinstance(max_abs, str) and max_abs.lower() == 'auto':
            abs_vals = np.array([ab for *_, ab in kept], float)
            max_abs = float(np.percentile(abs_vals, 95)) or 0.01
        for a,b,bias,_ in thin:  edges_mod.append((a,b,bias))
        for a,b,bias,_ in thick: edges_strong.append((a,b,bias))
    else:
        for a,b,bias,ab in cand:
            if ab < neutral_abs: continue
            if ab >= strong_abs: edges_strong.append((a,b,bias))
            elif ab >= moderate_abs: edges_mod.append((a,b,bias))

    connected = set()
    for i,j,_ in edges_mod + edges_strong: connected.add(i); connected.add(j)

    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
    # leave some bottom margin for 'order' mode text
    if direction_mode == 'order':
        fig.subplots_adjust(bottom=0.22)
    ax.add_artist(plt.Circle((0.5,0.5), target_radius, edgecolor='gray', facecolor='none', lw=2.5, zorder=0))

    # Custom diverging map: blue (lags) -> purple (neutral) -> red (leads)
    cmap = LinearSegmentedColormap.from_list(
        "leadlag_purple_mid",
        [
            (0.00, (0.10, 0.25, 0.80)),  # blue-ish for negative bias
            (0.50, (0.50, 0.00, 0.50)),  # purple at zero
            (1.00, (0.85, 0.20, 0.20)),  # red-ish for positive bias
        ],
        N=256,
    )

    max_abs_val = float(max_abs) if isinstance(max_abs,(int,float)) else 0.25
    norm = plt.Normalize(vmin=-max_abs_val, vmax=+max_abs_val)

    # ---- helpers for solid edges ----
    def add_group(recs, lw, alpha_base):
        if not recs: return None
        segs, cols, lws = [], [], []
        for (a,b,bias) in recs:
            p1, p2 = XYp[a], XYp[b]
            col = cmap(norm(bias))
            alpha = alpha_base + (min(abs(bias), max_abs_val) / max_abs_val) * (1.0 - alpha_base)
            segs.append((p1,p2)); cols.append((col[0], col[1], col[2], alpha)); lws.append(lw)
        lc = LineCollection(
            segs, colors=cols, linewidths=lws,
            zorder=1.2 if lw <= 2 else 1.6,  # moderates behind, strong above
            capstyle='butt', joinstyle='miter', antialiased=True
        )
        ax.add_collection(lc); return lc

    # ---- helper for gradient edges (red/blue with PURPLE center) ----
    def _draw_gradient_edges(ax, XYp, recs, *,
                             lw=3.6, alpha_base=0.90,
                             nseg=16, eps_frac=1e-3,
                             max_abs_val=0.25):
        if not recs: return None
        segs, cols, lws = [], [], []
        purple = np.array([0.60, 0.00, 0.60])  # mid color

        for (a, b, bias) in recs:
            p1 = XYp[a]; p2 = XYp[b]
            dx = float(p2[0] - p1[0]); dy = float(p2[1] - p1[1])
            L = (dx*dx + dy*dy) ** 0.5
            if L <= 1e-9: continue
            ux, uy = dx / L, dy / L

            if bias >= 0:
                c_leader = np.array([1.0, 0.0, 0.0])  # leader red
                c_lagger = np.array([0.0, 0.0, 1.0])  # lagger blue
            else:
                c_leader = np.array([0.0, 0.0, 1.0])  # leader blue
                c_lagger = np.array([1.0, 0.0, 0.0])  # lagger red

            alpha = alpha_base + (min(abs(bias), max_abs_val) / max_abs_val) * (1.0 - alpha_base)

            ts = np.linspace(0.0, 1.0, nseg + 1)
            eps = eps_frac  # tiny overlap to avoid gaps/dots

            for i in range(nseg):
                t0 = max(0.0, ts[i]   - eps)
                t1 = min(1.0, ts[i+1] + eps)

                x0 = p1[0] + ux * (t0 * L); y0 = p1[1] + uy * (t0 * L)
                x1 = p1[0] + ux * (t1 * L); y1 = p1[1] + uy * (t1 * L)
                segs.append([(x0, y0), (x1, y1)])

                # piecewise: leader -> PURPLE up to mid, then PURPLE -> lagger
                tm = 0.5 * (t0 + t1)
                if tm <= 0.5:
                    t_blend = tm * 2.0
                    rgb = (1.0 - t_blend) * c_leader + t_blend * purple
                else:
                    t_blend = (tm - 0.5) * 2.0
                    rgb = (1.0 - t_blend) * purple + t_blend * c_lagger

                cols.append((rgb[0], rgb[1], rgb[2], alpha))
                lws.append(lw)

        lc = LineCollection(
            segs, colors=cols, linewidths=lws,
            zorder=1.6 if lw >= 3 else 1.2,
            capstyle='butt', joinstyle='miter', antialiased=True
        )
        ax.add_collection(lc)
        return lc

    # draw edges
    if direction_mode == 'gradient':
        # Moderates: faint & thin; Strong: bold & more segments. Thresholds unchanged.
        lc_mod = _draw_gradient_edges(ax, XYp, edges_mod,
                                      lw=1.2, alpha_base=0.08, nseg=8,  max_abs_val=max_abs_val)
        lc_str = _draw_gradient_edges(ax, XYp, edges_strong,
                                      lw=3.6, alpha_base=0.92, nseg=18, max_abs_val=max_abs_val)
    else:  # 'order' mode: solid diverging colors; add channel-order line below
        lc_mod = add_group(edges_mod,   lw=1.2, alpha_base=0.08)
        lc_str = add_group(edges_strong, lw=3.6, alpha_base=0.92)

    # nodes & labels
    all_idx = list(range(len(present_names)))
    unconnected = [i for i in all_idx if i not in connected]
    if unconnected:
        ax.scatter(XYp[unconnected,0], XYp[unconnected,1], s=70, facecolor='white',
                   edgecolor='black', linewidth=1.0, zorder=2.0)
    if connected:
        conn = sorted(list(connected))
        ax.scatter(XYp[conn,0], XYp[conn,1], s=74, facecolor='black',
                   edgecolor='white', linewidth=1.0, zorder=2.2)
    for i,name in enumerate(present_names):
        x,y = XYp[i]
        if i in connected:
            ax.text(x,y+0.014, name, fontsize=7.5, fontweight='bold', ha='center', va='center')
        else:
            ax.text(x,y+0.014, name, fontsize=7.0, ha='center', va='center')

    # --- dPLI colorbar: direction-only (sign), strength shown by width/opacity ---
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm); sm.set_array([])
    ticks = [-max_abs_val, +max_abs_val]  # only the ends
    cbar = plt.colorbar(sm, ax=ax, fraction=0.03, pad=0.02, ticks=ticks)
    cbar.set_label("dPLI direction (sign only); strength = line width/opacity", fontsize=8)
    # vertical by default; if you switch to horizontal later, use set_xticklabels
    cbar.ax.set_yticklabels(["lags (−)", "leads (+)"])
    cbar.ax.minorticks_off()
    cbar.ax.tick_params(labelsize=6)

    # legend
    handles = [Patch(facecolor='white', edgecolor='black', label='present, unconnected'),
               Patch(facecolor='black', edgecolor='white', label='present, connected')]
    if mode == 'auto':
        if lc_mod is not None: handles.append(Line2D([0],[0], color='k', lw=1.2, alpha=0.7, label="kept (thin)"))
        if lc_str is not None: handles.append(Line2D([0],[0], color='k', lw=3.6, alpha=1.0, label="top kept (thick)"))
    else:
        if lc_mod is not None: handles.append(Line2D([0],[0], color='k', lw=1.2, alpha=0.7, label=f"moderate ≥ {moderate_abs:.2f}"))
        if lc_str is not None: handles.append(Line2D([0],[0], color='k', lw=3.6, alpha=1.0, label=f"strong ≥ {strong_abs:.2f}"))

    if direction_mode == 'gradient':
        handles.append(Line2D([0],[0], color='none', label="Edges fade: leader (red) → lagger (blue)"))

    ax.legend(handles=handles, loc='upper right', bbox_to_anchor=(1.15,1.15), fontsize=7, frameon=True)

    # bottom channel order line for 'order' mode
    if direction_mode == 'order':
        order_labels = [channel_names[i] for i in idx_l]
        fig.text(0.5, 0.03,
                 "Row/Column channel order (left→right): " + ", ".join(order_labels),
                 ha='center', va='center', fontsize=7)

    return fig

def plot_best_dpli(M, raw, channel_names, montage_name, **kwargs):
    # labels_for_plot = _choose_best_label_mapping(info_channel_names, final_raw)
    return plot_dpli_generic(M=M, raw=raw, channel_names=channel_names, montage_name=montage_name, **kwargs)

# -------------------------------
# wPLI plotting (manual + auto ready; NO title)
# -------------------------------
def plot_wpli_generic(
    W, raw, channel_names, montage_name,
    mode: str = 'manual',
    # Manual thresholds:
    neutral_min: float = 0.05,
    moderate_min: float = 0.10,
    strong_min: float = 0.20,
    max_val=0.40,
    # Auto mode (not used unless mode='auto'):
    auto_density: float = 0.15, strong_top_frac: float = 0.5,
    # Layout:
    target_radius: float = 0.49, rotate_deg: float = 0.0, shift_x: float = 0.0, shift_y: float = 0.0,
    figsize=(8,8), dpi=300
):
    # m_names, m_xy = _coords_for_montage(montage_name)
    m_xy = _find_topomap_coords(raw.info, picks=raw.ch_names)
    m_names = channel_names
    # coords_map = _get_coords_from_raw(raw)

    keep_idx = list(range(len(m_names)))
    if _is_hc_128_129(montage_name):
        exclude = set(NON_BRAIN_HC_128_129)
        keep_idx = [i for i, n in enumerate(m_names) if n not in exclude]
    m_names = [m_names[i] for i in keep_idx]; m_xy = m_xy[keep_idx]

    def _norm(s): return re.sub(r"[^0-9a-z]+", "", s.lower())
    label_norm_to_idx = {_norm(n): i for i, n in enumerate(channel_names)}

    pairs = []
    for i_m, nm in enumerate(m_names):
        k = _norm(nm)
        if k in label_norm_to_idx: pairs.append((i_m, label_norm_to_idx[k]))
    if len(pairs) < 2:
        raise RuntimeError("Not enough overlapping channels to plot wPLI.")

    idx_m, idx_l = zip(*pairs); idx_m, idx_l = list(idx_m), list(idx_l)

    W = np.asarray(W, float)
    Wsub = W[np.ix_(idx_l, idx_l)]
    np.fill_diagonal(Wsub, 0.0)

    XY_all = _normalize_xy(m_xy, target_radius, rotate_deg, shift_x, shift_y)
    XYp = np.stack([XY_all[i_m] for i_m in idx_m], axis=0)
    present_names = [m_names[i] for i in idx_m]

    cand = []
    nC = len(idx_l)
    for a in range(nC):
        for b in range(a + 1, nC):
            cand.append((a, b, float(Wsub[a, b])))

    edges_thin, edges_thick = [], []
    if mode == 'auto':
        n_pairs = len(cand)
        if n_pairs == 0: raise RuntimeError("No pairs for auto-density (wPLI).")
        keep_n = max(1, int(round(float(auto_density) * n_pairs)))
        kept = sorted(cand, key=lambda x: x[2], reverse=True)[:keep_n]
        cut = max(1, int(round((1.0 - float(strong_top_frac)) * len(kept))))
        thin, thick = kept[:cut], kept[cut:]
        if isinstance(max_val, str) and max_val.lower() == 'auto':
            vals = np.array([w for *_, w in kept], float)
            max_val = float(np.percentile(vals, 95)) or 0.05
        for a,b,w in thin:  edges_thin.append((a,b,w))
        for a,b,w in thick: edges_thick.append((a,b,w))
    else:
        for a,b,w in cand:
            if w < neutral_min: continue
            if w >= strong_min: edges_thick.append((a,b,w))
            elif w >= moderate_min: edges_thin.append((a,b,w))

    connected = set()
    for i,j,_ in edges_thin + edges_thick: connected.add(i); connected.add(j)

    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
    ax.add_artist(plt.Circle((0.5,0.5), target_radius, edgecolor='gray', facecolor='none', lw=2.5, zorder=0))

    # Use reversed magma so darker = stronger (more perceptible)
    cmap = cm.get_cmap('magma_r')
    max_val_f = float(max_val) if isinstance(max_val,(int,float)) else 0.40
    norm = plt.Normalize(vmin=0.0, vmax=max_val_f)

    def add_group(recs, lw, alpha_base):
        if not recs: return None
        segs, cols, lws = [], [], []
        for (a,b,w) in recs:
            p1, p2 = XYp[a], XYp[b]
            col = cmap(norm(w))
            alpha = alpha_base + (min(w, max_val_f) / max_val_f) * (1.0 - alpha_base)
            segs.append((p1,p2)); cols.append((col[0], col[1], col[2], alpha)); lws.append(lw)
        lc = LineCollection(
            segs, colors=cols, linewidths=lws,
            zorder=1.2 if lw <= 2 else 1.6,
            capstyle='butt', joinstyle='miter', antialiased=True
        )
        ax.add_collection(lc); return lc

    # moderates faint/thin; strong bold (thresholds unchanged)
    lc_mod = add_group(edges_thin, 1.2, 0.08)
    lc_str = add_group(edges_thick, 3.6, 0.92)

    all_idx = list(range(len(present_names)))
    unconnected = [i for i in all_idx if i not in connected]
    if unconnected:
        ax.scatter(XYp[unconnected,0], XYp[unconnected,1], s=70, facecolor='white', edgecolor='black', linewidth=1.0, zorder=2.0)
    if connected:
        conn = sorted(list(connected))
        ax.scatter(XYp[conn,0], XYp[conn,1], s=74, facecolor='black', edgecolor='white', linewidth=1.0, zorder=2.2)
    for i,name in enumerate(present_names):
        x,y = XYp[i]
        if i in connected:
            ax.text(x,y+0.014, name, fontsize=7.5, fontweight='bold', ha='center', va='center')
        else:
            ax.text(x,y+0.014, name, fontsize=7.0, ha='center', va='center')

    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm); sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, fraction=0.03, pad=0.02)
    cbar.set_label("wPLI strength (0–1)", fontsize=8)
    cbar.ax.tick_params(labelsize=6)

    # legend (no direction note for wPLI)
    handles = [Patch(facecolor='white', edgecolor='black', label='present, unconnected'),
               Patch(facecolor='black', edgecolor='white', label='present, connected')]
    if mode == 'auto':
        if lc_mod is not None: handles.append(Line2D([0],[0], color='k', lw=1.2, alpha=0.7, label="kept (thin)"))
        if lc_str is not None: handles.append(Line2D([0],[0], color='k', lw=3.6, alpha=1.0, label="top kept (thick)"))
    else:
        if lc_mod is not None: handles.append(Line2D([0],[0], color='k', lw=1.2, alpha=0.7, label=f"moderate ≥ {moderate_min:.2f}"))
        if lc_str is not None: handles.append(Line2D([0],[0], color='k', lw=3.6, alpha=1.0, label=f"strong ≥ {strong_min:.2f}"))

    ax.legend(handles=handles, loc='upper right', bbox_to_anchor=(1.15,1.15), fontsize=7, frameon=True)
    return fig

def plot_best_wpli(W, raw, channel_names, montage_name, **kwargs):
    # labels_for_plot = _choose_best_label_mapping(info_channel_names, final_raw)
    return plot_wpli_generic(W=W, raw=raw, channel_names=channel_names, montage_name=montage_name, **kwargs)









# # @ Valorisation Recherche HSCM, Societe en Commandite – 2025
# # See the file LICENCE for full license details.

# """
# ConnectivityDetails
# ----------------------------------------------------------
# - outputs (matrix TSV + heatmap PNG + head-shaped connectivity plot (if montage ≥4 matched channels)
# - For now uses MANUAL thresholds by default (standard values below)
# - Auto mode is implemented but disabled by default (ready for a future 'mode' input)

# Expected con_dict formats:
# - New nested:
#     {'wpli_results': {'final_wpli', 'average_wpli', 'channel_names'}}
#     {'dpli_results': {'final_dpli', 'average_dpli', 'channel_names'}}
# - Backward-compatible:
#     {'average_wpli', 'channel_names'}  or  {'average_dpli', 'channel_names'}

# Optional (future) plot_options (NOT required for now):
#     {
#       'mode': 'manual' | 'auto',   # default 'manual'
#       # dPLI manual:
#       'neutral_abs': 0.01, 'moderate_abs': 0.02, 'strong_abs': 0.08, 'max_abs': 0.25,
#       # dPLI auto:
#       'auto_density': 0.15, 'strong_top_frac': 0.5, 'max_abs': 'auto',
#       # wPLI manual:
#       'neutral_min': 0.05, 'moderate_min': 0.10, 'strong_min': 0.20, 'max_val': 0.40,
#       # wPLI auto:
#       'auto_density': 0.15, 'strong_top_frac': 0.5, 'max_val': 'auto',
#       # layout:
#       'target_radius': 0.49, 'rotate_deg': 0.0, 'shift_x': 0.0, 'shift_y': 0.0,
#       # dPLI direction visualization:
#       'direction_mode': 'gradient' | 'order'   # default 'gradient'
#     }
# """

# import os
# import re
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.patches import Patch
# from matplotlib.lines import Line2D
# from matplotlib.collections import LineCollection
# from matplotlib.colors import LinearSegmentedColormap
# import matplotlib.cm as cm

# import mne
# from mne.channels import make_standard_montage, get_builtin_montages
# from mne.channels.layout import _find_topomap_coords

# from flowpipe import SciNode, InputPlug, OutputPlug
# from commons.NodeInputException import NodeInputException
# from commons.NodeRuntimeException import NodeRuntimeException

# DEBUG = False

# # -------------------------------
# # ConnectivityDetails node
# # -------------------------------
# class ConnectivityDetails(SciNode):
#     """
#     Node for saving connectivity results (matrix, heatmap, and head plot) to disk.
#     Works for wPLI and dPLI results. Head plot is created only if ≥4 channels match a montage.
#     """
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         if DEBUG: print('ConnectivityDetails.__init__')
#         InputPlug('recording_path', self)
#         InputPlug('subject_info', self)
#         InputPlug('con_dict', self)
#         InputPlug('output_path', self)
#         self._is_master = False

#     def _extract_results(self, con_dict):
#         """Return metric ('wpli'|'dpli'), matrix (average), channel_names (list)."""
#         if isinstance(con_dict, dict):
#             if 'wpli_results' in con_dict:
#                 r = con_dict['wpli_results']
#                 return 'wpli', r['average_wpli'], r['channel_names']
#             if 'dpli_results' in con_dict:
#                 r = con_dict['dpli_results']
#                 return 'dpli', r['average_dpli'], r['channel_names']
#         if 'average_wpli' in con_dict:
#             return 'wpli', con_dict['average_wpli'], con_dict['channel_names']
#         if 'average_dpli' in con_dict:
#             return 'dpli', con_dict['average_dpli'], con_dict['channel_names']
#         raise NodeInputException(self.identifier, "con_dict",
#                                  "No wPLI/dPLI results found (expected 'wpli_results' or 'dpli_results').")

#     def compute(self, recording_path, subject_info, con_dict, output_path):
#         # --- Basic checks ---
#         if not recording_path:
#             raise NodeInputException(self.identifier, "recording_path", "Missing recording path.")
#         if not subject_info or "filename" not in subject_info:
#             raise NodeInputException(self.identifier, "subject_info", "Missing subject_info['filename'].")

#         subject_name = subject_info["filename"]
#         if output_path:
#             out_dir = output_path
#         elif os.path.isdir(recording_path):
#             out_dir = recording_path
#         else:
#             out_dir = os.path.dirname(recording_path)

#         print("************************************")
#         print(f"ConnectivityDetails called for subject: {subject_name}")
#         print(f"recording_path: {recording_path}")
#         print(f"output_path: {output_path!r}")
#         print(f"Saving outputs in: {out_dir}")
#         print("************************************")

#         # --- Extract connectivity ---
#         metric, matrix, channel_names = self._extract_results(con_dict)
#         base = f"{subject_name}_{metric}"
#         title = f"{metric.upper()} Connectivity"

#         tsv_path = os.path.join(out_dir, f"{base}_convalue.tsv")
#         img_path = os.path.join(out_dir, f"{base}_conheatmap.png")
#         head_path = os.path.join(out_dir, f"{base}_contopomap.png")

#         # --- Save matrix as TSV ---
#         try:
#             df = pd.DataFrame(matrix, index=channel_names, columns=channel_names)
#             df.to_csv(tsv_path, sep="\t")
#             self._log_manager.log(self.identifier, f"Saved connectivity TSV: {tsv_path}")
#         except Exception as e:
#             raise NodeRuntimeException(self.identifier, "TSV", f"Failed to save TSV: {str(e)}")

#         # --- Save matrix heatmap as PNG ---
#         try:
#             N = len(channel_names)
#             base_w, base_h = 8.0, 6.0
#             scale = 1.0 + 0.01 * max(0, N - 64)
#             fig_w = min(18.0, base_w * scale)
#             fig_h = min(14.0, base_h * scale)

#             plt.figure(figsize=(fig_w, fig_h), dpi=200)
#             im = plt.imshow(matrix, cmap="jet", aspect="auto")
#             cbar = plt.colorbar(im)
#             cbar.set_label(title)
#             cbar.ax.tick_params(labelsize=6)
#             plt.xticks(ticks=np.arange(N), labels=channel_names, rotation=90, fontsize=6)
#             plt.yticks(ticks=np.arange(N), labels=channel_names, fontsize=6)
#             plt.tick_params(length=0)
#             plt.tight_layout()
#             plt.savefig(img_path, dpi=200)
#             plt.close()
#             self._log_manager.log(self.identifier, f"Saved connectivity image: {img_path}")
#         except Exception as e:
#             raise NodeRuntimeException(self.identifier, "Image", f"Failed to save PNG: {str(e)}")

#         # --- NEW: Try to save head plot (manual thresholds by default) ---
#         try:
#             # 1) Best montage from names (dummy zeros; very fast)
#             final_raw, best_montage, matched = find_best_montage_from_names(channel_names, sfreq=1.0)
#             if len(matched) < 4:
#                 print("[INFO] <4 matched EEG channels -> skipping head plot.")
#                 return {}

#             # 2) Manual standard parameters (current default). Auto code is present but off.
#             if metric == 'dpli':
#                 fig = plot_best_dpli(
#                     M=matrix,
#                     info_channel_names=channel_names,
#                     final_raw=final_raw,
#                     best_montage_name=best_montage,
#                     mode='manual',
#                     neutral_abs=0.01,
#                     moderate_abs=0.02,
#                     strong_abs=0.08,
#                     max_abs=0.25,
#                     target_radius=0.49, rotate_deg=0.0, shift_x=0.0, shift_y=0.0,
#                     direction_mode='gradient'  # default behavior
#                 )
#             else:  # 'wpli'
#                 fig = plot_best_wpli(
#                     W=matrix,
#                     info_channel_names=channel_names,
#                     final_raw=final_raw,
#                     best_montage_name=best_montage,
#                     mode='manual',
#                     neutral_min=0.05,
#                     moderate_min=0.10,
#                     strong_min=0.20,
#                     max_val=0.40,
#                     target_radius=0.49, rotate_deg=0.0, shift_x=0.0, shift_y=0.0,
#                 )

#             fig.savefig(head_path, dpi=300, bbox_inches='tight')
#             plt.close(fig)
#             self._log_manager.log(self.identifier, f"Saved connectivity head plot: {head_path}")

#         except Exception as e:
#             # Soft-fail: TSV/heatmap were already saved
#             print(f"[WARN] Skipped head plot due to: {e}")

#         return {}

# # -------------------------------
# # Geometry / montage helpers
# # -------------------------------
# NON_BRAIN_HC_128_129 = [
#     'E127', 'E126', 'E17', 'E21', 'E14', 'E25', 'E8', 'E128', 'E125', 'E43',
#     'E120', 'E48', 'E119', 'E49', 'E113', 'E81', 'E73', 'E88', 'E68', 'E94',
#     'E63', 'E99', 'E56', 'E107'
# ]

# def _kasa_circle(xy: np.ndarray):
#     x, y = xy[:, 0], xy[:, 1]
#     A = np.c_[2 * x, 2 * y, np.ones_like(x)]
#     b = x ** 2 + y ** 2
#     xc, yc, c3 = np.linalg.lstsq(A, b, rcond=None)[0]
#     R = np.sqrt(max(c3 + xc ** 2 + yc ** 2, 0.0))
#     return float(xc), float(yc), float(R)

# def _coords_for_montage(montage_name: str):
#     montage = make_standard_montage(montage_name)
#     names = montage.ch_names
#     info = mne.create_info(names, sfreq=250.0, ch_types="eeg")
#     info.set_montage(montage)
#     picks = np.arange(len(names))
#     xy = _find_topomap_coords(info, picks=picks)
#     return names, xy

# def _normalize_xy(xy: np.ndarray, target_radius=0.49, rotate_deg=0.0, shift_x=0.0, shift_y=0.0):
#     xc, yc, _ = _kasa_circle(xy)
#     xy0 = xy - np.array([xc, yc])
#     Rref = float(np.max(np.linalg.norm(xy0, axis=1)))
#     scale = target_radius / Rref if Rref > 0 else 1.0
#     XY = xy0 * scale
#     if rotate_deg:
#         th = np.deg2rad(rotate_deg)
#         Rm = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
#         XY = XY @ Rm.T
#     XY = XY + np.array([0.5 + shift_x, 0.5 + shift_y])
#     return XY

# def _is_hc_128_129(name: str) -> bool:
#     m = name.lower().replace('_', '-').replace(' ', '-')
#     return ('gsn-hydrocel-128' in m) or ('gsn-hydrocel-129' in m)

# # -------------------------------
# # Channel renaming (Try1 / Try2) + label mapping
# # -------------------------------
# def make_ch_map_try1(ch_names):
#     ch_map = {}
#     for ch in ch_names:
#         if "vref" in ch.lower():
#             ch_map[ch] = "Cz"
#         else:
#             ch_map[ch] = ch.replace("EEG ", "E")
#     return ch_map

# def make_ch_map_try2(ch_names):
#     ch_map = {
#         ch: re.sub(r"[^0-9a-z]+", "",
#                    ch.lower().replace("eeg", "").replace("olr", "").replace("cle", ""))
#         for ch in ch_names
#     }
#     for ch in ch_names:
#         if "vref" in ch.lower():
#             ch_map[ch] = "Cz"
#     return ch_map

# def _norm_simple(s: str) -> str:
#     return re.sub(r"[^0-9a-z]+", "", s.lower())

# def _choose_best_label_mapping(info_channel_names, final_raw):
#     """Pick A/B/C mapping that best matches final_raw.ch_names (case/sep-insensitive)."""
#     A = list(info_channel_names)
#     map1 = make_ch_map_try1(info_channel_names); B = [map1.get(ch, ch) for ch in info_channel_names]
#     map2 = make_ch_map_try2(info_channel_names); C = [map2.get(ch, ch) for ch in info_channel_names]
#     final_norm = {_norm_simple(n) for n in final_raw.ch_names}
#     best = ("A", A, -1)
#     for tag, lab in [("A", A), ("B", B), ("C", C)]:
#         overlap = sum(1 for n in lab if _norm_simple(n) in final_norm)
#         if overlap > best[2]:
#             best = (tag, lab, overlap)
#     if DEBUG:
#         print(f"[INFO] label mapping guessed as pass {best[0]} (overlap={best[2]})")
#     return best[1]

# # -------------------------------
# # Montage scoring & search (from names only; dummy Raw)
# # -------------------------------
# def _score_for_montage(raw, montage_name: str) -> float:
#     tmp = raw.copy()
#     montage = make_standard_montage(montage_name)
#     tmp.set_montage(montage, match_alias=True, match_case=False, on_missing='ignore')
#     return 1.1 * len(tmp.info.get('dig') or []) - 0.1 * len(montage.ch_names)

# def find_best_montage_from_names(channel_names, sfreq=1.0):
#     """
#     Build a tiny RawArray with zeros, test passes A/B/C across built-in montages.
#     Return final_raw (winning montage & names), best_montage_name, matched_names.
#     """
#     n_ch = len(channel_names)
#     data = np.zeros((n_ch, 10), dtype=float)  # 10 samples is enough
#     raw_info = mne.create_info(ch_names=list(channel_names), sfreq=float(sfreq), ch_types='eeg')
#     raw_orig = mne.io.RawArray(data, raw_info)

#     ch_map_try1 = make_ch_map_try1(raw_orig.ch_names)
#     ch_map_try2 = make_ch_map_try2(raw_orig.ch_names)

#     best_name, best_score, best_pass = "", -np.inf, "A"
#     # Pass A
#     for item in get_builtin_montages():
#         s = _score_for_montage(raw_orig, item)
#         if s > best_score: best_name, best_score, best_pass = item, s, "A"
#     # Pass B
#     raw_try1 = raw_orig.copy().rename_channels(ch_map_try1)
#     for item in get_builtin_montages():
#         s = _score_for_montage(raw_try1, item)
#         if s > best_score: best_name, best_score, best_pass = item, s, "B"
#     # Pass C
#     raw_try2 = raw_orig.copy().rename_channels(ch_map_try2)
#     for item in get_builtin_montages():
#         s = _score_for_montage(raw_try2, item)
#         if s > best_score: best_name, best_score, best_pass = item, s, "C"

#     # Build final_raw per winning pass
#     if best_pass == "A":
#         final_raw = raw_orig.copy()
#     elif best_pass == "B":
#         final_raw = raw_orig.copy().rename_channels(ch_map_try1)
#     else:
#         final_raw = raw_orig.copy().rename_channels(ch_map_try2)

#     final_montage = make_standard_montage(best_name)
#     final_raw.set_montage(montage=final_montage, match_alias=True, match_case=False, on_missing='ignore')

#     # Matched channels (with non-zero positions)
#     matched = []
#     for idx, ch in enumerate(final_raw.info['chs']):
#         if ch['kind'] == mne.io.constants.FIFF.FIFFV_EEG_CH and not np.allclose(ch['loc'][:3], 0):
#             matched.append(final_raw.info['ch_names'][idx])

#     if DEBUG:
#         print(f"[INFO] Best montage: {best_name} (pass {best_pass}) score={best_score:.2f}")
#         print(f"[INFO] Matched: {len(matched)}")
#     return final_raw, best_name, matched

# # -------------------------------
# # dPLI plotting (manual + auto ready; NO title)
# # -------------------------------
# def plot_dpli_generic(
#     M, labels, montage_name,
#     mode: str = 'manual',
#     # Manual-threshold defaults:
#     neutral_abs: float = 0.01,
#     moderate_abs: float = 0.02,
#     strong_abs: float = 0.08,
#     max_abs=0.25,
#     # Auto mode knobs (not used unless mode='auto'):
#     auto_density: float = 0.15,
#     strong_top_frac: float = 0.5,
#     # Layout:
#     target_radius: float = 0.49, rotate_deg: float = 0.0, shift_x: float = 0.0, shift_y: float = 0.0,
#     figsize=(8,8), dpi=300,
#     # Direction visualization:
#     direction_mode: str = 'gradient'   # 'gradient' (default) or 'order'
# ):
#     # montage coords (exclude HydroCel non-brain)
#     m_names, m_xy = _coords_for_montage(montage_name)
#     keep_idx = list(range(len(m_names)))
#     if _is_hc_128_129(montage_name):
#         exclude = set(NON_BRAIN_HC_128_129)
#         keep_idx = [i for i, n in enumerate(m_names) if n not in exclude]
#     m_names = [m_names[i] for i in keep_idx]; m_xy = m_xy[keep_idx]

#     def _norm(s): return re.sub(r"[^0-9a-z]+", "", s.lower())
#     label_norm_to_idx = {_norm(n): i for i, n in enumerate(labels)}

#     pairs = []
#     for i_m, nm in enumerate(m_names):
#         k = _norm(nm)
#         if k in label_norm_to_idx:
#             pairs.append((i_m, label_norm_to_idx[k]))
#     if len(pairs) < 2:
#         raise RuntimeError("Not enough overlapping channels to plot dPLI.")

#     idx_m, idx_l = zip(*pairs); idx_m, idx_l = list(idx_m), list(idx_l)
#     D = np.asarray(M, float)[np.ix_(idx_l, idx_l)]
#     np.fill_diagonal(D, 0.5)

#     XY_all = _normalize_xy(m_xy, target_radius, rotate_deg, shift_x, shift_y)
#     XYp = np.stack([XY_all[i_m] for i_m in idx_m], axis=0)
#     present_names = [m_names[i] for i in idx_m]

#     # candidate edges (use upper triangle only)
#     cand = []
#     for a in range(len(idx_l)):
#         for b in range(a + 1, len(idx_l)):
#             bias = float(D[a, b]) - 0.5
#             cand.append((a, b, bias, abs(bias)))

#     edges_strong, edges_mod = [], []
#     if mode == 'auto':
#         n_pairs = len(cand)
#         if n_pairs == 0: raise RuntimeError("No pairs for auto-density.")
#         keep_n = max(1, int(round(float(auto_density) * n_pairs)))
#         kept = sorted(cand, key=lambda x: x[3], reverse=True)[:keep_n]
#         cut = max(1, int(round((1.0 - float(strong_top_frac)) * len(kept))))
#         thin, thick = kept[:cut], kept[cut:]
#         if isinstance(max_abs, str) and max_abs.lower() == 'auto':
#             abs_vals = np.array([ab for *_, ab in kept], float)
#             max_abs = float(np.percentile(abs_vals, 95)) or 0.01
#         for a,b,bias,_ in thin:  edges_mod.append((a,b,bias))
#         for a,b,bias,_ in thick: edges_strong.append((a,b,bias))
#     else:
#         for a,b,bias,ab in cand:
#             if ab < neutral_abs: continue
#             if ab >= strong_abs: edges_strong.append((a,b,bias))
#             elif ab >= moderate_abs: edges_mod.append((a,b,bias))

#     connected = set()
#     for i,j,_ in edges_mod + edges_strong: connected.add(i); connected.add(j)

#     fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
#     ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
#     # leave some bottom margin for 'order' mode text
#     if direction_mode == 'order':
#         fig.subplots_adjust(bottom=0.22)
#     ax.add_artist(plt.Circle((0.5,0.5), target_radius, edgecolor='gray', facecolor='none', lw=2.5, zorder=0))

#     # color mapping (for solid mode)
#     # cmap = cm.get_cmap('seismic')
#     # Custom diverging map: blue (lags) -> purple (neutral) -> red (leads)
#     cmap = LinearSegmentedColormap.from_list(
#         "leadlag_purple_mid",
#         [
#             (0.00, (0.10, 0.25, 0.80)),  # blue-ish for negative bias
#             (0.50, (0.50, 0.00, 0.50)),  # purple at zero
#             (1.00, (0.85, 0.20, 0.20)),  # red-ish for positive bias
#         ],
#         N=256,
#     )

#     max_abs_val = float(max_abs) if isinstance(max_abs,(int,float)) else 0.25
#     norm = plt.Normalize(vmin=-max_abs_val, vmax=+max_abs_val)

#     # ---- helpers for solid edges ----
#     def add_group(recs, lw, alpha_base):
#         if not recs: return None
#         segs, cols, lws = [], [], []
#         for (a,b,bias) in recs:
#             p1, p2 = XYp[a], XYp[b]
#             col = cmap(norm(bias))
#             alpha = alpha_base + (min(abs(bias), max_abs_val) / max_abs_val) * (1.0 - alpha_base)
#             segs.append((p1,p2)); cols.append((col[0], col[1], col[2], alpha)); lws.append(lw)
#         lc = LineCollection(
#             segs, colors=cols, linewidths=lws,
#             zorder=1.2 if lw <= 2 else 1.6,  # moderates behind, strong above
#             capstyle='butt', joinstyle='miter', antialiased=True
#         )
#         ax.add_collection(lc); return lc

#     # ---- helper for gradient edges (red/blue with PURPLE center) ----
#     def _draw_gradient_edges(ax, XYp, recs, *,
#                              lw=3.6, alpha_base=0.90,
#                              nseg=16, eps_frac=1e-3,
#                              max_abs_val=0.25):
#         if not recs: return None
#         segs, cols, lws = [], [], []
#         purple = np.array([0.60, 0.00, 0.60])  # mid color

#         for (a, b, bias) in recs:
#             p1 = XYp[a]; p2 = XYp[b]
#             dx = float(p2[0] - p1[0]); dy = float(p2[1] - p1[1])
#             L = (dx*dx + dy*dy) ** 0.5
#             if L <= 1e-9: continue
#             ux, uy = dx / L, dy / L

#             if bias >= 0:
#                 c_leader = np.array([1.0, 0.0, 0.0])  # leader red
#                 c_lagger = np.array([0.0, 0.0, 1.0])  # lagger blue
#             else:
#                 c_leader = np.array([0.0, 0.0, 1.0])  # leader blue
#                 c_lagger = np.array([1.0, 0.0, 0.0])  # lagger red

#             alpha = alpha_base + (min(abs(bias), max_abs_val) / max_abs_val) * (1.0 - alpha_base)

#             ts = np.linspace(0.0, 1.0, nseg + 1)
#             eps = eps_frac  # tiny overlap to avoid gaps/dots

#             for i in range(nseg):
#                 t0 = max(0.0, ts[i]   - eps)
#                 t1 = min(1.0, ts[i+1] + eps)

#                 x0 = p1[0] + ux * (t0 * L); y0 = p1[1] + uy * (t0 * L)
#                 x1 = p1[0] + ux * (t1 * L); y1 = p1[1] + uy * (t1 * L)
#                 segs.append([(x0, y0), (x1, y1)])

#                 # piecewise: leader -> PURPLE up to mid, then PURPLE -> lagger
#                 tm = 0.5 * (t0 + t1)
#                 if tm <= 0.5:
#                     # 0..1 across first half
#                     t_blend = tm * 2.0
#                     rgb = (1.0 - t_blend) * c_leader + t_blend * purple
#                 else:
#                     t_blend = (tm - 0.5) * 2.0
#                     rgb = (1.0 - t_blend) * purple + t_blend * c_lagger

#                 cols.append((rgb[0], rgb[1], rgb[2], alpha))
#                 lws.append(lw)

#         lc = LineCollection(
#             segs, colors=cols, linewidths=lws,
#             zorder=1.6 if lw >= 3 else 1.2,
#             capstyle='butt', joinstyle='miter', antialiased=True
#         )
#         ax.add_collection(lc)
#         return lc

#     # draw edges
#     if direction_mode == 'gradient':
#         # Moderates: faint & thin; Strong: bold & more segments. Thresholds unchanged.
#         lc_mod = _draw_gradient_edges(ax, XYp, edges_mod,
#                                       lw=1.2, alpha_base=0.08, nseg=8,  max_abs_val=max_abs_val)
#         lc_str = _draw_gradient_edges(ax, XYp, edges_strong,
#                                       lw=3.6, alpha_base=0.92, nseg=18, max_abs_val=max_abs_val)
#     else:  # 'order' mode: solid diverging colors; add channel-order line below
#         lc_mod = add_group(edges_mod,   lw=1.2, alpha_base=0.08)
#         lc_str = add_group(edges_strong, lw=3.6, alpha_base=0.92)

#     # nodes & labels
#     all_idx = list(range(len(present_names)))
#     unconnected = [i for i in all_idx if i not in connected]
#     if unconnected:
#         ax.scatter(XYp[unconnected,0], XYp[unconnected,1], s=70, facecolor='white',
#                    edgecolor='black', linewidth=1.0, zorder=2.0)
#     if connected:
#         conn = sorted(list(connected))
#         ax.scatter(XYp[conn,0], XYp[conn,1], s=74, facecolor='black',
#                    edgecolor='white', linewidth=1.0, zorder=2.2)
#     for i,name in enumerate(present_names):
#         x,y = XYp[i]
#         if i in connected:
#             ax.text(x,y+0.014, name, fontsize=7.5, fontweight='bold', ha='center', va='center')
#         else:
#             ax.text(x,y+0.014, name, fontsize=7.0, ha='center', va='center')

#     # colorbar
#     # sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm); sm.set_array([])
#     # cbar = plt.colorbar(sm, ax=ax, fraction=0.03, pad=0.02)
#     # if direction_mode == 'order':
#     #     cbar.set_label("Bias = dPLI − 0.5  (direction = row → col using channel order below)", fontsize=8)
#     # else:
#     #     cbar.set_label("Bias = dPLI − 0.5", fontsize=8)
#     # cbar.ax.tick_params(labelsize=6)

#     # --- dPLI colorbar: direction-only (sign), strength shown by width/opacity ---
#     sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm); sm.set_array([])
#     cbar = plt.colorbar(sm, ax=ax, fraction=0.03, pad=0.02)
#     cbar.set_label("dPLI direction (sign only); strength = line width/opacity", fontsize=8)

#     # Show direction categories instead of numeric values
#     cbar.set_ticks([-max_abs_val, 0.0, +max_abs_val])
#     cbar.ax.set_yticklabels(["lags (−)", "leads (+)"])  # if horizontal, use set_xticklabels
#     cbar.ax.tick_params(labelsize=6)


#     # legend
#     handles = [Patch(facecolor='white', edgecolor='black', label='present, unconnected'),
#                Patch(facecolor='black', edgecolor='white', label='present, connected')]
#     if mode == 'auto':
#         if lc_mod is not None: handles.append(Line2D([0],[0], color='k', lw=1.2, alpha=0.7, label="kept (thin)"))
#         if lc_str is not None: handles.append(Line2D([0],[0], color='k', lw=3.6, alpha=1.0, label="top kept (thick)"))
#     else:
#         if lc_mod is not None: handles.append(Line2D([0],[0], color='k', lw=1.2, alpha=0.7, label=f"moderate ≥ {moderate_abs:.2f}"))
#         if lc_str is not None: handles.append(Line2D([0],[0], color='k', lw=3.6, alpha=1.0, label=f"strong ≥ {strong_abs:.2f}"))

#     if direction_mode == 'gradient':
#         # small explanatory note (no arrows)
#         handles.append(Line2D([0],[0], color='none', label="Edges fade: leader (red) → lagger (blue)"))

#     ax.legend(handles=handles, loc='upper right', bbox_to_anchor=(1.15,1.15), fontsize=7, frameon=True)

#     # bottom channel order line for 'order' mode
#     if direction_mode == 'order':
#         # The matrix order used for rows/cols is labels[idx_l]
#         order_labels = [labels[i] for i in idx_l]
#         fig.text(0.5, 0.03,
#                  "Row/Column channel order (left→right): " + ", ".join(order_labels),
#                  ha='center', va='center', fontsize=7)

#     return fig

# def plot_best_dpli(M, info_channel_names, final_raw, best_montage_name, **kwargs):
#     labels_for_plot = _choose_best_label_mapping(info_channel_names, final_raw)
#     return plot_dpli_generic(M=M, labels=labels_for_plot, montage_name=best_montage_name, **kwargs)

# # -------------------------------
# # wPLI plotting (manual + auto ready; NO title)
# # -------------------------------
# def plot_wpli_generic(
#     W, labels, montage_name,
#     mode: str = 'manual',
#     # Manual thresholds:
#     neutral_min: float = 0.05,
#     moderate_min: float = 0.10,
#     strong_min: float = 0.20,
#     max_val=0.40,
#     # Auto mode (not used unless mode='auto'):
#     auto_density: float = 0.15, strong_top_frac: float = 0.5,
#     # Layout:
#     target_radius: float = 0.49, rotate_deg: float = 0.0, shift_x: float = 0.0, shift_y: float = 0.0,
#     figsize=(8,8), dpi=300
# ):
#     m_names, m_xy = _coords_for_montage(montage_name)
#     keep_idx = list(range(len(m_names)))
#     if _is_hc_128_129(montage_name):
#         exclude = set(NON_BRAIN_HC_128_129)
#         keep_idx = [i for i, n in enumerate(m_names) if n not in exclude]
#     m_names = [m_names[i] for i in keep_idx]; m_xy = m_xy[keep_idx]

#     def _norm(s): return re.sub(r"[^0-9a-z]+", "", s.lower())
#     label_norm_to_idx = {_norm(n): i for i, n in enumerate(labels)}

#     pairs = []
#     for i_m, nm in enumerate(m_names):
#         k = _norm(nm)
#         if k in label_norm_to_idx: pairs.append((i_m, label_norm_to_idx[k]))
#     if len(pairs) < 2:
#         raise RuntimeError("Not enough overlapping channels to plot wPLI.")

#     idx_m, idx_l = zip(*pairs); idx_m, idx_l = list(idx_m), list(idx_l)

#     W = np.asarray(W, float)
#     Wsub = W[np.ix_(idx_l, idx_l)]
#     np.fill_diagonal(Wsub, 0.0)

#     XY_all = _normalize_xy(m_xy, target_radius, rotate_deg, shift_x, shift_y)
#     XYp = np.stack([XY_all[i_m] for i_m in idx_m], axis=0)
#     present_names = [m_names[i] for i in idx_m]

#     cand = []
#     nC = len(idx_l)
#     for a in range(nC):
#         for b in range(a + 1, nC):
#             cand.append((a, b, float(Wsub[a, b])))

#     edges_thin, edges_thick = [], []
#     if mode == 'auto':
#         n_pairs = len(cand)
#         if n_pairs == 0: raise RuntimeError("No pairs for auto-density (wPLI).")
#         keep_n = max(1, int(round(float(auto_density) * n_pairs)))
#         kept = sorted(cand, key=lambda x: x[2], reverse=True)[:keep_n]
#         cut = max(1, int(round((1.0 - float(strong_top_frac)) * len(kept))))
#         thin, thick = kept[:cut], kept[cut:]
#         if isinstance(max_val, str) and max_val.lower() == 'auto':
#             vals = np.array([w for *_, w in kept], float)
#             max_val = float(np.percentile(vals, 95)) or 0.05
#         for a,b,w in thin:  edges_thin.append((a,b,w))
#         for a,b,w in thick: edges_thick.append((a,b,w))
#     else:
#         for a,b,w in cand:
#             if w < neutral_min: continue
#             if w >= strong_min: edges_thick.append((a,b,w))
#             elif w >= moderate_min: edges_thin.append((a,b,w))

#     connected = set()
#     for i,j,_ in edges_thin + edges_thick: connected.add(i); connected.add(j)

#     fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
#     ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
#     ax.add_artist(plt.Circle((0.5,0.5), target_radius, edgecolor='gray', facecolor='none', lw=2.5, zorder=0))

#     # Use reversed magma so darker = stronger (more perceptible)
#     cmap = cm.get_cmap('magma_r')
#     max_val_f = float(max_val) if isinstance(max_val,(int,float)) else 0.40
#     norm = plt.Normalize(vmin=0.0, vmax=max_val_f)

#     def add_group(recs, lw, alpha_base):
#         if not recs: return None
#         segs, cols, lws = [], [], []
#         for (a,b,w) in recs:
#             p1, p2 = XYp[a], XYp[b]
#             col = cmap(norm(w))
#             alpha = alpha_base + (min(w, max_val_f) / max_val_f) * (1.0 - alpha_base)
#             segs.append((p1,p2)); cols.append((col[0], col[1], col[2], alpha)); lws.append(lw)
#         lc = LineCollection(
#             segs, colors=cols, linewidths=lws,
#             zorder=1.2 if lw <= 2 else 1.6,
#             capstyle='butt', joinstyle='miter', antialiased=True
#         )
#         ax.add_collection(lc); return lc

#     # moderates faint/thin; strong bold (thresholds unchanged)
#     lc_mod = add_group(edges_thin, 1.2, 0.08)
#     lc_str = add_group(edges_thick, 3.6, 0.92)

#     all_idx = list(range(len(present_names)))
#     unconnected = [i for i in all_idx if i not in connected]
#     if unconnected:
#         ax.scatter(XYp[unconnected,0], XYp[unconnected,1], s=70, facecolor='white', edgecolor='black', linewidth=1.0, zorder=2.0)
#     if connected:
#         conn = sorted(list(connected))
#         ax.scatter(XYp[conn,0], XYp[conn,1], s=74, facecolor='black', edgecolor='white', linewidth=1.0, zorder=2.2)
#     for i,name in enumerate(present_names):
#         x,y = XYp[i]
#         if i in connected:
#             ax.text(x,y+0.014, name, fontsize=7.5, fontweight='bold', ha='center', va='center')
#         else:
#             ax.text(x,y+0.014, name, fontsize=7.0, ha='center', va='center')

#     sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm); sm.set_array([])
#     cbar = plt.colorbar(sm, ax=ax, fraction=0.03, pad=0.02)
#     cbar.set_label("wPLI strength (0–1)", fontsize=8)
#     cbar.ax.tick_params(labelsize=6)

#     # legend (no direction note for wPLI)
#     handles = [Patch(facecolor='white', edgecolor='black', label='present, unconnected'),
#                Patch(facecolor='black', edgecolor='white', label='present, connected')]
#     if mode == 'auto':
#         if lc_mod is not None: handles.append(Line2D([0],[0], color='k', lw=1.2, alpha=0.7, label="kept (thin)"))
#         if lc_str is not None: handles.append(Line2D([0],[0], color='k', lw=3.6, alpha=1.0, label="top kept (thick)"))
#     else:
#         if lc_mod is not None: handles.append(Line2D([0],[0], color='k', lw=1.2, alpha=0.7, label=f"moderate ≥ {moderate_min:.2f}"))
#         if lc_str is not None: handles.append(Line2D([0],[0], color='k', lw=3.6, alpha=1.0, label=f"strong ≥ {strong_min:.2f}"))

#     ax.legend(handles=handles, loc='upper right', bbox_to_anchor=(1.15,1.15), fontsize=7, frameon=True)
#     return fig

# def plot_best_wpli(W, info_channel_names, final_raw, best_montage_name, **kwargs):
#     labels_for_plot = _choose_best_label_mapping(info_channel_names, final_raw)
#     return plot_wpli_generic(W=W, labels=labels_for_plot, montage_name=best_montage_name, **kwargs)



















# """
# @ Valorisation Recherche HSCM, Societe en Commandite – 2025
# See the file LICENCE for full license details.

#     ConnectivityDetails
#     Node to save connectivity results (matrix and image) to disk.
#     Works for wPLI and dPLI results.
# """
# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from flowpipe import SciNode, InputPlug, OutputPlug
# from commons.NodeInputException import NodeInputException
# from commons.NodeRuntimeException import NodeRuntimeException

# DEBUG = False

# class ConnectivityDetails(SciNode):
#     """
#     Node for saving connectivity results (matrix and image) to disk.
#     Works for wPLI and dPLI results.

#     Parameters
#     ----------
#         recording_path: str
#             Path to the input EEG recording (used to find the output folder).
#         subject_info: dict
#             Metadata about the subject; must contain "filename".
#         con_dict: dict
#             Dictionary containing the connectivity results
#             (should contain either wPLI or dPLI outputs).
#         output_path: str or None
#             User-selected output directory (from UI path). If None, save to input folder.
#     Returns
#     -------
#         None
#     """
#     def __init__(self, **kwargs):
#         """ Initialize module ConnectivityDetails """
#         super().__init__(**kwargs)
#         if DEBUG: print('ConnectivityDetails.__init__')

#         # Input plugs
#         InputPlug('recording_path',self)
#         InputPlug('subject_info',self)
#         InputPlug('con_dict',self)
#         InputPlug('output_path',self)
#         self._is_master = False 
    
#     def compute(self, recording_path,subject_info,con_dict,output_path):
#         """
#         Save connectivity matrix (tsv) and its image (png) in the same directory as the input EEG.
#         """
#         # --- Basic checks ---
#         if not recording_path:
#             raise NodeInputException(self.identifier, "recording_path", "Missing recording path.")
#         if not subject_info or "filename" not in subject_info:
#             raise NodeInputException(self.identifier, "subject_info", "Missing subject_info['filename'].")

#         # --- Determine output directory and filenames ---

#         subject_name = subject_info["filename"]
#         # NEW: Use output_path if given, otherwise default to folder of input file
#         if output_path:
#             out_dir = output_path
#         elif os.path.isdir(recording_path):
#             out_dir = recording_path
#         else:
#             out_dir = os.path.dirname(recording_path)
            
#         print("************************************")
#         print(f"ConnectivityDetails called for subject: {subject_name}")
#         print(f"recording_path: {recording_path}")
#         print(f"output_path: {output_path!r}")  # !r will show "" for empty strings
#         print(f"Saving outputs in: {out_dir}")
#         print("************************************")

#         if "average_wpli" in con_dict:
#             matrix = con_dict["average_wpli"]
#             channel_names = con_dict["channel_names"]
#             title = "WPLI Connectivity"
#             base = f"{subject_name}_wpli"
#         elif "average_dpli" in con_dict:
#             matrix = con_dict["average_dpli"]
#             channel_names = con_dict["channel_names"]
#             title = "DPLI Connectivity"
#             base = f"{subject_name}_dpli"
#         else:
#             raise NodeInputException(self.identifier, "con_dict", "No wpli or dpli results found!")

#         tsv_path = os.path.join(out_dir, f"{base}_convalue.tsv")
#         img_path = os.path.join(out_dir, f"{base}_conpic.png")

#         # --- Extract connectivity results (supports both wpli and dpli) ---
#         key = next((k for k in con_dict.keys() if 'wpli' in k or 'dpli' in k), None)
#         if not key:
#             raise NodeInputException(self.identifier, "con_dict", "con_dict must contain a key with 'wpli' or 'dpli'.")

#         if "average_wpli" in con_dict:
#             matrix = con_dict["average_wpli"]
#             channel_names = con_dict["channel_names"]
#             title = "WPLI Connectivity"
#         elif "average_dpli" in con_dict:
#             matrix = con_dict["average_dpli"]
#             channel_names = con_dict["channel_names"]
#             title = "DPLI Connectivity"
#         else:
#             Exception(self.identifier, "con_dict", "No wpli or dpli results found!")



#         # --- Save matrix as TSV ---
#         try:
#             df = pd.DataFrame(matrix, index=channel_names, columns=channel_names)
#             df.to_csv(tsv_path, sep="\t")
#             self._log_manager.log(self.identifier, f"Saved connectivity TSV: {tsv_path}")
#         except Exception as e:
#             raise NodeRuntimeException(self.identifier, "TSV", f"Failed to save TSV: {str(e)}")

#         # --- Save matrix as PNG image ---
#         try:
#             plt.figure(figsize=(8, 6))
#             plt.imshow(matrix, cmap="jet", aspect="auto")
#             plt.colorbar(label=title)
#             plt.xticks(ticks=np.arange(len(channel_names)), labels=channel_names, rotation=90)
#             plt.yticks(ticks=np.arange(len(channel_names)), labels=channel_names)
#             plt.title(title)
#             plt.tight_layout()
#             plt.savefig(img_path)
#             plt.close()
#             self._log_manager.log(self.identifier, f"Saved connectivity image: {img_path}")
#         except Exception as e:
#             raise NodeRuntimeException(self.identifier, "Image", f"Failed to save PNG: {str(e)}")

#         return {}  # No need to return anything unless for the cache