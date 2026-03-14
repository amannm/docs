# Retrieve the credit balance summary for a customer

Retrieves the credit balance summary for a customer.

## Returns

Returns the credit balance summary.

## Parameters

- `filter` (object, required)
  The filter criteria for the credit balance summary.

  - `filter.type` (enum, required)
    Specify the type of this filter.
Possible enum values:
    - `applicability_scope`
      The balance summary for a given applicability scope.

    - `credit_grant`
      The balance summary for a given credit grant.

  - `filter.applicability_scope` (object, optional)
    The billing credit applicability scope for which to fetch credit balance summary.

    - `filter.applicability_scope.billable_items` (array of objects, optional)
      A list of billable items that the credit grant can apply to. We currently only support metered billable items. Cannot be used in combination with `price_type` or `prices`.

      - `filter.applicability_scope.billable_items.id` (string, required)
        The billable item ID this credit grant should apply to.

    - `filter.applicability_scope.price_type` (enum, optional)
      The price type that credit grants can apply to. We currently only support the `metered` price type. Cannot be used in combination with `prices`.
Possible enum values:
      - `metered`
        Credit grants being created can only apply to metered prices.

    - `filter.applicability_scope.prices` (array of objects, optional)
      A list of prices that the credit grant can apply to. We currently only support the `metered` prices. Cannot be used in combination with `price_type`.

      - `filter.applicability_scope.prices.id` (string, required)
        The price ID this credit grant should apply to.

  - `filter.credit_grant` (string, optional)
    The credit grant for which to fetch credit balance summary.

- `customer` (string, optional)
  The customer whose credit balance summary you’re retrieving.

- `customer_account` (string, optional)
  The account representing the customer whose credit balance summary you’re retrieving.

```curl
curl -G https://api.stripe.com/v1/billing/credit_balance_summary \
  -u "<<YOUR_SECRET_KEY>>" \
  -d customer=cus_QsEHa3GKweMwih \
  -d "filter[type]"=credit_grant \
  -d "filter[credit_grant]"=credgr_test_61R9rvFh1HgrFIoCp41L6nFOS1ekDCeW
```

### Response

```json
{
  "object": "billing.credit_balance_summary",
  "balances": [
    {
      "available_balance": {
        "monetary": {
          "currency": "usd",
          "value": 1000
        },
        "type": "monetary"
      },
      "ledger_balance": {
        "monetary": {
          "currency": "usd",
          "value": 1000
        },
        "type": "monetary"
      }
    }
  ],
  "customer": "cus_QsEHa3GKweMwih",
  "livemode": false
}
```
