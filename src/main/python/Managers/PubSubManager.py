"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
DEBUG = False
from Managers.Manager import Manager

class PubSubManager(Manager):
    """
        PubSubManager is a basic implementation of the publisher/subscriber code pattern.
        This pattern allows loose communication between objects based on a common topic.

        You can:
        -   Subscribe/Unsubscribe to a topic
        -   Publish a message to a topic
        
        Subscriber must implement the function on_topic_update(topic, message) to receive 
        a message when a topic is updated.
    """
    def __init__(self, managers):
        """ Initialize the PubSubManager. """
        super().__init__(managers)
        self._topics = {}
        self._temp_topics = []

    def initialize(self):
        """ Initialize the PubSubManager."""
        pass

    def clear_temp_topics(self):
        """ Clear temporary topics 
        
        Topic coming from modules starts with the identifier of the node.
        ex: "b96c5849-1c9c-4b54-8965-c63ecf2fb2b6.input1"
        This topic are considered temporary to make it easier to unsubscribe them all
        at once when a process/tool is closed.
        """
        for topic in self._temp_topics:
            # Reverse search the _topics dictionary and if a key starts with topic, delete it
            for key in list(self._topics.keys())[::-1]:
                if key.startswith(topic):
                    del self._topics[key]
            
        self._temp_topics = []

    def clear_topic(self, topic):
        """ Clear a topic
            arguments:
                topic (str):    The topic to clear
         """
        if DEBUG: print(f'PubSubManager.clear_topic topic:{topic}')
        if topic in self._topics:
            del self._topics[topic]

    def subscribe(self, subscriber, topic):
        """ Subscribe to a topic

            Topic coming from modules starts with the identifier of the node.
            ex: "b96c5849-1c9c-4b54-8965-c63ecf2fb2b6.input1"
            This topic are considered temporary to make it easier to unsubscribe them all
            at once when a process/tool is closed.

            arguments:
                subscriber (object):    The subscriber interested in the topic
                topic (str):            The topic to subscribe to
        
         """
        if DEBUG: print(f'PubSubManager.subscribe topic:{topic} subscriber:{subscriber}')
        if topic not in self._topics:
            self._topics[topic] = []
        
        self._topics[topic].append(subscriber)

        # Check if the topic is a temporary topic
        # topic format for nodes starts with an id like: b96c5849-1c9c-4b54-8965-c63ecf2fb2b6
        if len(topic)> 35 and topic[8] == '-' and topic[13] == '-' and topic[18] == '-' and topic[23] == '-':
            # substring with the position of a dot
            identifier = topic[0:35]
            if identifier not in self._temp_topics:
                self._temp_topics.append(identifier)

    def unsubscribe(self, subscriber, topic):
        """ Unsubscribe to a topic

            arguments:
                subscriber (object):    The subscriber
                topic (str):            The topic to unsubscribe
        
         """
        if DEBUG: print(f'PubSubManager.unsubscribe topic:{topic} subscriber:{subscriber}')
        if topic in self._topics:
            if subscriber in self._topics[topic]:
                self._topics[topic].remove(subscriber)
                if len(self._topics[topic]) == 0:
                    del self._topics[topic]

    def publish(self, sender, topic, message):
        """ Publish a message to a topic

            arguments:
                sender (object):    The sender of the message
                topic (str):        The topic of the message
                message (object):   The message to publish
        
         """
        if DEBUG: print(f'PubSubManager.publish topic:{topic} message:{message}')
        if topic in self._topics:
            for subscriber in self._topics[topic]:
                if subscriber != sender:
                    if DEBUG: print(f'PubSubManager.calling on_topic_update {topic}:{message}')
                    try:
                        subscriber.on_topic_update(topic, message, sender)
                    except Exception as exc:
                        print(exc)
                        raise exc
        else:
            if DEBUG: print(f'PubSubManager.publics topic not found:{topic}') 
            else: 
                pass

    def clear(self):
        """ Clear the topics dictionary """
        self._topics = {}