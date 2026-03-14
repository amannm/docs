# Create a Meter Event with asynchronous validation

Creates meter events. Events are processed asynchronously, including validation. Requires a meter event session for authentication. Supports up to 10,000 requests per second in livemode. For even higher rate-limits, contact sales.

## Parameters

- `events` (array of objects, required)
  List of meter events to include in the request. Supports up to 100 events per request.

  - `events.event_name` (string, required)
    The name of the meter event. Corresponds with the `event_name` field on a meter.

  - `events.payload` (map, required)
    The payload of the event. This must contain the fields corresponding to a meter’s `customer_mapping.event_payload_key` (default is `stripe_customer_id`) and `value_settings.event_payload_key` (default is `value`). Read more about the [payload](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage.md#payload-key-overrides).

  - `events.identifier` (string, optional)
    A unique identifier for the event. If not provided, one will be generated. We recommend using a globally unique identifier for this. We’ll enforce uniqueness within a rolling 24 hour period.

  - `events.timestamp` (timestamp, optional)
    The time of the event. Must be within the past 35 calendar days or up to 5 minutes in the future. Defaults to current timestamp if not specified.

## Returns

## Error Codes

| HTTP status code | Code                                | Description                              |
| ---------------- | ----------------------------------- | ---------------------------------------- |
| 401              | billing_meter_event_session_expired | The temporary session token has expired. |

```curl
curl -X POST https://meter-events.stripe.com/v2/billing/meter_event_stream \
  -H "Authorization: Bearer {{SESSION AUTH TOKEN}}" \
  -H "Stripe-Version: 2026-02-25.preview" \
  --json '{
    "events": [
        {
            "identifier": "idmp_12345678",
            "event_name": "ai_search_api",
            "timestamp": "2024-06-01T12:00:00.000Z",
            "payload": {
                "stripe_customer_id": "cus_12345678",
                "value": "25"
            }
        }
    ]
  }'
```

### Response

```json
{}
```
