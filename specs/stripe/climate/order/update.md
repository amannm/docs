# Update an order

Updates the specified order by setting the values of the parameters passed.

## Returns

The updated Climate order object.

## Parameters

- `order` (string, required)
  Unique identifier of the order.

- `beneficiary` (object, optional)
  Publicly sharable reference for the end beneficiary of carbon removal. Assumed to be the Stripe account if not set.

  - `beneficiary.public_name` (string, required)
    Publicly displayable name for the end beneficiary of carbon removal.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/climate/orders/climorder_1aTnU0B63jkB3XAQKUbA5yyl \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

### Response

```json
{
  "id": "climorder_1aTnU0B63jkB3XAQKUbA5yyl",
  "object": "climate.order",
  "amount_fees": 17,
  "amount_subtotal": 550,
  "amount_total": 567,
  "beneficiary": {
    "public_name": "{{YOUR_BUSINESS_NAME}}"
  },
  "canceled_at": null,
  "cancellation_reason": null,
  "certificate": null,
  "confirmed_at": 1881439205,
  "created": 1881439205,
  "currency": "usd",
  "delayed_at": null,
  "delivered_at": null,
  "delivery_details": [],
  "expected_delivery_year": 2027,
  "livemode": false,
  "metadata": {
    "order_id": "6735"
  },
  "metric_tons": "0.01",
  "product": "climsku_frontier_offtake_portfolio_2027",
  "product_substituted_at": null,
  "status": "confirmed"
}
```
