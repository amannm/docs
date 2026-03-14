# Create a redaction job

Creates a redaction job. When a job is created, it will start to validate.

## Returns

Returns the newly created RedactionJob object.

## Parameters

- `objects` (object, required)
  The objects to redact. These root objects and their related ones will be validated for redaction.

- `validation_behavior` (enum, optional)
  Determines the validation behavior of the job. Default is `error`.
Possible enum values:
  - `error`
    The job will generate a validation error for every object that cannot be redacted. If there are any errors, all of them will need to be resolved before the job can run.

  - `fix`
    The job will attempt to fix validation errors whenever possible. Some objects cannot be automatically fixed and will need to be resolved before the job can run.

```curl
curl https://api.stripe.com/v1/privacy/redaction_jobs \
  -u "<<YOUR_SECRET_KEY>>" \
  -d validation_behavior=error \
  -d "objects[customers][]"=cus_123
```

### Response

```json
{
  "id": "prj_123",
  "object": "privacy.redaction_job",
  "created": 1234567890,
  "livemode": true,
  "status": "validating",
  "validation_behavior": "error"
}
```
