# CampusOS 2.0 API Documentation

This document defines the REST API standards, global patterns, and feature endpoints of the CampusOS 2.0 platform.

---

## 1. Global API Standards

### 1.1 Content Negotiation
- **JSON API**: JSON endpoints accept and return `application/json`.
- **HTMX Dynamic Endpoints**: HTMX-oriented routes return partial HTML fragments (`text/html`) to be dynamically swapped in the client DOM.

### 1.2 Authentication
- **Session Auth**: Used for the server-rendered web application (via `Flask-Login`).
- **Token Auth (Future Mobile Integration)**: Bearer JWT tokens in the `Authorization` header.

### 1.3 Standard Error Payload
For JSON response endpoints:
```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable error description",
    "details": {}
  }
}
```

---

## 2. Core Infrastructure Endpoints

### 2.1 System Health Check
Used by orchestrators (e.g. Docker, Kubernetes) to verify system readiness.

- **URL**: `/health`
- **Method**: `GET`
- **Auth Required**: No
- **Query Parameters**: None
- **Response**:
  - **Status Code**: `200 OK`
  - **Payload**:
    ```json
    {
      "status": "healthy",
      "timestamp": "2026-05-23T01:26:13Z",
      "services": {
        "database": "connected",
        "redis": "connected",
        "celery": "active"
      }
    }
    ```
  - **Status Code**: `503 Service Unavailable` (if any vital backend system is offline)
  - **Payload**:
    ```json
    {
      "status": "unhealthy",
      "timestamp": "2026-05-23T01:26:13Z",
      "services": {
        "database": "disconnected",
        "redis": "connected",
        "celery": "active"
      }
    }
    ```
