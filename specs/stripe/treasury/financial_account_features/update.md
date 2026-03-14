# Update FinancialAccount Features

Updates the Features associated with a FinancialAccount.

## Returns

A dictionary of Features associated with the given FinancialAccount. Each entry in the dictionary is a Feature object, which may contain child Features.

## Parameters

- `card_issuing` (object, optional)
  Encodes the FinancialAccount’s ability to be used with the Issuing product, including attaching cards to and drawing funds from the FinancialAccount.

  - `card_issuing.requested` (boolean, required)
    Whether the FinancialAccount should have the Feature.

- `deposit_insurance` (object, optional)
  Represents whether this FinancialAccount is eligible for deposit insurance. Various factors determine the insurance amount.

  - `deposit_insurance.requested` (boolean, required)
    Whether the FinancialAccount should have the Feature.

- `financial_addresses` (object, optional)
  Contains Features that add FinancialAddresses to the FinancialAccount.

  - `financial_addresses.aba` (object, optional)
    Adds an ABA FinancialAddress to the FinancialAccount.

    - `financial_addresses.aba.requested` (boolean, required)
      Whether the FinancialAccount should have the Feature.

- `inbound_transfers` (object, optional)
  Contains settings related to adding funds to a FinancialAccount from another Account with the same owner.

  - `inbound_transfers.ach` (object, optional)
    Enables ACH Debits via the InboundTransfers API.

    - `inbound_transfers.ach.requested` (boolean, required)
      Whether the FinancialAccount should have the Feature.

- `intra_stripe_flows` (object, optional)
  Represents the ability for the FinancialAccount to send money to, or receive money from other FinancialAccounts (for example, via OutboundPayment).

  - `intra_stripe_flows.requested` (boolean, required)
    Whether the FinancialAccount should have the Feature.

- `outbound_payments` (object, optional)
  Includes Features related to initiating money movement out of the FinancialAccount to someone else’s bucket of money.

  - `outbound_payments.ach` (object, optional)
    Enables ACH transfers via the OutboundPayments API.

    - `outbound_payments.ach.requested` (boolean, required)
      Whether the FinancialAccount should have the Feature.

  - `outbound_payments.us_domestic_wire` (object, optional)
    Enables US domestic wire transfers via the OutboundPayments API.

    - `outbound_payments.us_domestic_wire.requested` (boolean, required)
      Whether the FinancialAccount should have the Feature.

- `outbound_transfers` (object, optional)
  Contains a Feature and settings related to moving money out of the FinancialAccount into another Account with the same owner.

  - `outbound_transfers.ach` (object, optional)
    Enables ACH transfers via the OutboundTransfers API.

    - `outbound_transfers.ach.requested` (boolean, required)
      Whether the FinancialAccount should have the Feature.

  - `outbound_transfers.us_domestic_wire` (object, optional)
    Enables US domestic wire transfers via the OutboundTransfers API.

    - `outbound_transfers.us_domestic_wire.requested` (boolean, required)
      Whether the FinancialAccount should have the Feature.

```curl
curl https://api.stripe.com/v1/treasury/financial_accounts/fa_1Mta0C2eZvKYlo2CaEtaPPFz/features \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "card_issuing[requested]"=false
```

### Response

```json
{
  "object": "treasury.financial_account_features",
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
