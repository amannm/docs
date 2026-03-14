# The Redaction Job object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `objects` (object, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The objects to redact in this job.

  - `objects.charges` (array of strings, nullable)
    Charge object identifiers usually starting with `ch_`

  - `objects.checkout_sessions` (array of strings, nullable)
    CheckoutSession object identifiers starting with `cs_`

  - `objects.customers` (array of strings, nullable)
    Customer object identifiers starting with `cus_`

  - `objects.identity_verification_sessions` (array of strings, nullable)
    Identity VerificationSessions object identifiers starting with `vs_`

  - `objects.invoices` (array of strings, nullable)
    Invoice object identifiers starting with `in_`

  - `objects.issuing_cardholders` (array of strings, nullable)
    Issuing Cardholder object identifiers starting with `ich_`

  - `objects.payment_intents` (array of strings, nullable)
    PaymentIntent object identifiers starting with `pi_`

  - `objects.radar_value_list_items` (array of strings, nullable)
    Fraud ValueListItem object identifiers starting with `rsli_`

  - `objects.setup_intents` (array of strings, nullable)
    SetupIntent object identifiers starting with `seti_`

- `status` (enum)
  The status of the job.
Possible enum values:
  - `canceled`
    The job is canceled. No objects are redacted.

  - `canceling`
    The job is canceling and no objects will be redacted.

  - `created`
    This job is newly created and will begin validating shortly.

  - `failed`
    The job failed to validate. View the job’s validation errors for more information.

  - `ready`
    The job is ready to run or cancel.

  - `redacting`
    The job is running. It is redacting the job’s specified objects.

  - `succeeded`
    The job is complete. The job’s objects are redacted.

  - `validating`
    The job is checking if the objects are eligible for redaction.

- `validation_behavior` (enum, nullable)
  Validation behavior determines how a job validates objects for redaction eligibility. Default is `error`.
Possible enum values:
  - `error`
    The job will generate a validation error for every object that cannot be redacted. If there are any errors, all of them will need to be resolved before the job can run.

  - `fix`
    The job will attempt to fix validation errors whenever possible. Some objects cannot be automatically fixed and will need to be resolved before the job can run.

### The Redaction Job object

```json
{
  "id": "prj_123",
  "object": "privacy.redaction_job",
  "created": 1234567890,
  "livemode": true,
  "status": "validating",
  "validation_behavior": "error"
}
```
