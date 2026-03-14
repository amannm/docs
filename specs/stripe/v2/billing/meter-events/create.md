# Create a Meter Event with synchronous validation

Creates a meter event. Events are validated synchronously, but are processed asynchronously. Supports up to 1,000 events per second in livemode. For higher rate-limits, please use meter event streams instead.

## Parameters

- `event_name` (string, required)
  The name of the meter event. Corresponds with the `event_name` field on a meter.

- `payload` (map, required)
  The payload of the event. This must contain the fields corresponding to a meter’s `customer_mapping.event_payload_key` (default is `stripe_customer_id`) and `value_settings.event_payload_key` (default is `value`). Read more about the [payload](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage.md#payload-key-overrides).

- `identifier` (string, optional)
  A unique identifier for the event. If not provided, one will be generated. We recommend using a globally unique identifier for this. We’ll enforce uniqueness within a rolling 24 hour period.

- `timestamp` (timestamp, optional)
  The time of the event. Must be within the past 35 calendar days or up to 5 minutes in the future. Defaults to current timestamp if not specified.

## Returns

## Response attributes

- `object` (string, value is "v2.billing.meter_event")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `created` (timestamp)
  The creation time of this meter event.

- `event_name` (string)
  The name of the meter event. Corresponds with the `event_name` field on a meter.

- `identifier` (string)
  A unique identifier for the event. If not provided, one will be generated. We recommend using a globally unique identifier for this. We’ll enforce uniqueness within a rolling 24 hour period.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `payload` (map)
  The payload of the event. This must contain the fields corresponding to a meter’s `customer_mapping.event_payload_key` (default is `stripe_customer_id`) and `value_settings.event_payload_key` (default is `value`). Read more about the [payload](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage.md#payload-key-overrides)…

- `timestamp` (timestamp)
  The time of the event. Must be within the past 35 calendar days or up to 5 minutes in the future. Defaults to current timestamp if not specified.

## Error Codes

| HTTP status code | Code                         | Description                                                                    |
| ---------------- | ---------------------------- | ------------------------------------------------------------------------------ |
| 400              | archived_meter               | The meter must be Active to submit events.                                     |
| 400              | duplicate_meter_event        | A meter event with a duplicate identifier has already been submitted.          |
| 400              | no_meter                     | A meter must exist to submit events.                                           |
| 400              | payload_invalid_value        | The value must be a positive integer.                                          |
| 400              | payload_no_customer_defined  | The payload must have a reference to the customer.                             |
| 400              | payload_no_value_defined     | The payload must have a value.                                                 |
| 409              | too_many_concurrent_requests | Cannot create multiple usage events for the same customer, meter concurrently. |

```curl
curl -X POST https://api.stripe.com/v2/billing/meter_events \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-02-25.preview" \
  --json '{
    "identifier": "idmp_12345678",
    "event_name": "ai_search_api",
    "timestamp": "2024-06-01T12:00:00.000Z",
    "payload": {
        "stripe_customer_id": "cus_12345678",
        "value": "25"
    }
  }'
```

### Response

```json
{
  "object": "v2.billing.meter_event",
  "created": "2024-06-01T12:10:00.000Z",
  "livemode": false,
  "identifier": "idmp_12345678",
  "event_name": "ai_search_api",
  "timestamp": "2024-06-01T12:00:00.000Z",
  "payload": {
    "stripe_customer_id": "cus_12345678",
    "value": "25"
  }
}
```
