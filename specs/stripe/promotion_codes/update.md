# Update a promotion code

Updates the specified promotion code by setting the values of the parameters passed. Most fields are, by design, not editable.

## Returns

The updated promotion code object is returned upon success. Otherwise, this call raises [an error](update.md#errors).

## Parameters

- `active` (boolean, optional)
  Whether the promotion code is currently active. A promotion code can only be reactivated when the coupon is still valid and the promotion code is otherwise redeemable.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `restrictions` (object, optional)
  Settings that restrict the redemption of the promotion code.

  - `restrictions.currency_options` (object, optional)
    Promotion codes defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

    - `restrictions.currency_options.<currency>.minimum_amount` (integer, optional)
      Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a purchase must be $100 or more to work).

```curl
curl https://api.stripe.com/v1/promotion_codes/promo_1MiM6KLkdIwHu7ixrIaX4wgn \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
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
  "metadata": {
    "order_id": "6735"
  },
  "restrictions": {
    "first_time_transaction": false,
    "minimum_amount": null,
    "minimum_amount_currency": null
  },
  "times_redeemed": 0
}
```
