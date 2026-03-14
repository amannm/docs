# Retrieve a DebitReversal

Retrieves a DebitReversal object.

## Returns

Returns a DebitReversal object.

```curl
curl https://api.stripe.com/v1/treasury/debit_reversals/debrev_1MtkMLLkdIwHu7ixIcVctOKK \
  -u "<<YOUR_SECRET_KEY>>"
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
