# The CreditReversal object

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

- `financial_account` (string)
  The FinancialAccount to reverse funds from.

- `hosted_regulatory_receipt_url` (string, nullable)
  A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `network` (enum)
  The rails used to reverse the funds.

- `received_credit` (string)
  The ReceivedCredit being reversed.

- `status` (enum)
  Status of the CreditReversal
Possible enum values:
  - `canceled`
    The CreditReversal has been canceled before it has been sent to the network and no funds have left the account. (Currently not supported).

  - `posted`
    The CreditReversal has been sent to the network and funds have left the account (with the Transaction posting)

  - `processing`
    The CreditReversal starting state. Funds are “held” by a pending Transaction (but they are still part of the current balance).

- `status_transitions` (object)
  Hash containing timestamps of when the object transitioned to a particular `status`.

  - `status_transitions.posted_at` (timestamp, nullable)
    Timestamp describing when the CreditReversal changed status to `posted`

- `transaction` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The Transaction associated with this object.

### The CreditReversal object

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
