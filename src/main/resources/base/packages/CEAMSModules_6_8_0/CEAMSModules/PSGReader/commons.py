"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
# To save the PSGReaderManager in order to reference it in PSGReader and PSGWriter
# This was needed to avoid classmethod in PSGReaderManager
psg_reader_manager = []

# Dictionary of sleep stages label to use in scinode
sleep_stages_name = {
    "W":'0',
    "N1":'1',
    "N2":'2',
    "N3":'3',
    "N4":'4',
    "R":'5',
    "movement":'6',
    "tech":'7',
    "unscored":'8',
    "undefined":'9'
}

# The event group for sleep stages
sleep_stages_group = "stage"

# The event group for sleep cycle
sleep_cycle_group = "cycle" # also the event name
# The event group for NREM period
nrem_period_group = "nremp" # also the event name
# The event group for REM period
rem_period_group = "remp" # also the event name

nremp_stages_with_n1 = ['1', '2', '3', '4']
nremp_stages_without_n1 = ['2', '3', '4']

class Units:
    metric = 'metric'
    imperial = 'imperial'

class Sex:
    male = 'M'
    female = 'F'
    unknown = 'X'

# list of asleep stage
asleep_stages = ['1', '2', '3', '4', '5']
# list of valid stages to compute the sleep onset
valid_stage = ['0', '1', '2', '3', '4', '5']

# list of repiratory events to look for match pattern
# not used yet
respiratory_evt_lst = ["respiratoires", "apnee", "hypop", "ap-central", "ap-obstruct", "ap-mixte"]