# Redact a VerificationSession

Redact a VerificationSession to remove all collected information from Stripe. This will redact the VerificationSession and all objects related to it, including VerificationReports, Events, request logs, etc.

A VerificationSession object can be redacted when it is in `requires_input` or `verified` [status](https://docs.stripe.com/docs/identity/how-sessions-work.md). Redacting a VerificationSession in `requires_action` state will automatically cancel it.

The redaction process may take up to four days. When the redaction process is in progress, the VerificationSession’s `redaction.status` field will be set to `processing`; when the process is finished, it will change to `redacted` and an `identity.verification_session.redacted` event will be emitted.

Redaction is irreversible. Redacted objects are still accessible in the Stripe API, but all the fields that contain personal data will be replaced by the string `[redacted]` or a similar placeholder. The `metadata` field will also be erased. Redacted objects cannot be updated or used for any purpose.

[Learn more](https://docs.stripe.com/docs/identity/verification-sessions.md#redact).

## Returns

Returns the redacted VerificationSession object

```curl
curl -X POST https://api.stripe.com/v1/identity/verification_sessions/vs_1NuN3kLkdIwHu7ixk5OvTq3b/redact \
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
  "redaction": {
    "status": "processing"
  },
  "status": "canceled",
  "type": "document",
  "url": null
}
```
