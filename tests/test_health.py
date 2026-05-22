def test_health_check_healthy(client):
    """Test health check route returns 200 OK and healthy status payload."""
    response = client.get('/health')
    assert response.status_code == 200
    
    data = response.get_json()
    assert data is not None
    assert data["status"] == "healthy"
    assert "database" in data["services"]
    assert "redis" in data["services"]
    assert "celery" in data["services"]
    assert data["services"]["database"] == "connected"
