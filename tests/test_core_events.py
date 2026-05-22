from app.core.events import event_dispatcher

def test_event_dispatcher_pub_sub():
    """Test core EventDispatcher subscribes and triggers listener functions correctly."""
    events_triggered = []
    
    def on_user_signup(user_id, email):
        events_triggered.append((user_id, email))
        
    # Subscribe
    event_dispatcher.subscribe('USER_SIGNUP', on_user_signup)
    
    # Dispatch
    event_dispatcher.dispatch('USER_SIGNUP', user_id=42, email='test@campusos.com')
    
    # Verify execution
    assert len(events_triggered) == 1
    assert events_triggered[0] == (42, 'test@campusos.com')
    
    # Unsubscribe
    event_dispatcher.unsubscribe('USER_SIGNUP', on_user_signup)
    event_dispatcher.dispatch('USER_SIGNUP', user_id=99, email='another@campusos.com')
    
    # Verify no second execution occurred
    assert len(events_triggered) == 1
