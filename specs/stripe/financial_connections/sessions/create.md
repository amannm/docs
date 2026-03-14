# Create a Session

To launch the Financial Connections authorization flow, create a `Session`. The session’s `client_secret` can be used to launch the flow using Stripe.js.

## Returns

Returns the `Session` object.

## Parameters

- `account_holder` (object, required)
  The account holder to link accounts for.

  - `account_holder.type` (enum, required)
    Type of account holder to collect accounts for.

  - `account_holder.account` (string, optional)
    The ID of the Stripe account whose accounts you will retrieve. Only available when `type` is `account`.

  - `account_holder.customer` (string, optional)
    The ID of the Stripe customer whose accounts you will retrieve. Only available when `type` is `customer`.

  - `account_holder.customer_account` (string, optional)
    The ID of Account representing a customer whose accounts you will retrieve. Only available when `type` is `customer`.

- `permissions` (array of strings, required)
  List of data features that you would like to request access to.

  Possible values are `balances`, `transactions`, `ownership`, and `payment_method`.

- `filters` (object, optional)
  Filters to restrict the kinds of accounts to collect.

  - `filters.account_subcategories` (array of enums, optional)
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

  - `filters.countries` (array of strings, optional)
    List of countries from which to collect accounts.

- `prefetch` (array of enums, optional)
  List of data features that you would like to retrieve upon account creation.
Possible enum values:
  - `balances`
    Requests to prefetch balance data on accounts collected in this session.

  - `ownership`
    Requests to prefetch ownership data on accounts collected in this session.

  - `transactions`
    Requests to prefetch transaction data on accounts collected in this session.

- `return_url` (string, optional)
  For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app.

```curl
curl https://api.stripe.com/v1/financial_connections/sessions \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "account_holder[type]"=customer \
  -d "account_holder[customer]"=cus_NiKSWdaFz2F6I0 \
  -d "permissions[]"=payment_method \
  -d "permissions[]"=balances \
  -d "filters[countries][]"=US
```

### Response

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
