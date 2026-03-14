# Redaction Job

The Redaction Job object redacts Stripe objects. You can use it to coordinate the removal of personal information from selected objects, making them permanently inaccessible in the Stripe Dashboard and API.

## Endpoints

### Create a redaction job

- [POST /v1/privacy/redaction_jobs](redaction-job/create.md)

### Update a redaction job

- [POST /v1/privacy/redaction_jobs/:id](redaction-job/update.md)

### Retrieve a redaction job

- [GET /v1/privacy/redaction_jobs/:id](redaction-job/retrieve.md)

### List all redaction jobs

- [GET /v1/privacy/redaction_jobs](redaction-job/list.md)

### Cancel a redaction job

- [POST /v1/privacy/redaction_jobs/:id/cancel](redaction-job/cancel.md)

### Run a redaction job

- [POST /v1/privacy/redaction_jobs/:id/run](redaction-job/run.md)

### Validate a redaction job

- [POST /v1/privacy/redaction_jobs/:id/validate](redaction-job/validate.md)
