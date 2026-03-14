# Retrieve a redaction job

Retrieves the details of a previously created redaction job.

## Returns

Returns the RedactionJob object.

## Parameters

- `job` (string, required)
  RedactionJob object identifier

```curl
curl https://api.stripe.com/v1/privacy/redaction_jobs/prj_123 \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "prj_123",
  "object": "privacy.redaction_job",
  "created": 1234567890,
  "livemode": true,
  "status": "ready",
  "validation_behavior": "error"
}
```
