# Retrieve a shipping rate

Returns the shipping rate object with the given ID.

## Returns

Returns a shipping rate object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/shipping_rates/shr_1MrRx2LkdIwHu7ixikgEA6Wd \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "shr_1MrRx2LkdIwHu7ixikgEA6Wd",
  "object": "shipping_rate",
  "active": true,
  "created": 1680207604,
  "delivery_estimate": null,
  "display_name": "Ground shipping",
  "fixed_amount": {
    "amount": 500,
    "currency": "usd"
  },
  "livemode": false,
  "metadata": {},
  "tax_behavior": "unspecified",
  "tax_code": null,
  "type": "fixed_amount"
}
```
