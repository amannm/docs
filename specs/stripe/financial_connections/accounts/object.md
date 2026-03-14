# The Account object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `account_holder` (object, nullable)
  The account holder that this account belongs to.

  - `account_holder.account` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
    The ID of the Stripe account that this account belongs to. Only available when `account_holder.type` is `account`.

  - `account_holder.customer` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
    The ID for an Account representing a customer that this account belongs to. Only available when `account_holder.type` is `customer`.

  - `account_holder.type` (enum)
    Type of account holder that this account belongs to.
Possible enum values:
    - `account`
      Account holder is a Stripe account object.

    - `customer`
      Account holder is a Stripe customer object.

- `account_numbers` (array of objects, nullable)
  Details about the account numbers.

  - `account_numbers.expected_expiry_date` (timestamp, nullable)
    When the account number is expected to expire, if applicable.

  - `account_numbers.identifier_type` (enum)
    The type of account number associated with the account.
Possible enum values:
    - `account_number`
      The account has a permanent account number.

    - `tokenized_account_number`
      The account number is a tokenized, will not match the permanent account number, and may become deactivated.

  - `account_numbers.status` (enum)
    Whether the account number is currently active and usable for transactions.
Possible enum values:
    - `deactivated`
      The tokenized account number cannot be used for transfers. It may have been revoked by the user.

    - `transactable`
      The account numbers can be used for transfers.

  - `account_numbers.supported_networks` (array of enums)
    The payment networks that the account number can be used for.
Possible enum values:
    - `ach`
      The account number can be used for ACH direct debit transactions.

- `balance` (object, nullable)
  The most recent information about the account’s balance.

  - `balance.as_of` (timestamp)
    The time that the external institution calculated this balance. Measured in seconds since the Unix epoch.

  - `balance.cash` (object, nullable)
    Information on a `cash` balance. Only set if `balance.type` is `cash`.

    - `balance.cash.available` (object, nullable)
      The funds available to the account holder. Typically this is the current balance after subtracting any outbound pending transactions and adding any inbound pending transactions.

      Each key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.

      Each value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder.

  - `balance.credit` (object, nullable)
    Information on a `credit` balance. Only set if `balance.type` is `credit`.

    - `balance.credit.used` (object, nullable)
      The credit that has been used by the account holder.

      Each key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.

      Each value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder.

  - `balance.current` (object)
    The balances owed to (or by) the account holder, before subtracting any outbound pending transactions or adding any inbound pending transactions.

    Each key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.

    Each value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder.

  - `balance.type` (enum)
    The `type` of the balance. An additional hash is included on the balance with a name matching this value.
Possible enum values:
    - `cash`
      Account balance is a cash balance

    - `credit`
      Account balance is a credit balance

- `balance_refresh` (object, nullable)
  The state of the most recent attempt to refresh the account balance.

  - `balance_refresh.last_attempted_at` (timestamp)
    The time at which the last refresh attempt was initiated. Measured in seconds since the Unix epoch.

  - `balance_refresh.next_refresh_available_at` (timestamp, nullable)
    Time at which the next balance refresh can be initiated. This value will be `null` when `status` is `pending`. Measured in seconds since the Unix epoch.

  - `balance_refresh.status` (enum)
    The status of the last refresh attempt.
Possible enum values:
    - `failed`
      The last balance refresh attempt failed.

    - `pending`
      The last balance refresh attempt is pending.

    - `succeeded`
      The last balance refresh attempt succeeded.

- `category` (enum)
  The type of the account. Account category is further divided in `subcategory`.
Possible enum values:
  - `cash`
    The account represents real funds held by the institution (e.g. a checking or savings account).

  - `credit`
    The account represents credit extended by the institution (e.g. a credit card or mortgage).

  - `investment`
    The account represents investments, or any account where there are funds of unknown liquidity.

  - `other`
    The account does not fall under the other categories.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `display_name` (string, nullable)
  A human-readable name that has been assigned to this account, either by the account holder or by the institution.

- `institution_name` (string)
  The name of the institution that holds this account.

- `last4` (string, nullable)
  The last 4 digits of the account number. If present, this will be 4 numeric characters.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `ownership` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The most recent information about the account’s owners.

- `ownership_refresh` (object, nullable)
  The state of the most recent attempt to refresh the account owners.

  - `ownership_refresh.last_attempted_at` (timestamp)
    The time at which the last refresh attempt was initiated. Measured in seconds since the Unix epoch.

  - `ownership_refresh.next_refresh_available_at` (timestamp, nullable)
    Time at which the next ownership refresh can be initiated. This value will be `null` when `status` is `pending`. Measured in seconds since the Unix epoch.

  - `ownership_refresh.status` (enum)
    The status of the last refresh attempt.
Possible enum values:
    - `failed`
      The last ownership refresh attempt failed.

    - `pending`
      The last ownership refresh attempt is pending.

    - `succeeded`
      The last ownership refresh attempt succeeded.

- `permissions` (array of enums, nullable)
  The list of permissions granted by this account.
Possible enum values:
  - `balances`
    Allows accessing balance data from the account.

  - `ownership`
    Allows accessing ownership data from the account.

  - `payment_method`
    Allows the creation of a payment method from the account.

  - `transactions`
    Allows accessing transactions data from the account.

- `status` (enum)
  The status of the link to the account.
Possible enum values:
  - `active`
    Stripe is able to retrieve data from the Account without issues.

  - `disconnected`
    Account connection has been terminated through the [disconnect API](https://docs.stripe.com/docs/api/financial_connections/accounts/disconnect.md) or an [end user request](https://support.stripe.com/user/how-do-i-disconnect-my-linked-financial-account).

  - `inactive`
    Stripe cannot retrieve data from the Account.

- `subcategory` (enum)
  If `category` is `cash`, one of:

  - `checking`
  - `savings`
  - `other`

  If `category` is `credit`, one of:

  - `mortgage`
  - `line_of_credit`
  - `credit_card`
  - `other`

  If `category` is `investment` or `other`, this will be `other`.
Possible enum values:
  - `checking`
    The account is a checking account.

  - `credit_card`
    The account represents a credit card.

  - `line_of_credit`
    The account represents a line of credit.

  - `mortgage`
    The account represents a mortgage.

  - `other`
    The account does not fall under any of the other subcategories.

  - `savings`
    The account is a savings account.

- `subscriptions` (array of enums, nullable)
  The list of data refresh subscriptions requested on this account.
Possible enum values:
  - `transactions`
    Subscribes to periodic transactions data refreshes from the account.

- `supported_payment_method_types` (array of enums)
  The [PaymentMethod type](https://docs.stripe.com/docs/api/payment_methods/object.md#payment_method_object-type)(s) that can be created from this account.
Possible enum values:
  - `link`
    A `link` PaymentMethod can be created.

  - `us_bank_account`
    A `us_bank_account` PaymentMethod can be created.

- `transaction_refresh` (object, nullable)
  The state of the most recent attempt to refresh the account transactions.

  - `transaction_refresh.id` (string)
    Unique identifier for the object.

  - `transaction_refresh.last_attempted_at` (timestamp)
    The time at which the last refresh attempt was initiated. Measured in seconds since the Unix epoch.

  - `transaction_refresh.next_refresh_available_at` (timestamp, nullable)
    Time at which the next transaction refresh can be initiated. This value will be `null` when `status` is `pending`. Measured in seconds since the Unix epoch.

  - `transaction_refresh.status` (enum)
    The status of the last refresh attempt.
Possible enum values:
    - `failed`
      The last transaction refresh attempt failed.

    - `pending`
      The last transaction refresh attempt is pending.

    - `succeeded`
      The last transaction refresh attempt succeeded.

### The Account object

```json
{
  "id": "fca_1MwVK82eZvKYlo2Cjw8FMxXf",
  "object": "financial_connections.account",
  "account_holder": {
    "customer": "cus_9s6XI9OFIdpjIg",
    "type": "customer"
  },
  "balance": null,
  "balance_refresh": null,
  "category": "cash",
  "created": 1681412208,
  "display_name": "Sample Checking Account",
  "institution_name": "StripeBank",
  "last4": "6789",
  "livemode": false,
  "ownership": null,
  "ownership_refresh": null,
  "permissions": [],
  "status": "active",
  "subcategory": "checking",
  "subscriptions": [],
  "supported_payment_method_types": [
    "us_bank_account"
  ],
  "transaction_refresh": null
}
```
