"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
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

class PSACohortReview(SciNode):
    """
    Class to read the PSA output file generated from Tool-> Sleep analysis -> PSA and
    generate the PSA file clean or transposed.
    
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
        "freq_band" : pandas DataFrame 
            frequency bands to average, columns=['num-start(Hz)','num-end(Hz)','den-start(Hz)','den-end(Hz)'])) 
        "activity_label" : string
            The activity variable to export/save i.e. 'Total', 'distribution per hour' or 'distribution per sleep cycle'.        
        "PSA_clean_flag" : bool
            Flag to generate and save the PSA file with only selected channels.
        "PSA_transposed_flag" : bool
            Flag to generate and save the transposed PSA file (1 subject per row)
        "output_dir" : string
            Output path to save the PSA file clean and/or transposed.

    Outputs:
        "out_df": pandas DataFrame
                PSA data converted into a dataframe with modifications applied. 
        
    """
    def __init__(self, **kwargs):
        """ Initialize module PSACohortReview """
        super().__init__(**kwargs)
        if DEBUG: print('SleepReport.__init__')

        # Input plugs
        InputPlug('filenames',self)
        InputPlug('subject_chans_label',self)
        InputPlug('ROIs_cohort',self)
        InputPlug('ROIs_subjects',self)
        InputPlug('freq_band',self)
        InputPlug('activity_label',self)
        InputPlug('PSA_clean_flag',self)
        InputPlug('PSA_transposed_flag',self)
        InputPlug('output_dir',self)
        
        # Output plugs
        OutputPlug('out_df',self)

        # A master module allows the process to be reexcuted multiple time.
        self._is_master = False 
        # To save the PSA activity from the list of filenames
        self.PSA_df = pd.DataFrame()
        self.PSA_label = ['filename', 'channel_label', 'freq_low_Hz', 'freq_high_Hz']
        self.PSA_clean_filename = "_clean"
        self.PSA_transposed_filename = "_transposed"
        self.freq_band_label = ['num-start(Hz)','num-end(Hz)','den-start(Hz)','den-end(Hz)']


    def compute(self, filenames, subject_chans_label, ROIs_cohort, ROIs_subjects, freq_band, activity_label, PSA_clean_flag, PSA_transposed_flag, output_dir):
        """
        To read the PSA output file generated from Tool-> Sleep analysis -> PSA and
        generate the PSA file clean or transposed.
        
        Inputs:
            "filenames": List of String
                List of filename (including path) to the PSA output file.
            "subject_chans_label" : dict
                Keys are the subjects
                Each item is a list of 3 elements [original chan label, modified chan label, selected flag]
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
            "freq_band" : string of pandas DataFrame 
                frequency bands to average, columns=['num-start(Hz)','num-end(Hz)','den-start(Hz)','den-end(Hz)'])) 
            "activity_label" : string
                The activity variable to export/save i.e. 'Total', 'distribution per hour' or 'distribution per sleep cycle'.
            "PSA_clean_flag" : bool"
                Flag to generate and save the PSA file with only selected channels.
            "PSA_transposed_flag" : bool
                Flag to generate and save the transposed PSA file (1 subject per row)
            "output_dir" : string
                Output path to save the PSA file clean and/or transposed.

        Outputs:
            "out_df": pandas DataFrame
                    PSA data converted into a dataframe with modifications applied. 
        
        """
        PSA_transposed_flag = int(PSA_transposed_flag)
        PSA_clean_flag = int(PSA_clean_flag)

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if len(filenames)==0:
            raise NodeInputException(self.identifier, "filenames", \
                f"PSACohortReview this input is empty, no file is read.")
        else:
            filenames = eval(filenames)
        try : 
            subject_chans_label = eval(subject_chans_label)
        except:
            raise NodeInputException(self.identifier, "subject_chans_label", \
                f"PSACohortReview this input is wrong, expect a dict with selected channels.")  
        try : 
            ROIs_cohort = eval(ROIs_cohort)
        except:
            raise NodeInputException(self.identifier, "ROIs_cohort", \
                f"PSACohortReview this input is wrong, expect a dict with selected channels for ROIs.")          
        try : 
            ROIs_subjects = eval(ROIs_subjects)
        except:
            raise NodeInputException(self.identifier, "ROIs_subjects", \
                f"PSACohortReview this input is wrong, expect a dict with selected ROIs.")   

        if (not freq_band=='') and not ("Empty DataFrame" in freq_band):
            freq_band = pd.read_csv(StringIO(freq_band), sep='\s+', index_col=0)

        if len(output_dir)==0:
            raise NodeInputException(self.identifier, "output_dir", \
                f"PSACohortReview this input is empty, no file will be saved.")

        # If at least one file will be saved
        if (PSA_clean_flag+PSA_transposed_flag)>0:
            # Apply modifications (rename and remove) to the self.PSA_df
            self.read_PSA_filename(filenames)
            self.rename_channels(subject_chans_label)
            self.remove_unchecked_channels(subject_chans_label)
        else:
            return {
                'out_df': self.PSA_df
            }

        # Write the PSA file without unselected channels
        if PSA_clean_flag==1:
            filename, file_extension = os.path.splitext(output_dir)
            if len(file_extension)==0:
                file_extension = '.tsv'
            try : 
                PSAfilename = filename+self.PSA_clean_filename+file_extension
                self.PSA_df.to_csv(PSAfilename, sep='\t', encoding='utf-8', index=False)
                # Log message for the Logs tab
                self._log_manager.log(self.identifier, f"{PSAfilename} is saved")
            except :
                error_message = f"Snooz can not write in the file {PSAfilename}."+\
                    f" Check if the drive is accessible and ensure the file is not already open."
                raise NodeRuntimeException(self.identifier, "PSACohortReview", error_message)            

        # Write the transposed PSA file without unselected channels
        # The transposed file average the energy in the frequency bands defined by the user (if any)
        if PSA_transposed_flag==1:
            
            # Find out the regular expression to extract the right PSA activity based on the activity_label
            if activity_label.lower()=="distribution per hour":
                activity_2_export = "hour\d(?:_[A-Za-z]+)?_act"
            elif activity_label.lower()=="distribution per sleep cycle":
                activity_2_export = "cyc\d(?:_[A-Za-z]+)?_act"
            else:
                activity_2_export = "total(?:_[A-Za-z]+)?_act"
            # Extract all the columns of the spectral data
            mask_activity = self.PSA_df.columns.str.contains(activity_2_export,regex=True)
            if any(mask_activity):
                activity_data_df = self.PSA_df.loc[:,mask_activity]
            # Look for a PSAOnEvents
            else:
                activity_2_export = "act_"
                # Extract all the columns of the spectral data
                mask_activity = self.PSA_df.columns.str.contains(activity_2_export,regex=True)
                activity_data_df = self.PSA_df.loc[:,mask_activity]

            # Dataframe to write in the transposed spectral file
            transposed_data_df = pd.DataFrame()
            for subject in subject_chans_label.keys():
                # subject_act_s : a pandas series (a column) of all activities extracted, one row per activity.
                subject_act_s = self._compile_1subject_std_chan(subject, subject_chans_label, freq_band, activity_data_df)
                # Generate another subject_act_s for the ROI
                if len(ROIs_cohort)>0:
                    subject_roi_s = self._compile_1subject_ROIs(subject, ROIs_cohort, ROIs_subjects, freq_band, activity_data_df)
                    # Concatenate them and add the official row in the dataframe.
                    subject_act_s = pd.concat([subject_act_s, subject_roi_s])                
                # Add the series of the subject into the dataframe 
                # To avoid error when all the channels are unchecked
                if not subject_act_s.empty:
                    transposed_data_df = pd.concat([transposed_data_df, subject_act_s], axis=1)
            transposed_data_df = transposed_data_df.T
            # Clean-up the dataframe
            transposed_data_df.reset_index(inplace=True, drop=False)
            transposed_data_df.rename({'index': self.PSA_label[0]}, axis=1, inplace=True)
            # Write the transposed PSA file without unselected channels
            filename, file_extension = os.path.splitext(output_dir)
            if len(file_extension)==0:
                file_extension = '.tsv'
            try : 
                PSAfilename = filename+self.PSA_transposed_filename+file_extension
                transposed_data_df.to_csv(PSAfilename, sep='\t', encoding='utf-8', index=False)
                # Log message for the Logs tab
                self._log_manager.log(self.identifier, f"{PSAfilename} is saved")
            except :
                error_message = f"Snooz can not write in the file {PSAfilename}."+\
                    f" Check if the drive is accessible and ensure the file is not already open."
                raise NodeRuntimeException(self.identifier, "PSACohortReview", error_message)        

        return {
            'out_df': self.PSA_df
        }


    # Read the list of filenames and init self.PSA_df
    def read_PSA_filename(self, filenames):
        for filename in filenames:
            # Read the csv file and convert the content into a Data Frame
            PSA_df = pd.read_csv(filename, delimiter='\t', header=0, encoding='utf-8',dtype={'filename': str})
            PSA_df = PSA_df.dropna(how='all')
            PSA_df.reset_index(drop=True, inplace=True)
            self.PSA_df = pd.concat([self.PSA_df, PSA_df])
            self.PSA_df.reset_index(drop=True, inplace=True)


    # Remove uncheck channels from self.PSA_df based on subject_chans_label
    def remove_unchecked_channels(self, subject_chans_label):
        for subject in subject_chans_label.keys():
            ori_chan_lst, mod_chan_list, check_lst = subject_chans_label[subject]
            if sum(check_lst)<len(check_lst):
                for chan, sel in zip(mod_chan_list,check_lst):
                    if sel==False:
                        # Look for the row index to drop
                        # Extract basename from subject TODO
                        basename = os.path.basename(subject)
                        index_2_rm = self.PSA_df[ (self.PSA_df[self.PSA_label[0]] == basename) & \
                                            (self.PSA_df[self.PSA_label[1]] == chan) ].index
                        # Drop the row from the data frame
                        self.PSA_df.drop(index_2_rm , inplace=True)
                        self.PSA_df.reset_index(drop=True, inplace=True)


    # Rename channels in self.PSA_df based on subject_chans_label
    def rename_channels(self, subject_chans_label):
        for subject in subject_chans_label.keys():
            ori_chan_lst, mod_chan_list, check_lst = subject_chans_label[subject]
            if ori_chan_lst!=mod_chan_list:
                for ori_chan, mod_chan in zip(ori_chan_lst,mod_chan_list):
                    if ori_chan != mod_chan:
                        # Extract basename from subject TODO
                        basename = os.path.basename(subject)
                        # Look for the row index to drop
                        index_2_rm = self.PSA_df[ (self.PSA_df[self.PSA_label[0]] == basename) & \
                                            (self.PSA_df[self.PSA_label[1]] == ori_chan) ].index
                        self.PSA_df.loc[index_2_rm, self.PSA_label[1]] = mod_chan


    def _compile_1subject_std_chan( self, subject_i, subject_chans_label, freq_band, activity_data_df):
        ''' Private function to transpose the spectral activity for one subject.
            Returns subject_act_s : a pandas series (a column) of all activities 
            extracted, one row per activity.

            inputs:
                subject_i : string
                    The current subject id to process
                subject_chans_label : dict
                    Keys are the subjects
                    Each item is a list of 3 elements [original chan label, modified chan label, selected flag]  
                freq_band : Pandas DataFrame
                    frequency bands to average, columns=['num-start(Hz)','num-end(Hz)','den-start(Hz)','den-end(Hz)'])) 
                activity_data_df : Pandas DataFrame
                    Dataframe of the activity selected (the columns are extracted from the self.PSA_df)        

            outputs:
                subject_act_s : pandas series
                    pandas series (a column) of all activities extracted, one row per activity.
                  
        '''
        basename = os.path.basename(subject_i) # TODO
        mask_row_sjt = np.asarray(self.PSA_df[self.PSA_label[0]]==basename).nonzero()
        # For each list of channels
        subject_act_s = pd.Series(dtype=float)
        # Make sure channels (renamed) are checked
        chan_np = np.array(subject_chans_label[subject_i][1]) # renamed channel label
        sel_np = np.array(subject_chans_label[subject_i][2])  # bool selection
        chan_sel = chan_np[sel_np]
        for chan in chan_sel:
            # Mask to extract the data of a specific channel
            mask_chan = np.asarray(self.PSA_df[self.PSA_label[1]]==chan).nonzero()
            # Mask to extract data of a specific channel from a subject
            # Indexes are unique
            mask_row_sjt_chan = np.intersect1d(mask_row_sjt[0],mask_chan[0],assume_unique=True)
            # Extract freq bins for the specific subject and channel (freq_start and freq_stop are pandas series of the available freq bins)
            freq_start = self.PSA_df[self.PSA_label[2]][mask_row_sjt_chan].reset_index(drop=True)
            freq_stop = self.PSA_df[self.PSA_label[3]][mask_row_sjt_chan].reset_index(drop=True)
            # Extract the spectral power for those bins
            data_sjt_chan = activity_data_df.iloc[mask_row_sjt_chan].reset_index(drop=True)

            # Compute each frequency band for each subject and channel
            for freq_index, freq_row in freq_band.iterrows():
                
                # Compute the power activity for each freq band
                    # mask_abs_band : frequency bin indexes for band numerator
                    # mask_rel_band : frequency bin indexes for band denumerator
                    # rel_freq_band_act : pandas series (column) with an activity per row
                mask_abs_band, mask_rel_band, rel_freq_band_act = \
                    self._compute_rel_band_act(data_sjt_chan, freq_row, freq_start, freq_stop)

                # Construct a dictionnary to rename the index of the series which 
                # are the activity into activity+rel+chan+freq_low+freq_high
                dict_2_rename = self._rename_index_freqvalues( chan, freq_row, rel_freq_band_act)

                # series (one column), each row is an activity
                band_to_add_s = rel_freq_band_act.rename(dict_2_rename)
                subject_act_s = pd.concat([subject_act_s,band_to_add_s])
            # subject_act_s.name = subject_i TODO
            subject_act_s.name = basename
        
        return subject_act_s


    def _compute_rel_band_act( self, data_sjt_chan, data_row, freq_start, freq_stop):
        ''' Compute the power activity for each freq band.
            Return :
                mask_abs_band : frequency bin indexes for band numerator
                mask_rel_band : frequency bin indexes for band denumerator
                rel_freq_band_act : pandas series (column) with an activity per row
        '''
        # Find freq bins indexes for the frequency band
        mask_abs_band = self._find_freq_bins_i(float(data_row.loc[self.freq_band_label[0]]), \
            float(data_row.loc[self.freq_band_label[1]]), freq_start, freq_stop)

        # Denominator if it is a relative power band                
        if np.isnan(float(data_row.loc[self.freq_band_label[2]]))==False and \
            np.isnan(float(data_row.loc[self.freq_band_label[3]]))==False:
            # Find freq bins indexes for the frequency band
            mask_rel_band = self._find_freq_bins_i(float(data_row.loc[self.freq_band_label[2]]), \
                float(data_row.loc[self.freq_band_label[3]]), freq_start, freq_stop) 
        else:
            mask_rel_band = []
            
        # Select all rows corresponding to the current subject, channel and band.
        # All activities are kept in different columns
        # sum the numerator band if multiples freq bins

        # If at least one freq bin is missing    
        if isinstance(mask_abs_band, list) and len(mask_abs_band)==0:
            # Extract the column without index
            # Here a dataframe is extracted
            temp = data_sjt_chan.iloc[mask_abs_band]
            # Convert temp to a Series and 
            # add NaN values to keep the index valid
            rel_freq_band_act = pd.Series(data = \
                np.ones((temp.shape[1]))*np.NaN,index=temp.columns)                                               
        # All freq bins are valid
        else:
            # If there is only one freq bin to add
            if isinstance(mask_abs_band, np.int64):
                # Extract the indexes (activities) with values
                # num_band_sum is a series (column) if more than one activities
                num_band_sum = data_sjt_chan.iloc[mask_abs_band]
            else:
                num_band_sum = data_sjt_chan.iloc[mask_abs_band]
                num_band_sum = num_band_sum.sum(axis=0)
                num_band_sum = num_band_sum.mask(num_band_sum==0,np.NaN)

            # If we expect a denominator
            if np.isnan(float(data_row.loc[self.freq_band_label[2]]))==False and \
                    np.isnan(float(data_row.loc[self.freq_band_label[3]]))==False:
                # If at least one freq bin is missing    
                if isinstance(mask_rel_band, list) and len(mask_rel_band)==0:
                    # Extract the column without index
                    # Here a dataframe is extracted
                    temp = data_sjt_chan.iloc[mask_rel_band]
                    # Convert temp to a Series and 
                    # add NaN values to keep the index valid
                    rel_freq_band_act = pd.Series(data = \
                        np.ones((temp.shape[1]))*np.NaN,index=temp.columns)         
                # All freq bins are valid                        
                else:
                    # If there is only one freq bin to add
                    if isinstance(mask_rel_band, np.int64):
                        # Extract the indexes (activities) with values
                        # den_band_sum is a series (column) if more than one activities
                        den_band_sum = data_sjt_chan.iloc[mask_rel_band]       
                    else:                                             
                        # sum the denumerator band
                        den_band_sum = data_sjt_chan.iloc[mask_rel_band]
                        # The sum of one value discard the index
                        #if den_band_sum.size>1: 
                        den_band_sum = den_band_sum.sum(axis=0)
                        #else:
                        den_band_sum = den_band_sum.mask(den_band_sum==0,1)  
                    # Compute the relative freq band
                    rel_freq_band_act = num_band_sum/den_band_sum*100
            else:
                rel_freq_band_act = num_band_sum
        return mask_abs_band, mask_rel_band, rel_freq_band_act


    def _find_freq_bins_i( self, band_start, band_stop, freq_bins_start, freq_bins_end):
        ''' Find freq bins indexes for the frequency band.
        '''
        # Compute the freq bin size (default one, the mode)
        # This list of freq bins is used to sum many bins
        list_tmp = (freq_bins_end-freq_bins_start).to_list()
        default_freq_len = max(set(list_tmp), key=list_tmp.count)
        freq_start_default = freq_bins_start.where(freq_bins_end-freq_bins_start<=default_freq_len)

        # Find the index linked to the freq band asked
        # Look first for a unique frequency bins
        mask_band_low = np.asarray(freq_bins_start==band_start).nonzero()
        mask_band_high = np.asarray(freq_bins_end==band_stop).nonzero()
        # Only the first match is taken 
        mask_band = np.intersect1d(mask_band_low, mask_band_high, assume_unique=True)
        if isinstance(mask_band,np.ndarray) and mask_band.size>0:
            return mask_band[0]
        else:
            # The frequency bins do not look to be tiny band and
            # the frequency band is not found
            if not (default_freq_len == 0.5 or default_freq_len == 1):
                mask_band = []
                return mask_band
            else:
                # print yello message
                # raise ValueError("Subject {}, channel {}, ".format(subject_i, chan)\
                #     + "Band {} not found in the frequency bins (tiny bins of {} Hz)"\
                #     .format(freq_index, default_freq_len))
                # Create the expected bins to add
                # Special case when the start freq is smaller than the bin len
                # ex. high-pass starts to 0.6 Hz and the default bin length is 1 Hz
                if band_start>=default_freq_len: # ex. 11 to 16 Hz with freq bins = 1 Hz
                    freq_bins_start = np.arange(band_start, band_stop, default_freq_len)
                else: # ex. 0.6-32 Hz with freq bins = 1 Hz
                    freq_bins_start = np.arange(default_freq_len, band_stop, default_freq_len)
                    freq_bins_start_tmp = np.ones(1)*band_start
                    freq_bins_start = np.concatenate((freq_bins_start_tmp,freq_bins_start))
                # Append freq bin index to add together
                # Only the first start freq bin match is taken
                # Only the freq bins with the default len or smaller are considered
                # then no freq band should be taken
                mask_band_low = []
                for freq_i in range(len(freq_bins_start)):
                    band_low = np.asarray(freq_start_default==freq_bins_start[freq_i]).nonzero()
                    if not (isinstance(band_low, tuple) and len(band_low[0])==0):
                        # extract first match only
                        if np.ndim(band_low)==1:
                            mask_band_low.append(band_low[0])
                        elif np.ndim(band_low)==2:
                            mask_band_low.append(band_low[0][0])
                    # If a bin is missing, return empty
                    else:
                        mask_band = []
                        return mask_band
                # If all bins were found, return the bins to add together
                mask_band = mask_band_low
                return mask_band


    # Construct a dictionnary to rename the index of the series which 
    # are the activity into activity+rel+chan+freq_low+freq_high
    def _rename_index_freqvalues( self, chan, data_row, rel_freq_band_act):
        
        # Flag to name the frequency band in the header in a smart way 
        smart_rep = 1 # otherwise . in decimal number are converted into _

        dict_2_rename = {}
        if smart_rep==1 : 

            label_low = str(data_row.loc['num-start(Hz)'])
            if label_low[-2:]==".0": # ex) 32.0 Hz -> 32
                label_low = label_low.replace('.0','')
            elif label_low[0:2]=="0.": # ex) 0.6 Hz -> 06;  0.005 -> 0005
                label_low = label_low.replace('0.','0')
            else: # ex) 10.5 -> 10_5
                label_low = label_low.replace('.','_')

            label_high = str(data_row.loc['num-end(Hz)'])
            if label_high[-2:]==".0": # ex) 32.0 Hz -> 32
                label_high = label_high.replace('.0','')
            elif label_high[0:2]=="0.": # ex) 0.6 Hz -> 06;  0.005 -> 0005
                label_high = label_high.replace('0.','0')
            else: # ex) 10.5 -> 10_5
                label_high = label_high.replace('.','_')                
        else:
            label_low  = str(data_row.loc['num-start(Hz)']).replace('.','_') 
            label_high = str(data_row.loc['num-end(Hz)']).replace('.','_') 

        for activity in rel_freq_band_act.index:
            # If we expect a denominator
            if np.isnan(float(data_row.loc['den-start(Hz)']))==False and \
                    np.isnan(float(data_row.loc['den-end(Hz)']))==False:                                        
                index = activity + '_rel_' + chan + '_' + label_low + '_' + label_high
            else:
                index = activity + '_abs_' + chan + '_' + label_low + '_' + label_high
            dict_2_rename[activity] = index
        return dict_2_rename


    def _compile_1subject_ROIs(self, subject_i, ROIs_cohort, ROIs_subjects, freq_band, activity_data_df):
        ''' Private function to compile the spectral activity of ROI for one subject.
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
                                                                                    ...            
            freq_band : pandas DataFrame 
                frequency bands to average, columns=['num-start(Hz)','num-end(Hz)','den-start(Hz)','den-end(Hz)'])) 
            activity_data_df : pandas DataFrame 
                Spectral data of the variables to export. All rows from self.PSA_df for the selected columns based on the variable labels.

        Returns : 
            subject_act_s : a pandas series (a column)
                Series of all activities extracted, one activity per row.

        ''' 
        # Mask to extract data for the current subject
        # Extract basename of the filename subject_i
        basename = os.path.basename(subject_i)
        mask_sjt = np.asarray(self.PSA_df[self.PSA_label[0]]==basename).nonzero()
        # To save the activity for the current subject
        subject_act_s = pd.Series(dtype=float)
        # Compute power only if the ROI is checked for the current subject
        all_ROIs_subject = ROIs_subjects[subject_i]
        # For each ROI available in the current subject
        for ROI_label, ROI_sel in all_ROIs_subject:
            if ROI_sel: # If checked by the user
                # Compute each frequency band for each subject and roi
                for freq_index, data_row in freq_band.iterrows():
                    # For each channel in the current ROI
                    chan_lst, roi_blank = ROIs_cohort[ROI_label] 
                    # Unchecked channels are removed from the PSA_df, so ne need to evaluate if they are selected
                    for i, chan in enumerate(chan_lst):
                        # Maks to extract the data of a specific channel
                        mask_chan = np.asarray(self.PSA_df[self.PSA_label[1]]==chan).nonzero()
                        # Mask to extract data of a specific channel from a subject (Indexes are unique)
                        mask_sjt_chan = np.intersect1d(mask_sjt[0],mask_chan[0],assume_unique=True)
                        if len(mask_sjt_chan)>0:
                            # Extract freq bins for the specific subject and channel
                            freq_start = self.PSA_df[self.PSA_label[2]][mask_sjt_chan].reset_index(drop=True)
                            freq_stop = self.PSA_df[self.PSA_label[3]][mask_sjt_chan].reset_index(drop=True)
                            # Extract the spectral power for those bins
                            data_sjt_chan = activity_data_df.iloc[mask_sjt_chan].reset_index(drop=True)
                            # Compute the power activity for each freq band
                                # mask_abs_band : frequency bin indexes for band numerator
                                # mask_rel_band : frequency bin indexes for band denumerator
                                # rel_freq_band_act : pandas series (column) with an activity per row
                            mask_abs_band, mask_rel_band, rel_freq_band_act_1chan = \
                                self._compute_rel_band_act(data_sjt_chan, data_row, freq_start, freq_stop)
                            # Print error message
                            if isinstance(mask_abs_band, list) and len(mask_abs_band)==0:
                                message = f'Subject: {subject_i}, channel: {chan} - freq band {freq_index} is not found'
                                raise NodeRuntimeException(self.identifier, "freq_band", f"PSACohortReview : {message}")
                            # Denominator if it is a relative power band                
                            if np.isnan(float(data_row.loc['den-start(Hz)']))==False and \
                                np.isnan(float(data_row.loc['den-end(Hz)']))==False:                                        
                                if isinstance(mask_rel_band, list) and len(mask_rel_band)==0:
                                    message = f'Subject: {subject_i}, channel: {chan} - denominator of the freq band {freq_index} is not found'     
                                    raise NodeRuntimeException(self.identifier, "freq_band", f"PSACohortReview : {message}")                                               
                        else:
                            # Add NaN values to a Series to keep the index valid 
                            # (ex.TOTACTTO)
                            rel_freq_band_act_1chan = pd.Series(data = np.ones((activity_data_df.shape[1]))*np.NaN, index=activity_data_df.columns)          

                        # Accumulate activity for each channel of the roi (axis=0 by default)
                        #rel_freq_band_act_roi = pd.concat([rel_freq_band_act_roi,rel_freq_band_act_1chan])
                        if i==0:
                            rel_freq_band_act_roi = rel_freq_band_act_1chan
                        else:
                            rel_freq_band_act_roi = pd.concat([rel_freq_band_act_roi,rel_freq_band_act_1chan], axis=1)

                    #---------------------------------------------------------------
                    # Average the power of each channel to manage the ROI
                    #---------------------------------------------------------------
                    # Mean over the column (every channel)
                    # act_roi is a pandas Series
                    # Average indexes with the same name
                    # ex) TOTACTS1 of every chan are averaged together
                    #rel_freq_band_act_roi.rename({'index': 'variable'}, inplace=True)
                    # Make sure the ROI includes at least 2 channels
                    if len(rel_freq_band_act_roi.shape)==2:
                        if roi_blank:
                            # The nan values are not skipped.  We want the ROI to be nan if there is a missing channel.
                            act_roi = rel_freq_band_act_roi.mean(axis=1, skipna=False)
                        else:
                            # The nan values are skipped.  We want the ROI to be valid event if there is a missing channel.
                            # The average value is still valid but based on less channels.                                 
                            act_roi = rel_freq_band_act_roi.mean(axis=1, skipna=True)                  
                    else:
                        act_roi = rel_freq_band_act_roi
                    # Construct a dictionnary to rename the index of the series which 
                    # are the activity into activity+rel+chan+freq_low+freq_high
                    dict_2_rename = self._rename_index_freqvalues( ROI_label, data_row, act_roi)
                    # series (one column), each row is an activity
                    band_to_add_s = act_roi.rename(dict_2_rename)
                    if not band_to_add_s.empty:
                        subject_act_s = pd.concat([subject_act_s,band_to_add_s])
                    subject_act_s.name = subject_i
        return subject_act_s
