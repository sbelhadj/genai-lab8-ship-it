# TaskFlow — Project Overview

## What is TaskFlow?

TaskFlow is an open-source task management REST API built with Python and Flask. It provides endpoints for creating, assigning, tracking, and reporting on tasks across software development teams. TaskFlow is designed for small-to-medium engineering teams who need a lightweight, self-hosted alternative to commercial project management tools.

## Architecture

TaskFlow follows a three-layer architecture:

- **API Layer** (Flask blueprints): Handles HTTP requests, input validation, and response formatting. All endpoints return JSON responses with standard HTTP status codes.
- **Service Layer** (business logic): Contains the core domain logic for task management, including state transitions, assignment rules, and notification triggers.
- **Data Layer** (SQLAlchemy + SQLite): Manages persistence using SQLAlchemy ORM with SQLite as the default database. PostgreSQL is supported for production deployments.

## Key Design Decisions

TaskFlow uses a stateless REST architecture with no server-side sessions. Authentication is handled via API keys passed in the `X-API-Key` header. Each API key is associated with a user account and has configurable permissions (read, write, admin).

The task state machine supports five states: `open`, `in_progress`, `review`, `done`, and `archived`. State transitions are validated by the service layer — for example, a task cannot move directly from `open` to `done` without passing through `in_progress`.

## Technology Stack

- **Language:** Python 3.11+
- **Framework:** Flask 3.0 with Flask-RESTful
- **ORM:** SQLAlchemy 2.0
- **Database:** SQLite (development), PostgreSQL (production)
- **Testing:** pytest with pytest-cov for coverage
- **Documentation:** Sphinx with autodoc
- **CI/CD:** GitHub Actions

## Project Structure

```
taskflow/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models/              # SQLAlchemy models
│   │   ├── task.py          # Task model with state machine
│   │   ├── user.py          # User model with permissions
│   │   └── project.py       # Project model
│   ├── api/                 # Flask blueprints
│   │   ├── tasks.py         # /api/tasks endpoints
│   │   ├── users.py         # /api/users endpoints
│   │   └── projects.py      # /api/projects endpoints
│   ├── services/            # Business logic
│   │   ├── task_service.py  # Task CRUD + state transitions
│   │   └── auth_service.py  # API key validation
│   └── utils/               # Shared utilities
├── tests/                   # pytest test suite
├── migrations/              # Alembic migrations
├── config.py                # Configuration management
└── requirements.txt         # Dependencies
```
