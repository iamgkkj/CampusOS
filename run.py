import os
from app import create_app, socketio, celery_init_app

app = create_app(os.environ.get('FLASK_ENV', 'development'))
celery = celery_init_app(app)

if __name__ == '__main__':
    # Run the application with SocketIO
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    
    app.logger.info(f"Starting CampusOS 2.0 on {host}:{port}")
    socketio.run(app, host=host, port=port, debug=app.debug)
