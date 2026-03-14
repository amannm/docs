# Create a CreditReversal

Reverses a ReceivedCredit and creates a CreditReversal object.

## Returns

Returns a CreditReversal object.

## Parameters

- `received_credit` (string, required)
  The ReceivedCredit to reverse.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/treasury/credit_reversals \
  -u "<<YOUR_SECRET_KEY>>" \
  -d received_credit=rc_1MtkGJLkdIwHu7ixWPuY9DGn
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
