# Retrieve a CreditReversal

Retrieves the details of an existing CreditReversal by passing the unique CreditReversal ID from either the CreditReversal creation request or CreditReversal list

## Returns

Returns a CreditReversal object.

```curl
curl https://api.stripe.com/v1/treasury/credit_reversals/credrev_1Mtklw2eZvKYlo2CJG2MWJM7 \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "credrev_1Mtklw2eZvKYlo2CJG2MWJM7",
  "object": "treasury.credit_reversal",
  "amount": 1000,
  "created": 1680756608,
  "currency": "usd",
  "financial_account": "fa_1Mtklw2eZvKYlo2CNHscZzs2",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ",
  "livemode": false,
  "metadata": {},
  "network": "ach",
  "received_credit": "rc_1Mtklw2eZvKYlo2CxuluQFPR",
  "status": "processing",
  "status_transitions": {
    "posted_at": null
  },
  "transaction": "trxn_1Mtklw2eZvKYlo2CKkbNA2TS"
}
```
