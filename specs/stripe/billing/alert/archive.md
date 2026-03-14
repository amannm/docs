# Archive a billing alert

Archives this alert, removing it from the list view and APIs. This is non-reversible.

## Returns

Returns the alert with its updated status.

#### Usage threshold

#### Usage threshold

```curl
curl -X POST https://api.stripe.com/v1/billing/alerts/alrt_12345/archive \
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
  "status": "archived"
}
```
