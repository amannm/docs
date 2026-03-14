# The Redaction Job Validation Error object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `code` (enum)
  A code indicating the reason for the error.
Possible enum values:
  - `invalid_cascading_source`
    The object is not redactable because of a related object’s existing state. Refer to the `message` prop for more context.

  - `invalid_file_purpose`
    The object’s related file is not redactable. Refer to the `message` prop for more context.

  - `invalid_state`
    The object is not redactable because of its own existing state. Refer to the `message` prop for more context.

  - `locked_by_other_job`
    The object is currently used in another redaction job. Cancel the other job to resolve this error.

  - `too_many_objects`
    Your job is trying to redact too many objects. Cancel this job and reduce the number of IDs in the Redaction Job’s `objects` prop in a new job. If this error persists, reach out to support.

- `erroring_object` (object, nullable)
  If the error is related to a specific object, this field includes the object’s identifier and object type.

  - `erroring_object.id` (string)
    Unique identifier for the object.

  - `erroring_object.object_type` (string)
    Erroring object type

- `message` (string)
  A human-readable message providing more details about the error.

### The Redaction Job Validation Error object

```json
{
  "id": "prjve_123",
  "object": "privacy.redaction_job_validation_error",
  "code": "invalid_state",
  "erroring_object": {
    "id": "pi_123",
    "object_type": "payment_intent"
  },
  "message": "PaymentIntent is not finalized. Confirm or cancel the payment intent."
}
```
