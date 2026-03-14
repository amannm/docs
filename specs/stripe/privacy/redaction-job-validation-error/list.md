# List all validation errors

Returns a list of validation errors for the specified redaction job.

## Returns

Returns a list of RedactionJob validation error objects.

## Parameters

- `job` (string, required)
  RedactionJob object identifier

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl https://api.stripe.com/v1/privacy/redaction_jobs/prj_123/validation_errors \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "object": "list",
  "url": "/v1/privacy/redaction_jobs/prj_123/validation_errors",
  "has_more": false,
  "data": [
    {
      "id": "prjve_123",
      "object": "privacy.redaction_job_validation_error",
      "code": "invalid_state",
      "erroring_object": {
        "id": "pi_123",
        "object_type": "payment_intent"
      },
      "message": "PaymentIntent is not finalized. Confirm or cancel the payment intent."
    }
  ]
}
```
