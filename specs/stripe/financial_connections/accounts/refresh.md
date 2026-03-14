# Refresh Account data

Refreshes the data associated with a Financial Connections `Account`.

## Returns

Returns an `Account` object if a valid identifier was provided and if you have sufficient permissions to that account. Raises [an error](refresh.md#errors) otherwise.

## Parameters

- `features` (array of enums, required)
  The list of account features that you would like to refresh.
Possible enum values:
  - `balance`
    Balance data from the account

  - `ownership`
    Ownership data from the account

  - `transactions`
    Transactions data from the account

```curl
curl https://api.stripe.com/v1/financial_connections/accounts/fca_1MwVK82eZvKYlo2Cjw8FMxXf/refresh \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "features[]"=balance
```

### Response

```json
{
  "id": "fca_1MwVK82eZvKYlo2Cjw8FMxXf",
  "object": "financial_connections.account",
  "account_holder": {
    "customer": "cus_9s6XI9OFIdpjIg",
    "type": "customer"
  },
  "balance": null,
  "balance_refresh": {
    "status": "pending",
    "last_attempted_at": 1681422295
  },
  "category": "cash",
  "created": 1681412208,
  "display_name": "Sample Checking Account",
  "institution_name": "StripeBank",
  "last4": "6789",
  "livemode": false,
  "ownership": null,
  "ownership_refresh": null,
  "permissions": [],
  "status": "pending",
  "subcategory": "checking",
  "subscriptions": [],
  "supported_payment_method_types": [
    "us_bank_account"
  ],
  "transaction_refresh": null
}
```
