# Retrieve a TransactionEntry

Retrieves a TransactionEntry object.

## Returns

Returns a TransactionEntry object.

```curl
curl https://api.stripe.com/v1/treasury/transaction_entries/trxne_1MtkgV2eZvKYlo2CmofEnIwJ \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "trxne_1MtkgV2eZvKYlo2CmofEnIwJ",
  "object": "treasury.transaction_entry",
  "balance_impact": {
    "cash": 0,
    "inbound_pending": 0,
    "outbound_pending": -1000
  },
  "created": 1680756271,
  "currency": "usd",
  "effective_at": 1680756271,
  "financial_account": "fa_1MtkgV2eZvKYlo2CdxyvnHeQ",
  "flow": "obt_1MtkgV2eZvKYlo2CCxhXVFLB",
  "flow_type": "outbound_transfer",
  "livemode": false,
  "transaction": "trxn_1MtkgV2eZvKYlo2CRYxD7KLh",
  "type": "outbound_transfer"
}
```
