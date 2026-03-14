# Subscribe to data refreshes for an Account

Subscribes to periodic refreshes of data associated with a Financial Connections `Account`. When the account status is active, data is typically refreshed once a day.

## Returns

Returns an `Account` object if a valid identifier was provided and if you have sufficient permissions to that account. Raises [an error](subscribe.md#errors) otherwise.

## Parameters

- `features` (array of enums, required)
  The list of account features to which you would like to subscribe.
Possible enum values:
  - `transactions`
    Transactions data from the account

```curl
curl https://api.stripe.com/v1/financial_connections/accounts/fca_1NQay62eZvKYlo2C8dflHjWB/subscribe \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "features[]"=transactions
```

### Response

```json
{
  "id": "fca_1NQay62eZvKYlo2C8dflHjWB",
  "object": "financial_connections.account",
  "account_holder": {
    "customer": "cus_9s6XKzkNRiz8i3",
    "type": "customer"
  },
  "balance": null,
  "balance_refresh": null,
  "category": "cash",
  "created": 1688583746,
  "display_name": "Sample Checking Account",
  "institution_name": "StripeBank",
  "last4": "6789",
  "livemode": false,
  "ownership": null,
  "ownership_refresh": null,
  "permissions": [],
  "status": "active",
  "subcategory": "checking",
  "subscriptions": [
    "transactions"
  ],
  "supported_payment_method_types": [
    "us_bank_account"
  ],
  "transaction_refresh": {
    "id": "fctxnref_OD10iHSd7eaheDkeabbQfnJ7",
    "status": "pending",
    "last_attempted_at": 1625337296
  }
}
```
