# List all Transactions

Retrieves a list of Transaction objects.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` Transactions, starting after Transaction `starting_after`. Each entry in the array is a separate Transaction object. If no more Transactions are available, the resulting array will be empty.

## Parameters

- `financial_account` (string, optional)
  Returns objects associated with this FinancialAccount.

- `created` (object, optional)
  Only return Transactions that were created during the given date interval.

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
  The results are in reverse chronological order by `created` or `posted_at`. The default is `created`.
Possible enum values:
  - `created`
    Timestamp describing when the Transaction was created.

  - `posted_at`
    Timestamp describing when the Transaction was posted.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Only return Transactions that have the given status: `open`, `posted`, or `void`.
Possible enum values:
  - `open`
    The initial state for all Transactions. The Transaction results in updates to the sub-balance amounts, but the current balance is not affected until the Transaction posts.

  - `posted`
    Funds have successfully entered or left the account. The current balance was affected.

  - `void`
    The Transaction never impacted the balance. For example, a Transaction would enter this state if an OutboundPayment was initiated but then canceled before the funds left the account.

- `status_transitions` (object, optional)
  A filter for the `status_transitions.posted_at` timestamp. When using this filter, `status=posted` and `order_by=posted_at` must also be specified.

  - `status_transitions.posted_at` (object, optional)
    Returns Transactions with `posted_at` within the specified range.

    - `status_transitions.posted_at.gt` (integer, optional)
      Minimum value to filter by (exclusive)

    - `status_transitions.posted_at.gte` (integer, optional)
      Minimum value to filter by (inclusive)

    - `status_transitions.posted_at.lt` (integer, optional)
      Maximum value to filter by (exclusive)

    - `status_transitions.posted_at.lte` (integer, optional)
      Maximum value to filter by (inclusive)

```curl
curl -G https://api.stripe.com/v1/treasury/transactions \
  -u "<<YOUR_SECRET_KEY>>" \
  -d financial_account=fa_1MtkYw2eZvKYlo2CrqmzUo3O \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/treasury/transactions",
  "has_more": false,
  "data": [
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
  ]
}
```
