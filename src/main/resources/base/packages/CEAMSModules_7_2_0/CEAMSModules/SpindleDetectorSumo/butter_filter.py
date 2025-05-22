import numpy as np
from scipy.signal import butter, resample_poly, sosfiltfilt
from fractions import Fraction

def butter_bandpass_filter_nan(data, lowcut, highcut, sample_rate, order):
    """
    Bandpass filter the data using Butterworth IIR filters, handling NaNs via interpolation.

    Parameters
    ----------
    data : ndarray
        The data to be filtered; format (n_samples,)
    lowcut : float
        The lower critical frequency
    highcut : float
        The higher critical frequency
    sample_rate : float
        The sampling rate of the given data
    order : int
        The order of the used filters

    Returns
    -------
    data : ndarray
        The bandpass filtered data; format (n_samples,)
    """

    # Identify NaN indices
    nan_mask = np.isnan(data)

    # Interpolate NaNs before filtering
    if np.any(nan_mask):
        data = np.copy(data)
        data[nan_mask] = np.interp(
            np.flatnonzero(nan_mask), np.flatnonzero(~nan_mask), data[~nan_mask]
        )

    sos_high = butter(order, lowcut, btype='hp', fs=sample_rate, output='sos')
    sos_low = butter(order, highcut, btype='lp', fs=sample_rate, output='sos')

    filtered_data = sosfiltfilt(sos_low, sosfiltfilt(sos_high, data, padlen=3 * order), padlen=3 * order)

    # Restore original NaN values
    filtered_data[nan_mask] = np.nan

    return filtered_data



def butter_bandpass_filter(data, lowcut, highcut, sample_rate, order):
    """
    Bandpass filter the data using Butterworth IIR filters.

    Two digital Butterworth IIR filters with the specified order are created, one highpass filter for the lower critical
    frequency and one lowpass filter for the higher critical frequency. Both filters use second-order sections (SOS).
    Then first the highpass filter is applied on the given data and on its result the lowpass filter is applied.
    Both filters are applied as forward-backward digital filters to correct the non-linear phase.

    Parameters
    ----------
    data : ndarray
        The data to be filtered; format (n_samples,)
    lowcut : float
        The lower critical frequency
    highcut : float
        The higher critical frequency
    sample_rate : float
        The sampling rate of the given data
    order : int
        The order of the used filters

    Returns
    -------
    data : ndarray
        the bandpass filtered data; format (n_samples,)
    """

    sos_high = butter(order, lowcut, btype='hp', fs=sample_rate, output='sos')
    sos_low = butter(order, highcut, btype='lp', fs=sample_rate, output='sos')
    return sosfiltfilt(sos_low, sosfiltfilt(sos_high, data, padlen=3 * order), padlen=3 * order)


def downsample(data, sample_rate, resampling_frequency):
    """
    Downsample the given data to a target frequency.

    Uses the scipy resample_poly function to transform the data from the original sample_rate to resampling_frequency.

    Parameters
    ----------
    data : ndarray
        The data to be downsampled; format (n_samples,)
    sample_rate : int or float
        The original sample rate of data
    resampling_frequency : int or float
        The target sample rate to transform data into, must not be higher than sample_rate

    Returns
    -------
    data : ndarray
        The downsampled data; format (n_samples_new,)
    """

    # original code
    # if (sample_rate != int(sample_rate)) | (resampling_frequency != int(resampling_frequency)):
    #     raise Exception('parameters "sample_rate" and "resampling_frequency" have to be integers')
    # elif sample_rate < resampling_frequency:
    #     raise Exception('the original sample frequency must not be lower than the resample frequency')
    # elif sample_rate == resampling_frequency:
    #     return data
    # sample_rate = int(sample_rate)
    # resampling_frequency = int(resampling_frequency)
    # gcd = np.gcd(sample_rate, resampling_frequency)
    # up = resampling_frequency // gcd
    # down = sample_rate // gcd

    # my code (to accept non-integer sample rates)
    if sample_rate < resampling_frequency:
        raise ValueError('The original sample frequency must not be lower than the resample frequency')
    elif sample_rate == resampling_frequency:
        return data
    # Compute rational approximation
    ratio = Fraction.from_float(resampling_frequency / sample_rate).limit_denominator(1000)  # Adjust limit if needed
    up, down = ratio.numerator, ratio.denominator

    return resample_poly(data, up, down)
