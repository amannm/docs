# The ReceivedDebit object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  Amount (in cents) transferred.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `description` (string)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `failure_code` (enum, nullable)
  Reason for the failure. A ReceivedDebit might fail because the FinancialAccount doesn’t have sufficient funds, is closed, or is frozen.
Possible enum values:
  - `account_closed`
    Funds can’t be pulled from a closed FinancialAccount.

  - `account_frozen`
    Funds can’t be pulled from a frozen FinancialAccount.

  - `insufficient_funds`
    The FinancialAccount doesn’t have a sufficient balance.

  - `international_transaction`
    International transactions can’t pull funds from the FinancialAccount.

  - `other`
    Funds can’t be pulled from the FinancialAccount for other reasons.

- `financial_account` (string, nullable)
  The FinancialAccount that funds were pulled from.

- `hosted_regulatory_receipt_url` (string, nullable)
  A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

- `initiating_payment_method_details` (object)
  Details about how a ReceivedDebit was created.

  - `initiating_payment_method_details.balance` (enum, nullable)
    Set when `type` is `balance`.
Possible enum values:
    - `payments`
      The Stripe payments balance.

  - `initiating_payment_method_details.billing_details` (object)
    The contact details of the person or business referenced by the received payment method details.

    - `initiating_payment_method_details.billing_details.address` (object)
      Billing address.

      - `initiating_payment_method_details.billing_details.address.city` (string, nullable)
        City, district, suburb, town, or village.

      - `initiating_payment_method_details.billing_details.address.country` (string, nullable)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `initiating_payment_method_details.billing_details.address.line1` (string, nullable)
        Address line 1, such as the street, PO Box, or company name.

      - `initiating_payment_method_details.billing_details.address.line2` (string, nullable)
        Address line 2, such as the apartment, suite, unit, or building.

      - `initiating_payment_method_details.billing_details.address.postal_code` (string, nullable)
        ZIP or postal code.

      - `initiating_payment_method_details.billing_details.address.state` (string, nullable)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `initiating_payment_method_details.billing_details.email` (string, nullable)
      Email address.

    - `initiating_payment_method_details.billing_details.name` (string, nullable)
      Full name.

  - `initiating_payment_method_details.financial_account` (object, nullable)
    Set when `type` is `financial_account`. This is a [FinancialAccount](object.md#financial_accounts) ID.

    - `initiating_payment_method_details.financial_account.id` (string)
      The FinancialAccount ID.

    - `initiating_payment_method_details.financial_account.network` (enum)
      The rails the ReceivedCredit was sent over. A FinancialAccount can only send funds over `stripe`.

  - `initiating_payment_method_details.issuing_card` (string, nullable)
    Set when `type` is `issuing_card`. This is an [Issuing Card](object.md#issuing_cards) ID.

  - `initiating_payment_method_details.type` (enum)
    Polymorphic type matching the originating money movement’s source. This can be an external account, a Stripe balance, or a FinancialAccount.

  - `initiating_payment_method_details.us_bank_account` (object, nullable)
    Set when `type` is `us_bank_account`.

    - `initiating_payment_method_details.us_bank_account.bank_name` (string, nullable)
      Bank name.

    - `initiating_payment_method_details.us_bank_account.last4` (string, nullable)
      The last four digits of the bank account number.

    - `initiating_payment_method_details.us_bank_account.routing_number` (string, nullable)
      The routing number for the bank account.

- `linked_flows` (object)
  Other flows linked to a ReceivedDebit.

  - `linked_flows.debit_reversal` (string, nullable)
    The DebitReversal created as a result of this ReceivedDebit being reversed.

  - `linked_flows.inbound_transfer` (string, nullable)
    Set if the ReceivedDebit is associated with an InboundTransfer’s return of funds.

  - `linked_flows.issuing_authorization` (string, nullable)
    Set if the ReceivedDebit was created due to an [Issuing Authorization](object.md#issuing_authorizations) object.

  - `linked_flows.issuing_transaction` (string, nullable)
    Set if the ReceivedDebit is also viewable as an [Issuing Dispute](object.md#issuing_disputes) object.

  - `linked_flows.payout` (string, nullable)
    Set if the ReceivedDebit was created due to a [Payout](object.md#payouts) object.

  - `linked_flows.topup` (string, nullable)
    Set if the ReceivedDebit was created due to a [Topup](object.md#topups) object.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `network` (enum)
  The network used for the ReceivedDebit.

- `reversal_details` (object, nullable)
  Details describing when a ReceivedDebit might be reversed.

  - `reversal_details.deadline` (timestamp, nullable)
    Time before which a ReceivedDebit can be reversed.

  - `reversal_details.restricted_reason` (enum, nullable)
    Set if a ReceivedDebit can’t be reversed.
Possible enum values:
    - `already_reversed`
      A ReceivedDebit that’s already reversed has this `restricted_reason`. It may have a `deadline` populated.

    - `deadline_passed`
      A ReceivedDebit that used to be reversible until the timestamp in `deadline`, but is no longer reversible. ACH ReceivedDebits are only reversible for some time after they’re created.

    - `network_restricted`
      Network constraints prevent Stripe from allowing reversal on some ReceivedDebits.

    - `other`
      A ReceivedDebit that was reversed because of another reason.

    - `source_flow_restricted`
      A ReceivedDebit that can’t be reversed because its `source_flow` is not reversible.

- `status` (enum)
  Status of the ReceivedDebit. ReceivedDebits are created with a status of either `succeeded` (approved) or `failed` (declined). The failure reason can be found under the `failure_code`.
Possible enum values:
  - `failed`
    The ReceivedDebit was declined, and no Transaction was created.

  - `succeeded`
    The ReceivedDebit was approved.

- `transaction` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The Transaction associated with this object.

### The ReceivedDebit object

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
