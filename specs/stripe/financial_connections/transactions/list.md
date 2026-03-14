# List Transactions

Returns a list of Financial Connections `Transaction` objects.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` `Transaction` objects, starting after transaction `starting_after`. Each entry in the array is a separate `Transaction` object. If no more transactions are available, the resulting array will be empty.

## Parameters

- `account` (string, required)
  The ID of the Financial Connections Account whose transactions will be retrieved.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `transacted_at` (object, optional)
  A filter on the list based on the object `transacted_at` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with the following options:

  - `transacted_at.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `transacted_at.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `transacted_at.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `transacted_at.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `transaction_refresh` (object, optional)
  A filter on the list based on the object `transaction_refresh` field. The value can be a dictionary with the following options:

  - `transaction_refresh.after` (string, required)
    Return results where the transactions were created or updated by a refresh that took place after this refresh (non-inclusive).

```curl
curl -G https://api.stripe.com/v1/financial_connections/transactions \
  -u "<<YOUR_SECRET_KEY>>" \
  -d account=fca_1NpHiT2eZvKYlo2C6pRwOFjr \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/financial_connections/transactions",
  "has_more": false,
  "data": [
    {
      "id": "fctxn_1NpHiT2eZvKYlo2CZFvnM3HJ",
      "object": "financial_connections.transaction",
      "account": "fca_1NpHiT2eZvKYlo2C6pRwOFjr",
      "amount": 300,
      "currency": "usd",
      "description": "Rocket Rides",
      "livemode": false,
      "status": "posted",
      "status_transitions": {
        "posted_at": 1694467941,
        "void_at": null
      },
      "transacted_at": 1694467941,
      "transaction_refresh": "fctxnref_OcWmGrWptAdJ2bmpYE2P0Hws",
      "updated": 1694467941
    }
  ]
}
```
