# Retrieve FinancialAccount Features

Retrieves Features information associated with the FinancialAccount.

## Returns

A dictionary of Features associated with the given FinancialAccount. Each entry in the dictionary is a Feature object, which might contain child Features.

```curl
curl https://api.stripe.com/v1/treasury/financial_accounts/fa_1Mta0C2eZvKYlo2CaEtaPPFz/features \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "object": "treasury.financial_account_features",
  "card_issuing": {
    "requested": true,
    "status": "active",
    "status_details": []
  },
  "deposit_insurance": {
    "requested": true,
    "status": "active",
    "status_details": []
  },
  "financial_addresses": {
    "aba": {
      "requested": true,
      "status": "active",
      "status_details": []
    }
  },
  "inbound_transfers": {
    "ach": {
      "requested": true,
      "status": "active",
      "status_details": []
    }
  },
  "intra_stripe_flows": {
    "requested": true,
    "status": "active",
    "status_details": []
  },
  "outbound_payments": {
    "ach": {
      "requested": true,
      "status": "active",
      "status_details": []
    },
    "us_domestic_wire": {
      "requested": true,
      "status": "active",
      "status_details": []
    }
  },
  "outbound_transfers": {
    "ach": {
      "requested": true,
      "status": "active",
      "status_details": []
    },
    "us_domestic_wire": {
      "requested": true,
      "status": "active",
      "status_details": []
    }
  }
}
```
