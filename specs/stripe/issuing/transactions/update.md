# Update a transaction

Updates the specified Issuing `Transaction` object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

## Returns

Returns an updated Issuing `Transaction` object if a valid identifier was provided.

## Parameters

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/issuing/transactions/ipi_1MzFN1K8F4fqH0lBmFq8CjbU \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

### Response

```json
{
  "id": "ipi_1MzFN1K8F4fqH0lBmFq8CjbU",
  "object": "issuing.transaction",
  "amount": -100,
  "amount_details": {
    "atm_fee": null
  },
  "authorization": "iauth_1MzFMzK8F4fqH0lBc9VdaZUp",
  "balance_transaction": "txn_1MzFN1K8F4fqH0lBQPtqUmJN",
  "card": "ic_1MzFMxK8F4fqH0lBjIUITRYi",
  "cardholder": "ich_1MzFMxK8F4fqH0lBXnFW0ROG",
  "created": 1682065867,
  "currency": "usd",
  "dispute": null,
  "livemode": false,
  "merchant_amount": -100,
  "merchant_currency": "usd",
  "merchant_data": {
    "category": "computer_software_stores",
    "category_code": "5734",
    "city": "SAN FRANCISCO",
    "country": "US",
    "name": "WWWW.BROWSEBUG.BIZ",
    "network_id": "1234567890",
    "postal_code": "94103",
    "state": "CA"
  },
  "metadata": {
    "order_id": "6735"
  },
  "type": "capture",
  "wallet": null
}
```
