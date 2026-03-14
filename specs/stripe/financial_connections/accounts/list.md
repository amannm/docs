# List Accounts

Returns a list of Financial Connections `Account` objects.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` `Account` objects, starting after account `starting_after`. Each entry in the array is a separate `Account` object. If no more accounts are available, the resulting array will be empty. This request will raise an error if more than one of `account_holder[account]`, `account_holder[customer]`, or `session` is specified.

## Parameters

- `account_holder` (object, optional)
  If present, only return accounts that belong to the specified account holder. `account_holder[customer]` and `account_holder[account]` are mutually exclusive.

  - `account_holder.account` (string, optional)
    The ID of the Stripe account whose accounts you will retrieve.

  - `account_holder.customer` (string, optional)
    The ID of the Stripe customer whose accounts you will retrieve.

  - `account_holder.customer_account` (string, optional)
    The ID of the Account representing a customer whose accounts you will retrieve.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `session` (string, optional)
  If present, only return accounts that were collected as part of the given session.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/financial_connections/accounts \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/financial_connections/accounts",
  "has_more": false,
  "data": [
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
  ]
}
```
