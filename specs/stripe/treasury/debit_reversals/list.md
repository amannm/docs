# List all DebitReversals

Returns a list of DebitReversals.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` DebitReversals, starting after DebitReversal `starting_after`. Each entry in the array is a separate DebitReversal object. If no more DebitReversals are available, the resulting array will be empty.

## Parameters

- `financial_account` (string, optional)
  Returns objects associated with this FinancialAccount.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `received_debit` (string, optional)
  Only return DebitReversals for the ReceivedDebit ID.

- `resolution` (enum, optional)
  Only return DebitReversals for a given resolution.
Possible enum values:
  - `lost`
    DebitReversal was lost, and no Transactions will be created.

  - `won`
    DebitReversal was won, and a crediting Transaction will be created.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Only return DebitReversals for a given status.
Possible enum values:
  - `canceled`
    The DebitReversal has been canceled before it has been sent to the network and no funds have been returned to the account. (Currently not supported).

  - `completed`
    The network has provided a resolution for the DebitReversal. If won, a crediting Transaction is created.

  - `processing`
    The DebitReversal starting state.

```curl
curl -G https://api.stripe.com/v1/treasury/debit_reversals \
  -u "<<YOUR_SECRET_KEY>>" \
  -d financial_account=fa_1MtkMLLkdIwHu7ixrkGP4bqB \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/treasury/debit_reversals",
  "has_more": false,
  "data": [
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
  ]
}
```
