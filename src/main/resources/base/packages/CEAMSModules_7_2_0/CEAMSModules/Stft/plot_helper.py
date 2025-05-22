"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Library helper for plotting data.
"""
import matplotlib.ticker as mticker
import numpy as np

def draw_spectogram(axis, psd, freq_bins, win_len, win_step, scale='log', \
    ylim=None, show_colorbar=False, fig=None):
        """
        Draw a spectogram on an axis given in parameter.

        Arguments
            axis:           The plot axis
            psd:            The power spectrum density data (2D array)
                            x array is the time, y array is the frequency
            freq_bins:      An array of all frequency bins
            win_len:        Window length in sec (how much data is taken for each fft)
            win_step:       Window step in sec (each time the fft is applied)
            scale:          Y axis scaling
            ylim:           Y limits (min, max)
            show_colorbar:  Show the color bar on the side of the spectrogram or not
            fig:            The figure where to show the colorbar. Must be set if
                            show_colorbar True

        return
            None
        """
        # Get the STD of the data to sue for the colormap limits
        std = np.std(psd.flatten())
        
        # Generate the X and Y tickers
        #seconds = psd.shape[-1]*win_len
        seconds = (psd.shape[-1]-1)*win_step+win_len

        x = np.linspace(0, seconds, psd.shape[1], endpoint=False)
        y = np.linspace(0, freq_bins[-1], psd.shape[0], endpoint=True)

        # Set the scales and limits
        axis.set_yscale(scale)
        if ylim:
            axis.set_ylim(ylim)
        else:
            axis.set_ylim(0.5, y[-1])

        # Draw the spectogram
        im = axis.pcolormesh(x,y,psd)

        if show_colorbar:
            cmap = fig.colorbar(im)
            cmap.set_label('$µV^2$')
            cmap.mappable.set_clim(0,std*2)

        # Format the X and Y axis ticker
        # Format secondes in HH:MM:SS format
        def fmtsec(x,pos):
            hours = int(x / 60 / 60)
            mins = int((x - hours*60*60) / 60)
            seconds = int(x % 60)
            return "{:02d}:{:02d}:{:02d}".format(hours,mins,seconds)
        axis.xaxis.set_major_formatter(mticker.FuncFormatter(fmtsec))
        for label in axis.get_xticklabels():
            label.set_ha("right")
            label.set_rotation(45)

        formatter = mticker.ScalarFormatter()
        formatter.set_scientific(False)
        axis.yaxis.set_major_formatter(formatter)
        axis.yaxis.set_minor_formatter(formatter)
        axis.tick_params(axis='y', which='minor', labelsize=8)
        
        # Set labels and title
        axis.set_xlabel('Time (HH:MM:SS)')
        axis.set_ylabel('Hz')
        axis.set_title(f'Spectrogram')