# Create a VerificationSession

Creates a VerificationSession object.

After the VerificationSession is created, display a verification modal using the session `client_secret` or send your users to the session’s `url`.

If your API key is in test mode, verification checks won’t actually process, though everything else will occur as if in live mode.

Related guide: [Verify your users’ identity documents](https://docs.stripe.com/docs/identity/verify-identity-documents.md)

## Returns

Returns the created VerificationSession object

## Parameters

- `client_reference_id` (string, optional)
  A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `options` (object, optional)
  A set of options for the session’s verification checks.

  - `options.document` (object, optional)
    Options that apply to the [document check](https://docs.stripe.com/docs/identity/verification-checks.md?type=document).

    - `options.document.allowed_types` (array of enums, optional)
      Array of strings of allowed identity document types. If the provided identity document isn’t one of the allowed types, the verification check will fail with a document_type_not_allowed error code.
Possible enum values:
      - `driving_license`
        Drivers license document type.

      - `id_card`
        ID card document type.

      - `passport`
        Passport document type.

    - `options.document.require_id_number` (boolean, optional)
      Collect an ID number and perform an [ID number check](https://docs.stripe.com/docs/identity/verification-checks.md?type=id-number) with the document’s extracted name and date of birth.

    - `options.document.require_live_capture` (boolean, optional)
      Disable image uploads, identity document images have to be captured using the device’s camera.

    - `options.document.require_matching_selfie` (boolean, optional)
      Capture a face image and perform a [selfie check](https://docs.stripe.com/docs/identity/verification-checks.md?type=selfie) comparing a photo ID and a picture of your user’s face. [Learn more](https://docs.stripe.com/docs/identity/selfie.md).

- `provided_details` (object, optional)
  Details provided about the user being verified. These details may be shown to the user.

  - `provided_details.email` (string, optional)
    Email of user being verified

    The maximum length is 800 characters.

  - `provided_details.phone` (string, optional)
    Phone number of user being verified

- `related_customer` (string, optional)
  Customer ID

- `related_customer_account` (string, optional)
  The ID of the Account representing a customer.

- `related_person` (object, optional)
  Tokens referencing a Person resource and it’s associated account.

  - `related_person.account` (string, required)
    A token representing a connected account. If provided, the person parameter is also required and must be associated with the account.

  - `related_person.person` (string, required)
    A token referencing a Person resource that this verification is being used to verify.

- `return_url` (string, optional)
  The URL that the user will be redirected to upon completing the verification flow.

- `type` (enum, optional)
  The type of [verification check](https://docs.stripe.com/docs/identity/verification-checks.md) to be performed. You must provide a `type` if not passing `verification_flow`.
Possible enum values:
  - `document`
    [Document check](https://docs.stripe.com/docs/identity/verification-checks.md?type=document).

  - `id_number`
    [ID number check](https://docs.stripe.com/docs/identity/verification-checks.md?type=id-number).

- `verification_flow` (string, optional)
  The ID of a verification flow from the Dashboard. See https://docs.stripe.com/identity/verification-flows.

```curl
curl https://api.stripe.com/v1/identity/verification_sessions \
  -u "<<YOUR_SECRET_KEY>>" \
  -d type=document
```

### Response

```json
{
  "id": "vs_1NuN4zLkdIwHu7ixleE6HvkI",
  "object": "identity.verification_session",
  "client_secret": "...",
  "created": 1695680197,
  "last_error": null,
  "last_verification_report": null,
  "livemode": false,
  "metadata": {},
  "options": {},
  "redaction": null,
  "status": "requires_input",
  "type": "document",
  "url": "..."
}
```
