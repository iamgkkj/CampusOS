from functools import wraps
from flask import abort
from flask_login import current_user
from app.core.exceptions import ForbiddenError

def has_role(*roles):
    """Decorator or helper to check if the current user possesses one of the specified roles."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)
            # We assume current_user has a 'role' attribute.
            # In Phase 0 models, this will be defined during Phase 1.
            user_role = getattr(current_user, 'role', None)
            if user_role not in roles:
                raise ForbiddenError(f"User role '{user_role}' is not authorized to access this resource.")
            return f(*args, **kwargs)
        return decorated_function
    return decorator
