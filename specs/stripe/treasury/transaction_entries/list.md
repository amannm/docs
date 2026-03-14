# List all TransactionEntries

Retrieves a list of TransactionEntry objects.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` TransactionEntries, starting after TransactionEntry `starting_after`. Each entry in the array is a separate TransactionEntry object. If no more TransactionEntries are available, the resulting array is empty.

## Parameters

- `financial_account` (string, optional)
  Returns objects associated with this FinancialAccount.

- `created` (object, optional)
  Only return TransactionEntries that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `order_by` (enum, optional)
  The results are in reverse chronological order by `created` or `effective_at`. The default is `created`.
Possible enum values:
  - `created`
    Timestamp describing when the TransactionEntry was created.

  - `effective_at`
    Timestamp describing when the TransactionEntry was effective.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `transaction` (string, optional)
  Only return TransactionEntries associated with this Transaction.

```curl
curl -G https://api.stripe.com/v1/treasury/transaction_entries \
  -u "<<YOUR_SECRET_KEY>>" \
  -d financial_account=fa_1MtkgV2eZvKYlo2CdxyvnHeQ \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/treasury/transaction_entries",
  "has_more": false,
  "data": [
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
  ]
}
```
