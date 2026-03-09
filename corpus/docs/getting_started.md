# TaskFlow — Getting Started

## Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git
- SQLite (included with Python) or PostgreSQL 14+ for production

## Installation

1. Clone the repository:
```bash
git clone https://github.com/taskflow/taskflow.git
cd taskflow
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
flask db upgrade
```

5. Create an admin user and API key:
```bash
flask create-admin --username admin --email admin@example.com
```
This outputs an API key like `tk_abc123def456`. Save it securely.

6. Run the development server:
```bash
flask run --debug
```
The API is available at `http://localhost:5000/api/`.

## Running Tests

TaskFlow uses pytest for testing:

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage report
python -m pytest tests/ --cov=app --cov-report=html

# Run only unit tests (faster)
python -m pytest tests/unit/ -v

# Run integration tests (requires database)
python -m pytest tests/integration/ -v
```

Test coverage target is 85%. The CI pipeline fails if coverage drops below this threshold.

## Configuration

TaskFlow uses environment variables for configuration:

| Variable | Default | Description |
|----------|---------|-------------|
| `FLASK_ENV` | `development` | Environment: `development`, `testing`, `production` |
| `DATABASE_URL` | `sqlite:///taskflow.db` | Database connection string |
| `SECRET_KEY` | (generated) | Flask secret key for session signing |
| `API_RATE_LIMIT` | `100` | Requests per minute per API key |
| `LOG_LEVEL` | `INFO` | Logging level: `DEBUG`, `INFO`, `WARNING`, `ERROR` |
| `CORS_ORIGINS` | `*` | Allowed CORS origins (comma-separated) |

For production, set these in a `.env` file or your deployment platform's environment configuration.

## Development Workflow

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Write tests first (TDD encouraged)
3. Implement the feature
4. Run tests: `pytest tests/ -v`
5. Create a pull request with description and test evidence
6. Code review by at least one team member
7. Merge to `main` after approval and CI passes
