from app.core.database import BaseModel, db

# Define placeholders or empty class structures for User during Phase 0 scaffolding.
# Will be fully populated in Phase 1.
class User(BaseModel):
    """User Model representing platform users (Student, Teacher, Admin)."""
    __tablename__ = 'users'
    
    # We define a basic schema to allow app factory and tests to initialize
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False) # student, teacher, admin
    is_active = db.Column(db.Boolean, default=True, nullable=False)
