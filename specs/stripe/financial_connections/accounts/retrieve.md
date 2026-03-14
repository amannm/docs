# Retrieve an Account

Retrieves the details of an Financial Connections `Account`.

## Returns

Returns an `Account` object if a valid identifier was provided, and raises [an error](retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/financial_connections/accounts/fca_1MwVK82eZvKYlo2Cjw8FMxXf \
  -u "<<YOUR_SECRET_KEY>>"
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
