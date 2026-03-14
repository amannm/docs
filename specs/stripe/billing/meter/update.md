# Update a billing meter

Updates a billing meter.

## Returns

Returns a billing meter.

## Parameters

- `display_name` (string, optional)
  The meter’s name. Not visible to the customer.

  The maximum length is 250 characters.

```curl
curl https://api.stripe.com/v1/billing/meters/mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA \
  -u "<<YOUR_SECRET_KEY>>" \
  -d display_name="Updated Display Name"
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
  "display_name": "Updated Display Name",
  "event_name": "ai_search_api",
  "event_time_window": null,
  "livemode": false,
  "status": "active",
  "status_transitions": {
    "deactivated_at": null
  },
  "updated": 1704898330,
  "value_settings": {
    "event_payload_key": "value"
  }
}
```
