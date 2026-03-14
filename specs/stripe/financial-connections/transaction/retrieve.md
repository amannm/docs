# Retrieve a Transaction

Retrieves the details of a Financial Connections `Transaction`

## Returns

Returns a `Transaction` object if a valid identifier was provided, and raises [an error](retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/financial_connections/transactions/fctxn_1MwVKd2eZvKYlo2ChNw2UxSa \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "fctxn_1MwVKd2eZvKYlo2ChNw2UxSa",
  "object": "financial_connections.transaction",
  "account": "fca_1MwVKd2eZvKYlo2CnlgoF3I4",
  "amount": 300,
  "currency": "usd",
  "description": "Rocket Rides",
  "livemode": false,
  "status": "posted",
  "status_transitions": {
    "posted_at": 1681412239,
    "void_at": null
  },
  "transacted_at": 1681412239,
  "transaction_refresh": "fctxnref_NhvAgiKSFDg9jOe6eIlj41X5",
  "updated": 1681412239
}
```
