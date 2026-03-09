# TaskFlow — Changelog

## v2.3.0 (2025-02-01)

### New Features
- Added task tagging system: tasks can have multiple string tags for categorization. Tags are searchable via the `GET /api/tasks?tags=bug,urgent` query parameter.
- Added bulk operations endpoint: `POST /api/tasks/bulk` accepts an array of task updates for batch processing. Maximum 50 operations per request.
- Added `archived` state to the task state machine. Done tasks can be archived to reduce clutter. Archived tasks are excluded from default list queries.

### Bug Fixes
- Fixed race condition in concurrent task updates that could cause lost writes. Implemented optimistic concurrency with version checking.
- Fixed pagination returning incorrect total count when filters were applied.
- Fixed API key validation not being case-insensitive, causing intermittent authentication failures.

### Breaking Changes
- The `DELETE /api/tasks/{id}` endpoint now requires admin permissions. Previously, any authenticated user could delete tasks.
- The `status` field in task responses now includes `archived` as a possible value. Clients that enumerate status values should be updated.

## v2.2.0 (2024-11-15)

### New Features
- Added rate limiting: 100 requests per minute per API key. Configurable via `API_RATE_LIMIT` environment variable.
- Added `due_date` field to tasks with ISO 8601 date format.
- Added overdue task notification system: tasks past their due date trigger notifications to the assignee.

### Improvements
- Improved query performance for large task lists by adding database indexes on `status`, `assignee`, and `priority` columns.
- Enhanced error responses with consistent format: `{error, code, details}`.

## v2.1.0 (2024-08-20)

### New Features
- Added project grouping: tasks can be organized into projects via the `project_id` field.
- Added `GET /api/projects` endpoint for project management.
- Added CORS support with configurable origins.

### Bug Fixes
- Fixed SQL injection vulnerability in the task search endpoint. All queries now use parameterized statements.
- Fixed memory leak in the notification service when processing large batches.

## v2.0.0 (2024-05-01)

### Major Changes
- Complete rewrite from Django to Flask for reduced complexity and faster startup.
- Switched from session-based auth to API key authentication.
- New three-layer architecture: API → Service → Data.
- SQLAlchemy 2.0 migration with async support preparation.

### Breaking Changes
- All endpoint paths changed from `/tasks/` to `/api/tasks/`.
- Authentication changed from cookie-based sessions to `X-API-Key` header.
- Response format standardized to JSON with consistent error structure.
