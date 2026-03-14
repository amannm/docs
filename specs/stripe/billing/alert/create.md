# Create a billing alert

Creates a billing alert

## Returns

Returns a billing alert

## Parameters

- `alert_type` (enum, required)
  The type of alert to create.
Possible enum values:
  - `usage_threshold`
    Use `usage_threshold` if you intend for an alert to fire when a usage threshold on a meter is crossed.

- `title` (string, required)
  The title of the alert.

  The maximum length is 256 characters.

- `usage_threshold` (object, optional)
  The configuration of the usage threshold.

  - `usage_threshold.gte` (integer, required)
    Defines the threshold value that triggers the alert.

  - `usage_threshold.meter` (string, required)
    The [Billing Meter](../meter.md) ID whose usage is monitored.

  - `usage_threshold.recurrence` (enum, required)
    Defines how the alert will behave.
Possible enum values:
    - `one_time`
      Use `one_time` if you intend for an alert to only fire once in the lifetime of a customer.

  - `usage_threshold.filters` (array of objects, optional)
    The filters allows limiting the scope of this usage alert. You can only specify up to one filter at this time.

    - `usage_threshold.filters.type` (enum, required)
      What type of filter is being applied to this usage alert.
Possible enum values:
      - `customer`
        Use `customer` if you intend to filter this alert to a customer.

    - `usage_threshold.filters.customer` (string, optional)
      Limit the scope to this usage alert only to this customer.

#### Usage threshold

#### Usage threshold

```curl
curl https://api.stripe.com/v1/billing/alerts \
  -u "<<YOUR_SECRET_KEY>>" \
  -d title="API Request usage alert" \
  -d alert_type=usage_threshold \
  -d "usage_threshold[gte]"=10000 \
  -d "usage_threshold[meter]"=mtr_12345 \
  -d "usage_threshold[recurrence]"=one_time
```

### Response

```json
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
}
```
