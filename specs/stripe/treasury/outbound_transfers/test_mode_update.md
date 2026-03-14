# Test mode: Update an OutboundTransfer

Updates a test mode created OutboundTransfer with tracking details. The OutboundTransfer must not be cancelable, and cannot be in the `canceled` or `failed` states.

## Returns

Returns the OutboundTransfer object with the updated tracking details. Returns an error if the OutboundTransfer is in an invalid state or if `tracking_details` has already been set.

## Parameters

- `tracking_details` (object, required)
  Details about network-specific tracking information.

  - `tracking_details.type` (enum, required)
    The US bank account network used to send funds.
Possible enum values:
    - `ach`
    - `us_domestic_wire`

  - `tracking_details.ach` (object, optional)
    ACH network tracking details.

    - `tracking_details.ach.trace_id` (string, required)
      ACH trace ID for funds sent over the `ach` network.

  - `tracking_details.us_domestic_wire` (object, optional)
    US domestic wire network tracking details.

    - `tracking_details.us_domestic_wire.chips` (string, optional)
      CHIPS System Sequence Number (SSN) for funds sent over the `us_domestic_wire` network.

    - `tracking_details.us_domestic_wire.imad` (string, optional)
      IMAD for funds sent over the `us_domestic_wire` network.

    - `tracking_details.us_domestic_wire.omad` (string, optional)
      OMAD for funds sent over the `us_domestic_wire` network.

```curl
curl https://api.stripe.com/v1/test_helpers/treasury/outbound_transfers/obt_1Mtaaz2eZvKYlo2CUu1tWGAl \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "tracking_details[type]"=ach \
  -d "tracking_details[ach][trace_id]"=841042400123450
```

### Response

```json
{
  "id": "obt_1Mtaaz2eZvKYlo2CUu1tWGAl",
  "object": "treasury.outbound_transfer",
  "amount": 10000,
  "cancelable": false,
  "created": 1680717489,
  "currency": "usd",
  "description": "OutboundTransfer to my external bank account",
  "destination_payment_method": "pm_1Mtaaz2eZvKYlo2C235TqrIn",
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
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYkJOwRj5U6NpOg9L70S_mhPE92VvJUt_P7rrE938uIHfjCSY3Bjn9Dufo8Z1h9709Gm-LmCbzT7a6j9kFN9w",
  "livemode": false,
  "metadata": {},
  "returned_details": null,
  "statement_descriptor": "transfer",
  "status": "posted",
  "status_transitions": {
    "posted_at": 1680717489,
    "failed_at": null,
    "canceled_at": null,
    "returned_at": null
  },
  "tracking_details": {
    "type": "ach",
    "ach": {
      "trace_id": "841042400123450"
    }
  },
  "transaction": "trxn_1Mtaaz2eZvKYlo2Cn9D12psR"
}
```
