# The VerificationSession object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `client_reference_id` (string, nullable)
  A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.

- `client_secret` (string, nullable)
  The short-lived client secret used by Stripe.js to [show a verification modal](https://docs.stripe.com/docs/js/identity/modal) inside your app. This client secret expires after 24 hours and can only be used once. Don’t store it, log it, embed it in a URL, or expose it to anyone other than the user. Make sure that you have TLS enabled on any page that includes the client secret. Refer to our docs on [passing the client secret to the frontend](https://docs.stripe.com/docs/identity/verification-sessions.md#client-secret) to learn more.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `last_error` (object, nullable)
  If present, this property tells you the last error encountered when processing the verification.

  - `last_error.code` (enum, nullable)
    A short machine-readable string giving the reason for the verification or user-session failure.
Possible enum values:
    - `abandoned`
      The user began the verification but didn’t submit it.

    - `consent_declined`
      The user declined to be verified by Stripe. Check with your legal counsel to see if you have an obligation to offer an alternative, non-biometric means to verify, such as through a manual review.

    - `country_not_supported`
      Stripe doesn’t verify users from the provided country.

    - `device_not_supported`
      The user’s device didn’t have a camera or they declined to grant Stripe permission to access it.

    - `document_expired`
      The provided identity document has expired.

    - `document_type_not_supported`
      The provided identity document isn’t one of the session’s [allowed document types](https://docs.stripe.com/docs/api/identity/verification_sessions/create.md#create_identity_verification_session-options-document-allow_document_types).

    - `document_unverified_other`
      Stripe couldn’t verify the provided identity document. See the [list of supported document types](https://docs.stripe.com/docs/identity/verification-checks.md?type=document).

    - `email_unverified_other`
      Stripe was unable to verify the provided email address.

    - `email_verification_declined`
      The user was unable to verify the provided email address.

    - `id_number_insufficient_document_data`
      The provided document didn’t contain enough data to match against the ID number.

    - `id_number_mismatch`
      The information provided couldn’t be matched against global databases.

    - `id_number_unverified_other`
      The information provided couldn’t be verified. See the [list of supported ID numbers](https://docs.stripe.com/docs/identity/verification-checks.md?type=id-number).

    - `phone_unverified_other`
      Stripe was unable to verify the provided phone number.

    - `phone_verification_declined`
      The user was unable to verify the provided phone number.

    - `selfie_document_missing_photo`
      The provided identity document didn’t contain a picture of a face.

    - `selfie_face_mismatch`
      The captured face image didn’t match with the document’s face.

    - `selfie_manipulated`
      The captured face image was manipulated.

    - `selfie_unverified_other`
      Stripe couldn’t verify the provided selfie.

    - `under_supported_age`
      Stripe doesn’t verify users under the age of majority.

  - `last_error.reason` (string, nullable)
    A message that explains the reason for verification or user-session failure.

- `last_verification_report` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  ID of the most recent VerificationReport. [Learn more about accessing detailed verification results.](https://docs.stripe.com/docs/identity/verification-sessions.md#results)

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `options` (object, nullable)
  A set of options for the session’s verification checks.

  - `options.document` (object, nullable)
    Options that apply to the [document check](https://docs.stripe.com/docs/identity/verification-checks.md?type=document).

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

  - `options.email` (object, nullable)
    Options that apply to the email check.

    - `options.email.require_verification` (boolean, nullable)
      Request one time password verification of `provided_details.email`.

  - `options.id_number` (object, nullable)
    Options that apply to the [id number check](https://docs.stripe.com/docs/identity/verification-checks.md?type=id_number).

  - `options.matching` (object, nullable)
    Options that apply to the matching check.

    - `options.matching.dob` (enum, nullable)
      Strictness of the DOB matching policy to apply.
Possible enum values:
      - `none`
        No matching requirement.

      - `similar`
        Fuzzy matching requirement.

    - `options.matching.name` (enum, nullable)
      Strictness of the name matching policy to apply.
Possible enum values:
      - `none`
        No matching requirement.

      - `similar`
        Fuzzy matching requirement.

  - `options.phone` (object, nullable)
    Options that apply to the phone check.

    - `options.phone.require_verification` (boolean, nullable)
      Request one time password verification of `provided_details.phone`.

- `provided_details` (object, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  Details provided about the user being verified. These details may be shown to the user.

  - `provided_details.email` (string, nullable)
    Email of user being verified

  - `provided_details.phone` (string, nullable)
    Phone number of user being verified

- `redaction` (object, nullable)
  Redaction status of this VerificationSession. If the VerificationSession is not redacted, this field will be null.

  - `redaction.status` (enum)
    Indicates whether this object and its related objects have been redacted or not.
Possible enum values:
    - `processing`
      This object has been redacted, and its related objects are in the process of being redacted. This process may take up to four days.

    - `redacted`
      This object and its related objects have been redacted.

- `related_customer` (string, nullable)
  Customer ID

- `related_customer_account` (string, nullable)
  The ID of the Account representing a customer.

- `related_person` (object, nullable)
  Tokens referencing the related Person resource and it’s associated account.

  - `related_person.account` (string)
    Token referencing the associated Account of the related Person resource.

  - `related_person.person` (string)
    Token referencing the related Person resource.

- `status` (enum)
  Status of this VerificationSession. [Learn more about the lifecycle of sessions](https://docs.stripe.com/docs/identity/how-sessions-work.md).
Possible enum values:
  - `canceled`
    The VerificationSession has been invalidated for future submission attempts.

  - `processing`
    The session has been submitted and is being processed. Most [verification checks](https://docs.stripe.com/docs/identity/verification-checks.md) are processed in less than 1 minute.

  - `requires_input`
    Requires user input before processing can continue.

  - `verified`
    Processing of all the verification checks are complete and successfully verified.

- `type` (enum)
  The type of [verification check](https://docs.stripe.com/docs/identity/verification-checks.md) to be performed.
Possible enum values:
  - `document`
    [Document check](https://docs.stripe.com/docs/identity/verification-checks.md?type=document).

  - `id_number`
    [ID number check](https://docs.stripe.com/docs/identity/verification-checks.md?type=id-number).

  - `verification_flow`
    Configuration provided by verification flow

- `url` (string, nullable)
  The short-lived URL that you use to redirect a user to Stripe to submit their identity information. This URL expires after 48 hours and can only be used once. Don’t store it, log it, send it in emails or expose it to anyone other than the user. Refer to our docs on [verifying identity documents](https://docs.stripe.com/docs/identity/verify-identity-documents.md?platform=web&type=redirect) to learn how to redirect users to Stripe.

- `verification_flow` (string, nullable)
  The configuration token of a verification flow from the dashboard.

- `verified_outputs` (object, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The user’s verified data.

  - `verified_outputs.address` (object, nullable)
    The user’s verified address.

    - `verified_outputs.address.city` (string, nullable)
      City, district, suburb, town, or village.

    - `verified_outputs.address.country` (string, nullable)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `verified_outputs.address.line1` (string, nullable)
      Address line 1, such as the street, PO Box, or company name.

    - `verified_outputs.address.line2` (string, nullable)
      Address line 2, such as the apartment, suite, unit, or building.

    - `verified_outputs.address.postal_code` (string, nullable)
      ZIP or postal code.

    - `verified_outputs.address.state` (string, nullable)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `verified_outputs.dob` (object, nullable, expandable (can be expanded into an object with the `expand` request parameter))
    The user’s verified date of birth.

    - `verified_outputs.dob.day` (integer, nullable)
      Numerical day between 1 and 31.

    - `verified_outputs.dob.month` (integer, nullable)
      Numerical month between 1 and 12.

    - `verified_outputs.dob.year` (integer, nullable)
      The four-digit year.

  - `verified_outputs.email` (string, nullable)
    The user’s verified email address

  - `verified_outputs.first_name` (string, nullable)
    The user’s verified first name.

  - `verified_outputs.id_number` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
    The user’s verified id number.

  - `verified_outputs.id_number_type` (enum, nullable)
    The user’s verified id number type.
Possible enum values:
    - `br_cpf`
      An individual CPF number from Brazil.

    - `sg_nric`
      A national registration identity card number from Singapore.

    - `us_ssn`
      A social security number from the United States. Only the last 4 digits are collected.

  - `verified_outputs.last_name` (string, nullable)
    The user’s verified last name.

  - `verified_outputs.phone` (string, nullable)
    The user’s verified phone number

  - `verified_outputs.sex` (enum, nullable, expandable (can be expanded into an object with the `expand` request parameter))
    The user’s verified sex.
Possible enum values:
    - `[redacted]`
      The verification has been redacted.

    - `female`
      Female

    - `male`
      Male

    - `unknown`
      Could not determine the user’s sex.

  - `verified_outputs.unparsed_place_of_birth` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
    The user’s verified place of birth as it appears in the document.

  - `verified_outputs.unparsed_sex` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
    The user’s verified sex as it appears in the document.

### The VerificationSession object

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
