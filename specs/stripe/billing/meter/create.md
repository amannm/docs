# Create a billing meter

Creates a billing meter.

## Returns

Returns a billing meter.

## Parameters

- `default_aggregation` (object, required)
  The default settings to aggregate a meter’s events with.

  - `default_aggregation.formula` (enum, required)
    Specifies how events are aggregated. Allowed values are `count` to count the number of events, `sum` to sum each event’s value and `last` to take the last event’s value in the window.
Possible enum values:
    - `count`
      Count the number of events.

    - `last`
      Take the last event’s value in the window.

    - `sum`
      Sum each event’s value.

- `display_name` (string, required)
  The meter’s name. Not visible to the customer.

  The maximum length is 250 characters.

- `event_name` (string, required)
  The name of the meter event to record usage for. Corresponds with the `event_name` field on meter events.

  The maximum length is 100 characters.

- `customer_mapping` (object, optional)
  Fields that specify how to map a meter event to a customer.

  - `customer_mapping.event_payload_key` (string, required)
    The key in the meter event payload to use for mapping the event to a customer.

    The maximum length is 100 characters.

  - `customer_mapping.type` (enum, required)
    The method for mapping a meter event to a customer. Must be `by_id`.
Possible enum values:
    - `by_id`
      Map a meter event to a customer by passing a customer ID in the event’s payload.

- `event_time_window` (enum, optional)
  The time window which meter events have been pre-aggregated for, if any.
Possible enum values:
  - `day`
    Events are pre-aggregated in daily buckets.

  - `hour`
    Events are pre-aggregated in hourly buckets.

- `value_settings` (object, optional)
  Fields that specify how to calculate a meter event’s value.

  - `value_settings.event_payload_key` (string, required)
    The key in the usage event payload to use as the value for this meter. For example, if the event payload contains usage on a `bytes_used` field, then set the event_payload_key to “bytes_used”.

    The maximum length is 100 characters.

```curl
curl https://api.stripe.com/v1/billing/meters \
  -u "<<YOUR_SECRET_KEY>>" \
  -d display_name="Search API Calls" \
  -d event_name=ai_search_api \
  -d "default_aggregation[formula]"=sum \
  -d "value_settings[event_payload_key]"=value \
  -d "customer_mapping[type]"=by_id \
  -d "customer_mapping[event_payload_key]"=stripe_customer_id
```

### Response

```json
{
  "id": "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA",
  "object": "billing.meter",
  "created": 1704824589,
  "customer_mapping": {
    "type": "by_id",
    "event_payload_key": "stripe_customer_id"
  },
  "default_aggregation": {
    "formula": "sum"
  },
  "display_name": "Search API Calls",
  "event_name": "ai_search_api",
  "event_time_window": null,
  "livemode": false,
  "status": "active",
  "status_transitions": {
    "deactivated_at": null
  },
  "updated": 1704824589,
  "value_settings": {
    "event_payload_key": "value"
  }
}
```
