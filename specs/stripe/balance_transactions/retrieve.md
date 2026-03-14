# Retrieve a balance transaction

Retrieves the balance transaction with the given ID.

Note that this endpoint previously used the path `/v1/balance/history/:id`.

## Returns

Returns a balance transaction if a valid balance transaction ID was provided. Raises [an error](retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/balance_transactions/txn_1MiN3gLkdIwHu7ixxapQrznl \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "txn_1MiN3gLkdIwHu7ixxapQrznl",
  "object": "balance_transaction",
  "amount": -400,
  "available_on": 1678043844,
  "created": 1678043844,
  "currency": "usd",
  "description": null,
  "exchange_rate": null,
  "fee": 0,
  "fee_details": [],
  "net": -400,
  "reporting_category": "transfer",
  "source": "tr_1MiN3gLkdIwHu7ixNCZvFdgA",
  "status": "available",
  "type": "transfer"
}
```
