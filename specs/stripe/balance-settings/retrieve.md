# Retrieve balance settings

Retrieves balance settings for a given connected account. Related guide: [Making API calls for connected accounts](https://docs.stripe.com/connect/authentication.md)

## Returns

Returns a balance settings object for the account specified in the request.

```curl
curl https://api.stripe.com/v1/balance_settings \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

### Response

```json
{
  "object": "balance_settings",
  "payments": {
    "debit_negative_balances": true,
    "payouts": {
      "minimum_balance_by_currency": {
        "usd": 1500,
        "cad": 8000
      },
      "schedule": {
        "interval": "weekly",
        "weekly_payout_days": [
          "monday",
          "wednesday"
        ]
      },
      "statement_descriptor": null,
      "status": "enabled"
    },
    "settlement_timing": {
      "delay_days_override": 3,
      "delay_days": 3
    }
  }
}
```
