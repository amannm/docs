# The DebitReversal object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  Amount (in cents) transferred.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `financial_account` (string, nullable)
  The FinancialAccount to reverse funds from.

- `hosted_regulatory_receipt_url` (string, nullable)
  A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

- `linked_flows` (object, nullable)
  Other flows linked to a DebitReversal.

  - `linked_flows.issuing_dispute` (string, nullable)
    Set if there is an Issuing dispute associated with the DebitReversal.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `network` (enum)
  The rails used to reverse the funds.

- `received_debit` (string)
  The ReceivedDebit being reversed.

- `status` (enum)
  Status of the DebitReversal
Possible enum values:
  - `failed`
    The network has resolved the DebitReversal against the user.

  - `processing`
    The DebitReversal starting state.

  - `succeeded`
    The network has resolved the DebitReversal in the users favour. A crediting Transaction is created.

- `status_transitions` (object)
  Hash containing timestamps of when the object transitioned to a particular `status`.

  - `status_transitions.completed_at` (timestamp, nullable)
    Timestamp describing when the DebitReversal changed status to `completed`.

- `transaction` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The Transaction associated with this object.

### The DebitReversal object

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
