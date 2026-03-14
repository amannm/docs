# Verification Session

A VerificationSession guides you through the process of collecting and verifying the identities of your users. It contains details about the type of verification, such as what [verification check](https://docs.stripe.com/docs/identity/verification-checks.md) to perform. Only create one VerificationSession for each verification in your system.

A VerificationSession transitions through [multiple statuses](https://docs.stripe.com/docs/identity/how-sessions-work.md) throughout its lifetime as it progresses through the verification flow. The VerificationSession contains the user’s verified data after verification checks are complete.

Related guide: [The Verification Sessions API](https://docs.stripe.com/docs/identity/verification-sessions.md)

## Endpoints

### Create a VerificationSession

- [POST /v1/identity/verification_sessions](verification_sessions/create.md)

### Update a VerificationSession

- [POST /v1/identity/verification_sessions/:id](verification_sessions/update.md)

### Retrieve a VerificationSession

- [GET /v1/identity/verification_sessions/:id](verification_sessions/retrieve.md)

### List VerificationSessions

- [GET /v1/identity/verification_sessions](verification_sessions/list.md)

### Cancel a VerificationSession

- [POST /v1/identity/verification_sessions/:id/cancel](verification_sessions/cancel.md)

### Redact a VerificationSession

- [POST /v1/identity/verification_sessions/:id/redact](verification_sessions/redact.md)
