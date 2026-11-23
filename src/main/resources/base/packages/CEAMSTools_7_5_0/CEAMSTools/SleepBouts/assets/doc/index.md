# Sleep Bouts

This tool detects sleep bouts from PSG files.

## What is a sleep bout?

Sleep bouts are defined as continuous periods of sleep stages. This tool detects three types of sleep bouts:

1. Continuous period of **N2** and **N3** stages
2. Continuous period of **N2**, **N3** and **REM** stages
3. Continuous period of **REM** stage

![](assets/20230206_115524_sleep_bouts.png)

## Output file

The output is a CSV (Comma separated Values) file. A new row is added for every file analyzed. The columns of the file are as follows:

- The name of the PSG file
- The ten longest sleep bouts of type 1
- The mean value of all sleep bouts of type 1
- The standard deviation value of all sleep bouts of type 1
- Repeat for type 2 and 3.
