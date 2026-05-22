# CampusOS 2.0 🎓

CampusOS 2.0 is a modern, enterprise-ready **Education Management Platform** designed for teachers, students, and administrators. Built from the ground up as a **Modular Monolith**, the platform integrates real-time communications, automated grading pipelines, manual/face-recognition attendance tracking, and intuitive dashboards.

## Project Heritage

This project is the successor to EDUcheck, an earlier educational management platform prototype.

Original Repository:
https://github.com/iamgkkj/EDUcheck

CampusOS is a complete redesign focused on modular architecture, scalability, maintainability, and production readiness while preserving the core vision of EDUcheck.

---

## 🚀 Tech Stack

CampusOS 2.0 leverages a robust, performant stack optimized for responsiveness and maintainability:

*   **Core Backend**: Python, Flask, Flask-SQLAlchemy (ORM), Flask-Login, Flask-SocketIO (Real-time).
*   **Asynchronous Processing**: Celery with Redis (Message Broker & Result Backend).
*   **Database**: PostgreSQL for strong transactional integrity.
*   **Modern Frontend**: Server-rendered Jinja2 templates styled with TailwindCSS, enhanced with **HTMX** for partial DOM swaps, and **Alpine.js** for client-side micro-interactions.
*   **Testing**: Pytest with automated transactional isolation.
*   **Infrastructure**: Docker & Docker Compose.

---

## 🏛 Architecture Blueprint

The platform uses a **Modular Monolith** style. Each domain (e.g., `auth`, `courses`, `assignments`) resides in a self-contained module in `app/modules/`.

### Core Rules:
1.  **Service Layer**: All business logic and database queries exist within services (`services.py`).
2.  **Thin Routes**: Routes (`routes.py`) only validate input, call services, and return the response.
3.  **Event-Driven**: Modules communicate via a central synchronous `EventDispatcher` or asynchronously through `Celery`.
4.  **Strict Layout**: Every module implements a uniform structure:
    ```
    app/modules/<domain>/
    ├── __init__.py
    ├── models.py
    ├── schemas.py
    ├── services.py
    ├── routes.py
    ├── forms.py
    └── permissions.py
    ```

---

## 🛠 Project Scaffolding Structure

```
/
├── app/
│   ├── __init__.py          # Flask app factory & Extension initialization
│   ├── config.py            # Configuration modes (Dev, Test, Prod)
│   ├── core/                # Shared utilities (DB, Events, Exceptions, Security)
│   └── modules/             # Domain modules
│       └── auth/            # Scaffolding layout for Authentication
├── docs/
│   ├── Context.md           # Single source of truth for project status
│   ├── Architecture.md      # Detailed application architectural blueprint
│   └── API.md               # API endpoint definitions and payloads
├── tests/                   # Pytest test suites
├── migrations/              # Database migration history (Alembic)
├── Dockerfile               # Multi-stage container specification
├── docker-compose.yml       # Production/development stack orchestration
├── requirements.txt         # Package dependencies
└── run.py                   # Main application entry point
```

---

## 📦 Getting Started

### 1. Local Development Setup

Clone the repository and enter the directory:
```bash
cd CampusOS
```

Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

### 2. Run Database & Cache via Docker

Start PostgreSQL and Redis:
```bash
docker compose up -d postgres redis
```

Generate/apply the migrations:
```bash
export FLASK_APP=run.py
export FLASK_ENV=development
flask db upgrade
```

### 3. Run the Application

Start the Flask web app:
```bash
python run.py
```

The application will be running on `http://localhost:5000`. You can test the system health at `http://localhost:5000/health`.

To run the Celery worker for background tasks:
```bash
celery -A run.celery worker --loglevel=info
```

### 4. Running the Complete Stack in Docker

To build and run all services (Web, Worker, DB, Redis) fully containerized:
```bash
docker compose up --build
```

---

## 🧪 Testing

The testing suite utilizes `pytest` and runs with isolated database transactions:

```bash
PYTHONPATH=. pytest
```

---

## 📄 Migration from EDUcheck

- Modernized architecture
- Improved modularity
- Enhanced scalability
- Better testing strategy
- Cleaner service-oriented design
- Future-ready API layer
- Improved developer experience

---

## 📄 Documentation Directory

For deep-dives into our architectural paradigms, API models, and implementation roadmaps, consult the `/docs` folder:
*   [Architecture Blueprint](file:///home/gopal/Documents/project/CampusOS/docs/Architecture.md)
*   [API Schema Guide](file:///home/gopal/Documents/project/CampusOS/docs/API.md)
*   [Project Context & Status](file:///home/gopal/Documents/project/CampusOS/docs/Context.md)
