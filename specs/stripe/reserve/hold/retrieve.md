# Retrieve a ReserveHold

Retrieve a ReserveHold.

## Returns

Returns a ReserveHold object.

## Parameters

- `id` (string, required)
  The identifier of the ReserveHold to retrieve.

```curl
curl https://api.stripe.com/v1/reserve/holds/reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

### Response

```json
{
  "id": "reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW",
  "object": "reserve.hold",
  "amount": 1000,
  "amount_releasable": 1000,
  "created": 1753380387,
  "created_by": "application",
  "currency": "usd",
  "is_releasable": true,
  "livemode": false,
  "metadata": {},
  "reason": "standalone",
  "release_schedule": {
    "release_after": 1755972386,
    "scheduled_release": 1755993600
  },
  "reserve_plan": null,
  "source_charge": null,
  "source_type": "card"
}
```
