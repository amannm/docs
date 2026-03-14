# Update a shipping rate

Updates an existing shipping rate object.

## Returns

Returns the modified shipping rate object if the call succeeded.

## Parameters

- `active` (boolean, optional)
  Whether the shipping rate can be used for new purchases. Defaults to `true`.

- `fixed_amount` (object, optional)
  Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.

  - `fixed_amount.currency_options` (object, optional)
    Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

    - `fixed_amount.currency_options.<currency>.amount` (integer, Required if adding a new currency_option.)
      A non-negative integer in cents representing how much to charge.

    - `fixed_amount.currency_options.<currency>.tax_behavior` (enum, recommended if calculating taxes)
      Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
Possible enum values:
      - `exclusive`
      - `inclusive`
      - `unspecified`

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `tax_behavior` (enum, Recommended if calculating taxes)
  Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
Possible enum values:
  - `exclusive`
  - `inclusive`
  - `unspecified`

```curl
curl https://api.stripe.com/v1/shipping_rates/shr_1MrRx2LkdIwHu7ixikgEA6Wd \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
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
  "metadata": {
    "order_id": "6735"
  },
  "tax_behavior": "unspecified",
  "tax_code": null,
  "type": "fixed_amount"
}
```
