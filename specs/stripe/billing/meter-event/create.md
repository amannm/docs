# Create a billing meter event

Creates a billing meter event.

## Returns

Returns a billing meter event.

## Parameters

- `event_name` (string, required)
  The name of the meter event. Corresponds with the `event_name` field on a meter.

  The maximum length is 100 characters.

- `payload` (object, required)
  The payload of the event. This must contain the fields corresponding to a meter’s `customer_mapping.event_payload_key` (default is `stripe_customer_id`) and `value_settings.event_payload_key` (default is `value`). Read more about the [payload](https://docs.stripe.com/billing/subscriptions/usage-based/meters/configure.md#meter-configuration-attributes).

- `identifier` (string, optional)
  A unique identifier for the event. If not provided, one is generated. We recommend using UUID-like identifiers. We will enforce uniqueness within a rolling period of at least 24 hours. The enforcement of uniqueness primarily addresses issues arising from accidental retries or other problems occurring within extremely brief time intervals. This approach helps prevent duplicate entries and ensures data integrity in high-frequency operations.

  The maximum length is 100 characters.

- `timestamp` (timestamp, optional)
  The time of the event. Measured in seconds since the Unix epoch. Must be within the past 35 calendar days or up to 5 minutes in the future. Defaults to current timestamp if not specified.

```curl
curl https://api.stripe.com/v1/billing/meter_events \
  -u "<<YOUR_SECRET_KEY>>" \
  -d event_name=ai_search_api \
  -d "payload[value]"=25 \
  -d "payload[stripe_customer_id]"=cus_NciAYcXfLnqBoz \
  -d identifier=identifier_123
```

### Response

```json
{
  "object": "billing.meter_event",
  "created": 1704824589,
  "event_name": "ai_search_api",
  "identifier": "identifier_123",
  "livemode": true,
  "payload": {
    "value": "25",
    "stripe_customer_id": "cus_NciAYcXfLnqBoz"
  },
  "timestamp": 1680210639
}
```
