# Retrieve a ReservePlan

Retrieve a ReservePlan.

## Returns

Returns a ReservePlan object.

## Parameters

- `id` (string, required)
  The identifier of the ReservePlan to retrieve.

```curl
curl https://api.stripe.com/v1/reserve/plans/resplan_61SxrVOzQu6XIJSCx41Q8rCFhzAUW \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

### Response

```json
{
  "id": "resplan_61SxrVOzQu6XIJSCx41Q8rCFhzAUW",
  "object": "reserve.plan",
  "created": 1753380438,
  "created_by": "application",
  "currency": "usd",
  "disabled_at": null,
  "livemode": false,
  "metadata": {},
  "percent": 15,
  "rolling_release": {
    "days_after_charge": 30,
    "expires_on": 1755972438
  },
  "status": "active",
  "type": "rolling_release"
}
```
