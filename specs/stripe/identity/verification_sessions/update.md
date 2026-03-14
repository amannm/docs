# Update a VerificationSession

Updates a VerificationSession object.

When the session status is `requires_input`, you can use this method to update the verification check and options.

## Returns

Returns the updated VerificationSession object

## Parameters

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

- `type` (enum, optional)
  The type of [verification check](https://docs.stripe.com/docs/identity/verification-checks.md) to be performed.
Possible enum values:
  - `document`
    [Document check](https://docs.stripe.com/docs/identity/verification-checks.md?type=document).

  - `id_number`
    [ID number check](https://docs.stripe.com/docs/identity/verification-checks.md?type=id-number).

```curl
curl https://api.stripe.com/v1/identity/verification_sessions/vs_1NuN9WLkdIwHu7ix597AR9uz \
  -u "<<YOUR_SECRET_KEY>>" \
  -d type=id_number
```

### Response

```json
{
  "id": "vs_1NuN9WLkdIwHu7ix597AR9uz",
  "object": "identity.verification_session",
  "client_secret": "...",
  "created": 1695680478,
  "last_error": null,
  "last_verification_report": null,
  "livemode": false,
  "metadata": {},
  "options": {},
  "redaction": null,
  "status": "requires_input",
  "type": "id_number",
  "url": "..."
}
```
