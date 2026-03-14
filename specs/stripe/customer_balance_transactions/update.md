# Update a customer credit balance transaction

Most credit balance transaction fields are immutable, but you may update its `description` and `metadata`.

## Returns

Returns a customer balance transaction object if the call succeeded.

## Parameters

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

  The maximum length is 350 characters.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/customers/cus_NcjdgdwZyI9Rj7/balance_transactions/cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

### Response

```json
{
  "id": "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI",
  "object": "customer_balance_transaction",
  "amount": -500,
  "created": 1680216086,
  "credit_note": null,
  "currency": "usd",
  "customer": "cus_NcjdgdwZyI9Rj7",
  "description": null,
  "ending_balance": -500,
  "invoice": null,
  "livemode": false,
  "metadata": {
    "order_id": "6735"
  },
  "type": "adjustment"
}
```
