"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
   To read the PSA output file generated from Tool-> Sleep analysis -> PSA and
    generate the PSA file clean or transposed.
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

from io import StringIO
import numpy as np
import os
import pandas as pd

DEBUG = True

class DetectionsCohortReview(SciNode):
    """
    Class to read the spindle/sw output files and generate the "Detected events cohort report" file clean or transposed.
    
    Inputs:
        "filenames": List of String
            List of filename (including path) to the PSA output file.
        "subject_chans_label" : dict
            Keys are the subjects
            Each item is a list of 3 elements [original chan label, modified chan label, bool selection flag]
        "ROIs_cohort" : dict
            Dict to manage the ROI created at the cohort level
            keys are ROIs labels
            Each item is a list of 2 elements [channel list to average, blank flag]
        "ROIs_subjects" : dict
            Dict to manage the ROI at the subject level
            keys are the subjects
            Each item is a list of n_ROIs with its selection label  [ROI#1 label, bool selection flag]
                                                                    [ROI#2 label, bool selection flag]
                                                                                ...
        "activity_label" : string
            The activity variable to export/save i.e. 'Total' or 'distribution per sleep cycle'.        
        "clean_flag" : bool
            Flag to generate and save the output file with only selected channels.
        "transposed_flag" : bool
            Flag to generate and save the transposed file (1 subject per row)
        "output_file" : string
            Output path to save the file clean and/or transposed.

    Outputs:
        "out_df": pandas DataFrame
                Detection events data converted into a dataframe with modifications applied. 
        
    """
    def __init__(self, **kwargs):
        """ Initialize module DetectionsCohortReview """
        super().__init__(**kwargs)
        if DEBUG: print('SleepReport.__init__')

        # Input plugs
        InputPlug('filenames',self)
        InputPlug('subject_chans_label',self)
        InputPlug('ROIs_cohort',self)
        InputPlug('ROIs_subjects',self)
        InputPlug('activity_label',self)
        InputPlug('clean_flag',self)
        InputPlug('transposed_flag',self)
        InputPlug('output_file',self)
        
        # Output plugs
        OutputPlug('out_df',self)

        # A master module allows the process to be reexcuted multiple time.
        self._is_master = False 

        # To save the detection info from the list of filenames
        self.df_data = pd.DataFrame()
        self.clean_filename = "_clean"
        self.transposed_filename = "_transposed"
        self.labels_to_extract = ['filename', 'chan_label']


    def compute(self, filenames, subject_chans_label, ROIs_cohort, ROIs_subjects, activity_label, clean_flag, transposed_flag, output_file):
        """
        To read the spindle/sw output files and generate the "Detected events cohort report" file clean or transposed.
        
        Inputs:
            "filenames": List of String
                List of filename (including path) to the PSA output file.
            "subject_chans_label" : dict
                Keys are the subjects
                Each item is a list of 3 elements [original chan label, modified chan label, bool selection flag]
            "ROIs_cohort" : dict
                Dict to manage the ROI created at the cohort level
                keys are ROIs labels
                Each item is a list of 2 elements [channel list to average, blank flag]
            "ROIs_subjects" : dict
                Dict to manage the ROI at the subject level
                keys are the subjects
                Each item is a list of n_ROIs with its selection label  [ROI#1 label, bool selection flag]
                                                                        [ROI#2 label, bool selection flag]
                                                                                    ...
            "activity_label" : string
                The activity variable to export/save i.e. 'Total' or 'distribution per sleep cycle'.        
            "clean_flag" : bool
                Flag to generate and save the output file with only selected channels.
            "transposed_flag" : bool
                Flag to generate and save the transposed file (1 subject per row)
            "output_file" : string
                Output path to save the file clean and/or transposed.

        Outputs:
            "out_df": pandas DataFrame
                    Detection events data converted into a dataframe with modifications applied. 
        
        """
        transposed_flag = int(transposed_flag) 
        clean_flag = int(clean_flag)

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if len(filenames)==0:
            raise NodeInputException(self.identifier, "filenames", \
                f"DetectionsCohortReview this input is empty, no file is read.")
        else:
            filenames = eval(filenames)
        try : 
            subject_chans_label = eval(subject_chans_label)
        except:
            raise NodeInputException(self.identifier, "subject_chans_label", \
                f"DetectionsCohortReview this input is wrong, expect a dict with selected channels.")  
        try : 
            ROIs_cohort = eval(ROIs_cohort)
        except:
            raise NodeInputException(self.identifier, "ROIs_cohort", \
                f"DetectionsCohortReview this input is wrong, expect a dict with selected channels for ROIs.")          
        try : 
            ROIs_subjects = eval(ROIs_subjects)
        except:
            raise NodeInputException(self.identifier, "ROIs_subjects", \
                f"DetectionsCohortReview this input is wrong, expect a dict with selected ROIs.")   

        if len(output_file)==0:
            raise NodeInputException(self.identifier, "output_file", \
                f"DetectionsCohortReview this input is empty, no file will be saved.")


        # If at least one file will be saved
        if (clean_flag+transposed_flag)>0:
            # Apply modifications (rename and remove) to the self.PSA_df
            self.read_filename_list(filenames)
            self.rename_channels(subject_chans_label)
            self.remove_unchecked_channels(subject_chans_label)
        else:
            return {
                'out_df': self.df_data
            }

        # Write the report without unselected channels
        if clean_flag==1:
            filename, file_extension = os.path.splitext(output_file)
            if len(file_extension)==0:
                file_extension = '.tsv'
            try: 
                self.df_data.to_csv(filename+self.clean_filename+file_extension, sep='\t', encoding='utf-8', index=False)
                # Log message for the Logs tab
                self._log_manager.log(self.identifier, f"{filename+self.clean_filename+file_extension} is saved")
            except : 
                error_message = f"ERROR : Snooz can not write in the file {filename+self.clean_filename+file_extension}. Current recording is skipped."
                self._log_manager.log(self.identifier, error_message)
                raise NodeRuntimeException(self.identifier, "DetectionsCohortReview", error_message)

        # Write the transposed report without unselected channels
        # In the transposed report, there is one subject per row and each electrode is labelled with its event characteristic (as a new column)
        if transposed_flag==1:
            
            # Find out the regular expression to extract the right characteristics based on the activity_label
            if activity_label.lower()=="distribution per sleep cycle":
                activity_2_export = "cyc\d_"
            else:
                activity_2_export = "total_"
            # Extract all the columns of the spectral data
            mask_activity = self.df_data.columns.str.contains(activity_2_export,regex=True)
            activity_data_df = self.df_data.loc[:,mask_activity]

            # Dataframe to write in the transposed spectral file
            transposed_data_df = pd.DataFrame()
            for subject in subject_chans_label.keys():
                # Extract id1 from the self.df_data and rename the column with id1
                mask_subject = np.asarray(self.df_data['filename']==subject).nonzero() 
                subject_id1 = self.df_data['id1'].iloc[mask_subject]
                subject_id1 = pd.Series(data=subject_id1.values[0], index=[subject_id1.name])
                # subject_act_s : a pandas series (a column) of all activities extracted, one row per activity.
                subject_act_s = self._compile_1subject_std_chan(subject, subject_chans_label, activity_data_df)
                # Generate another subject_act_s for the ROI
                if len(ROIs_cohort)>0:
                    subject_roi_s = self._compile_1subject_ROIs(subject, ROIs_cohort, ROIs_subjects, activity_data_df)
                    # Concatenate them and add the official row in the dataframe.
                    subject_act_s = pd.concat([subject_id1, subject_act_s, subject_roi_s])  
                else:
                    subject_act_s = pd.concat([subject_id1, subject_act_s])   
                # Add the series of the subject into the dataframe 
                # To avoid error when all the channels are unchecked
                if not subject_act_s.empty:
                    subject_act_s.name = subject
                    transposed_data_df = pd.concat([transposed_data_df, subject_act_s], axis=1)
            transposed_data_df = transposed_data_df.T
            # Clean-up the dataframe
            transposed_data_df.reset_index(inplace=True, drop=False)
            transposed_data_df.rename({'index': self.labels_to_extract[0]}, axis=1, inplace=True)
            # Write the transposed PSA file without unselected channels
            filename, file_extension = os.path.splitext(output_file)
            if len(file_extension)==0:
                file_extension = '.tsv'
            try : 
                transposed_data_df.to_csv(filename+self.transposed_filename+file_extension, sep='\t', encoding='utf-8', index=False)
                # Log message for the Logs tab
                self._log_manager.log(self.identifier, f"{filename+self.transposed_filename+file_extension} is saved")
            except : 
                error_message = f"Snooz can not write in the file {filename+self.transposed_filename+file_extension}."+\
                    f" Check if the drive is accessible and ensure the file is not already open."
                raise NodeRuntimeException(self.identifier, "DetectionsCohortReview", error_message)
        return {
            'out_df': self.df_data
        }


    # Read the list of filenames and init self.PSA_df
    def read_filename_list(self, filenames):
        for filename in filenames:
            # Read the csv file and convert the content into a Data Frame
            df_data = pd.read_csv(filename, delimiter='\t', header=0, encoding='utf-8',dtype={'filename': str})
            df_data = df_data.dropna(how='all')
            df_data.reset_index(drop=True, inplace=True)
            self.df_data = pd.concat([self.df_data, df_data])
            self.df_data.reset_index(drop=True, inplace=True)


    # Rename channels in self.df_data based on subject_chans_label
    def rename_channels(self, subject_chans_label):
        for subject in subject_chans_label.keys():
            # Extract basename of subject
            basename = os.path.basename(subject)
            ori_chan_lst, mod_chan_list, check_lst = subject_chans_label[subject]
            if ori_chan_lst!=mod_chan_list:
                for ori_chan, mod_chan in zip(ori_chan_lst,mod_chan_list):
                    if ori_chan != mod_chan:
                        # Look for the row index to drop
                        index_2_rm = self.df_data[ (self.df_data[self.labels_to_extract[0]] == basename) & \
                                            (self.df_data[self.labels_to_extract[1]] == ori_chan) ].index
                        self.df_data.loc[index_2_rm, self.labels_to_extract[1]] = mod_chan


    # Remove uncheck channels from self.df_data based on subject_chans_label
    def remove_unchecked_channels(self, subject_chans_label):
        for subject in subject_chans_label.keys():
            # Extract basename of subject
            basename = os.path.basename(subject)
            ori_chan_lst, mod_chan_list, check_lst = subject_chans_label[subject]
            if sum(check_lst)<len(check_lst):
                for chan, sel in zip(mod_chan_list,check_lst):
                    if sel==False:
                        # Look for the row index to drop
                        index_2_rm = self.df_data[ (self.df_data[self.labels_to_extract[0]] == basename) & \
                                            (self.df_data[self.labels_to_extract[1]] == chan) ].index
                        # Drop the row from the data frame
                        self.df_data.drop(index_2_rm , inplace=True)
                        self.df_data.reset_index(drop=True, inplace=True)


    def _compile_1subject_std_chan( self, subject_i, subject_chans_label, activity_data_df):
        ''' Private function to compile the activity for one subject.
            Returns subject_act_s : a pandas series (a column) of all activities 
            extracted, one row per activity.

            "subject_chans_label" : dict
                Keys are the subjects
                Each item is a list of 3 elements [original chan label, modified chan label, bool selection flag]
        '''
        # Extract basename of subject
        basename = os.path.basename(subject_i)
        mask_sjt = np.asarray(self.df_data['filename']==basename).nonzero()

        # For each list of channels
        subject_act_s = pd.Series(dtype=float)
        # Make sure channels (renamed) are checked
        chan_np = np.array(subject_chans_label[subject_i][1]) # renamed channel label
        sel_np = np.array(subject_chans_label[subject_i][2])  # bool selection
        chan_sel = chan_np[sel_np]
        for chan in chan_sel:
            # Mask to extract the data of a specific channel
            mask_chan = np.asarray(self.df_data[self.labels_to_extract[1]]==chan).nonzero()
            # Mask to extract data of a specific channel from a subject
            # Indexes are unique
            mask_sjt_chan = np.intersect1d(mask_sjt[0],mask_chan[0],assume_unique=True)
            # Extract the spectral power for those bins
            data_sjt_chan = activity_data_df.iloc[mask_sjt_chan].reset_index(drop=True)
            data_sjt_chan = pd.Series(data=data_sjt_chan.values[0], index=data_sjt_chan.columns)
            # Rename the index of the series which are the activity 
            # into activity + chan or activity + roi
            dict_2_rename = {}
            for activity in data_sjt_chan.index:
                index = activity + '_' + chan
                dict_2_rename[activity] = index
            # series (one column), each row is an activity
            data_sjt_chan = data_sjt_chan.rename(dict_2_rename)
            if not data_sjt_chan.empty:
                subject_act_s = pd.concat([subject_act_s,data_sjt_chan])
            subject_act_s.name = subject_i
        
        return subject_act_s


    def _compile_1subject_ROIs( self, subject_i, ROIs_cohort, ROIs_subjects, activity_data_df):
        ''' Private function to compile the activity of ROI for one subject.
            subject_act_s : a pandas series (a column) of all activities extracted, 
            one row per activity.

            Inputs : 
                subject_i : string
                    String to identify the subject
                ROIs_cohort : dict
                    Dict to manage the ROI created at the cohort level
                    keys are ROIs labels
                    Each item is a list of 2 elements [channel list to average, blank flag]
                ROIs_subjects : dict
                    Dict to manage the ROI at the subject level
                    keys are the subjects
                    Each item is a list of n_ROIs with its selection label  [ROI#1 label, bool selection flag]
                                                                            [ROI#2 label, bool selection flag]
        '''
        
        mask_sjt = np.asarray(self.df_data['filename']==subject_i).nonzero()
        # For each list of channels
        subject_act_s = pd.Series(dtype=float)
        # Compute  only if the ROI is checked for the current subject
        all_ROIs_subject = ROIs_subjects[subject_i]
        # For each ROI available in the current subject
        for ROI_label, ROI_sel in all_ROIs_subject:
            if ROI_sel: # If checked by the user
                data_chan_cur_roi = []
                # For each channel in the current ROI
                chan_lst, roi_blank = ROIs_cohort[ROI_label] 
                # Unchecked channels are removed from the df_data, so we need to evaluate if they are selected
                for i, chan in enumerate(chan_lst):
                    # Mask to extract the data of a specific channel
                    mask_chan = np.asarray(self.df_data[self.labels_to_extract[1]]==chan).nonzero()
                    # Mask to extract data of a specific channel from a subject
                    # Indexes are unique
                    mask_sjt_chan = np.intersect1d(mask_sjt[0],mask_chan[0],assume_unique=True)
                    if len(mask_sjt_chan)>0:
                        # Extract the spectral power for those bins
                        data_sjt_chan = activity_data_df.iloc[mask_sjt_chan].reset_index(drop=True)
                        data_sjt_chan = pd.Series(data=data_sjt_chan.values[0], index=data_sjt_chan.columns)                                           
                    else:
                        # Add NaN values to a Series to keep the index valid 
                        # (ex.TOTACTTO)
                        data_sjt_chan = pd.Series(data = \
                            np.ones((activity_data_df.shape[1]))*np.NaN, \
                                index=activity_data_df.columns)          

                    # Accumulate activity for each channel of the roi
                    data_sjt_chan.name = ROI_label
                    if len(data_chan_cur_roi)==0:
                        data_chan_cur_roi = data_sjt_chan
                    else:
                        data_chan_cur_roi = pd.concat([data_chan_cur_roi, data_sjt_chan], axis=1)

                #---------------------------------------------------------------
                # Average the activity of each channel
                #---------------------------------------------------------------
                # Mean over the column (every channel)
                # act_roi is a pandas Series
                # Average indexes with the same name
                # ex) TOTACTS1 of every chan are averaged together
                # Make sure the ROI includes at least 2 channels
                if len(data_chan_cur_roi.shape)==2:
                    if roi_blank:
                         # skipna=False means that if an index is NaN for a channel 
                         # the average for that index (ex: TOTACTS1) is nan. 
                         act_roi = data_chan_cur_roi.mean(skipna=False, axis=1) 
                         # It does not make sense for valid time in minutes
                         #  We take the highest values if all channels are valid 
                         act_roi[act_roi.index.str.contains('valid_min')] = \
                            data_chan_cur_roi[data_chan_cur_roi.index.str.contains('valid_min')].max(skipna=False, axis=1)
                    else:
                         # skipna=True means that if an index is NaN for a channel 
                         # the average for that index (ex: TOTACTS1) skip the NaN channel            
                         # and the average value is still valid but based on less channels.             
                         act_roi = data_chan_cur_roi.mean(skipna=True, axis=1)      
                         # It does not make sense for valid time in minutes
                         #  We take the highest values if all channels are valid      
                         act_roi[act_roi.index.str.contains('valid_min')] = \
                            data_chan_cur_roi[data_chan_cur_roi.index.str.contains('valid_min')].max(skipna=True, axis=1)                             
                else:
                    act_roi = data_chan_cur_roi
                # Convert into a series (column)
                #act_roi = pd.Series(data=act_roi.values[0], index=act_roi.columns)  

                # Rename the index of the series which are the activity 
                # into activity + chan or activity + roi
                dict_2_rename = {}
                for activity in act_roi.index:
                    index = activity + '_' + ROI_label
                    dict_2_rename[activity] = index
                # series (one column), each row is an activity
                roi_to_add_s = act_roi.rename(dict_2_rename)
                if not roi_to_add_s.empty:
                    subject_act_s = pd.concat([subject_act_s,roi_to_add_s])
                subject_act_s.name = subject_i

        return subject_act_s