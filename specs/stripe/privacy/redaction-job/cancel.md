# Cancel a redaction job

You can cancel a redaction job when it’s in one of these statuses: `ready`, `failed`.

Canceling the redaction job will abandon its attempt to redact the configured objects. A canceled job cannot be used again.

## Returns

Returns the RedactionJob object if successful. Otherwise, returns an error.

## Parameters

- `job` (string, required)
  RedactionJob object identifier

```curl
curl -X POST https://api.stripe.com/v1/privacy/redaction_jobs/prj_123/cancel \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "prj_123",
  "object": "privacy.redaction_job",
  "created": 1234567890,
  "livemode": true,
  "status": "canceling",
  "validation_behavior": "error"
}
```
