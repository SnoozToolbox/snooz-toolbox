"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    NetworkProperties
    Computes graph-theoretic network properties from a wPLI connectivity matrix.
    Outputs per-window and averaged metrics (characteristic path length, clustering
    coefficient, global efficiency, small-worldness, modularity, participation
    coefficient) to TSV files.
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

import os
import numpy as np
import csv
from scipy.signal import hilbert
from numba import njit, prange
from joblib import Parallel, delayed
from commons.parallel_utils import normalize_n_jobs, select_joblib_backend

DEBUG = False

class NetworkProperties(SciNode):
    """
    Computes graph-theoretic network properties from a wPLI connectivity matrix.

    For each sliding window the module builds a binary network (using either a
    minimally-spanning-tree threshold or a user-supplied threshold), then
    computes characteristic path length, clustering coefficient, global
    efficiency, small-worldness, modularity, and participation coefficient.
    Results are normalized against a random null-model network and written
    to two TSV files (network properties and per-channel participation
    coefficients).

    Parameters
    ----------
    recording_path : str
        Path to the recording file or directory. Used as fallback output
        directory when output_path is not provided.
    subject_info : dict
        Dictionary with subject metadata. Must contain at least the key
        'filename' (str) used to build the output file names.
    con_dict : dict
        Connectivity dictionary produced by a wPLI module. Expected to
        contain either a 'wpli_results' key whose value is a dict with
        'final_wpli' (ndarray of shape (num_windows, C, C)) and
        'channel_names' (list[str]), or those keys at the top level.
    threshold_mode : str
        Thresholding strategy: 'minimally_spanning_tree' (automatically
        finds the smallest threshold that keeps the network connected) or
        'custom_threshold' (uses threshold_value directly).
    threshold_value : float
        Threshold between 0 and 1 indicating the proportion of strongest
        connections to retain. Only used when threshold_mode is
        'custom_threshold'. Default is 0.05.
    output_path : str or None
        Directory where TSV result files are saved. Falls back to
        recording_path when not provided.

    Returns
    -------
    (no output plugs)
        Results are written to TSV files in the output directory.
    """
    def __init__(self, **kwargs):
        """ Initialize module NetworkProperties """
        super().__init__(**kwargs)
        if DEBUG: print('NetworkProperties.__init__')

        # Input plugs
        InputPlug('recording_path',self)
        InputPlug('subject_info',self)
        InputPlug('con_dict',self)
        InputPlug('threshold_mode',self)
        InputPlug('threshold_value',self)
        InputPlug('output_path',self)
        
    def _extract_results(self, con_dict):
        """Return metric ('wpli'), matrix , channel_names (list)."""
        if isinstance(con_dict, dict):
            if 'wpli_results' in con_dict:
                r = con_dict['wpli_results']
                return 'wpli', r['final_wpli'], r['channel_names']
        if 'final_wpli' in con_dict:
            return 'wpli', con_dict['final_wpli'], con_dict['channel_names']
        raise NodeInputException(self.identifier, "con_dict",
                                 "No wPLI/dPLI results found (expected 'wpli_results').")



    def compute(self, recording_path,subject_info,con_dict,threshold_mode,threshold_value,output_path):
        """
        Compute network properties from a wPLI connectivity matrix and write
        per-window results to TSV files.

        Parameters
        ----------
        recording_path : str
            Path to the recording file or directory. Used as fallback output
            directory when output_path is not provided.
        subject_info : dict
            Dictionary with subject metadata. Must contain at least the key
            'filename' (str) used to build the output file names.
        con_dict : dict
            Connectivity dictionary containing wPLI results. Expected to hold
            a 3-D array of shape (num_windows, C, C) under the key
            'final_wpli' and a list of channel labels under 'channel_names'.
        threshold_mode : str
            'minimally_spanning_tree' or 'custom_threshold'.
        threshold_value : float
            Proportion of strongest connections to retain (0–1). Only used
            when threshold_mode is 'custom_threshold'. Default 0.05.
        output_path : str or None
            Directory for TSV output files.

        Returns
        -------
        dict
            Empty dict (results are persisted to TSV files).

        Raises
        ------
        NodeInputException
            If any of the input parameters have invalid types or missing keys.
        NodeRuntimeException
            If an error occurs during the execution of the function.
        """

        # --- Basic checks ---
        if isinstance(threshold_mode, str): threshold_mode = threshold_mode.lower()
        if threshold_mode is None: threshold_mode = 'minimally_spanning_tree'

        if threshold_value is None: threshold_value = 0.05
        if threshold_mode == "custom_threshold":
            try:
                if isinstance(threshold_value, str): 
                    threshold_value = float(threshold_value)
            except:
                raise NodeInputException(self.identifier, "threshold_value", "For custom_threshold mode, threshold_value must be a number between 0 and 1.")
            
            if not (isinstance(threshold_value, (float)) and threshold_value<1 and threshold_value>0):
                raise NodeInputException(self.identifier, "threshold_value", "For custom_threshold mode, threshold_value must be a number between 0 and 1.")
        

        if not threshold_mode in ["minimally_spanning_tree", "custom_threshold"]:
            raise NodeInputException(self.identifier, "threshold_mode", 
                "Invalid threshold_mode provided. Must be 'minimally_spanning_tree' or 'custom_threshold'.")


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

        # --- Extract connectivity ---
        metric, WPLI_matrix, channel_names = self._extract_results(con_dict)
        if len(channel_names) < 32:
            return {}


        base = f"{subject_name}_{metric}"

        net_properties_tsv_file = os.path.join(out_dir, f"{base}_net_properties_results.tsv")
        participation_coefficient_tsv_file = os.path.join(out_dir, f"{base}_participation_coefficient_results.tsv")\
        
        if DEBUG:
            print("************************************")
            print(f"NetworkProperties called for subject: {subject_name}")
            print(f"recording_path: {recording_path}")
            print(f"threshold_mode: {threshold_mode}")
            print(f"threshold_value: {threshold_value}")
            print(f"output_path: {output_path!r}")
            print(f"Saving outputs in: {out_dir}")
            print(f"Connectivity metric: {metric}")
            print(f"Network properties output path: {net_properties_tsv_file}")
            print(f"Participation coefficient output path: {participation_coefficient_tsv_file}")
            print("************************************")


        num_windows = WPLI_matrix.shape[0]
        # num_channels = len(channel_names)

        threshold_range = np.arange(0.99, 0.0099, -.01)

        # Define TSV fieldnames
        net_properties_fieldnames = ['Window_number', 'charpath', 'clustering', 'GlobalEfficiency', 'SmallWorldness', 'Modularity',
                                    'Participation_coefficient', 'MinSpanTreeThreshold']
        


        # Initialize arrays to store values
        clustering_values      = np.zeros(num_windows)
        charpath_values        = np.zeros(num_windows)
        geff_values            = np.zeros(num_windows)
        bsw_values             = np.zeros(num_windows)
        modular_values         = np.zeros(num_windows)
        participation_values   = np.zeros(num_windows)

        # --- Process all windows in parallel ---
        effective_n_jobs = normalize_n_jobs(-1, num_windows)

        if effective_n_jobs == 1:
            results = [_process_window(WPLI_matrix[w], threshold_mode,
                                       threshold_value, threshold_range)
                       for w in range(num_windows)]
        else:
            backend = select_joblib_backend()
            parallel_kwargs = {"n_jobs": effective_n_jobs, "backend": backend}
            if backend == "threading":
                parallel_kwargs["prefer"] = "threads"
            results = Parallel(**parallel_kwargs)(
                delayed(_process_window)(WPLI_matrix[w], threshold_mode,
                                         threshold_value, threshold_range)
                for w in range(num_windows)
            )

        # --- Collect results and write TSVs ---
        with open(net_properties_tsv_file, mode='w', newline='') as net_properties_file, \
            open(participation_coefficient_tsv_file, mode='w', newline='') as participation_coefficient_file:

            net_properties_writer = csv.DictWriter(net_properties_file, fieldnames=net_properties_fieldnames, delimiter='\t')
            participation_coefficient_writer = csv.DictWriter(participation_coefficient_file, fieldnames=['Window_number'] + channel_names, delimiter='\t')

            net_properties_writer.writeheader()
            participation_coefficient_writer.writeheader()

            for win_i, (cp, cl, ge, sw, mod, part, tv, P) in enumerate(results):
                charpath_values[win_i]      = cp
                clustering_values[win_i]    = cl
                geff_values[win_i]          = ge
                bsw_values[win_i]           = sw
                modular_values[win_i]       = mod
                participation_values[win_i] = part

                net_properties_writer.writerow({
                    'Window_number': win_i + 1,
                    'charpath': cp,
                    'clustering': cl,
                    'GlobalEfficiency': ge,
                    'SmallWorldness': sw,
                    'Modularity': mod,
                    'Participation_coefficient': part,
                    'MinSpanTreeThreshold': tv if threshold_mode == "minimally_spanning_tree" else None
                })

                p_dict = {'Window_number': win_i + 1}
                for idx, ch in enumerate(channel_names):
                    p_dict[ch] = P[idx]
                participation_coefficient_writer.writerow(p_dict)

        if threshold_mode == "minimally_spanning_tree":
            threshold_values = [r[6] for r in results]
            print(f'The average threshold value of all sliding windows is: {np.mean(threshold_values)}')

        # Calculate average outputs
        charpath_output         = np.mean(charpath_values)
        clustering_output       = np.mean(clustering_values)
        GlobalEfficiency_output = np.mean(geff_values)
        SmallWorldness_output   = np.mean(bsw_values)
        Modularity_output       = np.mean(modular_values)
        participation_output    = np.mean(participation_values)

        results_dict = {
            'charpath': charpath_output,
            'clustering': clustering_output,
            'GlobalEfficiency': GlobalEfficiency_output,
            'SmallWorldness': SmallWorldness_output,
            'Modularity': Modularity_output,
            'Participation_coefficient': participation_output
        }

        if threshold_mode == "minimally_spanning_tree":
            results_dict['minimally_spanning_tree_threshold'] = np.mean(threshold_values)

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "This module calculates network properties Based on WPLI connectivity matrix.")

        return {
        }
    







def _process_window(pli, threshold_mode, threshold_value, threshold_range):
    """Compute network properties for a single window (called in parallel)."""
    if threshold_mode == "minimally_spanning_tree":
        thresh_value = find_smallest_connected_threshold(pli, threshold_range)
    else:
        thresh_value = threshold_value

    b_mat = threshold_matrix(pli, thresh_value)

    D = distance_matrix(b_mat)
    b_lambda, geff, _, _, _ = charpath(D)
    W0, R = null_model_und_sign(b_mat, 10, .1)

    C = clustering_coef_bu(b_mat)
    M, modular = community_louvain(b_mat, 1)
    P = participation_coef(b_mat, M)

    rlambda, rgeff, _, _, _ = charpath(distance_matrix(W0), 0, 0)
    rC = clustering_coef_bu(W0)

    clustering_value    = np.nanmean(C) / np.nanmean(rC)
    charpath_value      = b_lambda / rlambda
    geff_value          = geff / rgeff
    bsw_value           = clustering_value / charpath_value
    modular_value       = modular
    participation_value = np.mean(P)

    return (charpath_value, clustering_value, geff_value, bsw_value,
            modular_value, participation_value, thresh_value, P)


# def get_phase(signal):
#     phase = hilbert(signal)
#     return phase




def threshold_matrix(matrix, threshold=0.05):
    # THRESHOLD_MATRIX Threshold a matrix to have element below a significant amount to 0
    # Matrix: N*N matrix with value within any range
    # t_level: value from 0 to 1 which set the ratio of highest value
    # to keep. i.e. t_level = 0.05 -> keep only top 5% value
    t_matrix = matrix.copy()
    sorted_matrix = np.sort(t_matrix.flatten())
    one_values = np.size(t_matrix, axis=0)
    sorted_matrix = sorted_matrix[0: (len(sorted_matrix) - one_values)]
    idx = int(np.floor(len(sorted_matrix) * (1 - threshold))) 
    t_element = sorted_matrix[idx]
    t_matrix[t_matrix < t_element] = 0
    t_matrix[t_matrix >= t_element] = 1
    np.fill_diagonal(t_matrix, 0)
    return t_matrix

# def binarize_matrix(matrix):
#     binarized_matrix = matrix.copy()
#     binarized_matrix[binarized_matrix != 0.0] = 1
#     return binarized_matrix


def find_smallest_connected_threshold(pli_matrix, threshold_range):
        # loop through threshold_range and find the one with the minmally spanning tree
    
    smallest_threshold = threshold_range[-1]
    for i, threshold in enumerate(threshold_range):
        
        # Thresholding and binarization using the current threshold

        b_network = threshold_matrix(pli_matrix, threshold)

        # check if the binary network is disconnected
        # Here our binary network (b_network) is a weight matrix but also an adjacency matrix.

        distance = distance_matrix(b_network)

        # Here we check if there is one node that is disconnected
        if np.sum(np.isinf(distance)):
            smallest_threshold = threshold_range[i-1]
            break

    return smallest_threshold


def distance_matrix(Adj_matrix):
    #DISTANCE_MATRIX       Distance matrix
    #
    #   D = distance_matrix(Adj_matrix)
    #
    #   The distance matrix contains lengths of shortest paths between all
    #   pairs of nodes. An entry (u,v) represents the length of shortest path 
    #   from node u to node v. The average shortest path length is the 
    #   characteristic path length of the network.
    #
    #   Input:      Adj_matrix,      binary directed/undirected connection matrix
    #   Output:     D,      distance matrix
    A = Adj_matrix.astype(np.float32).copy()
    A[A!=0] = 1                                #binarize and convert to double format

    path_length = 1                            # path length
    Lpath_matrix = A                           # matrix of number of paths with path_length
    D = A.copy()                                      # distance matrix

    while 1:
        path_length += 1
        Lpath_matrix = np.matmul(Lpath_matrix, A)
        Idx = np.logical_and(Lpath_matrix!=0, D==0)
        if np.sum(Idx) > 0:
            D[Idx] = path_length
        else:
            break

    D[D ==0] = np.inf                      # assign inf to disconnected nodes
    np.fill_diagonal(D, 0)                 # clear diagonal

    return D





# CHARPATH       Characteristic path length, global efficiency and related statistics

#  The network characteristic path length is the average shortest path
# length between all pairs of nodes in the network. The global efficiency
# is the average inverse shortest path length in the network. The nodal
# eccentricity is the maximal path length between a node and any other
# node in the network. The radius is the minimal eccentricity, and the
# diameter is the maximal eccentricity.

#  Input:      D,              distance matrix
#             diagonal_dist   optional argument
#                             include distances on the main diagonal
#                                 (default: diagonal_dist=0)
#             infinite_dist   optional argument
#                             include infinite distances in calculation
#                                 (default: infinite_dist=0)

#  Outputs:    lambda,        network characteristic path length
#             efficiency,     network global efficiency
#             ecc,            nodal eccentricity
#             radius,         network radius
#             diameter,       network diameter

#  Notes:
#     The input distance matrix may be obtained with any of the distance
# functions, e.g. distance_bin, distance_wei.
#     Characteristic path length is defined here as the mean shortest
# path length between all pairs of nodes, for consistency with common
# usage. Note that characteristic path length is also defined as the
# median of the mean shortest path length from each node to all other
# nodes.
#     Infinitely long paths (i.e. paths between disconnected nodes) are
# included in computations by default. This behavior may be modified with
# via the infinite_dist argument.


#   Olaf Sporns, Indiana University, 2002/2007/2008
# Mika Rubinov, U Cambridge, 2010/2015

# Modification history
# 2002: original (OS)
# 2010: incorporation of global efficiency (MR)
# 2015: exclusion of diagonal weights by default (MR)
# 2016: inclusion of infinite distances by default (MR)
def charpath(D_matrix, diagonal_dist=0, infinite_dist=0):
    D = D_matrix.astype(np.float32).copy()
    if np.any(np.isnan(D)):
        raise ValueError("The distance matrix must not contain NaN values.")
    if diagonal_dist == 0:
        np.fill_diagonal(D, np.nan)
    if infinite_dist == 0:
        D[np.isinf(D)] = np.nan
        
    Dv = D[~np.isnan(D)]
    lambdaa = np.mean(Dv)
    # Efficiency: mean of inverse entries of D(G)
    efficiency = np.mean(1/Dv)
    # Eccentricity for each vertex
    eccentricity = np.nanmax(D, axis=1)
    # Radius of graph
    radius = np.nanmin(eccentricity)
    # Diameter of graph
    diameter = np.nanmax(eccentricity)
    return lambdaa, efficiency, eccentricity, radius, diameter




#NULL_MODEL_UND_SIGN     Random graphs with preserved weight, degree and strength distributions
#
#   This function randomizes an undirected network with positive and
#   negative weights, while preserving the degree and strength distributions.
#
#   Inputs: W,          Undirected weighted connection matrix
#           bin_swaps,  Average number of swaps of each edge in binary randomization.
#                           bin_swap=5 is the default (each edge rewired 5 times)
#                           bin_swap=0 implies no binary randomization
#           wei_freq,   Frequency of weight sorting in weighted randomization
#                           wei_freq must be in the range of: 0 < wei_freq <= 1
#
#   Output:     W0,     Randomized weighted connection matrix
#               R,      Correlation coefficient between strength sequences
#                           of input and output connection matrices
#
#   Notes:
#       The value of bin_swaps is ignored when binary topology is fully
#   connected (e.g. when the network has no negative weights).
#       Randomization may be better (and execution time will be slower) for
#   higher values of bin_swaps and wei_freq. Higher values of bin_swaps may
#   enable a more random binary organization, and higher values of wei_freq
#   may enable a more accurate conservation of strength sequences.
#       R are the correlation coefficients between positive and negative
#   strength sequences of input and output connection matrices and are
#   used to evaluate the accuracy with which strengths were preserved. Note
#   that correlation coefficients may be a rough measure of
#   strength-sequence accuracy and one could implement more formal tests
#   (such as the Kolmogorov-Smirnov test) if desired.
#
#   Reference: Rubinov and Sporns (2011) Neuroimage 56:2068-79
#
#
#   2011-2015, Mika Rubinov, U Cambridge

#   Modification History
#   Mar 2011: Original
#   Sep 2012: Edge-sorting acceleration
#   Dec 2015: Enforce preservation of negative degrees in sparse
#             networks with negative weights (thanks to Andrew Zalesky).
def null_model_und_sign(Connection_matrix, bin_swaps=5, wei_freq=.1):
    W = Connection_matrix.copy()
    if wei_freq<=0 or wei_freq>1:
        raise ValueError("wei_freq must be in the range of: 0 < wei_freq <= 1.")

    n = W.shape[0]
    np.fill_diagonal(W, 0)
    # positive adjacency matrix
    Ap = (W>0).astype(int)                                                   
    An = (W<0).astype(int) 
    if np.count_nonzero(Ap) < (n*(n-1)):
        W_r,_  = randmio_und_signed(W, bin_swaps)
        Ap_r = (W_r>0).astype(int) 
        An_r = (W_r<0).astype(int) 
    else:
        Ap_r = Ap.copy()
        An_r = An.copy()


    W0 = np.zeros((n,n))
    for s in [1,-1]:
        if s == 1:
            S = np.sum(W*Ap, axis=1)
            Wv = np.sort(W[(np.triu(Ap)).astype(bool)])
            J,I = np.where(np.triu(Ap_r).T!=0)
            Lij=n*J+I; 
        
        elif s == -1:
            S = np.sum(-W*An, axis=1)
            Wv = np.sort(-W[(np.triu(An_r)).astype(bool)])
            J,I = np.where(np.triu(An_r).T!=0)
            Lij=n*J+I; 
            
        P = np.outer(S, S)

        if wei_freq==1:
            for m in range(np.size(Wv),0,-1):
                oind = np.argsort(P[I, J])
                r = np.random.randint(0, m)
                o = oind[r]
                W0[I[o],J[o]] = s*Wv[r]
                f = 1 - Wv[r] / S[I[o]] if S[I[o]] != 0 else 1.0
                P[I[o],:] = P[I[o],:]*f
                P[:,I[o]] = P[:,I[o]]*f
                f = 1 - Wv[r] / S[J[o]] if S[J[o]] != 0 else 1.0
                P[J[o],:] = P[J[o],:]*f
                P[:,J[o]] = P[:,J[o]]*f

                S[[I[o], J[o]]] = S[[I[o], J[o]]] - Wv[r]
                I = np.delete(I,o)
                J = np.delete(J,o)
                Wv = np.delete(Wv,r)
                
        else:
            wei_period = (np.round(1/wei_freq)).astype(int)
            for m in range(np.size(Wv),1,-wei_period):
                oind = np.argsort(P[I, J])
                R = np.random.permutation(np.arange(m))[:min(m, wei_period)]
            # R = np.arange(m)
                o = oind[R]
                ii=Lij[o]%n
                jj=Lij[o]//n
                W0[ii,jj] = s*Wv[R]
                WA = accumarray(np.concatenate([I[o],J[o]]), Wv[np.concatenate([R,R])], n)
                IJu = (WA!=0).astype(np.int32)
                F = np.where(S[IJu] != 0, 1 - WA[IJu] / S[IJu], 1.0)
                F = np.repeat(np.expand_dims(F,1), n, axis=1)
                P[IJu,:] = P[IJu,:]*F             
                P[:,IJu] = P[:,IJu]*F
                S[IJu] = S[IJu]-WA[IJu] 
                o = oind[R]
                I = np.delete(I,o)
                J = np.delete(J,o)
                Lij = np.delete(Lij,o)
                Wv = np.delete(Wv,R)
    W0 = W0 + W0.T
    with np.errstate(invalid='ignore'):
        rpos = np.corrcoef(np.sum(W*(W>0).astype(np.int32),axis=0), np.sum(W0*(W0>0).astype(np.int32),axis=0))
        rneg = np.corrcoef(np.sum(-W*(W<0).astype(np.int32),axis=0), np.sum(-W0*(W0<0).astype(np.int32),axis=0))
    R=np.array([np.nan_to_num(rpos[1,0]), np.nan_to_num(rneg[1,0])])

    return W0, R



def accumarray(inds, data, size):
    if inds.shape != data.shape:
        raise ValueError("first and second arrays should be of the same size.")
    if np.max(inds)>=size:
        raise ValueError("indices maximum should be lower than size.")
    output = np.zeros(size)
    for i in range(size):
        output[i] = np.sum(data[inds==i])
    return output




def randmio_und_signed(W, ITER):
    R = W.astype(np.float32)
    n = R.shape[0]
    ITER = ITER*n*(n-1)/2
    maxAttempts = np.round(n/2)
    eff = 0
    for iter in range(int(ITER)):
        att = 0
        while(att<=maxAttempts):
            nodes = np.random.permutation(np.arange(n))[:4]
            a = nodes[0]
            b = nodes[1]
            c = nodes[2]
            d = nodes[3]

            r0_ab = R[a,b]
            r0_cd = R[c,d]
            r0_ad = R[a,d]
            r0_cb = R[c,b]

            if  (np.sign(r0_ab)==np.sign(r0_cd)) and \
                (np.sign(r0_ad)==np.sign(r0_cb)) and \
                (np.sign(r0_ab)!=np.sign(r0_ad)):
                R[a,d]=r0_ab
                R[a,b]=r0_ad
                R[d,a]=r0_ab
                R[b,a]=r0_ad
                R[c,b]=r0_cd
                R[c,d]=r0_cb
                R[b,c]=r0_cd
                R[d,c]=r0_cb
                eff += 1
            att += 1

    return R, eff




# CLUSTERING_COEF_BU     Clustering coefficient
#    C = clustering_coef_bu(A);
#    The clustering coefficient is the fraction of triangles around a node
#    (equiv. the fraction of node's neighbors that are neighbors of each other).
#    Input:      A,      binary undirected connection matrix
#    Output:     C,      clustering coefficient vector
#    Reference: Watts and Strogatz (1998) Nature 393:440-442.
#    Mika Rubinov, UNSW, 2007-2010

@njit(parallel=True)
def clustering_coef_bu(A):
    n = A.shape[0]
    C = np.zeros(n, dtype=np.float64)
    for u in prange(n):
        K = 0
        for v in range(n):
            if A[u, v] != 0:
                K += 1
        if K >= 2:
            S_sum = 0.0
            for vi in range(n):
                if A[u, vi] == 0:
                    continue
                for vj in range(n):
                    if A[u, vj] == 0:
                        continue
                    S_sum += A[vi, vj]
            C[u] = S_sum / (K * K - K)
    return C




#COMMUNITY_LOUVAIN     Optimal community structure

#   The optimal community structure is a subdivision of the network into
#   nonoverlapping groups of nodes which maximizes the number of within-
#	group edges, and minimizes the number of between-group edges.
#
#   This function is a fast and accurate multi-iterative generalization of
#   the Louvain community detection algorithm.
#
#   Inputs:
#       W,
#           directed/undirected weighted/binary connection matrix with
#           positive and possibly negative weights.
#       gamma,
#               resolution parameter (optional)
#               gamma>1,        detects smaller modules
#               0<=gamma<1,     detects larger modules
#               gamma=1,        classic modularity (default)
#       M0,
#           initial community affiliation vector (optional)
#       B,
#           objective-function type or custom objective matrix (optional)
#           'modularity',       modularity (default)
#           'potts',            Potts-model Hamiltonian (for binary networks)
#           'negative_sym',     symmetric treatment of negative weights
#           'negative_asym',    asymmetric treatment of negative weights
#           B,                  custom objective-function matrix
#
#           Note: see Rubinov and Sporns (2011) for a discussion of
#           symmetric vs. asymmetric treatment of negative weights.
#
#   Outputs:
#       M,
#           community affiliation vector
#       Q,
#           optimized community-structure statistic (modularity by default)
#
#   References:
#       Blondel et al. (2008)  J. Stat. Mech. P10008.
#       Reichardt and Bornholdt (2006) Phys. Rev. E 74, 016110.
#       Ronhovde and Nussinov (2008) Phys. Rev. E 80, 016109
#       Sun et al. (2008) Europhysics Lett 86, 28004.
#       Rubinov and Sporns (2011) Neuroimage 56:2068-79.
#
#   Mika Rubinov, U Cambridge 2015-2016

#   Modification history
#   2015: Original
#   2016: Included generalization for negative weights.
#         Enforced binary network input for Potts-model Hamiltonian.
#         Streamlined code and expanded documentation.
def community_louvain(W,gamma=1,M0=None,B='modularity'):

    n = len(W)
    s = np.sum(np.sum(W))
    if B == 'negative_sym' or B == 'negative_asym':
        W0 = W * (W>0).astype(int)
        s0 = np.sum(W0)
        B0 = W0-gamma*(np.outer(np.sum(W0,1),np.sum(W0,0)))/s0

        W1 =-W*(W<0)                          
        s1 = np.sum(W1)
        if s1:
            B1 = W1-gamma*(np.outer(np.sum(W1,1),np.sum(W1,0)))/s1
        else:
            B1 = 0

    elif np.min(W)<-1e-10:
        raise ValueError('The input connection matrix contains negative weights. '
                         'Specify "negative_sym" or "negative_asym" objective-function types.')

    if B == 'potts' and (W.astype(np.float32) != W.astype(bool).astype(np.float32)).any():
        raise ValueError('Potts-model Hamiltonian requires a binary W.')

    elif B == 'modularity':
        B = (W-gamma*np.outer(np.sum(W,1),np.sum(W,0))/s)/s

    elif B == 'potts':
        B = W-gamma*(1-W)
        
    elif B == 'negative_sym':
        B = B0/(s0+s1) - B1/(s0+s1)

    elif B == 'negative_asym':
        B = B0/s0 - B1/(s0+s1)
    else:
        raise ValueError('B type should be one of ["modularity", "potts", "negative_sym", "negative_asym"].')

    if M0 is None:
        M0 = np.arange(n)

    elif np.size(M0) != n:
        raise ValueError('M0 vector must contain n elements.')

    _, Mb = np.unique(M0.T, return_inverse=True)

    M = Mb.copy()

    B = (B+B.T)/2
    Hnm = np.zeros((n,n))
    for m in range(np.max(Mb)+1):
        Hnm[:,m] = np.sum(B[:, Mb==m], 1)

    Q0 = -np.inf
    ss = np.zeros((len(M0),len(M0))).astype(bool)
    for ii in range(len(M0)):
        for jj in range(len(M0)):
            ss[ii,jj] = M0[ii]==M0[jj]
    Q = np.sum(B[ss])

    first_iter = True
    while (Q-Q0)>1e-10:
        flag = True
        while flag:
            flag=False
            for u in np.random.permutation(np.arange(n)):
            #for u in np.arange(n):
                ma = Mb[u]
                dQ = Hnm[u,:] - Hnm[u, ma] + B[u,u]
                dQ[ma] = 0
                max_dq = np.max(dQ)
                mb = np.argmax(dQ)
                if max_dq > 1e-10:
                    flag=True
                    Mb[u] = mb
                    Hnm[:,mb] = Hnm[:,mb] + B[:,u]
                    Hnm[:,ma] = Hnm[:,ma] - B[:,u]

        _, Mb = np.unique(Mb.T, return_inverse=True)
        M0 = M.copy()
        if first_iter:
            M = Mb.copy()
            first_iter = False
        else:
            for u in range(n):
                M[M0==u] = Mb[u]
        n = np.max(Mb)+1
        B1 = np.zeros((n,n))
        for u in range(n):
            for v in range(u,n):
                bm = np.sum(B[np.ix_(Mb==u, Mb==v)])
                B1[u,v] = bm
                B1[v,u] = bm

        B = B1.copy()
        Mb = np.arange(n)
        Hnm = B.copy()

        Q0 = Q.copy()
        Q = np.trace(B)

    return M, Q    



def participation_coef (W, Ci):

#PARTICIPATION_COEF     Participation coefficient
#
#   P = participation_coef(W,Ci);
#
#   Participation coefficient is a measure of diversity of intermodular
#   connections of individual nodes.
#
#   Inputs:     W,      binary/weighted, directed/undirected connection matrix
#               Ci,     community affiliation vector
#
#   Output:     P,      participation coefficient
#
#   Note: The output for directed graphs is the "out-neighbor"
#         participation coefficient.
#
#   Reference: Guimera R, Amaral L. Nature (2005) 433:895-900.
#
#
#   2008-2011
#   Mika Rubinov, UNSW
#   Alex Fornito, University of Melbourne

#   Modification History:
#   Jul 2008: Original (Mika Rubinov)
#   Mar 2011: Weighted-network bug fixes (Alex Fornito)


    n = W.shape[0]
    Ko = np.sum(W, axis=1)
    aa = (W!=0).astype(int)
    Gc = np.matmul(aa , np.diag(Ci.squeeze()))
    Kc2 = np.zeros(n)
    for i in range(1, np.max(Ci)+1):
        Kc2 = Kc2 + (np.sum(W * (Gc==i).astype(int), axis=1) ** 2)

    P = np.ones(n) - (Kc2 / (Ko ** 2))
    P[Ko == 0] = 0

    return P

        
