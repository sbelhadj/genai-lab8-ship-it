# TaskFlow — Frequently Asked Questions

## General

### Can TaskFlow replace Jira or Asana?

TaskFlow is designed for small-to-medium teams (5-30 members) who want a lightweight, self-hosted solution. It covers core task management features but does not include advanced features like Gantt charts, resource planning, or portfolio management. For teams that need those capabilities, a commercial tool may be more appropriate.

### Is TaskFlow free?

Yes. TaskFlow is released under the MIT License. You can use, modify, and distribute it freely, including in commercial products.

### What browsers are supported for the web UI?

TaskFlow's API is browser-independent since it's a REST API. The optional web dashboard (in the `frontend/` directory) supports Chrome 90+, Firefox 88+, Safari 14+, and Edge 90+.

## Technical

### How do I reset my API key?

Use the admin endpoint: `POST /api/auth/rotate-key` with your current API key in the header. This invalidates the old key and returns a new one. If you've lost your key, an admin can generate a new one via `flask reset-key --username your_username`.

### What is the maximum request body size?

The default maximum request body size is 1 MB (1,048,576 bytes). This can be configured via the `MAX_CONTENT_LENGTH` environment variable. Requests exceeding this limit receive a `413 Payload Too Large` response.

### How does TaskFlow handle concurrent updates?

TaskFlow uses optimistic concurrency control. Each task has a `version` field that is incremented on every update. When updating a task, include the current version in the request body. If the version doesn't match (another update occurred), the API returns `409 Conflict` with the current task state.

### Can I use PostgreSQL instead of SQLite?

Yes. Set the `DATABASE_URL` environment variable to your PostgreSQL connection string: `postgresql://user:password@host:5432/taskflow`. Then run `flask db upgrade` to create the schema. PostgreSQL is recommended for production deployments with more than 5 concurrent users.

### How do I back up the database?

For SQLite: copy the `taskflow.db` file. For PostgreSQL: use `pg_dump taskflow > backup.sql`. We recommend daily automated backups for production deployments.

## Troubleshooting

### I get "Invalid state transition" errors

Task state transitions follow a strict state machine. You cannot skip states — for example, a task cannot go from `open` directly to `done`. The valid transitions are: `open` → `in_progress` → `review` → `done` → `archived`. Additionally, `review` → `in_progress` is allowed (reject from review). Check that you're following the correct sequence.

### Tests fail with "database locked"

This occurs when multiple test processes access the same SQLite database file simultaneously. Use `pytest -p no:parallel` to disable parallel test execution, or switch to PostgreSQL for test runs with `DATABASE_URL=postgresql://...`.

### The API returns 500 errors

Check the logs at `logs/taskflow.log`. Common causes: database connection issues, missing environment variables, or unhandled exceptions in custom middleware. Enable `DEBUG` logging level for more detail.
