# Create a ReserveRelease

Create a ReserveRelease to manually release funds from a ReserveHold.

## Returns

Returns a ReserveRelease object.

## Parameters

- `reserve_hold` (string, required)
  The ReserveHold to release.

- `amount` (integer, optional)
  Amount to release from the provided ReserveHold. A positive integer representing how much to release in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal) (e.g., 100 cents to release $1.00 or 100 to release ¥100, a zero-decimal currency). If not provided, the full releasable amount of the ReserveHold is released.

- `currency` (enum, optional)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/reserve/releases \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d reserve_hold=reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW \
  -d amount=500 \
  -d currency=usd
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
