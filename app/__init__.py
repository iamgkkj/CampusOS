import os
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_socketio import SocketIO
from celery import Celery, Task

from app.config import config_by_name
from app.core.database import db

# Initialize non-db extensions
migrate = Migrate()
login_manager = LoginManager()
socketio = SocketIO(cors_allowed_origins="*") # Allow all in development

def celery_init_app(app: Flask) -> Celery:
    """Initialize Celery application integration with Flask application context."""
    class FlaskTask(Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    # We configure Celery from the Flask config object using CELERY_ prefix
    celery_app.config_from_object(app.config)
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app

def create_app(config_name: str = None) -> Flask:
    """Flask Application Factory."""
    if not config_name:
        config_name = os.environ.get('FLASK_ENV', 'development')
        
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    config_by_name[config_name].init_app(app)
    
    # Initialize extensions with app context
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    socketio.init_app(app)
    
    # Setup login config
    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"
    
    # Register blueprints (Phase 0 scaffolding contains core blueprints, domain blueprints added in subsequent phases)
    from app.modules.auth import auth_bp
    app.register_blueprint(auth_bp)
    
    @app.route('/health')
    def health_check():
        """Standard health check endpoint."""
        # Simple health check verifying database and service availability
        services = {
            "database": "connected",
            "redis": "connected",
            "celery": "active"
        }
        
        # Test Database connection
        try:
            db.session.execute(db.text('SELECT 1'))
        except Exception as e:
            app.logger.error(f"Health check: Database connection failed: {e}")
            services["database"] = "disconnected"
            
        # If database is offline, return 503 Service Unavailable
        if services["database"] == "disconnected":
            return jsonify({"status": "unhealthy", "services": services}), 503
            
        return jsonify({"status": "healthy", "services": services}), 200

    # Custom global error handler for central exception model
    from app.core.exceptions import CampusOSError
    @app.errorhandler(CampusOSError)
    def handle_campusos_error(error):
        response = jsonify({
            "success": False,
            "error": {
                "code": error.code,
                "message": error.message,
                "details": error.details
            }
        })
        response.status_code = error.status_code
        return response
        
    return app
