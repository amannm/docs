# Retrieve an order

Retrieves the details of a Climate order object with the given ID.

## Returns

Returns a Climate order object if a valid identifier was provided. Throws an error otherwise.

## Parameters

- `order` (string, required)
  Unique identifier of the order.

```curl
curl https://api.stripe.com/v1/climate/orders/climorder_1aTnU0B63jkB3XAQKUbA5yyl \
  -u "<<YOUR_SECRET_KEY>>"
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
  "metadata": {},
  "metric_tons": "0.01",
  "product": "climsku_frontier_offtake_portfolio_2027",
  "product_substituted_at": null,
  "status": "confirmed"
}
```
