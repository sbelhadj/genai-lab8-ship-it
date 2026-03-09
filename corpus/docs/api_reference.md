# TaskFlow — API Reference

## Authentication

All API requests require an API key passed in the `X-API-Key` header. API keys are generated per user through the admin interface or the `/api/auth/create-key` endpoint.

```
GET /api/tasks
Headers:
  X-API-Key: tk_abc123def456
```

Invalid or missing API keys return a `401 Unauthorized` response with the body `{"error": "Invalid or missing API key"}`.

## Task Endpoints

### List Tasks

```
GET /api/tasks
```

Query parameters:
- `status` (optional): Filter by task status. Values: `open`, `in_progress`, `review`, `done`, `archived`.
- `assignee` (optional): Filter by assignee username.
- `priority` (optional): Filter by priority. Values: `low`, `medium`, `high`, `critical`.
- `project_id` (optional): Filter by project ID.
- `page` (optional, default=1): Page number for pagination.
- `per_page` (optional, default=20, max=100): Items per page.

Response: `200 OK` with JSON array of task objects.

### Create Task

```
POST /api/tasks
Content-Type: application/json
```

Required fields:
- `title` (string, 1-200 characters): Task title.

Optional fields:
- `description` (string, max 5000 characters): Detailed description.
- `priority` (string, default "medium"): One of `low`, `medium`, `high`, `critical`.
- `assignee` (string): Username of the assignee.
- `project_id` (integer): ID of the parent project.
- `due_date` (string, ISO 8601 format): Due date, e.g. `2025-03-15`.
- `tags` (array of strings): Labels for categorization.

Response: `201 Created` with the created task object.

### Get Task

```
GET /api/tasks/{task_id}
```

Response: `200 OK` with the task object, or `404 Not Found`.

### Update Task

```
PATCH /api/tasks/{task_id}
Content-Type: application/json
```

Any field from the create endpoint can be updated. State transitions are validated:
- `open` → `in_progress` (requires assignee)
- `in_progress` → `review`
- `review` → `done` or `review` → `in_progress` (reject)
- `done` → `archived`

Invalid transitions return `400 Bad Request` with `{"error": "Invalid state transition from X to Y"}`.

### Delete Task

```
DELETE /api/tasks/{task_id}
```

Response: `204 No Content`. Only admins can delete tasks. Non-admin users receive `403 Forbidden`.

## Task Object Schema

```json
{
  "id": 42,
  "title": "Fix login timeout bug",
  "description": "Users report session expiry after 5 minutes...",
  "status": "in_progress",
  "priority": "high",
  "assignee": "alice",
  "project_id": 7,
  "due_date": "2025-03-15",
  "tags": ["bug", "auth"],
  "created_at": "2025-01-10T14:30:00Z",
  "updated_at": "2025-01-12T09:15:00Z",
  "created_by": "bob"
}
```

## Error Responses

All errors follow a consistent format:

```json
{
  "error": "Human-readable error message",
  "code": "ERROR_CODE",
  "details": {}
}
```

Common error codes:
- `INVALID_API_KEY`: Authentication failed.
- `FORBIDDEN`: Insufficient permissions.
- `NOT_FOUND`: Resource does not exist.
- `VALIDATION_ERROR`: Request body failed validation. `details` contains field-level errors.
- `INVALID_STATE_TRANSITION`: Task state change is not allowed.
- `RATE_LIMITED`: Too many requests. Retry after the `Retry-After` header value.

## Rate Limiting

The API enforces rate limits of 100 requests per minute per API key. When exceeded, the API returns `429 Too Many Requests` with a `Retry-After` header indicating how many seconds to wait.
