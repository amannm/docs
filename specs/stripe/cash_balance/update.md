# Update a cash balance's settings

Changes the settings on a customer’s cash balance.

## Returns

The customer’s cash balance, with the updated settings.

## Parameters

- `settings` (object, optional)
  A hash of settings for this cash balance.

  - `settings.reconciliation_mode` (enum, optional)
    Controls how funds transferred by the customer are applied to payment intents and invoices. Valid options are `automatic`, `manual`, or `merchant_default`. For more information about these reconciliation modes, see [Reconciliation](https://docs.stripe.com/docs/payments/customer-balance/reconciliation.md).
Possible enum values:
    - `automatic`
    - `manual`
    - `merchant_default`

```curl
curl https://api.stripe.com/v1/customers/cus_Ob4Xiw8KXOqcvM/cash_balance \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "settings[reconciliation_mode]"=manual
```

### Response

```json
{
  "object": "cash_balance",
  "available": null,
  "customer": "cus_Ob4Xiw8KXOqcvM",
  "livemode": false,
  "settings": {
    "reconciliation_mode": "manual",
    "using_merchant_default": false
  }
}
```
