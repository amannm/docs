# Verification Report

A VerificationReport is the result of an attempt to collect and verify data from a user. The collection of verification checks performed is determined from the `type` and `options` parameters used. You can find the result of each verification check performed in the appropriate sub-resource: `document`, `id_number`, `selfie`.

Each VerificationReport contains a copy of any data collected by the user as well as reference IDs which can be used to access collected images through the [FileUpload](https://docs.stripe.com/docs/api/files.md) API. To configure and create VerificationReports, use the [VerificationSession](https://docs.stripe.com/docs/api/identity/verification_sessions.md) API.

Related guide: [Accessing verification results](https://docs.stripe.com/docs/identity/verification-sessions.md#results).

## Endpoints

### Retrieve a VerificationReport

- [GET /v1/identity/verification_reports/:id](verification_reports/retrieve.md)

### List VerificationReports

- [GET /v1/identity/verification_reports](verification_reports/list.md)
