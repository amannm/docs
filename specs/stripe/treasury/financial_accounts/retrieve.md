# Retrieve a FinancialAccount

Retrieves the details of a FinancialAccount.

## Returns

Return a FinancialAccount object.

```curl
curl https://api.stripe.com/v1/treasury/financial_accounts/fa_1MtZmL2eZvKYlo2Cer6cdwEC \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "fa_1MtZmL2eZvKYlo2Cer6cdwEC",
  "object": "treasury.financial_account",
  "active_features": [
    "financial_addresses.aba",
    "outbound_payments.ach",
    "outbound_payments.us_domestic_wire"
  ],
  "balance": {
    "cash": {
      "usd": 0
    },
    "inbound_pending": {
      "usd": 0
    },
    "outbound_pending": {
      "usd": 0
    }
  },
  "country": "US",
  "created": 1680714349,
  "financial_addresses": [
    {
      "aba": {
        "account_holder_name": "Jenny Rosen",
        "account_number_last4": "7890",
        "bank_name": "STRIPE TEST BANK",
        "routing_number": "0000000001"
      },
      "supported_networks": [
        "ach",
        "us_domestic_wire"
      ],
      "type": "aba"
    }
  ],
  "livemode": true,
  "metadata": null,
  "pending_features": [],
  "restricted_features": [],
  "status": "open",
  "status_details": {
    "closed": null
  },
  "supported_currencies": [
    "usd"
  ],
  "features": {}
}
```
