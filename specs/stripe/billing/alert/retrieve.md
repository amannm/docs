# Retrieve a billing alert

Retrieves a billing alert given an ID

## Returns

Returns the alert

#### Usage threshold

#### Usage threshold

```curl
curl https://api.stripe.com/v1/billing/alerts/alrt_12345 \
  -u "<<YOUR_SECRET_KEY>>"
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
