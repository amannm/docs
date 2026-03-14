# Retrieve a transaction

Retrieves an Issuing `Transaction` object.

## Returns

Returns an Issuing `Transaction` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/issuing/transactions/ipi_1MzFN1K8F4fqH0lBmFq8CjbU \
  -u "<<YOUR_SECRET_KEY>>"
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
  "metadata": {},
  "type": "capture",
  "wallet": null
}
```
