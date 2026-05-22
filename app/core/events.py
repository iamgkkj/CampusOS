from collections import defaultdict
import logging

logger = logging.getLogger(__name__)

class EventDispatcher:
    """Synchronous Event Dispatcher to enable decoupled communication between modules."""
    
    def __init__(self):
        self._listeners = defaultdict(list)
        
    def subscribe(self, event_type: str, listener_fn):
        """Subscribe a callable to an event type."""
        if listener_fn not in self._listeners[event_type]:
            self._listeners[event_type].append(listener_fn)
            logger.debug(f"Subscribed {listener_fn.__name__} to event {event_type}")
            
    def unsubscribe(self, event_type: str, listener_fn):
        """Unsubscribe a callable from an event type."""
        if listener_fn in self._listeners[event_type]:
            self._listeners[event_type].remove(listener_fn)
            logger.debug(f"Unsubscribed {listener_fn.__name__} from event {event_type}")
            
    def dispatch(self, event_type: str, **kwargs):
        """Synchronously dispatch an event to all subscribers."""
        logger.info(f"Dispatching event: {event_type} with parameters: {list(kwargs.keys())}")
        for listener in self._listeners[event_type]:
            try:
                listener(**kwargs)
            except Exception as e:
                logger.error(f"Error executing listener {listener.__name__} for event {event_type}: {e}", exc_info=True)

# Global dispatcher instance
event_dispatcher = EventDispatcher()
