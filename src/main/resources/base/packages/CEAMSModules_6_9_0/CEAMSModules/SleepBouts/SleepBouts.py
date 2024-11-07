"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Inputs:
        sleep_stages
        output_filename

"""

import os

from flowpipe import SciNode, InputPlug
import csv
import statistics as stat
import os.path

DEBUG = False

class SleepBouts(SciNode):
    """
        SleepBouts
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('SleepBouts.__init__')
        InputPlug('input_filename', self)
        InputPlug('sleep_stages', self)
        InputPlug('output_filename', self)
        InputPlug('export_in_seconds', self)

    def __del__(self):
        if DEBUG: print('SleepBouts.__del__')

    def subscribe_topics(self):
        pass

    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'SleepBouts.on_topic_update {topic}:{message}')

    def compute(self, input_filename, sleep_stages, output_filename, export_in_seconds):
        """
            enum EPSGSleepStage	//	Stades de sommeil
            {	StageWake = 0,
                StageN1 = 1,
                StageN2 = 2,
                StageN3 = 3,
                Stage3 = 3,		//	Rechtschaffen and Kales (R&K, 1968)
                Stage4 = 4,		//	Rechtschaffen and Kales (R&K, 1968)
                StageREM = 5,
                StageMT = 6,
                StageND = 9,
            };

        """
        if DEBUG: print('SleepBouts.compute')
        if not sleep_stages.empty:

            stages = sleep_stages.name.to_list()
            
            n2_n3_all = self.find_stages_bouts(stages, ['2', '3', '4'])
            n2_n3_rem_all = self.find_stages_bouts(stages, ['2', '3', '4', '5'])
            rem_all = self.find_stages_bouts(stages, ['5'])

            if export_in_seconds == "1":
                epoch_length = int(round(sleep_stages.duration_sec.to_list()[0]))
                n2_n3_all = [epoch_count * epoch_length for epoch_count in n2_n3_all]
                n2_n3_rem_all = [epoch_count * epoch_length for epoch_count in n2_n3_rem_all]
                rem_all = [epoch_count * epoch_length for epoch_count in rem_all]

            columns = 10
            n2_n3 = sorted(n2_n3_all, reverse=True)[0:columns]
            n2_n3_rem = sorted(n2_n3_rem_all, reverse=True)[0:columns]
            rem = sorted(rem_all, reverse=True)[0:columns]

            n2_n3 = n2_n3 + [0]*(columns - len(n2_n3))
            n2_n3_rem = n2_n3_rem + [0]*(columns - len(n2_n3_rem))
            rem = rem + [0]*(columns - len(rem))

            if len(n2_n3_all) > 0:
                n2_n3.append(stat.mean(n2_n3_all))
                n2_n3.append(stat.stdev(n2_n3_all) if len(n2_n3_all) > 1 else 0)
            else:
                n2_n3.append(0)
                n2_n3.append(0)

            if len(n2_n3_rem_all) > 0:
                n2_n3_rem.append(stat.mean(n2_n3_rem_all))
                n2_n3_rem.append(stat.stdev(n2_n3_rem_all) if len(n2_n3_rem_all) > 1 else 0)
            else:
                n2_n3_rem.append(0)
                n2_n3_rem.append(0)

            if len(rem_all) > 0:
                rem.append(stat.mean(rem_all))
                rem.append(stat.stdev(rem_all) if len(rem_all) > 1 else 0)
            else:
                rem.append(0)
                rem.append(0)

            n2_n3_names = [f'N2_N3_{i+1}' for i in range(columns) ]
            n2_n3_names.append('N2_N3_mean')
            n2_n3_names.append('N2_N3_std')

            n2_n3_rem_names = [f'N2_N3_R_{i+1}' for i in range(columns) ]
            n2_n3_rem_names.append('N2_N3_R_mean')
            n2_n3_rem_names.append('N2_N3_R_std')

            rem_names = [f'R_{i+1}' for i in range(columns) ]
            rem_names.append('R_mean')
            rem_names.append('R_std')
            
            fieldnames = ["filename"] + n2_n3_names + n2_n3_rem_names + rem_names

            if not os.path.isfile(output_filename):
                with open(output_filename, 'w+', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',')
                    writer.writerow(fieldnames)

            with open(output_filename, 'a+', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                row = {}
                row["filename"] = input_filename
                for idx, n2_n3_name in enumerate(n2_n3_names):
                    row[n2_n3_name] = n2_n3[idx]
                for idx, n2_n3_rem_name in enumerate(n2_n3_rem_names):
                    row[n2_n3_rem_name] = n2_n3_rem[idx]
                for idx, rem_name in enumerate(rem_names):
                    row[rem_name] = rem[idx]
                
                writer.writerow(row)

        return
        
    def find_stages_bouts(self, stages, target_stages):
        bouts = []
        count = -1
        idx = 0
        for stage in stages:
            if stage in target_stages:
                if count == -1:
                    count = 1
                else:
                    count = count + 1
            else:
                if count != -1:
                    bouts.append(count)
                    #print(f'idx:{idx} time:{idx * 30} count:{count}')
                    count = -1
            idx = idx + 1
        return bouts