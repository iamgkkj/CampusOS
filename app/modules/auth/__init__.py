from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Import routes and models to register them with the blueprint and metadata
from app.modules.auth import routes, models
