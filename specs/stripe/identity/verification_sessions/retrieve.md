# Retrieve a VerificationSession

Retrieves the details of a VerificationSession that was previously created.

When the session status is `requires_input`, you can use this method to retrieve a valid `client_secret` or `url` to allow re-submission.

## Returns

Returns a VerificationSession object

```curl
curl https://api.stripe.com/v1/identity/verification_sessions/vs_1NuNAILkdIwHu7ixh7OtGMLw \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
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
```
