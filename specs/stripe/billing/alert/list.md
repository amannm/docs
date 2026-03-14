# List billing alerts

Lists billing active and inactive alerts

## Returns

Returns a list of billing alerts

## Parameters

- `alert_type` (enum, optional)
  Filter results to only include this type of alert.
Possible enum values:
  - `usage_threshold`
    Use `usage_threshold` if you intend for an alert to fire when a usage threshold on a meter is crossed.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `meter` (string, optional)
  Filter results to only include alerts with the given meter.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

#### Usage threshold

#### Usage threshold

```curl
curl https://api.stripe.com/v1/billing/alerts \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "data": [
    {
      "id": "alrt_12345",
      "object": "billing.alert",
      "title": "API Request usage alert",
      "livemode": true,
      "alert_type": "usage_threshold",
      "usage_threshold": {
        "gte": 10000,
        "meter": "mtr_12345",
        "recurrence": "one_time"
      },
      "status": "active"
    },
    {
      "id": "alrt_67890",
      "object": "billing.alert",
      "title": "API Request usage alert",
      "livemode": true,
      "alert_type": "usage_threshold",
      "usage_threshold": {
        "gte": 120,
        "meter": "mtr_67890",
        "recurrence": "one_time"
      },
      "status": "active"
    }
  ]
}
```
