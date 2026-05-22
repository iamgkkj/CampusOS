from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime

class Base(DeclarativeBase):
    """Custom declarative base for SQLAlchemy models."""
    pass

db = SQLAlchemy(model_class=Base)

class BaseModel(db.Model):
    """Abstract Base Model for all domain models, tracking standard metadata."""
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    def save(self):
        """Save standard utility method."""
        db.session.add(self)
        db.session.commit()
        return self
        
    def delete(self):
        """Delete standard utility method."""
        db.session.delete(self)
        db.session.commit()
