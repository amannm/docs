# Retrieve an application fee refund

By default, you can see the 10 most recent refunds stored directly on the application fee object, but you can also retrieve details about a specific refund stored on the application fee.

## Returns

Returns the application fee refund object.

```curl
curl https://api.stripe.com/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds/fr_1MtJRpKbnvuxQXGuM6Ww0D24 \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "fr_1MtJRpKbnvuxQXGuM6Ww0D24",
  "object": "fee_refund",
  "amount": 100,
  "balance_transaction": null,
  "created": 1680651573,
  "currency": "usd",
  "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
  "metadata": {}
}
```
