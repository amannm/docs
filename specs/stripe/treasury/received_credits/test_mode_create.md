# Test mode: Create a ReceivedCredit

Use this endpoint to simulate a test mode ReceivedCredit initiated by a third party. In live mode, you can’t directly create ReceivedCredits initiated by third parties.

## Returns

A test mode ReceivedCredit object.

## Parameters

- `amount` (integer, required)
  Amount (in cents) to be transferred.

- `currency` (enum, required)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `financial_account` (string, required)
  The FinancialAccount to send funds to.

- `network` (enum, required)
  Specifies the network rails to be used. If not set, will default to the PaymentMethod’s preferred network. See the [docs](https://docs.stripe.com/docs/treasury/money-movement/timelines.md) to learn more about money movement timelines for each network type.

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `initiating_payment_method_details` (object, optional)
  Initiating payment method details for the object.

  - `initiating_payment_method_details.type` (enum, required)
    The source type.

  - `initiating_payment_method_details.us_bank_account` (object, optional)
    Optional fields for `us_bank_account`.

    - `initiating_payment_method_details.us_bank_account.account_holder_name` (string, optional)
      The bank account holder’s name.

    - `initiating_payment_method_details.us_bank_account.account_number` (string, optional)
      The bank account number.

    - `initiating_payment_method_details.us_bank_account.routing_number` (string, optional)
      The bank account’s routing number.

```curl
curl https://api.stripe.com/v1/test_helpers/treasury/received_credits \
  -u "<<YOUR_SECRET_KEY>>" \
  -d amount=1000 \
  -d currency=usd \
  -d financial_account=fa_1MtkSr2eZvKYlo2CsJozwFWD \
  -d network=ach
```

### Response

```json
{
  "id": "rc_1MtkSr2eZvKYlo2CcysvUbEw",
  "object": "treasury.received_credit",
  "amount": 1000,
  "created": 1680755425,
  "currency": "usd",
  "description": "Stripe Test",
  "failure_code": null,
  "financial_account": "fa_1MtkSr2eZvKYlo2CsJozwFWD",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw",
  "initiating_payment_method_details": {
    "billing_details": {
      "address": {
        "city": null,
        "country": null,
        "line1": null,
        "line2": null,
        "postal_code": null,
        "state": null
      },
      "email": null,
      "name": "Jane Austen"
    },
    "type": "us_bank_account",
    "us_bank_account": {
      "bank_name": "STRIPE TEST BANK",
      "last4": "6789",
      "routing_number": "110000000"
    }
  },
  "linked_flows": {
    "credit_reversal": null,
    "issuing_authorization": null,
    "issuing_transaction": null,
    "source_flow": null,
    "source_flow_type": null
  },
  "livemode": false,
  "network": "ach",
  "reversal_details": {
    "deadline": 1681084800,
    "restricted_reason": null
  },
  "status": "succeeded",
  "transaction": "trxn_1MtkSr2eZvKYlo2CuFFh9Rh0"
}
```
