# The Outbound Payment object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  Amount (in cents) transferred.

- `cancelable` (boolean)
  Returns `true` if the object can be canceled, and `false` otherwise.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `customer` (string, nullable)
  ID of the [customer](https://docs.stripe.com/docs/api/customers.md) to whom an OutboundPayment is sent.

- `description` (string, nullable)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `destination_payment_method` (string, nullable)
  The PaymentMethod via which an OutboundPayment is sent. This field can be empty if the OutboundPayment was created using `destination_payment_method_data`.

- `destination_payment_method_details` (object, nullable)
  Details about the PaymentMethod for an OutboundPayment.

  - `destination_payment_method_details.billing_details` (object)
    Contact details for the person or business receiving the OutboundPayment.

    - `destination_payment_method_details.billing_details.address` (object)
      Billing address.

      - `destination_payment_method_details.billing_details.address.city` (string, nullable)
        City, district, suburb, town, or village.

      - `destination_payment_method_details.billing_details.address.country` (string, nullable)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `destination_payment_method_details.billing_details.address.line1` (string, nullable)
        Address line 1, such as the street, PO Box, or company name.

      - `destination_payment_method_details.billing_details.address.line2` (string, nullable)
        Address line 2, such as the apartment, suite, unit, or building.

      - `destination_payment_method_details.billing_details.address.postal_code` (string, nullable)
        ZIP or postal code.

      - `destination_payment_method_details.billing_details.address.state` (string, nullable)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `destination_payment_method_details.billing_details.email` (string, nullable)
      Email address.

    - `destination_payment_method_details.billing_details.name` (string, nullable)
      Full name.

  - `destination_payment_method_details.financial_account` (object, nullable)
    Details about the `financial_account`.

    - `destination_payment_method_details.financial_account.id` (string)
      Token of the FinancialAccount.

    - `destination_payment_method_details.financial_account.network` (enum)
      The rails used to send funds.

  - `destination_payment_method_details.type` (enum)
    The type of the payment method used in the OutboundPayment.
Possible enum values:
    - `financial_account`
    - `us_bank_account`

  - `destination_payment_method_details.us_bank_account` (object, nullable)
    Details about the `us_bank_account`.

    - `destination_payment_method_details.us_bank_account.account_holder_type` (enum, nullable)
      Account holder type: individual or company.
Possible enum values:
      - `company`
        Account belongs to a company

      - `individual`
        Account belongs to an individual

    - `destination_payment_method_details.us_bank_account.account_type` (enum, nullable)
      Account type: checkings or savings. Defaults to checking if omitted.
Possible enum values:
      - `checking`
        Bank account type is checking

      - `savings`
        Bank account type is savings

    - `destination_payment_method_details.us_bank_account.bank_name` (string, nullable)
      Name of the bank associated with the bank account.

    - `destination_payment_method_details.us_bank_account.fingerprint` (string, nullable)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `destination_payment_method_details.us_bank_account.last4` (string, nullable)
      Last four digits of the bank account number.

    - `destination_payment_method_details.us_bank_account.mandate` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
      ID of the mandate used to make this payment.

    - `destination_payment_method_details.us_bank_account.network` (enum)
      The network rails used. See the [docs](https://docs.stripe.com/docs/treasury/money-movement/timelines.md) to learn more about money movement timelines for each network type.
Possible enum values:
      - `ach`
        ACH network

      - `us_domestic_wire`
        US domestic wire network

    - `destination_payment_method_details.us_bank_account.routing_number` (string, nullable)
      Routing number of the bank account.

- `end_user_details` (object, nullable)
  Details about the end user.

  - `end_user_details.ip_address` (string, nullable)
    IP address of the user initiating the OutboundPayment. Set if `present` is set to `true`. IP address collection is required for risk and compliance reasons. This will be used to help determine if the OutboundPayment is authorized or should be blocked.

  - `end_user_details.present` (boolean)
    `true` if the OutboundPayment creation request is being made on behalf of an end user by a platform. Otherwise, `false`.

- `expected_arrival_date` (timestamp)
  The date when funds are expected to arrive in the destination account.

- `financial_account` (string)
  The FinancialAccount that funds were pulled from.

- `hosted_regulatory_receipt_url` (string, nullable)
  A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `returned_details` (object, nullable)
  Details about a returned OutboundPayment. Only set when the status is `returned`.

  - `returned_details.code` (enum)
    Reason for the return.
Possible enum values:
    - `account_closed`
      The destination has been closed.

    - `account_frozen`
      The destination has been frozen.

    - `bank_account_restricted`
      The destination bank account has restrictions on either the type or number of transfers allowed. This normally indicates that the bank account is a savings or other non-checking account.

    - `bank_ownership_changed`
      The destination bank account is no longer valid because its branch has changed ownership.

    - `declined`
      The destination has declined this OutboundPayment.

    - `incorrect_account_holder_name`
      The destination bank notified us that the bank account holder name on file is incorrect.

    - `invalid_account_number`
      The destination bank account details on file are probably incorrect. The routing number seems correct, but the account number is invalid.

    - `invalid_currency`
      The destination was unable to process this OutboundPayment because of its currency.

    - `no_account`
      The destination bank account details on file are probably incorrect. No bank account exists with these details.

    - `other`
      The destination could not process this OutboundPayment.

  - `returned_details.transaction` (string, expandable (can be expanded into an object with the `expand` request parameter))
    The Transaction associated with this object.

- `statement_descriptor` (string)
  The description that appears on the receiving end for an OutboundPayment (for example, bank statement for external bank transfer).

- `status` (enum)
  Current status of the OutboundPayment: `processing`, `failed`, `posted`, `returned`, `canceled`. An OutboundPayment is `processing` if it has been created and is pending. The status changes to `posted` once the OutboundPayment has been “confirmed” and funds have left the account, or to `failed` or `canceled`. If an OutboundPayment fails to arrive at its destination, its status will change to `returned`.

- `status_transitions` (object)
  Hash containing timestamps of when the object transitioned to a particular `status`.

  - `status_transitions.canceled_at` (timestamp, nullable)
    Timestamp describing when an OutboundPayment changed status to `canceled`.

  - `status_transitions.failed_at` (timestamp, nullable)
    Timestamp describing when an OutboundPayment changed status to `failed`.

  - `status_transitions.posted_at` (timestamp, nullable)
    Timestamp describing when an OutboundPayment changed status to `posted`.

  - `status_transitions.returned_at` (timestamp, nullable)
    Timestamp describing when an OutboundPayment changed status to `returned`.

- `tracking_details` (object, nullable)
  Details about network-specific tracking information if available.

  - `tracking_details.ach` (object, nullable)
    ACH network tracking details.

    - `tracking_details.ach.trace_id` (string)
      ACH trace ID of the OutboundPayment for payments sent over the `ach` network.

  - `tracking_details.type` (enum)
    The US bank account network used to send funds.
Possible enum values:
    - `ach`
    - `us_domestic_wire`

  - `tracking_details.us_domestic_wire` (object, nullable)
    US domestic wire network tracking details.

    - `tracking_details.us_domestic_wire.chips` (string, nullable)
      CHIPS System Sequence Number (SSN) of the OutboundPayment for payments sent over the `us_domestic_wire` network.

    - `tracking_details.us_domestic_wire.imad` (string, nullable)
      IMAD of the OutboundPayment for payments sent over the `us_domestic_wire` network.

    - `tracking_details.us_domestic_wire.omad` (string, nullable)
      OMAD of the OutboundPayment for payments sent over the `us_domestic_wire` network.

- `transaction` (string, expandable (can be expanded into an object with the `expand` request parameter))
  The Transaction associated with this object.

### The Outbound Payment object

```json
{
  "id": "obp_1MtaD72eZvKYlo2Cu5d5S1kX",
  "object": "treasury.outbound_payment",
  "amount": 10000,
  "cancelable": false,
  "created": 1680716009,
  "currency": "usd",
  "customer": "cus_4QFOF3xrvBT2nU",
  "description": "OutboundPayment to a 3rd party",
  "destination_payment_method": "pm_1MtaD82eZvKYlo2CtGr4OxTt",
  "destination_payment_method_details": {
    "type": "us_bank_account",
    "destination": "ba_1MtaD62eZvKYlo2C8vwjm7bc"
  },
  "end_user_details": {
    "ip_address": null,
    "present": false
  },
  "expected_arrival_date": 1680716009,
  "financial_account": "fa_1MtaD72eZvKYlo2CYKM3DnUI",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgYgdA-GrKk6NZNsf-FXPEqqbHm44fwJ57pNybbkweviYUDJGYFOw4f9cAqpfvPKQZ6y0S2C5DYyRwmDs_36",
  "livemode": false,
  "metadata": {},
  "returned_details": null,
  "statement_descriptor": "payment",
  "status": "processing",
  "status_transitions": {
    "canceled_at": null,
    "failed_at": null,
    "posted_at": null,
    "returned_at": null
  },
  "transaction": "trxn_1MtaD72eZvKYlo2CmUu4Vs5c"
}
```
