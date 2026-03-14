# The VerificationReport object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `client_reference_id` (string, nullable)
  A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `document` (object, nullable)
  Result of the document check for this report.

  - `document.address` (object, nullable)
    Address as it appears in the document.

    - `document.address.city` (string, nullable)
      City, district, suburb, town, or village.

    - `document.address.country` (string, nullable)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `document.address.line1` (string, nullable)
      Address line 1, such as the street, PO Box, or company name.

    - `document.address.line2` (string, nullable)
      Address line 2, such as the apartment, suite, unit, or building.

    - `document.address.postal_code` (string, nullable)
      ZIP or postal code.

    - `document.address.state` (string, nullable)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `document.dob` (object, nullable, expandable (can be expanded into an object with the `expand` request parameter))
    Date of birth as it appears in the document.

    - `document.dob.day` (integer, nullable)
      Numerical day between 1 and 31.

    - `document.dob.month` (integer, nullable)
      Numerical month between 1 and 12.

    - `document.dob.year` (integer, nullable)
      The four-digit year.

  - `document.error` (object, nullable)
    Details on the verification error. Present when status is `unverified`.

    - `document.error.code` (enum, nullable)
      A short machine-readable string giving the reason for the verification failure.
Possible enum values:
      - `document_expired`
        The provided identity document has expired.

      - `document_type_not_supported`
        The provided identity document isn’t one of the session’s [allowed document types](https://docs.stripe.com/docs/api/identity/verification_sessions/create.md#create_identity_verification_session-options-document-allow_document_types).

      - `document_unverified_other`
        Stripe couldn’t verify the provided identity document. See the [list of supported document types](https://docs.stripe.com/docs/identity/verification-checks.md?type=document).

    - `document.error.reason` (string, nullable)
      A human-readable message giving the reason for the failure. These messages can be shown to your users.

  - `document.expiration_date` (object, nullable, expandable (can be expanded into an object with the `expand` request parameter))
    Expiration date of the document.

    - `document.expiration_date.day` (integer, nullable)
      Numerical day between 1 and 31.

    - `document.expiration_date.month` (integer, nullable)
      Numerical month between 1 and 12.

    - `document.expiration_date.year` (integer, nullable)
      The four-digit year.

  - `document.files` (array of strings, nullable)
    Array of [File](https://docs.stripe.com/docs/api/files.md) ids containing images for this document.

  - `document.first_name` (string, nullable)
    First name as it appears in the document.

  - `document.issued_date` (object, nullable)
    Issued date of the document.

    - `document.issued_date.day` (integer, nullable)
      Numerical day between 1 and 31.

    - `document.issued_date.month` (integer, nullable)
      Numerical month between 1 and 12.

    - `document.issued_date.year` (integer, nullable)
      The four-digit year.

  - `document.issuing_country` (string, nullable)
    Issuing country of the document.

  - `document.last_name` (string, nullable)
    Last name as it appears in the document.

  - `document.number` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
    Document ID number.

  - `document.sex` (enum, nullable, expandable (can be expanded into an object with the `expand` request parameter))
    Sex of the person in the document.
Possible enum values:
    - `[redacted]`
      The verification has been redacted.

    - `female`
      Female

    - `male`
      Male

    - `unknown`
      Could not determine the user’s sex.

  - `document.status` (enum)
    Status of this `document` check.
Possible enum values:
    - `unverified`
      The data being checked was not able to be verified.

    - `verified`
      The check resulted in a successful verification.

  - `document.type` (enum, nullable)
    Type of the document.
Possible enum values:
    - `driving_license`
      Drivers license document type.

    - `id_card`
      ID card document type.

    - `passport`
      Passport document type.

  - `document.unparsed_place_of_birth` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
    Place of birth as it appears in the document.

  - `document.unparsed_sex` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
    Sex as it appears in the document.

- `email` (object, nullable)
  Result of the email check for this report.

  - `email.email` (string, nullable)
    Email to be verified.

  - `email.error` (object, nullable)
    Details on the verification error. Present when status is `unverified`.

    - `email.error.code` (enum, nullable)
      A short machine-readable string giving the reason for the verification failure.
Possible enum values:
      - `email_unverified_other`
        Stripe was unable to verify the provided email address.

      - `email_verification_declined`
        The user was unable to verify the provided email address.

    - `email.error.reason` (string, nullable)
      A human-readable message giving the reason for the failure. These messages can be shown to your users.

  - `email.status` (enum)
    Status of this `email` check.
Possible enum values:
    - `unverified`
      The data being checked was not able to be verified.

    - `verified`
      The check resulted in a successful verification.

- `id_number` (object, nullable)
  Result of the id number check for this report.

  - `id_number.dob` (object, nullable, expandable (can be expanded into an object with the `expand` request parameter))
    Date of birth.

    - `id_number.dob.day` (integer, nullable)
      Numerical day between 1 and 31.

    - `id_number.dob.month` (integer, nullable)
      Numerical month between 1 and 12.

    - `id_number.dob.year` (integer, nullable)
      The four-digit year.

  - `id_number.error` (object, nullable)
    Details on the verification error. Present when status is `unverified`.

    - `id_number.error.code` (enum, nullable)
      A short machine-readable string giving the reason for the verification failure.
Possible enum values:
      - `id_number_insufficient_document_data`
        The provided document didn’t contain enough data to match against the ID number.

      - `id_number_mismatch`
        The information provided couldn’t be matched against global databases.

      - `id_number_unverified_other`
        The information provided couldn’t be verified. See the [list of supported ID numbers](https://docs.stripe.com/docs/identity/verification-checks.md?type=id-number).

    - `id_number.error.reason` (string, nullable)
      A human-readable message giving the reason for the failure. These messages can be shown to your users.

  - `id_number.first_name` (string, nullable)
    First name.

  - `id_number.id_number` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
    ID number. When `id_number_type` is `us_ssn`, only the last 4 digits are present.

  - `id_number.id_number_type` (enum, nullable)
    Type of ID number.
Possible enum values:
    - `br_cpf`
      An individual CPF number from Brazil.

    - `sg_nric`
      A national registration identity card number from Singapore.

    - `us_ssn`
      A social security number from the United States. Only the last 4 digits are collected.

  - `id_number.last_name` (string, nullable)
    Last name.

  - `id_number.status` (enum)
    Status of this `id_number` check.
Possible enum values:
    - `unverified`
      The data being checked was not able to be verified.

    - `verified`
      The check resulted in a successful verification.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `options` (object, nullable)
  Configuration options for this report.

  - `options.document` (object, nullable)
    Configuration options to apply to the `document` check.

    - `options.document.allowed_types` (array of enums, nullable)
      Array of strings of allowed identity document types. If the provided identity document isn’t one of the allowed types, the verification check will fail with a document_type_not_allowed error code.
Possible enum values:
      - `driving_license`
        Drivers license document type.

      - `id_card`
        ID card document type.

      - `passport`
        Passport document type.

    - `options.document.require_id_number` (boolean, nullable)
      Collect an ID number and perform an [ID number check](https://docs.stripe.com/docs/identity/verification-checks.md?type=id-number) with the document’s extracted name and date of birth.

    - `options.document.require_live_capture` (boolean, nullable)
      Disable image uploads, identity document images have to be captured using the device’s camera.

    - `options.document.require_matching_selfie` (boolean, nullable)
      Capture a face image and perform a [selfie check](https://docs.stripe.com/docs/identity/verification-checks.md?type=selfie) comparing a photo ID and a picture of your user’s face. [Learn more](https://docs.stripe.com/docs/identity/selfie.md).

  - `options.id_number` (object, nullable)
    Configuration options to apply to the `id_number` check.

- `phone` (object, nullable)
  Result of the phone check for this report.

  - `phone.error` (object, nullable)
    Details on the verification error. Present when status is `unverified`.

    - `phone.error.code` (enum, nullable)
      A short machine-readable string giving the reason for the verification failure.
Possible enum values:
      - `phone_unverified_other`
        Stripe was unable to verify the provided phone number.

      - `phone_verification_declined`
        The user was unable to verify the provided phone number.

    - `phone.error.reason` (string, nullable)
      A human-readable message giving the reason for the failure. These messages can be shown to your users.

  - `phone.phone` (string, nullable)
    Phone to be verified.

  - `phone.status` (enum)
    Status of this `phone` check.
Possible enum values:
    - `unverified`
      The data being checked was not able to be verified.

    - `verified`
      The check resulted in a successful verification.

- `selfie` (object, nullable)
  Result of the selfie check for this report.

  - `selfie.document` (string, nullable)
    ID of the [File](https://docs.stripe.com/docs/api/files.md) holding the image of the identity document used in this check.

  - `selfie.error` (object, nullable)
    Details on the verification error. Present when status is `unverified`.

    - `selfie.error.code` (enum, nullable)
      A short machine-readable string giving the reason for the verification failure.
Possible enum values:
      - `selfie_document_missing_photo`
        The provided identity document didn’t contain a picture of a face.

      - `selfie_face_mismatch`
        The captured face image didn’t match with the document’s face.

      - `selfie_manipulated`
        The captured face image was manipulated.

      - `selfie_unverified_other`
        Stripe couldn’t verify the provided selfie.

    - `selfie.error.reason` (string, nullable)
      A human-readable message giving the reason for the failure. These messages can be shown to your users.

  - `selfie.selfie` (string, nullable)
    ID of the [File](https://docs.stripe.com/docs/api/files.md) holding the image of the selfie used in this check.

  - `selfie.status` (enum)
    Status of this `selfie` check.
Possible enum values:
    - `unverified`
      The data being checked was not able to be verified.

    - `verified`
      The check resulted in a successful verification.

- `type` (enum)
  Type of report.
Possible enum values:
  - `document`
    Perform a document check.

  - `id_number`
    Perform an ID number check.

  - `verification_flow`
    Configuration provided by verification flow

- `verification_flow` (string, nullable)
  The configuration token of a verification flow from the dashboard.

- `verification_session` (string, nullable)
  ID of the VerificationSession that created this report.

### The VerificationReport object

```json
{
  "id": "vr_1MwBlH2eZvKYlo2C91hOpFMf",
  "object": "identity.verification_report",
  "created": 1681337011,
  "livemode": false,
  "options": {
    "document": {}
  },
  "type": "document",
  "verification_session": "vs_NhaxYCqOE27AqaUTxbIZOnHw",
  "document": {
    "status": "verified",
    "error": null,
    "first_name": "Jenny",
    "last_name": "Rosen",
    "address": {
      "line1": "1234 Main St.",
      "city": "San Francisco",
      "state": "CA",
      "zip": "94111",
      "country": "US"
    },
    "type": "driving_license",
    "files": [
      "file_NhaxRCXT8Iuu8apSuci00UC4",
      "file_NhaxDeWKGAOTc8Uec7UY9Ljj"
    ],
    "expiration_date": {
      "month": 12,
      "day": 1,
      "year": 2025
    },
    "issued_date": {
      "month": 12,
      "day": 1,
      "year": 2020
    },
    "issuing_country": "US"
  }
}
```
