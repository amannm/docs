# Run a redaction job

Run a redaction job in a `ready` status.

When you run a job, the configured objects will be redacted asynchronously. This action is irreversible and cannot be canceled once started.

The status of the job will move to `redacting`. Once all of the objects are redacted, the status will become `succeeded`. If the job’s `validation_behavior` is set to `fix`, the automatic fixes will be applied to objects at this step.

## Returns

Returns the RedactionJob object if successful. Otherwise, returns an error.

## Parameters

- `job` (string, required)
  RedactionJob object identifier

```curl
curl -X POST https://api.stripe.com/v1/privacy/redaction_jobs/prj_123/run \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "prj_123",
  "object": "privacy.redaction_job",
  "created": 1234567890,
  "livemode": true,
  "status": "redacting",
  "validation_behavior": "error"
}
```
