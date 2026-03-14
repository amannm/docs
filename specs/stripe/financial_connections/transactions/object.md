# The Transaction object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `account` (string)
  The ID of the Financial Connections Account this transaction belongs to.

- `amount` (integer)
  The amount of this transaction, in cents.

- `currency` (string)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `description` (string)
  The description of this transaction.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `status` (enum)
  The status of the transaction.
Possible enum values:
  - `pending`
    This transaction is processing and does not yet affect the account’s balance.

  - `posted`
    This transaction has processed and affects the account’s balance.

  - `void`
    This transaction has disappeared and no longer affects the account’s balance.

- `status_transitions` (object)
  The timestamps at which the transaction status was updated.

  - `status_transitions.posted_at` (timestamp, nullable)
    Time at which this transaction posted. Measured in seconds since the Unix epoch.

  - `status_transitions.void_at` (timestamp, nullable)
    Time at which this transaction was voided. Measured in seconds since the Unix epoch.

- `transacted_at` (timestamp)
  Time at which the transaction was transacted. Measured in seconds since the Unix epoch.

- `transaction_refresh` (string)
  The token of the transaction refresh that last updated or created this transaction.

- `updated` (timestamp)
  Time at which the object was last updated. Measured in seconds since the Unix epoch.

### The Transaction object

```json
{
  "id": "fctxn_1MwVKd2eZvKYlo2ChNw2UxSa",
  "object": "financial_connections.transaction",
  "account": "fca_1MwVKd2eZvKYlo2CnlgoF3I4",
  "amount": 300,
  "currency": "usd",
  "description": "Rocket Rides",
  "livemode": false,
  "status": "posted",
  "status_transitions": {
    "posted_at": 1681412239,
    "void_at": null
  },
  "transacted_at": 1681412239,
  "transaction_refresh": "fctxnref_NhvAgiKSFDg9jOe6eIlj41X5",
  "updated": 1681412239
}
```
