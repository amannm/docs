# Create a billing meter event adjustment

Creates a billing meter event adjustment.

## Returns

Returns a billing meter event adjustment.

## Parameters

- `event_name` (string, required)
  The name of the meter event. Corresponds with the `event_name` field on a meter.

  The maximum length is 100 characters.

- `type` (enum, required)
  Specifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet.
Possible enum values:
  - `cancel`
    Cancel a single meter event by identifier.

- `cancel` (object, optional)
  Specifies which event to cancel.

  - `cancel.identifier` (string, optional)
    Unique identifier for the event. You can only cancel events within 24 hours of Stripe receiving them.

    The maximum length is 100 characters.

```curl
curl https://api.stripe.com/v1/billing/meter_event_adjustments \
  -u "<<YOUR_SECRET_KEY>>" \
  -d type=cancel \
  -d event_name=ai_search_api \
  -d "cancel[identifier]"=identifier_123
```

### Response

```json
{
  "object": "billing.meter_event_adjustment",
  "livemode": false,
  "status": "pending",
  "event_name": "ai_search_api",
  "type": "cancel",
  "cancel": {
    "identifier": "identifier_123"
  }
}
```
