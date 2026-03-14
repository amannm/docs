# Update a FinancialAccount

Updates the details of a FinancialAccount.

## Returns

Returns a FinancialAccount object.

## Parameters

- `features` (object, optional)
  Encodes whether a FinancialAccount has access to a particular feature, with a status enum and associated `status_details`. Stripe or the platform may control features via the requested field.

  - `features.card_issuing` (object, optional)
    Encodes the FinancialAccount’s ability to be used with the Issuing product, including attaching cards to and drawing funds from the FinancialAccount.

    - `features.card_issuing.requested` (boolean, required)
      Whether the FinancialAccount should have the Feature.

  - `features.deposit_insurance` (object, optional)
    Represents whether this FinancialAccount is eligible for deposit insurance. Various factors determine the insurance amount.

    - `features.deposit_insurance.requested` (boolean, required)
      Whether the FinancialAccount should have the Feature.

  - `features.financial_addresses` (object, optional)
    Contains Features that add FinancialAddresses to the FinancialAccount.

    - `features.financial_addresses.aba` (object, optional)
      Adds an ABA FinancialAddress to the FinancialAccount.

      - `features.financial_addresses.aba.requested` (boolean, required)
        Whether the FinancialAccount should have the Feature.

  - `features.inbound_transfers` (object, optional)
    Contains settings related to adding funds to a FinancialAccount from another Account with the same owner.

    - `features.inbound_transfers.ach` (object, optional)
      Enables ACH Debits via the InboundTransfers API.

      - `features.inbound_transfers.ach.requested` (boolean, required)
        Whether the FinancialAccount should have the Feature.

  - `features.intra_stripe_flows` (object, optional)
    Represents the ability for the FinancialAccount to send money to, or receive money from other FinancialAccounts (for example, via OutboundPayment).

    - `features.intra_stripe_flows.requested` (boolean, required)
      Whether the FinancialAccount should have the Feature.

  - `features.outbound_payments` (object, optional)
    Includes Features related to initiating money movement out of the FinancialAccount to someone else’s bucket of money.

    - `features.outbound_payments.ach` (object, optional)
      Enables ACH transfers via the OutboundPayments API.

      - `features.outbound_payments.ach.requested` (boolean, required)
        Whether the FinancialAccount should have the Feature.

    - `features.outbound_payments.us_domestic_wire` (object, optional)
      Enables US domestic wire transfers via the OutboundPayments API.

      - `features.outbound_payments.us_domestic_wire.requested` (boolean, required)
        Whether the FinancialAccount should have the Feature.

  - `features.outbound_transfers` (object, optional)
    Contains a Feature and settings related to moving money out of the FinancialAccount into another Account with the same owner.

    - `features.outbound_transfers.ach` (object, optional)
      Enables ACH transfers via the OutboundTransfers API.

      - `features.outbound_transfers.ach.requested` (boolean, required)
        Whether the FinancialAccount should have the Feature.

    - `features.outbound_transfers.us_domestic_wire` (object, optional)
      Enables US domestic wire transfers via the OutboundTransfers API.

      - `features.outbound_transfers.us_domestic_wire.requested` (boolean, required)
        Whether the FinancialAccount should have the Feature.

- `forwarding_settings` (object, optional)
  A different bank account where funds can be deposited/debited in order to get the closing FA’s balance to $0

  - `forwarding_settings.type` (enum, required)
    The type of the bank account provided. This can be either “financial_account” or “payment_method”
Possible enum values:
    - `financial_account`
      A Financial Account belonging to the same Connected Account as the FA being closed

    - `payment_method`
      A payment method or verified bank account id representing an external bank account

  - `forwarding_settings.financial_account` (string, optional)
    The financial_account id

  - `forwarding_settings.payment_method` (string, optional)
    The payment_method or bank account id. This needs to be a verified bank account.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `nickname` (string, optional)
  The nickname for the FinancialAccount.

- `platform_restrictions` (object, optional)
  The set of functionalities that the platform can restrict on the FinancialAccount.

  - `platform_restrictions.inbound_flows` (enum, optional)
    Restricts all inbound money movement.
Possible enum values:
    - `restricted`
      The functionality is restricted.

    - `unrestricted`
      The functionality is not restricted.

  - `platform_restrictions.outbound_flows` (enum, optional)
    Restricts all outbound money movement.
Possible enum values:
    - `restricted`
      The functionality is restricted.

    - `unrestricted`
      The functionality is not restricted.

```curl
curl https://api.stripe.com/v1/treasury/financial_accounts/fa_1MtZmL2eZvKYlo2Cer6cdwEC \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
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
  "metadata": {
    "order_id": "6735"
  },
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
