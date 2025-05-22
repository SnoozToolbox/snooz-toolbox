"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
        Find components of a signal with idependant component analysis

    Parameters
    -----------        
        signals : List
            List of signal with dictionary of channels with SignalModel with 
            properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original

        -----------------------------------------------------------------
        Taken from _fastica.py
        Read more in the :ref:`User Guide <ICA>`.
        https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html

        algorithm : String, default='parallel'
            Apply parallel or deflational algorithm for FastICA. Valid value are :
            'parallel',
            'deflation'

        whiten : str or bool, default='arbitrary-variance'
            Specify the whitening strategy to use.
            If 'arbitrary-variance' (default), a whitening with variance arbitrary is used.
            If 'unit-variance', the whitening matrix is rescaled to ensure that each recovered source has unit variance.
            If False, the data is already considered to be whitened, and no whitening is performed.

        fun : str, {'logcosh', 'exp', 'cube'} or callable, default='logcosh'
            The functional form of the G function used in the approximation to 
            neg-entropy. Could be either 'logcosh', 'exp', or 'cube'.
            You can also provide your own function. It should return a tuple
            containing the value of the function, and of its derivative, in the
            point. Example::def my_g(x):return x ** 3, (3 * x ** 2).mean(axis=-1)

        fun_args : dict, default=None
            Arguments to send to the functional form.
            If empty and if fun='logcosh', fun_args will take value
            {'alpha' : 1.0}.

        max_iter : int, default=200
            Maximum number of iterations during fit.

        tol : float, default=1e-4
            Tolerance on update at each iteration.

        w_init : ndarray of shape (n_components, n_components), default=None
            The mixing matrix to be used to initialize the algorithm.

        random_state : int, RandomState instance or None, default=None
            Used to initialize ``w_init`` when not specified, with a
            normal distribution. Pass an int, for reproducible results
            across multiple function calls.
            See :term:`Glossary <random_state>`.      

    Returns
    ----------- 
        components: List of signal_models obtain after the decomposition
"""
import ica
from ica import ica1
import numpy as np
from tqdm import tqdm
from sklearn import decomposition
import sys

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException

from CEAMSModules.PSGReader.SignalModel import SignalModel

DEBUG = False

class IcaComponents(SciNode):
    """
        Find components of a signal with idependant component analysis

        Parameters
        -----------        
            signals : List
                List of signal with dictionary of channels with SignalModel with 
                properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original

            parameters : dict
                parameters to decompose the signal.

                ICA_algo : string ('infomax' or 'fastICA')

                n_components : int, default=None
                    Number of components to use. If None is passed, all are used.
                -----------------------------------------------------------------
                Taken from _fastica.py
                Read more in the :ref:`User Guide <ICA>`.
                https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html

                algorithm : String, default='parallel'
                    Apply parallel or deflational algorithm for FastICA. Valid value are :
                    'parallel',
                    'deflation'

                whiten : str or bool, default='arbitrary-variance'
                    Specify the whitening strategy to use.
                    If 'arbitrary-variance' (default), a whitening with variance arbitrary is used.
                    If 'unit-variance', the whitening matrix is rescaled to ensure that each recovered source has unit variance.
                    If False, the data is already considered to be whitened, and no whitening is performed.

                fun : str, {'logcosh', 'exp', 'cube'} or callable, default='logcosh'
                    The functional form of the G function used in the approximation to 
                    neg-entropy. Could be either 'logcosh', 'exp', or 'cube'.
                    You can also provide your own function. It should return a tuple
                    containing the value of the function, and of its derivative, in the
                    point. Example::def my_g(x):return x ** 3, (3 * x ** 2).mean(axis=-1)

                fun_args : dict, default=None
                    Arguments to send to the functional form.
                    If empty and if fun='logcosh', fun_args will take value
                    {'alpha' : 1.0}.

                max_iter : int, default=200
                    Maximum number of iterations during fit.

                tol : float, default=1e-4
                    Tolerance on update at each iteration.

                w_init : ndarray of shape (n_components, n_components), default=None
                    The mixing matrix to be used to initialize the algorithm.

                random_state : int, RandomState instance or None, default=None
                    Used to initialize ``w_init`` when not specified, with a
                    normal distribution. Pass an int, for reproducible results
                    across multiple function calls.
                    See :term:`Glossary <random_state>`.      

        Returns
        ----------- 
            components: List of signal_models obtain after the decomposition
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('IcaComponents.__init__')
        self._filename = None
        InputPlug('signals', self)
        InputPlug('parameters', self)
        OutputPlug('components', self)


    # The plugin subscribes to the publisher to receive the settings (messages) as input
    def subscribe_topics(self):
        pass

    def compute(self, signals, parameters):
        """
        Find components of a signal with idependant component analysis

        Parameters
        -----------        
            signals : List
                List of signal with dictionary of channels with SignalModel with 
                properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original

            parameters : dict
                parameters to decompose the signal.

                ICA_algo : string ('infomax' or 'fastICA')

                -----------------------------------------------------------------
                Taken from _fastica.py
                Read more in the :ref:`User Guide <ICA>`.
                https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html

                algorithm : String, default='parallel'
                    Apply parallel or deflational algorithm for FastICA. Valid value are :
                    'parallel',
                    'deflation'

                whiten : str or bool, default='arbitrary-variance'
                    Specify the whitening strategy to use.
                    If 'arbitrary-variance' (default), a whitening with variance arbitrary is used.
                    If 'unit-variance', the whitening matrix is rescaled to ensure that each recovered source has unit variance.
                    If False, the data is already considered to be whitened, and no whitening is performed.

                fun : str, {'logcosh', 'exp', 'cube'} or callable, default='logcosh'
                    The functional form of the G function used in the approximation to 
                    neg-entropy. Could be either 'logcosh', 'exp', or 'cube'.
                    You can also provide your own function. It should return a tuple
                    containing the value of the function, and of its derivative, in the
                    point. Example::def my_g(x):return x ** 3, (3 * x ** 2).mean(axis=-1)

                fun_args : dict, default=None
                    Arguments to send to the functional form.
                    If empty and if fun='logcosh', fun_args will take value
                    {'alpha' : 1.0}.

                max_iter : int, default=200
                    Maximum number of iterations during fit.

                tol : float, default=1e-4
                    Tolerance on update at each iteration.

                w_init : ndarray of shape (n_components, n_components), default=None
                    The mixing matrix to be used to initialize the algorithm.

                random_state : int, RandomState instance or None, default=None
                    Used to initialize ``w_init`` when not specified, with a
                    normal distribution. Pass an int, for reproducible results
                    across multiple function calls.
                    See :term:`Glossary <random_state>`.      

        Returns
        ----------- 
            components: List of signal_models obtain after the decomposition
        """

        if DEBUG: print('IcaComponents.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None  

        # Verify inputs
        if isinstance(signals,str) and signals=='':
            raise NodeInputException(self.identifier, "signals", \
                f"IcaComponents this input is not connected.")
        if not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", \
                f"IcaComponents input of wrong type. Expected: <class 'list'> received: {type(signals)}")
        elif isinstance(signals, list) and len(signals)==0:
            return {'signals_from_events': []}

        if isinstance(parameters, str) and len(parameters)>0:
            parameters = eval(parameters)

        signals_events = SignalModel.get_attribute(signals, None, 'start_time')
        samples_events = SignalModel.get_attribute(signals, 'samples', 'start_time')
        channel_events = SignalModel.get_attribute(signals, 'channel', 'start_time')

        # Set progress bar
        total_event = len(signals_events)
        desc = 'Applying ICA'
        
        # Safe check for terminal support
        use_progress_bar = sys.stdout is not None and sys.stdout.isatty()
        pbar = tqdm(total=total_event, desc=desc, disable=not use_progress_bar)

        if parameters['ICA_algo']=='fastICA':
            # Instanciate all FastIca class for each event and output to 
            # reconstruct signal in IcaRestore.py
            transformers = [decomposition.FastICA(n_components=None,
                                                algorithm=parameters['algorithm'],
                                                whiten=parameters['whiten'],
                                                fun=parameters['fun'],
                                                fun_args=None,
                                                max_iter=parameters['max_iter'],
                                                tol=parameters['tol'],
                                                w_init=None,
                                                random_state=parameters['random_state'])
                                                    for i in range(total_event)]

            components = []
            # Loop over events
            for signal, sample, chans, transformer in zip(signals_events, samples_events, channel_events, transformers):
                # sample is (n_channels, n_samples)
                # The fit_transform fonction take data with array-like of shape (n_samples, n_features)
                component = np.transpose(transformer.fit_transform(np.transpose(sample)))
                # component is (n_components, n_samples)
                for i, chan in enumerate(signal):
                    # Create new signal
                    new_signals_chan = chan.clone(clone_samples=False)
                    new_signals_chan.meta = {}
                    new_signals_chan.samples = component[i] #(n_samples,)
                    new_signals_chan.is_modified = True
                    new_signals_chan.alias = 'CMP'
                    new_signals_chan.channel = 'CMP_' + str(i)
                    new_signals_chan.meta['transformer'] = transformer
                    new_signals_chan.meta['chan_order'] = chans
                    components.append(new_signals_chan)
                pbar.update(1)

        elif parameters['ICA_algo']=='infomax':
            # Method with the ica1 function
            components = []
            for signal, sample, chans in zip(signals_events, samples_events, channel_events):
                n_components = sample.shape[0]
                # mixer, sources, unmixer = ica1(sample,n_components)
                #   w_mixer = [n_channels, n_components] or weights
                #   component = [n_components, n_samples] "activations or sources"
                #   unmixer = [n_components, n_components]
                w_mixer, component, w_unmixer = ica1(sample,n_components)
                for i, chan in enumerate(signal):
                    # Create new signal
                    new_signals_chan = chan.clone(clone_samples=False)
                    new_signals_chan.meta = {}
                    new_signals_chan.samples = component[i]
                    new_signals_chan.is_modified = True
                    new_signals_chan.alias = 'CMP'
                    new_signals_chan.channel = 'CMP_' + str(i)
                    new_signals_chan.meta['transformer'] = w_mixer
                    new_signals_chan.meta['chan_order'] = chans
                    components.append(new_signals_chan)
                pbar.update(1)

        #    # Method with the infomax model fitting
        #     n_components = samples_events[0].shape[0]
        #     models = [ica.ica(n_components=n_components) for i in range(total_event)]
        #     components = []
        #     # Loop over events
        #     for signal, sample, chans, model in zip(signals_events, samples_events, channel_events, models):
        #         # sample is (n_channels, n_samples)
        #         #   mix = [n_channels, n_components] or inv(weights)
        #         #   component = [n_components, n_samples] "activations or sources"
        #         model.ncomp = model.n_comp
        #         model = model.fit(sample)
        #         # sample is (n_channels, n_samples)
        #         #   ica1_mixer = [n_channels, n_components]
        #         #   ica1_unmixer = [n_components, n_components]
        #         #   ica1_component = [n_components, n_samples]
        #         # ica1_mixer, ica1_component, ica1_unmixer = ica.ica1(sample, n_components)
        #         for i, chan in enumerate(signal):
        #             # Create new signal
        #             new_signals_chan = chan.clone(clone_samples=False)
        #             new_signals_chan.meta = {}
        #             new_signals_chan.samples = model.sources[i] #(n_samples,)
        #             new_signals_chan.is_modified = True
        #             new_signals_chan.alias = 'CMP'
        #             new_signals_chan.channel = 'CMP_' + str(i)
        #             new_signals_chan.meta['transformer'] = model
        #             new_signals_chan.meta['chan_order'] = chans
        #             components.append(new_signals_chan)
        #         pbar.update(1)
        # pbar.close

        # Write the cache
        cache = {}
        cache['n_chan'] = len(channel_events[0])
        cache['signals'] = components
        self._cache_manager.write_mem_cache(self.identifier, cache)

        return {'components': components}     