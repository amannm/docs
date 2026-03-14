# Test mode: Create a ReceivedDebit

Use this endpoint to simulate a test mode ReceivedDebit initiated by a third party. In live mode, you can’t directly create ReceivedDebits initiated by third parties.

## Returns

A test mode ReceivedDebit object.

## Parameters

- `amount` (integer, required)
  Amount (in cents) to be transferred.

- `currency` (enum, required)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `financial_account` (string, required)
  The FinancialAccount to pull funds from.

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
curl https://api.stripe.com/v1/test_helpers/treasury/received_debits \
  -u "<<YOUR_SECRET_KEY>>" \
  -d amount=1000 \
  -d currency=usd \
  -d financial_account=fa_1MtkUY2eZvKYlo2CY3s6OQyK \
  -d network=ach
```

### Response

```json
{
  "id": "rd_1MtkUY2eZvKYlo2CT9SYD1AF",
  "object": "treasury.received_debit",
  "amount": 1000,
  "created": 1680755530,
  "currency": "usd",
  "description": "Stripe Test",
  "failure_code": null,
  "financial_account": "fa_1MtkUY2eZvKYlo2CY3s6OQyK",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg",
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
    "debit_reversal": null,
    "inbound_transfer": null,
    "issuing_authorization": null,
    "issuing_transaction": null,
    "payout": null
  },
  "livemode": false,
  "network": "ach",
  "reversal_details": {
    "deadline": 1681084800,
    "restricted_reason": null
  },
  "status": "succeeded",
  "transaction": "trxn_1MtkUY2eZvKYlo2ChymLKPp5"
}
```
