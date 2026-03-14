# Cancel a VerificationSession

A VerificationSession object can be canceled when it is in `requires_input` [status](https://docs.stripe.com/docs/identity/how-sessions-work.md).

Once canceled, future submission attempts are disabled. This cannot be undone. [Learn more](https://docs.stripe.com/docs/identity/verification-sessions.md#cancel).

## Returns

Returns the canceled VerificationSession object

```curl
curl -X POST https://api.stripe.com/v1/identity/verification_sessions/vs_1NuN3kLkdIwHu7ixk5OvTq3b/cancel \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "vs_1NuN3kLkdIwHu7ixk5OvTq3b",
  "object": "identity.verification_session",
  "client_secret": null,
  "created": 1695680120,
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
  "status": "canceled",
  "type": "document",
  "url": null
}
```
