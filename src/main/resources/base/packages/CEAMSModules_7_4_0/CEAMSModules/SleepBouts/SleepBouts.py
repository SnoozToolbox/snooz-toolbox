"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Inputs:
        sleep_stages
        output_filename

"""


import csv
import numpy as np
import os
import os.path
import pandas as pd

from flowpipe import SciNode, InputPlug
from commons.NodeRuntimeException import NodeRuntimeException

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
            
            # Variables with all the continuous bouts
            n2_n3_all = self.find_stages_bouts(stages, ['2', '3', '4'])
            n2_n3_rem_all = self.find_stages_bouts(stages, ['2', '3', '4', '5'])
            rem_all = self.find_stages_bouts(stages, ['5'])

            # Convert the duration in ecpoch into seconds
            if export_in_seconds == "1":
                epoch_length = int(round(sleep_stages.duration_sec.to_list()[0]))
                n2_n3_all = [epoch_count * epoch_length for epoch_count in n2_n3_all]
                n2_n3_rem_all = [epoch_count * epoch_length for epoch_count in n2_n3_rem_all]
                rem_all = [epoch_count * epoch_length for epoch_count in rem_all]

            # Keep only the 10 longest bouts (maximum) sorted from longest to shortest
            N_COLUMNS = 10
            n2_n3 = sorted(n2_n3_all, reverse=True)[0:N_COLUMNS]
            n2_n3_rem = sorted(n2_n3_rem_all, reverse=True)[0:N_COLUMNS]
            rem = sorted(rem_all, reverse=True)[0:N_COLUMNS]

            # Add missing values as NaN to keep the cell empty (not to zero)
            n2_n3 = n2_n3 + [np.nan]*(N_COLUMNS - len(n2_n3))
            n2_n3_rem = n2_n3_rem + [np.nan]*(N_COLUMNS - len(n2_n3_rem))
            rem = rem + [np.nan]*(N_COLUMNS - len(rem))

            # Compute the mean and standard deviation for the 10 longest bouts
            if np.sum(~np.isnan(n2_n3)) > 0:
                n2_n3_mean = np.nanmean(n2_n3)
                n2_n3_std = np.nanstd(n2_n3) if np.sum(~np.isnan(n2_n3)) > 2 else np.nan
                n2_n3.append(n2_n3_mean)
                n2_n3.append(n2_n3_std)                
            else:
                n2_n3.append(np.nan)
                n2_n3.append(np.nan)

            if np.sum(~np.isnan(n2_n3_rem)) > 0:
                n2_n3_rem_mean = np.nanmean(n2_n3_rem)
                n2_n3_rem_std = np.nanstd(n2_n3_rem) if np.sum(~np.isnan(n2_n3_rem)) > 2 else np.nan
                n2_n3_rem.append(n2_n3_rem_mean)
                n2_n3_rem.append(n2_n3_rem_std)
            else:
                n2_n3_rem.append(np.nan)
                n2_n3_rem.append(np.nan)

            if np.sum(~np.isnan(rem))> 0:
                rem_mean = np.nanmean(rem)
                rem_std = np.nanstd(rem) if np.sum(~np.isnan(rem)) > 2 else np.nan
                rem.append(rem_mean)
                rem.append(rem_std)
            else:
                rem.append(np.nan)
                rem.append(np.nan)

            # Compute the mean and standard deviation for all the bouts
            if np.sum(~np.isnan(n2_n3_all)) > 0:
                n2_n3.append(np.nanmean(n2_n3_all))
                n2_n3.append(np.nanstd(n2_n3_all) if np.sum(~np.isnan(n2_n3_all)) > 2 else np.nan)
            else:
                n2_n3.append(np.nan)
                n2_n3.append(np.nan)

            if np.sum(~np.isnan(n2_n3_rem_all)) > 0:
                n2_n3_rem.append(np.nanmean(n2_n3_rem_all))
                n2_n3_rem.append(np.nanstd(n2_n3_rem_all) if np.sum(~np.isnan(n2_n3_rem_all)) > 2 else np.nan)
            else:
                n2_n3_rem.append(np.nan)
                n2_n3_rem.append(np.nan)

            if np.sum(~np.isnan(rem_all)) > 0:
                rem.append(np.nanmean(rem_all))
                rem.append(np.nanstd(rem_all) if np.sum(~np.isnan(rem_all)) > 2 else np.nan)
            else:
                rem.append(np.nan)
                rem.append(np.nan)

            # Create the column names
            n2_n3_names = [f'N2_N3_{i+1}' for i in range(N_COLUMNS) ]
            n2_n3_names.append('N2_N3_1_10_mean')
            n2_n3_names.append('N2_N3_1_10_std')
            n2_n3_names.append('N2_N3_mean')
            n2_n3_names.append('N2_N3_std')

            n2_n3_rem_names = [f'N2_N3_R_{i+1}' for i in range(N_COLUMNS) ]
            n2_n3_rem_names.append('N2_N3_R_1_10_mean')
            n2_n3_rem_names.append('N2_N3_R_1_10_std')
            n2_n3_rem_names.append('N2_N3_R_mean')
            n2_n3_rem_names.append('N2_N3_R_std')

            rem_names = [f'R_{i+1}' for i in range(N_COLUMNS) ]
            rem_names.append('R_1_10_mean')
            rem_names.append('R_1_10_std')
            rem_names.append('R_mean')
            rem_names.append('R_std')
            
            fieldnames = ["filename"] + n2_n3_names + n2_n3_rem_names + rem_names

            # Create a pandas data frame
            bouts_df = pd.DataFrame(columns=fieldnames)
        
            # Add the data to the data frame
            bouts_df['filename'] = [input_filename]
            bouts_df[n2_n3_names] = n2_n3
            bouts_df[n2_n3_rem_names] = n2_n3_rem
            bouts_df[rem_names] = rem

            # Write the current report for the current subject into the tsv file
            write_header = not os.path.exists(output_filename)
            try: 
                bouts_df.to_csv(path_or_buf=output_filename, sep='\t', \
                    index=False, mode='a', header=write_header, encoding="utf_8")
            except:
                raise NodeRuntimeException(self.identifier, "PSA", 
                f"ERROR : Snooz can not write in the file {output_filename}. Check if the drive is accessible and ensure the file is not already open.")               
        # To write the info text file to describe the variable names
        if write_header:
            # Write the documentation file
            file_name, file_extension = os.path.splitext(output_filename)
            doc_filepath = file_name+"_info"+file_extension
            if not os.path.exists(doc_filepath):
                try:
                    self.write_doc_file(doc_filepath,N_COLUMNS)
                    # Log message for the Logs tab
                    self._log_manager.log(self.identifier, f"The file {doc_filepath} has been created.")
                except:
                    raise NodeRuntimeException(self.identifier, "Sleep bouts", f"ERROR : Snooz can not write in the file {doc_filepath}. Check if the drive is accessible and ensure the file is not already open.")    
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


    def _get_doc(self,N_COLUMNS):
        general_dict = \
        {
            'filename' : 'PSG filename',
        }
        N2_N3 = {}
        for i_column in range(N_COLUMNS):
            if i_column == 0:
                N2_N3_1_dict = \
                    {f'N2_N3_{i_column+1}' : f'The 1st longest bout of N2 or N3 sleep.'}
                N2_N3 = N2_N3_1_dict
            elif i_column == 1:
                N2_N3_2_dict = \
                    {f'N2_N3_{i_column+1}' : f'The 2sd longest bout of N2 or N3 sleep.'}
                N2_N3= N2_N3 | N2_N3_2_dict
            elif i_column == 2:
                N2_N3_3_dict = \
                    {f'N2_N3_{i_column+1}' : f'The 3rd longest bout of N2 or N3 sleep.'}
                N2_N3= N2_N3 | N2_N3_3_dict         
            else:
                new_dict = \
                    {f'N2_N3_{i_column+1}' : f'The {i_column+1}th longest bout of N2 or N3 sleep.'}
                N2_N3 = N2_N3 | new_dict

        N2_N3_stats = \
            {
                'N2_N3_1_10_mean' : 'The mean of the 1st 10 longest bouts of N2 or N3 sleep.',
                'N2_N3_1_10_std' : 'The standard deviation of the 1st 10 longest bouts of N2 or N3 sleep.',
                'N2_N3_mean' : 'The mean of the bouts of N2 or N3 sleep.',
                'N2_N3_std' : 'The standard deviation of the longest bouts of N2 or N3 sleep.',
            }

        # Define the dictionary for the N2 N3 R bouts
        N2_N3_R = {}
        for i_column in range(N_COLUMNS):
            if i_column == 0:
                N2_N3_R_1_dict = \
                    {f'N2_N3_R_{i_column+1}' : f'The 1st longest bout of N2, N3 and REM sleep.'}
                N2_N3_R = N2_N3_R_1_dict
            elif i_column == 1:
                N2_N3_R_2_dict = \
                    {f'N2_N3_R_{i_column+1}' : f'The 2sd longest bout of N2, N3 and REM sleep.'}
                N2_N3_R= N2_N3_R | N2_N3_R_2_dict
            elif i_column == 2:
                N2_N3_R_3_dict = \
                    {f'N2_N3_R_{i_column+1}' : f'The 3rd longest bout of N2, N3 and REM sleep.'}
                N2_N3_R= N2_N3_R | N2_N3_R_3_dict         
            else:
                new_dict = \
                    {f'N2_N3_R_{i_column+1}' : f'The {i_column+1}th longest bout of N2, N3 and REM sleep.'}
                N2_N3_R = N2_N3_R | new_dict

        N2_N3_R_stats = \
            {
                'N2_N3_R_1_10_mean' : 'The mean of the 1st 10 longest bouts of N2, N3 and REM sleep.',
                'N2_N3_R_1_10_std' : 'The standard deviation of the 1st 10 longest bouts of N2, N3 and REM sleep.',
                'N2_N3_R_mean' : 'The mean of the bouts of N2, N3 and REM sleep.',
                'N2_N3_R_std' : 'The standard deviation of the longest bouts of N2, N3 and REM sleep.',
            }
        
        # Define the dictionary for the R bouts according to the number of N_COLUMNS
        R_dict = {}
        for i_column in range(N_COLUMNS):
            if i_column == 0:
                R_1_dict = \
                    {f'R_{i_column+1}' : f'The 1st longest bout of REM sleep.'}
                R_dict = R_1_dict
            elif i_column == 1:
                R_2_dict = \
                    {f'R_{i_column+1}' : f'The 2sd longest bout of REM sleep.'}
                R_dict= R_dict | R_2_dict
            elif i_column == 2:
                R_3_dict = \
                    {f'R_{i_column+1}' : f'The 3rd longest bout of REM sleep.'}
                R_dict= R_dict | R_3_dict         
            else:
                new_dict = \
                    {f'R_{i_column+1}' : f'The {i_column+1}th longest bout of REM sleep.'}
                R_dict = R_dict | new_dict
        R_stats = \
            {
                'R_1_10_mean' : 'The mean of the 1st 10 longest bouts of REM sleep.',
                'R_1_10_std' : 'The standard deviation of the 1st 10 longest bouts of REM sleep.',
                'R_mean' : 'The mean of the bouts of REM sleep.',
                'R_std' : 'The standard deviation of the longest bouts of REM sleep.',
            }

        complete_dict = general_dict | N2_N3 | N2_N3_stats | N2_N3_R | N2_N3_R_stats | R_dict | R_stats
        return complete_dict      


    def write_doc_file(self, filepath, N_COLUMNS):
        """
        Write the documentation of the CSV file into a file.
        
        The documentation is written in a tab separated file with three N_COLUMNS.
        The first column is the Excel column name, the second column is the variable name 
        and the third column is the description of the variable.
            The path to the file to write.
        """
    
        filepath : str


        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            docwriter = csv.writer(csvfile, delimiter='\t')
            doc = self._get_doc(N_COLUMNS)
            for i, (k, v) in enumerate(doc.items()):
                row_name = self.excel_column_name(i+1)
                docwriter.writerow([row_name,k,v])


    def excel_column_name(self, number):
        column_name = ""
        while number > 0:
            remainder = (number - 1) % 26  # Subtract 1 to account for 0-based indexing
            column_name = chr(65 + remainder) + column_name  # 65 is the ASCII code for 'A'
            number = (number - 1) // 26
        return column_name
  