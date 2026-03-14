# Retrieve a coupon

Retrieves the coupon with the given ID.

## Returns

Returns a coupon if a valid coupon ID was provided. Raises [an error](retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/coupons/jMT0WJUD \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "jMT0WJUD",
  "object": "coupon",
  "amount_off": null,
  "created": 1678037688,
  "currency": null,
  "duration": "repeating",
  "duration_in_months": 3,
  "livemode": false,
  "max_redemptions": null,
  "metadata": {},
  "name": null,
  "percent_off": 25.5,
  "redeem_by": null,
  "times_redeemed": 0,
  "valid": true
}
```
