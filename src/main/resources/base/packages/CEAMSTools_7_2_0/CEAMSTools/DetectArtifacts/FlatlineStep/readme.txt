# Last line of Ui_MuscularStep must be
from . import muscular_res

# background scinode
50 50 50


The power is log10 transformed to make the data normally distributed. The threshold is based on the mode of the histogram (nbins=50) of the power of all selected channels.\nAn artifact is identified when the log10(power) < (mode+threshold*abs(mode))