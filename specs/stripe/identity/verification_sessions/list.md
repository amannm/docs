# List VerificationSessions

Returns a list of VerificationSessions

## Returns

List of VerificationSession objects that match the provided filter criteria.

## Parameters

- `client_reference_id` (string, optional)
  A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.

- `created` (object, optional)
  Only return VerificationSessions that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `related_customer` (string, optional)
  Customer ID

- `related_customer_account` (string, optional)
  The ID of the Account representing a customer.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Only return VerificationSessions with this status. [Learn more about the lifecycle of sessions](https://docs.stripe.com/docs/identity/how-sessions-work.md).
Possible enum values:
  - `canceled`
    The VerificationSession has been invalidated for future submission attempts.

  - `processing`
    The session has been submitted and is being processed. Most [verification checks](https://docs.stripe.com/docs/identity/verification-checks.md) are processed in less than 1 minute.

  - `requires_input`
    Requires user input before processing can continue.

  - `verified`
    Processing of all the verification checks are complete and successfully verified.

```curl
curl -G https://api.stripe.com/v1/identity/verification_sessions \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/identity/verification_sessions",
  "has_more": false,
  "data": [
    {
      "id": "vs_1NuNAILkdIwHu7ixh7OtGMLw",
      "object": "identity.verification_session",
      "client_secret": "...",
      "created": 1695680526,
      "last_error": null,
      "last_verification_report": null,
      "livemode": false,
      "metadata": {},
      "options": {
        "document": {
          "require_matching_selfie": true
        }
      },
      "redaction": null,
      "status": "requires_input",
      "type": "document",
      "url": "..."
    }
  ]
}
```
