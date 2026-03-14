# List all redaction jobs

Returns a list of redaction jobs.

## Returns

Returns a list of RedactionJob objects.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl https://api.stripe.com/v1/privacy/redaction_jobs \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "object": "list",
  "url": "/v1/privacy/redaction_jobs",
  "has_more": false,
  "data": [
    {
      "id": "prj_123",
      "object": "privacy.redaction_job",
      "created": 1234567890,
      "livemode": true,
      "status": "validating",
      "validation_behavior": "error"
    },
    {
      "id": "prj_456",
      "object": "privacy.redaction_job",
      "created": 1234567890,
      "livemode": true,
      "status": "success",
      "validation_behavior": "fix"
    }
  ]
}
```
