# Create an OutboundTransfer

Creates an OutboundTransfer.

## Returns

Returns an OutboundTransfer object if there were no issues with OutboundTransfer creation. The status of the created OutboundTransfer object is initially marked as `processing`.

## Parameters

- `amount` (integer, required)
  Amount (in cents) to be transferred.

- `currency` (enum, required)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `financial_account` (string, required)
  The FinancialAccount to pull funds from.

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `destination_payment_method` (string, optional)
  The PaymentMethod to use as the payment instrument for the OutboundTransfer.

- `destination_payment_method_data` (object, optional)
  Hash used to generate the PaymentMethod to be used for this OutboundTransfer. Exclusive with `destination_payment_method`.

  - `destination_payment_method_data.type` (enum, required)
    The type of the destination.
Possible enum values:
    - `financial_account`

  - `destination_payment_method_data.financial_account` (string, optional)
    Required if type is set to `financial_account`. The FinancialAccount ID to send funds to.

- `destination_payment_method_options` (object, optional)
  Hash describing payment method configuration details.

  - `destination_payment_method_options.us_bank_account` (object, optional)
    Optional fields for `us_bank_account`.

    - `destination_payment_method_options.us_bank_account.network` (enum, optional)
      Specifies the network rails to be used. If not set, will default to the PaymentMethod’s preferred network. See the [docs](https://docs.stripe.com/docs/treasury/money-movement/timelines.md) to learn more about money movement timelines for each network type.
Possible enum values:
      - `ach`
        ACH network

      - `us_domestic_wire`
        US domestic wire network

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `statement_descriptor` (string, optional)
  Statement descriptor to be shown on the receiving end of an OutboundTransfer. Maximum 10 characters for `ach` transfers or 140 characters for `us_domestic_wire` transfers. The default value is “transfer”. Can only include -#.$&*, spaces, and alphanumeric characters.

```curl
curl https://api.stripe.com/v1/treasury/outbound_transfers \
  -u "<<YOUR_SECRET_KEY>>" \
  -d financial_account=fa_1Mtaaz2eZvKYlo2CUf56sIA1 \
  -d destination_payment_method=pm_1234567890 \
  -d amount=500 \
  -d currency=usd \
  -d description="OutboundTransfer to my external bank account"
```

### Response

```json
{
  "id": "obt_1Mtaaz2eZvKYlo2CUu1tWGAl",
  "object": "treasury.outbound_transfer",
  "amount": 500,
  "cancelable": true,
  "created": 1680717489,
  "currency": "usd",
  "description": "OutboundTransfer to my external bank account",
  "destination_payment_method": "pm_1234567890",
  "destination_payment_method_details": {
    "billing_details": {
      "address": {
        "city": "San Francisco",
        "country": "US",
        "line1": "1234 Fake Street",
        "line2": null,
        "postal_code": "94102",
        "state": "CA"
      },
      "email": null,
      "name": "Jane Austen"
    },
    "type": "us_bank_account",
    "us_bank_account": {
      "account_holder_type": "company",
      "account_type": "checking",
      "bank_name": "STRIPE TEST BANK",
      "fingerprint": "AP24Iso0btGp4N10",
      "last4": "6789",
      "network": "ach",
      "routing_number": "110000000"
    }
  },
  "expected_arrival_date": 1680825600,
  "financial_account": "fa_1Mtaaz2eZvKYlo2CUf56sIA1",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYCCwVOvUY6NpO8ArWrjrz6Hxk3d8tQ4d_RvOqMTOeq6js5eE94-f-7DwBzjjD1wxIUhOyub1KFYH8QKxj9oA",
  "livemode": false,
  "metadata": {},
  "returned_details": null,
  "statement_descriptor": "transfer",
  "status": "processing",
  "status_transitions": {
    "canceled_at": null,
    "failed_at": null,
    "posted_at": null,
    "returned_at": null
  },
  "transaction": "trxn_1Mtaaz2eZvKYlo2Cn9D12psR"
}
```
