"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Module to display in the results view an hypnogram and its sleep cycles.

    Parameters
    ----------
        sleep_stages : pandas DataFrame
            List of sleep stages. (columns=['group','name','start_sec','duration_sec','channels'])
        sleep_cycles : List of tuples
            Each element of the list defines a sleep cycle. The first tuple is the 
            beginning and end of the NREM period. The second tuple is the beginning 
            and end of the REM period. Both beginning and end are inclusive indexes.
            The last variable [is_complete] tells of this cycle is complete. An incomplete
            cycle would be one without a REM period, it's often found at the end of the night.
            ((NREM_BEGIN,NREM_END), (REM_BEGIN,REM_END), is_complete)
        sleep_latency : int
            Sleep latency in epoch count
        epoch_len : int
            Epoch length in seconds
        fig_name : String
            Path to save the hypnogram picture (jpg). 
    Returns
    -----------
        None
"""
import os
import math
import numpy as np
from ..PSGReader import commons

# Conditionally import matplotlib based on headless mode
import config
if config.HEADLESS_MODE:
    # Use Agg backend in headless mode (no GUI required, perfect for PDF generation)
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib.figure import Figure
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle
else:
    # Use QtAgg backend in GUI mode
    import matplotlib
    matplotlib.use('QtAgg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle

plt.switch_backend('agg')  # turn off gui

from flowpipe import SciNode, InputPlug

DEBUG = False

class Hypnogram(SciNode):
    """ Module to display in the results view an hypnogram and its sleep cycles.

    Parameters
    ----------
        sleep_stages : pandas DataFrame
            List of sleep stages. (columns=['group','name','start_sec','duration_sec','channels'])
        sleep_cycles : List of tuples
            Each element of the list defines a sleep cycle. The first tuple is the 
            beginning and end of the NREM period. The second tuple is the beginning 
            and end of the REM period. Both beginning and end are inclusive indexes.
            The last variable [is_complete] tells of this cycle is complete. An incomplete
            cycle would be one without a REM period, it's often found at the end of the night.
            ((NREM_BEGIN,NREM_END), (REM_BEGIN,REM_END), is_complete)
        epoch_len : int
            Epoch length in seconds
        fig_name : String
            Path to save the hypnogram picture (jpg). 
    Returns
    -----------
        None
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('Hypnogram.__init__')
        InputPlug('sleep_stages', self)
        InputPlug('sleep_cycles', self)
        InputPlug('epoch_len_sec', self)
        InputPlug('fig_name', self )

    def subscribe_topics(self):
        pass

    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'Hypnogram.on_topic_update {topic}:{message}')

    def compute(self, sleep_stages, sleep_cycles, epoch_len_sec, fig_name):
        """
            Compute record the sleep stages and sleep cycles in the cache.
            The hypnogram will be built by the HypnogramResultsView class.
        """
        if DEBUG: print('Hypnogram.compute')

        if isinstance(epoch_len_sec,str):
            if epoch_len_sec=='':
                epoch_len_sec=None
            else:
                epoch_len_sec = int(epoch_len_sec)

        sleep_stages = sleep_stages.copy()
        sleep_cycles = sleep_cycles.copy()

        self._cache_manager.write_mem_cache(self.identifier, {"sleep_stages":sleep_stages,\
                                                              "sleep_cycles":sleep_cycles, \
                                                              "epoch_len_sec":epoch_len_sec})
        if isinstance(fig_name, str) and (len(fig_name)>0):
            # Plot and save Hypnogram
            if sleep_stages is not None:
                self.figure, self.hypno_ax = plt.subplots()
                self.figure.set_size_inches(16,4)
                self.hypno_ax.clear()
                # Extract filename from path
                PSG_filename = os.path.basename(fig_name)
                PSG_filename = os.path.splitext(PSG_filename)[0]
                self.subject_id = PSG_filename
                self.plot_hypnogram(sleep_stages, sleep_cycles, epoch_len=epoch_len_sec)
                root, ext = os.path.splitext(fig_name)
                if ext == '': fig_name = root + '.pdf'
                self.figure.savefig(fig_name)

        return None

    #def plot_hypnogram(self, hypno_ax, sleep_stages, sleep_cycles, epoch_len=None):
    def plot_hypnogram(self, sleep_stages, sleep_cycles, epoch_len=None):
        """ Plot an hypnogram based on the sleep stages in parameter 
        
        Parameters
        ----------
            sleep_stages : Panda dataframe
                List of sleep stages. (columns=['group','name','start_sec','duration_sec','channels'])
            epoch_len : integer (optional)
                Length of the epoch in seconds

        Returns
        -----------
            None
        """

        hypno_y_label = ["Unscored", "N3","N2","N1","R","Wake", "Cycles"]

        # Combined configuration for sleep stages: plot position and color
        stage_config = {
            "0": {"plot_pos": 5, "color": "white"},         # Awake
            "5": {"plot_pos": 4, "color": "green"},         # REM
            "1": {"plot_pos": 3, "color": "cornflowerblue"}, # N1
            "2": {"plot_pos": 2, "color": "blue"},          # N2
            "3": {"plot_pos": 1, "color": "darkblue"},      # N3
            "9": {"plot_pos": 0, "color": "gray"},          # Unscored
            "8": {"plot_pos": 0, "color": "gray"},          # etc.
            "7": {"plot_pos": 0, "color": "gray"},
        }

        # Derive level colors from stage config
        level_colors = {}
        for stage, config in stage_config.items():
            level_colors[config["plot_pos"]] = config["color"]

        # Hypnogram color definition for sleep cycles
        #                           R           G       B
        fill_color_complete_NREM =  [0/255, 32/255, 128/255]    # Colors values are between 0 and 1
        fill_color_complete_REM =   [0/255, 64/255, 0/255]      # Colors values are between 0 and 1
        fill_color_incomplete =     [150/255, 0/255, 0/255]     # Colors values are between 0 and 1
        alpha = 0.3

        # Remove unscored stages at the beginning and the end
        stages = []
        sleep_stages_nocycle = sleep_stages[sleep_stages.group == commons.sleep_stages_group].copy()
        sleep_stages_nocycle.reset_index(inplace=True, drop=True)
        sleep_stages_nocycle.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')
        scoring_start = sleep_stages_nocycle[(sleep_stages_nocycle['name']!='9') & (sleep_stages_nocycle['name']!='8')].first_valid_index()
        scoring_end = sleep_stages_nocycle[(sleep_stages_nocycle['name']!='9') & (sleep_stages_nocycle['name']!='8')].last_valid_index()
        all_stages = sleep_stages_nocycle['name'].values.tolist()
        if (not scoring_start==None) and (not scoring_end==None):
            scored_stages = all_stages[scoring_start:scoring_end+1]
        else:
            scored_stages = all_stages

        # Convert all stages to they plot value
        for s in scored_stages:
            stage = stage_config.get(s, {"plot_pos": 0})["plot_pos"]
            stages.append(stage)
        
        # Create color list based on original stage values
        colors = [stage_config.get(s, {"color": 'blue'})["color"] for s in scored_stages]
        
        # Draw background rectangles for each level (corresponding to sleep stages)
        for level in range(6): # From the number of unique values to plot (the 7 levels for stages)
            self.hypno_ax.add_patch(Rectangle((0, level - 0.5), len(stages), 1,
                facecolor=level_colors[level], alpha=alpha, edgecolor='none'))

        # Plot the hypnogram contour (black line)
        self.hypno_ax.plot(range(len(stages)), stages, color='black', linewidth=1)
        #self.hypno_ax.bar(range(len(stages)),stages, width=1,align='edge')
        self.hypno_ax.set_yticks(range(len(hypno_y_label)))
        self.hypno_ax.set_yticklabels([])
        self.hypno_ax.set_yticklabels(hypno_y_label)
        self.hypno_ax.set_ylabel('Sleep Stage')
        self.hypno_ax.set_xlabel('Elapsed Time (epoch)')
        # If the epoch length is defined, change the x axis for hour instead of epoch
        if isinstance(epoch_len, int) or isinstance(epoch_len, float):
            max_sec = len(scored_stages) * epoch_len
            max_hour = math.ceil(max_sec/3600)
            self.hypno_ax.set_xticks(np.arange(max_hour)*3600/epoch_len)
            lst_hour = range(max_hour)
            xticklabels=["{:02d}".format(x) for x in lst_hour]
            self.hypno_ax.set_xticklabels([])
            self.hypno_ax.set_xticklabels(xticklabels)
            self.hypno_ax.set_xlabel('Elapsed Time (h)')
            # Path to generate the picture
            #self.hypno_ax.set_title(f'Hypnogram with Sleep Cycles')
            self.hypno_ax.set_title(f'Hypnogram with Sleep Cycles - {self.subject_id}')

        if sleep_cycles is not None:
            self.draw_sleep_cycles(sleep_cycles, scoring_start, 
                fill_color_complete_NREM, fill_color_complete_REM, fill_color_incomplete, alpha)
            
            # Add legend for sleep cycle patches
            legend_patches = [
                Rectangle((0, 0), 1, 1, facecolor='black', label='Sleep Stages'),
                Rectangle((0, 0), 1, 1, facecolor=fill_color_complete_NREM, alpha=alpha, label='NREM Period'),
                Rectangle((0, 0), 1, 1, facecolor=fill_color_complete_REM, alpha=alpha, label='REM Period'),
                Rectangle((0, 0), 1, 1, facecolor=fill_color_incomplete, alpha=alpha, label='Incompl. Period')
            ]
            self.hypno_ax.legend(handles=legend_patches, loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=8, framealpha=0.9)


    #def draw_sleep_cycles(self, hypno_ax, sleep_cycles, scoring_start):
    def draw_sleep_cycles(self, sleep_cycles, scoring_start, 
        fill_color_complete_NREM, fill_color_complete_REM, fill_color_incomplete, alpha):
        """ Draw sleep cycles over the hypnogram.
        A sleep cycle is compose of two period, the NREM and REM period. The NREM period is identified
        by a rectangle that cover the stages 1,2,3 and the REM period is identified by a rectangle that
        cover the REM stage.
        
        Parameters
        ----------
            sleep_cycles : List of tuples
                Each element of the list defines a sleep cycle. The first tuple is the 
                beginning and end of the NREM period. The second tuple is the beginning 
                and end of the REM period. Both beginning and end are inclusive indexes.
                The last variable [is_complete] tells of this cycle is complete. An incomplete
                cycle would be one without a REM period, it's often found at the end of the night.
                ((NREM_BEGIN,NREM_END), (REM_BEGIN,REM_END), is_complete)

        Returns
        -----------
            None
        """
        # Plot the sleep cycles
        for index, (nrem, rem, is_complete) in enumerate(sleep_cycles):

            # NREM
            width = nrem[1] - nrem[0] +1  # the bounderies are inclusive
            if width >= 0:
                self.hypno_ax.add_patch(Rectangle((nrem[0]-scoring_start, 5.2), width, 6,
                linestyle = '-' if is_complete else '--',
                facecolor = fill_color_complete_NREM if is_complete else fill_color_incomplete,
                alpha = alpha,
                edgecolor = 'black',
                fill=True,
                linewidth=0.5))

                # Draw a black outline
                self.hypno_ax.add_patch(Rectangle((nrem[0]-scoring_start, 5.2), width, 6,
                linestyle = '-' if is_complete else '--',
                edgecolor = 'black',
                fill=False,
                linewidth=0.5))

            # REM
            width = rem[1] - rem[0] +1 # the bounderies are inclusive 
            if width >= 0:
                self.hypno_ax.add_patch(Rectangle((rem[0]-scoring_start, 5.2), width, 6,
                linestyle = '-' if is_complete else '--',
                facecolor = fill_color_complete_REM if is_complete else fill_color_incomplete,
                alpha = alpha,
                edgecolor = 'black',
                fill=True,
                linewidth=0.5))

                # Draw a black outline
                self.hypno_ax.add_patch(Rectangle((rem[0]-scoring_start, 5.2), width, 6,
                linestyle = '-' if is_complete else '--',
                edgecolor = 'black',
                fill=False,
                linewidth=0.5))

        # Draw horizontal arrows for complete sleep cycles
        for index, (nrem, rem, is_complete) in enumerate(sleep_cycles):
            if is_complete:
                # Calculate the full cycle span (from NREM start to REM end)
                cycle_start = min(nrem[0], rem[0]) - scoring_start
                cycle_end = max(nrem[1], rem[1]) - scoring_start
                cycle_width = cycle_end - cycle_start
                
                # Draw horizontal arrow at Wake level (y=5)
                # Arrow from cycle_start to cycle_end, centered vertically at y=5
                arrow_y = 5.6
                arrow_length = cycle_width
                
                # Use annotate for better arrow control
                self.hypno_ax.annotate('',
                    xy=(cycle_end, arrow_y),  # Arrow head position
                    xytext=(cycle_start, arrow_y),  # Arrow tail position
                    arrowprops=dict(
                        arrowstyle='<->',  # Double-headed arrow
                        color='black',
                        linewidth=1,
                        shrinkA=0,
                        shrinkB=0
                    ),
                    annotation_clip=False
                )
                
                # Add cycle label (C1, C2, etc.) above the arrow
                cycle_center_x = (cycle_start + cycle_end) / 2
                cycle_label = f'C{index + 1}'
                self.hypno_ax.text(cycle_center_x, arrow_y, cycle_label,
                    ha='center', va='center', fontsize=10, fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))

