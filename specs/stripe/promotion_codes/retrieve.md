# Retrieve a promotion code

Retrieves the promotion code with the given ID. In order to retrieve a promotion code by the customer-facing `code` use [list](https://docs.stripe.com/docs/api/promotion_codes/list.md) with the desired `code`.

## Returns

Returns a promotion code if a valid promotion code ID was provided. Raises [an error](retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/promotion_codes/promo_1MiM6KLkdIwHu7ixrIaX4wgn \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "promo_1MiM6KLkdIwHu7ixrIaX4wgn",
  "object": "promotion_code",
  "active": true,
  "code": "A1H1Q1MG",
  "promotion": {
    "type": "coupon",
    "coupon": "nVJYDOag"
  },
  "created": 1678040164,
  "customer": null,
  "expires_at": null,
  "livemode": false,
  "max_redemptions": null,
  "metadata": {},
  "restrictions": {
    "first_time_transaction": false,
    "minimum_amount": null,
    "minimum_amount_currency": null
  },
  "times_redeemed": 0
}
```
