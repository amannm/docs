# The Session object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `account_holder` (object, nullable)
  The account holder for whom accounts are collected in this session.

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

- `accounts` (object)
  The accounts that were collected as part of this Session.

  - `accounts.object` (string)
    String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

  - `accounts.data` (array of objects)
    Details about each object.

    - `accounts.data.id` (string)
      Unique identifier for the object.

    - `accounts.data.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `accounts.data.account_holder` (object, nullable)
      The account holder that this account belongs to.

      - `accounts.data.account_holder.account` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        The ID of the Stripe account that this account belongs to. Only available when `account_holder.type` is `account`.

      - `accounts.data.account_holder.customer` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        The ID for an Account representing a customer that this account belongs to. Only available when `account_holder.type` is `customer`.

      - `accounts.data.account_holder.type` (enum)
        Type of account holder that this account belongs to.
Possible enum values:
        - `account`
          Account holder is a Stripe account object.

        - `customer`
          Account holder is a Stripe customer object.

    - `accounts.data.account_numbers` (array of objects, nullable)
      Details about the account numbers.

      - `accounts.data.account_numbers.expected_expiry_date` (timestamp, nullable)
        When the account number is expected to expire, if applicable.

      - `accounts.data.account_numbers.identifier_type` (enum)
        The type of account number associated with the account.
Possible enum values:
        - `account_number`
          The account has a permanent account number.

        - `tokenized_account_number`
          The account number is a tokenized, will not match the permanent account number, and may become deactivated.

      - `accounts.data.account_numbers.status` (enum)
        Whether the account number is currently active and usable for transactions.
Possible enum values:
        - `deactivated`
          The tokenized account number cannot be used for transfers. It may have been revoked by the user.

        - `transactable`
          The account numbers can be used for transfers.

      - `accounts.data.account_numbers.supported_networks` (array of enums)
        The payment networks that the account number can be used for.
Possible enum values:
        - `ach`
          The account number can be used for ACH direct debit transactions.

    - `accounts.data.balance` (object, nullable)
      The most recent information about the account’s balance.

      - `accounts.data.balance.as_of` (timestamp)
        The time that the external institution calculated this balance. Measured in seconds since the Unix epoch.

      - `accounts.data.balance.cash` (object, nullable)
        Information on a `cash` balance. Only set if `balance.type` is `cash`.

        - `accounts.data.balance.cash.available` (object, nullable)
          The funds available to the account holder. Typically this is the current balance after subtracting any outbound pending transactions and adding any inbound pending transactions.

          Each key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.

          Each value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder.

      - `accounts.data.balance.credit` (object, nullable)
        Information on a `credit` balance. Only set if `balance.type` is `credit`.

        - `accounts.data.balance.credit.used` (object, nullable)
          The credit that has been used by the account holder.

          Each key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.

          Each value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder.

      - `accounts.data.balance.current` (object)
        The balances owed to (or by) the account holder, before subtracting any outbound pending transactions or adding any inbound pending transactions.

        Each key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.

        Each value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder.

      - `accounts.data.balance.type` (enum)
        The `type` of the balance. An additional hash is included on the balance with a name matching this value.
Possible enum values:
        - `cash`
          Account balance is a cash balance

        - `credit`
          Account balance is a credit balance

    - `accounts.data.balance_refresh` (object, nullable)
      The state of the most recent attempt to refresh the account balance.

      - `accounts.data.balance_refresh.last_attempted_at` (timestamp)
        The time at which the last refresh attempt was initiated. Measured in seconds since the Unix epoch.

      - `accounts.data.balance_refresh.next_refresh_available_at` (timestamp, nullable)
        Time at which the next balance refresh can be initiated. This value will be `null` when `status` is `pending`. Measured in seconds since the Unix epoch.

      - `accounts.data.balance_refresh.status` (enum)
        The status of the last refresh attempt.
Possible enum values:
        - `failed`
          The last balance refresh attempt failed.

        - `pending`
          The last balance refresh attempt is pending.

        - `succeeded`
          The last balance refresh attempt succeeded.

    - `accounts.data.category` (enum)
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

    - `accounts.data.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `accounts.data.display_name` (string, nullable)
      A human-readable name that has been assigned to this account, either by the account holder or by the institution.

    - `accounts.data.institution_name` (string)
      The name of the institution that holds this account.

    - `accounts.data.last4` (string, nullable)
      The last 4 digits of the account number. If present, this will be 4 numeric characters.

    - `accounts.data.livemode` (boolean)
      If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

    - `accounts.data.ownership` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
      The most recent information about the account’s owners.

    - `accounts.data.ownership_refresh` (object, nullable)
      The state of the most recent attempt to refresh the account owners.

      - `accounts.data.ownership_refresh.last_attempted_at` (timestamp)
        The time at which the last refresh attempt was initiated. Measured in seconds since the Unix epoch.

      - `accounts.data.ownership_refresh.next_refresh_available_at` (timestamp, nullable)
        Time at which the next ownership refresh can be initiated. This value will be `null` when `status` is `pending`. Measured in seconds since the Unix epoch.

      - `accounts.data.ownership_refresh.status` (enum)
        The status of the last refresh attempt.
Possible enum values:
        - `failed`
          The last ownership refresh attempt failed.

        - `pending`
          The last ownership refresh attempt is pending.

        - `succeeded`
          The last ownership refresh attempt succeeded.

    - `accounts.data.permissions` (array of enums, nullable)
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

    - `accounts.data.status` (enum)
      The status of the link to the account.
Possible enum values:
      - `active`
        Stripe is able to retrieve data from the Account without issues.

      - `disconnected`
        Account connection has been terminated through the [disconnect API](https://docs.stripe.com/docs/api/financial_connections/accounts/disconnect.md) or an [end user request](https://support.stripe.com/user/how-do-i-disconnect-my-linked-financial-account).

      - `inactive`
        Stripe cannot retrieve data from the Account.

    - `accounts.data.subcategory` (enum)
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

    - `accounts.data.subscriptions` (array of enums, nullable)
      The list of data refresh subscriptions requested on this account.
Possible enum values:
      - `transactions`
        Subscribes to periodic transactions data refreshes from the account.

    - `accounts.data.supported_payment_method_types` (array of enums)
      The [PaymentMethod type](https://docs.stripe.com/docs/api/payment_methods/object.md#payment_method_object-type)(s) that can be created from this account.
Possible enum values:
      - `link`
        A `link` PaymentMethod can be created.

      - `us_bank_account`
        A `us_bank_account` PaymentMethod can be created.

    - `accounts.data.transaction_refresh` (object, nullable)
      The state of the most recent attempt to refresh the account transactions.

      - `accounts.data.transaction_refresh.id` (string)
        Unique identifier for the object.

      - `accounts.data.transaction_refresh.last_attempted_at` (timestamp)
        The time at which the last refresh attempt was initiated. Measured in seconds since the Unix epoch.

      - `accounts.data.transaction_refresh.next_refresh_available_at` (timestamp, nullable)
        Time at which the next transaction refresh can be initiated. This value will be `null` when `status` is `pending`. Measured in seconds since the Unix epoch.

      - `accounts.data.transaction_refresh.status` (enum)
        The status of the last refresh attempt.
Possible enum values:
        - `failed`
          The last transaction refresh attempt failed.

        - `pending`
          The last transaction refresh attempt is pending.

        - `succeeded`
          The last transaction refresh attempt succeeded.

  - `accounts.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `accounts.url` (string)
    The URL where this list can be accessed.

- `client_secret` (string, nullable)
  A value that will be passed to the client to launch the authentication flow.

- `filters` (object, nullable)
  Filters applied to this session that restrict the kinds of accounts to collect.

  - `filters.account_subcategories` (array of enums, nullable)
    Restricts the Session to subcategories of accounts that can be linked. Valid subcategories are: `checking`, `savings`, `mortgage`, `line_of_credit`, `credit_card`.
Possible enum values:
    - `checking`
      The account is a checking account.

    - `credit_card`
      The account represents a credit card.

    - `line_of_credit`
      The account represents a line of credit.

    - `mortgage`
      The account represents a mortgage.

    - `savings`
      The account is a savings account.

  - `filters.countries` (array of strings, nullable)
    List of countries from which to filter accounts.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `permissions` (array of enums)
  Permissions requested for accounts collected during this session.
Possible enum values:
  - `balances`
    Requests access for balance data on accounts collected in this session.

  - `ownership`
    Requests access for ownership data on accounts collected in this session.

  - `payment_method`
    Requests permission for the creation of a payment method from an account collected in this session.

  - `transactions`
    Requests access for transaction data on accounts collected in this session.

- `prefetch` (array of enums, nullable)
  Data features requested to be retrieved upon account creation.
Possible enum values:
  - `balances`
    Requests to prefetch balance data on accounts collected in this session.

  - `ownership`
    Requests to prefetch ownership data on accounts collected in this session.

  - `transactions`
    Requests to prefetch transaction data on accounts collected in this session.

- `return_url` (string, nullable)
  For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app.

### The Session object

```json
{
  "id": "fcsess_1MwtnGLkdIwHu7ixs7NPQ7dq",
  "object": "financial_connections.session",
  "account_holder": {
    "customer": "cus_NiKSWdaFz2F6I0",
    "type": "customer"
  },
  "accounts": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/financial_connections/accounts"
  },
  "client_secret": "fcsess_client_secret_KRJTKvCY3IKoYTrW18EazcO3",
  "filters": {
    "countries": [
      "US"
    ]
  },
  "livemode": false,
  "permissions": [
    "balances",
    "payment_method"
  ]
}
```
