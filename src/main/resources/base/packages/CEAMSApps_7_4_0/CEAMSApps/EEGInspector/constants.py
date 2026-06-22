"""Constants and configuration for EEG Inspector"""

# Signal processing constants
FILTER_ORDER = 15
TARGET_RATE_HIGH = 256
TARGET_RATE_LOW = 200
SCALE_FACTOR_UV = 1e-6
LOWPASS_CUTOFF_HZ = 100

# Recording duration thresholds
SLEEP_RECORDING_THRESHOLD_SEC = 3600 # duration to decide if it is sleep or coma data

# DATA duration display to reject bad channel
PLOT_COMA_DURATION_SEC = 20          # duration plot for coma to select bad channel
# The whole recording is displayed for sleep data

# Data display optimization constants
DECIMATION_FACTOR_NONE = 1     # Base decimation factor for coma data
DECIMATION_FACTOR_WHOLE_REC = 103   # Decimation factor to display the whole recording for sleep data

# Epoch durations in seconds to remove bad epochs
EPOCH_SLEEP_LONG_SEC = 3600         # 1 h, all epochs are displayed 
EPOCH_SLEEP_SHORT_SEC = 1200        # 20 minutes, all epochs are displayed
EPOCH_SLEEP_DURATIONS = [EPOCH_SLEEP_LONG_SEC, EPOCH_SLEEP_SHORT_SEC]

EPOCH_SLEEP_SHORT_CHAR = '20'    # 20 minutes in text to display in the combo box
EPOCH_SLEEP_LONG_CHAR = '60'     # 60 minutes in text to display in the combo box
EPOCH_SLEEP_STAGE_SEC = 30          # 30 seconds for sleep staging

EPOCH_COMA_SHORT_SEC = 10           # 10 seconds
EPOCH_COMA_SHORT_CHAR = '10'         # 10 seconds in text to display in the combo box
EPOCH_COMA_LONG_SEC = 30            # 30 seconds
EPOCH_COMA_DURATIONS = [EPOCH_COMA_LONG_SEC, EPOCH_COMA_SHORT_SEC]

# Display settings
DEFAULT_N_CHANNELS = 30     # Number of channels to display when rejecting bad channels (without scrolling)
EPOCH_N_CHANNELS = 10       # Number of channels to display when rejecting bad epochs (without scrolling)

N_EPOCH_DISPLAY_COMA_SHORT = 3
N_EPOCH_DISPLAY_COMA_LONG = 2
PSD_FMAX_HZ = 62

# Popup window size settings for epoch detail view
EPOCH_POPUP_FIGURE_SIZE = (12, 8)  # Width, Height in inches for the popup figure

# Memory management settings
ENABLE_AUTOMATIC_MEMORY_CLEANUP = True     # Enable automatic memory cleanup
MAX_POPUP_FIGURES = 5                      # Maximum number of popup figures to keep open

# Plot scaling settings
PLOT_SCALES_SLEEP = {
    'mag': 1e-12, 'grad': 4e-11, 'eeg': 100e-6, 'eog': 150e-6, 'ecg': 5e-4,
    'emg': 1e-3, 'ref_meg': 1e-12, 'misc': 1e-3, 'stim': 1,
    'resp': 1, 'chpi': 1e-4, 'whitened': 1e2
}

PLOT_SCALES_COMA = {
    'mag': 1e-12, 'grad': 4e-11, 'eeg': 60e-6, 'eog': 150e-6, 'ecg': 5e-4,
    'emg': 1e-3, 'ref_meg': 1e-12, 'misc': 1e-3, 'stim': 1,
    'resp': 1, 'chpi': 1e-4, 'whitened': 1e2
}

# Montage-specific non-brain channels
GSN_HYDRO_129_NON_BRAIN_CHANNELS = [
    'E127', 'E126', 'E17', 'E21', 'E14', 'E25', 'E8', 'E128', 'E125', 'E43', 'E120', 'E48', 
    'E119', 'E49', 'E113', 'E81', 'E73', 'E88', 'E68', 'E94', 'E63', 'E99', 'E56', 'E107',
    'EEG 127', 'EEG 126', 'EEG 17', 'EEG 21', 'EEG 14', 'EEG 25', 'EEG 8', 'EEG 128', 
    'EEG 125', 'EEG 43', 'EEG 120', 'EEG 48', 'EEG 119', 'EEG 49', 'EEG 113', 'EEG 81', 
    'EEG 73', 'EEG 88', 'EEG 68', 'EEG 94', 'EEG 63', 'EEG 99', 'EEG 56', 'EEG 107'
]

# Non-brain channel keywords for automatic detection
NON_BRAIN_CHANNEL_KEYWORDS = [
    'eog', 'emg', 'ecg', 'cardiac', 'ekg', 'spo2', 'resp', 'sao2', 'loc', 'roc',
    'status', 'vref', 'eeg 129', 'e129', 'e1001', 'vertex reference', 'airflow',
    'thor', 'abdo', 'position', 'light', 'ox stat', 'pr', 'rat', 'lat',
    'the', 'snor', 'pulse', 'heart', 'canule', 'body', 'mic', 'sangle', 'sanmixte','tag','tad', 'dii'
]

# Event annotation constants
EVENT_GROUP_NAME = 'art_inspector'
EVENT_NAME_NON_BRAIN = 'non_brain'
EVENT_NAME_BAD_CHANNEL = 'art_channel'
EVENT_NAME_BAD_EPOCH = 'art_epoch'

# Montage name constant
GSN_HYDRO_129_MONTAGE_NAME = 'GSN-HydroCel-129'