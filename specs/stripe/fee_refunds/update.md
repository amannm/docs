# Update an application fee refund

Updates the specified application fee refund by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

This request only accepts metadata as an argument.

## Returns

Returns the application fee refund object if the update succeeded. This call will raise [an error](update.md#errors) if update parameters are invalid.

## Parameters

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds/fr_1MtJRpKbnvuxQXGuM6Ww0D24 \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
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
  "metadata": {
    "order_id": "6735"
  }
}
```
