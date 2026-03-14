# Validate a redaction job

Validate a redaction job when it is in a `failed` status.

When a job is created, it automatically begins to validate on the configured objects’ eligibility for redaction. Use this to validate the job again after its validation errors are resolved or the job’s `validation_behavior` is changed.

The status of the job will move to `validating`. Once all of the objects are validated, the status of the job will become `ready`. If there are any validation errors preventing the job from running, the status will become `failed`.

## Returns

Returns the RedactionJob object if successful. Otherwise, returns an error.

## Parameters

- `job` (string, required)
  RedactionJob object identifier

```curl
curl -X POST https://api.stripe.com/v1/privacy/redaction_jobs/prj_123/validate \
  -u "<<YOUR_SECRET_KEY>>"
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
