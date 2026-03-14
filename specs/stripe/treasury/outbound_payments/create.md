# Create an OutboundPayment

Creates an OutboundPayment.

## Returns

Returns an OutboundPayment object if there were no issues with OutboundPayment creation.

## Parameters

- `amount` (integer, required)
  Amount (in cents) to be transferred.

- `currency` (enum, required)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `financial_account` (string, required)
  The FinancialAccount to pull funds from.

- `customer` (string, optional)
  ID of the customer to whom the OutboundPayment is sent. Must match the Customer attached to the `destination_payment_method` passed in.

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `destination_payment_method` (string, optional)
  The PaymentMethod to use as the payment instrument for the OutboundPayment. Exclusive with `destination_payment_method_data`.

- `destination_payment_method_data` (object, optional)
  Hash used to generate the PaymentMethod to be used for this OutboundPayment. Exclusive with `destination_payment_method`.

  - `destination_payment_method_data.type` (enum, required)
    The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
Possible enum values:
    - `financial_account`
    - `us_bank_account`

  - `destination_payment_method_data.billing_details` (object, optional)
    Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.

    - `destination_payment_method_data.billing_details.address` (object, optional)
      Billing address.

      - `destination_payment_method_data.billing_details.address.city` (string, optional)
        City, district, suburb, town, or village.

      - `destination_payment_method_data.billing_details.address.country` (string, optional)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `destination_payment_method_data.billing_details.address.line1` (string, optional)
        Address line 1, such as the street, PO Box, or company name.

      - `destination_payment_method_data.billing_details.address.line2` (string, optional)
        Address line 2, such as the apartment, suite, unit, or building.

      - `destination_payment_method_data.billing_details.address.postal_code` (string, optional)
        ZIP or postal code.

      - `destination_payment_method_data.billing_details.address.state` (string, optional)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `destination_payment_method_data.billing_details.email` (string, optional)
      Email address.

      The maximum length is 800 characters.

    - `destination_payment_method_data.billing_details.name` (string, optional)
      Full name.

    - `destination_payment_method_data.billing_details.phone` (string, optional)
      Billing phone number (including extension).

  - `destination_payment_method_data.financial_account` (string, optional)
    Required if type is set to `financial_account`. The FinancialAccount ID to send funds to.

  - `destination_payment_method_data.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

  - `destination_payment_method_data.us_bank_account` (object, optional)
    Required hash if type is set to `us_bank_account`.

    - `destination_payment_method_data.us_bank_account.account_holder_type` (enum, optional)
      Account holder type: individual or company.
Possible enum values:
      - `company`
        Account belongs to a company

      - `individual`
        Account belongs to an individual

    - `destination_payment_method_data.us_bank_account.account_number` (string, optional)
      Account number of the bank account.

    - `destination_payment_method_data.us_bank_account.account_type` (enum, optional)
      Account type: checkings or savings. Defaults to checking if omitted.
Possible enum values:
      - `checking`
        Bank account type is checking

      - `savings`
        Bank account type is savings

    - `destination_payment_method_data.us_bank_account.financial_connections_account` (string, optional)
      The ID of a Financial Connections Account to use as a payment method.

    - `destination_payment_method_data.us_bank_account.routing_number` (string, optional)
      Routing number of the bank account.

- `destination_payment_method_options` (object, optional)
  Payment method-specific configuration for this OutboundPayment.

  - `destination_payment_method_options.us_bank_account` (object, optional)
    Optional fields for `us_bank_account`.

    - `destination_payment_method_options.us_bank_account.network` (enum, optional)
      Specifies the network rails to be used. If not set, will default to the PaymentMethod’s preferred network. See the [docs](https://docs.stripe.com/docs/treasury/money-movement/timelines.md) to learn more about money movement timelines for each network type.
Possible enum values:
      - `ach`
        ACH network

      - `us_domestic_wire`
        US domestic wire network

- `end_user_details` (object, optional)
  End user details.

  - `end_user_details.present` (boolean, required)
    `True` if the OutboundPayment creation request is being made on behalf of an end user by a platform. Otherwise, `false`.

  - `end_user_details.ip_address` (string, optional)
    IP address of the user initiating the OutboundPayment. Must be supplied if `present` is set to `true`.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `statement_descriptor` (string, optional)
  The description that appears on the receiving end for this OutboundPayment (for example, bank statement for external bank transfer). Maximum 10 characters for `ach` payments, 140 characters for `us_domestic_wire` payments, or 500 characters for `stripe` network transfers. Can only include -#.$&*, spaces, and alphanumeric characters. The default value is “payment”.

```curl
curl https://api.stripe.com/v1/treasury/outbound_payments \
  -u "<<YOUR_SECRET_KEY>>" \
  -d financial_account=fa_1MtaD72eZvKYlo2CYKM3DnUI \
  -d amount=10000 \
  -d currency=usd \
  -d customer=cus_4QFOF3xrvBT2nU \
  -d destination_payment_method=pm_1MtaD82eZvKYlo2Cn1XtS23o \
  -d description="OutboundPayment to a 3rd party"
```

### Response

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
