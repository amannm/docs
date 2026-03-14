# Retrieve a Transaction

Retrieves the details of an existing Transaction.

## Returns

Returns a Transaction object if a valid identifier was provided. Otherwise, returns an error.

```curl
curl https://api.stripe.com/v1/treasury/transactions/trxn_1MtkYw2eZvKYlo2ClMGIO54z \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "trxn_1MtkYw2eZvKYlo2ClMGIO54z",
  "object": "treasury.transaction",
  "amount": -100,
  "balance_impact": {
    "cash": -100,
    "inbound_pending": 0,
    "outbound_pending": 100
  },
  "created": 1680755802,
  "currency": "usd",
  "description": "Jane Austen (6789) | Outbound transfer | transfer",
  "financial_account": "fa_1MtkYw2eZvKYlo2CrqmzUo3O",
  "flow": "obt_1MtkYw2eZvKYlo2CqsyBpQts",
  "flow_type": "outbound_transfer",
  "livemode": false,
  "status": "open",
  "status_transitions": {
    "posted_at": null,
    "void_at": null
  }
}
```
