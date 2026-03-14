# Create a DebitReversal

Reverses a ReceivedDebit and creates a DebitReversal object.

## Returns

Returns a DebitReversal object.

## Parameters

- `received_debit` (string, required)
  The ReceivedDebit to reverse.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/treasury/debit_reversals \
  -u "<<YOUR_SECRET_KEY>>" \
  -d received_debit=rd_1MtkMLLkdIwHu7ixoiUFN4qd
```

### Response

```json
{
  "id": "debrev_1MtkMLLkdIwHu7ixIcVctOKK",
  "object": "treasury.debit_reversal",
  "amount": 1000,
  "created": 1680755021,
  "currency": "usd",
  "financial_account": "fa_1MtkMLLkdIwHu7ixrkGP4bqB",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KM6SuaEGMgaqNYp8YbE6NpNWYhI1PSbr_jlZwdPHUJHYBRG6-5T1Bmpq4GkpUhVvzLMDWZWkMVIveXHgiVwLUgpMM4Jx8w",
  "linked_flows": null,
  "livemode": false,
  "metadata": {},
  "network": "ach",
  "received_debit": "rd_1MtkMLLkdIwHu7ixoiUFN4qd",
  "status": "processing",
  "status_transitions": {
    "completed_at": null
  },
  "transaction": "trxn_1MtkMLLkdIwHu7ix2BG3LwWW"
}
```
