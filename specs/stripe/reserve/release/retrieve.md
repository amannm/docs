# Retrieve a ReserveRelease

Retrieve a ReserveRelease.

## Returns

Returns a ReserveRelease object.

## Parameters

- `id` (string, required)
  The identifier of the ReserveRelease to retrieve.

```curl
curl https://api.stripe.com/v1/reserve/releases/resrel_61SxyHbQOe90T6sLB41Q8rCFhzAUW \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "resrel_61SxyHbQOe90T6sLB41Q8rCFhzAUW",
  "object": "reserve.release",
  "amount": 500,
  "created": 1753406491,
  "created_by": "application",
  "currency": "usd",
  "livemode": false,
  "metadata": {},
  "reason": "hold_released_early",
  "released_at": 1753406491,
  "reserve_hold": "reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW",
  "reserve_plan": null
}
```
