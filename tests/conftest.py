import pytest
from app import create_app
from app.core.database import db as _db

@pytest.fixture(scope='session')
def app():
    """Create and configure a new Flask application instance for testing."""
    app = create_app('testing')
    
    # Establish application context
    with app.app_context():
        yield app

@pytest.fixture(scope='session')
def db(app):
    """Set up database schema for session scope testing."""
    _db.create_all()
    yield _db
    _db.drop_all()

@pytest.fixture(scope='function')
def db_session(db, app):
    """Provide a transactional database session for each test function."""
    connection = _db.engine.connect()
    transaction = connection.begin()
    
    # Bind session to the connection
    session = _db.scoped_session(options=dict(bind=connection))
    _db.session = session
    
    yield session
    
    # Roll back transactions after test complete to maintain isolation
    transaction.rollback()
    connection.close()
    session.remove()

@pytest.fixture
def client(app):
    """Provide a test client for the application."""
    return app.test_client()
