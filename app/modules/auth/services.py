from app.modules.auth.models import User
from app.core.database import db

class AuthService:
    """Service handling Authentication Business Logic."""
    
    @staticmethod
    def register_user(email: str, password_raw: str, role: str) -> User:
        """Register a new user."""
        # Business logic goes here (Phase 1)
        pass

    @staticmethod
    def authenticate_user(email: str, password_raw: str) -> User:
        """Authenticate a user."""
        # Business logic goes here (Phase 1)
        pass
