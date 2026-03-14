# List billing meters

Retrieve a list of billing meters.

## Returns

Returns a list of billing meters.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Filter results to only include meters with the given status.
Possible enum values:
  - `active`
    The meter is active.

  - `inactive`
    The meter is inactive. No more events for this meter will be accepted. The meter cannot be attached to a price.

```curl
curl https://api.stripe.com/v1/billing/meters \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "object": "list",
  "data": [
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
      "updated": 1704898330,
      "value_settings": {
        "event_payload_key": "value"
      }
    }
  ],
  "has_more": true,
  "url": "v1/billing/meters"
}
```
