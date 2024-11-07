"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""

class ContextManager(dict):
    """ Context manager 
    
    Context manager is used to share information between steps in the step-by-step
    interface. It is a simple dictionary that publish an update through the 
    PubSubManager whenever a value is modified.

    Example uses:

    Inside a BaseStepView subclass, write the following line to add or change a 
    value to the context:
    
    self._context_manager['my_variable'] = 'variable_content'

    Inside another BaseStepView subclass where you need that value, listen
    to the context manager topic for any update and filter the result on the message

    def on_topic_update(self, topic, message, sender):
        if topic == self._context_manager.topic:
            if message == "my_variable"
                new_value = self._context_manager[message]
                do_something(new_value)
    """
    
    def __init__(self, pub_sub_manager, *args):
        """ Init th user directory based on the platform"""
        super().__init__(*args)
        self._pub_sub_manager = pub_sub_manager
        self._topic = "context_manager_topic"
        self._pub_sub_manager.clear_topic(self._topic)

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)
        self._pub_sub_manager.publish(self, self._topic, key)

    # Properties
    @property
    def topic(self):
        return self._topic
    
    # Public methods
    def unsubscribe_all_topics(self):
        self._pub_sub_manager.clear_topic(self._topic)
