# Retrieve a cash balance

Retrieves a customer’s cash balance.

## Returns

The Cash Balance object for a given customer.

```curl
curl https://api.stripe.com/v1/customers/cus_OaCLf8Fi1nbFpJ/cash_balance \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "object": "cash_balance",
  "available": {
    "eur": 10000
  },
  "customer": "cus_OaCLf8Fi1nbFpJ",
  "livemode": false,
  "settings": {
    "reconciliation_mode": "automatic",
    "using_merchant_default": true
  }
}
```
