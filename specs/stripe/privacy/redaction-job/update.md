# Update a redaction job

Updates the properties of a redaction job without running or canceling the job.

If the job to update is in a `failed` status, it will not automatically start to validate. Once you applied all of the changes, use the validate API to start validation again.

## Returns

Returns the RedactionJob object with the updated changes.

## Parameters

- `job` (string, required)
  RedactionJob object identifier

- `validation_behavior` (enum, optional)
  Determines the validation behavior of the job. Default is `error`.
Possible enum values:
  - `error`
    The job will generate a validation error for every object that cannot be redacted. If there are any errors, all of them will need to be resolved before the job can run.

  - `fix`
    The job will attempt to fix validation errors whenever possible. Some objects cannot be automatically fixed and will need to be resolved before the job can run.

```curl
curl https://api.stripe.com/v1/privacy/redaction_jobs/prj_123 \
  -u "<<YOUR_SECRET_KEY>>" \
  -d validation_behavior=error
```

### Response

```json
{
  "id": "prj_123",
  "object": "privacy.redaction_job",
  "created": 1234567890,
  "livemode": true,
  "status": "failed",
  "validation_behavior": "fix"
}
```
